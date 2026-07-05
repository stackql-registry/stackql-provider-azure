--- 
title: record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets
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

Creates, updates, deletes, gets or lists a <code>record_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="record_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.record_sets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_type', value: 'list_by_type' },
        { label: 'list_by_dns_zone', value: 'list_by_dns_zone' }
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
    <td>The ID of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="AAAARecords" /></td>
    <td><code>array</code></td>
    <td>The list of AAAA records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="ARecords" /></td>
    <td><code>array</code></td>
    <td>The list of A records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="CNAMERecord" /></td>
    <td><code>object</code></td>
    <td>The CNAME record in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="MXRecords" /></td>
    <td><code>array</code></td>
    <td>The list of MX records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="NSRecords" /></td>
    <td><code>array</code></td>
    <td>The list of NS records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="PTRRecords" /></td>
    <td><code>array</code></td>
    <td>The list of PTR records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="SOARecord" /></td>
    <td><code>object</code></td>
    <td>The SOA record in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="SRVRecords" /></td>
    <td><code>array</code></td>
    <td>The list of SRV records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="TTL" /></td>
    <td><code>integer</code></td>
    <td>The TTL (time-to-live) of the records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="TXTRecords" /></td>
    <td><code>array</code></td>
    <td>The list of TXT records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="caaRecords" /></td>
    <td><code>array</code></td>
    <td>The list of CAA records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata attached to the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>provisioning State of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>A reference to a another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the record set.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_type">

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
    <td>The ID of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="AAAARecords" /></td>
    <td><code>array</code></td>
    <td>The list of AAAA records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="ARecords" /></td>
    <td><code>array</code></td>
    <td>The list of A records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="CNAMERecord" /></td>
    <td><code>object</code></td>
    <td>The CNAME record in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="MXRecords" /></td>
    <td><code>array</code></td>
    <td>The list of MX records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="NSRecords" /></td>
    <td><code>array</code></td>
    <td>The list of NS records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="PTRRecords" /></td>
    <td><code>array</code></td>
    <td>The list of PTR records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="SOARecord" /></td>
    <td><code>object</code></td>
    <td>The SOA record in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="SRVRecords" /></td>
    <td><code>array</code></td>
    <td>The list of SRV records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="TTL" /></td>
    <td><code>integer</code></td>
    <td>The TTL (time-to-live) of the records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="TXTRecords" /></td>
    <td><code>array</code></td>
    <td>The list of TXT records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="caaRecords" /></td>
    <td><code>array</code></td>
    <td>The list of CAA records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata attached to the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>provisioning State of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>A reference to a another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the record set.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_dns_zone">

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
    <td>The ID of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="AAAARecords" /></td>
    <td><code>array</code></td>
    <td>The list of AAAA records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="ARecords" /></td>
    <td><code>array</code></td>
    <td>The list of A records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="CNAMERecord" /></td>
    <td><code>object</code></td>
    <td>The CNAME record in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="MXRecords" /></td>
    <td><code>array</code></td>
    <td>The list of MX records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="NSRecords" /></td>
    <td><code>array</code></td>
    <td>The list of NS records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="PTRRecords" /></td>
    <td><code>array</code></td>
    <td>The list of PTR records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="SOARecord" /></td>
    <td><code>object</code></td>
    <td>The SOA record in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="SRVRecords" /></td>
    <td><code>array</code></td>
    <td>The list of SRV records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="TTL" /></td>
    <td><code>integer</code></td>
    <td>The TTL (time-to-live) of the records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="TXTRecords" /></td>
    <td><code>array</code></td>
    <td>The list of TXT records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="caaRecords" /></td>
    <td><code>array</code></td>
    <td>The list of CAA records in the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata attached to the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>provisioning State of the record set.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>A reference to a another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the record set.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-relative_record_set_name"><code>relative_record_set_name</code></a>, <a href="#parameter-record_type"><code>record_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a record set.</td>
</tr>
<tr>
    <td><a href="#list_by_type"><CopyableCode code="list_by_type" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-record_type"><code>record_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$recordsetnamesuffix"><code>$recordsetnamesuffix</code></a></td>
    <td>Lists the record sets of a specified type in a DNS zone.</td>
</tr>
<tr>
    <td><a href="#list_by_dns_zone"><CopyableCode code="list_by_dns_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$recordsetnamesuffix"><code>$recordsetnamesuffix</code></a></td>
    <td>Lists all record sets in a DNS zone.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-relative_record_set_name"><code>relative_record_set_name</code></a>, <a href="#parameter-record_type"><code>record_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates or updates a record set within a DNS zone.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-relative_record_set_name"><code>relative_record_set_name</code></a>, <a href="#parameter-record_type"><code>record_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates a record set within a DNS zone.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-relative_record_set_name"><code>relative_record_set_name</code></a>, <a href="#parameter-record_type"><code>record_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates or updates a record set within a DNS zone.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-relative_record_set_name"><code>relative_record_set_name</code></a>, <a href="#parameter-record_type"><code>record_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes a record set from a DNS zone. This operation cannot be undone.</td>
</tr>
<tr>
    <td><a href="#list_all_by_dns_zone"><CopyableCode code="list_all_by_dns_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$recordsetnamesuffix"><code>$recordsetnamesuffix</code></a></td>
    <td>Lists all record sets in a DNS zone.</td>
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
<tr id="parameter-record_type">
    <td><CopyableCode code="record_type" /></td>
    <td><code>string</code></td>
    <td>The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted). Known values are: "A", "AAAA", "CAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", and "TXT". Required.</td>
</tr>
<tr id="parameter-relative_record_set_name">
    <td><CopyableCode code="relative_record_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the record set, relative to the name of the zone. Required.</td>
</tr>
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
<tr id="parameter-$recordsetnamesuffix">
    <td><CopyableCode code="$recordsetnamesuffix" /></td>
    <td><code>string</code></td>
    <td>The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .\ . Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of record sets to return. If not specified, returns up to 100 record sets. Default value is None.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The etag of the record set. Omit this value to always delete the current record set. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_type', value: 'list_by_type' },
        { label: 'list_by_dns_zone', value: 'list_by_dns_zone' }
    ]}
>
<TabItem value="get">

Gets a record set.

```sql
SELECT
id,
name,
AAAARecords,
ARecords,
CNAMERecord,
MXRecords,
NSRecords,
PTRRecords,
SOARecord,
SRVRecords,
TTL,
TXTRecords,
caaRecords,
etag,
fqdn,
metadata,
provisioningState,
targetResource,
type
FROM azure.dns.record_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND zone_name = '{{ zone_name }}' -- required
AND relative_record_set_name = '{{ relative_record_set_name }}' -- required
AND record_type = '{{ record_type }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_type">

Lists the record sets of a specified type in a DNS zone.

```sql
SELECT
id,
name,
AAAARecords,
ARecords,
CNAMERecord,
MXRecords,
NSRecords,
PTRRecords,
SOARecord,
SRVRecords,
TTL,
TXTRecords,
caaRecords,
etag,
fqdn,
metadata,
provisioningState,
targetResource,
type
FROM azure.dns.record_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND zone_name = '{{ zone_name }}' -- required
AND record_type = '{{ record_type }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $recordsetnamesuffix = '{{ $recordsetnamesuffix }}'
;
```
</TabItem>
<TabItem value="list_by_dns_zone">

Lists all record sets in a DNS zone.

```sql
SELECT
id,
name,
AAAARecords,
ARecords,
CNAMERecord,
MXRecords,
NSRecords,
PTRRecords,
SOARecord,
SRVRecords,
TTL,
TXTRecords,
caaRecords,
etag,
fqdn,
metadata,
provisioningState,
targetResource,
type
FROM azure.dns.record_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND zone_name = '{{ zone_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $recordsetnamesuffix = '{{ $recordsetnamesuffix }}'
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

Creates or updates a record set within a DNS zone.

```sql
INSERT INTO azure.dns.record_sets (
etag,
properties,
resource_group_name,
zone_name,
relative_record_set_name,
record_type,
subscription_id,
If-Match,
If-None-Match
)
SELECT 
'{{ etag }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ zone_name }}',
'{{ relative_record_set_name }}',
'{{ record_type }}',
'{{ subscription_id }}',
'{{ If-Match }}',
'{{ If-None-Match }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: record_sets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the record_sets resource.
    - name: zone_name
      value: "{{ zone_name }}"
      description: Required parameter for the record_sets resource.
    - name: relative_record_set_name
      value: "{{ relative_record_set_name }}"
      description: Required parameter for the record_sets resource.
    - name: record_type
      value: "{{ record_type }}"
      description: Required parameter for the record_sets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the record_sets resource.
    - name: etag
      value: "{{ etag }}"
      description: |
        The etag of the record set.
    - name: properties
      value:
        metadata: "{{ metadata }}"
        TTL: {{ TTL }}
        targetResource:
          id: "{{ id }}"
        ARecords:
          - ipv4Address: "{{ ipv4Address }}"
        AAAARecords:
          - ipv6Address: "{{ ipv6Address }}"
        MXRecords:
          - preference: {{ preference }}
            exchange: "{{ exchange }}"
        NSRecords:
          - nsdname: "{{ nsdname }}"
        PTRRecords:
          - ptrdname: "{{ ptrdname }}"
        SRVRecords:
          - priority: {{ priority }}
            weight: {{ weight }}
            port: {{ port }}
            target: "{{ target }}"
        TXTRecords:
          - value: "{{ value }}"
        CNAMERecord:
          cname: "{{ cname }}"
        SOARecord:
          host: "{{ host }}"
          email: "{{ email }}"
          serialNumber: {{ serialNumber }}
          refreshTime: {{ refreshTime }}
          retryTime: {{ retryTime }}
          expireTime: {{ expireTime }}
          minimumTTL: {{ minimumTTL }}
        caaRecords:
          - flags: {{ flags }}
            tag: "{{ tag }}"
            value: "{{ value }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. Default value is None.
      description: The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. Default value is None.
    - name: If-None-Match
      value: "{{ If-None-Match }}"
      description: Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored. Default value is None.
      description: Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored. Default value is None.
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

Updates a record set within a DNS zone.

```sql
UPDATE azure.dns.record_sets
SET 
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND zone_name = '{{ zone_name }}' --required
AND relative_record_set_name = '{{ relative_record_set_name }}' --required
AND record_type = '{{ record_type }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
properties,
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

Creates or updates a record set within a DNS zone.

```sql
REPLACE azure.dns.record_sets
SET 
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND zone_name = '{{ zone_name }}' --required
AND relative_record_set_name = '{{ relative_record_set_name }}' --required
AND record_type = '{{ record_type }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
AND If-None-Match = '{{ If-None-Match}}'
RETURNING
id,
name,
etag,
properties,
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

Deletes a record set from a DNS zone. This operation cannot be undone.

```sql
DELETE FROM azure.dns.record_sets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND zone_name = '{{ zone_name }}' --required
AND relative_record_set_name = '{{ relative_record_set_name }}' --required
AND record_type = '{{ record_type }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_all_by_dns_zone"
    values={[
        { label: 'list_all_by_dns_zone', value: 'list_all_by_dns_zone' }
    ]}
>
<TabItem value="list_all_by_dns_zone">

Lists all record sets in a DNS zone.

```sql
EXEC azure.dns.record_sets.list_all_by_dns_zone 
@resource_group_name='{{ resource_group_name }}' --required, 
@zone_name='{{ zone_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$top='{{ $top }}', 
@$recordsetnamesuffix='{{ $recordsetnamesuffix }}'
;
```
</TabItem>
</Tabs>
