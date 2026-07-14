--- 
title: resource_sync_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sync_rules
  - extended_location
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

Creates, updates, deletes, gets or lists a <code>resource_sync_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_sync_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.extended_location.resource_sync_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_custom_location_id', value: 'list_by_custom_location_id' }
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority represents a priority of the Resource Sync Rule.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State for the Resource Sync Rule.</td>
</tr>
<tr>
    <td><CopyableCode code="selector" /></td>
    <td><code>object</code></td>
    <td>A label selector is composed of two parts, matchLabels and matchExpressions. The first part, matchLabels is a map of &#123;key,value&#125; pairs. A single &#123;key,value&#125; in the matchLabels map is equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and the values array contains only 'value'. The second part, matchExpressions is a list of resource selector requirements. Valid operators include In, NotIn, Exists, and DoesNotExist. The values set must be non-empty in the case of In and NotIn. The values set must be empty in the case of Exists and DoesNotExist. All of the requirements, from both matchLabels and matchExpressions must all be satisfied in order to match.</td>
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
    <td><CopyableCode code="targetResourceGroup" /></td>
    <td><code>string</code></td>
    <td>For an unmapped custom resource, its labels will be used to find matching resource sync rules. If this resource sync rule is one of the matching rules with highest priority, then the unmapped custom resource will be projected to the target resource group associated with this resource sync rule. The user creating this resource sync rule should have write permissions on the target resource group and this write permission will be validated when creating the resource sync rule.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_custom_location_id">

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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority represents a priority of the Resource Sync Rule.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State for the Resource Sync Rule.</td>
</tr>
<tr>
    <td><CopyableCode code="selector" /></td>
    <td><code>object</code></td>
    <td>A label selector is composed of two parts, matchLabels and matchExpressions. The first part, matchLabels is a map of &#123;key,value&#125; pairs. A single &#123;key,value&#125; in the matchLabels map is equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and the values array contains only 'value'. The second part, matchExpressions is a list of resource selector requirements. Valid operators include In, NotIn, Exists, and DoesNotExist. The values set must be non-empty in the case of In and NotIn. The values set must be empty in the case of Exists and DoesNotExist. All of the requirements, from both matchLabels and matchExpressions must all be satisfied in order to match.</td>
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
    <td><CopyableCode code="targetResourceGroup" /></td>
    <td><code>string</code></td>
    <td>For an unmapped custom resource, its labels will be used to find matching resource sync rules. If this resource sync rule is one of the matching rules with highest priority, then the unmapped custom resource will be projected to the target resource group associated with this resource sync rule. The user creating this resource sync rule should have write permissions on the target resource group and this write permission will be validated when creating the resource sync rule.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-child_resource_name"><code>child_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Resource Sync Rule. Gets the details of the resourceSyncRule with a specified resource group, subscription id Custom Location resource name and Resource Sync Rule name.</td>
</tr>
<tr>
    <td><a href="#list_by_custom_location_id"><CopyableCode code="list_by_custom_location_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Resource Sync Rules in a Custom Location. Gets a list of Resource Sync Rules in the specified subscription. The operation returns properties of each Resource Sync Rule.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-child_resource_name"><code>child_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Resource Sync Rule. Creates or updates a Resource Sync Rule in the parent Custom Location, Subscription Id and Resource Group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-child_resource_name"><code>child_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a Resource Sync Rule. Updates a Resource Sync Rule with the specified Resource Sync Rule name in the specified Resource Group, Subscription and Custom Location name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-child_resource_name"><code>child_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Resource Sync Rule. Creates or updates a Resource Sync Rule in the parent Custom Location, Subscription Id and Resource Group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-child_resource_name"><code>child_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Resource Sync Rule. Deletes the Resource Sync Rule with the specified Resource Sync Rule Name, Custom Location Resource Name, Resource Group, and Subscription Id.</td>
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
<tr id="parameter-child_resource_name">
    <td><CopyableCode code="child_resource_name" /></td>
    <td><code>string</code></td>
    <td>Resource Sync Rule name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Custom Locations name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_custom_location_id', value: 'list_by_custom_location_id' }
    ]}
>
<TabItem value="get">

Gets a Resource Sync Rule. Gets the details of the resourceSyncRule with a specified resource group, subscription id Custom Location resource name and Resource Sync Rule name.

```sql
SELECT
id,
name,
location,
priority,
provisioningState,
selector,
systemData,
tags,
targetResourceGroup,
type
FROM azure.extended_location.resource_sync_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND child_resource_name = '{{ child_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_custom_location_id">

Lists all Resource Sync Rules in a Custom Location. Gets a list of Resource Sync Rules in the specified subscription. The operation returns properties of each Resource Sync Rule.

```sql
SELECT
id,
name,
location,
priority,
provisioningState,
selector,
systemData,
tags,
targetResourceGroup,
type
FROM azure.extended_location.resource_sync_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a Resource Sync Rule. Creates or updates a Resource Sync Rule in the parent Custom Location, Subscription Id and Resource Group.

```sql
INSERT INTO azure.extended_location.resource_sync_rules (
tags,
location,
properties,
resource_group_name,
resource_name,
child_resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ child_resource_name }}',
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
- name: resource_sync_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the resource_sync_rules resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the resource_sync_rules resource.
    - name: child_resource_name
      value: "{{ child_resource_name }}"
      description: Required parameter for the resource_sync_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the resource_sync_rules resource.
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
        The set of properties specific to a Resource Sync Rule.
      value:
        priority: {{ priority }}
        provisioningState: "{{ provisioningState }}"
        selector:
          matchExpressions:
            - key: "{{ key }}"
              operator: "{{ operator }}"
              values: "{{ values }}"
          matchLabels: "{{ matchLabels }}"
        targetResourceGroup: "{{ targetResourceGroup }}"
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

Updates a Resource Sync Rule. Updates a Resource Sync Rule with the specified Resource Sync Rule name in the specified Resource Group, Subscription and Custom Location name.

```sql
UPDATE azure.extended_location.resource_sync_rules
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND child_resource_name = '{{ child_resource_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a Resource Sync Rule. Creates or updates a Resource Sync Rule in the parent Custom Location, Subscription Id and Resource Group.

```sql
REPLACE azure.extended_location.resource_sync_rules
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND child_resource_name = '{{ child_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Deletes a Resource Sync Rule. Deletes the Resource Sync Rule with the specified Resource Sync Rule Name, Custom Location Resource Name, Resource Group, and Subscription Id.

```sql
DELETE FROM azure.extended_location.resource_sync_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND child_resource_name = '{{ child_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
