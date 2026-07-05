--- 
title: suppressions
hide_title: false
hide_table_of_contents: false
keywords:
  - suppressions
  - advisor
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

Creates, updates, deletes, gets or lists a <code>suppressions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="suppressions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.advisor.suppressions" /></td></tr>
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
    <td>The resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the expiration time stamp.</td>
</tr>
<tr>
    <td><CopyableCode code="suppressionId" /></td>
    <td><code>string</code></td>
    <td>The GUID of the suppression.</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>string</code></td>
    <td>The duration for which the suppression is valid.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>The resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the expiration time stamp.</td>
</tr>
<tr>
    <td><CopyableCode code="suppressionId" /></td>
    <td><code>string</code></td>
    <td>The GUID of the suppression.</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>string</code></td>
    <td>The duration for which the suppression is valid.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-recommendation_id"><code>recommendation_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Obtains the details of a suppression.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Retrieves the list of snoozed or dismissed suppressions for a subscription. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-recommendation_id"><code>recommendation_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Enables the snoozed or dismissed attribute of a recommendation. The snoozed or dismissed attribute is referred to as a suppression. Use this API to create or update the snoozed or dismissed status of a recommendation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-recommendation_id"><code>recommendation_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Enables the activation of a snoozed or dismissed recommendation. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the suppression. Required.</td>
</tr>
<tr id="parameter-recommendation_id">
    <td><CopyableCode code="recommendation_id" /></td>
    <td><code>string</code></td>
    <td>The recommendation ID. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The page-continuation token to use with a paged version of this API. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of suppressions per page if a paged version of this API is being used. Default value is None.</td>
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

Obtains the details of a suppression.

```sql
SELECT
id,
name,
expirationTimeStamp,
suppressionId,
ttl,
type
FROM azure.advisor.suppressions
WHERE resource_uri = '{{ resource_uri }}' -- required
AND recommendation_id = '{{ recommendation_id }}' -- required
AND name = '{{ name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves the list of snoozed or dismissed suppressions for a subscription. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

```sql
SELECT
id,
name,
expirationTimeStamp,
suppressionId,
ttl,
type
FROM azure.advisor.suppressions
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Enables the snoozed or dismissed attribute of a recommendation. The snoozed or dismissed attribute is referred to as a suppression. Use this API to create or update the snoozed or dismissed status of a recommendation.

```sql
INSERT INTO azure.advisor.suppressions (
properties,
resource_uri,
recommendation_id,
name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ recommendation_id }}',
'{{ name }}'
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
- name: suppressions
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the suppressions resource.
    - name: recommendation_id
      value: "{{ recommendation_id }}"
      description: Required parameter for the suppressions resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the suppressions resource.
    - name: properties
      value:
        suppressionId: "{{ suppressionId }}"
        ttl: "{{ ttl }}"
`}</CodeBlock>

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

Enables the activation of a snoozed or dismissed recommendation. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

```sql
DELETE FROM azure.advisor.suppressions
WHERE resource_uri = '{{ resource_uri }}' --required
AND recommendation_id = '{{ recommendation_id }}' --required
AND name = '{{ name }}' --required
;
```
</TabItem>
</Tabs>
