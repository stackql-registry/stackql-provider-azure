--- 
title: replica_health_using_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_health_using_policies
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

Creates, updates, deletes, gets or lists a <code>replica_health_using_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replica_health_using_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.replica_health_using_policies" /></td></tr>
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
    <td><a href="#get_replica_health_using_policy"><CopyableCode code="get_replica_health_using_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-replica_id"><code>replica_id</code></a>, <a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-EventsHealthStateFilter"><code>EventsHealthStateFilter</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the health of a Service Fabric stateful service replica or stateless service instance using the specified policy. Gets the health of a Service Fabric stateful service replica or stateless service instance. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Use ApplicationHealthPolicy to optionally override the health policies used to evaluate the health. This API only uses 'ConsiderWarningAsError' field of the ApplicationHealthPolicy. The rest of the fields are ignored while evaluating the health of the replica.</td>
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
<tr id="parameter-partition_id">
    <td><CopyableCode code="partition_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the partition.</td>
</tr>
<tr id="parameter-replica_id">
    <td><CopyableCode code="replica_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the replica.</td>
</tr>
<tr id="parameter-EventsHealthStateFilter">
    <td><CopyableCode code="EventsHealthStateFilter" /></td>
    <td><code>integer</code></td>
    <td>Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values, obtained using the bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned. - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_replica_health_using_policy"
    values={[
        { label: 'get_replica_health_using_policy', value: 'get_replica_health_using_policy' }
    ]}
>
<TabItem value="get_replica_health_using_policy">

Gets the health of a Service Fabric stateful service replica or stateless service instance using the specified policy. Gets the health of a Service Fabric stateful service replica or stateless service instance. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Use ApplicationHealthPolicy to optionally override the health policies used to evaluate the health. This API only uses 'ConsiderWarningAsError' field of the ApplicationHealthPolicy. The rest of the fields are ignored while evaluating the health of the replica.

```sql
EXEC azure.servicefabric_dataplane.replica_health_using_policies.get_replica_health_using_policy 
@replica_id='{{ replica_id }}' --required, 
@partition_id='{{ partition_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@EventsHealthStateFilter='{{ EventsHealthStateFilter }}', 
@timeout='{{ timeout }}' 
@@json=
'{
"ConsiderWarningAsError": {{ ConsiderWarningAsError }}, 
"MaxPercentUnhealthyDeployedApplications": {{ MaxPercentUnhealthyDeployedApplications }}, 
"DefaultServiceTypeHealthPolicy": "{{ DefaultServiceTypeHealthPolicy }}", 
"ServiceTypeHealthPolicyMap": "{{ ServiceTypeHealthPolicyMap }}"
}'
;
```
</TabItem>
</Tabs>
