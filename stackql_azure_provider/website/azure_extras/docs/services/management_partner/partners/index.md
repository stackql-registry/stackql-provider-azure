--- 
title: partners
hide_title: false
hide_table_of_contents: false
keywords:
  - partners
  - management_partner
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

Creates, updates, deletes, gets or lists a <code>partners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="partners" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.management_partner.partners" /></td></tr>
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
    <td></td>
    <td></td>
    <td>Get a specific `Partner`. Get the management partner using the objectId and tenantId.</td>
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

Get a specific `Partner`. Get the management partner using the objectId and tenantId.

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
FROM azure_extras.management_partner.partners
;
```
</TabItem>
</Tabs>
