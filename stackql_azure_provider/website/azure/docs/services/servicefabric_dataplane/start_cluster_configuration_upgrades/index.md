--- 
title: start_cluster_configuration_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - start_cluster_configuration_upgrades
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

Creates, updates, deletes, gets or lists a <code>start_cluster_configuration_upgrades</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_cluster_configuration_upgrades" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.start_cluster_configuration_upgrades" /></td></tr>
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
    <td><a href="#start_cluster_configuration_upgrade"><CopyableCode code="start_cluster_configuration_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-ClusterConfig"><code>ClusterConfig</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Start upgrading the configuration of a Service Fabric standalone cluster. Validate the supplied configuration upgrade parameters and start upgrading the cluster configuration if the parameters are valid.</td>
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
    <td>The service endpoint. (default: )</td>
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
    defaultValue="start_cluster_configuration_upgrade"
    values={[
        { label: 'start_cluster_configuration_upgrade', value: 'start_cluster_configuration_upgrade' }
    ]}
>
<TabItem value="start_cluster_configuration_upgrade">

Start upgrading the configuration of a Service Fabric standalone cluster. Validate the supplied configuration upgrade parameters and start upgrading the cluster configuration if the parameters are valid.

```sql
EXEC azure.servicefabric_dataplane.start_cluster_configuration_upgrades.start_cluster_configuration_upgrade 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"ClusterConfig": "{{ ClusterConfig }}", 
"HealthCheckRetryTimeout": "{{ HealthCheckRetryTimeout }}", 
"HealthCheckWaitDurationInSeconds": "{{ HealthCheckWaitDurationInSeconds }}", 
"HealthCheckStableDurationInSeconds": "{{ HealthCheckStableDurationInSeconds }}", 
"UpgradeDomainTimeoutInSeconds": "{{ UpgradeDomainTimeoutInSeconds }}", 
"UpgradeTimeoutInSeconds": "{{ UpgradeTimeoutInSeconds }}", 
"MaxPercentUnhealthyApplications": {{ MaxPercentUnhealthyApplications }}, 
"MaxPercentUnhealthyNodes": {{ MaxPercentUnhealthyNodes }}, 
"MaxPercentDeltaUnhealthyNodes": {{ MaxPercentDeltaUnhealthyNodes }}, 
"MaxPercentUpgradeDomainDeltaUnhealthyNodes": {{ MaxPercentUpgradeDomainDeltaUnhealthyNodes }}, 
"ApplicationHealthPolicies": "{{ ApplicationHealthPolicies }}"
}'
;
```
</TabItem>
</Tabs>
