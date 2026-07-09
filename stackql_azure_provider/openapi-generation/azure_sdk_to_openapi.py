"""Generate per-service OpenAPI specs from the in-tree azure-sdk-for-python checkout.

Output layout: <out_dir>/<service_alias>.yaml

Stage 1 of the two-stage stackql provider build (mirrors the botocore-derived
AWS provider pipeline in ref/stackql-provider-aws). Instead of botocore's
service-2.json data files, the Azure SDK ships *generated Python code*; the
request builders (`build_*_request` functions), operation-group classes and
model classes are all mechanically generated (typespec-python or
autorest.python) and therefore statically parseable with `ast`.

Per SDK package we extract:
  - every `build_<group>_<method>_request` function: URL template, HTTP verb,
    api-version default, path/query/header parameters (+ serializer types)
  - every operation-group class method: docstring, body model, return type
    (ItemPaged -> paged list, LROPoller -> long-running op, plain model, None)
  - the model index (typespec `rest_field` and msrest `_attribute_map` styles)
    resolved transitively into OpenAPI schemas (wire-named properties)

Every emitted operation is stamped with `x-stackql-*` breadcrumbs that stage 2
(provider-dev/scripts/generate-provider.mjs) folds into
`components/x-stackQL-resources`.

Design rules carried over from the AWS provider (see CLAUDE.md):
  - no polymorphism in output ($ref only - no allOf/oneOf/anyOf,
    no additionalProperties; maps become {type: object, properties: {}})
  - YAML 1.1 bool keywords quoted
  - descriptions cleaned for MDX (docusaurus)
  - path params snake_cased in the path template + parameter names (path
    params have no wire meaning; query/header/body params keep the native
    camelCase wire names - the stackql casing engine renders snake aliases)
  - api-version baked into the OpenAPI path key (`...?api-version=2024-01-01`)
    exactly like the original AutoRest-based azure provider
"""

from __future__ import annotations

import argparse
import ast
import html
import re
import sys
import warnings

# generated SDK docstrings contain sequences like "\ " that raise
# SyntaxWarning under ast.parse on py3.12+ - harmless here
warnings.filterwarnings("ignore", category=SyntaxWarning)
from collections import OrderedDict
from pathlib import Path
from typing import Any, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
SDK_ROOT = REPO_ROOT / "sdk"

import yaml  # noqa: E402


# --------------------------------------------------------------------------- #
# description cleaning (same MDX-safety rules as the AWS provider)
# --------------------------------------------------------------------------- #

_ANY_TAG = re.compile(r"</?[a-zA-Z][^>]*>")
_PLACEHOLDER = re.compile(r"<([A-Za-z][A-Za-z0-9_\-:.]*)>")
_SPHINX_ROLE = re.compile(r":[a-z]+:`~?([^`]*)`")
_CODE_REF = re.compile(r"``([^`]*)``")
# markdown links with relative targets ("[X](./GetApplicationInfo.md)") point
# at SDK-internal docs that don't exist on the docs site; keep the link text
_RELATIVE_MD_LINK = re.compile(r"\[([^\]]*)\]\((?!https?://)[^)]*\)")


def clean_description(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    s = text
    # Sphinx roles (:class:`~azure...X`) -> just the target text.
    s = _SPHINX_ROLE.sub(r"\1", s)
    # RST double-backtick literals -> single backtick.
    s = _CODE_REF.sub(r"`\1`", s)
    # relative markdown links -> bare link text.
    s = _RELATIVE_MD_LINK.sub(r"\1", s)
    # Drop any HTML tags, decode entities.
    s = _ANY_TAG.sub("", s)
    s = html.unescape(s)
    # Backtick bare `<placeholder>` so MDX doesn't read it as JSX.
    s = _PLACEHOLDER.sub(r"`<\1>`", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s or None


def doc_summary(docstring: Optional[str]) -> Optional[str]:
    """First paragraph of a method docstring, up to the field list."""
    if not docstring:
        return None
    lines = []
    for line in docstring.splitlines():
        if re.match(r"\s*:(param|keyword|type|paramtype|return|returns|rtype|raises|ivar|vartype)", line):
            break
        lines.append(line)
    return clean_description(" ".join(lines))


def parse_docstring_params(docstring: Optional[str]) -> dict[str, str]:
    """Map of param-name -> description from :param x:/:keyword x: entries."""
    out: dict[str, str] = {}
    if not docstring:
        return out
    for m in re.finditer(
        r":(?:param|keyword)\s+(\w+):\s*(.*?)(?=\n\s*:|\Z)", docstring, re.DOTALL
    ):
        desc = clean_description(m.group(2))
        if desc:
            out[m.group(1)] = desc
    return out


# --------------------------------------------------------------------------- #
# YAML output (YAML 1.1 bool-keyword quoting, no anchors)
# --------------------------------------------------------------------------- #

_YAML_1_1_BOOL_KEYWORDS = {
    "y", "Y", "yes", "Yes", "YES",
    "n", "N", "no", "No", "NO",
    "true", "True", "TRUE",
    "false", "False", "FALSE",
    "on", "On", "ON",
    "off", "Off", "OFF",
}


def ordered_yaml_dump(data: Any, stream) -> None:
    class _Dumper(yaml.SafeDumper):
        def ignore_aliases(self, data):
            return True

    def _dict_repr(dumper, value):
        return dumper.represent_mapping("tag:yaml.org,2002:map", value.items())

    def _str_repr(dumper, value):
        if value in _YAML_1_1_BOOL_KEYWORDS:
            return dumper.represent_scalar("tag:yaml.org,2002:str", value, style="'")
        return dumper.represent_scalar("tag:yaml.org,2002:str", value)

    _Dumper.add_representer(OrderedDict, _dict_repr)
    _Dumper.add_representer(dict, _dict_repr)
    _Dumper.add_representer(str, _str_repr)
    yaml.dump(data, stream, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=110)


# --------------------------------------------------------------------------- #
# casing helpers
# --------------------------------------------------------------------------- #


def to_snake(s: str) -> str:
    s = s.replace("-", "_")
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"__+", "_", s)
    return s.lower()


def pluralise(noun: str) -> str:
    if noun.endswith("s"):
        return noun
    if noun.endswith("y") and len(noun) > 1 and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    if noun.endswith(("ch", "sh", "x", "z")):
        return noun + "es"
    return noun + "s"


# --------------------------------------------------------------------------- #
# serializer type-string -> OpenAPI schema
# --------------------------------------------------------------------------- #

SERIALIZER_TYPE_MAP = {
    "str": {"type": "string"},
    "int": {"type": "integer"},
    "long": {"type": "integer", "format": "int64"},
    "float": {"type": "number"},
    "bool": {"type": "boolean"},
    "iso-8601": {"type": "string", "format": "date-time"},
    "rfc-1123": {"type": "string"},
    "unix-time": {"type": "integer"},
    "duration": {"type": "string"},
    "date": {"type": "string", "format": "date"},
    "time": {"type": "string"},
    "decimal": {"type": "number"},
    "bytearray": {"type": "string", "format": "byte"},
    "base64": {"type": "string", "format": "byte"},
    "object": {"type": "object", "properties": {}},
}


def serializer_type_to_schema(tstr: str) -> dict:
    tstr = (tstr or "str").strip()
    if tstr.startswith("[") and tstr.endswith("]"):
        return {"type": "array", "items": serializer_type_to_schema(tstr[1:-1])}
    if tstr.startswith("{") and tstr.endswith("}"):
        return {"type": "object", "properties": {}}
    return dict(SERIALIZER_TYPE_MAP.get(tstr, {"type": "string"}))


# --------------------------------------------------------------------------- #
# model index: typespec (rest_field) + msrest (_attribute_map) styles
# --------------------------------------------------------------------------- #


class ModelField:
    __slots__ = ("attr", "wire", "annotation", "description", "readonly", "required")

    def __init__(self, attr, wire, annotation, description=None, readonly=False, required=False):
        self.attr = attr
        self.wire = wire
        self.annotation = annotation  # string form
        self.description = description
        self.readonly = readonly
        self.required = required


class ModelDef:
    __slots__ = ("name", "bases", "fields", "doc")

    def __init__(self, name, bases, doc=None):
        self.name = name
        self.bases = bases
        self.fields: "OrderedDict[str, ModelField]" = OrderedDict()
        self.doc = doc


# msrest _attribute_map type strings -> annotation-ish strings we can reuse
_MSREST_SCALARS = set(SERIALIZER_TYPE_MAP.keys())


def _parse_ivar_docs(docstring: Optional[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    if not docstring:
        return out
    for m in re.finditer(r":ivar\s+(\w+):\s*(.*?)(?=\n\s*:|\Z)", docstring, re.DOTALL):
        desc = clean_description(m.group(2))
        if desc:
            out[m.group(1)] = desc
    return out


class ModelIndex:
    """Parses model modules for one SDK package and lazily converts models
    (and enums) to OpenAPI schemas following the no-polymorphism rules."""

    def __init__(self):
        self.models: dict[str, ModelDef] = {}
        self.enums: dict[str, list] = {}
        self.emitted: "OrderedDict[str, dict]" = OrderedDict()
        self._in_progress: set[str] = set()

    # ---------- parsing ----------

    def add_module(self, path: Path) -> None:
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            return
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            base_names = [ast.unparse(b) for b in node.bases]
            if any("Enum" in b for b in base_names):
                values = []
                for stmt in node.body:
                    if isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.Constant):
                        if isinstance(stmt.value.value, str):
                            values.append(stmt.value.value)
                if values:
                    self.enums[node.name] = values
                continue
            self._add_model_class(node, base_names)

    def _add_model_class(self, node: ast.ClassDef, base_names: list[str]) -> None:
        doc = ast.get_docstring(node)
        model = ModelDef(node.name, base_names, doc=doc_summary(doc))
        ivar_docs = _parse_ivar_docs(doc)

        # --- typespec style: annotated class attrs with rest_field(...) ---
        prev_field: Optional[ModelField] = None
        for stmt in node.body:
            if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                attr = stmt.target.id
                if attr.startswith("_"):
                    prev_field = None
                    continue
                ann = ast.unparse(stmt.annotation)
                wire = attr
                readonly = False
                if isinstance(stmt.value, ast.Call):
                    fn = ast.unparse(stmt.value.func)
                    if "rest_field" in fn or "rest_discriminator" in fn:
                        for kw in stmt.value.keywords:
                            if kw.arg == "name" and isinstance(kw.value, ast.Constant):
                                wire = kw.value.value
                            if kw.arg == "visibility":
                                try:
                                    vis = [
                                        e.value
                                        for e in kw.value.elts  # type: ignore[attr-defined]
                                        if isinstance(e, ast.Constant)
                                    ]
                                    readonly = vis == ["read"]
                                except AttributeError:
                                    pass
                required = not ann.startswith("Optional[") and "None" not in ann
                f = ModelField(attr, wire, ann, ivar_docs.get(attr), readonly, required)
                model.fields[attr] = f
                prev_field = f
                continue
            # a bare string Expr right after a field is its docstring
            if (
                prev_field is not None
                and isinstance(stmt, ast.Expr)
                and isinstance(stmt.value, ast.Constant)
                and isinstance(stmt.value.value, str)
            ):
                if not prev_field.description:
                    prev_field.description = clean_description(stmt.value.value)
                prev_field = None
                continue
            prev_field = None

        # --- msrest style: _attribute_map / _validation dict literals ---
        validation: dict[str, dict] = {}
        for stmt in node.body:
            if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
                tname = getattr(stmt.targets[0], "id", None)
                if tname == "_validation" and isinstance(stmt.value, ast.Dict):
                    for k, v in zip(stmt.value.keys, stmt.value.values):
                        if isinstance(k, ast.Constant) and isinstance(v, ast.Dict):
                            flags = {}
                            for fk, fv in zip(v.keys, v.values):
                                if isinstance(fk, ast.Constant) and isinstance(fv, ast.Constant):
                                    flags[fk.value] = fv.value
                            validation[k.value] = flags
        for stmt in node.body:
            if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
                tname = getattr(stmt.targets[0], "id", None)
                if tname == "_attribute_map" and isinstance(stmt.value, ast.Dict):
                    for k, v in zip(stmt.value.keys, stmt.value.values):
                        if not (isinstance(k, ast.Constant) and isinstance(v, ast.Dict)):
                            continue
                        attr = k.value
                        wire, tstr = attr, "object"
                        for fk, fv in zip(v.keys, v.values):
                            if isinstance(fk, ast.Constant) and isinstance(fv, ast.Constant):
                                if fk.value == "key":
                                    wire = fv.value
                                elif fk.value == "type":
                                    tstr = fv.value
                        flags = validation.get(attr, {})
                        # msrest client-side flattening: dotted keys
                        # ("properties.provisioningState") describe the NESTED
                        # wire structure. Keep the dotted path; schema assembly
                        # rebuilds the nesting (and the ARM properties hoist
                        # picks the leaves up from there).
                        model.fields[attr] = ModelField(
                            attr, wire, f"msrest:{tstr}", ivar_docs.get(attr),
                            bool(flags.get("readonly")), bool(flags.get("required")),
                        )

        if model.fields or base_names:
            self.models[node.name] = model

    # ---------- schema emission ----------

    def _merged_fields(self, name: str, _seen=None) -> "OrderedDict[str, ModelField]":
        _seen = _seen or set()
        if name in _seen or name not in self.models:
            return OrderedDict()
        _seen.add(name)
        model = self.models[name]
        merged: "OrderedDict[str, ModelField]" = OrderedDict()
        for base in model.bases:
            base_name = base.split(".")[-1].strip("\"'")
            if base_name in self.models:
                merged.update(self._merged_fields(base_name, _seen))
        merged.update(model.fields)
        return merged

    def ref(self, name: str) -> dict:
        """Return a $ref to the named model/enum, emitting it on first use."""
        if name in self.enums:
            if name not in self.emitted:
                self.emitted[name] = {"type": "string", "enum": list(self.enums[name])}
            return {"$ref": f"#/components/schemas/{name}"}
        if name not in self.models:
            return {"type": "object", "properties": {}}
        if name not in self.emitted:
            self.emitted[name] = {}  # recursion guard stub
            self.emitted[name] = self._convert_model(name)
        return {"$ref": f"#/components/schemas/{name}"}

    def assemble_props(self, fields, writable_only: bool = False):
        """(properties, required) with msrest dotted wire paths rebuilt into
        nested objects (`properties.provisioningState` nests under a
        `properties` object, matching the wire shape)."""
        props: "OrderedDict[str, Any]" = OrderedDict()
        required: list[str] = []
        for f in fields.values():
            if writable_only and f.readonly:
                continue
            wire = str(f.wire)
            schema = self.annotation_to_schema(f.annotation)
            if f.description:
                schema = {**schema, "description": f.description}
            if "." not in wire:
                key = _safe_property_name(wire)
                props[key] = schema
                if f.required and not (writable_only is False and f.readonly):
                    required.append(key)
                continue
            # dotted path: descend/create inline objects
            parts = [_safe_property_name(p) for p in wire.split(".")]
            node = props
            ok = True
            for seg in parts[:-1]:
                child = node.get(seg)
                if child is None or not isinstance(child, dict) or "$ref" in child:
                    child = {"type": "object", "properties": OrderedDict()}
                    node[seg] = child
                child.setdefault("properties", OrderedDict())
                node = child["properties"]
                if not isinstance(node, dict):
                    ok = False
                    break
            if ok:
                node[parts[-1]] = schema
                if f.required and parts[0] not in required:
                    required.append(parts[0])
        return props, required

    def _convert_model(self, name: str) -> dict:
        model = self.models[name]
        out: dict = {"type": "object"}
        if model.doc:
            out["description"] = model.doc
        props, required = self.assemble_props(self._merged_fields(name))
        out["properties"] = props
        # `required` here reflects request semantics; keep response schema
        # permissive (stackql column inference ignores required anyway)
        if required:
            out["required"] = required
        return out

    def body_schema(self, name: str) -> Optional[dict]:
        """Inline top-level schema for a request body model: writable fields
        only, with `required` populated - inlined (not $ref'd) so stackql's
        required-param scan reaches the required list directly."""
        if name not in self.models:
            return None
        props, required = self.assemble_props(self._merged_fields(name), writable_only=True)
        if not props:
            return None
        out: dict = {"type": "object", "properties": props}
        if required:
            out["required"] = required
        return out

    # ---------- annotation conversion ----------

    def annotation_to_schema(self, ann: Optional[str]) -> dict:
        if not ann:
            return {"type": "object", "properties": {}}
        ann = ann.strip()

        if ann.startswith("msrest:"):
            return self._msrest_type_to_schema(ann[len("msrest:"):])

        # strip Optional/quotes
        m = re.match(r"^Optional\[(.*)\]$", ann)
        if m:
            return self.annotation_to_schema(m.group(1))
        ann = ann.strip("\"'")

        # Union[str, _models.SomeEnum] (extensible enums) and general unions:
        # prefer a _models member, else the first alternative.
        m = re.match(r"^Union\[(.*)\]$", ann)
        if m:
            alts = _split_top_level(m.group(1))
            model_alt = next((a for a in alts if "_models." in a), None)
            pick = model_alt or alts[0]
            if pick.strip() == "None" and len(alts) > 1:
                pick = alts[0]
            return self.annotation_to_schema(pick)

        m = re.match(r"^(?:typing\.)?(?:List|list|Sequence|Iterable)\[(.*)\]$", ann)
        if m:
            return {"type": "array", "items": self.annotation_to_schema(m.group(1))}

        m = re.match(r"^(?:typing\.)?(?:Dict|dict|Mapping|MutableMapping)\[(.*)\]$", ann)
        if m:
            return {"type": "object", "properties": {}}

        m = re.match(r"^_models\.(\w+)$", ann)
        if m:
            return self.ref(m.group(1))
        # bare model name (quoted forward ref without _models prefix)
        if ann in self.models or ann in self.enums:
            return self.ref(ann)

        base = ann.split(".")[-1]
        simple = {
            "str": {"type": "string"},
            "int": {"type": "integer"},
            "float": {"type": "number"},
            "bool": {"type": "boolean"},
            "bytes": {"type": "string", "format": "byte"},
            "datetime": {"type": "string", "format": "date-time"},
            "date": {"type": "string", "format": "date"},
            "time": {"type": "string"},
            "timedelta": {"type": "string"},
            "Decimal": {"type": "number"},
            "Any": {"type": "object", "properties": {}},
            "JSON": {"type": "object", "properties": {}},
            "object": {"type": "object", "properties": {}},
        }
        if base in simple:
            return dict(simple[base])
        if ann.startswith("Literal["):
            return {"type": "string"}
        return {"type": "object", "properties": {}}

    def _msrest_type_to_schema(self, tstr: str) -> dict:
        tstr = tstr.strip()
        if tstr.startswith("[") and tstr.endswith("]"):
            return {"type": "array", "items": self._msrest_type_to_schema(tstr[1:-1])}
        if tstr.startswith("{") and tstr.endswith("}"):
            return {"type": "object", "properties": {}}
        if tstr in _MSREST_SCALARS:
            return serializer_type_to_schema(tstr)
        if tstr in self.models or tstr in self.enums:
            return self.ref(tstr)
        return {"type": "object", "properties": {}}


def _split_top_level(s: str) -> list[str]:
    """Split 'a, b[c, d], e' on top-level commas."""
    parts, depth, cur = [], 0, []
    for ch in s:
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur:
        parts.append("".join(cur).strip())
    return parts


# OpenAPI keywords that collide as property names (same rule as AWS - see
# CLAUDE.md rule "reserved property names"). Renamed with trailing underscore.
OPENAPI_RESERVED_PROPERTY_NAMES = {
    "items", "type", "properties", "required", "enum", "format", "default",
    "oneOf", "anyOf", "allOf", "not", "additionalProperties", "discriminator",
}
# `type` and `properties` are ubiquitous legitimate ARM wire names - stackql
# handles them fine as property names in practice (the original azure provider
# shipped them for years). Only `items` trips the introspector.
OPENAPI_RESERVED_PROPERTY_NAMES = {"items"}


def _safe_property_name(name: str) -> str:
    if name in OPENAPI_RESERVED_PROPERTY_NAMES:
        return name + "_"
    return name


# --------------------------------------------------------------------------- #
# build_*_request function parsing
# --------------------------------------------------------------------------- #


class BuildFn:
    __slots__ = (
        "name", "url", "http_method", "api_version", "params", "has_body_content",
    )

    def __init__(self, name):
        self.name = name
        self.url: Optional[str] = None
        self.http_method: str = "get"
        self.api_version: Optional[str] = None
        # list of dicts: {py, wire, in, required, schema}
        self.params: list[dict] = []
        self.has_body_content = False


def parse_build_fn(fn: ast.FunctionDef) -> Optional[BuildFn]:
    bf = BuildFn(fn.name)

    # ----- signature: required/optional by python convention -----
    pos_args = [a.arg for a in fn.args.posonlyargs + fn.args.args]
    kw_args = [a.arg for a in fn.args.kwonlyargs]
    kw_defaults = {}
    for a, d in zip(fn.args.kwonlyargs, fn.args.kw_defaults):
        kw_defaults[a.arg] = d  # None means no default -> required
    required_py = set(pos_args) | {k for k in kw_args if kw_defaults.get(k) is None}

    wire_map: dict[str, dict] = {}  # py name -> {wire, in, tstr}

    for node in ast.walk(fn):
        # _url = "..."  |  _url = kwargs.pop("template_url", "...")
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            t = node.targets[0]
            if isinstance(t, ast.Name) and t.id == "_url" and bf.url is None:
                if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                    bf.url = node.value.value
                elif (
                    isinstance(node.value, ast.Call)
                    and getattr(node.value.func, "attr", "") == "pop"
                    and len(node.value.args) == 2
                    and isinstance(node.value.args[1], ast.Constant)
                ):
                    bf.url = node.value.args[1].value
            # path_format_arguments = { "wireName": _SERIALIZER.url("py_name", ...) }
            if isinstance(t, ast.Name) and t.id == "path_format_arguments" and isinstance(node.value, ast.Dict):
                for k, v in zip(node.value.keys, node.value.values):
                    if not isinstance(k, ast.Constant):
                        continue
                    if isinstance(v, ast.Call) and v.args and isinstance(v.args[0], ast.Constant):
                        py = str(v.args[0].value).replace("self._config.", "")
                        tstr = v.args[2].value if len(v.args) > 2 and isinstance(v.args[2], ast.Constant) else "str"
                        wire_map[py] = {"wire": k.value, "in": "path", "tstr": tstr}
            # _params["api-version"] / _params["$expand"] = _SERIALIZER.query("expand", expand, "str")
            if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name):
                target_name = t.value.id
                key = None
                if isinstance(t.slice, ast.Constant):
                    key = t.slice.value
                if key is None:
                    continue
                if target_name in ("_params", "_query_parameters") and isinstance(node.value, ast.Call):
                    call = node.value
                    if (
                        getattr(call.func, "attr", "") == "query"
                        and call.args
                        and isinstance(call.args[0], ast.Constant)
                    ):
                        py = str(call.args[0].value)
                        tstr = call.args[2].value if len(call.args) > 2 and isinstance(call.args[2], ast.Constant) else "str"
                        if key != "api-version":
                            wire_map.setdefault(py, {"wire": key, "in": "query", "tstr": tstr})
                if target_name in ("_headers", "_header_parameters") and isinstance(node.value, ast.Call):
                    call = node.value
                    if (
                        getattr(call.func, "attr", "") == "header"
                        and call.args
                        and isinstance(call.args[0], ast.Constant)
                    ):
                        py = str(call.args[0].value)
                        tstr = call.args[2].value if len(call.args) > 2 and isinstance(call.args[2], ast.Constant) else "str"
                        if py not in ("accept", "content_type"):
                            wire_map.setdefault(py, {"wire": key, "in": "header", "tstr": tstr})
        # api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-01-01"))
        if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "pop":
            if (
                node.args
                and isinstance(node.args[0], ast.Constant)
                and node.args[0].value == "api-version"
                and len(node.args) > 1
                and isinstance(node.args[1], ast.Constant)
            ):
                bf.api_version = str(node.args[1].value)
        # return HttpRequest(method="GET", ...)
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "HttpRequest":
            for kw in node.keywords:
                if kw.arg == "method" and isinstance(kw.value, ast.Constant):
                    bf.http_method = str(kw.value.value).lower()
                if kw.arg in ("content", "json"):
                    bf.has_body_content = True

    if not bf.url:
        return None

    # assemble parameter list in signature order (positional first)
    for py in pos_args + kw_args:
        if py in ("kwargs", "args"):
            continue
        info = wire_map.get(py)
        if not info:
            continue  # e.g. etag/match_condition handled via prep_if_match
        bf.params.append(
            {
                "py": py,
                "wire": info["wire"],
                "in": info["in"],
                "required": py in required_py or info["in"] == "path",
                "schema": serializer_type_to_schema(info["tstr"]),
            }
        )
    # subscription_id is normally passed from client config, not the
    # signature; make sure it's present if the URL references it.
    if "subscription_id" in wire_map and not any(p["py"] == "subscription_id" for p in bf.params):
        info = wire_map["subscription_id"]
        bf.params.append(
            {
                "py": "subscription_id",
                "wire": info["wire"],
                "in": info["in"],
                "required": True,
                "schema": serializer_type_to_schema(info["tstr"]),
            }
        )
    return bf


# --------------------------------------------------------------------------- #
# operation-group class parsing
# --------------------------------------------------------------------------- #


class OpMethod:
    __slots__ = (
        "group", "name", "build_fn_name", "docstring", "body_model",
        "return_ann", "paged_key", "is_lro", "src_order", "bf",
    )

    def __init__(self, group, name):
        self.group = group
        self.name = name
        self.build_fn_name: Optional[str] = None
        self.docstring: Optional[str] = None
        self.body_model: Optional[str] = None
        self.return_ann: Optional[str] = None
        self.paged_key: Optional[str] = None
        self.is_lro = False
        self.src_order = 0
        self.bf: Optional["BuildFn"] = None  # module-scoped builder


_MODELS_RE = re.compile(r"_models\.(\w+)")


def _find_build_call(fn: ast.FunctionDef) -> Optional[str]:
    for node in ast.walk(fn):
        if isinstance(node, ast.Call):
            fname = getattr(node.func, "id", None)
            if fname and fname.startswith("build_") and fname.endswith("_request"):
                return fname
    return None


def _find_initial_call(fn: ast.FunctionDef) -> Optional[str]:
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                if node.func.attr.startswith("_") and node.func.attr.endswith("_initial"):
                    return node.func.attr
    return None


_PAGING_LINK_KEYS = re.compile(r"next|skip|continuation|@odata", re.IGNORECASE)


def _find_paged_key(fn: ast.FunctionDef) -> Optional[str]:
    """Row-array key for paged responses: deserialized.get("value", []) /
    deserialized["value"] / list_of_elem = deserialized.value

    The extract_data closure also reads the pagination link
    (deserialized.get("nextLink")); link-shaped keys are never the row key.
    """
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if (
                node.func.attr == "get"
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "deserialized"
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and not _PAGING_LINK_KEYS.search(str(node.args[0].value))
            ):
                return str(node.args[0].value)
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            t = node.targets[0]
            if isinstance(t, ast.Name) and t.id == "list_of_elem":
                v = node.value
                if isinstance(v, ast.Attribute) and isinstance(v.value, ast.Name) and v.value.id == "deserialized":
                    # msrest attr name -> wire key is resolved by caller
                    return "@attr:" + v.attr
                if isinstance(v, ast.Subscript) and isinstance(v.slice, ast.Constant):
                    return str(v.slice.value)
    return None


def _body_model_from_args(fn: ast.FunctionDef, path_query_pynames: set) -> Optional[str]:
    """Positional params annotated with a _models.X (or Union incl. one) that
    aren't path/query params are the request body."""
    for a in fn.args.posonlyargs + fn.args.args:
        if a.arg in ("self",) or a.arg in path_query_pynames:
            continue
        if a.annotation is None:
            continue
        ann = ast.unparse(a.annotation)
        m = _MODELS_RE.search(ann)
        if m:
            return m.group(1)
        # msrest style: parameters: "X" quoted forward ref w/o _models
    return None


def parse_legacy_class_ops(node: ast.ClassDef) -> list[tuple[OpMethod, BuildFn]]:
    """Ancient msrest style (no request builders): each method carries
    `<name>.metadata = {'url': ...}` at class level and builds the request
    inline via `self._client.get(url, query_parameters, ...)`."""
    out: list[tuple[OpMethod, BuildFn]] = []

    # metadata urls: Assign targets like `send.metadata = {'url': '/sms'}`
    meta_urls: dict[str, str] = {}
    for stmt in node.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
            t = stmt.targets[0]
            if (
                isinstance(t, ast.Attribute)
                and t.attr == "metadata"
                and isinstance(t.value, ast.Name)
                and isinstance(stmt.value, ast.Dict)
            ):
                for k, v in zip(stmt.value.keys, stmt.value.values):
                    if isinstance(k, ast.Constant) and k.value == "url" and isinstance(v, ast.Constant):
                        meta_urls[t.value.id] = str(v.value)

    for i, fn in enumerate(s for s in node.body if isinstance(s, ast.FunctionDef)):
        if fn.name.startswith("_") or fn.name not in meta_urls:
            continue
        bf = BuildFn(f"legacy_{node.name}_{fn.name}")
        bf.url = meta_urls[fn.name]

        required_py = set()
        defaults_start = len(fn.args.args) - len(fn.args.defaults)
        for j, a in enumerate(fn.args.args):
            if a.arg == "self":
                continue
            if j < defaults_start:
                required_py.add(a.arg)

        wire_map: dict[str, dict] = {}
        body_model = None
        response_model = None
        for sub in ast.walk(fn):
            if isinstance(sub, ast.Assign) and len(sub.targets) == 1:
                t = sub.targets[0]
                if isinstance(t, ast.Name) and t.id == "api_version" and isinstance(sub.value, ast.Constant):
                    bf.api_version = str(sub.value.value)
                if isinstance(t, ast.Name) and t.id == "path_format_arguments" and isinstance(sub.value, ast.Dict):
                    for k, v in zip(sub.value.keys, sub.value.values):
                        if (
                            isinstance(k, ast.Constant)
                            and isinstance(v, ast.Call)
                            and v.args
                            and isinstance(v.args[0], ast.Constant)
                        ):
                            py = str(v.args[0].value).replace("self._config.", "")
                            tstr = v.args[2].value if len(v.args) > 2 and isinstance(v.args[2], ast.Constant) else "str"
                            wire_map[py] = {"wire": k.value, "in": "path", "tstr": tstr}
                if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name):
                    coll = t.value.id
                    key = t.slice.value if isinstance(t.slice, ast.Constant) else None
                    if key and isinstance(sub.value, ast.Call):
                        call = sub.value
                        cattr = getattr(call.func, "attr", "")
                        if call.args and isinstance(call.args[0], ast.Constant):
                            py = str(call.args[0].value).replace("self._config.", "")
                            tstr = (
                                call.args[2].value
                                if len(call.args) > 2 and isinstance(call.args[2], ast.Constant)
                                else "str"
                            )
                            if coll == "query_parameters" and cattr == "query" and key != "api-version":
                                wire_map.setdefault(py, {"wire": key, "in": "query", "tstr": tstr})
                            elif coll == "header_parameters" and cattr == "header" and py not in ("accept", "content_type"):
                                wire_map.setdefault(py, {"wire": key, "in": "header", "tstr": tstr})
            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute):
                # request = self._client.get(url, ...)
                if (
                    isinstance(sub.func.value, ast.Attribute)
                    and getattr(sub.func.value.value, "id", "") == "self"
                    and sub.func.value.attr == "_client"
                    and sub.func.attr in ("get", "put", "post", "patch", "delete", "head", "options")
                ):
                    bf.http_method = sub.func.attr
                # body_content = self._serialize.body(body, 'SendMessageRequest')
                if sub.func.attr == "body" and len(sub.args) > 1 and isinstance(sub.args[1], ast.Constant):
                    body_model = str(sub.args[1].value).strip("[]{}")
                    bf.has_body_content = True
                # deserialized = self._deserialize('XCollection', pipeline_response)
                if sub.func.attr == "_deserialize" and sub.args and isinstance(sub.args[0], ast.Constant):
                    v = str(sub.args[0].value)
                    if v and v[0].isupper():
                        response_model = v.strip("[]")

        for py in list(required_py) + [p for p in wire_map if p not in required_py]:
            info = wire_map.get(py)
            if not info:
                continue
            bf.params.append(
                {
                    "py": py,
                    "wire": info["wire"],
                    "in": info["in"],
                    "required": py in required_py or info["in"] == "path",
                    "schema": serializer_type_to_schema(info["tstr"]),
                }
            )

        op = OpMethod(node.name, fn.name)
        op.src_order = i
        op.build_fn_name = bf.name
        op.docstring = ast.get_docstring(fn)
        op.return_ann = ast.unparse(fn.returns) if fn.returns else None
        op.body_model = body_model
        op.paged_key = _find_paged_key(fn)
        paged = any(
            isinstance(c, ast.Call) and getattr(c.func, "id", "") == "ItemPaged"
            for c in ast.walk(fn)
        )
        if response_model and not op.return_ann:
            op.return_ann = (
                f"ItemPaged['_models.{response_model}']" if paged else f"_models.{response_model}"
            )
        elif response_model and paged and "ItemPaged" not in (op.return_ann or ""):
            op.return_ann = f"ItemPaged['_models.{response_model}']"
        out.append((op, bf))
    return out


def parse_operations_module(path: Path):
    """Returns (build_fns: dict, op_methods: list[OpMethod]).

    Build functions are scoped to this module - old-style packages (one file
    per operation group) reuse names like `build_list_request` across modules,
    so builders must never be pooled across modules.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return {}, []

    build_fns: dict[str, BuildFn] = {}
    op_methods: list[OpMethod] = []
    referenced_builders: set[str] = set()

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name.startswith("build_"):
            bf = parse_build_fn(node)
            if bf:
                build_fns[node.name] = bf

    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        cls_name = node.name
        if not (cls_name.endswith("Operations") or cls_name.endswith("OperationsMixin") or cls_name.endswith("Mixin")):
            continue

        # collect defs; skip @overload variants
        defs: dict[str, ast.FunctionDef] = {}
        overloads: dict[str, list[ast.FunctionDef]] = {}
        order: dict[str, int] = {}
        for i, stmt in enumerate(node.body):
            if not isinstance(stmt, ast.FunctionDef):
                continue
            deco = [ast.unparse(d) for d in stmt.decorator_list]
            if any(d == "overload" or d.endswith(".overload") for d in deco):
                overloads.setdefault(stmt.name, []).append(stmt)
                continue
            defs[stmt.name] = stmt
            order[stmt.name] = i

        def _emit_class_ops(include_private: bool) -> int:
            emitted = 0
            for mname, fn in defs.items():
                public_name = mname
                if mname.startswith("_"):
                    if not include_private:
                        continue
                    if mname.startswith("__") or mname.endswith("_initial"):
                        continue
                    public_name = mname.lstrip("_")
                    if not public_name:
                        continue
                op = OpMethod(cls_name, public_name)
                op.src_order = order.get(mname, 0)
                op.docstring = ast.get_docstring(fn)
                op.return_ann = ast.unparse(fn.returns) if fn.returns else None
                op.is_lro = public_name.startswith("begin_")

                target_fn = fn
                op.build_fn_name = _find_build_call(fn)
                if not op.build_fn_name:
                    init_name = _find_initial_call(fn)
                    if init_name and init_name in defs:
                        target_fn = defs[init_name]
                        op.build_fn_name = _find_build_call(target_fn)
                if not op.build_fn_name or op.build_fn_name not in build_fns:
                    continue
                referenced_builders.add(op.build_fn_name)

                bf = build_fns[op.build_fn_name]
                pynames = {p["py"] for p in bf.params}
                # body model: prefer the impl/_initial signature; overloads
                # carry the typed form when the impl uses Union[..., IO[bytes]]
                op.body_model = _body_model_from_args(target_fn, pynames)
                if not op.body_model:
                    for ov in overloads.get(mname, []):
                        op.body_model = _body_model_from_args(ov, pynames)
                        if op.body_model:
                            break

                op.paged_key = _find_paged_key(fn)
                op_methods.append(op)
                emitted += 1
            return emitted

        # Customised clients (e.g. azure-ai-inference) keep the generated ops
        # private and re-export a hand-written surface from _patch.py. When a
        # class has no public ops at all, fall back to its private methods -
        # they are the real REST operations.
        if _emit_class_ops(include_private=False) == 0:
            _emit_class_ops(include_private=True)

    # Ancient msrest fallback: no request builders at all - methods carry
    # `<name>.metadata = {'url': ...}` and build requests inline.
    if not build_fns:
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name.endswith(("Operations", "OperationsMixin", "Mixin")):
                for op, bf in parse_legacy_class_ops(node):
                    build_fns[bf.name] = bf
                    op_methods.append(op)
        return build_fns, op_methods

    # Last-resort fallback: a module with builders but no parseable op class
    # (LLC-style / protocol-only packages). Synthesize one op per builder so
    # the REST surface is still reachable (no response schema / docs).
    if not op_methods and build_fns:
        stem = path.stem  # e.g. _rate_card_operations or _operations
        group_hint = None
        m = re.match(r"^_?(.*?)_operations$", stem)
        if m and m.group(1):
            group_hint = m.group(1)
        for fname, bf in build_fns.items():
            core = re.sub(r"^build_", "", re.sub(r"_request$", "", fname))
            method_name = core
            if group_hint and core.startswith(group_hint + "_"):
                method_name = core[len(group_hint) + 1:]
            op = OpMethod("_BuilderFallbackMixin", method_name or core)
            op.build_fn_name = fname
            op_methods.append(op)

    return build_fns, op_methods


# --------------------------------------------------------------------------- #
# ARM `properties` envelope flattening (SELECT result sets)
# --------------------------------------------------------------------------- #
#
# Nearly every ARM resource nests its interesting attributes under a
# top-level `properties` object. For SELECT projections we synthesize a
# `<Model>Flattened` schema (top-level fields + the properties model's
# fields hoisted up one level, top-level names win clashes) and stage 2
# attaches a generic golang_template_json_v0.3.0 response transform that
# reshapes each row to match. Request bodies keep the native nested shape.


def _ref_name(schema: Optional[dict]) -> Optional[str]:
    if isinstance(schema, dict) and "$ref" in schema:
        return schema["$ref"].rsplit("/", 1)[-1]
    return None


def make_flattened_schema(model_index: ModelIndex, model_name: str) -> Optional[str]:
    """Emit `<model_name>Flattened` if the model has an ARM-style
    `properties` envelope; returns the flattened schema name or None.

    Two shapes are handled:
      - typespec / plain msrest: a `properties` field $ref-ing a sub-model
      - msrest client-side flattening: dotted wire paths
        (`properties.provisioningState`) already assembled into an inline
        `properties` object by assemble_props
    """
    flat_name = f"{model_name}Flattened"
    if flat_name in model_index.emitted:
        return flat_name
    if model_name not in model_index.models:
        return None
    fields = model_index._merged_fields(model_name)
    props, _req = model_index.assemble_props(fields)
    penv = props.get("properties")
    if not isinstance(penv, dict):
        return None

    inner: "OrderedDict[str, Any]" = OrderedDict()
    props_model = _ref_name(penv)
    if props_model and props_model in model_index.models:
        inner, _ = model_index.assemble_props(model_index._merged_fields(props_model))
    elif isinstance(penv.get("properties"), dict) and penv["properties"]:
        inner = penv["properties"]
    if not inner:
        return None

    out_props: "OrderedDict[str, Any]" = OrderedDict()
    for wire, schema in props.items():
        if wire == "properties":
            continue
        out_props[wire] = schema
    for wire, schema in inner.items():
        # top-level names win clashes (the transform emits props first, so a
        # duplicate JSON key resolves to the top-level value)
        out_props.setdefault(wire, schema)
    if not out_props:
        return None
    model_index.emitted[flat_name] = {
        "type": "object",
        "description": f"Flattened view of {model_name} ('properties' hoisted to the top level).",
        "properties": out_props,
    }
    return flat_name


def _element_model_of_value_field(model_index: ModelIndex, envelope: str) -> Optional[str]:
    """For XxxListResult-style envelopes: the model name of value[]'s items."""
    fields = model_index._merged_fields(envelope)
    vf = next((f for f in fields.values() if str(f.wire) == "value"), None)
    if vf is None:
        return None
    schema = model_index.annotation_to_schema(vf.annotation)
    if schema.get("type") == "array":
        return _ref_name(schema.get("items"))
    return None


# --------------------------------------------------------------------------- #
# mastered naming / verb overrides (provider-dev/config/name-overrides.json)
# --------------------------------------------------------------------------- #
#
# Generic inference gets acronyms wrong occasionally (VNetPeering ->
# v_net_peering) and some SDK method names carry the same wart verbatim
# (detach_v_net). The overrides file is the mastered fix-up layer, applied
# AFTER inference:
#   - segments:  whole snake-segment rewrites on every resource/method name
#   - resources: exact renames keyed by '<service>.<resource>'
#   - methods:   exact renames keyed by '<service>.<resource>.<method>'
#   - verbs:     SQL verb overrides keyed by '<service>.<resource>.<method>'

_DEFAULT_OVERRIDES_PATH = (
    Path(__file__).resolve().parents[1] / "provider-dev" / "config" / "name-overrides.json"
)


class NameOverrides:
    def __init__(self, path: Optional[Path] = None):
        self.segments: dict[str, str] = {}
        self.resources: dict[str, str] = {}
        self.methods: dict[str, str] = {}
        self.verbs: dict[str, str] = {}
        self.servers: dict[str, list] = {}
        p = path or _DEFAULT_OVERRIDES_PATH
        if p and p.exists():
            import json
            doc = json.loads(p.read_text(encoding="utf-8"))
            self.segments = doc.get("segments") or {}
            self.resources = doc.get("resources") or {}
            self.methods = doc.get("methods") or {}
            self.verbs = doc.get("verbs") or {}
            self.servers = doc.get("servers") or {}

    def apply_segments(self, name: str) -> str:
        for seg, repl in self.segments.items():
            name = re.sub(rf"(^|_){re.escape(seg)}(_|$)", rf"\g<1>{repl}\g<2>", name)
            # run twice for adjacent occurrences sharing an underscore
            name = re.sub(rf"(^|_){re.escape(seg)}(_|$)", rf"\g<1>{repl}\g<2>", name)
        return name

    def resource_name(self, alias: str, resource: str) -> str:
        resource = self.apply_segments(resource)
        return self.resources.get(f"{alias}.{resource}", resource)

    def method_name(self, alias: str, resource: str, method: str) -> str:
        method = self.apply_segments(method)
        return self.methods.get(f"{alias}.{resource}.{method}", method)

    def verb(self, alias: str, resource: str, method: str, inferred: str) -> str:
        return self.verbs.get(f"{alias}.{resource}.{method}", inferred)


# --------------------------------------------------------------------------- #
# verb + resource inference
# --------------------------------------------------------------------------- #

# Method-name qualifiers that do NOT indicate a sub-resource (list_by_resource_group
# still targets the group's resource).
_LIST_QUALIFIERS = re.compile(
    r"^(list|get)(_all)?(_by_[a-z0-9_]+|_in_[a-z0-9_]+)?$"
)


def infer_verb(method_name: str, http_method: str) -> str:
    n = method_name[6:] if method_name.startswith("begin_") else method_name
    if http_method == "get" and (n == "get" or n == "list" or n.startswith("get_") or n.startswith("list_")):
        return "SELECT"
    if n.startswith("create_or_update") or n.startswith("create_or_replace"):
        return "INSERT"
    if n.startswith("create") and http_method in ("put", "post"):
        return "INSERT"
    if n.startswith("update") and http_method in ("patch", "put"):
        return "UPDATE"
    if n.startswith("replace") and http_method == "put":
        return "REPLACE"
    if n.startswith("set_") and http_method == "put":
        return "REPLACE"
    if http_method == "delete" or n.startswith("delete") or n.startswith("purge"):
        return "DELETE"
    return "EXEC"


_MIXIN_VERB_PREFIXES = (
    "get_", "list_", "create_or_update_", "create_", "update_", "delete_",
    "set_", "put_", "purge_", "backup_", "restore_", "begin_",
)


def infer_resource(group_class: str, method_name: str, service_alias: str) -> str:
    """Resource = operation-group snake name; mixin classes (client-level ops)
    fall back to noun extraction from the method name."""
    if group_class.endswith("OperationsMixin") or group_class.endswith("Mixin"):
        n = method_name[6:] if method_name.startswith("begin_") else method_name
        noun = n
        for p in ("get_", "list_", "create_or_update_", "create_", "update_",
                  "delete_", "set_", "put_", "purge_", "backup_", "restore_"):
            if n.startswith(p) and len(n) > len(p):
                noun = n[len(p):]
                break
        else:
            if n in ("get", "list"):
                return service_alias.split("_")[-1]
        # strip list qualifiers (list_widgets_by_farm -> widgets_by_farm -> widgets)
        noun = re.sub(r"_by_[a-z0-9_]+$", "", noun)
        return pluralise(noun) if noun else service_alias
    g = group_class
    for suffix in ("Operations",):
        if g.endswith(suffix):
            g = g[: -len(suffix)]
    # the bare `Operations` group (ARM provider-operations listing) strips
    # to the empty string - it IS the `operations` resource
    return to_snake(g) or "operations"


# Preference rank used by stage 2's dedupe (lower = preferred keeper).
def method_rank(method_name: str) -> int:
    n = method_name
    if n == "get":
        return 0
    if n == "list" or n == "list_all":
        return 1
    if n.startswith("list_by_") or n.startswith("list_in_"):
        return 2
    if n == "create_or_update":
        return 3
    if n.startswith("list"):
        return 4
    if n.startswith("get_by"):
        return 5
    if n.startswith("get"):
        return 6
    return 9


# --------------------------------------------------------------------------- #
# package discovery
# --------------------------------------------------------------------------- #

SKIP_PACKAGES = {
    # meta / runtime / non-REST packages
    "azure", "azure-common", "azure-core", "azure-core-experimental",
    "azure-core-tracing-opentelemetry", "azure-mgmt", "azure-mgmt-core",
    "azure-identity", "azure-identity-broker", "azure-keyvault",
    "azure-monitor", "azure-monitor-opentelemetry", "azure-storage",
    "azure-template", "azure-openai", "azure-postgresql-auth",
    "azure-storage-extensions", "azure-eventhub",
    "azure-eventhub-checkpointstoreblob", "azure-eventhub-checkpointstoreblob-aio",
    "azure-eventhub-checkpointstoretable", "azure-servicebus",
    "azure-schemaregistry-avroencoder", "azure-schemaregistry-jsonencoder",
    "azure-appconfiguration-provider", "azure-messaging-webpubsubclient",
    "azure-media-videoanalyzer-edge", "azure-iot-deviceupdate",
    "azure-ai-ml",  # ML SDK: multi-restclient composite, not a REST surface
    "azure-cosmos",  # hand-written client, no request builders
    "azure-ai-agentserver-core", "azure-ai-agentserver-ghcopilot",
    "azure-ai-agentserver-invocations", "azure-ai-agentserver-optimization",
    "azure-ai-agentserver-responses",
}

_VERSION_DIR_RE = re.compile(r"^v\d{4}_\d{2}_\d{2}.*$|^v\d{4}_\d{2}.*$|^v\d+_\d+(_\d+)?.*$")


def find_operation_modules(pkg_dir: Path) -> list[Path]:
    """All sync operations modules containing request builders; for multiapi
    packages, only the latest version directory."""
    candidates: list[Path] = []
    for p in pkg_dir.rglob("*.py"):
        parts = p.parts
        if "aio" in parts or "_aio" in parts:
            continue
        if p.name in ("__init__.py", "_patch.py", "_vendor.py"):
            continue
        parent = p.parent.name
        if parent not in ("operations", "_operations"):
            continue
        if not (p.name == "_operations.py" or p.name.endswith("_operations.py")):
            continue
        candidates.append(p)

    if not candidates:
        return []

    # multiapi: keep only modules under the lexically-greatest version dir
    def version_tag(p: Path):
        for part in p.parts:
            if _VERSION_DIR_RE.match(part):
                return part
        return None

    tags = {version_tag(p) for p in candidates}
    tags.discard(None)
    if tags:
        latest = sorted(tags)[-1]
        candidates = [p for p in candidates if version_tag(p) in (None, latest)]

    # keep modules with request builders (modern) or method-level metadata
    # urls (ancient msrest - handled by parse_legacy_class_ops)
    out = []
    for p in candidates:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "def build_" in text or re.search(r"\.metadata = \{['\"]url['\"]", text):
            out.append(p)
    return sorted(out)


def find_model_modules(ops_module: Path, pkg_dir: Path) -> list[Path]:
    """models/_models*.py + _enums*.py near the operations module."""
    out: list[Path] = []
    # operations dir -> package base dir
    base = ops_module.parent.parent
    for cand_dir in (base / "models", base.parent / "models", base / "_models"):
        if cand_dir.is_dir():
            for f in sorted(cand_dir.glob("*.py")):
                if f.name.startswith(("_models", "_enums", "models", "_generated_models")):
                    out.append(f)
            if out:
                return out
    return out


def find_client_endpoint(pkg_dir: Path, is_mgmt: bool) -> tuple[str, Optional[dict]]:
    """Returns (server_url, variables|None)."""
    if is_mgmt:
        return "https://management.azure.com/", None
    # look for _endpoint = "{xxx}" or base_url= in any sync _client.py
    for p in sorted(pkg_dir.rglob("_client.py")):
        if "aio" in p.parts:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        m = re.search(r"_endpoint\s*=\s*\"([^\"]+)\"", text)
        if m:
            tpl = m.group(1)
            if tpl.startswith("http") and "{" not in tpl:
                return tpl, None
            # '{vaultBaseUrl}' / '{endpoint}/language' etc
            vars_found = re.findall(r"\{(\w+)\}", tpl)
            out_tpl = tpl
            variables = {}
            for v in vars_found:
                snake = to_snake(v)
                out_tpl = out_tpl.replace("{" + v + "}", "{" + snake + "}")
                variables[snake] = {
                    "default": "",
                    "description": (
                        f"The service endpoint host (no scheme), e.g. "
                        f"myaccount.table.cosmos.azure.com:443 - value of the "
                        f"client `{v}` parameter."
                    ),
                }
            # stackql's request mux requires server templates to carry a
            # scheme; a bare '{endpoint}' template never resolves ("mux:
            # path must start with a slash"). Users supply the HOST part.
            if out_tpl.startswith("{"):
                out_tpl = "https://" + out_tpl
            return out_tpl, variables
        m = re.search(r"base_url:?\s*(?:str)?\s*=\s*kwargs\.pop\(\s*\"base_url\",\s*\"([^\"]+)\"", text)
        if m:
            return m.group(1), None
    return "https://{endpoint}", {"endpoint": {"default": "", "description": "The service endpoint host (no scheme)."}}


def get_client_title(pkg_dir: Path, alias: str) -> tuple[str, str]:
    """(title, description) from the client class docstring / README."""
    title = alias.replace("_", " ").title()
    description = None
    found_class = False
    for p in sorted(pkg_dir.rglob("*client.py")):
        if "aio" in p.parts or p.name.startswith("test"):
            continue
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except (SyntaxError, OSError):
            continue
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name.endswith("Client"):
                title = re.sub(r"(?<!^)(?=[A-Z])", " ", node.name).replace("  ", " ")
                doc = ast.get_docstring(node)
                if doc:
                    description = doc_summary(doc)
                found_class = True
                break
        if found_class:
            break
    readme = pkg_dir / "README.md"
    if not description and readme.exists():
        try:
            for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
                line = line.strip()
                if line.startswith("#"):
                    heading = line.lstrip("# ").strip()
                    # generic repo heading is useless as a title
                    if not found_class and "SDK for Python" not in heading:
                        title = heading
                    continue
                if line and not line.startswith(("[", "!", "<", "#")):
                    description = clean_description(line)
                    break
        except OSError:
            pass
    return title, description or f"Azure {title} (package {pkg_dir.name})"


def service_alias_for(pkg_name: str, is_mgmt: bool) -> str:
    if is_mgmt:
        return to_snake(pkg_name.replace("azure-mgmt-", ""))
    return to_snake(pkg_name.replace("azure-", ""))


# --------------------------------------------------------------------------- #
# spec assembly per package
# --------------------------------------------------------------------------- #


# Path params are wire-neutral (template substitution only), but their names
# surface in SQL WHERE clauses - a param literally named `table` / `group` /
# `key` etc collides with the SQL grammar and forces users to quote. Rename
# with a `_name` suffix at generation time.
SQL_RESERVED_PATH_PARAMS = {
    "table", "key", "group", "view", "type", "default", "order", "index",
    "user", "role", "select", "from", "where", "column", "schema",
    "database", "value", "values", "set", "left", "right", "join", "case",
    "end", "if", "function", "call", "add", "drop", "partition",
}


def snake_param(name: str) -> str:
    s = to_snake(name)
    if s in SQL_RESERVED_PATH_PARAMS:
        return s + "_name"
    return s


def snake_path(url: str) -> tuple[str, dict[str, str]]:
    """Snake-case `{placeholders}` in a URL template. Returns (new_url, renames
    keyed by original placeholder)."""
    renames: dict[str, str] = {}

    def _sub(m):
        orig = m.group(1)
        snake = snake_param(orig)
        renames[orig] = snake
        return "{" + snake + "}"

    return re.sub(r"\{([^{}]+)\}", _sub, url), renames


def build_spec_for_package(
    pkg_dir: Path,
    alias: str,
    is_mgmt: bool,
    report: dict,
) -> Optional[dict]:
    ops_modules = find_operation_modules(pkg_dir)
    if not ops_modules:
        return None

    model_index = ModelIndex()
    model_files_seen: set[Path] = set()
    all_ops: list[OpMethod] = []

    for om in ops_modules:
        for mf in find_model_modules(om, pkg_dir):
            if mf not in model_files_seen:
                model_files_seen.add(mf)
                model_index.add_module(mf)
        bfs, ops = parse_operations_module(om)
        # bind each op to its module-scoped builder (builder names repeat
        # across old-style modules, so a global pool would mis-resolve URLs)
        for op in ops:
            op.bf = bfs.get(op.build_fn_name or "")
        all_ops.extend(ops)

    if not all_ops:
        return None

    server_url, server_vars = find_client_endpoint(pkg_dir, is_mgmt)
    title, description = get_client_title(pkg_dir, alias)

    paths: "OrderedDict[str, dict]" = OrderedDict()
    ops_emitted = 0
    ops_skipped = 0

    # Sort ops so canonical CRUD methods land first within each resource -
    # stage 2's dedupe keeps the first method per signature bucket.
    all_ops.sort(key=lambda o: (o.group, method_rank(
        o.name[6:] if o.name.startswith("begin_") else o.name), o.src_order))

    api_versions = set()

    for op in all_ops:
        bf = op.bf
        if not bf or not bf.url:
            ops_skipped += 1
            continue

        method_name = op.name[6:] if op.name.startswith("begin_") else op.name
        resource = infer_resource(op.group, op.name, alias)
        verb = infer_verb(op.name, bf.http_method)
        # mastered fix-ups (name-overrides.json) applied over the inference
        resource = OVERRIDES.resource_name(alias, resource)
        method_name = OVERRIDES.method_name(alias, resource, method_name)
        verb = OVERRIDES.verb(alias, resource, method_name, verb)

        url_snaked, renames = snake_path(bf.url)
        # Some data-plane builders embed the client endpoint in the operation
        # URL ("{url}/Tables"). The endpoint belongs in the server template
        # (already emitted as servers[0].url) - strip the leading placeholder
        # so the path starts with '/' (stackql's mux requires it) and the
        # phantom endpoint param is dropped from `parameters` below.
        url_snaked = re.sub(r"^\{[^{}]+\}", "", url_snaked) or "/"
        if not url_snaked.startswith("/"):
            url_snaked = "/" + url_snaked
        path_key = url_snaked
        if bf.api_version:
            sep = "&" if "?" in path_key else "?"
            path_key = f"{path_key}{sep}api-version={bf.api_version}"
            api_versions.add(bf.api_version)

        # ----- parameters -----
        param_docs = parse_docstring_params(op.docstring)
        parameters: list[dict] = []
        seen_wire = set()
        for p in bf.params:
            wire = p["wire"]
            loc = p["in"]
            if loc == "path":
                name = renames.get(wire, snake_param(wire))
                # endpoint args stripped from the path template are server
                # variables, not path params - drop them here (users supply
                # them as server params, e.g. WHERE url = 'https://...')
                if "{" + name + "}" not in url_snaked:
                    continue
            else:
                name = wire
            if (name, loc) in seen_wire:
                continue
            seen_wire.add((name, loc))
            entry = {
                "name": name,
                "in": loc,
                "required": bool(p["required"]),
                "schema": p["schema"],
            }
            desc = param_docs.get(p["py"])
            if desc:
                entry["description"] = desc
            parameters.append(entry)

        # ----- operation block -----
        op_block: "OrderedDict[str, Any]" = OrderedDict()
        group_pascal = op.group
        for suffix in ("OperationsMixin", "Operations", "Mixin"):
            if group_pascal.endswith(suffix):
                group_pascal = group_pascal[: -len(suffix)]
                break
        op_block["operationId"] = f"{group_pascal or alias}_{OVERRIDES.apply_segments(op.name)}"
        desc = doc_summary(op.docstring)
        if desc:
            op_block["description"] = desc
        op_block["parameters"] = parameters

        # ----- request body -----
        if op.body_model:
            body_schema = model_index.body_schema(op.body_model)
            if body_schema is None:
                body_schema = model_index.annotation_to_schema(f"_models.{op.body_model}")
                if "$ref" not in body_schema and "properties" not in body_schema:
                    body_schema = {"type": "object", "properties": {}}
            op_block["requestBody"] = {
                "required": True,
                "content": {"application/json": {"schema": body_schema}},
            }
        elif bf.has_body_content and bf.http_method in ("put", "post", "patch"):
            # body exists but is untyped (JSON / IO); surface a free-form body
            op_block["requestBody"] = {
                "required": False,
                "content": {"application/json": {"schema": {"type": "object", "properties": {}}}},
            }

        # ----- response -----
        response_schema = None
        object_key = None
        flatten_kind = None  # 'list' | 'singleton' (properties envelope hoist)
        ret = op.return_ann or ""
        paged = bool(re.search(r"\b(ItemPaged|AsyncItemPaged|Iterable)\[", ret))
        mret = _MODELS_RE.search(ret)
        model_name = mret.group(1) if mret else None

        if paged and model_name:
            key = op.paged_key or "value"
            if key.startswith("@attr:"):
                # msrest: attr name -> wire key via the envelope model
                attr = key[len("@attr:"):]
                key = attr
                # find any list-envelope model with this attr to get wire name
                for mdl in model_index.models.values():
                    if attr in mdl.fields and str(mdl.fields[attr].wire) and mdl.name.endswith(("ListResult", "List", "Collection")):
                        key = str(mdl.fields[attr].wire).split(".")[0]
                        break
            key = _safe_property_name(key)
            flat = make_flattened_schema(model_index, model_name) if verb == "SELECT" else None
            item_ref = (
                {"$ref": f"#/components/schemas/{flat}"}
                if flat
                else model_index.ref(model_name)
            )
            page_name = f"Paged{flat or model_name}"
            if page_name not in model_index.emitted:
                model_index.emitted[page_name] = {
                    "type": "object",
                    "properties": {
                        key: {"type": "array", "items": item_ref},
                        "nextLink": {"type": "string"},
                    },
                }
            response_schema = {"$ref": f"#/components/schemas/{page_name}"}
            object_key = f"$.{key}"
            if flat:
                flatten_kind = "list"
        elif model_name:
            # non-paged ListResult envelopes still carry rows under `value`
            elem = None
            if model_name.endswith(("ListResult", "Collection", "List")):
                elem = _element_model_of_value_field(model_index, model_name)
            if elem:
                object_key = "$.value"
                flat = make_flattened_schema(model_index, elem) if verb == "SELECT" else None
                if flat:
                    env_name = f"{model_name}Flattened"
                    if env_name not in model_index.emitted:
                        model_index.emitted[env_name] = {
                            "type": "object",
                            "properties": {
                                "value": {
                                    "type": "array",
                                    "items": {"$ref": f"#/components/schemas/{flat}"},
                                },
                                "nextLink": {"type": "string"},
                            },
                        }
                    response_schema = {"$ref": f"#/components/schemas/{env_name}"}
                    flatten_kind = "list"
                else:
                    response_schema = model_index.ref(model_name)
            else:
                flat = make_flattened_schema(model_index, model_name) if verb == "SELECT" else None
                if flat:
                    response_schema = {"$ref": f"#/components/schemas/{flat}"}
                    flatten_kind = "singleton"
                else:
                    response_schema = model_index.ref(model_name)
        elif re.search(r"->?\s*bool$", ret) or ret == "bool":
            response_schema = {"type": "boolean"}

        if response_schema is not None:
            responses = {
                "200": {
                    "description": "Success",
                    "content": {"application/json": {"schema": response_schema}},
                }
            }
        elif op.is_lro or verb == "DELETE":
            responses = {"204": {"description": "Success (no content / accepted)"}}
        else:
            responses = {"200": {"description": "Success"}}
        op_block["responses"] = responses

        # ----- x-stackql breadcrumbs -----
        op_block["x-stackql-resource"] = resource
        op_block["x-stackql-method"] = method_name
        op_block["x-stackql-verb"] = verb
        if object_key and verb == "SELECT":
            op_block["x-stackql-objectKey"] = object_key
        if flatten_kind:
            # stage 2 attaches the generic golang_template_json response
            # transform that hoists the ARM `properties` envelope
            op_block["x-stackql-flatten"] = flatten_kind
            if flatten_kind == "list" and object_key:
                op_block["x-stackql-flattenKey"] = object_key.lstrip("$.")

        path_item = paths.setdefault(path_key, OrderedDict())
        if bf.http_method in path_item:
            # collision: same (path, verb) from two groups - keep first
            ops_skipped += 1
            continue
        path_item[bf.http_method] = op_block
        ops_emitted += 1

    if ops_emitted == 0:
        return None

    latest_api = sorted(api_versions)[-1] if api_versions else "unversioned"

    spec: "OrderedDict[str, Any]" = OrderedDict()
    spec["openapi"] = "3.0.0"
    servers = [{"url": server_url}]
    if server_vars:
        servers[0]["variables"] = server_vars
    # mastered per-service server templates (name-overrides.json `servers`):
    # data-plane hosts must keep variables to a single DNS label for
    # stackql's request router to match
    if alias in OVERRIDES.servers:
        servers = OVERRIDES.servers[alias]
    spec["servers"] = servers
    spec["info"] = OrderedDict(
        [
            ("title", title),
            ("description", description),
            ("contact", {
                "name": "StackQL Studios",
                "url": "https://stackql.io/",
                "email": "info@stackql.io",
            }),
            ("version", f"{latest_api}-stackql-generated"),
            ("x-serviceAlias", alias),
            ("x-sdkPackage", pkg_dir.name),
            ("x-plane", "mgmt" if is_mgmt else "data"),
        ]
    )
    spec["security"] = [{"azure_auth": ["user_impersonation"]}]
    spec["components"] = OrderedDict()
    spec["components"]["securitySchemes"] = {
        "azure_auth": {
            "description": "Azure Active Directory OAuth2 Flow.",
            "type": "oauth2",
            "flows": {
                "implicit": {
                    "authorizationUrl": "https://login.microsoftonline.com/common/oauth2/authorize",
                    "scopes": {"user_impersonation": "impersonate your user account"},
                }
            },
        }
    }
    spec["components"]["schemas"] = model_index.emitted
    spec["paths"] = paths

    report["ops_emitted"] += ops_emitted
    report["ops_skipped"] += ops_skipped
    return spec


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #


def discover_packages() -> list[tuple[Path, str, bool]]:
    """Returns [(pkg_dir, alias, is_mgmt)]. Handles alias collisions between
    mgmt and data planes (data plane gets `_dataplane` suffix)."""
    found: list[tuple[Path, str, bool]] = []
    for svc_dir in sorted(SDK_ROOT.iterdir()):
        if not svc_dir.is_dir():
            continue
        for pkg_dir in sorted(svc_dir.iterdir()):
            if not pkg_dir.is_dir() or not pkg_dir.name.startswith("azure"):
                continue
            if pkg_dir.name in SKIP_PACKAGES or pkg_dir.name.endswith("-nspkg"):
                continue
            if not ((pkg_dir / "setup.py").exists() or (pkg_dir / "pyproject.toml").exists()):
                continue
            is_mgmt = "-mgmt-" in pkg_dir.name
            alias = service_alias_for(pkg_dir.name, is_mgmt)
            found.append((pkg_dir, alias, is_mgmt))

    # collision resolution: mgmt keeps the bare alias
    by_alias: dict[str, list[int]] = {}
    for i, (_, alias, _m) in enumerate(found):
        by_alias.setdefault(alias, []).append(i)
    out = []
    for alias, idxs in by_alias.items():
        if len(idxs) == 1:
            out.append(found[idxs[0]])
            continue
        for i in idxs:
            pkg_dir, a, is_mgmt = found[i]
            if is_mgmt:
                out.append((pkg_dir, a, is_mgmt))
            else:
                out.append((pkg_dir, a + "_dataplane", is_mgmt))
    out.sort(key=lambda t: t[1])
    return out


# module-level so build_spec_for_package sees it; re-initialised in main()
OVERRIDES = NameOverrides()


def main() -> int:
    global OVERRIDES
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--service", action="append", default=[],
                    help="only emit these service aliases (repeatable)")
    ap.add_argument("--name-overrides", default=None,
                    help="path to name-overrides.json (default: provider-dev/config/name-overrides.json)")
    ap.add_argument("--list", action="store_true", help="list discovered packages and exit")
    args = ap.parse_args()

    OVERRIDES = NameOverrides(Path(args.name_overrides) if args.name_overrides else None)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    packages = discover_packages()
    if args.list:
        for pkg_dir, alias, is_mgmt in packages:
            print(f"{alias:45s} {'mgmt' if is_mgmt else 'data':4s} {pkg_dir.name}")
        return 0

    wanted = set(args.service)
    written = 0
    skipped: list[str] = []
    report = {"ops_emitted": 0, "ops_skipped": 0}

    for pkg_dir, alias, is_mgmt in packages:
        if wanted and alias not in wanted:
            continue
        try:
            spec = build_spec_for_package(pkg_dir, alias, is_mgmt, report)
        except Exception as exc:  # noqa: BLE001 - keep the batch going
            print(f"  fail  {alias}: {type(exc).__name__}: {exc}", file=sys.stderr)
            skipped.append(alias)
            continue
        if spec is None:
            skipped.append(alias)
            continue
        with open(out_dir / f"{alias}.yaml", "w", encoding="utf-8") as f:
            ordered_yaml_dump(spec, f)
        n_paths = len(spec["paths"])
        print(f"  ok    {alias}  ({n_paths} paths)")
        written += 1

    print(
        f"\nWrote {written} services to {out_dir} "
        f"({report['ops_emitted']} operations; {report['ops_skipped']} skipped ops; "
        f"{len(skipped)} packages without parseable REST surface)"
    )
    if skipped:
        print("skipped packages: " + ", ".join(sorted(skipped)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
