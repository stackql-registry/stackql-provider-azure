--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - desktopvirtualization
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

Creates, updates, deletes, gets or lists an <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktopvirtualization.applications" /></td></tr>
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
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>Resource Type of Application. Known values are: "InBuilt" and "MsixApplication".</td>
</tr>
<tr>
    <td><CopyableCode code="commandLineArguments" /></td>
    <td><code>string</code></td>
    <td>Command Line Arguments for Application.</td>
</tr>
<tr>
    <td><CopyableCode code="commandLineSetting" /></td>
    <td><code>string</code></td>
    <td>Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Required. Known values are: "DoNotAllow", "Allow", and "Require".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of Application.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>Specifies a path for the executable file for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of Application.</td>
</tr>
<tr>
    <td><CopyableCode code="iconContent" /></td>
    <td><code>string (byte)</code></td>
    <td>the icon a 64 bit string as a byte array.</td>
</tr>
<tr>
    <td><CopyableCode code="iconHash" /></td>
    <td><code>string</code></td>
    <td>Hash of the icon.</td>
</tr>
<tr>
    <td><CopyableCode code="iconIndex" /></td>
    <td><code>integer</code></td>
    <td>Index of the icon.</td>
</tr>
<tr>
    <td><CopyableCode code="iconPath" /></td>
    <td><code>string</code></td>
    <td>Path to icon.</td>
</tr>
<tr>
    <td><CopyableCode code="msixPackageApplicationId" /></td>
    <td><code>string</code></td>
    <td>Specifies the package application Id for MSIX applications.</td>
</tr>
<tr>
    <td><CopyableCode code="msixPackageFamilyName" /></td>
    <td><code>string</code></td>
    <td>Specifies the package family name for MSIX applications.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of Application. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="showInPortal" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to show the RemoteApp program in the RD Web Access server.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>Resource Type of Application. Known values are: "InBuilt" and "MsixApplication".</td>
</tr>
<tr>
    <td><CopyableCode code="commandLineArguments" /></td>
    <td><code>string</code></td>
    <td>Command Line Arguments for Application.</td>
</tr>
<tr>
    <td><CopyableCode code="commandLineSetting" /></td>
    <td><code>string</code></td>
    <td>Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all. Required. Known values are: "DoNotAllow", "Allow", and "Require".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of Application.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>Specifies a path for the executable file for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of Application.</td>
</tr>
<tr>
    <td><CopyableCode code="iconContent" /></td>
    <td><code>string (byte)</code></td>
    <td>the icon a 64 bit string as a byte array.</td>
</tr>
<tr>
    <td><CopyableCode code="iconHash" /></td>
    <td><code>string</code></td>
    <td>Hash of the icon.</td>
</tr>
<tr>
    <td><CopyableCode code="iconIndex" /></td>
    <td><code>integer</code></td>
    <td>Index of the icon.</td>
</tr>
<tr>
    <td><CopyableCode code="iconPath" /></td>
    <td><code>string</code></td>
    <td>Path to icon.</td>
</tr>
<tr>
    <td><CopyableCode code="msixPackageApplicationId" /></td>
    <td><code>string</code></td>
    <td>Specifies the package application Id for MSIX applications.</td>
</tr>
<tr>
    <td><CopyableCode code="msixPackageFamilyName" /></td>
    <td><code>string</code></td>
    <td>Specifies the package family name for MSIX applications.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of Application. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="showInPortal" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to show the RemoteApp program in the RD Web Access server.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an application.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List applications.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an application.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an application.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an application.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove an application.</td>
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
<tr id="parameter-application_group_name">
    <td><CopyableCode code="application_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application group. Required.</td>
</tr>
<tr id="parameter-application_name">
    <td><CopyableCode code="application_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application within the specified application group. Required.</td>
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

Get an application.

```sql
SELECT
id,
name,
applicationType,
commandLineArguments,
commandLineSetting,
description,
filePath,
friendlyName,
iconContent,
iconHash,
iconIndex,
iconPath,
msixPackageApplicationId,
msixPackageFamilyName,
objectId,
showInPortal,
systemData,
type
FROM azure.desktopvirtualization.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND application_group_name = '{{ application_group_name }}' -- required
AND application_name = '{{ application_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List applications.

```sql
SELECT
id,
name,
applicationType,
commandLineArguments,
commandLineSetting,
description,
filePath,
friendlyName,
iconContent,
iconHash,
iconIndex,
iconPath,
msixPackageApplicationId,
msixPackageFamilyName,
objectId,
showInPortal,
systemData,
type
FROM azure.desktopvirtualization.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND application_group_name = '{{ application_group_name }}' -- required
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

Create or update an application.

```sql
INSERT INTO azure.desktopvirtualization.applications (
properties,
resource_group_name,
application_group_name,
application_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ application_group_name }}',
'{{ application_name }}',
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
- name: applications
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the applications resource.
    - name: application_group_name
      value: "{{ application_group_name }}"
      description: Required parameter for the applications resource.
    - name: application_name
      value: "{{ application_name }}"
      description: Required parameter for the applications resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the applications resource.
    - name: properties
      value:
        description: "{{ description }}"
        friendlyName: "{{ friendlyName }}"
        filePath: "{{ filePath }}"
        msixPackageFamilyName: "{{ msixPackageFamilyName }}"
        msixPackageApplicationId: "{{ msixPackageApplicationId }}"
        applicationType: "{{ applicationType }}"
        commandLineSetting: "{{ commandLineSetting }}"
        commandLineArguments: "{{ commandLineArguments }}"
        showInPortal: {{ showInPortal }}
        iconPath: "{{ iconPath }}"
        iconIndex: {{ iconIndex }}
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

Update an application.

```sql
UPDATE azure.desktopvirtualization.applications
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_group_name = '{{ application_group_name }}' --required
AND application_name = '{{ application_name }}' --required
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

Create or update an application.

```sql
REPLACE azure.desktopvirtualization.applications
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_group_name = '{{ application_group_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Remove an application.

```sql
DELETE FROM azure.desktopvirtualization.applications
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND application_group_name = '{{ application_group_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
