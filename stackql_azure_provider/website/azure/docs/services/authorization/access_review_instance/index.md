--- 
title: access_review_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instance
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

Creates, updates, deletes, gets or lists an <code>access_review_instance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_review_instance" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_instance" /></td></tr>
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
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>An action to stop an access review instance.</td>
</tr>
<tr>
    <td><a href="#reset_decisions"><CopyableCode code="reset_decisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>An action to reset all decisions for an access review instance.</td>
</tr>
<tr>
    <td><a href="#apply_decisions"><CopyableCode code="apply_decisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>An action to apply all decisions for an access review instance.</td>
</tr>
<tr>
    <td><a href="#send_reminders"><CopyableCode code="send_reminders" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>An action to send reminders for an access review instance.</td>
</tr>
<tr>
    <td><a href="#accept_recommendations"><CopyableCode code="accept_recommendations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>An action to accept recommendations for decision in an access review instance.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="stop"
    values={[
        { label: 'stop', value: 'stop' },
        { label: 'reset_decisions', value: 'reset_decisions' },
        { label: 'apply_decisions', value: 'apply_decisions' },
        { label: 'send_reminders', value: 'send_reminders' },
        { label: 'accept_recommendations', value: 'accept_recommendations' }
    ]}
>
<TabItem value="stop">

An action to stop an access review instance.

```sql
EXEC azure.authorization.access_review_instance.stop 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_decisions">

An action to reset all decisions for an access review instance.

```sql
EXEC azure.authorization.access_review_instance.reset_decisions 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="apply_decisions">

An action to apply all decisions for an access review instance.

```sql
EXEC azure.authorization.access_review_instance.apply_decisions 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="send_reminders">

An action to send reminders for an access review instance.

```sql
EXEC azure.authorization.access_review_instance.send_reminders 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="accept_recommendations">

An action to accept recommendations for decision in an access review instance.

```sql
EXEC azure.authorization.access_review_instance.accept_recommendations 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required
;
```
</TabItem>
</Tabs>
