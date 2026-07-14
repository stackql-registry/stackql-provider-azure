--- 
title: recommended_action_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended_action_sessions
  - rdbms
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

Creates, updates, deletes, gets or lists a <code>recommended_action_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recommended_action_sessions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.rdbms.recommended_action_sessions" /></td></tr>
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
    <td><a href="#create_recommended_action_session"><CopyableCode code="create_recommended_action_session" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-advisor_name"><code>advisor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-databaseName"><code>databaseName</code></a></td>
    <td></td>
    <td>Create recommendation action session for the advisor.</td>
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
<tr id="parameter-advisor_name">
    <td><CopyableCode code="advisor_name" /></td>
    <td><code>string</code></td>
    <td>The advisor name for recommendation action. Required.</td>
</tr>
<tr id="parameter-databaseName">
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
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
    defaultValue="create_recommended_action_session"
    values={[
        { label: 'create_recommended_action_session', value: 'create_recommended_action_session' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_recommended_action_session">

Create recommendation action session for the advisor.

```sql
INSERT INTO azure_extras.rdbms.recommended_action_sessions (
resource_group_name,
server_name,
advisor_name,
subscription_id,
databaseName
)
SELECT 
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ advisor_name }}',
'{{ subscription_id }}',
'{{ databaseName }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: recommended_action_sessions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the recommended_action_sessions resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the recommended_action_sessions resource.
    - name: advisor_name
      value: "{{ advisor_name }}"
      description: Required parameter for the recommended_action_sessions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the recommended_action_sessions resource.
    - name: databaseName
      value: "{{ databaseName }}"
      description: Required parameter for the recommended_action_sessions resource.
`}</CodeBlock>

</TabItem>
</Tabs>
