--- 
title: capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - capabilities
  - chaos
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

Creates, updates, deletes, gets or lists a <code>capabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="capabilities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.chaos.capabilities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Localized string of the description.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersSchema" /></td>
    <td><code>string</code></td>
    <td>URL to retrieve JSON schema of the Capability parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provisioning state. Not currently in use because resource is created synchronously. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Running". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Running)</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>String of the Publisher that this Capability extends.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>String of the Target Type that this Capability extends.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="urn" /></td>
    <td><code>string</code></td>
    <td>String of the URN for this Capability Type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Localized string of the description.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersSchema" /></td>
    <td><code>string</code></td>
    <td>URL to retrieve JSON schema of the Capability parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provisioning state. Not currently in use because resource is created synchronously. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Running". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Running)</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>String of the Publisher that this Capability extends.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>String of the Target Type that this Capability extends.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="urn" /></td>
    <td><code>string</code></td>
    <td>String of the URN for this Capability Type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-parent_provider_namespace"><code>parent_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource_name"><code>parent_resource_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-capability_name"><code>capability_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Capability resource that extends a Target resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-parent_provider_namespace"><code>parent_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource_name"><code>parent_resource_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-continuationToken"><code>continuationToken</code></a></td>
    <td>Get a list of Capability resources that extend a Target resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-parent_provider_namespace"><code>parent_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource_name"><code>parent_resource_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-capability_name"><code>capability_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Capability resource that extends a Target resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-parent_provider_namespace"><code>parent_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource_name"><code>parent_resource_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-capability_name"><code>capability_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Capability resource that extends a Target resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-parent_provider_namespace"><code>parent_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource_name"><code>parent_resource_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-capability_name"><code>capability_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Capability that extends a Target resource.</td>
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
<tr id="parameter-capability_name">
    <td><CopyableCode code="capability_name" /></td>
    <td><code>string</code></td>
    <td>String that represents a Capability resource name. Required.</td>
</tr>
<tr id="parameter-parent_provider_namespace">
    <td><CopyableCode code="parent_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The parent resource provider namespace. Required.</td>
</tr>
<tr id="parameter-parent_resource_name">
    <td><CopyableCode code="parent_resource_name" /></td>
    <td><code>string</code></td>
    <td>The parent resource name. Required.</td>
</tr>
<tr id="parameter-parent_resource_type">
    <td><CopyableCode code="parent_resource_type" /></td>
    <td><code>string</code></td>
    <td>The parent resource type. Required.</td>
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
<tr id="parameter-target_name">
    <td><CopyableCode code="target_name" /></td>
    <td><code>string</code></td>
    <td>String that represents a Target resource name. Required.</td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>String that sets the continuation token. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a Capability resource that extends a Target resource.

```sql
SELECT
id,
name,
description,
parametersSchema,
provisioningState,
publisher,
systemData,
targetType,
type,
urn
FROM azure.chaos.capabilities
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND parent_provider_namespace = '{{ parent_provider_namespace }}' -- required
AND parent_resource_type = '{{ parent_resource_type }}' -- required
AND parent_resource_name = '{{ parent_resource_name }}' -- required
AND target_name = '{{ target_name }}' -- required
AND capability_name = '{{ capability_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of Capability resources that extend a Target resource.

```sql
SELECT
id,
name,
description,
parametersSchema,
provisioningState,
publisher,
systemData,
targetType,
type,
urn
FROM azure.chaos.capabilities
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND parent_provider_namespace = '{{ parent_provider_namespace }}' -- required
AND parent_resource_type = '{{ parent_resource_type }}' -- required
AND parent_resource_name = '{{ parent_resource_name }}' -- required
AND target_name = '{{ target_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND continuationToken = '{{ continuationToken }}'
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

Create or update a Capability resource that extends a Target resource.

```sql
INSERT INTO azure.chaos.capabilities (
properties,
resource_group_name,
parent_provider_namespace,
parent_resource_type,
parent_resource_name,
target_name,
capability_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ parent_provider_namespace }}',
'{{ parent_resource_type }}',
'{{ parent_resource_name }}',
'{{ target_name }}',
'{{ capability_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: capabilities
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the capabilities resource.
    - name: parent_provider_namespace
      value: "{{ parent_provider_namespace }}"
      description: Required parameter for the capabilities resource.
    - name: parent_resource_type
      value: "{{ parent_resource_type }}"
      description: Required parameter for the capabilities resource.
    - name: parent_resource_name
      value: "{{ parent_resource_name }}"
      description: Required parameter for the capabilities resource.
    - name: target_name
      value: "{{ target_name }}"
      description: Required parameter for the capabilities resource.
    - name: capability_name
      value: "{{ capability_name }}"
      description: Required parameter for the capabilities resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the capabilities resource.
    - name: properties
      description: |
        The properties of a capability resource.
      value:
        publisher: "{{ publisher }}"
        targetType: "{{ targetType }}"
        description: "{{ description }}"
        parametersSchema: "{{ parametersSchema }}"
        urn: "{{ urn }}"
        provisioningState: "{{ provisioningState }}"
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

Create or update a Capability resource that extends a Target resource.

```sql
REPLACE azure.chaos.capabilities
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND parent_provider_namespace = '{{ parent_provider_namespace }}' --required
AND parent_resource_type = '{{ parent_resource_type }}' --required
AND parent_resource_name = '{{ parent_resource_name }}' --required
AND target_name = '{{ target_name }}' --required
AND capability_name = '{{ capability_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
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

Delete a Capability that extends a Target resource.

```sql
DELETE FROM azure.chaos.capabilities
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND parent_provider_namespace = '{{ parent_provider_namespace }}' --required
AND parent_resource_type = '{{ parent_resource_type }}' --required
AND parent_resource_name = '{{ parent_resource_name }}' --required
AND target_name = '{{ target_name }}' --required
AND capability_name = '{{ capability_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
