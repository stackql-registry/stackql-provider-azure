--- 
title: iot_security_solution
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solution
  - security
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

Creates, updates, deletes, gets or lists an <code>iot_security_solution</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iot_security_solution" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.iot_security_solution" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalWorkspaces" /></td>
    <td><code>array</code></td>
    <td>List of additional workspaces.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDiscoveredResources" /></td>
    <td><code>array</code></td>
    <td>List of resources that were automatically discovered as relevant to the security solution.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledDataSources" /></td>
    <td><code>array</code></td>
    <td>Disabled data sources. Disabling these data sources compromises the system.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Resource display name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="export" /></td>
    <td><code>array</code></td>
    <td>List of additional options for exporting to workspace data.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubs" /></td>
    <td><code>array</code></td>
    <td>IoT Hub resource IDs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationsConfiguration" /></td>
    <td><code>array</code></td>
    <td>List of the configuration status for each recommendation type.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the IoT Security solution. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
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
    <td><CopyableCode code="unmaskedIpLoggingStatus" /></td>
    <td><code>string</code></td>
    <td>Unmasked IP address logging status. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="userDefinedResources" /></td>
    <td><code>object</code></td>
    <td>Properties of the IoT Security solution's user defined resources.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Workspace resource ID.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalWorkspaces" /></td>
    <td><code>array</code></td>
    <td>List of additional workspaces.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDiscoveredResources" /></td>
    <td><code>array</code></td>
    <td>List of resources that were automatically discovered as relevant to the security solution.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledDataSources" /></td>
    <td><code>array</code></td>
    <td>Disabled data sources. Disabling these data sources compromises the system.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Resource display name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="export" /></td>
    <td><code>array</code></td>
    <td>List of additional options for exporting to workspace data.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubs" /></td>
    <td><code>array</code></td>
    <td>IoT Hub resource IDs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationsConfiguration" /></td>
    <td><code>array</code></td>
    <td>List of the configuration status for each recommendation type.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the IoT Security solution. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
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
    <td><CopyableCode code="unmaskedIpLoggingStatus" /></td>
    <td><code>string</code></td>
    <td>Unmasked IP address logging status. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="userDefinedResources" /></td>
    <td><code>object</code></td>
    <td>Properties of the IoT Security solution's user defined resources.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Workspace resource ID.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalWorkspaces" /></td>
    <td><code>array</code></td>
    <td>List of additional workspaces.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDiscoveredResources" /></td>
    <td><code>array</code></td>
    <td>List of resources that were automatically discovered as relevant to the security solution.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledDataSources" /></td>
    <td><code>array</code></td>
    <td>Disabled data sources. Disabling these data sources compromises the system.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Resource display name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="export" /></td>
    <td><code>array</code></td>
    <td>List of additional options for exporting to workspace data.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubs" /></td>
    <td><code>array</code></td>
    <td>IoT Hub resource IDs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationsConfiguration" /></td>
    <td><code>array</code></td>
    <td>List of the configuration status for each recommendation type.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the IoT Security solution. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
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
    <td><CopyableCode code="unmaskedIpLoggingStatus" /></td>
    <td><code>string</code></td>
    <td>Unmasked IP address logging status. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="userDefinedResources" /></td>
    <td><code>object</code></td>
    <td>Properties of the IoT Security solution's user defined resources.</td>
</tr>
<tr>
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Workspace resource ID.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>User this method to get details of a specific IoT Security solution based on solution name.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Use this method to get the list IoT Security solutions organized by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Use this method to get the list of IoT Security solutions by subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Use this method to create or update yours IoT Security solution.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Use this method to update existing IoT Security solution tags or user defined resources. To update other fields use the CreateOrUpdate method.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Use this method to create or update yours IoT Security solution.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Use this method to delete yours IoT Security solution.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-solution_name">
    <td><CopyableCode code="solution_name" /></td>
    <td><code>string</code></td>
    <td>The name of the IoT Security solution. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter the IoT Security solution with OData syntax. Supports filtering by iotHubs. Default value is None.</td>
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

User this method to get details of a specific IoT Security solution based on solution name.

```sql
SELECT
id,
name,
additionalWorkspaces,
autoDiscoveredResources,
disabledDataSources,
displayName,
export,
iotHubs,
location,
recommendationsConfiguration,
status,
systemData,
tags,
type,
unmaskedIpLoggingStatus,
userDefinedResources,
workspace
FROM azure.security.iot_security_solution
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND solution_name = '{{ solution_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Use this method to get the list IoT Security solutions organized by resource group.

```sql
SELECT
id,
name,
additionalWorkspaces,
autoDiscoveredResources,
disabledDataSources,
displayName,
export,
iotHubs,
location,
recommendationsConfiguration,
status,
systemData,
tags,
type,
unmaskedIpLoggingStatus,
userDefinedResources,
workspace
FROM azure.security.iot_security_solution
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Use this method to get the list of IoT Security solutions by subscription.

```sql
SELECT
id,
name,
additionalWorkspaces,
autoDiscoveredResources,
disabledDataSources,
displayName,
export,
iotHubs,
location,
recommendationsConfiguration,
status,
systemData,
tags,
type,
unmaskedIpLoggingStatus,
userDefinedResources,
workspace
FROM azure.security.iot_security_solution
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Use this method to create or update yours IoT Security solution.

```sql
INSERT INTO azure.security.iot_security_solution (
properties,
tags,
location,
resource_group_name,
solution_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ solution_name }}',
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
- name: iot_security_solution
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the iot_security_solution resource.
    - name: solution_name
      value: "{{ solution_name }}"
      description: Required parameter for the iot_security_solution resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the iot_security_solution resource.
    - name: properties
      description: |
        Security Solution data.
      value:
        workspace: "{{ workspace }}"
        displayName: "{{ displayName }}"
        status: "{{ status }}"
        export:
          - "{{ export }}"
        disabledDataSources:
          - "{{ disabledDataSources }}"
        iotHubs:
          - "{{ iotHubs }}"
        userDefinedResources:
          query: "{{ query }}"
          querySubscriptions:
            - "{{ querySubscriptions }}"
        autoDiscoveredResources:
          - "{{ autoDiscoveredResources }}"
        recommendationsConfiguration:
          - recommendationType: "{{ recommendationType }}"
            name: "{{ name }}"
            status: "{{ status }}"
        unmaskedIpLoggingStatus: "{{ unmaskedIpLoggingStatus }}"
        additionalWorkspaces:
          - workspace: "{{ workspace }}"
            type: "{{ type }}"
            dataTypes: "{{ dataTypes }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
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

Use this method to update existing IoT Security solution tags or user defined resources. To update other fields use the CreateOrUpdate method.

```sql
UPDATE azure.security.iot_security_solution
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND solution_name = '{{ solution_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Use this method to create or update yours IoT Security solution.

```sql
REPLACE azure.security.iot_security_solution
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND solution_name = '{{ solution_name }}' --required
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

Use this method to delete yours IoT Security solution.

```sql
DELETE FROM azure.security.iot_security_solution
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND solution_name = '{{ solution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
