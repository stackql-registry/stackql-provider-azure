--- 
title: peer_asns
hide_title: false
hide_table_of_contents: false
keywords:
  - peer_asns
  - peering
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

Creates, updates, deletes, gets or lists a <code>peer_asns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="peer_asns" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.peer_asns" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>The ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="peerAsn" /></td>
    <td><code>integer</code></td>
    <td>The Autonomous System Number (ASN) of the peer.</td>
</tr>
<tr>
    <td><CopyableCode code="peerContactInfo" /></td>
    <td><code>object</code></td>
    <td>The contact information of the peer.</td>
</tr>
<tr>
    <td><CopyableCode code="peerName" /></td>
    <td><code>string</code></td>
    <td>The name of the peer.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="validationState" /></td>
    <td><code>string</code></td>
    <td>The validation state of the ASN associated with the peer. Known values are: "None", "Pending", "Approved", and "Failed".</td>
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
    <td>The ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="peerAsn" /></td>
    <td><code>integer</code></td>
    <td>The Autonomous System Number (ASN) of the peer.</td>
</tr>
<tr>
    <td><CopyableCode code="peerContactInfo" /></td>
    <td><code>object</code></td>
    <td>The contact information of the peer.</td>
</tr>
<tr>
    <td><CopyableCode code="peerName" /></td>
    <td><code>string</code></td>
    <td>The name of the peer.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="validationState" /></td>
    <td><code>string</code></td>
    <td>The validation state of the ASN associated with the peer. Known values are: "None", "Pending", "Approved", and "Failed".</td>
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
    <td><a href="#parameter-peer_asn_name"><code>peer_asn_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the peer ASN with the specified name under the given subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the peer ASNs under the given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-peer_asn_name"><code>peer_asn_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-peer_asn_name"><code>peer_asn_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-peer_asn_name"><code>peer_asn_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing peer ASN with the specified name under the given subscription.</td>
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
<tr id="parameter-peer_asn_name">
    <td><CopyableCode code="peer_asn_name" /></td>
    <td><code>string</code></td>
    <td>The peer ASN name. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the peer ASN with the specified name under the given subscription.

```sql
SELECT
id,
name,
peerAsn,
peerContactInfo,
peerName,
type,
validationState
FROM azure.peering.peer_asns
WHERE peer_asn_name = '{{ peer_asn_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all of the peer ASNs under the given subscription.

```sql
SELECT
id,
name,
peerAsn,
peerContactInfo,
peerName,
type,
validationState
FROM azure.peering.peer_asns
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription.

```sql
INSERT INTO azure.peering.peer_asns (
properties,
peer_asn_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ peer_asn_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: peer_asns
  props:
    - name: peer_asn_name
      value: "{{ peer_asn_name }}"
      description: Required parameter for the peer_asns resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the peer_asns resource.
    - name: properties
      value:
        peerAsn: {{ peerAsn }}
        peerContactInfo:
          emails:
            - "{{ emails }}"
          phone:
            - "{{ phone }}"
        peerName: "{{ peerName }}"
        validationState: "{{ validationState }}"
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

Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription.

```sql
REPLACE azure.peering.peer_asns
SET 
properties = '{{ properties }}'
WHERE 
peer_asn_name = '{{ peer_asn_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Deletes an existing peer ASN with the specified name under the given subscription.

```sql
DELETE FROM azure.peering.peer_asns
WHERE peer_asn_name = '{{ peer_asn_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
