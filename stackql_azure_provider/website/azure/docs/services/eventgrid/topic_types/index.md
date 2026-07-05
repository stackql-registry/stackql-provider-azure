--- 
title: topic_types
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_types
  - eventgrid
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

Creates, updates, deletes, gets or lists a <code>topic_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="topic_types" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid.topic_types" /></td></tr>
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
    <td><CopyableCode code="additionalEnforcedPermissions" /></td>
    <td><code>array</code></td>
    <td>Permissions which are enforced for creating and updating system topics of this this topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="areRegionalAndGlobalSourcesSupported" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate that a topic type can support both regional or global system topics.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name for the topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>Namespace of the provider of the topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the topic type. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRegionType" /></td>
    <td><code>string</code></td>
    <td>Region type of the resource. Known values are: "RegionalResource" and "GlobalResource". (RegionalResource, GlobalResource)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceFormat" /></td>
    <td><code>string</code></td>
    <td>Source resource format.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedLocations" /></td>
    <td><code>array</code></td>
    <td>List of locations supported by this topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedScopesForSource" /></td>
    <td><code>array</code></td>
    <td>Supported source scopes.</td>
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
    <td><CopyableCode code="additionalEnforcedPermissions" /></td>
    <td><code>array</code></td>
    <td>Permissions which are enforced for creating and updating system topics of this this topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="areRegionalAndGlobalSourcesSupported" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate that a topic type can support both regional or global system topics.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name for the topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>Namespace of the provider of the topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the topic type. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRegionType" /></td>
    <td><code>string</code></td>
    <td>Region type of the resource. Known values are: "RegionalResource" and "GlobalResource". (RegionalResource, GlobalResource)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceFormat" /></td>
    <td><code>string</code></td>
    <td>Source resource format.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedLocations" /></td>
    <td><code>array</code></td>
    <td>List of locations supported by this topic type.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedScopesForSource" /></td>
    <td><code>array</code></td>
    <td>Supported source scopes.</td>
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
    <td><a href="#parameter-topic_type_name"><code>topic_type_name</code></a></td>
    <td></td>
    <td>Get a topic type. Get information about a topic type.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>List topic types. List all registered topic types.</td>
</tr>
<tr>
    <td><a href="#list_event_types"><CopyableCode code="list_event_types" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-topic_type_name"><code>topic_type_name</code></a></td>
    <td></td>
    <td>List event types. List event types for a topic type.</td>
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
<tr id="parameter-topic_type_name">
    <td><CopyableCode code="topic_type_name" /></td>
    <td><code>string</code></td>
    <td>Name of the topic type. Required.</td>
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

Get a topic type. Get information about a topic type.

```sql
SELECT
id,
name,
additionalEnforcedPermissions,
areRegionalAndGlobalSourcesSupported,
description,
displayName,
provider,
provisioningState,
resourceRegionType,
sourceResourceFormat,
supportedLocations,
supportedScopesForSource,
systemData,
type
FROM azure.eventgrid.topic_types
WHERE topic_type_name = '{{ topic_type_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List topic types. List all registered topic types.

```sql
SELECT
id,
name,
additionalEnforcedPermissions,
areRegionalAndGlobalSourcesSupported,
description,
displayName,
provider,
provisioningState,
resourceRegionType,
sourceResourceFormat,
supportedLocations,
supportedScopesForSource,
systemData,
type
FROM azure.eventgrid.topic_types
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_event_types"
    values={[
        { label: 'list_event_types', value: 'list_event_types' }
    ]}
>
<TabItem value="list_event_types">

List event types. List event types for a topic type.

```sql
EXEC azure.eventgrid.topic_types.list_event_types 
@topic_type_name='{{ topic_type_name }}' --required
;
```
</TabItem>
</Tabs>
