--- 
title: msix_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - msix_packages
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>msix_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="msix_packages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.msix_packages" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly Name to be displayed in the portal.</td>
</tr>
<tr>
    <td><CopyableCode code="imagePath" /></td>
    <td><code>string</code></td>
    <td>VHD/CIM image path on Network Share.</td>
</tr>
<tr>
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>Make this version of the package the active one across the hostpool.</td>
</tr>
<tr>
    <td><CopyableCode code="isRegularRegistration" /></td>
    <td><code>boolean</code></td>
    <td>Specifies how to register Package in feed.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date Package was last updated, found in the appxmanifest.xml.</td>
</tr>
<tr>
    <td><CopyableCode code="packageApplications" /></td>
    <td><code>array</code></td>
    <td>List of package applications.</td>
</tr>
<tr>
    <td><CopyableCode code="packageDependencies" /></td>
    <td><code>array</code></td>
    <td>List of package dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="packageFamilyName" /></td>
    <td><code>string</code></td>
    <td>Package Family Name from appxmanifest.xml. Contains Package Name and Publisher name.</td>
</tr>
<tr>
    <td><CopyableCode code="packageName" /></td>
    <td><code>string</code></td>
    <td>Package Name from appxmanifest.xml.</td>
</tr>
<tr>
    <td><CopyableCode code="packageRelativePath" /></td>
    <td><code>string</code></td>
    <td>Relative Path to the package inside the image.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Package version found in the appxmanifest.xml.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly Name to be displayed in the portal.</td>
</tr>
<tr>
    <td><CopyableCode code="imagePath" /></td>
    <td><code>string</code></td>
    <td>VHD/CIM image path on Network Share.</td>
</tr>
<tr>
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>Make this version of the package the active one across the hostpool.</td>
</tr>
<tr>
    <td><CopyableCode code="isRegularRegistration" /></td>
    <td><code>boolean</code></td>
    <td>Specifies how to register Package in feed.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date Package was last updated, found in the appxmanifest.xml.</td>
</tr>
<tr>
    <td><CopyableCode code="packageApplications" /></td>
    <td><code>array</code></td>
    <td>List of package applications.</td>
</tr>
<tr>
    <td><CopyableCode code="packageDependencies" /></td>
    <td><code>array</code></td>
    <td>List of package dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="packageFamilyName" /></td>
    <td><code>string</code></td>
    <td>Package Family Name from appxmanifest.xml. Contains Package Name and Publisher name.</td>
</tr>
<tr>
    <td><CopyableCode code="packageName" /></td>
    <td><code>string</code></td>
    <td>Package Name from appxmanifest.xml.</td>
</tr>
<tr>
    <td><CopyableCode code="packageRelativePath" /></td>
    <td><code>string</code></td>
    <td>Relative Path to the package inside the image.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Package version found in the appxmanifest.xml.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-msix_package_full_name"><code>msix_package_full_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a msixpackage.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List MSIX packages in hostpool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-msix_package_full_name"><code>msix_package_full_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a MSIX package.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-msix_package_full_name"><code>msix_package_full_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an MSIX Package.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-msix_package_full_name"><code>msix_package_full_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a MSIX package.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-msix_package_full_name"><code>msix_package_full_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove an MSIX Package.</td>
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
<tr id="parameter-host_pool_name">
    <td><CopyableCode code="host_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the host pool within the specified resource group. Required.</td>
</tr>
<tr id="parameter-msix_package_full_name">
    <td><CopyableCode code="msix_package_full_name" /></td>
    <td><code>string</code></td>
    <td>The version specific package full name of the MSIX package within specified hostpool. Required.</td>
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
<tr id="parameter-initialSkip">
    <td><CopyableCode code="initialSkip" /></td>
    <td><code>integer</code></td>
    <td>Initial number of items to skip. Default value is None.</td>
</tr>
<tr id="parameter-isDescending">
    <td><CopyableCode code="isDescending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the collection is descending. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Number of items per page. Default value is None.</td>
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

Get a msixpackage.

```sql
SELECT
id,
name,
displayName,
imagePath,
isActive,
isRegularRegistration,
lastUpdated,
packageApplications,
packageDependencies,
packageFamilyName,
packageName,
packageRelativePath,
systemData,
type,
version
FROM azure.desktop_virtualization.msix_packages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND msix_package_full_name = '{{ msix_package_full_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List MSIX packages in hostpool.

```sql
SELECT
id,
name,
displayName,
imagePath,
isActive,
isRegularRegistration,
lastUpdated,
packageApplications,
packageDependencies,
packageFamilyName,
packageName,
packageRelativePath,
systemData,
type,
version
FROM azure.desktop_virtualization.msix_packages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
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

Create or update a MSIX package.

```sql
INSERT INTO azure.desktop_virtualization.msix_packages (
properties,
resource_group_name,
host_pool_name,
msix_package_full_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ host_pool_name }}',
'{{ msix_package_full_name }}',
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
- name: msix_packages
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the msix_packages resource.
    - name: host_pool_name
      value: "{{ host_pool_name }}"
      description: Required parameter for the msix_packages resource.
    - name: msix_package_full_name
      value: "{{ msix_package_full_name }}"
      description: Required parameter for the msix_packages resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the msix_packages resource.
    - name: properties
      value:
        imagePath: "{{ imagePath }}"
        packageName: "{{ packageName }}"
        packageFamilyName: "{{ packageFamilyName }}"
        displayName: "{{ displayName }}"
        packageRelativePath: "{{ packageRelativePath }}"
        isRegularRegistration: {{ isRegularRegistration }}
        isActive: {{ isActive }}
        packageDependencies:
          - dependencyName: "{{ dependencyName }}"
            publisher: "{{ publisher }}"
            minVersion: "{{ minVersion }}"
        version: "{{ version }}"
        lastUpdated: "{{ lastUpdated }}"
        packageApplications:
          - appId: "{{ appId }}"
            description: "{{ description }}"
            appUserModelID: "{{ appUserModelID }}"
            friendlyName: "{{ friendlyName }}"
            iconImageName: "{{ iconImageName }}"
            rawIcon: "{{ rawIcon }}"
            rawPng: "{{ rawPng }}"
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

Update an MSIX Package.

```sql
UPDATE azure.desktop_virtualization.msix_packages
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND msix_package_full_name = '{{ msix_package_full_name }}' --required
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

Create or update a MSIX package.

```sql
REPLACE azure.desktop_virtualization.msix_packages
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND msix_package_full_name = '{{ msix_package_full_name }}' --required
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

Remove an MSIX Package.

```sql
DELETE FROM azure.desktop_virtualization.msix_packages
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND msix_package_full_name = '{{ msix_package_full_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
