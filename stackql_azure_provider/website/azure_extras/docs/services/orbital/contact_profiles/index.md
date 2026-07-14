--- 
title: contact_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_profiles
  - orbital
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>contact_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="contact_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.orbital.contact_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="autoTrackingConfiguration" /></td>
    <td><code>string</code></td>
    <td>Auto-tracking configuration. Known values are: "disabled", "xBand", and "sBand".</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubUri" /></td>
    <td><code>string</code></td>
    <td>ARM resource identifier of the Event Hub used for telemetry. Requires granting Orbital Resource Provider the rights to send telemetry into the hub.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links of the Contact Profile. Describes RF links, modem processing, and IP endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Minimum viable elevation for the contact in decimal degrees. Used for listing the available contacts with a spacecraft at a given ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumViableContactDuration" /></td>
    <td><code>string</code></td>
    <td>Minimum viable contact duration in ISO 8601 format. Used for listing the available contacts with a spacecraft at a given ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Network configuration of customer virtual network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the resource's creation, deletion, or modification. Known values are: "creating", "succeeded", "failed", "canceled", "updating", and "deleting".</td>
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
    <td><CopyableCode code="thirdPartyConfigurations" /></td>
    <td><code>array</code></td>
    <td>Third-party mission configuration of the Contact Profile. Describes RF links, modem processing, and IP endpoints.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="autoTrackingConfiguration" /></td>
    <td><code>string</code></td>
    <td>Auto-tracking configuration. Known values are: "disabled", "xBand", and "sBand".</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubUri" /></td>
    <td><code>string</code></td>
    <td>ARM resource identifier of the Event Hub used for telemetry. Requires granting Orbital Resource Provider the rights to send telemetry into the hub.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links of the Contact Profile. Describes RF links, modem processing, and IP endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Minimum viable elevation for the contact in decimal degrees. Used for listing the available contacts with a spacecraft at a given ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumViableContactDuration" /></td>
    <td><code>string</code></td>
    <td>Minimum viable contact duration in ISO 8601 format. Used for listing the available contacts with a spacecraft at a given ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Network configuration of customer virtual network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the resource's creation, deletion, or modification. Known values are: "creating", "succeeded", "failed", "canceled", "updating", and "deleting".</td>
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
    <td><CopyableCode code="thirdPartyConfigurations" /></td>
    <td><code>array</code></td>
    <td>Third-party mission configuration of the Contact Profile. Describes RF links, modem processing, and IP endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="autoTrackingConfiguration" /></td>
    <td><code>string</code></td>
    <td>Auto-tracking configuration. Known values are: "disabled", "xBand", and "sBand".</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubUri" /></td>
    <td><code>string</code></td>
    <td>ARM resource identifier of the Event Hub used for telemetry. Requires granting Orbital Resource Provider the rights to send telemetry into the hub.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links of the Contact Profile. Describes RF links, modem processing, and IP endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Minimum viable elevation for the contact in decimal degrees. Used for listing the available contacts with a spacecraft at a given ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumViableContactDuration" /></td>
    <td><code>string</code></td>
    <td>Minimum viable contact duration in ISO 8601 format. Used for listing the available contacts with a spacecraft at a given ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Network configuration of customer virtual network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the resource's creation, deletion, or modification. Known values are: "creating", "succeeded", "failed", "canceled", "updating", and "deleting".</td>
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
    <td><CopyableCode code="thirdPartyConfigurations" /></td>
    <td><code>array</code></td>
    <td>Third-party mission configuration of the Contact Profile. Describes RF links, modem processing, and IP endpoints.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-contact_profile_name"><code>contact_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified contact Profile in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Returns list of contact profiles by Resource Group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Returns list of contact profiles by Subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-contact_profile_name"><code>contact_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-subnetId"><code>subnetId</code></a></td>
    <td></td>
    <td>Creates or updates a contact profile.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-contact_profile_name"><code>contact_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specified contact profile tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-contact_profile_name"><code>contact_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-subnetId"><code>subnetId</code></a></td>
    <td></td>
    <td>Creates or updates a contact profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-contact_profile_name"><code>contact_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specified contact profile resource.</td>
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
<tr id="parameter-contact_profile_name">
    <td><CopyableCode code="contact_profile_name" /></td>
    <td><code>string</code></td>
    <td>Contact Profile name. Required.</td>
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
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>An opaque string that the resource provider uses to skip over previously-returned results. This is used when a previous list operation call returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the specified contact Profile in a specified resource group.

```sql
SELECT
id,
name,
autoTrackingConfiguration,
eventHubUri,
links,
location,
minimumElevationDegrees,
minimumViableContactDuration,
networkConfiguration,
provisioningState,
systemData,
tags,
thirdPartyConfigurations,
type
FROM azure_extras.orbital.contact_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND contact_profile_name = '{{ contact_profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns list of contact profiles by Resource Group.

```sql
SELECT
id,
name,
autoTrackingConfiguration,
eventHubUri,
links,
location,
minimumElevationDegrees,
minimumViableContactDuration,
networkConfiguration,
provisioningState,
systemData,
tags,
thirdPartyConfigurations,
type
FROM azure_extras.orbital.contact_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Returns list of contact profiles by Subscription.

```sql
SELECT
id,
name,
autoTrackingConfiguration,
eventHubUri,
links,
location,
minimumElevationDegrees,
minimumViableContactDuration,
networkConfiguration,
provisioningState,
systemData,
tags,
thirdPartyConfigurations,
type
FROM azure_extras.orbital.contact_profiles
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
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

Creates or updates a contact profile.

```sql
INSERT INTO azure_extras.orbital.contact_profiles (
subnetId,
resource_group_name,
contact_profile_name,
subscription_id
)
SELECT 
'{{ subnetId }}' /* required */,
'{{ resource_group_name }}',
'{{ contact_profile_name }}',
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
- name: contact_profiles
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the contact_profiles resource.
    - name: contact_profile_name
      value: "{{ contact_profile_name }}"
      description: Required parameter for the contact_profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the contact_profiles resource.
    - name: subnetId
      value: "{{ subnetId }}"
      description: |
        ARM resource identifier of the subnet delegated to the Microsoft.Orbital/orbitalGateways. Needs to be at least a class C subnet, and should not have any IP created in it. Required.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates the specified contact profile tags.

```sql
UPDATE azure_extras.orbital.contact_profiles
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND contact_profile_name = '{{ contact_profile_name }}' --required
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

Creates or updates a contact profile.

```sql
REPLACE azure_extras.orbital.contact_profiles
SET 
subnetId = '{{ subnetId }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND contact_profile_name = '{{ contact_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND subnetId = '{{ subnetId }}' --required
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

Deletes a specified contact profile resource.

```sql
DELETE FROM azure_extras.orbital.contact_profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND contact_profile_name = '{{ contact_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
