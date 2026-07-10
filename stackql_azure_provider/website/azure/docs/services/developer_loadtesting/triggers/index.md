--- 
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - developer_loadtesting
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

Creates, updates, deletes, gets or lists a <code>triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="triggers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.triggers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_trigger"
    values={[
        { label: 'get_trigger', value: 'get_trigger' },
        { label: 'list_triggers', value: 'list_triggers' }
    ]}
>
<TabItem value="get_trigger">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the trigger.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the trigger. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The type of the trigger. Required. "ScheduleTestsTrigger"</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the trigger. Known values are: "Active", "Paused", "Completed", and "Disabled". (Active, Paused, Completed, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="stateDetails" /></td>
    <td><code>object</code></td>
    <td>Details of current state of the trigger.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the trigger. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_triggers">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the trigger.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the trigger. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The type of the trigger. Required. "ScheduleTestsTrigger"</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the trigger. Known values are: "Active", "Paused", "Completed", and "Disabled". (Active, Paused, Completed, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="stateDetails" /></td>
    <td><code>object</code></td>
    <td>Details of current state of the trigger.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the trigger. Required.</td>
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
    <td><a href="#get_trigger"><CopyableCode code="get_trigger" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-trigger_id"><code>trigger_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resource read operation template.</td>
</tr>
<tr>
    <td><a href="#list_triggers"><CopyableCode code="list_triggers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-testIds"><code>testIds</code></a>, <a href="#parameter-states"><code>states</code></a>, <a href="#parameter-lastModifiedStartTime"><code>lastModifiedStartTime</code></a>, <a href="#parameter-lastModifiedEndTime"><code>lastModifiedEndTime</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Resource list operation template.</td>
</tr>
<tr>
    <td><a href="#create_or_update_trigger"><CopyableCode code="create_or_update_trigger" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-trigger_id"><code>trigger_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create or update operation template.</td>
</tr>
<tr>
    <td><a href="#create_or_update_trigger"><CopyableCode code="create_or_update_trigger" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-trigger_id"><code>trigger_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create or update operation template.</td>
</tr>
<tr>
    <td><a href="#delete_trigger"><CopyableCode code="delete_trigger" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-trigger_id"><code>trigger_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resource delete operation template.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-trigger_id">
    <td><CopyableCode code="trigger_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the trigger. Required.</td>
</tr>
<tr id="parameter-lastModifiedEndTime">
    <td><CopyableCode code="lastModifiedEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime(RFC 3339 literal format) of the last updated time range to filter triggers. Default value is None.</td>
</tr>
<tr id="parameter-lastModifiedStartTime">
    <td><CopyableCode code="lastModifiedStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime(RFC 3339 literal format) of the last updated time range to filter triggers. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-states">
    <td><CopyableCode code="states" /></td>
    <td><code>string</code></td>
    <td>Filter triggers based on a comma separated list of states. Known values are: "Active", "Paused", "Completed", and "Disabled". Default value is None.</td>
</tr>
<tr id="parameter-testIds">
    <td><CopyableCode code="testIds" /></td>
    <td><code>string</code></td>
    <td>Search based on triggers associated with the provided test ids. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_trigger"
    values={[
        { label: 'get_trigger', value: 'get_trigger' },
        { label: 'list_triggers', value: 'list_triggers' }
    ]}
>
<TabItem value="get_trigger">

Resource read operation template.

```sql
SELECT
createdBy,
createdDateTime,
description,
displayName,
kind,
lastModifiedBy,
lastModifiedDateTime,
state,
stateDetails,
triggerId
FROM azure.developer_loadtesting.triggers
WHERE trigger_id = '{{ trigger_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_triggers">

Resource list operation template.

```sql
SELECT
createdBy,
createdDateTime,
description,
displayName,
kind,
lastModifiedBy,
lastModifiedDateTime,
state,
stateDetails,
triggerId
FROM azure.developer_loadtesting.triggers
WHERE endpoint = '{{ endpoint }}' -- required
AND testIds = '{{ testIds }}'
AND states = '{{ states }}'
AND lastModifiedStartTime = '{{ lastModifiedStartTime }}'
AND lastModifiedEndTime = '{{ lastModifiedEndTime }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_trigger"
    values={[
        { label: 'create_or_update_trigger', value: 'create_or_update_trigger' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_trigger">

Create or update operation template.

```sql
INSERT INTO azure.developer_loadtesting.triggers (
displayName,
description,
kind,
state,
trigger_id,
endpoint
)
SELECT 
'{{ displayName }}' /* required */,
'{{ description }}',
'{{ kind }}' /* required */,
'{{ state }}',
'{{ trigger_id }}',
'{{ endpoint }}'
RETURNING
createdBy,
createdDateTime,
description,
displayName,
kind,
lastModifiedBy,
lastModifiedDateTime,
state,
stateDetails,
triggerId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: triggers
  props:
    - name: trigger_id
      value: "{{ trigger_id }}"
      description: Required parameter for the triggers resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the triggers resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The name of the trigger. Required.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the trigger.
    - name: kind
      value: "{{ kind }}"
      description: |
        The type of the trigger. Required. "ScheduleTestsTrigger"
    - name: state
      value: "{{ state }}"
      description: |
        The current state of the trigger. Known values are: "Active", "Paused", "Completed", and "Disabled".
      valid_values: ['Active', 'Paused', 'Completed', 'Disabled']
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_trigger"
    values={[
        { label: 'create_or_update_trigger', value: 'create_or_update_trigger' }
    ]}
>
<TabItem value="create_or_update_trigger">

Create or update operation template.

```sql
REPLACE azure.developer_loadtesting.triggers
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
kind = '{{ kind }}',
state = '{{ state }}'
WHERE 
trigger_id = '{{ trigger_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND displayName = '{{ displayName }}' --required
AND kind = '{{ kind }}' --required
RETURNING
createdBy,
createdDateTime,
description,
displayName,
kind,
lastModifiedBy,
lastModifiedDateTime,
state,
stateDetails,
triggerId;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_trigger"
    values={[
        { label: 'delete_trigger', value: 'delete_trigger' }
    ]}
>
<TabItem value="delete_trigger">

Resource delete operation template.

```sql
DELETE FROM azure.developer_loadtesting.triggers
WHERE trigger_id = '{{ trigger_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
