--- 
title: package
hide_title: false
hide_table_of_contents: false
keywords:
  - package
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

Creates, updates, deletes, gets or lists a <code>package</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="package" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.package" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_runtime_environment', value: 'list_by_runtime_environment' }
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
    <td><CopyableCode code="allOf" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentLink" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the contentLink of the Package.</td>
</tr>
<tr>
    <td><CopyableCode code="default" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets the isGlobal flag of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the error info of the Package.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the Package. Known values are: "Created", "Creating", "StartingImportModuleRunbook", "RunningImportModuleRunbook", "ContentRetrieved", "ContentDownloaded", "ContentValidated", "ConnectionTypeImported", "ContentStored", "ModuleDataStored", "ActivitiesStored", "ModuleImportRunbookComplete", "Succeeded", "Failed", "Canceled", and "Updating". (Created, Creating, StartingImportModuleRunbook, RunningImportModuleRunbook, ContentRetrieved, ContentDownloaded, ContentValidated, ConnectionTypeImported, ContentStored, ModuleDataStored, ActivitiesStored, ModuleImportRunbookComplete, Succeeded, Failed, Canceled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the size in bytes of the Package.</td>
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
    <td>Gets or sets the version of the Package.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_runtime_environment">

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
    <td><CopyableCode code="allOf" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentLink" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the contentLink of the Package.</td>
</tr>
<tr>
    <td><CopyableCode code="default" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets the isGlobal flag of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the error info of the Package.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the Package. Known values are: "Created", "Creating", "StartingImportModuleRunbook", "RunningImportModuleRunbook", "ContentRetrieved", "ContentDownloaded", "ContentValidated", "ConnectionTypeImported", "ContentStored", "ModuleDataStored", "ActivitiesStored", "ModuleImportRunbookComplete", "Succeeded", "Failed", "Canceled", and "Updating". (Created, Creating, StartingImportModuleRunbook, RunningImportModuleRunbook, ContentRetrieved, ContentDownloaded, ContentValidated, ConnectionTypeImported, ContentStored, ModuleDataStored, ActivitiesStored, ModuleImportRunbookComplete, Succeeded, Failed, Canceled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the size in bytes of the Package.</td>
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
    <td>Gets or sets the version of the Package.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runtime_environment_name"><code>runtime_environment_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the Package identified by Package name.</td>
</tr>
<tr>
    <td><a href="#list_by_runtime_environment"><CopyableCode code="list_by_runtime_environment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runtime_environment_name"><code>runtime_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the a list of Packages.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runtime_environment_name"><code>runtime_environment_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the package identified by package name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runtime_environment_name"><code>runtime_environment_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the Package identified by Package name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runtime_environment_name"><code>runtime_environment_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the package identified by package name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runtime_environment_name"><code>runtime_environment_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the package by name.</td>
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
<tr id="parameter-package_name">
    <td><CopyableCode code="package_name" /></td>
    <td><code>string</code></td>
    <td>The Package name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-runtime_environment_name">
    <td><CopyableCode code="runtime_environment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Runtime Environment. Required.</td>
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
        { label: 'list_by_runtime_environment', value: 'list_by_runtime_environment' }
    ]}
>
<TabItem value="get">

Retrieve the Package identified by Package name.

```sql
SELECT
id,
name,
allOf,
contentLink,
default,
error,
location,
provisioningState,
sizeInBytes,
systemData,
tags,
type,
version
FROM azure.automation.package
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND runtime_environment_name = '{{ runtime_environment_name }}' -- required
AND package_name = '{{ package_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_runtime_environment">

Retrieve the a list of Packages.

```sql
SELECT
id,
name,
allOf,
contentLink,
default,
error,
location,
provisioningState,
sizeInBytes,
systemData,
tags,
type,
version
FROM azure.automation.package
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND runtime_environment_name = '{{ runtime_environment_name }}' -- required
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

Create or update the package identified by package name.

```sql
INSERT INTO azure.automation.package (
properties,
allOf,
resource_group_name,
automation_account_name,
runtime_environment_name,
package_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ allOf }}',
'{{ resource_group_name }}',
'{{ automation_account_name }}',
'{{ runtime_environment_name }}',
'{{ package_name }}',
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
- name: package
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the package resource.
    - name: automation_account_name
      value: "{{ automation_account_name }}"
      description: Required parameter for the package resource.
    - name: runtime_environment_name
      value: "{{ runtime_environment_name }}"
      description: Required parameter for the package resource.
    - name: package_name
      value: "{{ package_name }}"
      description: Required parameter for the package resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the package resource.
    - name: properties
      description: |
        Gets or sets the package create properties. Required.
      value:
        contentLink:
          uri: "{{ uri }}"
          contentHash:
            algorithm: "{{ algorithm }}"
            value: "{{ value }}"
          version: "{{ version }}"
    - name: allOf
      description: |
        The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.
      value:
        id: "{{ id }}"
        name: "{{ name }}"
        type: "{{ type }}"
        systemData:
          createdBy: "{{ createdBy }}"
          createdByType: "{{ createdByType }}"
          createdAt: "{{ createdAt }}"
          lastModifiedBy: "{{ lastModifiedBy }}"
          lastModifiedByType: "{{ lastModifiedByType }}"
          lastModifiedAt: "{{ lastModifiedAt }}"
        tags: "{{ tags }}"
        location: "{{ location }}"
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

Update the Package identified by Package name.

```sql
UPDATE azure.automation.package
SET 
properties = '{{ properties }}',
allOf = '{{ allOf }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND runtime_environment_name = '{{ runtime_environment_name }}' --required
AND package_name = '{{ package_name }}' --required
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

Create or update the package identified by package name.

```sql
REPLACE azure.automation.package
SET 
properties = '{{ properties }}',
allOf = '{{ allOf }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND runtime_environment_name = '{{ runtime_environment_name }}' --required
AND package_name = '{{ package_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Delete the package by name.

```sql
DELETE FROM azure.automation.package
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND runtime_environment_name = '{{ runtime_environment_name }}' --required
AND package_name = '{{ package_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
