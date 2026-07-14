--- 
title: edge_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_modules
  - video_analyzer
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

Creates, updates, deletes, gets or lists an <code>edge_modules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="edge_modules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.video_analyzer.edge_modules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_provisioning_token"
    values={[
        { label: 'list_provisioning_token', value: 'list_provisioning_token' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_provisioning_token">

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
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date of the registration token. The Azure Video Analyzer IoT edge module must be initialized and connected to the Internet prior to the token expiration date.</td>
</tr>
<tr>
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
    <td>The token blob to be provided to the Azure Video Analyzer IoT edge module through the Azure IoT Edge module twin properties.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="edgeModuleId" /></td>
    <td><code>string</code></td>
    <td>Internal ID generated for the instance of the Video Analyzer edge module.</td>
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
    <td><CopyableCode code="@nextLink" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#list_provisioning_token"><CopyableCode code="list_provisioning_token" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-edge_module_name"><code>edge_module_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new provisioning token. Creates a new provisioning token. A provisioning token allows for a single instance of Azure Video analyzer IoT edge module to be initialized and authorized to the cloud account. The provisioning token itself is short lived and it is only used for the initial handshake between IoT edge module and the cloud. After the initial handshake, the IoT edge module will agree on a set of authentication keys which will be auto-rotated as long as the module is able to periodically connect to the cloud. A new provisioning token can be generated for the same IoT edge module in case the module state lost or reset.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-edge_module_name"><code>edge_module_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves an existing edge module resource. Retrieves an existing edge module resource with the given name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>List all existing edge module resources. List all existing edge module resources, along with their JSON representations.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-edge_module_name"><code>edge_module_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new edge module or updates an existing one. Creates a new edge module or updates an existing one. An edge module resource enables a single instance of an Azure Video Analyzer IoT edge module to interact with the Video Analyzer Account. This is used for authorization and also to make sure that the particular edge module instance only has access to the data it requires from the Azure Video Analyzer service. A new edge module resource should be created for every new instance of an Azure Video Analyzer edge module deployed to you Azure IoT edge environment. Edge module resources can be deleted if the specific module is not in use anymore.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-edge_module_name"><code>edge_module_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new edge module or updates an existing one. Creates a new edge module or updates an existing one. An edge module resource enables a single instance of an Azure Video Analyzer IoT edge module to interact with the Video Analyzer Account. This is used for authorization and also to make sure that the particular edge module instance only has access to the data it requires from the Azure Video Analyzer service. A new edge module resource should be created for every new instance of an Azure Video Analyzer edge module deployed to you Azure IoT edge environment. Edge module resources can be deleted if the specific module is not in use anymore.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-edge_module_name"><code>edge_module_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing edge module resource. Deletes an existing edge module resource. Deleting the edge module resource will prevent an Azure Video Analyzer IoT edge module which was previously initiated with the module provisioning token from communicating with the cloud.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The Azure Video Analyzer account name.</td>
</tr>
<tr id="parameter-edge_module_name">
    <td><CopyableCode code="edge_module_name" /></td>
    <td><code>string</code></td>
    <td>The Edge Module name.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_provisioning_token"
    values={[
        { label: 'list_provisioning_token', value: 'list_provisioning_token' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_provisioning_token">

Creates a new provisioning token. Creates a new provisioning token. A provisioning token allows for a single instance of Azure Video analyzer IoT edge module to be initialized and authorized to the cloud account. The provisioning token itself is short lived and it is only used for the initial handshake between IoT edge module and the cloud. After the initial handshake, the IoT edge module will agree on a set of authentication keys which will be auto-rotated as long as the module is able to periodically connect to the cloud. A new provisioning token can be generated for the same IoT edge module in case the module state lost or reset.

```sql
SELECT
expirationDate,
token
FROM azure_extras.video_analyzer.edge_modules
WHERE edge_module_name = '{{ edge_module_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Retrieves an existing edge module resource. Retrieves an existing edge module resource with the given name.

```sql
SELECT
id,
name,
edgeModuleId,
systemData,
type
FROM azure_extras.video_analyzer.edge_modules
WHERE edge_module_name = '{{ edge_module_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all existing edge module resources. List all existing edge module resources, along with their JSON representations.

```sql
SELECT
@nextLink,
value
FROM azure_extras.video_analyzer.edge_modules
WHERE account_name = '{{ account_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
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

Creates a new edge module or updates an existing one. Creates a new edge module or updates an existing one. An edge module resource enables a single instance of an Azure Video Analyzer IoT edge module to interact with the Video Analyzer Account. This is used for authorization and also to make sure that the particular edge module instance only has access to the data it requires from the Azure Video Analyzer service. A new edge module resource should be created for every new instance of an Azure Video Analyzer edge module deployed to you Azure IoT edge environment. Edge module resources can be deleted if the specific module is not in use anymore.

```sql
INSERT INTO azure_extras.video_analyzer.edge_modules (
id,
name,
type,
systemData,
properties,
edge_module_name,
account_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ type }}',
'{{ systemData }}',
'{{ properties }}',
'{{ edge_module_name }}',
'{{ account_name }}',
'{{ resource_group_name }}',
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
- name: edge_modules
  props:
    - name: edge_module_name
      value: "{{ edge_module_name }}"
      description: Required parameter for the edge_modules resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the edge_modules resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the edge_modules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the edge_modules resource.
    - name: id
      value: "{{ id }}"
      description: |
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource.
    - name: type
      value: "{{ type }}"
      description: |
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".
    - name: systemData
      description: |
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
      value:
        createdBy: "{{ createdBy }}"
        createdByType: "{{ createdByType }}"
        createdAt: "{{ createdAt }}"
        lastModifiedBy: "{{ lastModifiedBy }}"
        lastModifiedByType: "{{ lastModifiedByType }}"
        lastModifiedAt: "{{ lastModifiedAt }}"
    - name: properties
      value:
        edgeModuleId: "{{ edgeModuleId }}"
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

Creates a new edge module or updates an existing one. Creates a new edge module or updates an existing one. An edge module resource enables a single instance of an Azure Video Analyzer IoT edge module to interact with the Video Analyzer Account. This is used for authorization and also to make sure that the particular edge module instance only has access to the data it requires from the Azure Video Analyzer service. A new edge module resource should be created for every new instance of an Azure Video Analyzer edge module deployed to you Azure IoT edge environment. Edge module resources can be deleted if the specific module is not in use anymore.

```sql
REPLACE azure_extras.video_analyzer.edge_modules
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
systemData = '{{ systemData }}',
properties = '{{ properties }}'
WHERE 
edge_module_name = '{{ edge_module_name }}' --required
AND account_name = '{{ account_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
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

Deletes an existing edge module resource. Deletes an existing edge module resource. Deleting the edge module resource will prevent an Azure Video Analyzer IoT edge module which was previously initiated with the module provisioning token from communicating with the cloud.

```sql
DELETE FROM azure_extras.video_analyzer.edge_modules
WHERE edge_module_name = '{{ edge_module_name }}' --required
AND account_name = '{{ account_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
