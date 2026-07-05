--- 
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - chaos
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

Creates, updates, deletes, gets or lists an <code>actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.chaos.actions" /></td></tr>
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
    <td><CopyableCode code="actionName" /></td>
    <td><code>string</code></td>
    <td>The short name of the action (e.g., "Shutdown").</td>
</tr>
<tr>
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>The type of the action. Known values are: "Discrete", "Continuous", and "Cancelable". (Discrete, Continuous, Cancelable)</td>
</tr>
<tr>
    <td><CopyableCode code="canonicalId" /></td>
    <td><code>string</code></td>
    <td>Canonical identifier of the action (e.g., "microsoft-compute-shutdown/1.0").</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of what this action does.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Human-readable display name of the action.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersSchema" /></td>
    <td><code>object</code></td>
    <td>JSON Schema describing the parameters for this action.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedRoles" /></td>
    <td><code>array</code></td>
    <td>Recommended Azure RBAC role definition GUIDs for this action.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedTargetTypes" /></td>
    <td><code>array</code></td>
    <td>List of target types supported by this action.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the action (e.g., "1.0.0").</td>
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
    <td><CopyableCode code="actionName" /></td>
    <td><code>string</code></td>
    <td>The short name of the action (e.g., "Shutdown").</td>
</tr>
<tr>
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>The type of the action. Known values are: "Discrete", "Continuous", and "Cancelable". (Discrete, Continuous, Cancelable)</td>
</tr>
<tr>
    <td><CopyableCode code="canonicalId" /></td>
    <td><code>string</code></td>
    <td>Canonical identifier of the action (e.g., "microsoft-compute-shutdown/1.0").</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of what this action does.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Human-readable display name of the action.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersSchema" /></td>
    <td><code>object</code></td>
    <td>JSON Schema describing the parameters for this action.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedRoles" /></td>
    <td><code>array</code></td>
    <td>Recommended Azure RBAC role definition GUIDs for this action.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedTargetTypes" /></td>
    <td><code>array</code></td>
    <td>List of target types supported by this action.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the action (e.g., "1.0.0").</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-action_name"><code>action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an Action resource for a given location.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-continuationToken"><code>continuationToken</code></a></td>
    <td>Get a list of Action resources for a given location.</td>
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
<tr id="parameter-action_name">
    <td><CopyableCode code="action_name" /></td>
    <td><code>string</code></td>
    <td>String that represents an Action resource name. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>String that sets the continuation token. Default value is None.</td>
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

Get an Action resource for a given location.

```sql
SELECT
id,
name,
actionName,
actionType,
canonicalId,
description,
displayName,
parametersSchema,
recommendedRoles,
supportedTargetTypes,
systemData,
type,
version
FROM azure_extras.chaos.actions
WHERE location = '{{ location }}' -- required
AND action_name = '{{ action_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of Action resources for a given location.

```sql
SELECT
id,
name,
actionName,
actionType,
canonicalId,
description,
displayName,
parametersSchema,
recommendedRoles,
supportedTargetTypes,
systemData,
type,
version
FROM azure_extras.chaos.actions
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND continuationToken = '{{ continuationToken }}'
;
```
</TabItem>
</Tabs>
