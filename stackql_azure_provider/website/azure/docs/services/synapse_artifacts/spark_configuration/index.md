--- 
title: spark_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - spark_configuration
  - synapse_artifacts
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

Creates, updates, deletes, gets or lists a <code>spark_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="spark_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.spark_configuration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_spark_configuration"
    values={[
        { label: 'get_spark_configuration', value: 'get_spark_configuration' },
        { label: 'get_spark_configurations_by_workspace', value: 'get_spark_configurations_by_workspace' }
    ]}
>
<TabItem value="get_spark_configuration">

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
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>Annotations for SparkConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="configMergeRule" /></td>
    <td><code>object</code></td>
    <td>SparkConfiguration configMergeRule.</td>
</tr>
<tr>
    <td><CopyableCode code="configs" /></td>
    <td><code>object</code></td>
    <td>SparkConfiguration configs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of resource creation.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The identity that created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description about the SparkConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>additional Notes.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_spark_configurations_by_workspace">

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
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>Annotations for SparkConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="configMergeRule" /></td>
    <td><code>object</code></td>
    <td>SparkConfiguration configMergeRule.</td>
</tr>
<tr>
    <td><CopyableCode code="configs" /></td>
    <td><code>object</code></td>
    <td>SparkConfiguration configs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of resource creation.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The identity that created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description about the SparkConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>additional Notes.</td>
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
    <td><a href="#get_spark_configuration"><CopyableCode code="get_spark_configuration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-spark_configuration_name"><code>spark_configuration_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a sparkConfiguration.</td>
</tr>
<tr>
    <td><a href="#get_spark_configurations_by_workspace"><CopyableCode code="get_spark_configurations_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists sparkconfigurations.</td>
</tr>
<tr>
    <td><a href="#create_or_update_spark_configuration"><CopyableCode code="create_or_update_spark_configuration" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-spark_configuration_name"><code>spark_configuration_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-configs"><code>configs</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a sparkconfiguration.</td>
</tr>
<tr>
    <td><a href="#create_or_update_spark_configuration"><CopyableCode code="create_or_update_spark_configuration" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-spark_configuration_name"><code>spark_configuration_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-configs"><code>configs</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a sparkconfiguration.</td>
</tr>
<tr>
    <td><a href="#delete_spark_configuration"><CopyableCode code="delete_spark_configuration" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-spark_configuration_name"><code>spark_configuration_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a sparkConfiguration.</td>
</tr>
<tr>
    <td><a href="#rename_spark_configuration"><CopyableCode code="rename_spark_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-spark_configuration_name"><code>spark_configuration_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a sparkConfiguration.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-spark_configuration_name">
    <td><CopyableCode code="spark_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The spark Configuration name. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the sparkConfiguration entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the sparkConfiguration entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_spark_configuration"
    values={[
        { label: 'get_spark_configuration', value: 'get_spark_configuration' },
        { label: 'get_spark_configurations_by_workspace', value: 'get_spark_configurations_by_workspace' }
    ]}
>
<TabItem value="get_spark_configuration">

Gets a sparkConfiguration.

```sql
SELECT
id,
name,
annotations,
configMergeRule,
configs,
created,
createdBy,
description,
etag,
notes,
type
FROM azure.synapse_artifacts.spark_configuration
WHERE spark_configuration_name = '{{ spark_configuration_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_spark_configurations_by_workspace">

Lists sparkconfigurations.

```sql
SELECT
id,
name,
annotations,
configMergeRule,
configs,
created,
createdBy,
description,
etag,
notes,
type
FROM azure.synapse_artifacts.spark_configuration
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_spark_configuration"
    values={[
        { label: 'create_or_update_spark_configuration', value: 'create_or_update_spark_configuration' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_spark_configuration">

Creates or updates a sparkconfiguration.

```sql
INSERT INTO azure.synapse_artifacts.spark_configuration (
description,
configs,
annotations,
notes,
createdBy,
created,
configMergeRule,
spark_configuration_name,
endpoint,
If-Match
)
SELECT 
'{{ description }}',
'{{ configs }}' /* required */,
'{{ annotations }}',
'{{ notes }}',
'{{ createdBy }}',
'{{ created }}',
'{{ configMergeRule }}',
'{{ spark_configuration_name }}',
'{{ endpoint }}',
'{{ If-Match }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: spark_configuration
  props:
    - name: spark_configuration_name
      value: "{{ spark_configuration_name }}"
      description: Required parameter for the spark_configuration resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the spark_configuration resource.
    - name: description
      value: "{{ description }}"
      description: |
        Description about the SparkConfiguration.
    - name: configs
      value: "{{ configs }}"
      description: |
        SparkConfiguration configs. Required.
    - name: annotations
      value:
        - "{{ annotations }}"
      description: |
        Annotations for SparkConfiguration.
    - name: notes
      value: "{{ notes }}"
      description: |
        additional Notes.
    - name: createdBy
      value: "{{ createdBy }}"
      description: |
        The identity that created the resource.
    - name: created
      value: "{{ created }}"
      description: |
        The timestamp of resource creation.
    - name: configMergeRule
      value: "{{ configMergeRule }}"
      description: |
        SparkConfiguration configMergeRule.
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the sparkConfiguration entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the sparkConfiguration entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_spark_configuration"
    values={[
        { label: 'create_or_update_spark_configuration', value: 'create_or_update_spark_configuration' }
    ]}
>
<TabItem value="create_or_update_spark_configuration">

Creates or updates a sparkconfiguration.

```sql
REPLACE azure.synapse_artifacts.spark_configuration
SET 
description = '{{ description }}',
configs = '{{ configs }}',
annotations = '{{ annotations }}',
notes = '{{ notes }}',
createdBy = '{{ createdBy }}',
created = '{{ created }}',
configMergeRule = '{{ configMergeRule }}'
WHERE 
spark_configuration_name = '{{ spark_configuration_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND configs = '{{ configs }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_spark_configuration"
    values={[
        { label: 'delete_spark_configuration', value: 'delete_spark_configuration' }
    ]}
>
<TabItem value="delete_spark_configuration">

Deletes a sparkConfiguration.

```sql
DELETE FROM azure.synapse_artifacts.spark_configuration
WHERE spark_configuration_name = '{{ spark_configuration_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename_spark_configuration"
    values={[
        { label: 'rename_spark_configuration', value: 'rename_spark_configuration' }
    ]}
>
<TabItem value="rename_spark_configuration">

Renames a sparkConfiguration.

```sql
EXEC azure.synapse_artifacts.spark_configuration.rename_spark_configuration 
@spark_configuration_name='{{ spark_configuration_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
