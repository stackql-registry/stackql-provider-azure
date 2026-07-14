--- 
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
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

Creates, updates, deletes, gets or lists a <code>contacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="contacts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.orbital.contacts" /></td></tr>
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
    <td><CopyableCode code="antennaConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration associated with the allocated antenna.</td>
</tr>
<tr>
    <td><CopyableCode code="contactProfile" /></td>
    <td><code>object</code></td>
    <td>The reference to the contact profile resource. Required.</td>
</tr>
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
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>Any error message while scheduling a contact.</td>
</tr>
<tr>
    <td><CopyableCode code="groundStationName" /></td>
    <td><code>string</code></td>
    <td>Azure Ground Station name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Maximum elevation of the antenna during the contact in decimal degrees.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the resource's creation, deletion, or modification. Known values are: "creating", "succeeded", "failed", "canceled", "updating", and "deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="reservationEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Reservation end time of a contact (ISO 8601 UTC standard). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Reservation start time of a contact (ISO 8601 UTC standard). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rxEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Receive end time of a contact (ISO 8601 UTC standard).</td>
</tr>
<tr>
    <td><CopyableCode code="rxStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Receive start time of a contact (ISO 8601 UTC standard).</td>
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
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of a contact. Known values are: "scheduled", "cancelled", "succeeded", "failed", and "providerCancelled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="txEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Transmit end time of a contact (ISO 8601 UTC standard).</td>
</tr>
<tr>
    <td><CopyableCode code="txStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Transmit start time of a contact (ISO 8601 UTC standard).</td>
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
    <td><CopyableCode code="antennaConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration associated with the allocated antenna.</td>
</tr>
<tr>
    <td><CopyableCode code="contactProfile" /></td>
    <td><code>object</code></td>
    <td>The reference to the contact profile resource. Required.</td>
</tr>
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
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>Any error message while scheduling a contact.</td>
</tr>
<tr>
    <td><CopyableCode code="groundStationName" /></td>
    <td><code>string</code></td>
    <td>Azure Ground Station name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumElevationDegrees" /></td>
    <td><code>number</code></td>
    <td>Maximum elevation of the antenna during the contact in decimal degrees.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the resource's creation, deletion, or modification. Known values are: "creating", "succeeded", "failed", "canceled", "updating", and "deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="reservationEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Reservation end time of a contact (ISO 8601 UTC standard). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Reservation start time of a contact (ISO 8601 UTC standard). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rxEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Receive end time of a contact (ISO 8601 UTC standard).</td>
</tr>
<tr>
    <td><CopyableCode code="rxStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Receive start time of a contact (ISO 8601 UTC standard).</td>
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
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of a contact. Known values are: "scheduled", "cancelled", "succeeded", "failed", and "providerCancelled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="txEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Transmit end time of a contact (ISO 8601 UTC standard).</td>
</tr>
<tr>
    <td><CopyableCode code="txStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Transmit start time of a contact (ISO 8601 UTC standard).</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-contact_name"><code>contact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified contact in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Returns list of contacts by spacecraftName.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-contact_name"><code>contact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a contact.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-spacecraft_name"><code>spacecraft_name</code></a>, <a href="#parameter-contact_name"><code>contact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specified contact.</td>
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
<tr id="parameter-contact_name">
    <td><CopyableCode code="contact_name" /></td>
    <td><code>string</code></td>
    <td>Contact name. Required.</td>
</tr>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified contact in a specified resource group.

```sql
SELECT
id,
name,
antennaConfiguration,
contactProfile,
endAzimuthDegrees,
endElevationDegrees,
errorMessage,
groundStationName,
maximumElevationDegrees,
provisioningState,
reservationEndTime,
reservationStartTime,
rxEndTime,
rxStartTime,
startAzimuthDegrees,
startElevationDegrees,
status,
systemData,
txEndTime,
txStartTime,
type
FROM azure_extras.orbital.contacts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND spacecraft_name = '{{ spacecraft_name }}' -- required
AND contact_name = '{{ contact_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns list of contacts by spacecraftName.

```sql
SELECT
id,
name,
antennaConfiguration,
contactProfile,
endAzimuthDegrees,
endElevationDegrees,
errorMessage,
groundStationName,
maximumElevationDegrees,
provisioningState,
reservationEndTime,
reservationStartTime,
rxEndTime,
rxStartTime,
startAzimuthDegrees,
startElevationDegrees,
status,
systemData,
txEndTime,
txStartTime,
type
FROM azure_extras.orbital.contacts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND spacecraft_name = '{{ spacecraft_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a contact.

```sql
INSERT INTO azure_extras.orbital.contacts (
properties,
resource_group_name,
spacecraft_name,
contact_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ spacecraft_name }}',
'{{ contact_name }}',
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
- name: contacts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the contacts resource.
    - name: spacecraft_name
      value: "{{ spacecraft_name }}"
      description: Required parameter for the contacts resource.
    - name: contact_name
      value: "{{ contact_name }}"
      description: Required parameter for the contacts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the contacts resource.
    - name: properties
      value:
        provisioningState: "{{ provisioningState }}"
        reservationStartTime: "{{ reservationStartTime }}"
        reservationEndTime: "{{ reservationEndTime }}"
        groundStationName: "{{ groundStationName }}"
        contactProfile:
          id: "{{ id }}"
`}</CodeBlock>

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

Deletes a specified contact.

```sql
DELETE FROM azure_extras.orbital.contacts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND spacecraft_name = '{{ spacecraft_name }}' --required
AND contact_name = '{{ contact_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
