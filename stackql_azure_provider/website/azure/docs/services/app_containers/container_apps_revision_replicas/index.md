--- 
title: container_apps_revision_replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_revision_replicas
  - app_containers
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

Creates, updates, deletes, gets or lists a <code>container_apps_revision_replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps_revision_replicas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_containers.container_apps_revision_replicas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_replica"
    values={[
        { label: 'get_replica', value: 'get_replica' },
        { label: 'list_replicas', value: 'list_replicas' }
    ]}
>
<TabItem value="get_replica">

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
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>The containers collection under a replica.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp describing when the pod was created by controller.</td>
</tr>
<tr>
    <td><CopyableCode code="initContainers" /></td>
    <td><code>array</code></td>
    <td>The init containers collection under a replica.</td>
</tr>
<tr>
    <td><CopyableCode code="runningState" /></td>
    <td><code>string</code></td>
    <td>Current running state of the replica. Known values are: "Running", "NotRunning", and "Unknown". (Running, NotRunning, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="runningStateDetails" /></td>
    <td><code>string</code></td>
    <td>The details of replica current running state.</td>
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
<TabItem value="list_replicas">

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
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>The containers collection under a replica.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp describing when the pod was created by controller.</td>
</tr>
<tr>
    <td><CopyableCode code="initContainers" /></td>
    <td><code>array</code></td>
    <td>The init containers collection under a replica.</td>
</tr>
<tr>
    <td><CopyableCode code="runningState" /></td>
    <td><code>string</code></td>
    <td>Current running state of the replica. Known values are: "Running", "NotRunning", and "Unknown". (Running, NotRunning, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="runningStateDetails" /></td>
    <td><code>string</code></td>
    <td>The details of replica current running state.</td>
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
    <td><a href="#get_replica"><CopyableCode code="get_replica" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-revision_name"><code>revision_name</code></a>, <a href="#parameter-replica_name"><code>replica_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a replica for a Container App Revision. Get a replica for a Container App Revision.</td>
</tr>
<tr>
    <td><a href="#list_replicas"><CopyableCode code="list_replicas" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-revision_name"><code>revision_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List replicas for a Container App Revision. List replicas for a Container App Revision.</td>
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
<tr id="parameter-container_app_name">
    <td><CopyableCode code="container_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App. Required.</td>
</tr>
<tr id="parameter-replica_name">
    <td><CopyableCode code="replica_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App Revision Replica. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-revision_name">
    <td><CopyableCode code="revision_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App Revision. Required.</td>
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
    defaultValue="get_replica"
    values={[
        { label: 'get_replica', value: 'get_replica' },
        { label: 'list_replicas', value: 'list_replicas' }
    ]}
>
<TabItem value="get_replica">

Get a replica for a Container App Revision. Get a replica for a Container App Revision.

```sql
SELECT
id,
name,
containers,
createdTime,
initContainers,
runningState,
runningStateDetails,
systemData,
type
FROM azure.app_containers.container_apps_revision_replicas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND revision_name = '{{ revision_name }}' -- required
AND replica_name = '{{ replica_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_replicas">

List replicas for a Container App Revision. List replicas for a Container App Revision.

```sql
SELECT
id,
name,
containers,
createdTime,
initContainers,
runningState,
runningStateDetails,
systemData,
type
FROM azure.app_containers.container_apps_revision_replicas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND revision_name = '{{ revision_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
