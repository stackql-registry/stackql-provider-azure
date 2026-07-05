--- 
title: module
hide_title: false
hide_table_of_contents: false
keywords:
  - module
  - automation
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

Creates, updates, deletes, gets or lists a <code>module</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="module" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.module" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
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
    <td><CopyableCode code="activityCount" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the activity count of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="contentLink" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the contentLink of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the description.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the error info of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the etag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isComposite" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets type of module, if its composite or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isGlobal" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets the isGlobal flag of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last modified time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the module. Known values are: "Created", "Creating", "StartingImportModuleRunbook", "RunningImportModuleRunbook", "ContentRetrieved", "ContentDownloaded", "ContentValidated", "ConnectionTypeImported", "ContentStored", "ModuleDataStored", "ActivitiesStored", "ModuleImportRunbookComplete", "Succeeded", "Failed", "Canceled", and "Updating". (Created, Creating, StartingImportModuleRunbook, RunningImportModuleRunbook, ContentRetrieved, ContentDownloaded, ContentValidated, ConnectionTypeImported, ContentStored, ModuleDataStored, ActivitiesStored, ModuleImportRunbookComplete, Succeeded, Failed, Canceled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the size in bytes of the module.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the version of the module.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_automation_account">

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
    <td><CopyableCode code="activityCount" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the activity count of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="contentLink" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the contentLink of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the description.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the error info of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the etag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isComposite" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets type of module, if its composite or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isGlobal" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets the isGlobal flag of the module.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last modified time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the module. Known values are: "Created", "Creating", "StartingImportModuleRunbook", "RunningImportModuleRunbook", "ContentRetrieved", "ContentDownloaded", "ContentValidated", "ConnectionTypeImported", "ContentStored", "ModuleDataStored", "ActivitiesStored", "ModuleImportRunbookComplete", "Succeeded", "Failed", "Canceled", and "Updating". (Created, Creating, StartingImportModuleRunbook, RunningImportModuleRunbook, ContentRetrieved, ContentDownloaded, ContentValidated, ConnectionTypeImported, ContentStored, ModuleDataStored, ActivitiesStored, ModuleImportRunbookComplete, Succeeded, Failed, Canceled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the size in bytes of the module.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the version of the module.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-module_name"><code>module_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the module identified by module name.</td>
</tr>
<tr>
    <td><a href="#list_by_automation_account"><CopyableCode code="list_by_automation_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a list of modules.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-module_name"><code>module_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or Update the module identified by module name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-module_name"><code>module_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the module identified by module name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-module_name"><code>module_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or Update the module identified by module name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-module_name"><code>module_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the module by name.</td>
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
<tr id="parameter-automation_account_name">
    <td><CopyableCode code="automation_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the automation account. Required.</td>
</tr>
<tr id="parameter-module_name">
    <td><CopyableCode code="module_name" /></td>
    <td><code>string</code></td>
    <td>The module name. Required.</td>
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
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
    ]}
>
<TabItem value="get">

Retrieve the module identified by module name.

```sql
SELECT
id,
name,
activityCount,
contentLink,
creationTime,
description,
error,
etag,
isComposite,
isGlobal,
lastModifiedTime,
location,
provisioningState,
sizeInBytes,
systemData,
tags,
type,
version
FROM azure.automation.module
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND module_name = '{{ module_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_automation_account">

Retrieve a list of modules.

```sql
SELECT
id,
name,
activityCount,
contentLink,
creationTime,
description,
error,
etag,
isComposite,
isGlobal,
lastModifiedTime,
location,
provisioningState,
sizeInBytes,
systemData,
tags,
type,
version
FROM azure.automation.module
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
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

Create or Update the module identified by module name.

```sql
INSERT INTO azure.automation.module (
properties,
name,
location,
tags,
resource_group_name,
automation_account_name,
module_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ name }}',
'{{ location }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ automation_account_name }}',
'{{ module_name }}',
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
- name: module
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the module resource.
    - name: automation_account_name
      value: "{{ automation_account_name }}"
      description: Required parameter for the module resource.
    - name: module_name
      value: "{{ module_name }}"
      description: Required parameter for the module resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the module resource.
    - name: properties
      description: |
        Gets or sets the module create properties. Required.
      value:
        contentLink:
          uri: "{{ uri }}"
          contentHash:
            algorithm: "{{ algorithm }}"
            value: "{{ value }}"
          version: "{{ version }}"
    - name: name
      value: "{{ name }}"
      description: |
        Gets or sets name of the resource.
    - name: location
      value: "{{ location }}"
      description: |
        Gets or sets the location of the resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Gets or sets the tags attached to the resource.
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

Update the module identified by module name.

```sql
UPDATE azure.automation.module
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND module_name = '{{ module_name }}' --required
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

Create or Update the module identified by module name.

```sql
REPLACE azure.automation.module
SET 
properties = '{{ properties }}',
name = '{{ name }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND module_name = '{{ module_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Delete the module by name.

```sql
DELETE FROM azure.automation.module
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND module_name = '{{ module_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
