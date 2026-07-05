--- 
title: simplified_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - simplified_solutions
  - selfhelp
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

Creates, updates, deletes, gets or lists a <code>simplified_solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="simplified_solutions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.selfhelp.simplified_solutions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="appendix" /></td>
    <td><code>object</code></td>
    <td>Additional parameter response for Simplified Solutions.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td>The HTML content that needs to be rendered and shown to customer.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Client input parameters to run Simplified Solutions.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of Simplified Solution provisioning. Known values are: "Succeeded", "PartialComplete", "Failed", "Running", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="solutionId" /></td>
    <td><code>string</code></td>
    <td>Solution Id to identify single Simplified Solution.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-simplified_solutions_resource_name"><code>simplified_solutions_resource_name</code></a></td>
    <td></td>
    <td>Get the simplified Solutions using the applicable solutionResourceName while creating the simplified Solutions.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-simplified_solutions_resource_name"><code>simplified_solutions_resource_name</code></a></td>
    <td></td>
    <td>Creates Simplified Solutions for an Azure subscription using 'solutionId' from Discovery Solutions as the input. Simplified Solutions API makes the consumption of solutions APIs easier while still providing access to the same powerful solutions rendered in Solutions API. With Simplified Solutions, users don't have to worry about stitching together the article using replacement maps and can use the content in the API response to directly render as HTML content..</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>scope = resourceUri of affected resource. For example: /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read. Required.</td>
</tr>
<tr id="parameter-simplified_solutions_resource_name">
    <td><CopyableCode code="simplified_solutions_resource_name" /></td>
    <td><code>string</code></td>
    <td>Simplified Solutions Resource Name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get the simplified Solutions using the applicable solutionResourceName while creating the simplified Solutions.

```sql
SELECT
id,
name,
appendix,
content,
parameters,
provisioningState,
solutionId,
systemData,
title,
type
FROM azure_extras.selfhelp.simplified_solutions
WHERE scope = '{{ scope }}' -- required
AND simplified_solutions_resource_name = '{{ simplified_solutions_resource_name }}' -- required
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

Creates Simplified Solutions for an Azure subscription using 'solutionId' from Discovery Solutions as the input. Simplified Solutions API makes the consumption of solutions APIs easier while still providing access to the same powerful solutions rendered in Solutions API. With Simplified Solutions, users don't have to worry about stitching together the article using replacement maps and can use the content in the API response to directly render as HTML content..

```sql
INSERT INTO azure_extras.selfhelp.simplified_solutions (
properties,
scope,
simplified_solutions_resource_name
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ simplified_solutions_resource_name }}'
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
- name: simplified_solutions
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the simplified_solutions resource.
    - name: simplified_solutions_resource_name
      value: "{{ simplified_solutions_resource_name }}"
      description: Required parameter for the simplified_solutions resource.
    - name: properties
      value:
        solutionId: "{{ solutionId }}"
        parameters: "{{ parameters }}"
`}</CodeBlock>

</TabItem>
</Tabs>
