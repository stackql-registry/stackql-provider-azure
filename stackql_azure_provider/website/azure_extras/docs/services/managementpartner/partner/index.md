--- 
title: partner
hide_title: false
hide_table_of_contents: false
keywords:
  - partner
  - managementpartner
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

Creates, updates, deletes, gets or lists a <code>partner</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="partner" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.managementpartner.partner" /></td></tr>
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
    <td>Identifier of the partner.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the partner.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the partner was created.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>Type of the partner.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>This is the object id.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerId" /></td>
    <td><code>string</code></td>
    <td>This is the partner id.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerName" /></td>
    <td><code>string</code></td>
    <td>This is the partner name.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>This is the partner state. Known values are: "Active" and "Deleted".</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>This is the tenant id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of resource. "Microsoft.ManagementPartner/partners".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the partner was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>This is the version.</td>
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
    <td><a href="#parameter-partner_id"><code>partner_id</code></a></td>
    <td></td>
    <td>Get a specific `Partner`. Get the management partner using the partnerId, objectId and tenantId.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-partner_id"><code>partner_id</code></a></td>
    <td></td>
    <td>Create a specific `Partner`. Create a management partner for the objectId and tenantId.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-partner_id"><code>partner_id</code></a></td>
    <td></td>
    <td>Update a specific `Partner`. Update the management partner for the objectId and tenantId.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-partner_id"><code>partner_id</code></a></td>
    <td></td>
    <td>Delete a specific `Partner`. Delete the management partner for the objectId and tenantId.</td>
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
<tr id="parameter-partner_id">
    <td><CopyableCode code="partner_id" /></td>
    <td><code>string</code></td>
    <td>Id of the Partner. Required.</td>
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

Get a specific `Partner`. Get the management partner using the partnerId, objectId and tenantId.

```sql
SELECT
id,
name,
createdTime,
etag,
objectId,
partnerId,
partnerName,
state,
tenantId,
type,
updatedTime,
version
FROM azure_extras.managementpartner.partner
WHERE partner_id = '{{ partner_id }}' -- required
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

Create a specific `Partner`. Create a management partner for the objectId and tenantId.

```sql
INSERT INTO azure_extras.managementpartner.partner (
partner_id
)
SELECT 
'{{ partner_id }}'
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
- name: partner
  props:
    - name: partner_id
      value: "{{ partner_id }}"
      description: Required parameter for the partner resource.
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

Update a specific `Partner`. Update the management partner for the objectId and tenantId.

```sql
UPDATE azure_extras.managementpartner.partner
SET 
-- No updatable properties
WHERE 
partner_id = '{{ partner_id }}' --required
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

Delete a specific `Partner`. Delete the management partner for the objectId and tenantId.

```sql
DELETE FROM azure_extras.managementpartner.partner
WHERE partner_id = '{{ partner_id }}' --required
;
```
</TabItem>
</Tabs>
