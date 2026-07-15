--- 
title: cluster_upgrade_progress
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_upgrade_progress
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>cluster_upgrade_progress</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_upgrade_progress" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.cluster_upgrade_progress" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_cluster_upgrade_progress"
    values={[
        { label: 'get_cluster_upgrade_progress', value: 'get_cluster_upgrade_progress' }
    ]}
>
<TabItem value="get_cluster_upgrade_progress">

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
    <td><CopyableCode code="CodeVersion" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ConfigVersion" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="CurrentUpgradeDomainProgress" /></td>
    <td><code>object</code></td>
    <td>Information about the current in-progress upgrade domain. Not applicable to node-by-node upgrades.</td>
</tr>
<tr>
    <td><CopyableCode code="CurrentUpgradeUnitsProgress" /></td>
    <td><code>object</code></td>
    <td>Information about the current in-progress upgrade units.</td>
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
    <td><CopyableCode code="IsNodeByNode" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="NextUpgradeDomain" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="UnhealthyEvaluations" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDescription" /></td>
    <td><code>object</code></td>
    <td>Represents a ServiceFabric cluster upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDomainDurationInMilliseconds" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDomainProgressAtFailure" /></td>
    <td><code>object</code></td>
    <td>The detailed upgrade progress for nodes in the current upgrade domain at the point of failure. Not applicable to node-by-node upgrades.</td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDomains" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDurationInMilliseconds" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeState" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeUnits" /></td>
    <td><code>array</code></td>
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
    <td><a href="#get_cluster_upgrade_progress"><CopyableCode code="get_cluster_upgrade_progress" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the progress of the current cluster upgrade. Gets the current progress of the ongoing cluster upgrade. If no upgrade is currently in progress, get the last state of the previous cluster upgrade.</td>
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
    defaultValue="get_cluster_upgrade_progress"
    values={[
        { label: 'get_cluster_upgrade_progress', value: 'get_cluster_upgrade_progress' }
    ]}
>
<TabItem value="get_cluster_upgrade_progress">

Gets the progress of the current cluster upgrade. Gets the current progress of the ongoing cluster upgrade. If no upgrade is currently in progress, get the last state of the previous cluster upgrade.

```sql
SELECT
CodeVersion,
ConfigVersion,
CurrentUpgradeDomainProgress,
CurrentUpgradeUnitsProgress,
FailureReason,
FailureTimestampUtc,
IsNodeByNode,
NextUpgradeDomain,
RollingUpgradeMode,
StartTimestampUtc,
UnhealthyEvaluations,
UpgradeDescription,
UpgradeDomainDurationInMilliseconds,
UpgradeDomainProgressAtFailure,
UpgradeDomains,
UpgradeDurationInMilliseconds,
UpgradeState,
UpgradeUnits
FROM azure.service_fabric_dataplane.cluster_upgrade_progress
WHERE endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
