--- 
title: pipeline_topologies
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_topologies
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>pipeline_topologies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipeline_topologies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.video_analyzer.pipeline_topologies" /></td></tr>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="processors" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sinks" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU details. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="sources" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><CopyableCode code="@nextLink" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#parameter-pipeline_topology_name"><code>pipeline_topology_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a specific pipeline topology by name. Retrieves a specific pipeline topology by name. If a topology with that name has been previously created, the call will return the JSON representation of that topology.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Retrieves a list of pipeline topologies. Retrieves a list of pipeline topologies that have been added to the account, if any, along with their JSON representation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-pipeline_topology_name"><code>pipeline_topology_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates or updates a pipeline topology. Creates a new pipeline topology or updates an existing one, with the given name. A pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-pipeline_topology_name"><code>pipeline_topology_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing pipeline topology. Updates an existing pipeline topology with the given name. If the associated live pipelines or pipeline jobs are in active or processing state, respectively, then only the description can be updated. Else, the properties that can be updated include: description, parameter declarations, sources, processors, and sinks.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pipeline_topology_name"><code>pipeline_topology_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates or updates a pipeline topology. Creates a new pipeline topology or updates an existing one, with the given name. A pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pipeline_topology_name"><code>pipeline_topology_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a pipeline topology. Deletes a pipeline topology with the given name. This method should be called after all instances of the topology have been stopped and deleted.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The Azure Video Analyzer account name.</td>
</tr>
<tr id="parameter-pipeline_topology_name">
    <td><CopyableCode code="pipeline_topology_name" /></td>
    <td><code>string</code></td>
    <td>Pipeline topology unique identifier.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Restricts the set of items returned.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.</td>
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

Retrieves a specific pipeline topology by name. Retrieves a specific pipeline topology by name. If a topology with that name has been previously created, the call will return the JSON representation of that topology.

```sql
SELECT
id,
name,
description,
kind,
parameters,
processors,
sinks,
sku,
sources,
systemData,
type
FROM azure_extras.video_analyzer.pipeline_topologies
WHERE pipeline_topology_name = '{{ pipeline_topology_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of pipeline topologies. Retrieves a list of pipeline topologies that have been added to the account, if any, along with their JSON representation.

```sql
SELECT
@nextLink,
value
FROM azure_extras.video_analyzer.pipeline_topologies
WHERE account_name = '{{ account_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a pipeline topology. Creates a new pipeline topology or updates an existing one, with the given name. A pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics.

```sql
INSERT INTO azure_extras.video_analyzer.pipeline_topologies (
kind,
sku,
properties,
pipeline_topology_name,
account_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ kind }}' /* required */,
'{{ sku }}' /* required */,
'{{ properties }}',
'{{ pipeline_topology_name }}',
'{{ account_name }}',
'{{ resource_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
properties,
sku,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: pipeline_topologies
  props:
    - name: pipeline_topology_name
      value: "{{ pipeline_topology_name }}"
      description: Required parameter for the pipeline_topologies resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the pipeline_topologies resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the pipeline_topologies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the pipeline_topologies resource.
    - name: kind
      value: "{{ kind }}"
    - name: sku
      description: |
        The SKU details. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: properties
      value:
        description: "{{ description }}"
        parameters:
          - name: "{{ name }}"
            type: "{{ type }}"
            description: "{{ description }}"
            default: "{{ default }}"
        sources:
          - @type: "{{ @type }}"
            name: "{{ name }}"
        processors:
          - @type: "{{ @type }}"
            name: "{{ name }}"
            inputs: "{{ inputs }}"
        sinks:
          - @type: "{{ @type }}"
            name: "{{ name }}"
            inputs: "{{ inputs }}"
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

Updates an existing pipeline topology. Updates an existing pipeline topology with the given name. If the associated live pipelines or pipeline jobs are in active or processing state, respectively, then only the description can be updated. Else, the properties that can be updated include: description, parameter declarations, sources, processors, and sinks.

```sql
UPDATE azure_extras.video_analyzer.pipeline_topologies
SET 
kind = '{{ kind }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
pipeline_topology_name = '{{ pipeline_topology_name }}' --required
AND account_name = '{{ account_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
sku,
systemData,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a pipeline topology. Creates a new pipeline topology or updates an existing one, with the given name. A pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics.

```sql
REPLACE azure_extras.video_analyzer.pipeline_topologies
SET 
kind = '{{ kind }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
pipeline_topology_name = '{{ pipeline_topology_name }}' --required
AND account_name = '{{ account_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND kind = '{{ kind }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
kind,
properties,
sku,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a pipeline topology. Deletes a pipeline topology with the given name. This method should be called after all instances of the topology have been stopped and deleted.

```sql
DELETE FROM azure_extras.video_analyzer.pipeline_topologies
WHERE pipeline_topology_name = '{{ pipeline_topology_name }}' --required
AND account_name = '{{ account_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
