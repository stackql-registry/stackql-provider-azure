--- 
title: move_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - move_collections
  - resourcemover
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

Creates, updates, deletes, gets or lists a <code>move_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="move_collections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resourcemover.move_collections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_required_for"
    values={[
        { label: 'list_required_for', value: 'list_required_for' },
        { label: 'get', value: 'get' },
        { label: 'list_move_collections_by_resource_group', value: 'list_move_collections_by_resource_group' },
        { label: 'list_move_collections_by_subscription', value: 'list_move_collections_by_subscription' }
    ]}
>
<TabItem value="list_required_for">

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
    <td><CopyableCode code="sourceIds" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of source Ids for which the input resource is required.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the move collection errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Defines the MSI properties of the Move Collection.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="moveRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the move region which indicates the region where the VM Regional to Zonal move will be conducted.</td>
</tr>
<tr>
    <td><CopyableCode code="moveType" /></td>
    <td><code>string</code></td>
    <td>Defines the MoveType. Known values are: "RegionToRegion" and "RegionToZone".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sourceRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the source region.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target region.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the version of move collection.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_move_collections_by_resource_group">

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
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the move collection errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Defines the MSI properties of the Move Collection.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="moveRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the move region which indicates the region where the VM Regional to Zonal move will be conducted.</td>
</tr>
<tr>
    <td><CopyableCode code="moveType" /></td>
    <td><code>string</code></td>
    <td>Defines the MoveType. Known values are: "RegionToRegion" and "RegionToZone".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sourceRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the source region.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target region.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the version of move collection.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_move_collections_by_subscription">

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
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the move collection errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Defines the MSI properties of the Move Collection.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="moveRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the move region which indicates the region where the VM Regional to Zonal move will be conducted.</td>
</tr>
<tr>
    <td><CopyableCode code="moveType" /></td>
    <td><code>string</code></td>
    <td>Defines the MoveType. Known values are: "RegionToRegion" and "RegionToZone".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sourceRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the source region.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRegion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target region.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the version of move collection.</td>
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
    <td><a href="#list_required_for"><CopyableCode code="list_required_for" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sourceId"><code>sourceId</code></a></td>
    <td></td>
    <td>List of the move resources for which an arm resource is required for.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the move collection.</td>
</tr>
<tr>
    <td><a href="#list_move_collections_by_resource_group"><CopyableCode code="list_move_collections_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Move Collections. Get all the Move Collections in the resource group.</td>
</tr>
<tr>
    <td><a href="#list_move_collections_by_subscription"><CopyableCode code="list_move_collections_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Move Collections. Get all the Move Collections in the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a move collection.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a move collection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a move collection.</td>
</tr>
<tr>
    <td><a href="#prepare"><CopyableCode code="prepare" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-moveResources"><code>moveResources</code></a></td>
    <td></td>
    <td>Initiates prepare for the set of resources included in the request body. The prepare operation is on the moveResources that are in the moveState 'PreparePending' or 'PrepareFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.</td>
</tr>
<tr>
    <td><a href="#initiate_move"><CopyableCode code="initiate_move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-moveResources"><code>moveResources</code></a></td>
    <td></td>
    <td>Moves the set of resources included in the request body. The move operation is triggered after the moveResources are in the moveState 'MovePending' or 'MoveFailed', on a successful completion the moveResource moveState do a transition to CommitPending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.</td>
</tr>
<tr>
    <td><a href="#commit"><CopyableCode code="commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-moveResources"><code>moveResources</code></a></td>
    <td></td>
    <td>Commits the set of resources included in the request body. The commit operation is triggered on the moveResources in the moveState 'CommitPending' or 'CommitFailed', on a successful completion the moveResource moveState do a transition to Committed. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.</td>
</tr>
<tr>
    <td><a href="#discard"><CopyableCode code="discard" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-moveResources"><code>moveResources</code></a></td>
    <td></td>
    <td>Discards the set of resources included in the request body. The discard operation is triggered on the moveResources in the moveState 'CommitPending' or 'DiscardFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.</td>
</tr>
<tr>
    <td><a href="#resolve_dependencies"><CopyableCode code="resolve_dependencies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Computes, resolves and validate the dependencies of the moveResources in the move collection.</td>
</tr>
<tr>
    <td><a href="#bulk_remove"><CopyableCode code="bulk_remove" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes the set of move resources included in the request body from move collection. The orchestration is done by service. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.</td>
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
<tr id="parameter-move_collection_name">
    <td><CopyableCode code="move_collection_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-sourceId">
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>The sourceId for which the api is invoked. Required.</td>
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
    defaultValue="list_required_for"
    values={[
        { label: 'list_required_for', value: 'list_required_for' },
        { label: 'get', value: 'get' },
        { label: 'list_move_collections_by_resource_group', value: 'list_move_collections_by_resource_group' },
        { label: 'list_move_collections_by_subscription', value: 'list_move_collections_by_subscription' }
    ]}
>
<TabItem value="list_required_for">

List of the move resources for which an arm resource is required for.

```sql
SELECT
sourceIds
FROM azure.resourcemover.move_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND move_collection_name = '{{ move_collection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND sourceId = '{{ sourceId }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the move collection.

```sql
SELECT
id,
name,
errors,
etag,
identity,
location,
moveRegion,
moveType,
provisioningState,
sourceRegion,
systemData,
tags,
targetRegion,
type,
version
FROM azure.resourcemover.move_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND move_collection_name = '{{ move_collection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_move_collections_by_resource_group">

Get all Move Collections. Get all the Move Collections in the resource group.

```sql
SELECT
id,
name,
errors,
etag,
identity,
location,
moveRegion,
moveType,
provisioningState,
sourceRegion,
systemData,
tags,
targetRegion,
type,
version
FROM azure.resourcemover.move_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_move_collections_by_subscription">

Get all Move Collections. Get all the Move Collections in the subscription.

```sql
SELECT
id,
name,
errors,
etag,
identity,
location,
moveRegion,
moveType,
provisioningState,
sourceRegion,
systemData,
tags,
targetRegion,
type,
version
FROM azure.resourcemover.move_collections
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

Creates or updates a move collection.

```sql
INSERT INTO azure.resourcemover.move_collections (
tags,
location,
identity,
properties,
resource_group_name,
move_collection_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ move_collection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
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
- name: move_collections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the move_collections resource.
    - name: move_collection_name
      value: "{{ move_collection_name }}"
      description: Required parameter for the move_collections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the move_collections resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: identity
      description: |
        Defines the MSI properties of the Move Collection.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
    - name: properties
      description: |
        Defines the move collection properties.
      value:
        sourceRegion: "{{ sourceRegion }}"
        targetRegion: "{{ targetRegion }}"
        moveRegion: "{{ moveRegion }}"
        provisioningState: "{{ provisioningState }}"
        version: "{{ version }}"
        moveType: "{{ moveType }}"
        errors:
          properties:
            code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                target: "{{ target }}"
                details: "{{ details }}"
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

Updates a move collection.

```sql
UPDATE azure.resourcemover.move_collections
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND move_collection_name = '{{ move_collection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
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

Deletes a move collection.

```sql
DELETE FROM azure.resourcemover.move_collections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND move_collection_name = '{{ move_collection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="prepare"
    values={[
        { label: 'prepare', value: 'prepare' },
        { label: 'initiate_move', value: 'initiate_move' },
        { label: 'commit', value: 'commit' },
        { label: 'discard', value: 'discard' },
        { label: 'resolve_dependencies', value: 'resolve_dependencies' },
        { label: 'bulk_remove', value: 'bulk_remove' }
    ]}
>
<TabItem value="prepare">

Initiates prepare for the set of resources included in the request body. The prepare operation is on the moveResources that are in the moveState 'PreparePending' or 'PrepareFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.

```sql
EXEC azure.resourcemover.move_collections.prepare 
@resource_group_name='{{ resource_group_name }}' --required, 
@move_collection_name='{{ move_collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validateOnly": {{ validateOnly }}, 
"moveResources": "{{ moveResources }}", 
"moveResourceInputType": "{{ moveResourceInputType }}"
}'
;
```
</TabItem>
<TabItem value="initiate_move">

Moves the set of resources included in the request body. The move operation is triggered after the moveResources are in the moveState 'MovePending' or 'MoveFailed', on a successful completion the moveResource moveState do a transition to CommitPending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.

```sql
EXEC azure.resourcemover.move_collections.initiate_move 
@resource_group_name='{{ resource_group_name }}' --required, 
@move_collection_name='{{ move_collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validateOnly": {{ validateOnly }}, 
"moveResources": "{{ moveResources }}", 
"moveResourceInputType": "{{ moveResourceInputType }}"
}'
;
```
</TabItem>
<TabItem value="commit">

Commits the set of resources included in the request body. The commit operation is triggered on the moveResources in the moveState 'CommitPending' or 'CommitFailed', on a successful completion the moveResource moveState do a transition to Committed. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.

```sql
EXEC azure.resourcemover.move_collections.commit 
@resource_group_name='{{ resource_group_name }}' --required, 
@move_collection_name='{{ move_collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validateOnly": {{ validateOnly }}, 
"moveResources": "{{ moveResources }}", 
"moveResourceInputType": "{{ moveResourceInputType }}"
}'
;
```
</TabItem>
<TabItem value="discard">

Discards the set of resources included in the request body. The discard operation is triggered on the moveResources in the moveState 'CommitPending' or 'DiscardFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.

```sql
EXEC azure.resourcemover.move_collections.discard 
@resource_group_name='{{ resource_group_name }}' --required, 
@move_collection_name='{{ move_collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validateOnly": {{ validateOnly }}, 
"moveResources": "{{ moveResources }}", 
"moveResourceInputType": "{{ moveResourceInputType }}"
}'
;
```
</TabItem>
<TabItem value="resolve_dependencies">

Computes, resolves and validate the dependencies of the moveResources in the move collection.

```sql
EXEC azure.resourcemover.move_collections.resolve_dependencies 
@resource_group_name='{{ resource_group_name }}' --required, 
@move_collection_name='{{ move_collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_remove">

Removes the set of move resources included in the request body from move collection. The orchestration is done by service. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.

```sql
EXEC azure.resourcemover.move_collections.bulk_remove 
@resource_group_name='{{ resource_group_name }}' --required, 
@move_collection_name='{{ move_collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validateOnly": {{ validateOnly }}, 
"moveResources": "{{ moveResources }}", 
"moveResourceInputType": "{{ moveResourceInputType }}"
}'
;
```
</TabItem>
</Tabs>
