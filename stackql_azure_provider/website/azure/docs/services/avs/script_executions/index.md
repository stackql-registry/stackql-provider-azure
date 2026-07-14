--- 
title: script_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - script_executions
  - avs
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

Creates, updates, deletes, gets or lists a <code>script_executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="script_executions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.avs.script_executions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Standard error output stream from the powershell execution.</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Error message if the script was able to run, but if the script itself had errors or powershell threw an exception.</td>
</tr>
<tr>
    <td><CopyableCode code="finishedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the script execution was finished.</td>
</tr>
<tr>
    <td><CopyableCode code="hiddenParameters" /></td>
    <td><code>array</code></td>
    <td>Parameters that will be hidden/not visible to ARM, such as passwords and credentials.</td>
</tr>
<tr>
    <td><CopyableCode code="information" /></td>
    <td><code>array</code></td>
    <td>Standard information out stream from the powershell execution.</td>
</tr>
<tr>
    <td><CopyableCode code="namedOutputs" /></td>
    <td><code>object</code></td>
    <td>User-defined dictionary.</td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>array</code></td>
    <td>Standard output stream from the powershell execution.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>Parameters the script will accept.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the script execution resource. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Running", "Cancelling", "Cancelled", and "Deleting". (Succeeded, Failed, Canceled, Pending, Running, Cancelling, Cancelled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="retention" /></td>
    <td><code>string</code></td>
    <td>Time to live for the resource. If not provided, will be available for 60 days.</td>
</tr>
<tr>
    <td><CopyableCode code="scriptCmdletId" /></td>
    <td><code>string</code></td>
    <td>A reference to the script cmdlet resource if user is running a AVS script.</td>
</tr>
<tr>
    <td><CopyableCode code="startedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the script execution was started.</td>
</tr>
<tr>
    <td><CopyableCode code="submittedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the script execution was submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>string</code></td>
    <td>Time limit for execution. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Standard warning out stream from the powershell execution.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Standard error output stream from the powershell execution.</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Error message if the script was able to run, but if the script itself had errors or powershell threw an exception.</td>
</tr>
<tr>
    <td><CopyableCode code="finishedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the script execution was finished.</td>
</tr>
<tr>
    <td><CopyableCode code="hiddenParameters" /></td>
    <td><code>array</code></td>
    <td>Parameters that will be hidden/not visible to ARM, such as passwords and credentials.</td>
</tr>
<tr>
    <td><CopyableCode code="information" /></td>
    <td><code>array</code></td>
    <td>Standard information out stream from the powershell execution.</td>
</tr>
<tr>
    <td><CopyableCode code="namedOutputs" /></td>
    <td><code>object</code></td>
    <td>User-defined dictionary.</td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>array</code></td>
    <td>Standard output stream from the powershell execution.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>Parameters the script will accept.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the script execution resource. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Running", "Cancelling", "Cancelled", and "Deleting". (Succeeded, Failed, Canceled, Pending, Running, Cancelling, Cancelled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="retention" /></td>
    <td><code>string</code></td>
    <td>Time to live for the resource. If not provided, will be available for 60 days.</td>
</tr>
<tr>
    <td><CopyableCode code="scriptCmdletId" /></td>
    <td><code>string</code></td>
    <td>A reference to the script cmdlet resource if user is running a AVS script.</td>
</tr>
<tr>
    <td><CopyableCode code="startedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the script execution was started.</td>
</tr>
<tr>
    <td><CopyableCode code="submittedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the script execution was submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>string</code></td>
    <td>Time limit for execution. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Standard warning out stream from the powershell execution.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-script_execution_name"><code>script_execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ScriptExecution.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ScriptExecution resources by PrivateCloud.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-script_execution_name"><code>script_execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a ScriptExecution.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-script_execution_name"><code>script_execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a ScriptExecution.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-script_execution_name"><code>script_execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ScriptExecution.</td>
</tr>
<tr>
    <td><a href="#get_execution_logs"><CopyableCode code="get_execution_logs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-script_execution_name"><code>script_execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Return the logs for a script execution resource.</td>
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
<tr id="parameter-private_cloud_name">
    <td><CopyableCode code="private_cloud_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private cloud. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-script_execution_name">
    <td><CopyableCode code="script_execution_name" /></td>
    <td><code>string</code></td>
    <td>Name of the script cmdlet. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a ScriptExecution.

```sql
SELECT
id,
name,
errors,
failureReason,
finishedAt,
hiddenParameters,
information,
namedOutputs,
output,
parameters,
provisioningState,
retention,
scriptCmdletId,
startedAt,
submittedAt,
systemData,
timeout,
type,
warnings
FROM azure.avs.script_executions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND script_execution_name = '{{ script_execution_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List ScriptExecution resources by PrivateCloud.

```sql
SELECT
id,
name,
errors,
failureReason,
finishedAt,
hiddenParameters,
information,
namedOutputs,
output,
parameters,
provisioningState,
retention,
scriptCmdletId,
startedAt,
submittedAt,
systemData,
timeout,
type,
warnings
FROM azure.avs.script_executions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create a ScriptExecution.

```sql
INSERT INTO azure.avs.script_executions (
properties,
resource_group_name,
private_cloud_name,
script_execution_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ script_execution_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: script_executions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the script_executions resource.
    - name: private_cloud_name
      value: "{{ private_cloud_name }}"
      description: Required parameter for the script_executions resource.
    - name: script_execution_name
      value: "{{ script_execution_name }}"
      description: Required parameter for the script_executions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the script_executions resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        scriptCmdletId: "{{ scriptCmdletId }}"
        parameters:
          - type: "{{ type }}"
            name: "{{ name }}"
        hiddenParameters:
          - type: "{{ type }}"
            name: "{{ name }}"
        failureReason: "{{ failureReason }}"
        timeout: "{{ timeout }}"
        retention: "{{ retention }}"
        submittedAt: "{{ submittedAt }}"
        startedAt: "{{ startedAt }}"
        finishedAt: "{{ finishedAt }}"
        provisioningState: "{{ provisioningState }}"
        output:
          - "{{ output }}"
        namedOutputs: "{{ namedOutputs }}"
        information:
          - "{{ information }}"
        warnings:
          - "{{ warnings }}"
        errors:
          - "{{ errors }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a ScriptExecution.

```sql
REPLACE azure.avs.script_executions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND script_execution_name = '{{ script_execution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a ScriptExecution.

```sql
DELETE FROM azure.avs.script_executions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND script_execution_name = '{{ script_execution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_execution_logs"
    values={[
        { label: 'get_execution_logs', value: 'get_execution_logs' }
    ]}
>
<TabItem value="get_execution_logs">

Return the logs for a script execution resource.

```sql
EXEC azure.avs.script_executions.get_execution_logs 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@script_execution_name='{{ script_execution_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
