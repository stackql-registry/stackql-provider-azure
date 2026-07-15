--- 
title: marketplace_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements
  - marketplace_ordering
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

Creates, updates, deletes, gets or lists a <code>marketplace_agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="marketplace_agreements" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.marketplace_ordering.marketplace_agreements" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_agreement', value: 'get_agreement' },
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
    <td><CopyableCode code="accepted" /></td>
    <td><code>boolean</code></td>
    <td>If any version of the terms have been accepted, otherwise false.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseTextLink" /></td>
    <td><code>string</code></td>
    <td>Link to HTML with Microsoft and Publisher terms.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceTermsLink" /></td>
    <td><code>string</code></td>
    <td>Link to HTML with Azure Marketplace terms.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>Plan identifier string of image being deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyPolicyLink" /></td>
    <td><code>string</code></td>
    <td>Link to the privacy policy of the publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Offer identifier string of image being deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Publisher identifier string of image being deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="retrieveDatetime" /></td>
    <td><code>string</code></td>
    <td>Date and time in UTC of when the terms were accepted. This is empty if Accepted is false.</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>Terms signature.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_agreement">

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
    <td><CopyableCode code="cancelDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC of when the terms were cancelled. This is empty if state is active.</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>Offer identifier string of image being deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Publisher identifier string of image being deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="signDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC of when the terms were accepted. This is empty if state is cancelled.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Whether the agreement is active or cancelled. Known values are: "Active" and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><CopyableCode code="cancelDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC of when the terms were cancelled. This is empty if state is active.</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>Offer identifier string of image being deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Publisher identifier string of image being deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="signDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC of when the terms were accepted. This is empty if state is cancelled.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Whether the agreement is active or cancelled. Known values are: "Active" and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-offer_type"><code>offer_type</code></a>, <a href="#parameter-publisher_id"><code>publisher_id</code></a>, <a href="#parameter-offer_id"><code>offer_id</code></a>, <a href="#parameter-plan_id"><code>plan_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get marketplace terms.</td>
</tr>
<tr>
    <td><a href="#get_agreement"><CopyableCode code="get_agreement" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-publisher_id"><code>publisher_id</code></a>, <a href="#parameter-offer_id"><code>offer_id</code></a>, <a href="#parameter-plan_id"><code>plan_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get marketplace agreement.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List marketplace agreements in the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-offer_type"><code>offer_type</code></a>, <a href="#parameter-publisher_id"><code>publisher_id</code></a>, <a href="#parameter-offer_id"><code>offer_id</code></a>, <a href="#parameter-plan_id"><code>plan_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Save marketplace terms.</td>
</tr>
<tr>
    <td><a href="#sign"><CopyableCode code="sign" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-publisher_id"><code>publisher_id</code></a>, <a href="#parameter-offer_id"><code>offer_id</code></a>, <a href="#parameter-plan_id"><code>plan_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sign marketplace terms.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-publisher_id"><code>publisher_id</code></a>, <a href="#parameter-offer_id"><code>offer_id</code></a>, <a href="#parameter-plan_id"><code>plan_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel marketplace terms.</td>
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
<tr id="parameter-offer_id">
    <td><CopyableCode code="offer_id" /></td>
    <td><code>string</code></td>
    <td>Offer identifier string of image being deployed. Required.</td>
</tr>
<tr id="parameter-offer_type">
    <td><CopyableCode code="offer_type" /></td>
    <td><code>string</code></td>
    <td>Offer Type, currently only virtualmachine type is supported. "virtualmachine" Required.</td>
</tr>
<tr id="parameter-plan_id">
    <td><CopyableCode code="plan_id" /></td>
    <td><code>string</code></td>
    <td>Plan identifier string of image being deployed. Required.</td>
</tr>
<tr id="parameter-publisher_id">
    <td><CopyableCode code="publisher_id" /></td>
    <td><code>string</code></td>
    <td>Publisher identifier string of image being deployed. Required.</td>
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
        { label: 'get_agreement', value: 'get_agreement' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get marketplace terms.

```sql
SELECT
id,
name,
accepted,
licenseTextLink,
marketplaceTermsLink,
plan,
privacyPolicyLink,
product,
publisher,
retrieveDatetime,
signature,
systemData,
type
FROM azure.marketplace_ordering.marketplace_agreements
WHERE offer_type = '{{ offer_type }}' -- required
AND publisher_id = '{{ publisher_id }}' -- required
AND offer_id = '{{ offer_id }}' -- required
AND plan_id = '{{ plan_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_agreement">

Get marketplace agreement.

```sql
SELECT
id,
name,
cancelDate,
offer,
publisher,
signDate,
state,
type
FROM azure.marketplace_ordering.marketplace_agreements
WHERE publisher_id = '{{ publisher_id }}' -- required
AND offer_id = '{{ offer_id }}' -- required
AND plan_id = '{{ plan_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List marketplace agreements in the subscription.

```sql
SELECT
id,
name,
cancelDate,
offer,
publisher,
signDate,
state,
type
FROM azure.marketplace_ordering.marketplace_agreements
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Save marketplace terms.

```sql
INSERT INTO azure.marketplace_ordering.marketplace_agreements (
properties,
offer_type,
publisher_id,
offer_id,
plan_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ offer_type }}',
'{{ publisher_id }}',
'{{ offer_id }}',
'{{ plan_id }}',
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
- name: marketplace_agreements
  props:
    - name: offer_type
      value: "{{ offer_type }}"
      description: Required parameter for the marketplace_agreements resource.
    - name: publisher_id
      value: "{{ publisher_id }}"
      description: Required parameter for the marketplace_agreements resource.
    - name: offer_id
      value: "{{ offer_id }}"
      description: Required parameter for the marketplace_agreements resource.
    - name: plan_id
      value: "{{ plan_id }}"
      description: Required parameter for the marketplace_agreements resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the marketplace_agreements resource.
    - name: properties
      value:
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        plan: "{{ plan }}"
        licenseTextLink: "{{ licenseTextLink }}"
        privacyPolicyLink: "{{ privacyPolicyLink }}"
        marketplaceTermsLink: "{{ marketplaceTermsLink }}"
        retrieveDatetime: "{{ retrieveDatetime }}"
        signature: "{{ signature }}"
        accepted: {{ accepted }}
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="sign"
    values={[
        { label: 'sign', value: 'sign' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="sign">

Sign marketplace terms.

```sql
EXEC azure.marketplace_ordering.marketplace_agreements.sign 
@publisher_id='{{ publisher_id }}' --required, 
@offer_id='{{ offer_id }}' --required, 
@plan_id='{{ plan_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancel marketplace terms.

```sql
EXEC azure.marketplace_ordering.marketplace_agreements.cancel 
@publisher_id='{{ publisher_id }}' --required, 
@offer_id='{{ offer_id }}' --required, 
@plan_id='{{ plan_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
