--- 
title: compose_deployment_upgrade_progress
hide_title: false
hide_table_of_contents: false
keywords:
  - compose_deployment_upgrade_progress
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

Creates, updates, deletes, gets or lists a <code>compose_deployment_upgrade_progress</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="compose_deployment_upgrade_progress" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.compose_deployment_upgrade_progress" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_compose_deployment_upgrade_progress"
    values={[
        { label: 'get_compose_deployment_upgrade_progress', value: 'get_compose_deployment_upgrade_progress' }
    ]}
>
<TabItem value="get_compose_deployment_upgrade_progress">

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
    <td><CopyableCode code="ApplicationHealthPolicy" /></td>
    <td><code>object</code></td>
    <td>Defines a health policy used to evaluate the health of an application or one of its children entities.</td>
</tr>
<tr>
    <td><CopyableCode code="ApplicationName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ApplicationUnhealthyEvaluations" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ApplicationUpgradeStatusDetails" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="CurrentUpgradeDomainDuration" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="CurrentUpgradeDomainProgress" /></td>
    <td><code>object</code></td>
    <td>Information about the current in-progress upgrade domain. Not applicable to node-by-node upgrades.</td>
</tr>
<tr>
    <td><CopyableCode code="DeploymentName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="FailureReason" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="FailureTimestampUtc" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ForceRestart" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="MonitoringPolicy" /></td>
    <td><code>object</code></td>
    <td>Describes the parameters for monitoring an upgrade in Monitored mode.</td>
</tr>
<tr>
    <td><CopyableCode code="RollingUpgradeMode" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="StartTimestampUtc" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="TargetApplicationTypeVersion" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDomainProgressAtFailure" /></td>
    <td><code>object</code></td>
    <td>Information about the upgrade domain progress at the time of upgrade failure.</td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDuration" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeKind" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeReplicaSetCheckTimeoutInSeconds" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeState" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeStatusDetails" /></td>
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
    <td><a href="#get_compose_deployment_upgrade_progress"><CopyableCode code="get_compose_deployment_upgrade_progress" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets details for the latest upgrade performed on this Service Fabric compose deployment. Returns the information about the state of the compose deployment upgrade along with details to aid debugging application health issues.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The identity of the deployment.</td>
</tr>
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

## `SELECT` examples

<Tabs
    defaultValue="get_compose_deployment_upgrade_progress"
    values={[
        { label: 'get_compose_deployment_upgrade_progress', value: 'get_compose_deployment_upgrade_progress' }
    ]}
>
<TabItem value="get_compose_deployment_upgrade_progress">

Gets details for the latest upgrade performed on this Service Fabric compose deployment. Returns the information about the state of the compose deployment upgrade along with details to aid debugging application health issues.

```sql
SELECT
ApplicationHealthPolicy,
ApplicationName,
ApplicationUnhealthyEvaluations,
ApplicationUpgradeStatusDetails,
CurrentUpgradeDomainDuration,
CurrentUpgradeDomainProgress,
DeploymentName,
FailureReason,
FailureTimestampUtc,
ForceRestart,
MonitoringPolicy,
RollingUpgradeMode,
StartTimestampUtc,
TargetApplicationTypeVersion,
UpgradeDomainProgressAtFailure,
UpgradeDuration,
UpgradeKind,
UpgradeReplicaSetCheckTimeoutInSeconds,
UpgradeState,
UpgradeStatusDetails
FROM azure.servicefabric_dataplane.compose_deployment_upgrade_progress
WHERE deployment_name = '{{ deployment_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
