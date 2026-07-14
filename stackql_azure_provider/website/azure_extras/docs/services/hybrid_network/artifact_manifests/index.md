--- 
title: artifact_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_manifests
  - hybrid_network
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

Creates, updates, deletes, gets or lists an <code>artifact_manifests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="artifact_manifests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.hybrid_network.artifact_manifests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_artifact_store', value: 'list_by_artifact_store' }
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
    <td><CopyableCode code="artifactManifestState" /></td>
    <td><code>string</code></td>
    <td>The artifact manifest state. Known values are: "Unknown", "Uploading", "Uploaded", "Validating", "ValidationFailed", and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The artifacts list.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the ArtifactManifest resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
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
<TabItem value="list_by_artifact_store">

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
    <td><CopyableCode code="artifactManifestState" /></td>
    <td><code>string</code></td>
    <td>The artifact manifest state. Known values are: "Unknown", "Uploading", "Uploaded", "Validating", "ValidationFailed", and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The artifacts list.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the ArtifactManifest resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_manifest_name"><code>artifact_manifest_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a artifact manifest resource.</td>
</tr>
<tr>
    <td><a href="#list_by_artifact_store"><CopyableCode code="list_by_artifact_store" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the artifact manifest.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_manifest_name"><code>artifact_manifest_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a artifact manifest.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_manifest_name"><code>artifact_manifest_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a artifact manifest resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_manifest_name"><code>artifact_manifest_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a artifact manifest.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_manifest_name"><code>artifact_manifest_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified artifact manifest.</td>
</tr>
<tr>
    <td><a href="#list_credential"><CopyableCode code="list_credential" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_manifest_name"><code>artifact_manifest_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List credential for publishing artifacts defined in artifact manifest.</td>
</tr>
<tr>
    <td><a href="#update_state"><CopyableCode code="update_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_manifest_name"><code>artifact_manifest_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update state for artifact manifest.</td>
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
<tr id="parameter-artifact_manifest_name">
    <td><CopyableCode code="artifact_manifest_name" /></td>
    <td><code>string</code></td>
    <td>The name of the artifact manifest. Required.</td>
</tr>
<tr id="parameter-artifact_store_name">
    <td><CopyableCode code="artifact_store_name" /></td>
    <td><code>string</code></td>
    <td>The name of the artifact store. Required.</td>
</tr>
<tr id="parameter-publisher_name">
    <td><CopyableCode code="publisher_name" /></td>
    <td><code>string</code></td>
    <td>The name of the publisher. Required.</td>
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
        { label: 'list_by_artifact_store', value: 'list_by_artifact_store' }
    ]}
>
<TabItem value="get">

Gets information about a artifact manifest resource.

```sql
SELECT
id,
name,
artifactManifestState,
artifacts,
location,
provisioningState,
systemData,
tags,
type
FROM azure_extras.hybrid_network.artifact_manifests
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND artifact_store_name = '{{ artifact_store_name }}' -- required
AND artifact_manifest_name = '{{ artifact_manifest_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_artifact_store">

Gets information about the artifact manifest.

```sql
SELECT
id,
name,
artifactManifestState,
artifacts,
location,
provisioningState,
systemData,
tags,
type
FROM azure_extras.hybrid_network.artifact_manifests
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND artifact_store_name = '{{ artifact_store_name }}' -- required
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

Creates or updates a artifact manifest.

```sql
INSERT INTO azure_extras.hybrid_network.artifact_manifests (
tags,
location,
properties,
resource_group_name,
publisher_name,
artifact_store_name,
artifact_manifest_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ publisher_name }}',
'{{ artifact_store_name }}',
'{{ artifact_manifest_name }}',
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
- name: artifact_manifests
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the artifact_manifests resource.
    - name: publisher_name
      value: "{{ publisher_name }}"
      description: Required parameter for the artifact_manifests resource.
    - name: artifact_store_name
      value: "{{ artifact_store_name }}"
      description: Required parameter for the artifact_manifests resource.
    - name: artifact_manifest_name
      value: "{{ artifact_manifest_name }}"
      description: Required parameter for the artifact_manifests resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the artifact_manifests resource.
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
        Artifact manifest properties.
      value:
        provisioningState: "{{ provisioningState }}"
        artifactManifestState: "{{ artifactManifestState }}"
        artifacts:
          - artifactName: "{{ artifactName }}"
            artifactType: "{{ artifactType }}"
            artifactVersion: "{{ artifactVersion }}"
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

Updates a artifact manifest resource.

```sql
UPDATE azure_extras.hybrid_network.artifact_manifests
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND artifact_store_name = '{{ artifact_store_name }}' --required
AND artifact_manifest_name = '{{ artifact_manifest_name }}' --required
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

Creates or updates a artifact manifest.

```sql
REPLACE azure_extras.hybrid_network.artifact_manifests
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND artifact_store_name = '{{ artifact_store_name }}' --required
AND artifact_manifest_name = '{{ artifact_manifest_name }}' --required
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

Deletes the specified artifact manifest.

```sql
DELETE FROM azure_extras.hybrid_network.artifact_manifests
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND artifact_store_name = '{{ artifact_store_name }}' --required
AND artifact_manifest_name = '{{ artifact_manifest_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_credential"
    values={[
        { label: 'list_credential', value: 'list_credential' },
        { label: 'update_state', value: 'update_state' }
    ]}
>
<TabItem value="list_credential">

List credential for publishing artifacts defined in artifact manifest.

```sql
EXEC azure_extras.hybrid_network.artifact_manifests.list_credential 
@resource_group_name='{{ resource_group_name }}' --required, 
@publisher_name='{{ publisher_name }}' --required, 
@artifact_store_name='{{ artifact_store_name }}' --required, 
@artifact_manifest_name='{{ artifact_manifest_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_state">

Update state for artifact manifest.

```sql
EXEC azure_extras.hybrid_network.artifact_manifests.update_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@publisher_name='{{ publisher_name }}' --required, 
@artifact_store_name='{{ artifact_store_name }}' --required, 
@artifact_manifest_name='{{ artifact_manifest_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"artifactManifestState": "{{ artifactManifestState }}"
}'
;
```
</TabItem>
</Tabs>
