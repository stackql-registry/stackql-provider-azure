--- 
title: proxy_artifact
hide_title: false
hide_table_of_contents: false
keywords:
  - proxy_artifact
  - hybridnetwork
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

Creates, updates, deletes, gets or lists a <code>proxy_artifact</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="proxy_artifact" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridnetwork.proxy_artifact" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactState" /></td>
    <td><code>string</code></td>
    <td>The artifact state. Known values are: "Unknown", "Preview", "Active", and "Deprecated".</td>
</tr>
<tr>
    <td><CopyableCode code="artifactType" /></td>
    <td><code>string</code></td>
    <td>The artifact type. Known values are: "Unknown", "OCIArtifact", "VhdImageFile", "ArmTemplate", and "ImageFile".</td>
</tr>
<tr>
    <td><CopyableCode code="artifactVersion" /></td>
    <td><code>string</code></td>
    <td>The artifact version.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-artifactName"><code>artifactName</code></a></td>
    <td></td>
    <td>Get a Artifact overview information.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the available artifacts in the parent Artifact Store.</td>
</tr>
<tr>
    <td><a href="#update_state"><CopyableCode code="update_state" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-artifact_store_name"><code>artifact_store_name</code></a>, <a href="#parameter-artifact_version_name"><code>artifact_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-artifactName"><code>artifactName</code></a></td>
    <td></td>
    <td>Change artifact state defined in artifact store.</td>
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
<tr id="parameter-artifactName">
    <td><CopyableCode code="artifactName" /></td>
    <td><code>string</code></td>
    <td>The name of the artifact. Required.</td>
</tr>
<tr id="parameter-artifact_store_name">
    <td><CopyableCode code="artifact_store_name" /></td>
    <td><code>string</code></td>
    <td>The name of the artifact store. Required.</td>
</tr>
<tr id="parameter-artifact_version_name">
    <td><CopyableCode code="artifact_version_name" /></td>
    <td><code>string</code></td>
    <td>The name of the artifact version. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a Artifact overview information.

```sql
SELECT
id,
name,
artifactState,
artifactType,
artifactVersion,
systemData,
type
FROM azure.hybridnetwork.proxy_artifact
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND artifact_store_name = '{{ artifact_store_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND artifactName = '{{ artifactName }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the available artifacts in the parent Artifact Store.

```sql
SELECT
id,
name,
systemData,
type
FROM azure.hybridnetwork.proxy_artifact
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND artifact_store_name = '{{ artifact_store_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_state"
    values={[
        { label: 'update_state', value: 'update_state' }
    ]}
>
<TabItem value="update_state">

Change artifact state defined in artifact store.

```sql
UPDATE azure.hybridnetwork.proxy_artifact
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND artifact_store_name = '{{ artifact_store_name }}' --required
AND artifact_version_name = '{{ artifact_version_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND artifactName = '{{ artifactName }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
