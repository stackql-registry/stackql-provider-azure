--- 
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="projects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.projects" /></td></tr>
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
    <td><CopyableCode code="azureAuthenticationInfo" /></td>
    <td><code>object</code></td>
    <td>Field that defines the Azure active directory application info, used to connect to the target Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>UTC Date and time when project was created.</td>
</tr>
<tr>
    <td><CopyableCode code="databasesInfo" /></td>
    <td><code>array</code></td>
    <td>List of DatabaseInfo.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The project's provisioning state. Known values are: "Deleting" and "Succeeded". (Deleting, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceConnectionInfo" /></td>
    <td><code>object</code></td>
    <td>Information for connecting to source.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePlatform" /></td>
    <td><code>string</code></td>
    <td>Source platform for the project. Required. Known values are: "SQL", "MySQL", "PostgreSql", "MongoDb", and "Unknown". (SQL, MySQL, PostgreSql, MongoDb, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
</tr>
<tr>
    <td><CopyableCode code="targetConnectionInfo" /></td>
    <td><code>object</code></td>
    <td>Information for connecting to target.</td>
</tr>
<tr>
    <td><CopyableCode code="targetPlatform" /></td>
    <td><code>string</code></td>
    <td>Target platform for the project. Required. Known values are: "SQLDB", "SQLMI", "AzureDbForMySql", "AzureDbForPostgreSql", "MongoDb", and "Unknown". (SQLDB, SQLMI, AzureDbForMySql, AzureDbForPostgreSql, MongoDb, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="azureAuthenticationInfo" /></td>
    <td><code>object</code></td>
    <td>Field that defines the Azure active directory application info, used to connect to the target Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>UTC Date and time when project was created.</td>
</tr>
<tr>
    <td><CopyableCode code="databasesInfo" /></td>
    <td><code>array</code></td>
    <td>List of DatabaseInfo.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The project's provisioning state. Known values are: "Deleting" and "Succeeded". (Deleting, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceConnectionInfo" /></td>
    <td><code>object</code></td>
    <td>Information for connecting to source.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePlatform" /></td>
    <td><code>string</code></td>
    <td>Source platform for the project. Required. Known values are: "SQL", "MySQL", "PostgreSql", "MongoDb", and "Unknown". (SQL, MySQL, PostgreSql, MongoDb, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
</tr>
<tr>
    <td><CopyableCode code="targetConnectionInfo" /></td>
    <td><code>object</code></td>
    <td>Information for connecting to target.</td>
</tr>
<tr>
    <td><CopyableCode code="targetPlatform" /></td>
    <td><code>string</code></td>
    <td>Target platform for the project. Required. Known values are: "SQLDB", "SQLMI", "AzureDbForMySql", "AzureDbForPostgreSql", "MongoDb", and "Unknown". (SQLDB, SQLMI, AzureDbForMySql, AzureDbForPostgreSql, MongoDb, Unknown)</td>
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
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get project information. The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get projects in a service. The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update project. The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update project. The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update project. The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteRunningTasks"><code>deleteRunningTasks</code></a></td>
    <td>Delete project. The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project.</td>
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
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>Name of the service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-deleteRunningTasks">
    <td><CopyableCode code="deleteRunningTasks" /></td>
    <td><code>boolean</code></td>
    <td>Delete the resource even if it contains running tasks. Default value is None.</td>
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

Get project information. The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.

```sql
SELECT
id,
name,
azureAuthenticationInfo,
creationTime,
databasesInfo,
etag,
location,
provisioningState,
sourceConnectionInfo,
sourcePlatform,
systemData,
tags,
targetConnectionInfo,
targetPlatform,
type
FROM azure.data_migration.projects
WHERE group_name = '{{ group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get projects in a service. The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource.

```sql
SELECT
id,
name,
azureAuthenticationInfo,
creationTime,
databasesInfo,
etag,
location,
provisioningState,
sourceConnectionInfo,
sourcePlatform,
systemData,
tags,
targetConnectionInfo,
targetPlatform,
type
FROM azure.data_migration.projects
WHERE group_name = '{{ group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
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

Create or update project. The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one.

```sql
INSERT INTO azure.data_migration.projects (
properties,
etag,
location,
tags,
group_name,
service_name,
project_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ location }}',
'{{ tags }}',
'{{ group_name }}',
'{{ service_name }}',
'{{ project_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: projects
  props:
    - name: group_name
      value: "{{ group_name }}"
      description: Required parameter for the projects resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the projects resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the projects resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the projects resource.
    - name: properties
      description: |
        Project properties.
      value:
        sourcePlatform: "{{ sourcePlatform }}"
        azureAuthenticationInfo:
          applicationId: "{{ applicationId }}"
          appKey: "{{ appKey }}"
          tenantId: "{{ tenantId }}"
          ignoreAzurePermissions: {{ ignoreAzurePermissions }}
        targetPlatform: "{{ targetPlatform }}"
        creationTime: "{{ creationTime }}"
        sourceConnectionInfo:
          type: "{{ type }}"
          userName: "{{ userName }}"
          password: "{{ password }}"
        targetConnectionInfo:
          type: "{{ type }}"
          userName: "{{ userName }}"
          password: "{{ password }}"
        databasesInfo:
          - sourceDatabaseName: "{{ sourceDatabaseName }}"
        provisioningState: "{{ provisioningState }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        HTTP strong entity tag value. This is ignored if submitted.
    - name: location
      value: "{{ location }}"
      description: |
        :vartype location: str
    - name: tags
      value: "{{ tags }}"
      description: |
        :vartype tags: dict[str, str]
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

Update project. The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project.

```sql
UPDATE azure.data_migration.projects
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Create or update project. The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one.

```sql
REPLACE azure.data_migration.projects
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Delete project. The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project.

```sql
DELETE FROM azure.data_migration.projects
WHERE group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteRunningTasks = '{{ deleteRunningTasks }}'
;
```
</TabItem>
</Tabs>
