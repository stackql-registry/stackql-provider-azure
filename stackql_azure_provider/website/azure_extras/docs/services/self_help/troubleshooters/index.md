--- 
title: troubleshooters
hide_title: false
hide_table_of_contents: false
keywords:
  - troubleshooters
  - self_help
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

Creates, updates, deletes, gets or lists a <code>troubleshooters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="troubleshooters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.self_help.troubleshooters" /></td></tr>
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
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Client input parameters to run Troubleshooter Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of troubleshooter provisioning. Known values are: "Succeeded", "Failed", "Canceled", "Running", and "AutoContinue".</td>
</tr>
<tr>
    <td><CopyableCode code="solutionId" /></td>
    <td><code>string</code></td>
    <td>Solution Id to identify single troubleshooter.</td>
</tr>
<tr>
    <td><CopyableCode code="steps" /></td>
    <td><code>array</code></td>
    <td>List of step object.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-troubleshooter_name"><code>troubleshooter_name</code></a></td>
    <td></td>
    <td>Gets troubleshooter instance result which includes the step status/result of the troubleshooter resource name that is being executed. Get API is used to retrieve the result of a Troubleshooter instance, which includes the status and result of each step in the Troubleshooter workflow. This API requires the Troubleshooter resource name that was created using the Create API.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-troubleshooter_name"><code>troubleshooter_name</code></a></td>
    <td></td>
    <td>Creates the specific troubleshooter action under a resource or subscription using the ‘solutionId’ and ‘properties.parameters’ as the trigger. Azure Troubleshooters help with hard to classify issues, reducing the gap between customer observed problems and solutions by guiding the user effortlessly through the troubleshooting process. Each Troubleshooter flow represents a problem area within Azure and has a complex tree-like structure that addresses many root causes. These flows are prepared with the help of Subject Matter experts and customer support engineers by carefully considering previous support requests raised by customers. Troubleshooters terminate at a well curated solution based off of resource backend signals and customer manual selections.</td>
</tr>
<tr>
    <td><a href="#continue_method"><CopyableCode code="continue_method" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-troubleshooter_name"><code>troubleshooter_name</code></a></td>
    <td></td>
    <td>Uses ‘stepId’ and ‘responses’ as the trigger to continue the troubleshooting steps for the respective troubleshooter resource name. Continue API is used to provide inputs that are required for the specific troubleshooter to progress into the next step in the process. This API is used after the Troubleshooter has been created using the Create API.</td>
</tr>
<tr>
    <td><a href="#end"><CopyableCode code="end" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-troubleshooter_name"><code>troubleshooter_name</code></a></td>
    <td></td>
    <td>Ends the troubleshooter action.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-troubleshooter_name"><code>troubleshooter_name</code></a></td>
    <td></td>
    <td>Restarts the troubleshooter API using applicable troubleshooter resource name as the input. It returns new resource name which should be used in subsequent request. The old resource name is obsolete after this API is invoked.</td>
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
<tr id="parameter-troubleshooter_name">
    <td><CopyableCode code="troubleshooter_name" /></td>
    <td><code>string</code></td>
    <td>Troubleshooter resource Name. Required.</td>
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

Gets troubleshooter instance result which includes the step status/result of the troubleshooter resource name that is being executed. Get API is used to retrieve the result of a Troubleshooter instance, which includes the status and result of each step in the Troubleshooter workflow. This API requires the Troubleshooter resource name that was created using the Create API.

```sql
SELECT
id,
name,
parameters,
provisioningState,
solutionId,
steps,
systemData,
type
FROM azure_extras.self_help.troubleshooters
WHERE scope = '{{ scope }}' -- required
AND troubleshooter_name = '{{ troubleshooter_name }}' -- required
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

Creates the specific troubleshooter action under a resource or subscription using the ‘solutionId’ and ‘properties.parameters’ as the trigger. Azure Troubleshooters help with hard to classify issues, reducing the gap between customer observed problems and solutions by guiding the user effortlessly through the troubleshooting process. Each Troubleshooter flow represents a problem area within Azure and has a complex tree-like structure that addresses many root causes. These flows are prepared with the help of Subject Matter experts and customer support engineers by carefully considering previous support requests raised by customers. Troubleshooters terminate at a well curated solution based off of resource backend signals and customer manual selections.

```sql
INSERT INTO azure_extras.self_help.troubleshooters (
properties,
scope,
troubleshooter_name
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ troubleshooter_name }}'
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
- name: troubleshooters
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the troubleshooters resource.
    - name: troubleshooter_name
      value: "{{ troubleshooter_name }}"
      description: Required parameter for the troubleshooters resource.
    - name: properties
      value:
        solutionId: "{{ solutionId }}"
        parameters: "{{ parameters }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="continue_method"
    values={[
        { label: 'continue_method', value: 'continue_method' },
        { label: 'end', value: 'end' },
        { label: 'restart', value: 'restart' }
    ]}
>
<TabItem value="continue_method">

Uses ‘stepId’ and ‘responses’ as the trigger to continue the troubleshooting steps for the respective troubleshooter resource name. Continue API is used to provide inputs that are required for the specific troubleshooter to progress into the next step in the process. This API is used after the Troubleshooter has been created using the Create API.

```sql
EXEC azure_extras.self_help.troubleshooters.continue_method 
@scope='{{ scope }}' --required, 
@troubleshooter_name='{{ troubleshooter_name }}' --required 
@@json=
'{
"stepId": "{{ stepId }}", 
"responses": "{{ responses }}"
}'
;
```
</TabItem>
<TabItem value="end">

Ends the troubleshooter action.

```sql
EXEC azure_extras.self_help.troubleshooters.end 
@scope='{{ scope }}' --required, 
@troubleshooter_name='{{ troubleshooter_name }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restarts the troubleshooter API using applicable troubleshooter resource name as the input. It returns new resource name which should be used in subsequent request. The old resource name is obsolete after this API is invoked.

```sql
EXEC azure_extras.self_help.troubleshooters.restart 
@scope='{{ scope }}' --required, 
@troubleshooter_name='{{ troubleshooter_name }}' --required
;
```
</TabItem>
</Tabs>
