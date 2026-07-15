--- 
title: relationship
hide_title: false
hide_table_of_contents: false
keywords:
  - relationship
  - purview_data_map
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

Creates, updates, deletes, gets or lists a <code>relationship</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="relationship" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_data_map.relationship" /></td></tr>
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
    <td><CopyableCode code="referredEntities" /></td>
    <td><code>object</code></td>
    <td>The referred entity header.</td>
</tr>
<tr>
    <td><CopyableCode code="relationship" /></td>
    <td><code>object</code></td>
    <td>Atlas relationship instance.</td>
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
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-extendedInfo"><code>extendedInfo</code></a></td>
    <td>Get relationship information between entities by its GUID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new relationship between entities.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update an existing relationship between entities.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a relationship between entities by its GUID.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-guid">
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the relationship. Required.</td>
</tr>
<tr id="parameter-extendedInfo">
    <td><CopyableCode code="extendedInfo" /></td>
    <td><code>boolean</code></td>
    <td>Limits whether includes extended information. Default value is None.</td>
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

Get relationship information between entities by its GUID.

```sql
SELECT
referredEntities,
relationship
FROM azure.purview_data_map.relationship
WHERE guid = '{{ guid }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND extendedInfo = '{{ extendedInfo }}'
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

Create a new relationship between entities.

```sql
INSERT INTO azure.purview_data_map.relationship (
attributes,
typeName,
lastModifiedTS,
createTime,
createdBy,
end1,
end2,
guid,
homeId,
label,
provenanceType,
status,
updateTime,
updatedBy,
version,
endpoint
)
SELECT 
'{{ attributes }}',
'{{ typeName }}',
'{{ lastModifiedTS }}',
{{ createTime }},
'{{ createdBy }}',
'{{ end1 }}',
'{{ end2 }}',
'{{ guid }}',
'{{ homeId }}',
'{{ label }}',
{{ provenanceType }},
'{{ status }}',
{{ updateTime }},
'{{ updatedBy }}',
{{ version }},
'{{ endpoint }}'
RETURNING
attributes,
createTime,
createdBy,
end1,
end2,
guid,
homeId,
label,
lastModifiedTS,
provenanceType,
status,
typeName,
updateTime,
updatedBy,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: relationship
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the relationship resource.
    - name: attributes
      value: "{{ attributes }}"
      description: |
        The attributes of the struct.
    - name: typeName
      value: "{{ typeName }}"
      description: |
        The name of the type.
    - name: lastModifiedTS
      value: "{{ lastModifiedTS }}"
      description: |
        ETag for concurrency control.
    - name: createTime
      value: {{ createTime }}
      description: |
        The created time of the record.
    - name: createdBy
      value: "{{ createdBy }}"
      description: |
        The user who created the record.
    - name: end1
      description: |
        Reference to an object-instance of a type - like entity.
      value:
        guid: "{{ guid }}"
        typeName: "{{ typeName }}"
        uniqueAttributes: "{{ uniqueAttributes }}"
    - name: end2
      description: |
        Reference to an object-instance of a type - like entity.
      value:
        guid: "{{ guid }}"
        typeName: "{{ typeName }}"
        uniqueAttributes: "{{ uniqueAttributes }}"
    - name: guid
      value: "{{ guid }}"
      description: |
        The GUID of the relationship.
    - name: homeId
      value: "{{ homeId }}"
      description: |
        The home ID of the relationship.
    - name: label
      value: "{{ label }}"
      description: |
        The label of the relationship.
    - name: provenanceType
      value: {{ provenanceType }}
      description: |
        Used to record the provenance of an instance of an entity or relationship.
    - name: status
      value: "{{ status }}"
      description: |
        The enum of relationship status. Known values are: "ACTIVE" and "DELETED".
      valid_values: ['ACTIVE', 'DELETED']
    - name: updateTime
      value: {{ updateTime }}
      description: |
        The update time of the record.
    - name: updatedBy
      value: "{{ updatedBy }}"
      description: |
        The user who updated the record.
    - name: version
      value: {{ version }}
      description: |
        The version of the relationship.
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

Update an existing relationship between entities.

```sql
UPDATE azure.purview_data_map.relationship
SET 
attributes = '{{ attributes }}',
typeName = '{{ typeName }}',
lastModifiedTS = '{{ lastModifiedTS }}',
createTime = {{ createTime }},
createdBy = '{{ createdBy }}',
end1 = '{{ end1 }}',
end2 = '{{ end2 }}',
guid = '{{ guid }}',
homeId = '{{ homeId }}',
label = '{{ label }}',
provenanceType = {{ provenanceType }},
status = '{{ status }}',
updateTime = {{ updateTime }},
updatedBy = '{{ updatedBy }}',
version = {{ version }}
WHERE 
endpoint = '{{ endpoint }}' --required
RETURNING
attributes,
createTime,
createdBy,
end1,
end2,
guid,
homeId,
label,
lastModifiedTS,
provenanceType,
status,
typeName,
updateTime,
updatedBy,
version;
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

Delete a relationship between entities by its GUID.

```sql
DELETE FROM azure.purview_data_map.relationship
WHERE guid = '{{ guid }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
