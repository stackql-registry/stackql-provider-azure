--- 
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - agrifood
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood.extensions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_farm_beats', value: 'list_by_farm_beats' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalApiProperties" /></td>
    <td><code>object</code></td>
    <td>Additional api properties.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag value to implement optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionApiDocsLink" /></td>
    <td><code>string</code></td>
    <td>Extension api docs link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionAuthLink" /></td>
    <td><code>string</code></td>
    <td>Extension auth link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionCategory" /></td>
    <td><code>string</code></td>
    <td>Extension category. e.g. weather/sensor/satellite.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>Extension Id.</td>
</tr>
<tr>
    <td><CopyableCode code="installedExtensionVersion" /></td>
    <td><code>string</code></td>
    <td>Installed extension version.</td>
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
<TabItem value="list_by_farm_beats">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalApiProperties" /></td>
    <td><code>object</code></td>
    <td>Additional api properties.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag value to implement optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionApiDocsLink" /></td>
    <td><code>string</code></td>
    <td>Extension api docs link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionAuthLink" /></td>
    <td><code>string</code></td>
    <td>Extension auth link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionCategory" /></td>
    <td><code>string</code></td>
    <td>Extension category. e.g. weather/sensor/satellite.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>Extension Id.</td>
</tr>
<tr>
    <td><CopyableCode code="installedExtensionVersion" /></td>
    <td><code>string</code></td>
    <td>Installed extension version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-extension_id"><code>extension_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get installed extension details by extension id.</td>
</tr>
<tr>
    <td><a href="#list_by_farm_beats"><CopyableCode code="list_by_farm_beats" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$maxPageSize"><code>$maxPageSize</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get installed extensions details.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-extension_id"><code>extension_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Install or Update extension. AdditionalApiProperties are merged patch and if the extension is updated to a new version then the obsolete entries will be auto deleted from AdditionalApiProperties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-extension_id"><code>extension_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Install or Update extension. AdditionalApiProperties are merged patch and if the extension is updated to a new version then the obsolete entries will be auto deleted from AdditionalApiProperties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-extension_id"><code>extension_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Uninstall extension.</td>
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
<tr id="parameter-extension_id">
    <td><CopyableCode code="extension_id" /></td>
    <td><code>string</code></td>
    <td>Id of extension resource. Required.</td>
</tr>
<tr id="parameter-farm_beats_resource_name">
    <td><CopyableCode code="farm_beats_resource_name" /></td>
    <td><code>string</code></td>
    <td>FarmBeats resource name. Required.</td>
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
<tr id="parameter-$maxPageSize">
    <td><CopyableCode code="$maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of items needed (inclusive). Minimum = 10, Maximum = 1000, Default value = 50. Default value is 50.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_farm_beats', value: 'list_by_farm_beats' }
    ]}
>
<TabItem value="get">

Get installed extension details by extension id.

```sql
SELECT
id,
name,
additionalApiProperties,
eTag,
extensionApiDocsLink,
extensionAuthLink,
extensionCategory,
extensionId,
installedExtensionVersion,
systemData,
type
FROM azure_extras.agrifood.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' -- required
AND extension_id = '{{ extension_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_farm_beats">

Get installed extensions details.

```sql
SELECT
id,
name,
additionalApiProperties,
eTag,
extensionApiDocsLink,
extensionAuthLink,
extensionCategory,
extensionId,
installedExtensionVersion,
systemData,
type
FROM azure_extras.agrifood.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $maxPageSize = '{{ $maxPageSize }}'
AND $skipToken = '{{ $skipToken }}'
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

Install or Update extension. AdditionalApiProperties are merged patch and if the extension is updated to a new version then the obsolete entries will be auto deleted from AdditionalApiProperties.

```sql
INSERT INTO azure_extras.agrifood.extensions (
extensionVersion,
additionalApiProperties,
resource_group_name,
farm_beats_resource_name,
extension_id,
subscription_id
)
SELECT 
'{{ extensionVersion }}',
'{{ additionalApiProperties }}',
'{{ resource_group_name }}',
'{{ farm_beats_resource_name }}',
'{{ extension_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: extensions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the extensions resource.
    - name: farm_beats_resource_name
      value: "{{ farm_beats_resource_name }}"
      description: Required parameter for the extensions resource.
    - name: extension_id
      value: "{{ extension_id }}"
      description: Required parameter for the extensions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the extensions resource.
    - name: extensionVersion
      value: "{{ extensionVersion }}"
      description: |
        Extension Version.
    - name: additionalApiProperties
      value: "{{ additionalApiProperties }}"
      description: |
        Additional Api Properties.
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

Install or Update extension. AdditionalApiProperties are merged patch and if the extension is updated to a new version then the obsolete entries will be auto deleted from AdditionalApiProperties.

```sql
REPLACE azure_extras.agrifood.extensions
SET 
extensionVersion = '{{ extensionVersion }}',
additionalApiProperties = '{{ additionalApiProperties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' --required
AND extension_id = '{{ extension_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
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

Uninstall extension.

```sql
DELETE FROM azure_extras.agrifood.extensions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' --required
AND extension_id = '{{ extension_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
