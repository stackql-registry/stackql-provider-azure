--- 
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
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

Creates, updates, deletes, gets or lists a <code>scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scripts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kusto.scripts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_database', value: 'list_by_database' }
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
    <td><CopyableCode code="continueOnErrors" /></td>
    <td><code>boolean</code></td>
    <td>Flag that indicates whether to continue if one of the command fails.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>A unique string. If changed the script will be applied again.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the managed identity to be used. When provided, the managed identity will be used to read the script content from the scriptUrl.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPermissionsAction" /></td>
    <td><code>string</code></td>
    <td>Indicates if the permissions for the script caller are kept following completion of the script. Known values are: "RetainPermissionOnScriptCompletion" and "RemovePermissionOnScriptCompletion". (RetainPermissionOnScriptCompletion, RemovePermissionOnScriptCompletion)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled". (Running, Creating, Deleting, Succeeded, Failed, Moving, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="scriptContent" /></td>
    <td><code>string</code></td>
    <td>The script content. This property should be used when the script is provide inline and not through file in a SA. Must not be used together with scriptUrl and scriptUrlSasToken properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scriptLevel" /></td>
    <td><code>string</code></td>
    <td>Differentiates between the type of script commands included - Database or Cluster. The default is Database. Known values are: "Database" and "Cluster". (Database, Cluster)</td>
</tr>
<tr>
    <td><CopyableCode code="scriptUrl" /></td>
    <td><code>string</code></td>
    <td>The url to the KQL script blob file. Must not be used together with scriptContent property.</td>
</tr>
<tr>
    <td><CopyableCode code="scriptUrlSasToken" /></td>
    <td><code>string</code></td>
    <td>The SaS token that provide read access to the file which contain the script. Must be provided when using scriptUrl property.</td>
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
<TabItem value="list_by_database">

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
    <td><CopyableCode code="continueOnErrors" /></td>
    <td><code>boolean</code></td>
    <td>Flag that indicates whether to continue if one of the command fails.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>A unique string. If changed the script will be applied again.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the managed identity to be used. When provided, the managed identity will be used to read the script content from the scriptUrl.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPermissionsAction" /></td>
    <td><code>string</code></td>
    <td>Indicates if the permissions for the script caller are kept following completion of the script. Known values are: "RetainPermissionOnScriptCompletion" and "RemovePermissionOnScriptCompletion". (RetainPermissionOnScriptCompletion, RemovePermissionOnScriptCompletion)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled". (Running, Creating, Deleting, Succeeded, Failed, Moving, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="scriptContent" /></td>
    <td><code>string</code></td>
    <td>The script content. This property should be used when the script is provide inline and not through file in a SA. Must not be used together with scriptUrl and scriptUrlSasToken properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scriptLevel" /></td>
    <td><code>string</code></td>
    <td>Differentiates between the type of script commands included - Database or Cluster. The default is Database. Known values are: "Database" and "Cluster". (Database, Cluster)</td>
</tr>
<tr>
    <td><CopyableCode code="scriptUrl" /></td>
    <td><code>string</code></td>
    <td>The url to the KQL script blob file. Must not be used together with scriptContent property.</td>
</tr>
<tr>
    <td><CopyableCode code="scriptUrlSasToken" /></td>
    <td><code>string</code></td>
    <td>The SaS token that provide read access to the file which contain the script. Must be provided when using scriptUrl property.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Kusto cluster database script.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the list of database scripts for given database.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a Kusto database script.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a database script.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a Kusto database script.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Kusto database script.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Checks that the script name is valid and is not already in use.</td>
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
    <td>The name of the Kusto cluster. Required.</td>
</tr>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database in the Kusto cluster. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Kusto database script. Required.</td>
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
        { label: 'list_by_database', value: 'list_by_database' }
    ]}
>
<TabItem value="get">

Gets a Kusto cluster database script.

```sql
SELECT
id,
name,
continueOnErrors,
forceUpdateTag,
managedIdentityResourceId,
principalPermissionsAction,
provisioningState,
scriptContent,
scriptLevel,
scriptUrl,
scriptUrlSasToken,
systemData,
type
FROM azure.kusto.scripts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND script_name = '{{ script_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_database">

Returns the list of database scripts for given database.

```sql
SELECT
id,
name,
continueOnErrors,
forceUpdateTag,
managedIdentityResourceId,
principalPermissionsAction,
provisioningState,
scriptContent,
scriptLevel,
scriptUrl,
scriptUrlSasToken,
systemData,
type
FROM azure.kusto.scripts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND database_name = '{{ database_name }}' -- required
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

Creates a Kusto database script.

```sql
INSERT INTO azure.kusto.scripts (
properties,
resource_group_name,
cluster_name,
database_name,
script_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ database_name }}',
'{{ script_name }}',
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
- name: scripts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the scripts resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the scripts resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the scripts resource.
    - name: script_name
      value: "{{ script_name }}"
      description: Required parameter for the scripts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the scripts resource.
    - name: properties
      description: |
        The database script.
      value:
        scriptUrl: "{{ scriptUrl }}"
        scriptUrlSasToken: "{{ scriptUrlSasToken }}"
        scriptContent: "{{ scriptContent }}"
        forceUpdateTag: "{{ forceUpdateTag }}"
        continueOnErrors: {{ continueOnErrors }}
        provisioningState: "{{ provisioningState }}"
        scriptLevel: "{{ scriptLevel }}"
        principalPermissionsAction: "{{ principalPermissionsAction }}"
        managedIdentityResourceId: "{{ managedIdentityResourceId }}"
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

Updates a database script.

```sql
UPDATE azure.kusto.scripts
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND database_name = '{{ database_name }}' --required
AND script_name = '{{ script_name }}' --required
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

Creates a Kusto database script.

```sql
REPLACE azure.kusto.scripts
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND database_name = '{{ database_name }}' --required
AND script_name = '{{ script_name }}' --required
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

Deletes a Kusto database script.

```sql
DELETE FROM azure.kusto.scripts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND database_name = '{{ database_name }}' --required
AND script_name = '{{ script_name }}' --required
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

Checks that the script name is valid and is not already in use.

```sql
EXEC azure.kusto.scripts.check_name_availability 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
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
