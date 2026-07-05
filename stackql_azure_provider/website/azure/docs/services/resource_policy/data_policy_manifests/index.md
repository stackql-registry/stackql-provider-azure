--- 
title: data_policy_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - data_policy_manifests
  - resource_policy
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

Creates, updates, deletes, gets or lists a <code>data_policy_manifests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_policy_manifests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_policy.data_policy_manifests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_policy_mode"
    values={[
        { label: 'get_by_policy_mode', value: 'get_by_policy_mode' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_policy_mode">

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
    <td><CopyableCode code="effects" /></td>
    <td><code>array</code></td>
    <td>The effect definition.</td>
</tr>
<tr>
    <td><CopyableCode code="fieldValues" /></td>
    <td><code>array</code></td>
    <td>The non-alias field accessor values that can be used in the policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isBuiltInOnly" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether policy mode is allowed only in built-in definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaces" /></td>
    <td><code>array</code></td>
    <td>The list of namespaces for the data policy manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="policyMode" /></td>
    <td><code>string</code></td>
    <td>The policy mode of the data policy manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceFunctions" /></td>
    <td><code>object</code></td>
    <td>The resource functions definition specified in the data manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTypeAliases" /></td>
    <td><code>array</code></td>
    <td>An array of resource type aliases.</td>
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
    <td><CopyableCode code="effects" /></td>
    <td><code>array</code></td>
    <td>The effect definition.</td>
</tr>
<tr>
    <td><CopyableCode code="fieldValues" /></td>
    <td><code>array</code></td>
    <td>The non-alias field accessor values that can be used in the policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isBuiltInOnly" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether policy mode is allowed only in built-in definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaces" /></td>
    <td><code>array</code></td>
    <td>The list of namespaces for the data policy manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="policyMode" /></td>
    <td><code>string</code></td>
    <td>The policy mode of the data policy manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceFunctions" /></td>
    <td><code>object</code></td>
    <td>The resource functions definition specified in the data manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTypeAliases" /></td>
    <td><code>array</code></td>
    <td>An array of resource type aliases.</td>
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
    <td><a href="#get_by_policy_mode"><CopyableCode code="get_by_policy_mode" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_mode"><code>policy_mode</code></a></td>
    <td></td>
    <td>Retrieves a data policy manifest. This operation retrieves the data policy manifest with the given policy mode.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves data policy manifests. This operation retrieves a list of all the data policy manifests that match the optional given $filter. Valid values for $filter are: \"$filter=namespace eq '&#123;0&#125;'\". If $filter is not provided, the unfiltered list includes all data policy manifests for data resource types. If $filter=namespace is provided, the returned list only includes all data policy manifests that have a namespace matching the provided value.</td>
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
<tr id="parameter-policy_mode">
    <td><CopyableCode code="policy_mode" /></td>
    <td><code>string</code></td>
    <td>The policy mode of the data policy manifest to get. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Valid values for $filter are: \"namespace eq '&#123;value&#125;'\". If $filter is not provided, no filtering is performed. If $filter=namespace eq '&#123;value&#125;' is provided, the returned list only includes all data policy manifests that have a namespace matching the provided value. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_policy_mode"
    values={[
        { label: 'get_by_policy_mode', value: 'get_by_policy_mode' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_policy_mode">

Retrieves a data policy manifest. This operation retrieves the data policy manifest with the given policy mode.

```sql
SELECT
id,
name,
effects,
fieldValues,
isBuiltInOnly,
namespaces,
policyMode,
resourceFunctions,
resourceTypeAliases,
systemData,
type
FROM azure.resource_policy.data_policy_manifests
WHERE policy_mode = '{{ policy_mode }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves data policy manifests. This operation retrieves a list of all the data policy manifests that match the optional given $filter. Valid values for $filter are: \"$filter=namespace eq '&#123;0&#125;'\". If $filter is not provided, the unfiltered list includes all data policy manifests for data resource types. If $filter=namespace is provided, the returned list only includes all data policy manifests that have a namespace matching the provided value.

```sql
SELECT
id,
name,
effects,
fieldValues,
isBuiltInOnly,
namespaces,
policyMode,
resourceFunctions,
resourceTypeAliases,
systemData,
type
FROM azure.resource_policy.data_policy_manifests
WHERE $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
