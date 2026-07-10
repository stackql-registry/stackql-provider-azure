--- 
title: application_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - application_upgrades
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

Creates, updates, deletes, gets or lists an <code>application_upgrades</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_upgrades" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.application_upgrades" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_application_upgrade"
    values={[
        { label: 'get_application_upgrade', value: 'get_application_upgrade' }
    ]}
>
<TabItem value="get_application_upgrade">

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
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
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
    <td><CopyableCode code="TargetApplicationTypeVersion" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="TypeName" /></td>
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
    <td>Describes the parameters for an application upgrade. Note that upgrade description replaces the existing application description. This means that if the parameters are not specified, the existing parameters on the applications will be overwritten with the empty parameters list. This would result in the application using the default value of the parameters from the application manifest. If you do not want to change any existing parameter values, please get the application parameters first using the GetApplicationInfo query and then supply those values as Parameters in this ApplicationUpgradeDescription. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDomainDurationInMilliseconds" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UpgradeDomainProgressAtFailure" /></td>
    <td><code>object</code></td>
    <td>Information about the upgrade domain progress at the time of upgrade failure.</td>
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
    <td><CopyableCode code="UpgradeStatusDetails" /></td>
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
    <td><a href="#get_application_upgrade"><CopyableCode code="get_application_upgrade" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets details for the latest upgrade performed on this application. Returns information about the state of the latest application upgrade along with details to aid debugging application health issues.</td>
</tr>
<tr>
    <td><a href="#update_application_upgrade"><CopyableCode code="update_application_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Name"><code>Name</code></a>, <a href="#parameter-UpgradeKind"><code>UpgradeKind</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Updates an ongoing application upgrade in the Service Fabric cluster. Updates the parameters of an ongoing application upgrade from the ones specified at the time of starting the application upgrade. This may be required to mitigate stuck application upgrades due to incorrect parameters or issues in the application to make progress.</td>
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
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the application name is "fabric:/myapp/app1", the application identity would be "myapp~app1" in 6.0+ and "myapp/app1" in previous versions.</td>
</tr>
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
    defaultValue="get_application_upgrade"
    values={[
        { label: 'get_application_upgrade', value: 'get_application_upgrade' }
    ]}
>
<TabItem value="get_application_upgrade">

Gets details for the latest upgrade performed on this application. Returns information about the state of the latest application upgrade along with details to aid debugging application health issues.

```sql
SELECT
CurrentUpgradeDomainProgress,
CurrentUpgradeUnitsProgress,
FailureReason,
FailureTimestampUtc,
IsNodeByNode,
Name,
NextUpgradeDomain,
RollingUpgradeMode,
StartTimestampUtc,
TargetApplicationTypeVersion,
TypeName,
UnhealthyEvaluations,
UpgradeDescription,
UpgradeDomainDurationInMilliseconds,
UpgradeDomainProgressAtFailure,
UpgradeDomains,
UpgradeDurationInMilliseconds,
UpgradeState,
UpgradeStatusDetails,
UpgradeUnits
FROM azure.servicefabric_dataplane.application_upgrades
WHERE application_id = '{{ application_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_application_upgrade"
    values={[
        { label: 'update_application_upgrade', value: 'update_application_upgrade' }
    ]}
>
<TabItem value="update_application_upgrade">

Updates an ongoing application upgrade in the Service Fabric cluster. Updates the parameters of an ongoing application upgrade from the ones specified at the time of starting the application upgrade. This may be required to mitigate stuck application upgrades due to incorrect parameters or issues in the application to make progress.

```sql
EXEC azure.servicefabric_dataplane.application_upgrades.update_application_upgrade 
@application_id='{{ application_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"Name": "{{ Name }}", 
"UpgradeKind": "{{ UpgradeKind }}", 
"ApplicationHealthPolicy": "{{ ApplicationHealthPolicy }}", 
"UpdateDescription": "{{ UpdateDescription }}"
}'
;
```
</TabItem>
</Tabs>
