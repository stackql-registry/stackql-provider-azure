--- 
title: container_registry
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry
  - containerregistry_dataplane
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

Creates, updates, deletes, gets or lists a <code>container_registry</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_registry" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerregistry_dataplane.container_registry" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_manifest"
    values={[
        { label: 'get_manifest', value: 'get_manifest' },
        { label: 'get_manifest_properties', value: 'get_manifest_properties' },
        { label: 'get_properties', value: 'get_properties' },
        { label: 'get_repositories', value: 'get_repositories' }
    ]}
>
<TabItem value="get_manifest">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>(V1) Image name.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>object</code></td>
    <td>(OCI, OCIIndex) Additional metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="architecture" /></td>
    <td><code>string</code></td>
    <td>(V1) CPU architecture.</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>(V2, OCI) Image config descriptor.</td>
</tr>
<tr>
    <td><CopyableCode code="fsLayers" /></td>
    <td><code>array</code></td>
    <td>(V1) List of layer information.</td>
</tr>
<tr>
    <td><CopyableCode code="history" /></td>
    <td><code>array</code></td>
    <td>(V1) Image history.</td>
</tr>
<tr>
    <td><CopyableCode code="layers" /></td>
    <td><code>array</code></td>
    <td>(V2, OCI) List of V2 image layer information.</td>
</tr>
<tr>
    <td><CopyableCode code="manifests" /></td>
    <td><code>array</code></td>
    <td>(ManifestList, OCIIndex) List of V2 image layer information.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaType" /></td>
    <td><code>string</code></td>
    <td>Media type for this Manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaVersion" /></td>
    <td><code>integer</code></td>
    <td>Schema version.</td>
</tr>
<tr>
    <td><CopyableCode code="signatures" /></td>
    <td><code>array</code></td>
    <td>(V1) Image signature.</td>
</tr>
<tr>
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td>(V1) Image tag.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_manifest_properties">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="imageName" /></td>
    <td><code>string</code></td>
    <td>Repository name.</td>
</tr>
<tr>
    <td><CopyableCode code="manifest" /></td>
    <td><code>object</code></td>
    <td>Manifest details.</td>
</tr>
<tr>
    <td><CopyableCode code="registry" /></td>
    <td><code>string</code></td>
    <td>Registry login server name. This is likely to be similar to &#123;registry-name&#125;.azurecr.io.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_properties">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="changeableAttributes" /></td>
    <td><code>object</code></td>
    <td>Writeable properties of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Image created time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="imageName" /></td>
    <td><code>string</code></td>
    <td>Image name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Image last update time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="manifestCount" /></td>
    <td><code>integer</code></td>
    <td>Number of the manifests. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="registry" /></td>
    <td><code>string</code></td>
    <td>Registry login server name. This is likely to be similar to &#123;registry-name&#125;.azurecr.io. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tagCount" /></td>
    <td><code>integer</code></td>
    <td>Number of the tags. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_repositories">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

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
    <td><a href="#get_manifest"><CopyableCode code="get_manifest" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-reference"><code>reference</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the manifest identified by `name` and `reference` where `reference` can be a tag or digest.</td>
</tr>
<tr>
    <td><a href="#get_manifest_properties"><CopyableCode code="get_manifest_properties" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-digest"><code>digest</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get manifest attributes.</td>
</tr>
<tr>
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get repository attributes.</td>
</tr>
<tr>
    <td><a href="#get_repositories"><CopyableCode code="get_repositories" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-last"><code>last</code></a>, <a href="#parameter-n"><code>n</code></a></td>
    <td>List repositories.</td>
</tr>
<tr>
    <td><a href="#create_manifest"><CopyableCode code="create_manifest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-reference"><code>reference</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Put the manifest identified by `name` and `reference` where `reference` can be a tag or digest.</td>
</tr>
<tr>
    <td><a href="#delete_manifest"><CopyableCode code="delete_manifest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-reference"><code>reference</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the manifest identified by `name` and `reference`. Note that a manifest can *only* be deleted by `digest`.</td>
</tr>
<tr>
    <td><a href="#delete_repository"><CopyableCode code="delete_repository" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the repository identified by `name`.</td>
</tr>
<tr>
    <td><a href="#update_properties"><CopyableCode code="update_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the attribute identified by `name` where `reference` is the name of the repository.</td>
</tr>
<tr>
    <td><a href="#get_tags"><CopyableCode code="get_tags" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-last"><code>last</code></a>, <a href="#parameter-n"><code>n</code></a>, <a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-digest"><code>digest</code></a></td>
    <td>List tags of a repository.</td>
</tr>
<tr>
    <td><a href="#get_tag_properties"><CopyableCode code="get_tag_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-reference"><code>reference</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get tag attributes by tag.</td>
</tr>
<tr>
    <td><a href="#update_tag_attributes"><CopyableCode code="update_tag_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-reference"><code>reference</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update tag attributes.</td>
</tr>
<tr>
    <td><a href="#delete_tag"><CopyableCode code="delete_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-reference"><code>reference</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete tag.</td>
</tr>
<tr>
    <td><a href="#get_manifests"><CopyableCode code="get_manifests" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-last"><code>last</code></a>, <a href="#parameter-n"><code>n</code></a>, <a href="#parameter-orderby"><code>orderby</code></a></td>
    <td>List manifests of a repository.</td>
</tr>
<tr>
    <td><a href="#update_manifest_properties"><CopyableCode code="update_manifest_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-digest"><code>digest</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update properties of a manifest.</td>
</tr>
<tr>
    <td><a href="#check_docker_v2_support"><CopyableCode code="check_docker_v2_support" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Tells whether this Docker Registry instance supports Docker Registry HTTP API v2.</td>
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
<tr id="parameter-digest">
    <td><CopyableCode code="digest" /></td>
    <td><code>string</code></td>
    <td>Digest of a BLOB. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the image (including the namespace). Required.</td>
</tr>
<tr id="parameter-reference">
    <td><CopyableCode code="reference" /></td>
    <td><code>string</code></td>
    <td>Tag name. Required.</td>
</tr>
<tr id="parameter-digest">
    <td><CopyableCode code="digest" /></td>
    <td><code>string</code></td>
    <td>filter by digest. Default value is None.</td>
</tr>
<tr id="parameter-last">
    <td><CopyableCode code="last" /></td>
    <td><code>string</code></td>
    <td>Query parameter for the last item in previous query. Result set will include values lexically after last. Default value is None.</td>
</tr>
<tr id="parameter-n">
    <td><CopyableCode code="n" /></td>
    <td><code>integer</code></td>
    <td>query parameter for max number of items. Default value is None.</td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>string</code></td>
    <td>orderby query parameter. Known values are: "none", "timedesc", and "timeasc". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_manifest"
    values={[
        { label: 'get_manifest', value: 'get_manifest' },
        { label: 'get_manifest_properties', value: 'get_manifest_properties' },
        { label: 'get_properties', value: 'get_properties' },
        { label: 'get_repositories', value: 'get_repositories' }
    ]}
>
<TabItem value="get_manifest">

Get the manifest identified by `name` and `reference` where `reference` can be a tag or digest.

```sql
SELECT
name,
annotations,
architecture,
config,
fsLayers,
history,
layers,
manifests,
mediaType,
schemaVersion,
signatures,
tag
FROM azure.containerregistry_dataplane.container_registry
WHERE name = '{{ name }}' -- required
AND reference = '{{ reference }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_manifest_properties">

Get manifest attributes.

```sql
SELECT
imageName,
manifest,
registry
FROM azure.containerregistry_dataplane.container_registry
WHERE name = '{{ name }}' -- required
AND digest = '{{ digest }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_properties">

Get repository attributes.

```sql
SELECT
changeableAttributes,
createdTime,
imageName,
lastUpdateTime,
manifestCount,
registry,
tagCount
FROM azure.containerregistry_dataplane.container_registry
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_repositories">

List repositories.

```sql
SELECT
value
FROM azure.containerregistry_dataplane.container_registry
WHERE endpoint = '{{ endpoint }}' -- required
AND last = '{{ last }}'
AND n = '{{ n }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_manifest"
    values={[
        { label: 'create_manifest', value: 'create_manifest' },
        { label: 'delete_manifest', value: 'delete_manifest' },
        { label: 'delete_repository', value: 'delete_repository' },
        { label: 'update_properties', value: 'update_properties' },
        { label: 'get_tags', value: 'get_tags' },
        { label: 'get_tag_properties', value: 'get_tag_properties' },
        { label: 'update_tag_attributes', value: 'update_tag_attributes' },
        { label: 'delete_tag', value: 'delete_tag' },
        { label: 'get_manifests', value: 'get_manifests' },
        { label: 'update_manifest_properties', value: 'update_manifest_properties' },
        { label: 'check_docker_v2_support', value: 'check_docker_v2_support' }
    ]}
>
<TabItem value="create_manifest">

Put the manifest identified by `name` and `reference` where `reference` can be a tag or digest.

```sql
EXEC azure.containerregistry_dataplane.container_registry.create_manifest 
@name='{{ name }}' --required, 
@reference='{{ reference }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"schemaVersion": {{ schemaVersion }}
}'
;
```
</TabItem>
<TabItem value="delete_manifest">

Delete the manifest identified by `name` and `reference`. Note that a manifest can *only* be deleted by `digest`.

```sql
EXEC azure.containerregistry_dataplane.container_registry.delete_manifest 
@name='{{ name }}' --required, 
@reference='{{ reference }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_repository">

Delete the repository identified by `name`.

```sql
EXEC azure.containerregistry_dataplane.container_registry.delete_repository 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="update_properties">

Update the attribute identified by `name` where `reference` is the name of the repository.

```sql
EXEC azure.containerregistry_dataplane.container_registry.update_properties 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"deleteEnabled": {{ deleteEnabled }}, 
"writeEnabled": {{ writeEnabled }}, 
"listEnabled": {{ listEnabled }}, 
"readEnabled": {{ readEnabled }}
}'
;
```
</TabItem>
<TabItem value="get_tags">

List tags of a repository.

```sql
EXEC azure.containerregistry_dataplane.container_registry.get_tags 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@last='{{ last }}', 
@n='{{ n }}', 
@orderby='{{ orderby }}', 
@digest='{{ digest }}'
;
```
</TabItem>
<TabItem value="get_tag_properties">

Get tag attributes by tag.

```sql
EXEC azure.containerregistry_dataplane.container_registry.get_tag_properties 
@name='{{ name }}' --required, 
@reference='{{ reference }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="update_tag_attributes">

Update tag attributes.

```sql
EXEC azure.containerregistry_dataplane.container_registry.update_tag_attributes 
@name='{{ name }}' --required, 
@reference='{{ reference }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"deleteEnabled": {{ deleteEnabled }}, 
"writeEnabled": {{ writeEnabled }}, 
"listEnabled": {{ listEnabled }}, 
"readEnabled": {{ readEnabled }}
}'
;
```
</TabItem>
<TabItem value="delete_tag">

Delete tag.

```sql
EXEC azure.containerregistry_dataplane.container_registry.delete_tag 
@name='{{ name }}' --required, 
@reference='{{ reference }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_manifests">

List manifests of a repository.

```sql
EXEC azure.containerregistry_dataplane.container_registry.get_manifests 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@last='{{ last }}', 
@n='{{ n }}', 
@orderby='{{ orderby }}'
;
```
</TabItem>
<TabItem value="update_manifest_properties">

Update properties of a manifest.

```sql
EXEC azure.containerregistry_dataplane.container_registry.update_manifest_properties 
@name='{{ name }}' --required, 
@digest='{{ digest }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"deleteEnabled": {{ deleteEnabled }}, 
"writeEnabled": {{ writeEnabled }}, 
"listEnabled": {{ listEnabled }}, 
"readEnabled": {{ readEnabled }}
}'
;
```
</TabItem>
<TabItem value="check_docker_v2_support">

Tells whether this Docker Registry instance supports Docker Registry HTTP API v2.

```sql
EXEC azure.containerregistry_dataplane.container_registry.check_docker_v2_support 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
