--- 
title: premier_add_on_offers
hide_title: false
hide_table_of_contents: false
keywords:
  - premier_add_on_offers
  - web
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

Creates, updates, deletes, gets or lists a <code>premier_add_on_offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="premier_add_on_offers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.premier_add_on_offers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_premier_add_on_offers"
    values={[
        { label: 'list_premier_add_on_offers', value: 'list_premier_add_on_offers' }
    ]}
>
<TabItem value="list_premier_add_on_offers">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="legalTermsUrl" /></td>
    <td><code>string</code></td>
    <td>Legal terms URL.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceOffer" /></td>
    <td><code>string</code></td>
    <td>Marketplace offer.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplacePublisher" /></td>
    <td><code>string</code></td>
    <td>Marketplace publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyPolicyUrl" /></td>
    <td><code>string</code></td>
    <td>Privacy policy URL.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Premier add on offer Product.</td>
</tr>
<tr>
    <td><CopyableCode code="promoCodeRequired" /></td>
    <td><code>boolean</code></td>
    <td>true if promotion code is required; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="quota" /></td>
    <td><code>integer</code></td>
    <td>Premier add on offer Quota.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Premier add on SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="vendor" /></td>
    <td><code>string</code></td>
    <td>Premier add on offer Vendor.</td>
</tr>
<tr>
    <td><CopyableCode code="webHostingPlanRestrictions" /></td>
    <td><code>string</code></td>
    <td>App Service plans this offer is restricted to. Known values are: "None", "Free", "Shared", "Basic", "Standard", and "Premium". (None, Free, Shared, Basic, Standard, Premium)</td>
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
    <td><a href="#list_premier_add_on_offers"><CopyableCode code="list_premier_add_on_offers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all premier add-on offers. Description for List all premier add-on offers.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_premier_add_on_offers"
    values={[
        { label: 'list_premier_add_on_offers', value: 'list_premier_add_on_offers' }
    ]}
>
<TabItem value="list_premier_add_on_offers">

List all premier add-on offers. Description for List all premier add-on offers.

```sql
SELECT
id,
name,
kind,
legalTermsUrl,
marketplaceOffer,
marketplacePublisher,
privacyPolicyUrl,
product,
promoCodeRequired,
quota,
sku,
type,
vendor,
webHostingPlanRestrictions
FROM azure.web.premier_add_on_offers
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
