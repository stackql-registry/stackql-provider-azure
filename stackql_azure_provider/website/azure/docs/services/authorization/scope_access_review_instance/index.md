--- 
title: scope_access_review_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instance
  - authorization
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

Creates, updates, deletes, gets or lists a <code>scope_access_review_instance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scope_access_review_instance" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_instance" /></td></tr>
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
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>An action to stop an access review instance.</td>
</tr>
<tr>
    <td><a href="#record_all_decisions"><CopyableCode code="record_all_decisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>An action to approve/deny all decisions for a review with certain filters.</td>
</tr>
<tr>
    <td><a href="#reset_decisions"><CopyableCode code="reset_decisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>An action to reset all decisions for an access review instance.</td>
</tr>
<tr>
    <td><a href="#apply_decisions"><CopyableCode code="apply_decisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>An action to apply all decisions for an access review instance.</td>
</tr>
<tr>
    <td><a href="#send_reminders"><CopyableCode code="send_reminders" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>An action to send reminders for an access review instance.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the access review instance. Required.</td>
</tr>
<tr id="parameter-schedule_definition_id">
    <td><CopyableCode code="schedule_definition_id" /></td>
    <td><code>string</code></td>
    <td>The id of the access review schedule definition. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the resource. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="stop"
    values={[
        { label: 'stop', value: 'stop' },
        { label: 'record_all_decisions', value: 'record_all_decisions' },
        { label: 'reset_decisions', value: 'reset_decisions' },
        { label: 'apply_decisions', value: 'apply_decisions' },
        { label: 'send_reminders', value: 'send_reminders' }
    ]}
>
<TabItem value="stop">

An action to stop an access review instance.

```sql
EXEC azure.authorization.scope_access_review_instance.stop 
@scope='{{ scope }}' --required, 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required
;
```
</TabItem>
<TabItem value="record_all_decisions">

An action to approve/deny all decisions for a review with certain filters.

```sql
EXEC azure.authorization.scope_access_review_instance.record_all_decisions 
@scope='{{ scope }}' --required, 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required 
@@json=
'{
"decision": "{{ decision }}", 
"justification": "{{ justification }}"
}'
;
```
</TabItem>
<TabItem value="reset_decisions">

An action to reset all decisions for an access review instance.

```sql
EXEC azure.authorization.scope_access_review_instance.reset_decisions 
@scope='{{ scope }}' --required, 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required
;
```
</TabItem>
<TabItem value="apply_decisions">

An action to apply all decisions for an access review instance.

```sql
EXEC azure.authorization.scope_access_review_instance.apply_decisions 
@scope='{{ scope }}' --required, 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required
;
```
</TabItem>
<TabItem value="send_reminders">

An action to send reminders for an access review instance.

```sql
EXEC azure.authorization.scope_access_review_instance.send_reminders 
@scope='{{ scope }}' --required, 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required
;
```
</TabItem>
</Tabs>
