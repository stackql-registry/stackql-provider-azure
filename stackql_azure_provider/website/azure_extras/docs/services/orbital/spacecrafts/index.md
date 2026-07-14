--- 
title: spacecrafts
hide_title: false
hide_table_of_contents: false
keywords:
  - spacecrafts
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

Creates, updates, deletes, gets or lists a <code>spacecrafts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="spacecrafts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.orbital.spacecrafts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_available_contacts"
    values={[
        { label: 'list_available_contacts', value: 'list_available_contacts' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_available_contacts">

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
    <td><CopyableCode code="endAzimuthDegrees" /></td>
    <td><code>number</code></td>
    <td>Azimuth of the antenna at the end of the contact in decimal degrees.</td>
</tr>
<tr>
    <td><CopyableCode code="endElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Spacecraft elevation above the horizon at contact end.</td>
</tr>
<tr>
    <td><CopyableCode code="groundStationName" /></td>
    <td><code>string</code></td>
    <td>Name of Azure Ground Station.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Maximum elevation of the antenna during the contact in decimal degrees.</td>
</tr>
<tr>
    <td><CopyableCode code="rxEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time to lost receiving a signal (ISO 8601 UTC standard).</td>
</tr>
<tr>
    <td><CopyableCode code="rxStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Earliest time to receive a signal (ISO 8601 UTC standard).</td>
</tr>
<tr>
    <td><CopyableCode code="spacecraft" /></td>
    <td><code>object</code></td>
    <td>The reference to the spacecraft resource.</td>
</tr>
<tr>
    <td><CopyableCode code="startAzimuthDegrees" /></td>
    <td><code>number</code></td>
    <td>Azimuth of the antenna at the start of the contact in decimal degrees.</td>
</tr>
<tr>
    <td><CopyableCode code="startElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Spacecraft elevation above the horizon at contact start.</td>
</tr>
<tr>
    <td><CopyableCode code="txEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which antenna transmit will be disabled (ISO 8601 UTC standard).</td>
</tr>
<tr>
    <td><CopyableCode code="txStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which antenna transmit will be enabled (ISO 8601 UTC standard).</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Immutable list of Spacecraft links. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="noradId" /></td>
    <td><code>string</code></td>
    <td>NORAD ID of the spacecraft.</td>
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
    <td><CopyableCode code="titleLine" /></td>
    <td><code>string</code></td>
    <td>Title line of the two-line element set (TLE). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tleLine1" /></td>
    <td><code>string</code></td>
    <td>Line 1 of the two-line element set (TLE). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tleLine2" /></td>
    <td><code>string</code></td>
    <td>Line 2 of the two-line element set (TLE). Required.</td>
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
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Immutable list of Spacecraft links. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="noradId" /></td>
    <td><code>string</code></td>
    <td>NORAD ID of the spacecraft.</td>
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
    <td><CopyableCode code="titleLine" /></td>
    <td><code>string</code></td>
    <td>Title line of the two-line element set (TLE). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tleLine1" /></td>
    <td><code>string</code></td>
    <td>Line 1 of the two-line element set (TLE). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tleLine2" /></td>
    <td><code>string</code></td>
    <td>Line 2 of the two-line element set (TLE). Required.</td>
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
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Immutable list of Spacecraft links. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="noradId" /></td>
    <td><code>string</code></td>
    <td>NORAD ID of the spacecraft.</td>
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
    <td><CopyableCode code="titleLine" /></td>
    <td><code>string</code></td>
    <td>Title line of the two-line element set (TLE). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tleLine1" /></td>
    <td><code>string</code></td>
    <td>Line 1 of the two-line element set (TLE). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tleLine2" /></td>
    <td><code>string</code></td>
    <td>Line 2 of the two-line element set (TLE). Required.</td>
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
    <td><a href="#list_available_contacts"><CopyableCode code="list_available_contacts" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns list of available contacts. A contact is available if the spacecraft is visible from the ground station for more than the minimum viable contact duration provided in the contact profile.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified spacecraft in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Returns list of spacecrafts by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Returns list of spacecrafts by subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-centerFrequencyMHz"><code>centerFrequencyMHz</code></a>, <a href="#parameter-bandwidthMHz"><code>bandwidthMHz</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-polarization"><code>polarization</code></a></td>
    <td></td>
    <td>Creates or updates a spacecraft resource.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specified spacecraft tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-centerFrequencyMHz"><code>centerFrequencyMHz</code></a>, <a href="#parameter-bandwidthMHz"><code>bandwidthMHz</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-polarization"><code>polarization</code></a></td>
    <td></td>
    <td>Creates or updates a spacecraft resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specified spacecraft resource.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-spacecraft_name">
    <td><CopyableCode code="spacecraft_name" /></td>
    <td><code>string</code></td>
    <td>Spacecraft ID. Required.</td>
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
    defaultValue="list_available_contacts"
    values={[
        { label: 'list_available_contacts', value: 'list_available_contacts' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_available_contacts">

Returns list of available contacts. A contact is available if the spacecraft is visible from the ground station for more than the minimum viable contact duration provided in the contact profile.

```sql
SELECT
endAzimuthDegrees,
endElevationDegrees,
groundStationName,
maximumElevationDegrees,
rxEndTime,
rxStartTime,
spacecraft,
startAzimuthDegrees,
startElevationDegrees,
txEndTime,
txStartTime
FROM azure_extras.orbital.spacecrafts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND spacecraft_name = '{{ spacecraft_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the specified spacecraft in a specified resource group.

```sql
SELECT
id,
name,
links,
location,
noradId,
provisioningState,
systemData,
tags,
titleLine,
tleLine1,
tleLine2,
type
FROM azure_extras.orbital.spacecrafts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND spacecraft_name = '{{ spacecraft_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns list of spacecrafts by resource group.

```sql
SELECT
id,
name,
links,
location,
noradId,
provisioningState,
systemData,
tags,
titleLine,
tleLine1,
tleLine2,
type
FROM azure_extras.orbital.spacecrafts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Returns list of spacecrafts by subscription.

```sql
SELECT
id,
name,
links,
location,
noradId,
provisioningState,
systemData,
tags,
titleLine,
tleLine1,
tleLine2,
type
FROM azure_extras.orbital.spacecrafts
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

Creates or updates a spacecraft resource.

```sql
INSERT INTO azure_extras.orbital.spacecrafts (
name,
centerFrequencyMHz,
bandwidthMHz,
direction,
polarization,
resource_group_name,
spacecraft_name,
subscription_id
)
SELECT 
'{{ name }}' /* required */,
{{ centerFrequencyMHz }} /* required */,
{{ bandwidthMHz }} /* required */,
'{{ direction }}' /* required */,
'{{ polarization }}' /* required */,
'{{ resource_group_name }}',
'{{ spacecraft_name }}',
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
- name: spacecrafts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the spacecrafts resource.
    - name: spacecraft_name
      value: "{{ spacecraft_name }}"
      description: Required parameter for the spacecrafts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the spacecrafts resource.
    - name: name
      value: "{{ name }}"
      description: |
        Link name. Required.
    - name: centerFrequencyMHz
      value: {{ centerFrequencyMHz }}
      description: |
        Center Frequency in MHz. Required.
    - name: bandwidthMHz
      value: {{ bandwidthMHz }}
      description: |
        Bandwidth in MHz. Required.
    - name: direction
      value: "{{ direction }}"
      description: |
        Direction (Uplink or Downlink). Required. Known values are: "Uplink" and "Downlink".
    - name: polarization
      value: "{{ polarization }}"
      description: |
        Polarization. e.g. (RHCP, LHCP). Required. Known values are: "RHCP", "LHCP", "linearVertical", and "linearHorizontal".
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

Updates the specified spacecraft tags.

```sql
UPDATE azure_extras.orbital.spacecrafts
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND spacecraft_name = '{{ spacecraft_name }}' --required
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

Creates or updates a spacecraft resource.

```sql
REPLACE azure_extras.orbital.spacecrafts
SET 
name = '{{ name }}',
centerFrequencyMHz = {{ centerFrequencyMHz }},
bandwidthMHz = {{ bandwidthMHz }},
direction = '{{ direction }}',
polarization = '{{ polarization }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND spacecraft_name = '{{ spacecraft_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND name = '{{ name }}' --required
AND centerFrequencyMHz = '{{ centerFrequencyMHz }}' --required
AND bandwidthMHz = '{{ bandwidthMHz }}' --required
AND direction = '{{ direction }}' --required
AND polarization = '{{ polarization }}' --required
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

Deletes a specified spacecraft resource.

```sql
DELETE FROM azure_extras.orbital.spacecrafts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND spacecraft_name = '{{ spacecraft_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
