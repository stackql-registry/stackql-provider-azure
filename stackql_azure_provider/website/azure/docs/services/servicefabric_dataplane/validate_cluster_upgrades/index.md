--- 
title: validate_cluster_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - validate_cluster_upgrades
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

Creates, updates, deletes, gets or lists a <code>validate_cluster_upgrades</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="validate_cluster_upgrades" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.validate_cluster_upgrades" /></td></tr>
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
    <td><a href="#validate_cluster_upgrade"><CopyableCode code="validate_cluster_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Validate and assess the impact of a code or configuration version update of a Service Fabric cluster. Validate the supplied upgrade parameters and assess the expected impact of a code or configuration version upgrade of a Service Fabric cluster. The upgrade will not be initiated.</td>
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
    defaultValue="validate_cluster_upgrade"
    values={[
        { label: 'validate_cluster_upgrade', value: 'validate_cluster_upgrade' }
    ]}
>
<TabItem value="validate_cluster_upgrade">

Validate and assess the impact of a code or configuration version update of a Service Fabric cluster. Validate the supplied upgrade parameters and assess the expected impact of a code or configuration version upgrade of a Service Fabric cluster. The upgrade will not be initiated.

```sql
EXEC azure.servicefabric_dataplane.validate_cluster_upgrades.validate_cluster_upgrade 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"CodeVersion": "{{ CodeVersion }}", 
"ConfigVersion": "{{ ConfigVersion }}", 
"UpgradeKind": "{{ UpgradeKind }}", 
"RollingUpgradeMode": "{{ RollingUpgradeMode }}", 
"UpgradeReplicaSetCheckTimeoutInSeconds": {{ UpgradeReplicaSetCheckTimeoutInSeconds }}, 
"ForceRestart": {{ ForceRestart }}, 
"SortOrder": "{{ SortOrder }}", 
"MonitoringPolicy": "{{ MonitoringPolicy }}", 
"ClusterHealthPolicy": "{{ ClusterHealthPolicy }}", 
"EnableDeltaHealthEvaluation": {{ EnableDeltaHealthEvaluation }}, 
"ClusterUpgradeHealthPolicy": "{{ ClusterUpgradeHealthPolicy }}", 
"ApplicationHealthPolicyMap": "{{ ApplicationHealthPolicyMap }}", 
"InstanceCloseDelayDurationInSeconds": {{ InstanceCloseDelayDurationInSeconds }}
}'
;
```
</TabItem>
</Tabs>
