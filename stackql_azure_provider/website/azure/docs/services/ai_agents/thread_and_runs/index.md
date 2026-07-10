--- 
title: thread_and_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - thread_and_runs
  - ai_agents
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

Creates, updates, deletes, gets or lists a <code>thread_and_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="thread_and_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_agents.thread_and_runs" /></td></tr>
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
    <td><a href="#create_thread_and_run"><CopyableCode code="create_thread_and_run" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a new agent thread and immediately starts a run using that new thread.</td>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_thread_and_run"
    values={[
        { label: 'create_thread_and_run', value: 'create_thread_and_run' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_thread_and_run">

Creates a new agent thread and immediately starts a run using that new thread.

```sql
INSERT INTO azure.ai_agents.thread_and_runs (
endpoint
)
SELECT 
'{{ endpoint }}'
RETURNING
id,
assistant_id,
thread_id,
cancelled_at,
completed_at,
created_at,
expires_at,
failed_at,
incomplete_details,
instructions,
last_error,
max_completion_tokens,
max_prompt_tokens,
metadata,
model,
object,
parallel_tool_calls,
required_action,
response_format,
started_at,
status,
temperature,
tool_choice,
tool_resources,
tools,
top_p,
truncation_strategy,
usage
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: thread_and_runs
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the thread_and_runs resource.
`}</CodeBlock>

</TabItem>
</Tabs>
