--- 
title: append_blob
hide_title: false
hide_table_of_contents: false
keywords:
  - append_blob
  - storage_blob
  - azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure resources using SQL
custom_edit_url: null
image: /img/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>append_blob</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="append_blob" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_blob.append_blob" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-Content-Length"><code>Content-Length</code></a>, <a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-blob-content-type"><code>x-ms-blob-content-type</code></a>, <a href="#parameter-x-ms-blob-content-encoding"><code>x-ms-blob-content-encoding</code></a>, <a href="#parameter-x-ms-blob-content-language"><code>x-ms-blob-content-language</code></a>, <a href="#parameter-x-ms-blob-content-md5"><code>x-ms-blob-content-md5</code></a>, <a href="#parameter-x-ms-blob-cache-control"><code>x-ms-blob-cache-control</code></a>, <a href="#parameter-x-ms-meta"><code>x-ms-meta</code></a>, <a href="#parameter-x-ms-lease-id"><code>x-ms-lease-id</code></a>, <a href="#parameter-x-ms-blob-content-disposition"><code>x-ms-blob-content-disposition</code></a>, <a href="#parameter-x-ms-encryption-key"><code>x-ms-encryption-key</code></a>, <a href="#parameter-x-ms-encryption-key-sha256"><code>x-ms-encryption-key-sha256</code></a>, <a href="#parameter-x-ms-encryption-algorithm"><code>x-ms-encryption-algorithm</code></a>, <a href="#parameter-x-ms-encryption-scope"><code>x-ms-encryption-scope</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a>, <a href="#parameter-x-ms-if-tags"><code>x-ms-if-tags</code></a>, <a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-x-ms-tags"><code>x-ms-tags</code></a>, <a href="#parameter-x-ms-immutability-policy-until-date"><code>x-ms-immutability-policy-until-date</code></a>, <a href="#parameter-x-ms-immutability-policy-mode"><code>x-ms-immutability-policy-mode</code></a>, <a href="#parameter-x-ms-legal-hold"><code>x-ms-legal-hold</code></a></td>
    <td>The Create Append Blob operation creates a new append blob.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-Content-Length">
    <td><CopyableCode code="Content-Length" /></td>
    <td><code>integer</code></td>
    <td>The length of the request. Required.</td>
</tr>
<tr id="parameter-account">
    <td><CopyableCode code="account" /></td>
    <td><code>string</code></td>
    <td>Storage account name. (default: )</td>
</tr>
<tr id="parameter-x-ms-version">
    <td><CopyableCode code="x-ms-version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Modified-Since">
    <td><CopyableCode code="If-Modified-Since" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see</td>
</tr>
<tr id="parameter-x-ms-blob-cache-control">
    <td><CopyableCode code="x-ms-blob-cache-control" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-blob-content-disposition">
    <td><CopyableCode code="x-ms-blob-content-disposition" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-blob-content-encoding">
    <td><CopyableCode code="x-ms-blob-content-encoding" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-blob-content-language">
    <td><CopyableCode code="x-ms-blob-content-language" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-blob-content-md5">
    <td><CopyableCode code="x-ms-blob-content-md5" /></td>
    <td><code>string (byte)</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-blob-content-type">
    <td><CopyableCode code="x-ms-blob-content-type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-client-request-id">
    <td><CopyableCode code="x-ms-client-request-id" /></td>
    <td><code>string</code></td>
    <td>Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-encryption-algorithm">
    <td><CopyableCode code="x-ms-encryption-algorithm" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-encryption-key">
    <td><CopyableCode code="x-ms-encryption-key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-encryption-key-sha256">
    <td><CopyableCode code="x-ms-encryption-key-sha256" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-encryption-scope">
    <td><CopyableCode code="x-ms-encryption-scope" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-if-tags">
    <td><CopyableCode code="x-ms-if-tags" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-immutability-policy-mode">
    <td><CopyableCode code="x-ms-immutability-policy-mode" /></td>
    <td><code>string</code></td>
    <td>Specifies the immutability policy mode to set on the blob. Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.</td>
</tr>
<tr id="parameter-x-ms-immutability-policy-until-date">
    <td><CopyableCode code="x-ms-immutability-policy-until-date" /></td>
    <td><code>string</code></td>
    <td>Specifies the date time when the blobs immutability policy is set to expire. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-lease-id">
    <td><CopyableCode code="x-ms-lease-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-legal-hold">
    <td><CopyableCode code="x-ms-legal-hold" /></td>
    <td><code>boolean</code></td>
    <td>Specified if a legal hold should be set on the blob. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-meta">
    <td><CopyableCode code="x-ms-meta" /></td>
    <td><code>object</code></td>
    <td>Optional. Specifies a user-defined name-value pair associated with the blob. If no name-value pairs are specified, the operation will copy the metadata from the source blob or file to the destination blob. If one or more name-value pairs are specified, the destination blob is created with the specified metadata, and metadata is not copied from the source blob or file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more information. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-tags">
    <td><CopyableCode code="x-ms-tags" /></td>
    <td><code>string</code></td>
    <td>Optional. Used to set blob tags in various blob operations. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

The Create Append Blob operation creates a new append blob.

```sql
INSERT INTO azure.storage_blob.append_blob (
blobCacheControl,
blobContentType,
blobContentMD5,
blobContentEncoding,
blobContentLanguage,
blobContentDisposition,
Content-Length,
x-ms-version,
account,
timeout,
x-ms-blob-content-type,
x-ms-blob-content-encoding,
x-ms-blob-content-language,
x-ms-blob-content-md5,
x-ms-blob-cache-control,
x-ms-meta,
x-ms-lease-id,
x-ms-blob-content-disposition,
x-ms-encryption-key,
x-ms-encryption-key-sha256,
x-ms-encryption-algorithm,
x-ms-encryption-scope,
If-Modified-Since,
If-Unmodified-Since,
If-Match,
If-None-Match,
x-ms-if-tags,
x-ms-client-request-id,
x-ms-tags,
x-ms-immutability-policy-until-date,
x-ms-immutability-policy-mode,
x-ms-legal-hold
)
SELECT 
'{{ blobCacheControl }}',
'{{ blobContentType }}',
'{{ blobContentMD5 }}',
'{{ blobContentEncoding }}',
'{{ blobContentLanguage }}',
'{{ blobContentDisposition }}',
'{{ Content-Length }}',
'{{ x-ms-version }}',
'{{ account }}',
'{{ timeout }}',
'{{ x-ms-blob-content-type }}',
'{{ x-ms-blob-content-encoding }}',
'{{ x-ms-blob-content-language }}',
'{{ x-ms-blob-content-md5 }}',
'{{ x-ms-blob-cache-control }}',
'{{ x-ms-meta }}',
'{{ x-ms-lease-id }}',
'{{ x-ms-blob-content-disposition }}',
'{{ x-ms-encryption-key }}',
'{{ x-ms-encryption-key-sha256 }}',
'{{ x-ms-encryption-algorithm }}',
'{{ x-ms-encryption-scope }}',
'{{ If-Modified-Since }}',
'{{ If-Unmodified-Since }}',
'{{ If-Match }}',
'{{ If-None-Match }}',
'{{ x-ms-if-tags }}',
'{{ x-ms-client-request-id }}',
'{{ x-ms-tags }}',
'{{ x-ms-immutability-policy-until-date }}',
'{{ x-ms-immutability-policy-mode }}',
'{{ x-ms-legal-hold }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: append_blob
  props:
    - name: Content-Length
      value: {{ Content-Length }}
      description: Required parameter for the append_blob resource.
    - name: x-ms-version
      value: "{{ x-ms-version }}"
      description: Required parameter for the append_blob resource.
    - name: account
      value: "{{ account }}"
      description: Required parameter for the append_blob resource.
    - name: blobCacheControl
      value: "{{ blobCacheControl }}"
      description: |
        Optional. Sets the blob's cache control. If specified, this property is stored with the blob and returned with a read request.
    - name: blobContentType
      value: "{{ blobContentType }}"
      description: |
        Optional. Sets the blob's content type. If specified, this property is stored with the blob and returned with a read request.
    - name: blobContentMD5
      value: "{{ blobContentMD5 }}"
      description: |
        Optional. An MD5 hash of the blob content. Note that this hash is not validated, as the hashes for the individual blocks were validated when each was uploaded.
    - name: blobContentEncoding
      value: "{{ blobContentEncoding }}"
      description: |
        Optional. Sets the blob's content encoding. If specified, this property is stored with the blob and returned with a read request.
    - name: blobContentLanguage
      value: "{{ blobContentLanguage }}"
      description: |
        Optional. Set the blob's content language. If specified, this property is stored with the blob and returned with a read request.
    - name: blobContentDisposition
      value: "{{ blobContentDisposition }}"
      description: |
        Optional. Sets the blob's Content-Disposition header.
    - name: timeout
      value: {{ timeout }}
      description: The timeout parameter is expressed in seconds. For more information, see
      description: The timeout parameter is expressed in seconds. For more information, see
    - name: x-ms-blob-content-type
      value: "{{ x-ms-blob-content-type }}"
    - name: x-ms-blob-content-encoding
      value: "{{ x-ms-blob-content-encoding }}"
    - name: x-ms-blob-content-language
      value: "{{ x-ms-blob-content-language }}"
    - name: x-ms-blob-content-md5
      value: "{{ x-ms-blob-content-md5 }}"
    - name: x-ms-blob-cache-control
      value: "{{ x-ms-blob-cache-control }}"
    - name: x-ms-meta
      value: "{{ x-ms-meta }}"
      description: Optional. Specifies a user-defined name-value pair associated with the blob. If no name-value pairs are specified, the operation will copy the metadata from the source blob or file to the destination blob. If one or more name-value pairs are specified, the destination blob is created with the specified metadata, and metadata is not copied from the source blob or file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more information. Default value is None.
      description: Optional. Specifies a user-defined name-value pair associated with the blob. If no name-value pairs are specified, the operation will copy the metadata from the source blob or file to the destination blob. If one or more name-value pairs are specified, the destination blob is created with the specified metadata, and metadata is not copied from the source blob or file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more information. Default value is None.
    - name: x-ms-lease-id
      value: "{{ x-ms-lease-id }}"
    - name: x-ms-blob-content-disposition
      value: "{{ x-ms-blob-content-disposition }}"
    - name: x-ms-encryption-key
      value: "{{ x-ms-encryption-key }}"
    - name: x-ms-encryption-key-sha256
      value: "{{ x-ms-encryption-key-sha256 }}"
    - name: x-ms-encryption-algorithm
      value: "{{ x-ms-encryption-algorithm }}"
    - name: x-ms-encryption-scope
      value: "{{ x-ms-encryption-scope }}"
    - name: If-Modified-Since
      value: "{{ If-Modified-Since }}"
    - name: If-Unmodified-Since
      value: "{{ If-Unmodified-Since }}"
    - name: If-Match
      value: "{{ If-Match }}"
    - name: If-None-Match
      value: "{{ If-None-Match }}"
    - name: x-ms-if-tags
      value: "{{ x-ms-if-tags }}"
    - name: x-ms-client-request-id
      value: "{{ x-ms-client-request-id }}"
      description: Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.
      description: Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.
    - name: x-ms-tags
      value: "{{ x-ms-tags }}"
      description: Optional. Used to set blob tags in various blob operations. Default value is None.
      description: Optional. Used to set blob tags in various blob operations. Default value is None.
    - name: x-ms-immutability-policy-until-date
      value: "{{ x-ms-immutability-policy-until-date }}"
      description: Specifies the date time when the blobs immutability policy is set to expire. Default value is None.
      description: Specifies the date time when the blobs immutability policy is set to expire. Default value is None.
    - name: x-ms-immutability-policy-mode
      value: "{{ x-ms-immutability-policy-mode }}"
      description: Specifies the immutability policy mode to set on the blob. Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.
      description: Specifies the immutability policy mode to set on the blob. Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.
    - name: x-ms-legal-hold
      value: {{ x-ms-legal-hold }}
      description: Specified if a legal hold should be set on the blob. Default value is None.
      description: Specified if a legal hold should be set on the blob. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>
