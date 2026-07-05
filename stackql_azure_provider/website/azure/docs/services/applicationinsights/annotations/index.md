--- 
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
  - applicationinsights
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

Creates, updates, deletes, gets or lists an <code>annotations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="annotations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.annotations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
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
    <td><CopyableCode code="AnnotationName" /></td>
    <td><code>string</code></td>
    <td>Name of annotation.</td>
</tr>
<tr>
    <td><CopyableCode code="Category" /></td>
    <td><code>string</code></td>
    <td>Category of annotation, free form.</td>
</tr>
<tr>
    <td><CopyableCode code="EventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when event occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="Id" /></td>
    <td><code>string</code></td>
    <td>Unique Id for annotation.</td>
</tr>
<tr>
    <td><CopyableCode code="Properties" /></td>
    <td><code>string</code></td>
    <td>Serialized JSON object for detailed properties.</td>
</tr>
<tr>
    <td><CopyableCode code="RelatedAnnotation" /></td>
    <td><code>string</code></td>
    <td>Related parent annotation if any.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="AnnotationName" /></td>
    <td><code>string</code></td>
    <td>Name of annotation.</td>
</tr>
<tr>
    <td><CopyableCode code="Category" /></td>
    <td><code>string</code></td>
    <td>Category of annotation, free form.</td>
</tr>
<tr>
    <td><CopyableCode code="EventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when event occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="Id" /></td>
    <td><code>string</code></td>
    <td>Unique Id for annotation.</td>
</tr>
<tr>
    <td><CopyableCode code="Properties" /></td>
    <td><code>string</code></td>
    <td>Serialized JSON object for detailed properties.</td>
</tr>
<tr>
    <td><CopyableCode code="RelatedAnnotation" /></td>
    <td><code>string</code></td>
    <td>Related parent annotation if any.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-start"><code>start</code></a>, <a href="#parameter-end"><code>end</code></a></td>
    <td></td>
    <td>Gets the list of annotations for a component for given time range.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-annotation_id"><code>annotation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the annotation for given id.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create an Annotation of an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-annotation_id"><code>annotation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an Annotation of an Application Insights component.</td>
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
<tr id="parameter-annotation_id">
    <td><CopyableCode code="annotation_id" /></td>
    <td><code>string</code></td>
    <td>The unique annotation ID. This is unique within a Application Insights component. Required.</td>
</tr>
<tr id="parameter-end">
    <td><CopyableCode code="end" /></td>
    <td><code>string</code></td>
    <td>The end time to query for annotations. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component resource. Required.</td>
</tr>
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string</code></td>
    <td>The start time to query from for annotations, cannot be older than 90 days from current date. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

Gets the list of annotations for a component for given time range.

```sql
SELECT
AnnotationName,
Category,
EventTime,
Id,
Properties,
RelatedAnnotation
FROM azure.applicationinsights.annotations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND start = '{{ start }}' -- required
AND end = '{{ end }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the annotation for given id.

```sql
SELECT
AnnotationName,
Category,
EventTime,
Id,
Properties,
RelatedAnnotation
FROM azure.applicationinsights.annotations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND annotation_id = '{{ annotation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create an Annotation of an Application Insights component.

```sql
INSERT INTO azure.applicationinsights.annotations (
AnnotationName,
Category,
EventTime,
Id,
Properties,
RelatedAnnotation,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ AnnotationName }}',
'{{ Category }}',
'{{ EventTime }}',
'{{ Id }}',
'{{ Properties }}',
'{{ RelatedAnnotation }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
AnnotationName,
Category,
EventTime,
Id,
Properties,
RelatedAnnotation
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: annotations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the annotations resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the annotations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the annotations resource.
    - name: AnnotationName
      value: "{{ AnnotationName }}"
      description: |
        Name of annotation.
    - name: Category
      value: "{{ Category }}"
      description: |
        Category of annotation, free form.
    - name: EventTime
      value: "{{ EventTime }}"
      description: |
        Time when event occurred.
    - name: Id
      value: "{{ Id }}"
      description: |
        Unique Id for annotation.
    - name: Properties
      value: "{{ Properties }}"
      description: |
        Serialized JSON object for detailed properties.
    - name: RelatedAnnotation
      value: "{{ RelatedAnnotation }}"
      description: |
        Related parent annotation if any.
`}</CodeBlock>

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

Delete an Annotation of an Application Insights component.

```sql
DELETE FROM azure.applicationinsights.annotations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND annotation_id = '{{ annotation_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
