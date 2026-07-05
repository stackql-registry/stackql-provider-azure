--- 
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
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

Creates, updates, deletes, gets or lists an <code>agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_agents.agents" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_agent"
    values={[
        { label: 'get_agent', value: 'get_agent' },
        { label: 'list_agents', value: 'list_agents' }
    ]}
>
<TabItem value="get_agent">

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
    <td>The identifier, which can be referenced in API endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this object was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="instructions" /></td>
    <td><code>string</code></td>
    <td>The system instructions for the agent to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A set of up to 16 key/value pairs that can be attached to an object, used for storing additional information about that object in a structured format. Keys may be up to 64 characters in length and values may be up to 512 characters in length. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The ID of the model to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always assistant. Required. Default value is "assistant".</td>
</tr>
<tr>
    <td><CopyableCode code="response_format" /></td>
    <td><code>object</code></td>
    <td>The response format of the tool calls used by this agent. Is one of the following types: str, Union[str, "_models.AgentsResponseFormatMode"], AgentsResponseFormat, ResponseFormatJsonSchemaType</td>
</tr>
<tr>
    <td><CopyableCode code="temperature" /></td>
    <td><code>number</code></td>
    <td>What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tool_resources" /></td>
    <td><code>object</code></td>
    <td>A set of resources that are used by the agent's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tools" /></td>
    <td><code>array</code></td>
    <td>The collection of tools enabled for the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="top_p" /></td>
    <td><code>number</code></td>
    <td>An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_agents">

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
    <td>The identifier, which can be referenced in API endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this object was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="instructions" /></td>
    <td><code>string</code></td>
    <td>The system instructions for the agent to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A set of up to 16 key/value pairs that can be attached to an object, used for storing additional information about that object in a structured format. Keys may be up to 64 characters in length and values may be up to 512 characters in length. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The ID of the model to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always assistant. Required. Default value is "assistant".</td>
</tr>
<tr>
    <td><CopyableCode code="response_format" /></td>
    <td><code>object</code></td>
    <td>The response format of the tool calls used by this agent. Is one of the following types: str, Union[str, "_models.AgentsResponseFormatMode"], AgentsResponseFormat, ResponseFormatJsonSchemaType</td>
</tr>
<tr>
    <td><CopyableCode code="temperature" /></td>
    <td><code>number</code></td>
    <td>What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tool_resources" /></td>
    <td><code>object</code></td>
    <td>A set of resources that are used by the agent's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tools" /></td>
    <td><code>array</code></td>
    <td>The collection of tools enabled for the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="top_p" /></td>
    <td><code>number</code></td>
    <td>An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both. Required.</td>
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
    <td><a href="#get_agent"><CopyableCode code="get_agent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-assistant_id"><code>assistant_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves an existing agent.</td>
</tr>
<tr>
    <td><a href="#list_agents"><CopyableCode code="list_agents" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>Gets a list of agents that were previously created.</td>
</tr>
<tr>
    <td><a href="#create_agent"><CopyableCode code="create_agent" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a new agent.</td>
</tr>
<tr>
    <td><a href="#update_agent"><CopyableCode code="update_agent" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-assistant_id"><code>assistant_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Modifies an existing agent.</td>
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
<tr id="parameter-assistant_id">
    <td><CopyableCode code="assistant_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the agent to modify. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>A cursor for use in pagination. before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order by the created_at timestamp of the objects. asc for ascending order and desc for descending order. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_agent"
    values={[
        { label: 'get_agent', value: 'get_agent' },
        { label: 'list_agents', value: 'list_agents' }
    ]}
>
<TabItem value="get_agent">

Retrieves an existing agent.

```sql
SELECT
id,
name,
created_at,
description,
instructions,
metadata,
model,
object,
response_format,
temperature,
tool_resources,
tools,
top_p
FROM azure.ai_agents.agents
WHERE assistant_id = '{{ assistant_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_agents">

Gets a list of agents that were previously created.

```sql
SELECT
id,
name,
created_at,
description,
instructions,
metadata,
model,
object,
response_format,
temperature,
tool_resources,
tools,
top_p
FROM azure.ai_agents.agents
WHERE endpoint = '{{ endpoint }}' -- required
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_agent"
    values={[
        { label: 'create_agent', value: 'create_agent' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_agent">

Creates a new agent.

```sql
INSERT INTO azure.ai_agents.agents (
endpoint
)
SELECT 
'{{ endpoint }}'
RETURNING
id,
name,
created_at,
description,
instructions,
metadata,
model,
object,
response_format,
temperature,
tool_resources,
tools,
top_p
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: agents
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the agents resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_agent"
    values={[
        { label: 'update_agent', value: 'update_agent' }
    ]}
>
<TabItem value="update_agent">

Modifies an existing agent.

```sql
EXEC azure.ai_agents.agents.update_agent 
@assistant_id='{{ assistant_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
