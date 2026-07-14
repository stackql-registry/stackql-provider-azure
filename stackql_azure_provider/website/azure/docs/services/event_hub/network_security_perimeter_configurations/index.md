--- 
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - event_hub
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_security_perimeter_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hub.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-resource_association_name"><code>resource_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes any information about the association.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-resource_association_name"><code>resource_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes any information about the association.</td>
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
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The Namespace name. Required.</td>
</tr>
<tr id="parameter-resource_association_name">
    <td><CopyableCode code="resource_association_name" /></td>
    <td><code>string</code></td>
    <td>The ResourceAssociation Name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group within the azure subscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Refreshes any information about the association.

```sql
INSERT INTO azure.event_hub.network_security_perimeter_configurations (
resource_group_name,
namespace_name,
resource_association_name,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ resource_association_name }}',
'{{ subscription_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_security_perimeter_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_security_perimeter_configurations resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the network_security_perimeter_configurations resource.
    - name: resource_association_name
      value: "{{ resource_association_name }}"
      description: Required parameter for the network_security_perimeter_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_security_perimeter_configurations resource.
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

Refreshes any information about the association.

```sql
REPLACE azure.event_hub.network_security_perimeter_configurations
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND resource_association_name = '{{ resource_association_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required;
```
</TabItem>
</Tabs>
