--- 
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - hdinsight
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

Creates, updates, deletes, gets or lists an <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.extensions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'get_monitoring_status', value: 'get_monitoring_status' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

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
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error message associated with the cluster creation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The async operation state. Known values are: "InProgress", "Succeeded", and "Failed". (InProgress, Succeeded, Failed)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get">

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
    <td><CopyableCode code="clusterMonitoringEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The status of the monitor on the HDInsight cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The workspace ID of the monitor on the HDInsight cluster.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_monitoring_status">

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
    <td><CopyableCode code="clusterMonitoringEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The status of the monitor on the HDInsight cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The workspace ID of the monitor on the HDInsight cluster.</td>
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
    <td><a href="#get_azure_async_operation_status"><CopyableCode code="get_azure_async_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the async operation status.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the extension properties for the specified HDInsight cluster extension.</td>
</tr>
<tr>
    <td><a href="#get_monitoring_status"><CopyableCode code="get_monitoring_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of Operations Management Suite (OMS) on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an HDInsight cluster extension.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified extension for HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#disable_monitoring"><CopyableCode code="disable_monitoring" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables the Operations Management Suite (OMS) on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#enable_monitoring"><CopyableCode code="enable_monitoring" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enables the Operations Management Suite (OMS) on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#get_azure_monitor_status"><CopyableCode code="get_azure_monitor_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of Azure Monitor on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#enable_azure_monitor"><CopyableCode code="enable_azure_monitor" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enables the Azure Monitor on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#disable_azure_monitor"><CopyableCode code="disable_azure_monitor" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables the Azure Monitor on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#get_azure_monitor_agent_status"><CopyableCode code="get_azure_monitor_agent_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of Azure Monitor Agent on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#enable_azure_monitor_agent"><CopyableCode code="enable_azure_monitor_agent" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enables the Azure Monitor Agent on the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#disable_azure_monitor_agent"><CopyableCode code="disable_azure_monitor_agent" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables the Azure Monitor Agent on the HDInsight cluster.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
</tr>
<tr id="parameter-extension_name">
    <td><CopyableCode code="extension_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster extension. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The long running operation id. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'get_monitoring_status', value: 'get_monitoring_status' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

Gets the async operation status.

```sql
SELECT
error,
status
FROM azure.hdinsight.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND extension_name = '{{ extension_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the extension properties for the specified HDInsight cluster extension.

```sql
SELECT
clusterMonitoringEnabled,
workspaceId
FROM azure.hdinsight.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND extension_name = '{{ extension_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_monitoring_status">

Gets the status of Operations Management Suite (OMS) on the HDInsight cluster.

```sql
SELECT
clusterMonitoringEnabled,
workspaceId
FROM azure.hdinsight.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates an HDInsight cluster extension.

```sql
INSERT INTO azure.hdinsight.extensions (
workspaceId,
primaryKey,
resource_group_name,
cluster_name,
extension_name,
subscription_id
)
SELECT 
'{{ workspaceId }}',
'{{ primaryKey }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ extension_name }}',
'{{ subscription_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: extensions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the extensions resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the extensions resource.
    - name: extension_name
      value: "{{ extension_name }}"
      description: Required parameter for the extensions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the extensions resource.
    - name: workspaceId
      value: "{{ workspaceId }}"
      description: |
        The workspace ID for the cluster monitoring extension.
    - name: primaryKey
      value: "{{ primaryKey }}"
      description: |
        The certificate for the cluster monitoring extensions.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'disable_monitoring', value: 'disable_monitoring' }
    ]}
>
<TabItem value="delete">

Deletes the specified extension for HDInsight cluster.

```sql
DELETE FROM azure.hdinsight.extensions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND extension_name = '{{ extension_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="disable_monitoring">

Disables the Operations Management Suite (OMS) on the HDInsight cluster.

```sql
DELETE FROM azure.hdinsight.extensions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="enable_monitoring"
    values={[
        { label: 'enable_monitoring', value: 'enable_monitoring' },
        { label: 'get_azure_monitor_status', value: 'get_azure_monitor_status' },
        { label: 'enable_azure_monitor', value: 'enable_azure_monitor' },
        { label: 'disable_azure_monitor', value: 'disable_azure_monitor' },
        { label: 'get_azure_monitor_agent_status', value: 'get_azure_monitor_agent_status' },
        { label: 'enable_azure_monitor_agent', value: 'enable_azure_monitor_agent' },
        { label: 'disable_azure_monitor_agent', value: 'disable_azure_monitor_agent' }
    ]}
>
<TabItem value="enable_monitoring">

Enables the Operations Management Suite (OMS) on the HDInsight cluster.

```sql
EXEC azure.hdinsight.extensions.enable_monitoring 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"workspaceId": "{{ workspaceId }}", 
"primaryKey": "{{ primaryKey }}"
}'
;
```
</TabItem>
<TabItem value="get_azure_monitor_status">

Gets the status of Azure Monitor on the HDInsight cluster.

```sql
EXEC azure.hdinsight.extensions.get_azure_monitor_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_azure_monitor">

Enables the Azure Monitor on the HDInsight cluster.

```sql
EXEC azure.hdinsight.extensions.enable_azure_monitor 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"workspaceId": "{{ workspaceId }}", 
"primaryKey": "{{ primaryKey }}", 
"selectedConfigurations": "{{ selectedConfigurations }}"
}'
;
```
</TabItem>
<TabItem value="disable_azure_monitor">

Disables the Azure Monitor on the HDInsight cluster.

```sql
EXEC azure.hdinsight.extensions.disable_azure_monitor 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_azure_monitor_agent_status">

Gets the status of Azure Monitor Agent on the HDInsight cluster.

```sql
EXEC azure.hdinsight.extensions.get_azure_monitor_agent_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_azure_monitor_agent">

Enables the Azure Monitor Agent on the HDInsight cluster.

```sql
EXEC azure.hdinsight.extensions.enable_azure_monitor_agent 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"workspaceId": "{{ workspaceId }}", 
"primaryKey": "{{ primaryKey }}", 
"selectedConfigurations": "{{ selectedConfigurations }}"
}'
;
```
</TabItem>
<TabItem value="disable_azure_monitor_agent">

Disables the Azure Monitor Agent on the HDInsight cluster.

```sql
EXEC azure.hdinsight.extensions.disable_azure_monitor_agent 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
