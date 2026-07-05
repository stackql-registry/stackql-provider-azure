--- 
title: private_link_scoped_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scoped_resources
  - monitor
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

Creates, updates, deletes, gets or lists a <code>private_link_scoped_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_link_scoped_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.private_link_scoped_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_private_link_scope', value: 'list_by_private_link_scope' }
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
    <td>The kind of scoped Azure monitor resource. Known values are: "Resource" and "Metrics". (Resource, Metrics)</td>
</tr>
<tr>
    <td><CopyableCode code="linkedResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the scoped Azure monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure monitor resource. Known values are: "Succeeded", "Provisioning", "Failed", and "Canceled". (Succeeded, Provisioning, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionLocation" /></td>
    <td><code>string</code></td>
    <td>The location of a scoped subscription. Only needs to be specified for metric dataplane subscriptions.</td>
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
<TabItem value="list_by_private_link_scope">

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
    <td>The kind of scoped Azure monitor resource. Known values are: "Resource" and "Metrics". (Resource, Metrics)</td>
</tr>
<tr>
    <td><CopyableCode code="linkedResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the scoped Azure monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure monitor resource. Known values are: "Succeeded", "Provisioning", "Failed", and "Canceled". (Succeeded, Provisioning, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionLocation" /></td>
    <td><code>string</code></td>
    <td>The location of a scoped subscription. Only needs to be specified for metric dataplane subscriptions.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a scoped resource in a private link scope.</td>
</tr>
<tr>
    <td><a href="#list_by_private_link_scope"><CopyableCode code="list_by_private_link_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-kind"><code>kind</code></a></td>
    <td>Gets all scoped resources on a private link scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add an Azure monitor scoped resource in the private link scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add an Azure monitor scoped resource in the private link scope.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Azure monitor scoped resource with a given name.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the scoped resource object. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-scope_name">
    <td><CopyableCode code="scope_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure Monitor PrivateLinkScope resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the private link resource. Not specifying a kind will return scoped resources of all kinds. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_private_link_scope', value: 'list_by_private_link_scope' }
    ]}
>
<TabItem value="get">

Gets a scoped resource in a private link scope.

```sql
SELECT
id,
name,
kind,
linkedResourceId,
provisioningState,
subscriptionLocation,
systemData,
type
FROM azure.monitor.private_link_scoped_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scope_name = '{{ scope_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_private_link_scope">

Gets all scoped resources on a private link scope.

```sql
SELECT
id,
name,
kind,
linkedResourceId,
provisioningState,
subscriptionLocation,
systemData,
type
FROM azure.monitor.private_link_scoped_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scope_name = '{{ scope_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND kind = '{{ kind }}'
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

Add an Azure monitor scoped resource in the private link scope.

```sql
INSERT INTO azure.monitor.private_link_scoped_resources (
properties,
resource_group_name,
scope_name,
name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ scope_name }}',
'{{ name }}',
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
- name: private_link_scoped_resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the private_link_scoped_resources resource.
    - name: scope_name
      value: "{{ scope_name }}"
      description: Required parameter for the private_link_scoped_resources resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the private_link_scoped_resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the private_link_scoped_resources resource.
    - name: properties
      description: |
        Resource properties.
      value:
        kind: "{{ kind }}"
        linkedResourceId: "{{ linkedResourceId }}"
        subscriptionLocation: "{{ subscriptionLocation }}"
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

Add an Azure monitor scoped resource in the private link scope.

```sql
REPLACE azure.monitor.private_link_scoped_resources
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND scope_name = '{{ scope_name }}' --required
AND name = '{{ name }}' --required
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

Deletes an Azure monitor scoped resource with a given name.

```sql
DELETE FROM azure.monitor.private_link_scoped_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND scope_name = '{{ scope_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
