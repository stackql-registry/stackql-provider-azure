--- 
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - neonpostgres
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.neonpostgres.projects" /></td></tr>
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
    <td><CopyableCode code="attributes" /></td>
    <td><code>array</code></td>
    <td>Additional attributes for the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="branch" /></td>
    <td><code>object</code></td>
    <td>The Branch properties of the project. This is optional.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string</code></td>
    <td>Timestamp indicating when the entity was created.</td>
</tr>
<tr>
    <td><CopyableCode code="databases" /></td>
    <td><code>array</code></td>
    <td>Neon Databases associated with the project.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultEndpointSettings" /></td>
    <td><code>object</code></td>
    <td>Default endpoint settings for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>Endpoints associated with the project.</td>
</tr>
<tr>
    <td><CopyableCode code="entityId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="entityName" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="historyRetention" /></td>
    <td><code>integer</code></td>
    <td>The retention period for project history in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="pgVersion" /></td>
    <td><code>integer</code></td>
    <td>Postgres version for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="regionId" /></td>
    <td><code>string</code></td>
    <td>Region where the project is created.</td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>Roles associated with the project.</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>integer</code></td>
    <td>Data Storage bytes per hour for the project.</td>
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
    <td><CopyableCode code="attributes" /></td>
    <td><code>array</code></td>
    <td>Additional attributes for the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="branch" /></td>
    <td><code>object</code></td>
    <td>The Branch properties of the project. This is optional.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string</code></td>
    <td>Timestamp indicating when the entity was created.</td>
</tr>
<tr>
    <td><CopyableCode code="databases" /></td>
    <td><code>array</code></td>
    <td>Neon Databases associated with the project.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultEndpointSettings" /></td>
    <td><code>object</code></td>
    <td>Default endpoint settings for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>Endpoints associated with the project.</td>
</tr>
<tr>
    <td><CopyableCode code="entityId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="entityName" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="historyRetention" /></td>
    <td><code>integer</code></td>
    <td>The retention period for project history in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="pgVersion" /></td>
    <td><code>integer</code></td>
    <td>Postgres version for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="regionId" /></td>
    <td><code>string</code></td>
    <td>Region where the project is created.</td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>Roles associated with the project.</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>integer</code></td>
    <td>Data Storage bytes per hour for the project.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Project.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Project resources by OrganizationResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Project.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Project.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Project.</td>
</tr>
<tr>
    <td><a href="#get_connection_uri"><CopyableCode code="get_connection_uri" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Action to retrieve the connection URI for the Neon Database.</td>
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
<tr id="parameter-organization_name">
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Neon Organizations resource. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Project. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a Project.

```sql
SELECT
id,
name,
attributes,
branch,
createdAt,
databases,
defaultEndpointSettings,
endpoints,
entityId,
entityName,
historyRetention,
pgVersion,
provisioningState,
regionId,
roles,
storage,
systemData,
type
FROM azure_isv.neonpostgres.projects
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Project resources by OrganizationResource.

```sql
SELECT
id,
name,
attributes,
branch,
createdAt,
databases,
defaultEndpointSettings,
endpoints,
entityId,
entityName,
historyRetention,
pgVersion,
provisioningState,
regionId,
roles,
storage,
systemData,
type
FROM azure_isv.neonpostgres.projects
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
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

Create a Project.

```sql
INSERT INTO azure_isv.neonpostgres.projects (
properties,
resource_group_name,
organization_name,
project_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ organization_name }}',
'{{ project_name }}',
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
- name: projects
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the projects resource.
    - name: organization_name
      value: "{{ organization_name }}"
      description: Required parameter for the projects resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the projects resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the projects resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        entityId: "{{ entityId }}"
        entityName: "{{ entityName }}"
        createdAt: "{{ createdAt }}"
        provisioningState: "{{ provisioningState }}"
        attributes:
          - name: "{{ name }}"
            value: "{{ value }}"
        regionId: "{{ regionId }}"
        storage: {{ storage }}
        pgVersion: {{ pgVersion }}
        historyRetention: {{ historyRetention }}
        defaultEndpointSettings:
          autoscalingLimitMinCu: {{ autoscalingLimitMinCu }}
          autoscalingLimitMaxCu: {{ autoscalingLimitMaxCu }}
        branch:
          entityId: "{{ entityId }}"
          entityName: "{{ entityName }}"
          createdAt: "{{ createdAt }}"
          provisioningState: "{{ provisioningState }}"
          attributes:
            - name: "{{ name }}"
              value: "{{ value }}"
          projectId: "{{ projectId }}"
          parentId: "{{ parentId }}"
          roleName: "{{ roleName }}"
          databaseName: "{{ databaseName }}"
          roles:
            - entityId: "{{ entityId }}"
              entityName: "{{ entityName }}"
              createdAt: "{{ createdAt }}"
              provisioningState: "{{ provisioningState }}"
              attributes: "{{ attributes }}"
              branchId: "{{ branchId }}"
              permissions: "{{ permissions }}"
              isSuperUser: {{ isSuperUser }}
          databases:
            - entityId: "{{ entityId }}"
              entityName: "{{ entityName }}"
              createdAt: "{{ createdAt }}"
              provisioningState: "{{ provisioningState }}"
              attributes: "{{ attributes }}"
              branchId: "{{ branchId }}"
              ownerName: "{{ ownerName }}"
          endpoints:
            - entityId: "{{ entityId }}"
              entityName: "{{ entityName }}"
              createdAt: "{{ createdAt }}"
              provisioningState: "{{ provisioningState }}"
              attributes: "{{ attributes }}"
              projectId: "{{ projectId }}"
              branchId: "{{ branchId }}"
              endpointType: "{{ endpointType }}"
        roles:
          - entityId: "{{ entityId }}"
            entityName: "{{ entityName }}"
            createdAt: "{{ createdAt }}"
            provisioningState: "{{ provisioningState }}"
            attributes: "{{ attributes }}"
            branchId: "{{ branchId }}"
            permissions: "{{ permissions }}"
            isSuperUser: {{ isSuperUser }}
        databases:
          - entityId: "{{ entityId }}"
            entityName: "{{ entityName }}"
            createdAt: "{{ createdAt }}"
            provisioningState: "{{ provisioningState }}"
            attributes: "{{ attributes }}"
            branchId: "{{ branchId }}"
            ownerName: "{{ ownerName }}"
        endpoints:
          - entityId: "{{ entityId }}"
            entityName: "{{ entityName }}"
            createdAt: "{{ createdAt }}"
            provisioningState: "{{ provisioningState }}"
            attributes: "{{ attributes }}"
            projectId: "{{ projectId }}"
            branchId: "{{ branchId }}"
            endpointType: "{{ endpointType }}"
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

Update a Project.

```sql
UPDATE azure_isv.neonpostgres.projects
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND project_name = '{{ project_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a Project.

```sql
REPLACE azure_isv.neonpostgres.projects
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND project_name = '{{ project_name }}' --required
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

Delete a Project.

```sql
DELETE FROM azure_isv.neonpostgres.projects
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND project_name = '{{ project_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_connection_uri"
    values={[
        { label: 'get_connection_uri', value: 'get_connection_uri' }
    ]}
>
<TabItem value="get_connection_uri">

Action to retrieve the connection URI for the Neon Database.

```sql
EXEC azure_isv.neonpostgres.projects.get_connection_uri 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"projectId": "{{ projectId }}", 
"branchId": "{{ branchId }}", 
"databaseName": "{{ databaseName }}", 
"roleName": "{{ roleName }}", 
"endpointId": "{{ endpointId }}", 
"isPooled": {{ isPooled }}
}'
;
```
</TabItem>
</Tabs>
