--- 
title: gallery_scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_scripts
  - compute
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

Creates, updates, deletes, gets or lists a <code>gallery_scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gallery_scripts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_scripts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_gallery', value: 'list_by_gallery' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of this gallery script definition resource. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="endOfLifeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of life date of the gallery Script Definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="eula" /></td>
    <td><code>string</code></td>
    <td>The Eula agreement (End User License Agreement) for the gallery Script Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyStatementUri" /></td>
    <td><code>string</code></td>
    <td>The privacy statement uri.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseNoteUri" /></td>
    <td><code>string</code></td>
    <td>The release note uri.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedOSType" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify the supported type of the OS that application is built for. Possible values are: **Windows,** **Linux.**. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_gallery">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of this gallery script definition resource. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="endOfLifeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of life date of the gallery Script Definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="eula" /></td>
    <td><code>string</code></td>
    <td>The Eula agreement (End User License Agreement) for the gallery Script Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyStatementUri" /></td>
    <td><code>string</code></td>
    <td>The privacy statement uri.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseNoteUri" /></td>
    <td><code>string</code></td>
    <td>The release note uri.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedOSType" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify the supported type of the OS that application is built for. Possible values are: **Windows,** **Linux.**. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-gallery_script_name"><code>gallery_script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves information about a gallery script definition.</td>
</tr>
<tr>
    <td><a href="#list_by_gallery"><CopyableCode code="list_by_gallery" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List gallery Script Definitions in a gallery.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-gallery_script_name"><code>gallery_script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a Gallery Script Definition. Gallery scripts allow the storage, sharing and reuse of common scripts.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-gallery_script_name"><code>gallery_script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a gallery Script Definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-gallery_script_name"><code>gallery_script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a Gallery Script Definition. Gallery scripts allow the storage, sharing and reuse of common scripts.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-gallery_script_name"><code>gallery_script_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a gallery Script Definition.</td>
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
<tr id="parameter-gallery_name">
    <td><CopyableCode code="gallery_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Shared Image Gallery. Required.</td>
</tr>
<tr id="parameter-gallery_script_name">
    <td><CopyableCode code="gallery_script_name" /></td>
    <td><code>string</code></td>
    <td>The name of the gallery Script Definition to be retrieved. Required.</td>
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
        { label: 'list_by_gallery', value: 'list_by_gallery' }
    ]}
>
<TabItem value="get">

Retrieves information about a gallery script definition.

```sql
SELECT
id,
name,
description,
endOfLifeDate,
eula,
location,
privacyStatementUri,
provisioningState,
releaseNoteUri,
supportedOSType,
systemData,
tags,
type
FROM azure.compute.gallery_scripts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND gallery_script_name = '{{ gallery_script_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_gallery">

List gallery Script Definitions in a gallery.

```sql
SELECT
id,
name,
description,
endOfLifeDate,
eula,
location,
privacyStatementUri,
provisioningState,
releaseNoteUri,
supportedOSType,
systemData,
tags,
type
FROM azure.compute.gallery_scripts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
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

Create or update a Gallery Script Definition. Gallery scripts allow the storage, sharing and reuse of common scripts.

```sql
INSERT INTO azure.compute.gallery_scripts (
tags,
location,
properties,
resource_group_name,
gallery_name,
gallery_script_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ gallery_name }}',
'{{ gallery_script_name }}',
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
- name: gallery_scripts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the gallery_scripts resource.
    - name: gallery_name
      value: "{{ gallery_name }}"
      description: Required parameter for the gallery_scripts resource.
    - name: gallery_script_name
      value: "{{ gallery_script_name }}"
      description: Required parameter for the gallery_scripts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the gallery_scripts resource.
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
        Describes the properties of a gallery Script Definition.
      value:
        description: "{{ description }}"
        eula: "{{ eula }}"
        privacyStatementUri: "{{ privacyStatementUri }}"
        releaseNoteUri: "{{ releaseNoteUri }}"
        endOfLifeDate: "{{ endOfLifeDate }}"
        supportedOSType: "{{ supportedOSType }}"
        provisioningState: "{{ provisioningState }}"
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

Update a gallery Script Definition.

```sql
UPDATE azure.compute.gallery_scripts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gallery_name = '{{ gallery_name }}' --required
AND gallery_script_name = '{{ gallery_script_name }}' --required
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

Create or update a Gallery Script Definition. Gallery scripts allow the storage, sharing and reuse of common scripts.

```sql
REPLACE azure.compute.gallery_scripts
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gallery_name = '{{ gallery_name }}' --required
AND gallery_script_name = '{{ gallery_script_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Delete a gallery Script Definition.

```sql
DELETE FROM azure.compute.gallery_scripts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND gallery_name = '{{ gallery_name }}' --required
AND gallery_script_name = '{{ gallery_script_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
