package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"os"
	"reflect"
	"text/template"
)

func main() {
	tplBytes, _ := os.ReadFile(os.Args[1])
	dataBytes, _ := os.ReadFile(os.Args[2])
	var data interface{}
	json.Unmarshal(dataBytes, &data)
	fm := template.FuncMap{
		"toJson": func(v interface{}) (string, error) { b, e := json.Marshal(v); return string(b), e },
		"kindOf": func(v interface{}) string { if v == nil { return "invalid" }; return reflect.TypeOf(v).Kind().String() },
	}
	tpl, err := template.New("t").Funcs(fm).Parse(string(tplBytes))
	if err != nil { fmt.Println("PARSE ERROR:", err); os.Exit(1) }
	var buf bytes.Buffer
	if err := tpl.Execute(&buf, data); err != nil { fmt.Println("EXEC ERROR:", err); os.Exit(1) }
	var out interface{}
	if err := json.Unmarshal(buf.Bytes(), &out); err != nil {
		fmt.Println("INVALID JSON OUTPUT:", err)
		fmt.Println(buf.String())
		os.Exit(1)
	}
	pretty, _ := json.MarshalIndent(out, "", " ")
	fmt.Println("VALID JSON:")
	fmt.Println(string(pretty))
}
