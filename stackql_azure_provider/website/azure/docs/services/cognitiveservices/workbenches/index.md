--- 
title: workbenches
hide_title: false
hide_table_of_contents: false
keywords:
  - workbenches
  - cognitiveservices
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

Creates, updates, deletes, gets or lists a <code>workbenches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workbenches" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitiveservices.workbenches" /></td></tr>
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
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>object</code></td>
    <td>Network connectivity endpoints assigned to the workbench.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of the workbench resource.</td>
</tr>
<tr>
    <td><CopyableCode code="datasetId" /></td>
    <td><code>string</code></td>
    <td>The dataset ID to mount for the workbench.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Error details for the workbench resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeBeforeShutdown" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 duration before the idle workbench is automatically shut down (e.g., 'PT30M').</td>
</tr>
<tr>
    <td><CopyableCode code="imageLink" /></td>
    <td><code>string</code></td>
    <td>Container image URI (e.g., MCR or ACR image path) for the workbench. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the workbench resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the workbench resource. Known values are: "Accepted", "Succeeded", "Failed", "Canceled", "Deleting", "Scaling", "Disabled", "Starting", "Stopping", "Restarting", and "Stopped". (Accepted, Succeeded, Failed, Canceled, Deleting, Scaling, Disabled, Starting, Stopping, Restarting, Stopped)</td>
</tr>
<tr>
    <td><CopyableCode code="sshSettings" /></td>
    <td><code>object</code></td>
    <td>SSH configuration for remote access to the workbench.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetClusterId" /></td>
    <td><code>string</code></td>
    <td>ARM resource ID of the parent cluster that hosts this workbench. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="webEndpoint" /></td>
    <td><code>string</code></td>
    <td>The web endpoint URL for accessing the workbench.</td>
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
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>object</code></td>
    <td>Network connectivity endpoints assigned to the workbench.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of the workbench resource.</td>
</tr>
<tr>
    <td><CopyableCode code="datasetId" /></td>
    <td><code>string</code></td>
    <td>The dataset ID to mount for the workbench.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Error details for the workbench resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeBeforeShutdown" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 duration before the idle workbench is automatically shut down (e.g., 'PT30M').</td>
</tr>
<tr>
    <td><CopyableCode code="imageLink" /></td>
    <td><code>string</code></td>
    <td>Container image URI (e.g., MCR or ACR image path) for the workbench. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the workbench resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the workbench resource. Known values are: "Accepted", "Succeeded", "Failed", "Canceled", "Deleting", "Scaling", "Disabled", "Starting", "Stopping", "Restarting", and "Stopped". (Accepted, Succeeded, Failed, Canceled, Deleting, Scaling, Disabled, Starting, Stopping, Restarting, Stopped)</td>
</tr>
<tr>
    <td><CopyableCode code="sshSettings" /></td>
    <td><code>object</code></td>
    <td>SSH configuration for remote access to the workbench.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetClusterId" /></td>
    <td><code>string</code></td>
    <td>ARM resource ID of the parent cluster that hosts this workbench. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="webEndpoint" /></td>
    <td><code>string</code></td>
    <td>The web endpoint URL for accessing the workbench.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified workbench associated with the project.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the workbenches associated with the project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a workbench associated with the project.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Updates a workbench associated with the project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a workbench associated with the project.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified workbench associated with the project.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a stopped workbench resource. This is a long-running operation that returns 202 Accepted. Returns 204 if the workbench is already in the target state.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops a running workbench resource. This is a long-running operation that returns 202 Accepted. Returns 204 if the workbench is already in the target state.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-workbench_name"><code>workbench_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts a running workbench resource. This is a long-running operation that returns 202 Accepted. Returns 204 if the workbench is already in the target state.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of Cognitive Services account. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of Cognitive Services account's project. Required.</td>
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
<tr id="parameter-workbench_name">
    <td><CopyableCode code="workbench_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workbench associated with the project. Required.</td>
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

Gets the specified workbench associated with the project.

```sql
SELECT
id,
name,
connectivityEndpoints,
creationTime,
datasetId,
errors,
etag,
identity,
idleTimeBeforeShutdown,
imageLink,
location,
provisioningState,
sshSettings,
systemData,
tags,
targetClusterId,
type,
webEndpoint
FROM azure.cognitiveservices.workbenches
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND workbench_name = '{{ workbench_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the workbenches associated with the project.

```sql
SELECT
id,
name,
connectivityEndpoints,
creationTime,
datasetId,
errors,
etag,
identity,
idleTimeBeforeShutdown,
imageLink,
location,
provisioningState,
sshSettings,
systemData,
tags,
targetClusterId,
type,
webEndpoint
FROM azure.cognitiveservices.workbenches
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND project_name = '{{ project_name }}' -- required
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

Creates or updates a workbench associated with the project.

```sql
INSERT INTO azure.cognitiveservices.workbenches (
properties,
location,
tags,
identity,
resource_group_name,
account_name,
project_name,
workbench_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ project_name }}',
'{{ workbench_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workbenches
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workbenches resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the workbenches resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the workbenches resource.
    - name: workbench_name
      value: "{{ workbench_name }}"
      description: Required parameter for the workbenches resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workbenches resource.
    - name: properties
      description: |
        Properties of the workbench resource. Required.
      value:
        targetClusterId: "{{ targetClusterId }}"
        imageLink: "{{ imageLink }}"
        idleTimeBeforeShutdown: "{{ idleTimeBeforeShutdown }}"
        datasetId: "{{ datasetId }}"
        sshSettings:
          sshPublicKey: "{{ sshPublicKey }}"
          adminEnabled: {{ adminEnabled }}
        connectivityEndpoints:
          publicIpAddress: "{{ publicIpAddress }}"
          sshPort: {{ sshPort }}
        webEndpoint: "{{ webEndpoint }}"
        provisioningState: "{{ provisioningState }}"
        errors:
          - code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details: "{{ details }}"
            additionalInfo: "{{ additionalInfo }}"
        creationTime: "{{ creationTime }}"
    - name: location
      value: "{{ location }}"
      description: |
        The location of the workbench resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: identity
      description: |
        Identity for the resource.
      value:
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a workbench associated with the project.

```sql
UPDATE azure.cognitiveservices.workbenches
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND project_name = '{{ project_name }}' --required
AND workbench_name = '{{ workbench_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
systemData,
tags,
type;
```
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

Creates or updates a workbench associated with the project.

```sql
REPLACE azure.cognitiveservices.workbenches
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND project_name = '{{ project_name }}' --required
AND workbench_name = '{{ workbench_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
systemData,
tags,
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

Deletes the specified workbench associated with the project.

```sql
DELETE FROM azure.cognitiveservices.workbenches
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND project_name = '{{ project_name }}' --required
AND workbench_name = '{{ workbench_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'restart', value: 'restart' }
    ]}
>
<TabItem value="start">

Starts a stopped workbench resource. This is a long-running operation that returns 202 Accepted. Returns 204 if the workbench is already in the target state.

```sql
EXEC azure.cognitiveservices.workbenches.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@workbench_name='{{ workbench_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a running workbench resource. This is a long-running operation that returns 202 Accepted. Returns 204 if the workbench is already in the target state.

```sql
EXEC azure.cognitiveservices.workbenches.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@workbench_name='{{ workbench_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restarts a running workbench resource. This is a long-running operation that returns 202 Accepted. Returns 204 if the workbench is already in the target state.

```sql
EXEC azure.cognitiveservices.workbenches.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@workbench_name='{{ workbench_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
