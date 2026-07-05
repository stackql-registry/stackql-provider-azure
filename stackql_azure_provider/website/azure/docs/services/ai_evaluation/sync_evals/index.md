--- 
title: sync_evals
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_evals
  - ai_evaluation
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

Creates, updates, deletes, gets or lists a <code>sync_evals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sync_evals" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.sync_evals" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-data_source"><code>data_source</code></a>, <a href="#parameter-testing_criteria"><code>testing_criteria</code></a></td>
    <td></td>
    <td>Synchronize evaluation runs from connected resources.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Synchronize evaluation runs from connected resources.

```sql
INSERT INTO azure.ai_evaluation.sync_evals (
data_source,
testing_criteria,
properties,
customInference,
endpoint
)
SELECT 
'{{ data_source }}' /* required */,
'{{ testing_criteria }}' /* required */,
'{{ properties }}',
'{{ customInference }}',
'{{ endpoint }}'
RETURNING
id,
datasource_item_id,
eval_id,
run_id,
created_at,
datasource_item,
object,
results,
sample,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sync_evals
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the sync_evals resource.
    - name: data_source
      description: |
        Identifier of the evaluator. Required.
      value:
        type: "{{ type }}"
        source:
          type: "{{ type }}"
          content:
            item:
              type: "{{ type }}"
            sample: "{{ sample }}"
    - name: testing_criteria
      description: |
        Evaluators to be used for the evaluation. Required.
      value:
        - type: "{{ type }}"
          name: "{{ name }}"
          evaluator_name: "{{ evaluator_name }}"
          evaluator_version: "{{ evaluator_version }}"
          initialization_parameters: "{{ initialization_parameters }}"
          data_mapping: "{{ data_mapping }}"
    - name: properties
      value: "{{ properties }}"
      description: |
        Evaluation's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.
    - name: customInference
      description: |
        Custom inference configuration.
      value:
        endpointUrl: "{{ endpointUrl }}"
        DeploymentId: "{{ DeploymentId }}"
`}</CodeBlock>

</TabItem>
</Tabs>
