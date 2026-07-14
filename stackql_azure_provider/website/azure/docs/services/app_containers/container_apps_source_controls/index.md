--- 
title: container_apps_source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_source_controls
  - app_containers
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

Creates, updates, deletes, gets or lists a <code>container_apps_source_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps_source_controls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_containers.container_apps_source_controls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_container_app', value: 'list_by_container_app' }
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
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>The branch which will trigger the auto deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="githubActionConfiguration" /></td>
    <td><code>object</code></td>
    <td>Container App Revision Template with all possible settings and the defaults if user did not provide them. The defaults are populated as they were at the creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="operationState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning State of the operation. Known values are: "InProgress", "Succeeded", "Failed", and "Canceled". (InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="repoUrl" /></td>
    <td><code>string</code></td>
    <td>The repo url which will be integrated to ContainerApp.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_container_app">

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
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>The branch which will trigger the auto deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="githubActionConfiguration" /></td>
    <td><code>object</code></td>
    <td>Container App Revision Template with all possible settings and the defaults if user did not provide them. The defaults are populated as they were at the creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="operationState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning State of the operation. Known values are: "InProgress", "Succeeded", "Failed", and "Canceled". (InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="repoUrl" /></td>
    <td><code>string</code></td>
    <td>The repo url which will be integrated to ContainerApp.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a SourceControl of a Container App. Get a SourceControl of a Container App.</td>
</tr>
<tr>
    <td><a href="#list_by_container_app"><CopyableCode code="list_by_container_app" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Container App SourceControls in a given resource group. Get the Container App SourceControls in a given resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the SourceControl for a Container App. Create or update the SourceControl for a Container App.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the SourceControl for a Container App. Create or update the SourceControl for a Container App.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Container App SourceControl. Delete a Container App SourceControl.</td>
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
<tr id="parameter-container_app_name">
    <td><CopyableCode code="container_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-source_control_name">
    <td><CopyableCode code="source_control_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App SourceControl. Required.</td>
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
        { label: 'list_by_container_app', value: 'list_by_container_app' }
    ]}
>
<TabItem value="get">

Get a SourceControl of a Container App. Get a SourceControl of a Container App.

```sql
SELECT
id,
name,
branch,
githubActionConfiguration,
operationState,
repoUrl,
systemData,
type
FROM azure.app_containers.container_apps_source_controls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND source_control_name = '{{ source_control_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_container_app">

Get the Container App SourceControls in a given resource group. Get the Container App SourceControls in a given resource group.

```sql
SELECT
id,
name,
branch,
githubActionConfiguration,
operationState,
repoUrl,
systemData,
type
FROM azure.app_containers.container_apps_source_controls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
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

Create or update the SourceControl for a Container App. Create or update the SourceControl for a Container App.

```sql
INSERT INTO azure.app_containers.container_apps_source_controls (
properties,
resource_group_name,
container_app_name,
source_control_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ container_app_name }}',
'{{ source_control_name }}',
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
- name: container_apps_source_controls
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the container_apps_source_controls resource.
    - name: container_app_name
      value: "{{ container_app_name }}"
      description: Required parameter for the container_apps_source_controls resource.
    - name: source_control_name
      value: "{{ source_control_name }}"
      description: Required parameter for the container_apps_source_controls resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the container_apps_source_controls resource.
    - name: properties
      description: |
        SourceControl resource specific properties.
      value:
        operationState: "{{ operationState }}"
        repoUrl: "{{ repoUrl }}"
        branch: "{{ branch }}"
        githubActionConfiguration:
          registryInfo:
            registryUrl: "{{ registryUrl }}"
            registryUserName: "{{ registryUserName }}"
            registryPassword: "{{ registryPassword }}"
          azureCredentials:
            clientId: "{{ clientId }}"
            clientSecret: "{{ clientSecret }}"
            tenantId: "{{ tenantId }}"
            kind: "{{ kind }}"
            subscriptionId: "{{ subscriptionId }}"
          contextPath: "{{ contextPath }}"
          githubPersonalAccessToken: "{{ githubPersonalAccessToken }}"
          image: "{{ image }}"
          publishType: "{{ publishType }}"
          os: "{{ os }}"
          runtimeStack: "{{ runtimeStack }}"
          runtimeVersion: "{{ runtimeVersion }}"
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

Create or update the SourceControl for a Container App. Create or update the SourceControl for a Container App.

```sql
REPLACE azure.app_containers.container_apps_source_controls
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND source_control_name = '{{ source_control_name }}' --required
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

Delete a Container App SourceControl. Delete a Container App SourceControl.

```sql
DELETE FROM azure.app_containers.container_apps_source_controls
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND source_control_name = '{{ source_control_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
