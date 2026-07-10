--- 
title: feature_importances
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_importances
  - ai_personalizer
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

Creates, updates, deletes, gets or lists a <code>feature_importances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_importances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_personalizer.feature_importances" /></td></tr>
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
    <td><a href="#create_feature_importance"><CopyableCode code="create_feature_importance" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-feature_importance_id"><code>feature_importance_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create Feature Importance. Submit a new Feature Importance job.</td>
</tr>
<tr>
    <td><a href="#delete_feature_importance"><CopyableCode code="delete_feature_importance" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-feature_importance_id"><code>feature_importance_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Feature Importance. Delete the Feature Importance associated with the Id.</td>
</tr>
<tr>
    <td><a href="#list_feature_importances"><CopyableCode code="list_feature_importances" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a></td>
    <td>All Feature Importances. List of all Feature Importances.</td>
</tr>
<tr>
    <td><a href="#get_feature_importance"><CopyableCode code="get_feature_importance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-feature_importance_id"><code>feature_importance_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Feature Importance. Get the Feature Importance associated with the Id.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-feature_importance_id">
    <td><CopyableCode code="feature_importance_id" /></td>
    <td><code>string</code></td>
    <td>Id of the Feature Importance. Required.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>An offset into the collection of the first resource to be returned. Defaults to 0. Default value is 0.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the collection. Defaults to maximum value of integer. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_feature_importance"
    values={[
        { label: 'create_feature_importance', value: 'create_feature_importance' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_feature_importance">

Create Feature Importance. Submit a new Feature Importance job.

```sql
INSERT INTO azure.ai_personalizer.feature_importances (
feature_importance_id,
endpoint
)
SELECT 
'{{ feature_importance_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_importances
  props:
    - name: feature_importance_id
      value: "{{ feature_importance_id }}"
      description: Required parameter for the feature_importances resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the feature_importances resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_feature_importance"
    values={[
        { label: 'delete_feature_importance', value: 'delete_feature_importance' }
    ]}
>
<TabItem value="delete_feature_importance">

Feature Importance. Delete the Feature Importance associated with the Id.

```sql
DELETE FROM azure.ai_personalizer.feature_importances
WHERE feature_importance_id = '{{ feature_importance_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_feature_importances"
    values={[
        { label: 'list_feature_importances', value: 'list_feature_importances' },
        { label: 'get_feature_importance', value: 'get_feature_importance' }
    ]}
>
<TabItem value="list_feature_importances">

All Feature Importances. List of all Feature Importances.

```sql
EXEC azure.ai_personalizer.feature_importances.list_feature_importances 
@endpoint='{{ endpoint }}' --required, 
@top='{{ top }}', 
@skip='{{ skip }}'
;
```
</TabItem>
<TabItem value="get_feature_importance">

Feature Importance. Get the Feature Importance associated with the Id.

```sql
EXEC azure.ai_personalizer.feature_importances.get_feature_importance 
@feature_importance_id='{{ feature_importance_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
