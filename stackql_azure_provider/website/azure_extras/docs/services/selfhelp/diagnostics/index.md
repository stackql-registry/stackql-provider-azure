--- 
title: diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics
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

Creates, updates, deletes, gets or lists a <code>diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="diagnostics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.selfhelp.diagnostics" /></td></tr>
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
    <td><CopyableCode code="acceptedAt" /></td>
    <td><code>string</code></td>
    <td>Diagnostic Request Accepted time.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Array of Diagnostics.</td>
</tr>
<tr>
    <td><CopyableCode code="globalParameters" /></td>
    <td><code>object</code></td>
    <td>Global parameters is an optional map which can be used to add key and value to request body to improve the diagnostics results.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>array</code></td>
    <td>SolutionIds that are needed to be invoked.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of diagnostic provisioning. Known values are: "Succeeded", "PartialComplete", "Failed", "Running", and "Canceled".</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-diagnostics_resource_name"><code>diagnostics_resource_name</code></a></td>
    <td></td>
    <td>Get the diagnostics using the 'diagnosticsResourceName' you chose while creating the diagnostic.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-diagnostics_resource_name"><code>diagnostics_resource_name</code></a></td>
    <td></td>
    <td>Creates a diagnostic for the specific resource using solutionId from discovery solutions. Diagnostics are powerful solutions that access product resources or other relevant data and provide the root cause of the issue and the steps to address the issue..</td>
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
<tr id="parameter-diagnostics_resource_name">
    <td><CopyableCode code="diagnostics_resource_name" /></td>
    <td><code>string</code></td>
    <td>Unique resource name for insight resources. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>scope = resourceUri of affected resource. For example: /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read. Required.</td>
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

Get the diagnostics using the 'diagnosticsResourceName' you chose while creating the diagnostic.

```sql
SELECT
id,
name,
acceptedAt,
diagnostics,
globalParameters,
insights,
provisioningState,
systemData,
type
FROM azure_extras.selfhelp.diagnostics
WHERE scope = '{{ scope }}' -- required
AND diagnostics_resource_name = '{{ diagnostics_resource_name }}' -- required
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

Creates a diagnostic for the specific resource using solutionId from discovery solutions. Diagnostics are powerful solutions that access product resources or other relevant data and provide the root cause of the issue and the steps to address the issue..

```sql
INSERT INTO azure_extras.selfhelp.diagnostics (
properties,
scope,
diagnostics_resource_name
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ diagnostics_resource_name }}'
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
- name: diagnostics
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the diagnostics resource.
    - name: diagnostics_resource_name
      value: "{{ diagnostics_resource_name }}"
      description: Required parameter for the diagnostics resource.
    - name: properties
      value:
        globalParameters: "{{ globalParameters }}"
        insights:
          - solutionId: "{{ solutionId }}"
            additionalParameters: "{{ additionalParameters }}"
`}</CodeBlock>

</TabItem>
</Tabs>
