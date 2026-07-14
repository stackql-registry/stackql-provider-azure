--- 
title: edge_device_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_device_jobs
  - azure_stack_hci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>edge_device_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="edge_device_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.edge_device_jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_edge_device', value: 'list_by_edge_device' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. "HCI"</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_edge_device">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. "HCI"</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-edge_device_name"><code>edge_device_name</code></a></td>
    <td></td>
    <td>Get a EdgeDeviceJob.</td>
</tr>
<tr>
    <td><a href="#list_by_edge_device"><CopyableCode code="list_by_edge_device" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-edge_device_name"><code>edge_device_name</code></a></td>
    <td></td>
    <td>List EdgeDeviceJob resources by EdgeDevice.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-edge_device_name"><code>edge_device_name</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create a EdgeDeviceJob.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-edge_device_name"><code>edge_device_name</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create a EdgeDeviceJob.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-edge_device_name"><code>edge_device_name</code></a></td>
    <td></td>
    <td>Delete a EdgeDeviceJob.</td>
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
<tr id="parameter-edge_device_name">
    <td><CopyableCode code="edge_device_name" /></td>
    <td><code>string</code></td>
    <td>Name of Device. Default value is "default".</td>
</tr>
<tr id="parameter-jobs_name">
    <td><CopyableCode code="jobs_name" /></td>
    <td><code>string</code></td>
    <td>Name of EdgeDevice Job. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_edge_device', value: 'list_by_edge_device' }
    ]}
>
<TabItem value="get">

Get a EdgeDeviceJob.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure_stack.azure_stack_hci.edge_device_jobs
WHERE resource_uri = '{{ resource_uri }}' -- required
AND jobs_name = '{{ jobs_name }}' -- required
AND edge_device_name = '{{ edge_device_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_edge_device">

List EdgeDeviceJob resources by EdgeDevice.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure_stack.azure_stack_hci.edge_device_jobs
WHERE resource_uri = '{{ resource_uri }}' -- required
AND edge_device_name = '{{ edge_device_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create a EdgeDeviceJob.

```sql
INSERT INTO azure_stack.azure_stack_hci.edge_device_jobs (
kind,
resource_uri,
jobs_name,
edge_device_name
)
SELECT 
'{{ kind }}' /* required */,
'{{ resource_uri }}',
'{{ jobs_name }}',
'{{ edge_device_name }}'
RETURNING
id,
name,
kind,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: edge_device_jobs
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the edge_device_jobs resource.
    - name: jobs_name
      value: "{{ jobs_name }}"
      description: Required parameter for the edge_device_jobs resource.
    - name: edge_device_name
      value: "{{ edge_device_name }}"
      description: Required parameter for the edge_device_jobs resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. "HCI"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a EdgeDeviceJob.

```sql
REPLACE azure_stack.azure_stack_hci.edge_device_jobs
SET 
kind = '{{ kind }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND jobs_name = '{{ jobs_name }}' --required
AND edge_device_name = '{{ edge_device_name }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
kind,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a EdgeDeviceJob.

```sql
DELETE FROM azure_stack.azure_stack_hci.edge_device_jobs
WHERE resource_uri = '{{ resource_uri }}' --required
AND jobs_name = '{{ jobs_name }}' --required
AND edge_device_name = '{{ edge_device_name }}' --required
;
```
</TabItem>
</Tabs>
