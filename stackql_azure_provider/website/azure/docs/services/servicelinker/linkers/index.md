--- 
title: linkers
hide_title: false
hide_table_of_contents: false
keywords:
  - linkers
  - servicelinker
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

Creates, updates, deletes, gets or lists a <code>linkers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="linkers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicelinker.linkers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_dryrun"
    values={[
        { label: 'get_dryrun', value: 'get_dryrun' },
        { label: 'list_dryrun', value: 'list_dryrun' }
    ]}
>
<TabItem value="get_dryrun">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="operationPreviews" /></td>
    <td><code>array</code></td>
    <td>the preview of the operations for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameters of the dryrun.</td>
</tr>
<tr>
    <td><CopyableCode code="prerequisiteResults" /></td>
    <td><code>array</code></td>
    <td>the result of the dryrun.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
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
<TabItem value="list_dryrun">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="operationPreviews" /></td>
    <td><code>array</code></td>
    <td>the preview of the operations for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameters of the dryrun.</td>
</tr>
<tr>
    <td><CopyableCode code="prerequisiteResults" /></td>
    <td><code>array</code></td>
    <td>the result of the dryrun.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
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
    <td><a href="#get_dryrun"><CopyableCode code="get_dryrun" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>get a dryrun job.</td>
</tr>
<tr>
    <td><a href="#list_dryrun"><CopyableCode code="list_dryrun" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>list dryrun jobs.</td>
</tr>
<tr>
    <td><a href="#create_dryrun"><CopyableCode code="create_dryrun" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>create a dryrun job to do necessary check before actual creation.</td>
</tr>
<tr>
    <td><a href="#update_dryrun"><CopyableCode code="update_dryrun" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>add a dryrun job to do necessary check before actual creation.</td>
</tr>
<tr>
    <td><a href="#delete_dryrun"><CopyableCode code="delete_dryrun" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>delete a dryrun job.</td>
</tr>
<tr>
    <td><a href="#list_dapr_configurations"><CopyableCode code="list_dapr_configurations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>List the dapr configuration supported by Service Connector.</td>
</tr>
<tr>
    <td><a href="#generate_configurations"><CopyableCode code="generate_configurations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>Generate configurations for a Linker.</td>
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
<tr id="parameter-dryrun_name">
    <td><CopyableCode code="dryrun_name" /></td>
    <td><code>string</code></td>
    <td>The name of dryrun. Required.</td>
</tr>
<tr id="parameter-linker_name">
    <td><CopyableCode code="linker_name" /></td>
    <td><code>string</code></td>
    <td>The name Linker resource. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource to be connected. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_dryrun"
    values={[
        { label: 'get_dryrun', value: 'get_dryrun' },
        { label: 'list_dryrun', value: 'list_dryrun' }
    ]}
>
<TabItem value="get_dryrun">

get a dryrun job.

```sql
SELECT
id,
name,
operationPreviews,
parameters,
prerequisiteResults,
provisioningState,
systemData,
type
FROM azure.servicelinker.linkers
WHERE resource_uri = '{{ resource_uri }}' -- required
AND dryrun_name = '{{ dryrun_name }}' -- required
;
```
</TabItem>
<TabItem value="list_dryrun">

list dryrun jobs.

```sql
SELECT
id,
name,
operationPreviews,
parameters,
prerequisiteResults,
provisioningState,
systemData,
type
FROM azure.servicelinker.linkers
WHERE resource_uri = '{{ resource_uri }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_dryrun"
    values={[
        { label: 'create_dryrun', value: 'create_dryrun' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_dryrun">

create a dryrun job to do necessary check before actual creation.

```sql
INSERT INTO azure.servicelinker.linkers (
properties,
resource_uri,
dryrun_name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ dryrun_name }}'
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
- name: linkers
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the linkers resource.
    - name: dryrun_name
      value: "{{ dryrun_name }}"
      description: Required parameter for the linkers resource.
    - name: properties
      value:
        parameters:
          actionName: "{{ actionName }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_dryrun"
    values={[
        { label: 'update_dryrun', value: 'update_dryrun' }
    ]}
>
<TabItem value="update_dryrun">

add a dryrun job to do necessary check before actual creation.

```sql
UPDATE azure.servicelinker.linkers
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND dryrun_name = '{{ dryrun_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_dryrun"
    values={[
        { label: 'delete_dryrun', value: 'delete_dryrun' }
    ]}
>
<TabItem value="delete_dryrun">

delete a dryrun job.

```sql
DELETE FROM azure.servicelinker.linkers
WHERE resource_uri = '{{ resource_uri }}' --required
AND dryrun_name = '{{ dryrun_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_dapr_configurations"
    values={[
        { label: 'list_dapr_configurations', value: 'list_dapr_configurations' },
        { label: 'generate_configurations', value: 'generate_configurations' }
    ]}
>
<TabItem value="list_dapr_configurations">

List the dapr configuration supported by Service Connector.

```sql
EXEC azure.servicelinker.linkers.list_dapr_configurations 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="generate_configurations">

Generate configurations for a Linker.

```sql
EXEC azure.servicelinker.linkers.generate_configurations 
@resource_uri='{{ resource_uri }}' --required, 
@linker_name='{{ linker_name }}' --required 
@@json=
'{
"deleteOrUpdateBehavior": "{{ deleteOrUpdateBehavior }}", 
"action": "{{ action }}", 
"customizedKeys": "{{ customizedKeys }}", 
"daprProperties": "{{ daprProperties }}", 
"additionalConfigurations": "{{ additionalConfigurations }}", 
"additionalConnectionStringProperties": "{{ additionalConnectionStringProperties }}", 
"configurationStore": "{{ configurationStore }}"
}'
;
```
</TabItem>
</Tabs>
