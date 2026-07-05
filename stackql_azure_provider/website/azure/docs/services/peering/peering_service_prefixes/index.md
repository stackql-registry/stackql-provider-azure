--- 
title: peering_service_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - peering_service_prefixes
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

Creates, updates, deletes, gets or lists a <code>peering_service_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="peering_service_prefixes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.peering_service_prefixes" /></td></tr>
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
    <td>The ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="learnedType" /></td>
    <td><code>string</code></td>
    <td>The prefix learned type. Known values are: "None", "ViaPartner", and "ViaSession".</td>
</tr>
<tr>
    <td><CopyableCode code="prefix" /></td>
    <td><code>string</code></td>
    <td>Valid route prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixValidationState" /></td>
    <td><code>string</code></td>
    <td>The prefix validation state. Known values are: "None", "Invalid", "Verified", "Failed", "Pending", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Updating", "Deleting", and "Failed".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_service_name"><code>peering_service_name</code></a>, <a href="#parameter-prefix_name"><code>prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the peering service prefix.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_service_name"><code>peering_service_name</code></a>, <a href="#parameter-prefix_name"><code>prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the peering prefix.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_service_name"><code>peering_service_name</code></a>, <a href="#parameter-prefix_name"><code>prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the peering prefix.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_service_name"><code>peering_service_name</code></a>, <a href="#parameter-prefix_name"><code>prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>removes the peering prefix.</td>
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
<tr id="parameter-peering_service_name">
    <td><CopyableCode code="peering_service_name" /></td>
    <td><code>string</code></td>
    <td>The peering service name. Required.</td>
</tr>
<tr id="parameter-prefix_name">
    <td><CopyableCode code="prefix_name" /></td>
    <td><code>string</code></td>
    <td>The prefix name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the peering service prefix.

```sql
SELECT
id,
name,
learnedType,
prefix,
prefixValidationState,
provisioningState,
type
FROM azure.peering.peering_service_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND peering_service_name = '{{ peering_service_name }}' -- required
AND prefix_name = '{{ prefix_name }}' -- required
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

Creates or updates the peering prefix.

```sql
INSERT INTO azure.peering.peering_service_prefixes (
properties,
resource_group_name,
peering_service_name,
prefix_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ peering_service_name }}',
'{{ prefix_name }}',
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
- name: peering_service_prefixes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the peering_service_prefixes resource.
    - name: peering_service_name
      value: "{{ peering_service_name }}"
      description: Required parameter for the peering_service_prefixes resource.
    - name: prefix_name
      value: "{{ prefix_name }}"
      description: Required parameter for the peering_service_prefixes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the peering_service_prefixes resource.
    - name: properties
      value:
        prefix: "{{ prefix }}"
        prefixValidationState: "{{ prefixValidationState }}"
        learnedType: "{{ learnedType }}"
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

Creates or updates the peering prefix.

```sql
REPLACE azure.peering.peering_service_prefixes
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND peering_service_name = '{{ peering_service_name }}' --required
AND prefix_name = '{{ prefix_name }}' --required
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

removes the peering prefix.

```sql
DELETE FROM azure.peering.peering_service_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND peering_service_name = '{{ peering_service_name }}' --required
AND prefix_name = '{{ prefix_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
