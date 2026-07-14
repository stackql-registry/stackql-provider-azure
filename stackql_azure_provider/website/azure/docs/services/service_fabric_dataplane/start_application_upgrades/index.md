--- 
title: start_application_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - start_application_upgrades
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

Creates, updates, deletes, gets or lists a <code>start_application_upgrades</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_application_upgrades" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.start_application_upgrades" /></td></tr>
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
    <td><a href="#start_application_upgrade"><CopyableCode code="start_application_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Name"><code>Name</code></a>, <a href="#parameter-TargetApplicationTypeVersion"><code>TargetApplicationTypeVersion</code></a>, <a href="#parameter-UpgradeKind"><code>UpgradeKind</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Starts upgrading an application in the Service Fabric cluster. Validates the supplied application upgrade parameters and starts upgrading the application if the parameters are valid. Note, [ApplicationParameter](https://docs.microsoft.com/dotnet/api/system.fabric.description.applicationdescription.applicationparameters)s are not preserved across an application upgrade. In order to preserve current application parameters, the user should get the parameters using GetApplicationInfo operation first and pass them into the upgrade API call as shown in the example.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="start_application_upgrade"
    values={[
        { label: 'start_application_upgrade', value: 'start_application_upgrade' }
    ]}
>
<TabItem value="start_application_upgrade">

Starts upgrading an application in the Service Fabric cluster. Validates the supplied application upgrade parameters and starts upgrading the application if the parameters are valid. Note, [ApplicationParameter](https://docs.microsoft.com/dotnet/api/system.fabric.description.applicationdescription.applicationparameters)s are not preserved across an application upgrade. In order to preserve current application parameters, the user should get the parameters using GetApplicationInfo operation first and pass them into the upgrade API call as shown in the example.

```sql
EXEC azure.service_fabric_dataplane.start_application_upgrades.start_application_upgrade 
@application_id='{{ application_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"Name": "{{ Name }}", 
"TargetApplicationTypeVersion": "{{ TargetApplicationTypeVersion }}", 
"Parameters": "{{ Parameters }}", 
"UpgradeKind": "{{ UpgradeKind }}", 
"RollingUpgradeMode": "{{ RollingUpgradeMode }}", 
"UpgradeReplicaSetCheckTimeoutInSeconds": {{ UpgradeReplicaSetCheckTimeoutInSeconds }}, 
"ForceRestart": {{ ForceRestart }}, 
"SortOrder": "{{ SortOrder }}", 
"MonitoringPolicy": "{{ MonitoringPolicy }}", 
"ApplicationHealthPolicy": "{{ ApplicationHealthPolicy }}", 
"InstanceCloseDelayDurationInSeconds": {{ InstanceCloseDelayDurationInSeconds }}, 
"ManagedApplicationIdentity": "{{ ManagedApplicationIdentity }}"
}'
;
```
</TabItem>
</Tabs>
