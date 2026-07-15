--- 
title: upgrade_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - upgrade_histories
  - app_network
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

Creates, updates, deletes, gets or lists a <code>upgrade_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="upgrade_histories" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_network.upgrade_histories" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_app_link_member"
    values={[
        { label: 'list_by_app_link_member', value: 'list_by_app_link_member' }
    ]}
>
<TabItem value="list_by_app_link_member">

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
    <td><CopyableCode code="endTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>End timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="fromVersion" /></td>
    <td><code>string</code></td>
    <td>Version upgraded from. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedBy" /></td>
    <td><code>string</code></td>
    <td>Upgrade initiator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start timestamp. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="toVersion" /></td>
    <td><code>string</code></td>
    <td>Version upgraded to. Required.</td>
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
    <td><a href="#list_by_app_link_member"><CopyableCode code="list_by_app_link_member" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-app_link_name"><code>app_link_name</code></a>, <a href="#parameter-app_link_member_name"><code>app_link_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List UpgradeHistory resources by AppLinkMember.</td>
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
<tr id="parameter-app_link_member_name">
    <td><CopyableCode code="app_link_member_name" /></td>
    <td><code>string</code></td>
    <td>The name of the AppLinkMember. Required.</td>
</tr>
<tr id="parameter-app_link_name">
    <td><CopyableCode code="app_link_name" /></td>
    <td><code>string</code></td>
    <td>The name of the AppLink. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_app_link_member"
    values={[
        { label: 'list_by_app_link_member', value: 'list_by_app_link_member' }
    ]}
>
<TabItem value="list_by_app_link_member">

List UpgradeHistory resources by AppLinkMember.

```sql
SELECT
id,
name,
endTimestamp,
fromVersion,
initiatedBy,
provisioningState,
startTimestamp,
systemData,
toVersion,
type
FROM azure.app_network.upgrade_histories
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND app_link_name = '{{ app_link_name }}' -- required
AND app_link_member_name = '{{ app_link_member_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
