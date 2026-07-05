--- 
title: edge_action_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_action_versions
  - edgeactions
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

Creates, updates, deletes, gets or lists an <code>edge_action_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="edge_action_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.edgeactions.edge_action_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_edge_action', value: 'list_by_edge_action' }
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
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type. Required. Known values are: "zip", "file", and "others". (zip, file, others)</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultVersion" /></td>
    <td><code>string</code></td>
    <td>The active state. Required. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastPackageUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last update time in UTC for package update.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Upgrading". (Succeeded, Failed, Canceled, Provisioning, Upgrading)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationStatus" /></td>
    <td><code>string</code></td>
    <td>The validation status. Known values are: "Succeeded" and "Failed". (Succeeded, Failed)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_edge_action">

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
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type. Required. Known values are: "zip", "file", and "others". (zip, file, others)</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultVersion" /></td>
    <td><code>string</code></td>
    <td>The active state. Required. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastPackageUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last update time in UTC for package update.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Upgrading". (Succeeded, Failed, Canceled, Provisioning, Upgrading)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationStatus" /></td>
    <td><code>string</code></td>
    <td>The validation status. Known values are: "Succeeded" and "Failed". (Succeeded, Failed)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a EdgeActionVersion.</td>
</tr>
<tr>
    <td><a href="#list_by_edge_action"><CopyableCode code="list_by_edge_action" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List EdgeActionVersion resources by EdgeAction.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a EdgeActionVersion.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a EdgeActionVersion.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a EdgeActionVersion.</td>
</tr>
<tr>
    <td><a href="#get_version_code"><CopyableCode code="get_version_code" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the version code for the edge action version.</td>
</tr>
<tr>
    <td><a href="#deploy_version_code"><CopyableCode code="deploy_version_code" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-content"><code>content</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>A long-running resource action.</td>
</tr>
<tr>
    <td><a href="#swap_default"><CopyableCode code="swap_default" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_action_name"><code>edge_action_name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Swap the default version for the edge action.</td>
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
<tr id="parameter-edge_action_name">
    <td><CopyableCode code="edge_action_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Edge Action. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The name of the Edge Action version. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_edge_action', value: 'list_by_edge_action' }
    ]}
>
<TabItem value="get">

Get a EdgeActionVersion.

```sql
SELECT
id,
name,
deploymentType,
isDefaultVersion,
lastPackageUpdateTime,
location,
provisioningState,
systemData,
tags,
type,
validationStatus
FROM azure.edgeactions.edge_action_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND edge_action_name = '{{ edge_action_name }}' -- required
AND version = '{{ version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_edge_action">

List EdgeActionVersion resources by EdgeAction.

```sql
SELECT
id,
name,
deploymentType,
isDefaultVersion,
lastPackageUpdateTime,
location,
provisioningState,
systemData,
tags,
type,
validationStatus
FROM azure.edgeactions.edge_action_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND edge_action_name = '{{ edge_action_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a EdgeActionVersion.

```sql
INSERT INTO azure.edgeactions.edge_action_versions (
tags,
location,
properties,
resource_group_name,
edge_action_name,
version,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ edge_action_name }}',
'{{ version }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: edge_action_versions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the edge_action_versions resource.
    - name: edge_action_name
      value: "{{ edge_action_name }}"
      description: Required parameter for the edge_action_versions resource.
    - name: version
      value: "{{ version }}"
      description: Required parameter for the edge_action_versions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the edge_action_versions resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        deploymentType: "{{ deploymentType }}"
        validationStatus: "{{ validationStatus }}"
        provisioningState: "{{ provisioningState }}"
        isDefaultVersion: "{{ isDefaultVersion }}"
        lastPackageUpdateTime: "{{ lastPackageUpdateTime }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a EdgeActionVersion.

```sql
UPDATE azure.edgeactions.edge_action_versions
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND edge_action_name = '{{ edge_action_name }}' --required
AND version = '{{ version }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Delete a EdgeActionVersion.

```sql
DELETE FROM azure.edgeactions.edge_action_versions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND edge_action_name = '{{ edge_action_name }}' --required
AND version = '{{ version }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_version_code"
    values={[
        { label: 'get_version_code', value: 'get_version_code' },
        { label: 'deploy_version_code', value: 'deploy_version_code' },
        { label: 'swap_default', value: 'swap_default' }
    ]}
>
<TabItem value="get_version_code">

Get the version code for the edge action version.

```sql
EXEC azure.edgeactions.edge_action_versions.get_version_code 
@resource_group_name='{{ resource_group_name }}' --required, 
@edge_action_name='{{ edge_action_name }}' --required, 
@version='{{ version }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="deploy_version_code">

A long-running resource action.

```sql
EXEC azure.edgeactions.edge_action_versions.deploy_version_code 
@resource_group_name='{{ resource_group_name }}' --required, 
@edge_action_name='{{ edge_action_name }}' --required, 
@version='{{ version }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"content": "{{ content }}", 
"name": "{{ name }}"
}'
;
```
</TabItem>
<TabItem value="swap_default">

Swap the default version for the edge action.

```sql
EXEC azure.edgeactions.edge_action_versions.swap_default 
@resource_group_name='{{ resource_group_name }}' --required, 
@edge_action_name='{{ edge_action_name }}' --required, 
@version='{{ version }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
