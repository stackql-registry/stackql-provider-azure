--- 
title: upgrade_orchestration_service_states
hide_title: false
hide_table_of_contents: false
keywords:
  - upgrade_orchestration_service_states
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>upgrade_orchestration_service_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="upgrade_orchestration_service_states" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.upgrade_orchestration_service_states" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_upgrade_orchestration_service_state"
    values={[
        { label: 'get_upgrade_orchestration_service_state', value: 'get_upgrade_orchestration_service_state' }
    ]}
>
<TabItem value="get_upgrade_orchestration_service_state">

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
    <td><CopyableCode code="ServiceState" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#get_upgrade_orchestration_service_state"><CopyableCode code="get_upgrade_orchestration_service_state" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Get the service state of Service Fabric Upgrade Orchestration Service. Get the service state of Service Fabric Upgrade Orchestration Service. This API is internally used for support purposes.</td>
</tr>
<tr>
    <td><a href="#set_upgrade_orchestration_service_state"><CopyableCode code="set_upgrade_orchestration_service_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Update the service state of Service Fabric Upgrade Orchestration Service. Update the service state of Service Fabric Upgrade Orchestration Service. This API is internally used for support purposes.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_upgrade_orchestration_service_state"
    values={[
        { label: 'get_upgrade_orchestration_service_state', value: 'get_upgrade_orchestration_service_state' }
    ]}
>
<TabItem value="get_upgrade_orchestration_service_state">

Get the service state of Service Fabric Upgrade Orchestration Service. Get the service state of Service Fabric Upgrade Orchestration Service. This API is internally used for support purposes.

```sql
SELECT
ServiceState
FROM azure.servicefabric_dataplane.upgrade_orchestration_service_states
WHERE endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="set_upgrade_orchestration_service_state"
    values={[
        { label: 'set_upgrade_orchestration_service_state', value: 'set_upgrade_orchestration_service_state' }
    ]}
>
<TabItem value="set_upgrade_orchestration_service_state">

Update the service state of Service Fabric Upgrade Orchestration Service. Update the service state of Service Fabric Upgrade Orchestration Service. This API is internally used for support purposes.

```sql
EXEC azure.servicefabric_dataplane.upgrade_orchestration_service_states.set_upgrade_orchestration_service_state 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"ServiceState": "{{ ServiceState }}"
}'
;
```
</TabItem>
</Tabs>
