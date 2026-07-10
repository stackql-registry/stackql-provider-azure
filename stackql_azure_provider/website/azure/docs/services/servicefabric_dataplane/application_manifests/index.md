--- 
title: application_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - application_manifests
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists an <code>application_manifests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_manifests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.application_manifests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_application_manifest"
    values={[
        { label: 'get_application_manifest', value: 'get_application_manifest' }
    ]}
>
<TabItem value="get_application_manifest">

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
    <td><CopyableCode code="Manifest" /></td>
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
    <td><a href="#get_application_manifest"><CopyableCode code="get_application_manifest" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ApplicationTypeVersion"><code>ApplicationTypeVersion</code></a>, <a href="#parameter-application_type_name"><code>application_type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the manifest describing an application type. The response contains the application manifest XML as a string.</td>
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
<tr id="parameter-ApplicationTypeVersion">
    <td><CopyableCode code="ApplicationTypeVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the application type.</td>
</tr>
<tr id="parameter-application_type_name">
    <td><CopyableCode code="application_type_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application type.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_application_manifest"
    values={[
        { label: 'get_application_manifest', value: 'get_application_manifest' }
    ]}
>
<TabItem value="get_application_manifest">

Gets the manifest describing an application type. The response contains the application manifest XML as a string.

```sql
SELECT
Manifest
FROM azure.servicefabric_dataplane.application_manifests
WHERE ApplicationTypeVersion = '{{ ApplicationTypeVersion }}' -- required
AND application_type_name = '{{ application_type_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
