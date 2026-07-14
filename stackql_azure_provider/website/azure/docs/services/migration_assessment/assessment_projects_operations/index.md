--- 
title: assessment_projects_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_projects_operations
  - migration_assessment
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

Creates, updates, deletes, gets or lists an <code>assessment_projects_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assessment_projects_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migration_assessment.assessment_projects_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentSolutionId" /></td>
    <td><code>string</code></td>
    <td>Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this project was created. Date-Time represented in ISO-8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="customerStorageAccountArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM id of the storage account used for interactions when public access is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="customerWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The ARM id of service map workspace created by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerWorkspaceLocation" /></td>
    <td><code>string</code></td>
    <td>Location of service map workspace created by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections to the project.</td>
</tr>
<tr>
    <td><CopyableCode code="projectStatus" /></td>
    <td><code>string</code></td>
    <td>Assessment project status. Known values are: "Active" and "Inactive".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint at which the collector agent can call agent REST API.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this project was last updated. Date-Time represented in ISO-8601 format.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentSolutionId" /></td>
    <td><code>string</code></td>
    <td>Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this project was created. Date-Time represented in ISO-8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="customerStorageAccountArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM id of the storage account used for interactions when public access is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="customerWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The ARM id of service map workspace created by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerWorkspaceLocation" /></td>
    <td><code>string</code></td>
    <td>Location of service map workspace created by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections to the project.</td>
</tr>
<tr>
    <td><CopyableCode code="projectStatus" /></td>
    <td><code>string</code></td>
    <td>Assessment project status. Known values are: "Active" and "Inactive".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint at which the collector agent can call agent REST API.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this project was last updated. Date-Time represented in ISO-8601 format.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentSolutionId" /></td>
    <td><code>string</code></td>
    <td>Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this project was created. Date-Time represented in ISO-8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="customerStorageAccountArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM id of the storage account used for interactions when public access is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="customerWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The ARM id of service map workspace created by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerWorkspaceLocation" /></td>
    <td><code>string</code></td>
    <td>Location of service map workspace created by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections to the project.</td>
</tr>
<tr>
    <td><CopyableCode code="projectStatus" /></td>
    <td><code>string</code></td>
    <td>Assessment project status. Known values are: "Active" and "Inactive".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint at which the collector agent can call agent REST API.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this project was last updated. Date-Time represented in ISO-8601 format.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AssessmentProject.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AssessmentProject resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AssessmentProject resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a AssessmentProject.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a AssessmentProject.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a AssessmentProject.</td>
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
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Assessment Project Name. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a AssessmentProject.

```sql
SELECT
id,
name,
assessmentSolutionId,
createdTimestamp,
customerStorageAccountArmId,
customerWorkspaceId,
customerWorkspaceLocation,
location,
privateEndpointConnections,
projectStatus,
provisioningState,
publicNetworkAccess,
serviceEndpoint,
systemData,
tags,
type,
updatedTimestamp
FROM azure.migration_assessment.assessment_projects_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List AssessmentProject resources by resource group.

```sql
SELECT
id,
name,
assessmentSolutionId,
createdTimestamp,
customerStorageAccountArmId,
customerWorkspaceId,
customerWorkspaceLocation,
location,
privateEndpointConnections,
projectStatus,
provisioningState,
publicNetworkAccess,
serviceEndpoint,
systemData,
tags,
type,
updatedTimestamp
FROM azure.migration_assessment.assessment_projects_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List AssessmentProject resources by subscription ID.

```sql
SELECT
id,
name,
assessmentSolutionId,
createdTimestamp,
customerStorageAccountArmId,
customerWorkspaceId,
customerWorkspaceLocation,
location,
privateEndpointConnections,
projectStatus,
provisioningState,
publicNetworkAccess,
serviceEndpoint,
systemData,
tags,
type,
updatedTimestamp
FROM azure.migration_assessment.assessment_projects_operations
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a AssessmentProject.

```sql
INSERT INTO azure.migration_assessment.assessment_projects_operations (
tags,
location,
properties,
resource_group_name,
project_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ project_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: assessment_projects_operations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the assessment_projects_operations resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the assessment_projects_operations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the assessment_projects_operations resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        createdTimestamp: "{{ createdTimestamp }}"
        updatedTimestamp: "{{ updatedTimestamp }}"
        serviceEndpoint: "{{ serviceEndpoint }}"
        assessmentSolutionId: "{{ assessmentSolutionId }}"
        projectStatus: "{{ projectStatus }}"
        customerWorkspaceId: "{{ customerWorkspaceId }}"
        customerWorkspaceLocation: "{{ customerWorkspaceLocation }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              groupIds:
                - "{{ groupIds }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        customerStorageAccountArmId: "{{ customerStorageAccountArmId }}"
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

Update a AssessmentProject.

```sql
UPDATE azure.migration_assessment.assessment_projects_operations
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND project_name = '{{ project_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete a AssessmentProject.

```sql
DELETE FROM azure.migration_assessment.assessment_projects_operations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND project_name = '{{ project_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
