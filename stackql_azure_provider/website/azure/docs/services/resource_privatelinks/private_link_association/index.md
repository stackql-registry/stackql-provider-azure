--- 
title: private_link_association
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_association
  - resource_privatelinks
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

Creates, updates, deletes, gets or lists a <code>private_link_association</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_link_association" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_privatelinks.private_link_association" /></td></tr>
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
    <td>The plaResourceID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The pla name.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLink" /></td>
    <td><code>string</code></td>
    <td>The rmpl Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the private link association.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantID" /></td>
    <td><code>string</code></td>
    <td>The TenantID.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The operation type.</td>
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
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>private link association information.</td>
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
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-pla_id"><code>pla_id</code></a></td>
    <td></td>
    <td>Get a single private link association.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Get a private link association for a management group scope.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-pla_id"><code>pla_id</code></a></td>
    <td></td>
    <td>Delete a PrivateLinkAssociation.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-pla_id"><code>pla_id</code></a></td>
    <td></td>
    <td>Create a PrivateLinkAssociation.</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The management group ID. Required.</td>
</tr>
<tr id="parameter-pla_id">
    <td><CopyableCode code="pla_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the PLA. Required.</td>
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

Get a single private link association.

```sql
SELECT
id,
name,
privateLink,
publicNetworkAccess,
scope,
tenantID,
type
FROM azure.resource_privatelinks.private_link_association
WHERE group_id = '{{ group_id }}' -- required
AND pla_id = '{{ pla_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a private link association for a management group scope.

```sql
SELECT
value
FROM azure.resource_privatelinks.private_link_association
WHERE group_id = '{{ group_id }}' -- required
;
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

Delete a PrivateLinkAssociation.

```sql
DELETE FROM azure.resource_privatelinks.private_link_association
WHERE group_id = '{{ group_id }}' --required
AND pla_id = '{{ pla_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' }
    ]}
>
<TabItem value="put">

Create a PrivateLinkAssociation.

```sql
EXEC azure.resource_privatelinks.private_link_association.put 
@group_id='{{ group_id }}' --required, 
@pla_id='{{ pla_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
