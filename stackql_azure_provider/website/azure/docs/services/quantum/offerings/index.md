--- 
title: offerings
hide_title: false
hide_table_of_contents: false
keywords:
  - offerings
  - quantum
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

Creates, updates, deletes, gets or lists an <code>offerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="offerings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quantum.offerings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>Unique provider's id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Provider's display name.</td>
</tr>
<tr>
    <td><CopyableCode code="aad" /></td>
    <td><code>object</code></td>
    <td>Azure Active Directory info.</td>
</tr>
<tr>
    <td><CopyableCode code="company" /></td>
    <td><code>string</code></td>
    <td>Company name.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultEndpoint" /></td>
    <td><code>string</code></td>
    <td>Provider's default endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description about this provider.</td>
</tr>
<tr>
    <td><CopyableCode code="managedApplication" /></td>
    <td><code>object</code></td>
    <td>Provider's Managed-Application info.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingDimensions" /></td>
    <td><code>array</code></td>
    <td>The list of pricing dimensions from the provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerType" /></td>
    <td><code>string</code></td>
    <td>Provider type.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaDimensions" /></td>
    <td><code>array</code></td>
    <td>The list of quota dimensions from the provider.</td>
</tr>
<tr>
    <td><CopyableCode code="skus" /></td>
    <td><code>array</code></td>
    <td>The list of skus available from this provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targets" /></td>
    <td><code>array</code></td>
    <td>The list of targets available from this provider.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the list of all provider offerings available for the given location.</td>
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
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>Location. Required.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Returns the list of all provider offerings available for the given location.

```sql
SELECT
id,
name,
aad,
company,
defaultEndpoint,
description,
managedApplication,
pricingDimensions,
providerType,
quotaDimensions,
skus,
targets
FROM azure.quantum.offerings
WHERE location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
