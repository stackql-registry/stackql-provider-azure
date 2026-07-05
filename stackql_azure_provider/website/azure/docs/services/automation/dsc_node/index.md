--- 
title: dsc_node
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node
  - automation
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

Creates, updates, deletes, gets or lists a <code>dsc_node</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dsc_node" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_node" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
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
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the account id of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the etag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionHandler" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of extensionHandler properties for a Node.</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ip of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSeen" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last seen time of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeConfiguration" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the configuration of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the node id.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the registration time of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalCount" /></td>
    <td><code>integer</code></td>
    <td>Gets the total number of records matching filter criteria.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_automation_account">

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
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the account id of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the etag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionHandler" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of extensionHandler properties for a Node.</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ip of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSeen" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last seen time of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeConfiguration" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the configuration of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the node id.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the registration time of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalCount" /></td>
    <td><code>integer</code></td>
    <td>Gets the total number of records matching filter criteria.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the dsc node identified by node id.</td>
</tr>
<tr>
    <td><a href="#list_by_automation_account"><CopyableCode code="list_by_automation_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$inlinecount"><code>$inlinecount</code></a></td>
    <td>Retrieve a list of dsc nodes.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the dsc node.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the dsc node identified by node id.</td>
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
<tr id="parameter-automation_account_name">
    <td><CopyableCode code="automation_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the automation account. Required.</td>
</tr>
<tr id="parameter-node_id">
    <td><CopyableCode code="node_id" /></td>
    <td><code>string</code></td>
    <td>The node id. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-$inlinecount">
    <td><CopyableCode code="$inlinecount" /></td>
    <td><code>string</code></td>
    <td>Return total rows. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of rows to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of rows to take. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
    ]}
>
<TabItem value="get">

Retrieve the dsc node identified by node id.

```sql
SELECT
id,
name,
accountId,
etag,
extensionHandler,
ip,
lastSeen,
nodeConfiguration,
nodeId,
registrationTime,
status,
systemData,
totalCount,
type
FROM azure.automation.dsc_node
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND node_id = '{{ node_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_automation_account">

Retrieve a list of dsc nodes.

```sql
SELECT
id,
name,
accountId,
etag,
extensionHandler,
ip,
lastSeen,
nodeConfiguration,
nodeId,
registrationTime,
status,
systemData,
totalCount,
type
FROM azure.automation.dsc_node
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
AND $inlinecount = '{{ $inlinecount }}'
;
```
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

Update the dsc node.

```sql
UPDATE azure.automation.dsc_node
SET 
nodeId = '{{ nodeId }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND node_id = '{{ node_id }}' --required
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

Delete the dsc node identified by node id.

```sql
DELETE FROM azure.automation.dsc_node
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND node_id = '{{ node_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
