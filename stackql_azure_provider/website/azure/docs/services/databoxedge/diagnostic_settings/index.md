--- 
title: diagnostic_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings
  - databoxedge
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

Creates, updates, deletes, gets or lists a <code>diagnostic_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="diagnostic_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databoxedge.diagnostic_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_diagnostic_proactive_log_collection_settings"
    values={[
        { label: 'get_diagnostic_proactive_log_collection_settings', value: 'get_diagnostic_proactive_log_collection_settings' }
    ]}
>
<TabItem value="get_diagnostic_proactive_log_collection_settings">

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
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userConsent" /></td>
    <td><code>string</code></td>
    <td>Proactive diagnostic collection consent flag. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
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
    <td><a href="#get_diagnostic_proactive_log_collection_settings"><CopyableCode code="get_diagnostic_proactive_log_collection_settings" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the proactive log collection settings of the specified Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#update_diagnostic_proactive_log_collection_settings"><CopyableCode code="update_diagnostic_proactive_log_collection_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Updates the proactive log collection settings on a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#get_diagnostic_remote_support_settings"><CopyableCode code="get_diagnostic_remote_support_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the diagnostic remote support settings of the specified Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#update_diagnostic_remote_support_settings"><CopyableCode code="update_diagnostic_remote_support_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Updates the diagnostic remote support settings on a Data Box Edge/Data Box Gateway device.</td>
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
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
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
    defaultValue="get_diagnostic_proactive_log_collection_settings"
    values={[
        { label: 'get_diagnostic_proactive_log_collection_settings', value: 'get_diagnostic_proactive_log_collection_settings' }
    ]}
>
<TabItem value="get_diagnostic_proactive_log_collection_settings">

Gets the proactive log collection settings of the specified Data Box Edge/Data Box Gateway device.

```sql
SELECT
id,
name,
systemData,
type,
userConsent
FROM azure.databoxedge.diagnostic_settings
WHERE device_name = '{{ device_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_diagnostic_proactive_log_collection_settings"
    values={[
        { label: 'update_diagnostic_proactive_log_collection_settings', value: 'update_diagnostic_proactive_log_collection_settings' },
        { label: 'get_diagnostic_remote_support_settings', value: 'get_diagnostic_remote_support_settings' },
        { label: 'update_diagnostic_remote_support_settings', value: 'update_diagnostic_remote_support_settings' }
    ]}
>
<TabItem value="update_diagnostic_proactive_log_collection_settings">

Updates the proactive log collection settings on a Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.diagnostic_settings.update_diagnostic_proactive_log_collection_settings 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_diagnostic_remote_support_settings">

Gets the diagnostic remote support settings of the specified Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.diagnostic_settings.get_diagnostic_remote_support_settings 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_diagnostic_remote_support_settings">

Updates the diagnostic remote support settings on a Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.diagnostic_settings.update_diagnostic_remote_support_settings 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
