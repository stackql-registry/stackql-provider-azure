--- 
title: web_pub_sub_replica_shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_replica_shared_private_link_resources
  - web_pubsub
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

Creates, updates, deletes, gets or lists a <code>web_pub_sub_replica_shared_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="web_pub_sub_replica_shared_private_link_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.web_pub_sub_replica_shared_private_link_resources" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The group id from the provider of resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving".</td>
</tr>
<tr>
    <td><CopyableCode code="requestMessage" /></td>
    <td><code>string</code></td>
    <td>The request message for requesting approval of the shared private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the shared private link resource. Known values are: "Pending", "Approved", "Rejected", "Disconnected", and "Timeout".</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The group id from the provider of resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving".</td>
</tr>
<tr>
    <td><CopyableCode code="requestMessage" /></td>
    <td><code>string</code></td>
    <td>The request message for requesting approval of the shared private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the shared private link resource. Known values are: "Pending", "Approved", "Rejected", "Disconnected", and "Timeout".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-replica_name"><code>replica_name</code></a>, <a href="#parameter-shared_private_link_resource_name"><code>shared_private_link_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified shared private link resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-replica_name"><code>replica_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List shared private link resources.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-replica_name"><code>replica_name</code></a>, <a href="#parameter-shared_private_link_resource_name"><code>shared_private_link_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a shared private link resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-replica_name"><code>replica_name</code></a>, <a href="#parameter-shared_private_link_resource_name"><code>shared_private_link_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a shared private link resource.</td>
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
<tr id="parameter-replica_name">
    <td><CopyableCode code="replica_name" /></td>
    <td><code>string</code></td>
    <td>The name of the replica. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr id="parameter-shared_private_link_resource_name">
    <td><CopyableCode code="shared_private_link_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the shared private link resource. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the specified shared private link resource.

```sql
SELECT
id,
name,
groupId,
privateLinkResourceId,
provisioningState,
requestMessage,
status,
systemData,
type
FROM azure.web_pubsub.web_pub_sub_replica_shared_private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND replica_name = '{{ replica_name }}' -- required
AND shared_private_link_resource_name = '{{ shared_private_link_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List shared private link resources.

```sql
SELECT
id,
name,
groupId,
privateLinkResourceId,
provisioningState,
requestMessage,
status,
systemData,
type
FROM azure.web_pubsub.web_pub_sub_replica_shared_private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND replica_name = '{{ replica_name }}' -- required
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

Create or update a shared private link resource.

```sql
INSERT INTO azure.web_pubsub.web_pub_sub_replica_shared_private_link_resources (
properties,
resource_group_name,
resource_name,
replica_name,
shared_private_link_resource_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ replica_name }}',
'{{ shared_private_link_resource_name }}',
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
- name: web_pub_sub_replica_shared_private_link_resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the web_pub_sub_replica_shared_private_link_resources resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the web_pub_sub_replica_shared_private_link_resources resource.
    - name: replica_name
      value: "{{ replica_name }}"
      description: Required parameter for the web_pub_sub_replica_shared_private_link_resources resource.
    - name: shared_private_link_resource_name
      value: "{{ shared_private_link_resource_name }}"
      description: Required parameter for the web_pub_sub_replica_shared_private_link_resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the web_pub_sub_replica_shared_private_link_resources resource.
    - name: properties
      value:
        groupId: "{{ groupId }}"
        privateLinkResourceId: "{{ privateLinkResourceId }}"
        requestMessage: "{{ requestMessage }}"
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

Create or update a shared private link resource.

```sql
REPLACE azure.web_pubsub.web_pub_sub_replica_shared_private_link_resources
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND replica_name = '{{ replica_name }}' --required
AND shared_private_link_resource_name = '{{ shared_private_link_resource_name }}' --required
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
