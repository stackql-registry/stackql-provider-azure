--- 
title: solution
hide_title: false
hide_table_of_contents: false
keywords:
  - solution
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

Creates, updates, deletes, gets or lists a <code>solution</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="solution" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.selfhelp.solution" /></td></tr>
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
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td>The HTML content that needs to be rendered and shown to customer.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Client input parameters to run Solution.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of solution provisioning. Known values are: "Succeeded", "PartialComplete", "Failed", "Running", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="replacementMaps" /></td>
    <td><code>object</code></td>
    <td>Solution replacement maps.</td>
</tr>
<tr>
    <td><CopyableCode code="sections" /></td>
    <td><code>array</code></td>
    <td>List of section object.</td>
</tr>
<tr>
    <td><CopyableCode code="solutionId" /></td>
    <td><code>string</code></td>
    <td>Solution Id to identify single solution.</td>
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
    <td><CopyableCode code="triggerCriteria" /></td>
    <td><code>array</code></td>
    <td>Solution request trigger criteria.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-solution_resource_name"><code>solution_resource_name</code></a></td>
    <td></td>
    <td>Get the solution using the applicable solutionResourceName while creating the solution.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-solution_resource_name"><code>solution_resource_name</code></a></td>
    <td></td>
    <td>Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId and requiredInputs’ from discovery solutions. Azure solutions comprise a comprehensive library of self-help resources that have been thoughtfully curated by Azure engineers to aid customers in resolving typical troubleshooting issues. These solutions encompass: (1.) Dynamic and context-aware diagnostics, guided troubleshooting wizards, and data visualizations. (2.) Rich instructional video tutorials and illustrative diagrams and images. (3.) Thoughtfully assembled textual troubleshooting instructions. All these components are seamlessly converged into unified solutions tailored to address a specific support problem area.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-solution_resource_name"><code>solution_resource_name</code></a></td>
    <td></td>
    <td>Update the requiredInputs or additional information needed to execute the solution.</td>
</tr>
<tr>
    <td><a href="#warm_up"><CopyableCode code="warm_up" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-solution_resource_name"><code>solution_resource_name</code></a></td>
    <td></td>
    <td>Warm up the solution resource by preloading asynchronous diagnostics results into cache.</td>
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
<tr id="parameter-solution_resource_name">
    <td><CopyableCode code="solution_resource_name" /></td>
    <td><code>string</code></td>
    <td>Solution resource Name. Required.</td>
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

Get the solution using the applicable solutionResourceName while creating the solution.

```sql
SELECT
id,
name,
content,
parameters,
provisioningState,
replacementMaps,
sections,
solutionId,
systemData,
title,
triggerCriteria,
type
FROM azure_extras.selfhelp.solution
WHERE scope = '{{ scope }}' -- required
AND solution_resource_name = '{{ solution_resource_name }}' -- required
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

Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId and requiredInputs’ from discovery solutions. Azure solutions comprise a comprehensive library of self-help resources that have been thoughtfully curated by Azure engineers to aid customers in resolving typical troubleshooting issues. These solutions encompass: (1.) Dynamic and context-aware diagnostics, guided troubleshooting wizards, and data visualizations. (2.) Rich instructional video tutorials and illustrative diagrams and images. (3.) Thoughtfully assembled textual troubleshooting instructions. All these components are seamlessly converged into unified solutions tailored to address a specific support problem area.

```sql
INSERT INTO azure_extras.selfhelp.solution (
properties,
scope,
solution_resource_name
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ solution_resource_name }}'
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
- name: solution
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the solution resource.
    - name: solution_resource_name
      value: "{{ solution_resource_name }}"
      description: Required parameter for the solution resource.
    - name: properties
      value:
        triggerCriteria:
          - name: "{{ name }}"
            value: "{{ value }}"
        parameters: "{{ parameters }}"
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

Update the requiredInputs or additional information needed to execute the solution.

```sql
UPDATE azure_extras.selfhelp.solution
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND solution_resource_name = '{{ solution_resource_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="warm_up"
    values={[
        { label: 'warm_up', value: 'warm_up' }
    ]}
>
<TabItem value="warm_up">

Warm up the solution resource by preloading asynchronous diagnostics results into cache.

```sql
EXEC azure_extras.selfhelp.solution.warm_up 
@scope='{{ scope }}' --required, 
@solution_resource_name='{{ solution_resource_name }}' --required 
@@json=
'{
"parameters": "{{ parameters }}"
}'
;
```
</TabItem>
</Tabs>
