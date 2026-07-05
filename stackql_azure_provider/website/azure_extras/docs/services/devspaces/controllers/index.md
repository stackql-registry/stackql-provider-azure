--- 
title: controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - controllers
  - devspaces
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

Creates, updates, deletes, gets or lists a <code>controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="controllers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.devspaces.controllers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneFqdn" /></td>
    <td><code>string</code></td>
    <td>DNS name for accessing DataPlane services.</td>
</tr>
<tr>
    <td><CopyableCode code="hostSuffix" /></td>
    <td><code>string</code></td>
    <td>DNS suffix for public endpoints running in the Azure Dev Spaces Controller.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region where the Azure resource is located.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Azure Dev Spaces Controller. Known values are: "Succeeded", "Failed", "Canceled", "Updating", "Creating", "Deleting", and "Deleted".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Model representing SKU for Azure Dev Spaces Controller. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostApiServerFqdn" /></td>
    <td><code>string</code></td>
    <td>DNS of the target container host's API server.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostCredentialsBase64" /></td>
    <td><code>string</code></td>
    <td>Credentials of the target container host (base64). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the target container host. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneFqdn" /></td>
    <td><code>string</code></td>
    <td>DNS name for accessing DataPlane services.</td>
</tr>
<tr>
    <td><CopyableCode code="hostSuffix" /></td>
    <td><code>string</code></td>
    <td>DNS suffix for public endpoints running in the Azure Dev Spaces Controller.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region where the Azure resource is located.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Azure Dev Spaces Controller. Known values are: "Succeeded", "Failed", "Canceled", "Updating", "Creating", "Deleting", and "Deleted".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Model representing SKU for Azure Dev Spaces Controller. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostApiServerFqdn" /></td>
    <td><code>string</code></td>
    <td>DNS of the target container host's API server.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostCredentialsBase64" /></td>
    <td><code>string</code></td>
    <td>Credentials of the target container host (base64). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the target container host. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneFqdn" /></td>
    <td><code>string</code></td>
    <td>DNS name for accessing DataPlane services.</td>
</tr>
<tr>
    <td><CopyableCode code="hostSuffix" /></td>
    <td><code>string</code></td>
    <td>DNS suffix for public endpoints running in the Azure Dev Spaces Controller.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region where the Azure resource is located.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Azure Dev Spaces Controller. Known values are: "Succeeded", "Failed", "Canceled", "Updating", "Creating", "Deleting", and "Deleted".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Model representing SKU for Azure Dev Spaces Controller. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostApiServerFqdn" /></td>
    <td><code>string</code></td>
    <td>DNS of the target container host's API server.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostCredentialsBase64" /></td>
    <td><code>string</code></td>
    <td>Credentials of the target container host (base64). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetContainerHostResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the target container host. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Azure Dev Spaces Controller. Gets the properties for an Azure Dev Spaces Controller.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Azure Dev Spaces Controllers in a resource group. Lists all the Azure Dev Spaces Controllers with their properties in the specified resource group and subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Azure Dev Spaces Controllers in a subscription. Lists all the Azure Dev Spaces Controllers with their properties in the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sku"><code>sku</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates an Azure Dev Spaces Controller. Creates an Azure Dev Spaces Controller with the specified create parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an Azure Dev Spaces Controller. Updates the properties of an existing Azure Dev Spaces Controller with the specified update parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Azure Dev Spaces Controller. Deletes an existing Azure Dev Spaces Controller.</td>
</tr>
<tr>
    <td><a href="#list_connection_details"><CopyableCode code="list_connection_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetContainerHostResourceId"><code>targetContainerHostResourceId</code></a></td>
    <td></td>
    <td>Lists connection details for an Azure Dev Spaces Controller. Lists connection details for the underlying container resources of an Azure Dev Spaces Controller.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Resource group to which the resource belongs. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets an Azure Dev Spaces Controller. Gets the properties for an Azure Dev Spaces Controller.

```sql
SELECT
id,
name,
dataPlaneFqdn,
hostSuffix,
location,
provisioningState,
sku,
tags,
targetContainerHostApiServerFqdn,
targetContainerHostCredentialsBase64,
targetContainerHostResourceId,
type
FROM azure_extras.devspaces.controllers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the Azure Dev Spaces Controllers in a resource group. Lists all the Azure Dev Spaces Controllers with their properties in the specified resource group and subscription.

```sql
SELECT
id,
name,
dataPlaneFqdn,
hostSuffix,
location,
provisioningState,
sku,
tags,
targetContainerHostApiServerFqdn,
targetContainerHostCredentialsBase64,
targetContainerHostResourceId,
type
FROM azure_extras.devspaces.controllers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the Azure Dev Spaces Controllers in a subscription. Lists all the Azure Dev Spaces Controllers with their properties in the subscription.

```sql
SELECT
id,
name,
dataPlaneFqdn,
hostSuffix,
location,
provisioningState,
sku,
tags,
targetContainerHostApiServerFqdn,
targetContainerHostCredentialsBase64,
targetContainerHostResourceId,
type
FROM azure_extras.devspaces.controllers
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates an Azure Dev Spaces Controller. Creates an Azure Dev Spaces Controller with the specified create parameters.

```sql
INSERT INTO azure_extras.devspaces.controllers (
tags,
location,
sku,
properties,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}',
'{{ sku }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: controllers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the controllers resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the controllers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the controllers resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tags for the Azure resource.
    - name: location
      value: "{{ location }}"
      description: |
        Region where the Azure resource is located.
    - name: sku
      description: |
        Model representing SKU for Azure Dev Spaces Controller. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: properties
      value:
        targetContainerHostResourceId: "{{ targetContainerHostResourceId }}"
        targetContainerHostCredentialsBase64: "{{ targetContainerHostCredentialsBase64 }}"
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

Updates an Azure Dev Spaces Controller. Updates the properties of an existing Azure Dev Spaces Controller with the specified update parameters.

```sql
UPDATE azure_extras.devspaces.controllers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
sku,
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

Deletes an Azure Dev Spaces Controller. Deletes an existing Azure Dev Spaces Controller.

```sql
DELETE FROM azure_extras.devspaces.controllers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_connection_details"
    values={[
        { label: 'list_connection_details', value: 'list_connection_details' }
    ]}
>
<TabItem value="list_connection_details">

Lists connection details for an Azure Dev Spaces Controller. Lists connection details for the underlying container resources of an Azure Dev Spaces Controller.

```sql
EXEC azure_extras.devspaces.controllers.list_connection_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetContainerHostResourceId": "{{ targetContainerHostResourceId }}"
}'
;
```
</TabItem>
</Tabs>
