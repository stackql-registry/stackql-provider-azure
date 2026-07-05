--- 
title: start_rollback_compose_deployment_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - start_rollback_compose_deployment_upgrades
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

Creates, updates, deletes, gets or lists a <code>start_rollback_compose_deployment_upgrades</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_rollback_compose_deployment_upgrades" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.start_rollback_compose_deployment_upgrades" /></td></tr>
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
    <td><a href="#start_rollback_compose_deployment_upgrade"><CopyableCode code="start_rollback_compose_deployment_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Starts rolling back a compose deployment upgrade in the Service Fabric cluster. Rollback a service fabric compose deployment upgrade.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="start_rollback_compose_deployment_upgrade"
    values={[
        { label: 'start_rollback_compose_deployment_upgrade', value: 'start_rollback_compose_deployment_upgrade' }
    ]}
>
<TabItem value="start_rollback_compose_deployment_upgrade">

Starts rolling back a compose deployment upgrade in the Service Fabric cluster. Rollback a service fabric compose deployment upgrade.

```sql
EXEC azure.servicefabric_dataplane.start_rollback_compose_deployment_upgrades.start_rollback_compose_deployment_upgrade 
@deployment_name='{{ deployment_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
