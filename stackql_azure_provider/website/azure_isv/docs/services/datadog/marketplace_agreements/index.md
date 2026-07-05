--- 
title: marketplace_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements
  - datadog
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.marketplace_agreements" /></td></tr>
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
    <td>ARM id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the agreement.</td>
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
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>Plan identifier string.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyPolicyLink" /></td>
    <td><code>string</code></td>
    <td>Link to the privacy policy of the publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product identifier string.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Publisher identifier string.</td>
</tr>
<tr>
    <td><CopyableCode code="retrieveDatetime" /></td>
    <td><code>string (date-time)</code></td>
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
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Datadog marketplace agreements in the subscription. List Datadog marketplace agreements in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Datadog marketplace agreement in the subscription. Create Datadog marketplace agreement in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Datadog marketplace agreement in the subscription. Create Datadog marketplace agreement in the subscription.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List Datadog marketplace agreements in the subscription. List Datadog marketplace agreements in the subscription.

```sql
SELECT
id,
name,
accepted,
licenseTextLink,
plan,
privacyPolicyLink,
product,
publisher,
retrieveDatetime,
signature,
systemData,
type
FROM azure_isv.datadog.marketplace_agreements
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

Create Datadog marketplace agreement in the subscription. Create Datadog marketplace agreement in the subscription.

```sql
INSERT INTO azure_isv.datadog.marketplace_agreements (
properties,
subscription_id
)
SELECT 
'{{ properties }}',
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
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the marketplace_agreements resource.
    - name: properties
      description: |
        Represents the properties of the resource.
      value:
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        plan: "{{ plan }}"
        licenseTextLink: "{{ licenseTextLink }}"
        privacyPolicyLink: "{{ privacyPolicyLink }}"
        retrieveDatetime: "{{ retrieveDatetime }}"
        signature: "{{ signature }}"
        accepted: {{ accepted }}
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

Create Datadog marketplace agreement in the subscription. Create Datadog marketplace agreement in the subscription.

```sql
REPLACE azure_isv.datadog.marketplace_agreements
SET 
properties = '{{ properties }}'
WHERE 
subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
