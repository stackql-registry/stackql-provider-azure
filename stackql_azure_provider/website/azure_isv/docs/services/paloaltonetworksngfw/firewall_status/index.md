--- 
title: firewall_status
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_status
  - paloaltonetworksngfw
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>firewall_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewall_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworksngfw.firewall_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="healthReason" /></td>
    <td><code>string</code></td>
    <td>Detail description of current health of the Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Current status of the Firewall. Known values are: "GREEN", "YELLOW", "RED", and "INITIALIZING".</td>
</tr>
<tr>
    <td><CopyableCode code="isPanoramaManaged" /></td>
    <td><code>string</code></td>
    <td>Panorama Managed: Default is False. Default will be CloudSec managed. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="isStrataCloudManaged" /></td>
    <td><code>string</code></td>
    <td>Strata Cloud Manager. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="panoramaStatus" /></td>
    <td><code>object</code></td>
    <td>Panorama Status.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Deleted".</td>
</tr>
<tr>
    <td><CopyableCode code="strataCloudManagerInfo" /></td>
    <td><code>object</code></td>
    <td>This field is only present if Strata Cloud Manager is managing the policy for this firewall.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a FirewallStatusResource.</td>
</tr>
<tr>
    <td><a href="#list_by_firewalls"><CopyableCode code="list_by_firewalls" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FirewallStatusResource resources by Firewalls.</td>
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
<tr id="parameter-firewall_name">
    <td><CopyableCode code="firewall_name" /></td>
    <td><code>string</code></td>
    <td>Firewall resource name. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get a FirewallStatusResource.

```sql
SELECT
id,
name,
healthReason,
healthStatus,
isPanoramaManaged,
isStrataCloudManaged,
panoramaStatus,
provisioningState,
strataCloudManagerInfo,
systemData,
type
FROM azure_isv.paloaltonetworksngfw.firewall_status
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND firewall_name = '{{ firewall_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_firewalls"
    values={[
        { label: 'list_by_firewalls', value: 'list_by_firewalls' }
    ]}
>
<TabItem value="list_by_firewalls">

List FirewallStatusResource resources by Firewalls.

```sql
EXEC azure_isv.paloaltonetworksngfw.firewall_status.list_by_firewalls 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_name='{{ firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
