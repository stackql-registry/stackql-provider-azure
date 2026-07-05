--- 
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - dns
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

Creates, updates, deletes, gets or lists a <code>zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zones" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.zones" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfRecordSets" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of record sets that can be created in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfRecordsPerRecordSet" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of records per record set that can be created in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="nameServers" /></td>
    <td><code>array</code></td>
    <td>The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfRecordSets" /></td>
    <td><code>integer</code></td>
    <td>The current number of record sets in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationVirtualNetworks" /></td>
    <td><code>array</code></td>
    <td>A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.</td>
</tr>
<tr>
    <td><CopyableCode code="resolutionVirtualNetworks" /></td>
    <td><code>array</code></td>
    <td>A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneType" /></td>
    <td><code>string</code></td>
    <td>The type of this DNS zone (Public or Private). Known values are: "Public" and "Private".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfRecordSets" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of record sets that can be created in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfRecordsPerRecordSet" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of records per record set that can be created in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="nameServers" /></td>
    <td><code>array</code></td>
    <td>The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfRecordSets" /></td>
    <td><code>integer</code></td>
    <td>The current number of record sets in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationVirtualNetworks" /></td>
    <td><code>array</code></td>
    <td>A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.</td>
</tr>
<tr>
    <td><CopyableCode code="resolutionVirtualNetworks" /></td>
    <td><code>array</code></td>
    <td>A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneType" /></td>
    <td><code>string</code></td>
    <td>The type of this DNS zone (Public or Private). Known values are: "Public" and "Private".</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfRecordSets" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of record sets that can be created in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfRecordsPerRecordSet" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of records per record set that can be created in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="nameServers" /></td>
    <td><code>array</code></td>
    <td>The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfRecordSets" /></td>
    <td><code>integer</code></td>
    <td>The current number of record sets in this DNS zone. This is a read-only property and any attempt to set this value will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationVirtualNetworks" /></td>
    <td><code>array</code></td>
    <td>A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.</td>
</tr>
<tr>
    <td><CopyableCode code="resolutionVirtualNetworks" /></td>
    <td><code>array</code></td>
    <td>A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneType" /></td>
    <td><code>string</code></td>
    <td>The type of this DNS zone (Public or Private). Known values are: "Public" and "Private".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the DNS zones within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the DNS zones in all resource groups in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates or updates a DNS zone. Does not modify DNS records within the zone.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates a DNS zone. Does not modify DNS records within the zone.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates or updates a DNS zone. Does not modify DNS records within the zone.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone.</td>
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
    <td>The name of the resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_name">
    <td><CopyableCode code="zone_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DNS zone (without a terminating dot). Required.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of DNS zones to return. If not specified, returns up to 100 zones. Default value is None.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The etag of the DNS zone. Omit this value to always delete the current zone. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>Set to '*' to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone.

```sql
SELECT
id,
name,
etag,
location,
maxNumberOfRecordSets,
maxNumberOfRecordsPerRecordSet,
nameServers,
numberOfRecordSets,
registrationVirtualNetworks,
resolutionVirtualNetworks,
tags,
type,
zoneType
FROM azure.dns.zones
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND zone_name = '{{ zone_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the DNS zones within a resource group.

```sql
SELECT
id,
name,
etag,
location,
maxNumberOfRecordSets,
maxNumberOfRecordsPerRecordSet,
nameServers,
numberOfRecordSets,
registrationVirtualNetworks,
resolutionVirtualNetworks,
tags,
type,
zoneType
FROM azure.dns.zones
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list">

Lists the DNS zones in all resource groups in a subscription.

```sql
SELECT
id,
name,
etag,
location,
maxNumberOfRecordSets,
maxNumberOfRecordsPerRecordSet,
nameServers,
numberOfRecordSets,
registrationVirtualNetworks,
resolutionVirtualNetworks,
tags,
type,
zoneType
FROM azure.dns.zones
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
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

Creates or updates a DNS zone. Does not modify DNS records within the zone.

```sql
INSERT INTO azure.dns.zones (
location,
tags,
etag,
properties,
resource_group_name,
zone_name,
subscription_id,
If-Match,
If-None-Match
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ etag }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ zone_name }}',
'{{ subscription_id }}',
'{{ If-Match }}',
'{{ If-None-Match }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: zones
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the zones resource.
    - name: zone_name
      value: "{{ zone_name }}"
      description: Required parameter for the zones resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the zones resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: etag
      value: "{{ etag }}"
      description: |
        The etag of the zone.
    - name: properties
      value:
        zoneType: "{{ zoneType }}"
        registrationVirtualNetworks:
          - id: "{{ id }}"
        resolutionVirtualNetworks:
          - id: "{{ id }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. Default value is None.
      description: The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. Default value is None.
    - name: If-None-Match
      value: "{{ If-None-Match }}"
      description: Set to '*' to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored. Default value is None.
      description: Set to '*' to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored. Default value is None.
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

Updates a DNS zone. Does not modify DNS records within the zone.

```sql
UPDATE azure.dns.zones
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND zone_name = '{{ zone_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
location,
properties,
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

Creates or updates a DNS zone. Does not modify DNS records within the zone.

```sql
REPLACE azure.dns.zones
SET 
location = '{{ location }}',
tags = '{{ tags }}',
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND zone_name = '{{ zone_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND If-Match = '{{ If-Match}}'
AND If-None-Match = '{{ If-None-Match}}'
RETURNING
id,
name,
etag,
location,
properties,
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

Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone.

```sql
DELETE FROM azure.dns.zones
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND zone_name = '{{ zone_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
