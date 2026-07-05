--- 
title: attached_database_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_database_configurations
  - kusto
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

Creates, updates, deletes, gets or lists an <code>attached_database_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="attached_database_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kusto.attached_database_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cluster', value: 'list_by_cluster' }
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
    <td><CopyableCode code="attachedDatabaseNames" /></td>
    <td><code>array</code></td>
    <td>The list of databases from the clusterResourceId which are currently attached to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the cluster where the databases you would like to attach reside. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database which you would like to attach, use * if you want to follow all current and future databases. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseNameOverride" /></td>
    <td><code>string</code></td>
    <td>Overrides the original database name. Relevant only when attaching to a specific database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseNamePrefix" /></td>
    <td><code>string</code></td>
    <td>Adds a prefix to the attached databases name. When following an entire cluster, that prefix would be added to all of the databases original names from leader cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPrincipalsModificationKind" /></td>
    <td><code>string</code></td>
    <td>The default principals modification kind. Required. Known values are: "Union", "Replace", and "None". (Union, Replace, None)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled". (Running, Creating, Deleting, Succeeded, Failed, Moving, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tableLevelSharingProperties" /></td>
    <td><code>object</code></td>
    <td>Table level sharing specifications.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_cluster">

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
    <td><CopyableCode code="attachedDatabaseNames" /></td>
    <td><code>array</code></td>
    <td>The list of databases from the clusterResourceId which are currently attached to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the cluster where the databases you would like to attach reside. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database which you would like to attach, use * if you want to follow all current and future databases. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseNameOverride" /></td>
    <td><code>string</code></td>
    <td>Overrides the original database name. Relevant only when attaching to a specific database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseNamePrefix" /></td>
    <td><code>string</code></td>
    <td>Adds a prefix to the attached databases name. When following an entire cluster, that prefix would be added to all of the databases original names from leader cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPrincipalsModificationKind" /></td>
    <td><code>string</code></td>
    <td>The default principals modification kind. Required. Known values are: "Union", "Replace", and "None". (Union, Replace, None)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled". (Running, Creating, Deleting, Succeeded, Failed, Moving, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tableLevelSharingProperties" /></td>
    <td><code>object</code></td>
    <td>Table level sharing specifications.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-attached_database_configuration_name"><code>attached_database_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns an attached database configuration.</td>
</tr>
<tr>
    <td><a href="#list_by_cluster"><CopyableCode code="list_by_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the list of attached database configurations of the given Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-attached_database_configuration_name"><code>attached_database_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an attached database configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-attached_database_configuration_name"><code>attached_database_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an attached database configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-attached_database_configuration_name"><code>attached_database_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the attached database configuration with the given name.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Checks that the attached database configuration resource name is valid and is not already in use.</td>
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
<tr id="parameter-attached_database_configuration_name">
    <td><CopyableCode code="attached_database_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the attached database configuration. Required.</td>
</tr>
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Kusto cluster. Required.</td>
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
        { label: 'list_by_cluster', value: 'list_by_cluster' }
    ]}
>
<TabItem value="get">

Returns an attached database configuration.

```sql
SELECT
id,
name,
attachedDatabaseNames,
clusterResourceId,
databaseName,
databaseNameOverride,
databaseNamePrefix,
defaultPrincipalsModificationKind,
location,
provisioningState,
systemData,
tableLevelSharingProperties,
type
FROM azure.kusto.attached_database_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND attached_database_configuration_name = '{{ attached_database_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cluster">

Returns the list of attached database configurations of the given Kusto cluster.

```sql
SELECT
id,
name,
attachedDatabaseNames,
clusterResourceId,
databaseName,
databaseNameOverride,
databaseNamePrefix,
defaultPrincipalsModificationKind,
location,
provisioningState,
systemData,
tableLevelSharingProperties,
type
FROM azure.kusto.attached_database_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
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

Creates or updates an attached database configuration.

```sql
INSERT INTO azure.kusto.attached_database_configurations (
properties,
location,
resource_group_name,
cluster_name,
attached_database_configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ attached_database_configuration_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: attached_database_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the attached_database_configurations resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the attached_database_configurations resource.
    - name: attached_database_configuration_name
      value: "{{ attached_database_configuration_name }}"
      description: Required parameter for the attached_database_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the attached_database_configurations resource.
    - name: properties
      description: |
        The properties of the attached database configuration.
      value:
        provisioningState: "{{ provisioningState }}"
        databaseName: "{{ databaseName }}"
        clusterResourceId: "{{ clusterResourceId }}"
        attachedDatabaseNames:
          - "{{ attachedDatabaseNames }}"
        defaultPrincipalsModificationKind: "{{ defaultPrincipalsModificationKind }}"
        tableLevelSharingProperties:
          tablesToInclude:
            - "{{ tablesToInclude }}"
          tablesToExclude:
            - "{{ tablesToExclude }}"
          externalTablesToInclude:
            - "{{ externalTablesToInclude }}"
          externalTablesToExclude:
            - "{{ externalTablesToExclude }}"
          materializedViewsToInclude:
            - "{{ materializedViewsToInclude }}"
          materializedViewsToExclude:
            - "{{ materializedViewsToExclude }}"
          functionsToInclude:
            - "{{ functionsToInclude }}"
          functionsToExclude:
            - "{{ functionsToExclude }}"
        databaseNameOverride: "{{ databaseNameOverride }}"
        databaseNamePrefix: "{{ databaseNamePrefix }}"
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
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

Creates or updates an attached database configuration.

```sql
REPLACE azure.kusto.attached_database_configurations
SET 
properties = '{{ properties }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND attached_database_configuration_name = '{{ attached_database_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Deletes the attached database configuration with the given name.

```sql
DELETE FROM azure.kusto.attached_database_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND attached_database_configuration_name = '{{ attached_database_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="check_name_availability">

Checks that the attached database configuration resource name is valid and is not already in use.

```sql
EXEC azure.kusto.attached_database_configurations.check_name_availability 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
