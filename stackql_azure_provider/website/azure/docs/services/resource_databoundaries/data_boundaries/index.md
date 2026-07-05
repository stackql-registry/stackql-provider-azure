--- 
title: data_boundaries
hide_title: false
hide_table_of_contents: false
keywords:
  - data_boundaries
  - resource_databoundaries
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

Creates, updates, deletes, gets or lists a <code>data_boundaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_boundaries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_databoundaries.data_boundaries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_scope"
    values={[
        { label: 'get_scope', value: 'get_scope' },
        { label: 'get_tenant', value: 'get_tenant' }
    ]}
>
<TabItem value="get_scope">

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
    <td><CopyableCode code="dataBoundary" /></td>
    <td><code>string</code></td>
    <td>The data boundary definition. Known values are: "NotDefined", "Global", and "EU". (NotDefined, Global, EU)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "Accepted", "Running", "Creating", "Canceled", "Failed", "Succeeded", and "Updating". (Accepted, Running, Creating, Canceled, Failed, Succeeded, Updating)</td>
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
<TabItem value="get_tenant">

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
    <td><CopyableCode code="dataBoundary" /></td>
    <td><code>string</code></td>
    <td>The data boundary definition. Known values are: "NotDefined", "Global", and "EU". (NotDefined, Global, EU)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "Accepted", "Running", "Creating", "Canceled", "Failed", "Succeeded", and "Updating". (Accepted, Running, Creating, Canceled, Failed, Succeeded, Updating)</td>
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
    <td><a href="#get_scope"><CopyableCode code="get_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-default"><code>default</code></a></td>
    <td></td>
    <td>Get data boundary at specified scope.</td>
</tr>
<tr>
    <td><a href="#get_tenant"><CopyableCode code="get_tenant" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-default"><code>default</code></a></td>
    <td></td>
    <td>Get data boundary of tenant.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-default"><code>default</code></a></td>
    <td></td>
    <td>Opt-in tenant to data boundary.</td>
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
<tr id="parameter-default">
    <td><CopyableCode code="default" /></td>
    <td><code>string</code></td>
    <td>Default string modeled as parameter for auto generation to work correctly. "default" Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_scope"
    values={[
        { label: 'get_scope', value: 'get_scope' },
        { label: 'get_tenant', value: 'get_tenant' }
    ]}
>
<TabItem value="get_scope">

Get data boundary at specified scope.

```sql
SELECT
id,
name,
dataBoundary,
provisioningState,
systemData,
type
FROM azure.resource_databoundaries.data_boundaries
WHERE scope = '{{ scope }}' -- required
AND default = '{{ default }}' -- required
;
```
</TabItem>
<TabItem value="get_tenant">

Get data boundary of tenant.

```sql
SELECT
id,
name,
dataBoundary,
provisioningState,
systemData,
type
FROM azure.resource_databoundaries.data_boundaries
WHERE default = '{{ default }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' }
    ]}
>
<TabItem value="put">

Opt-in tenant to data boundary.

```sql
EXEC azure.resource_databoundaries.data_boundaries.put 
@default='{{ default }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
