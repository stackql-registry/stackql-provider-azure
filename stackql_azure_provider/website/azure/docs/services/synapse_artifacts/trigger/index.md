--- 
title: trigger
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger
  - synapse_artifacts
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

Creates, updates, deletes, gets or lists a <code>trigger</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="trigger" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.trigger" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_trigger"
    values={[
        { label: 'get_trigger', value: 'get_trigger' },
        { label: 'get_triggers_by_workspace', value: 'get_triggers_by_workspace' }
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the trigger.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Trigger description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeState" /></td>
    <td><code>string</code></td>
    <td>Indicates if trigger is running or not. Updated when Start/Stop APIs are called on the Trigger. Known values are: "Started", "Stopped", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_triggers_by_workspace">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the trigger.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Trigger description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeState" /></td>
    <td><code>string</code></td>
    <td>Indicates if trigger is running or not. Updated when Start/Stop APIs are called on the Trigger. Known values are: "Started", "Stopped", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a trigger.</td>
</tr>
<tr>
    <td><a href="#get_triggers_by_workspace"><CopyableCode code="get_triggers_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists triggers.</td>
</tr>
<tr>
    <td><a href="#create_or_update_trigger"><CopyableCode code="create_or_update_trigger" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a trigger.</td>
</tr>
<tr>
    <td><a href="#create_or_update_trigger"><CopyableCode code="create_or_update_trigger" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a trigger.</td>
</tr>
<tr>
    <td><a href="#delete_trigger"><CopyableCode code="delete_trigger" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a trigger.</td>
</tr>
<tr>
    <td><a href="#get_event_subscription_status"><CopyableCode code="get_event_subscription_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a trigger's event subscription status.</td>
</tr>
<tr>
    <td><a href="#subscribe_trigger_to_events"><CopyableCode code="subscribe_trigger_to_events" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Subscribe event trigger to events.</td>
</tr>
<tr>
    <td><a href="#unsubscribe_trigger_from_events"><CopyableCode code="unsubscribe_trigger_from_events" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Unsubscribe event trigger from events.</td>
</tr>
<tr>
    <td><a href="#start_trigger"><CopyableCode code="start_trigger" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Starts a trigger.</td>
</tr>
<tr>
    <td><a href="#stop_trigger"><CopyableCode code="stop_trigger" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stops a trigger.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-trigger_name">
    <td><CopyableCode code="trigger_name" /></td>
    <td><code>string</code></td>
    <td>The trigger name. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the trigger entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the trigger entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_trigger"
    values={[
        { label: 'get_trigger', value: 'get_trigger' },
        { label: 'get_triggers_by_workspace', value: 'get_triggers_by_workspace' }
    ]}
>
<TabItem value="get_trigger">

Gets a trigger.

```sql
SELECT
id,
name,
,
annotations,
description,
etag,
runtimeState,
type
FROM azure.synapse_artifacts.trigger
WHERE trigger_name = '{{ trigger_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_triggers_by_workspace">

Lists triggers.

```sql
SELECT
id,
name,
,
annotations,
description,
etag,
runtimeState,
type
FROM azure.synapse_artifacts.trigger
WHERE endpoint = '{{ endpoint }}' -- required
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

Creates or updates a trigger.

```sql
INSERT INTO azure.synapse_artifacts.trigger (
,
type,
description,
annotations,
trigger_name,
endpoint,
If-Match
)
SELECT 
'{{  }}',
'{{ type }}' /* required */,
'{{ description }}',
'{{ annotations }}',
'{{ trigger_name }}',
'{{ endpoint }}',
'{{ If-Match }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: trigger
  props:
    - name: trigger_name
      value: "{{ trigger_name }}"
      description: Required parameter for the trigger resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the trigger resource.
    - name: 
      value: "{{  }}"
      description: |
        Unmatched properties from the message are deserialized to this collection.
    - name: type
      value: "{{ type }}"
      description: |
        Trigger type. Required.
    - name: description
      value: "{{ description }}"
      description: |
        Trigger description.
    - name: annotations
      value: "{{ annotations }}"
      description: |
        List of tags that can be used for describing the trigger.
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the trigger entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the trigger entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
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

Creates or updates a trigger.

```sql
REPLACE azure.synapse_artifacts.trigger
SET 
 = '{{  }}',
type = '{{ type }}',
description = '{{ description }}',
annotations = '{{ annotations }}'
WHERE 
trigger_name = '{{ trigger_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND type = '{{ type }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
properties,
type;
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

Deletes a trigger.

```sql
DELETE FROM azure.synapse_artifacts.trigger
WHERE trigger_name = '{{ trigger_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_event_subscription_status"
    values={[
        { label: 'get_event_subscription_status', value: 'get_event_subscription_status' },
        { label: 'subscribe_trigger_to_events', value: 'subscribe_trigger_to_events' },
        { label: 'unsubscribe_trigger_from_events', value: 'unsubscribe_trigger_from_events' },
        { label: 'start_trigger', value: 'start_trigger' },
        { label: 'stop_trigger', value: 'stop_trigger' }
    ]}
>
<TabItem value="get_event_subscription_status">

Get a trigger's event subscription status.

```sql
EXEC azure.synapse_artifacts.trigger.get_event_subscription_status 
@trigger_name='{{ trigger_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="subscribe_trigger_to_events">

Subscribe event trigger to events.

```sql
EXEC azure.synapse_artifacts.trigger.subscribe_trigger_to_events 
@trigger_name='{{ trigger_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="unsubscribe_trigger_from_events">

Unsubscribe event trigger from events.

```sql
EXEC azure.synapse_artifacts.trigger.unsubscribe_trigger_from_events 
@trigger_name='{{ trigger_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="start_trigger">

Starts a trigger.

```sql
EXEC azure.synapse_artifacts.trigger.start_trigger 
@trigger_name='{{ trigger_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="stop_trigger">

Stops a trigger.

```sql
EXEC azure.synapse_artifacts.trigger.stop_trigger 
@trigger_name='{{ trigger_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
