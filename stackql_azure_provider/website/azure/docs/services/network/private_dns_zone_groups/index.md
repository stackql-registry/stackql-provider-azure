--- 
title: private_dns_zone_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - private_dns_zone_groups
  - network
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

Creates, updates, deletes, gets or lists a <code>private_dns_zone_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_dns_zone_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_dns_zone_groups" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="privateDnsZoneConfigs" /></td>
    <td><code>array</code></td>
    <td>A collection of private dns zone configurations of the private dns zone group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private dns zone group resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td>Name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="privateDnsZoneConfigs" /></td>
    <td><code>array</code></td>
    <td>A collection of private dns zone configurations of the private dns zone group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private dns zone group resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-private_dns_zone_group_name"><code>private_dns_zone_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the private dns zone group resource by specified private dns zone group name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all private dns zone groups in a private endpoint.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-private_dns_zone_group_name"><code>private_dns_zone_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a private dns zone group in the specified private endpoint.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-private_dns_zone_group_name"><code>private_dns_zone_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a private dns zone group in the specified private endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-private_dns_zone_group_name"><code>private_dns_zone_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified private dns zone group.</td>
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
<tr id="parameter-private_dns_zone_group_name">
    <td><CopyableCode code="private_dns_zone_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the private endpoint. Required.</td>
</tr>
<tr id="parameter-private_endpoint_name">
    <td><CopyableCode code="private_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the private endpoint. Required.</td>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the private dns zone group resource by specified private dns zone group name.

```sql
SELECT
id,
name,
etag,
privateDnsZoneConfigs,
provisioningState
FROM azure.network.private_dns_zone_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_endpoint_name = '{{ private_endpoint_name }}' -- required
AND private_dns_zone_group_name = '{{ private_dns_zone_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all private dns zone groups in a private endpoint.

```sql
SELECT
id,
name,
etag,
privateDnsZoneConfigs,
provisioningState
FROM azure.network.private_dns_zone_groups
WHERE private_endpoint_name = '{{ private_endpoint_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
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

Creates or updates a private dns zone group in the specified private endpoint.

```sql
INSERT INTO azure.network.private_dns_zone_groups (
id,
name,
properties,
resource_group_name,
private_endpoint_name,
private_dns_zone_group_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_endpoint_name }}',
'{{ private_dns_zone_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: private_dns_zone_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the private_dns_zone_groups resource.
    - name: private_endpoint_name
      value: "{{ private_endpoint_name }}"
      description: Required parameter for the private_dns_zone_groups resource.
    - name: private_dns_zone_group_name
      value: "{{ private_dns_zone_group_name }}"
      description: Required parameter for the private_dns_zone_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the private_dns_zone_groups resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the resource that is unique within a resource group. This name can be used to access the resource.
    - name: properties
      description: |
        Properties of the private dns zone group.
      value:
        provisioningState: "{{ provisioningState }}"
        privateDnsZoneConfigs:
          - name: "{{ name }}"
            properties:
              privateDnsZoneId: "{{ privateDnsZoneId }}"
              recordSets:
                - recordType: "{{ recordType }}"
                  recordSetName: "{{ recordSetName }}"
                  fqdn: "{{ fqdn }}"
                  provisioningState: "{{ provisioningState }}"
                  ttl: {{ ttl }}
                  ipAddresses: "{{ ipAddresses }}"
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

Creates or updates a private dns zone group in the specified private endpoint.

```sql
REPLACE azure.network.private_dns_zone_groups
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_endpoint_name = '{{ private_endpoint_name }}' --required
AND private_dns_zone_group_name = '{{ private_dns_zone_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties;
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

Deletes the specified private dns zone group.

```sql
DELETE FROM azure.network.private_dns_zone_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND private_endpoint_name = '{{ private_endpoint_name }}' --required
AND private_dns_zone_group_name = '{{ private_dns_zone_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
