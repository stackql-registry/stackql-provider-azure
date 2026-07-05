--- 
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
  - onlineexperimentation_dataplane
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

Creates, updates, deletes, gets or lists a <code>metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metrics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.onlineexperimentation_dataplane.metrics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_metric"
    values={[
        { label: 'get_metric', value: 'get_metric' },
        { label: 'list_metrics', value: 'list_metrics' }
    ]}
>
<TabItem value="get_metric">

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
    <td>Identifier for this experiment metric. Must start with a lowercase letter and contain only lowercase letters, numbers, and underscores. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>Categories associated with the experiment metric. Used for organizing and filtering metrics. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>The metric definition specifying how the metric value is calculated from event data. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A detailed description of the experiment metric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="desiredDirection" /></td>
    <td><code>string</code></td>
    <td>The desired direction for changes in the metric value. Required. Known values are: "Increase", "Decrease", and "Neutral". (Increase, Decrease, Neutral)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A user-friendly display name for the experiment metric shown in reports and dashboards. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>ETag of the experiment metric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp (UTC) of the last modification to the experiment metric resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle" /></td>
    <td><code>string</code></td>
    <td>Determines whether it is included in experiment analysis. Required. Known values are: "Active" and "Inactive". (Active, Inactive)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_metrics">

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
    <td>Identifier for this experiment metric. Must start with a lowercase letter and contain only lowercase letters, numbers, and underscores. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>Categories associated with the experiment metric. Used for organizing and filtering metrics. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>The metric definition specifying how the metric value is calculated from event data. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A detailed description of the experiment metric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="desiredDirection" /></td>
    <td><code>string</code></td>
    <td>The desired direction for changes in the metric value. Required. Known values are: "Increase", "Decrease", and "Neutral". (Increase, Decrease, Neutral)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A user-friendly display name for the experiment metric shown in reports and dashboards. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>ETag of the experiment metric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp (UTC) of the last modification to the experiment metric resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle" /></td>
    <td><code>string</code></td>
    <td>Determines whether it is included in experiment analysis. Required. Known values are: "Active" and "Inactive". (Active, Inactive)</td>
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
    <td><a href="#get_metric"><CopyableCode code="get_metric" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-experiment_metric_id"><code>experiment_metric_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a></td>
    <td>Fetches an experiment metric by ID.</td>
</tr>
<tr>
    <td><a href="#list_metrics"><CopyableCode code="list_metrics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Lists experiment metrics.</td>
</tr>
<tr>
    <td><a href="#create_or_update_metric"><CopyableCode code="create_or_update_metric" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-experiment_metric_id"><code>experiment_metric_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-lifecycle"><code>lifecycle</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-categories"><code>categories</code></a>, <a href="#parameter-desiredDirection"><code>desiredDirection</code></a>, <a href="#parameter-definition"><code>definition</code></a></td>
    <td><a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a></td>
    <td>Creates or updates an experiment metric.</td>
</tr>
<tr>
    <td><a href="#create_or_update_metric"><CopyableCode code="create_or_update_metric" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-experiment_metric_id"><code>experiment_metric_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-lifecycle"><code>lifecycle</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-categories"><code>categories</code></a>, <a href="#parameter-desiredDirection"><code>desiredDirection</code></a>, <a href="#parameter-definition"><code>definition</code></a></td>
    <td><a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a></td>
    <td>Creates or updates an experiment metric.</td>
</tr>
<tr>
    <td><a href="#delete_metric"><CopyableCode code="delete_metric" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-experiment_metric_id"><code>experiment_metric_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a></td>
    <td>Deletes an experiment metric.</td>
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
<tr id="parameter-experiment_metric_id">
    <td><CopyableCode code="experiment_metric_id" /></td>
    <td><code>string</code></td>
    <td>Identifier for this experiment metric. Must start with a lowercase letter and contain only lowercase letters, numbers, and underscores. Required.</td>
</tr>
<tr id="parameter-If-Modified-Since">
    <td><CopyableCode code="If-Modified-Since" /></td>
    <td><code>string</code></td>
    <td>The request should only proceed if the entity was modified after this time. Default value is None.</td>
</tr>
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td>The request should only proceed if the entity was not modified after this time. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_metric"
    values={[
        { label: 'get_metric', value: 'get_metric' },
        { label: 'list_metrics', value: 'list_metrics' }
    ]}
>
<TabItem value="get_metric">

Fetches an experiment metric by ID.

```sql
SELECT
id,
categories,
definition,
description,
desiredDirection,
displayName,
eTag,
lastModifiedAt,
lifecycle
FROM azure.onlineexperimentation_dataplane.metrics
WHERE experiment_metric_id = '{{ experiment_metric_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
;
```
</TabItem>
<TabItem value="list_metrics">

Lists experiment metrics.

```sql
SELECT
id,
categories,
definition,
description,
desiredDirection,
displayName,
eTag,
lastModifiedAt,
lifecycle
FROM azure.onlineexperimentation_dataplane.metrics
WHERE endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_metric"
    values={[
        { label: 'create_or_update_metric', value: 'create_or_update_metric' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_metric">

Creates or updates an experiment metric.

```sql
INSERT INTO azure.onlineexperimentation_dataplane.metrics (
lifecycle,
displayName,
description,
categories,
desiredDirection,
definition,
experiment_metric_id,
endpoint,
If-Unmodified-Since,
If-Modified-Since
)
SELECT 
'{{ lifecycle }}' /* required */,
'{{ displayName }}' /* required */,
'{{ description }}' /* required */,
'{{ categories }}' /* required */,
'{{ desiredDirection }}' /* required */,
'{{ definition }}' /* required */,
'{{ experiment_metric_id }}',
'{{ endpoint }}',
'{{ If-Unmodified-Since }}',
'{{ If-Modified-Since }}'
RETURNING
id,
categories,
definition,
description,
desiredDirection,
displayName,
eTag,
lastModifiedAt,
lifecycle
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: metrics
  props:
    - name: experiment_metric_id
      value: "{{ experiment_metric_id }}"
      description: Required parameter for the metrics resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the metrics resource.
    - name: lifecycle
      value: "{{ lifecycle }}"
      description: |
        Determines whether it is included in experiment analysis. Required. Known values are: "Active" and "Inactive".
      valid_values: ['Active', 'Inactive']
    - name: displayName
      value: "{{ displayName }}"
      description: |
        A user-friendly display name for the experiment metric shown in reports and dashboards. Required.
    - name: description
      value: "{{ description }}"
      description: |
        A detailed description of the experiment metric. Required.
    - name: categories
      value:
        - "{{ categories }}"
      description: |
        Categories associated with the experiment metric. Used for organizing and filtering metrics. Required.
    - name: desiredDirection
      value: "{{ desiredDirection }}"
      description: |
        The desired direction for changes in the metric value. Required. Known values are: "Increase", "Decrease", and "Neutral".
      valid_values: ['Increase', 'Decrease', 'Neutral']
    - name: definition
      description: |
        The metric definition specifying how the metric value is calculated from event data. Required.
      value:
        type: "{{ type }}"
    - name: If-Unmodified-Since
      value: "{{ If-Unmodified-Since }}"
      description: The request should only proceed if the entity was not modified after this time. Default value is None.
      description: The request should only proceed if the entity was not modified after this time. Default value is None.
    - name: If-Modified-Since
      value: "{{ If-Modified-Since }}"
      description: The request should only proceed if the entity was modified after this time. Default value is None.
      description: The request should only proceed if the entity was modified after this time. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_metric"
    values={[
        { label: 'create_or_update_metric', value: 'create_or_update_metric' }
    ]}
>
<TabItem value="create_or_update_metric">

Creates or updates an experiment metric.

```sql
REPLACE azure.onlineexperimentation_dataplane.metrics
SET 
lifecycle = '{{ lifecycle }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
categories = '{{ categories }}',
desiredDirection = '{{ desiredDirection }}',
definition = '{{ definition }}'
WHERE 
experiment_metric_id = '{{ experiment_metric_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND lifecycle = '{{ lifecycle }}' --required
AND displayName = '{{ displayName }}' --required
AND description = '{{ description }}' --required
AND categories = '{{ categories }}' --required
AND desiredDirection = '{{ desiredDirection }}' --required
AND definition = '{{ definition }}' --required
AND If-Unmodified-Since = '{{ If-Unmodified-Since}}'
AND If-Modified-Since = '{{ If-Modified-Since}}'
RETURNING
id,
categories,
definition,
description,
desiredDirection,
displayName,
eTag,
lastModifiedAt,
lifecycle;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_metric"
    values={[
        { label: 'delete_metric', value: 'delete_metric' }
    ]}
>
<TabItem value="delete_metric">

Deletes an experiment metric.

```sql
DELETE FROM azure.onlineexperimentation_dataplane.metrics
WHERE experiment_metric_id = '{{ experiment_metric_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
;
```
</TabItem>
</Tabs>
