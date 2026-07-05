--- 
title: trigger_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger_runs
  - datafactory
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

Creates, updates, deletes, gets or lists a <code>trigger_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="trigger_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datafactory.trigger_runs" /></td></tr>
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
    <td><a href="#query_by_factory"><CopyableCode code="query_by_factory" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-lastUpdatedAfter"><code>lastUpdatedAfter</code></a>, <a href="#parameter-lastUpdatedBefore"><code>lastUpdatedBefore</code></a></td>
    <td></td>
    <td>Query trigger runs.</td>
</tr>
<tr>
    <td><a href="#rerun"><CopyableCode code="rerun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rerun single trigger instance by runId.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel a single trigger instance by runId.</td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The pipeline run identifier. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-trigger_name">
    <td><CopyableCode code="trigger_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="query_by_factory"
    values={[
        { label: 'query_by_factory', value: 'query_by_factory' },
        { label: 'rerun', value: 'rerun' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="query_by_factory">

Query trigger runs.

```sql
EXEC azure.datafactory.trigger_runs.query_by_factory 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"continuationToken": "{{ continuationToken }}", 
"lastUpdatedAfter": "{{ lastUpdatedAfter }}", 
"lastUpdatedBefore": "{{ lastUpdatedBefore }}", 
"filters": "{{ filters }}", 
"orderBy": "{{ orderBy }}"
}'
;
```
</TabItem>
<TabItem value="rerun">

Rerun single trigger instance by runId.

```sql
EXEC azure.datafactory.trigger_runs.rerun 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancel a single trigger instance by runId.

```sql
EXEC azure.datafactory.trigger_runs.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
