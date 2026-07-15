--- 
title: glossary
hide_title: false
hide_table_of_contents: false
keywords:
  - glossary
  - purview_catalog
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

Creates, updates, deletes, gets or lists a <code>glossary</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="glossary" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_catalog.glossary" /></td></tr>
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
    <td><a href="#create_glossary"><CopyableCode code="create_glossary" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a glossary.</td>
</tr>
<tr>
    <td><a href="#update_glossary_category"><CopyableCode code="update_glossary_category" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-category_guid"><code>category_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the given glossary category by its GUID.</td>
</tr>
<tr>
    <td><a href="#update_glossary_term"><CopyableCode code="update_glossary_term" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Update the given glossary term by its GUID.</td>
</tr>
<tr>
    <td><a href="#update_glossary"><CopyableCode code="update_glossary" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the given glossary.</td>
</tr>
<tr>
    <td><a href="#delete_glossary_category"><CopyableCode code="delete_glossary_category" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-category_guid"><code>category_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a glossary category.</td>
</tr>
<tr>
    <td><a href="#delete_glossary_term"><CopyableCode code="delete_glossary_term" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a glossary term.</td>
</tr>
<tr>
    <td><a href="#delete_glossary"><CopyableCode code="delete_glossary" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a glossary.</td>
</tr>
<tr>
    <td><a href="#list_glossaries"><CopyableCode code="list_glossaries" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a>, <a href="#parameter-ignoreTermsAndCategories"><code>ignoreTermsAndCategories</code></a></td>
    <td>Get all glossaries registered with Atlas.</td>
</tr>
<tr>
    <td><a href="#list_related_categories"><CopyableCode code="list_related_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_guid"><code>category_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get all related categories (parent and children). Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.</td>
</tr>
<tr>
    <td><a href="#list_category_terms"><CopyableCode code="list_category_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_guid"><code>category_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get all terms associated with the specific category.</td>
</tr>
<tr>
    <td><a href="#list_related_terms"><CopyableCode code="list_related_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get all related terms for a specific term by its GUID. Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.</td>
</tr>
<tr>
    <td><a href="#list_glossary_categories"><CopyableCode code="list_glossary_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get the categories belonging to a specific glossary.</td>
</tr>
<tr>
    <td><a href="#list_glossary_categories_headers"><CopyableCode code="list_glossary_categories_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get the category headers belonging to a specific glossary.</td>
</tr>
<tr>
    <td><a href="#list_glossary_terms"><CopyableCode code="list_glossary_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get terms belonging to a specific glossary.</td>
</tr>
<tr>
    <td><a href="#list_glossary_term_headers"><CopyableCode code="list_glossary_term_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get term headers belonging to a specific glossary.</td>
</tr>
<tr>
    <td><a href="#list_terms_by_glossary_name"><CopyableCode code="list_terms_by_glossary_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_name"><code>glossary_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Get terms by glossary name.</td>
</tr>
<tr>
    <td><a href="#get_glossary_category"><CopyableCode code="get_glossary_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_guid"><code>category_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get specific glossary category by its GUID.</td>
</tr>
<tr>
    <td><a href="#get_glossary_term"><CopyableCode code="get_glossary_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Get a specific glossary term by its GUID.</td>
</tr>
<tr>
    <td><a href="#get_entities_assigned_with_term"><CopyableCode code="get_entities_assigned_with_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get all related objects assigned with the specified term.</td>
</tr>
<tr>
    <td><a href="#assign_term_to_entities"><CopyableCode code="assign_term_to_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Assign the given term to the provided list of related objects.</td>
</tr>
<tr>
    <td><a href="#remove_term_assignment_from_entities"><CopyableCode code="remove_term_assignment_from_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the term assignment for the given list of related objects.</td>
</tr>
<tr>
    <td><a href="#delete_term_assignment_from_entities"><CopyableCode code="delete_term_assignment_from_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the term assignment for the given list of related objects.</td>
</tr>
<tr>
    <td><a href="#get_glossary"><CopyableCode code="get_glossary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a specific Glossary by its GUID.</td>
</tr>
<tr>
    <td><a href="#get_detailed_glossary"><CopyableCode code="get_detailed_glossary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Get a specific glossary with detailed information.</td>
</tr>
<tr>
    <td><a href="#get_import_csv_operation_status"><CopyableCode code="get_import_csv_operation_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-operation_guid"><code>operation_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the status of import csv operation.</td>
</tr>
<tr>
    <td><a href="#create_glossary_categories"><CopyableCode code="create_glossary_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create glossary category in bulk.</td>
</tr>
<tr>
    <td><a href="#create_glossary_category"><CopyableCode code="create_glossary_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a glossary category.</td>
</tr>
<tr>
    <td><a href="#partial_update_glossary_category"><CopyableCode code="partial_update_glossary_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_guid"><code>category_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the glossary category partially.</td>
</tr>
<tr>
    <td><a href="#create_glossary_term"><CopyableCode code="create_glossary_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Create a glossary term.</td>
</tr>
<tr>
    <td><a href="#partial_update_glossary_term"><CopyableCode code="partial_update_glossary_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_guid"><code>term_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Update the glossary term partially.</td>
</tr>
<tr>
    <td><a href="#create_glossary_terms"><CopyableCode code="create_glossary_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Create glossary terms in bulk.</td>
</tr>
<tr>
    <td><a href="#partial_update_glossary"><CopyableCode code="partial_update_glossary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Update the glossary partially. Some properties such as qualifiedName are not allowed to be updated.</td>
</tr>
<tr>
    <td><a href="#export_glossary_terms_as_csv"><CopyableCode code="export_glossary_terms_as_csv" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_guid"><code>glossary_guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Export Glossary Terms as csv file.</td>
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
<tr id="parameter-category_guid">
    <td><CopyableCode code="category_guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the category.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-glossary_guid">
    <td><CopyableCode code="glossary_guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier for glossary.</td>
</tr>
<tr id="parameter-glossary_name">
    <td><CopyableCode code="glossary_name" /></td>
    <td><code>string</code></td>
    <td>The name of the glossary.</td>
</tr>
<tr id="parameter-operation_guid">
    <td><CopyableCode code="operation_guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier for async operation/job.</td>
</tr>
<tr id="parameter-term_guid">
    <td><CopyableCode code="term_guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier for glossary term.</td>
</tr>
<tr id="parameter-ignoreTermsAndCategories">
    <td><CopyableCode code="ignoreTermsAndCategories" /></td>
    <td><code>boolean</code></td>
    <td>Whether ignore terms and categories. Default value is False.</td>
</tr>
<tr id="parameter-includeTermHierarchy">
    <td><CopyableCode code="includeTermHierarchy" /></td>
    <td><code>boolean</code></td>
    <td>Whether include term hierarchy. Default value is False.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>The page size - by default there is no paging. Default value is None.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>The offset for pagination purpose. Default value is None.</td>
</tr>
<tr id="parameter-sort">
    <td><CopyableCode code="sort" /></td>
    <td><code>string</code></td>
    <td>The sort order, ASC (default) or DESC. Default value is "ASC".</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_glossary"
    values={[
        { label: 'create_glossary', value: 'create_glossary' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_glossary">

Create a glossary.

```sql
INSERT INTO azure.purview_catalog.glossary (
endpoint
)
SELECT 
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: glossary
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the glossary resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_glossary_category"
    values={[
        { label: 'update_glossary_category', value: 'update_glossary_category' },
        { label: 'update_glossary_term', value: 'update_glossary_term' },
        { label: 'update_glossary', value: 'update_glossary' }
    ]}
>
<TabItem value="update_glossary_category">

Update the given glossary category by its GUID.

```sql
UPDATE azure.purview_catalog.glossary
SET 
-- No updatable properties
WHERE 
category_guid = '{{ category_guid }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="update_glossary_term">

Update the given glossary term by its GUID.

```sql
UPDATE azure.purview_catalog.glossary
SET 
-- No updatable properties
WHERE 
term_guid = '{{ term_guid }}' --required
AND endpoint = '{{ endpoint }}' --required
AND includeTermHierarchy = {{ includeTermHierarchy}};
```
</TabItem>
<TabItem value="update_glossary">

Update the given glossary.

```sql
UPDATE azure.purview_catalog.glossary
SET 
-- No updatable properties
WHERE 
glossary_guid = '{{ glossary_guid }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_glossary_category"
    values={[
        { label: 'delete_glossary_category', value: 'delete_glossary_category' },
        { label: 'delete_glossary_term', value: 'delete_glossary_term' },
        { label: 'delete_glossary', value: 'delete_glossary' }
    ]}
>
<TabItem value="delete_glossary_category">

Delete a glossary category.

```sql
DELETE FROM azure.purview_catalog.glossary
WHERE category_guid = '{{ category_guid }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_glossary_term">

Delete a glossary term.

```sql
DELETE FROM azure.purview_catalog.glossary
WHERE term_guid = '{{ term_guid }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_glossary">

Delete a glossary.

```sql
DELETE FROM azure.purview_catalog.glossary
WHERE glossary_guid = '{{ glossary_guid }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_glossaries"
    values={[
        { label: 'list_glossaries', value: 'list_glossaries' },
        { label: 'list_related_categories', value: 'list_related_categories' },
        { label: 'list_category_terms', value: 'list_category_terms' },
        { label: 'list_related_terms', value: 'list_related_terms' },
        { label: 'list_glossary_categories', value: 'list_glossary_categories' },
        { label: 'list_glossary_categories_headers', value: 'list_glossary_categories_headers' },
        { label: 'list_glossary_terms', value: 'list_glossary_terms' },
        { label: 'list_glossary_term_headers', value: 'list_glossary_term_headers' },
        { label: 'list_terms_by_glossary_name', value: 'list_terms_by_glossary_name' },
        { label: 'get_glossary_category', value: 'get_glossary_category' },
        { label: 'get_glossary_term', value: 'get_glossary_term' },
        { label: 'get_entities_assigned_with_term', value: 'get_entities_assigned_with_term' },
        { label: 'assign_term_to_entities', value: 'assign_term_to_entities' },
        { label: 'remove_term_assignment_from_entities', value: 'remove_term_assignment_from_entities' },
        { label: 'delete_term_assignment_from_entities', value: 'delete_term_assignment_from_entities' },
        { label: 'get_glossary', value: 'get_glossary' },
        { label: 'get_detailed_glossary', value: 'get_detailed_glossary' },
        { label: 'get_import_csv_operation_status', value: 'get_import_csv_operation_status' },
        { label: 'create_glossary_categories', value: 'create_glossary_categories' },
        { label: 'create_glossary_category', value: 'create_glossary_category' },
        { label: 'partial_update_glossary_category', value: 'partial_update_glossary_category' },
        { label: 'create_glossary_term', value: 'create_glossary_term' },
        { label: 'partial_update_glossary_term', value: 'partial_update_glossary_term' },
        { label: 'create_glossary_terms', value: 'create_glossary_terms' },
        { label: 'partial_update_glossary', value: 'partial_update_glossary' },
        { label: 'export_glossary_terms_as_csv', value: 'export_glossary_terms_as_csv' }
    ]}
>
<TabItem value="list_glossaries">

Get all glossaries registered with Atlas.

```sql
EXEC azure.purview_catalog.glossary.list_glossaries 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}', 
@ignoreTermsAndCategories={{ ignoreTermsAndCategories }}
;
```
</TabItem>
<TabItem value="list_related_categories">

Get all related categories (parent and children). Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.

```sql
EXEC azure.purview_catalog.glossary.list_related_categories 
@category_guid='{{ category_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="list_category_terms">

Get all terms associated with the specific category.

```sql
EXEC azure.purview_catalog.glossary.list_category_terms 
@category_guid='{{ category_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="list_related_terms">

Get all related terms for a specific term by its GUID. Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.

```sql
EXEC azure.purview_catalog.glossary.list_related_terms 
@term_guid='{{ term_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="list_glossary_categories">

Get the categories belonging to a specific glossary.

```sql
EXEC azure.purview_catalog.glossary.list_glossary_categories 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="list_glossary_categories_headers">

Get the category headers belonging to a specific glossary.

```sql
EXEC azure.purview_catalog.glossary.list_glossary_categories_headers 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="list_glossary_terms">

Get terms belonging to a specific glossary.

```sql
EXEC azure.purview_catalog.glossary.list_glossary_terms 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="list_glossary_term_headers">

Get term headers belonging to a specific glossary.

```sql
EXEC azure.purview_catalog.glossary.list_glossary_term_headers 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="list_terms_by_glossary_name">

Get terms by glossary name.

```sql
EXEC azure.purview_catalog.glossary.list_terms_by_glossary_name 
@glossary_name='{{ glossary_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="get_glossary_category">

Get specific glossary category by its GUID.

```sql
EXEC azure.purview_catalog.glossary.get_glossary_category 
@category_guid='{{ category_guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_glossary_term">

Get a specific glossary term by its GUID.

```sql
EXEC azure.purview_catalog.glossary.get_glossary_term 
@term_guid='{{ term_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="get_entities_assigned_with_term">

Get all related objects assigned with the specified term.

```sql
EXEC azure.purview_catalog.glossary.get_entities_assigned_with_term 
@term_guid='{{ term_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="assign_term_to_entities">

Assign the given term to the provided list of related objects.

```sql
EXEC azure.purview_catalog.glossary.assign_term_to_entities 
@term_guid='{{ term_guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="remove_term_assignment_from_entities">

Delete the term assignment for the given list of related objects.

```sql
EXEC azure.purview_catalog.glossary.remove_term_assignment_from_entities 
@term_guid='{{ term_guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_term_assignment_from_entities">

Delete the term assignment for the given list of related objects.

```sql
EXEC azure.purview_catalog.glossary.delete_term_assignment_from_entities 
@term_guid='{{ term_guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_glossary">

Get a specific Glossary by its GUID.

```sql
EXEC azure.purview_catalog.glossary.get_glossary 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_detailed_glossary">

Get a specific glossary with detailed information.

```sql
EXEC azure.purview_catalog.glossary.get_detailed_glossary 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="get_import_csv_operation_status">

Get the status of import csv operation.

```sql
EXEC azure.purview_catalog.glossary.get_import_csv_operation_status 
@operation_guid='{{ operation_guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_glossary_categories">

Create glossary category in bulk.

```sql
EXEC azure.purview_catalog.glossary.create_glossary_categories 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_glossary_category">

Create a glossary category.

```sql
EXEC azure.purview_catalog.glossary.create_glossary_category 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="partial_update_glossary_category">

Update the glossary category partially.

```sql
EXEC azure.purview_catalog.glossary.partial_update_glossary_category 
@category_guid='{{ category_guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_glossary_term">

Create a glossary term.

```sql
EXEC azure.purview_catalog.glossary.create_glossary_term 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="partial_update_glossary_term">

Update the glossary term partially.

```sql
EXEC azure.purview_catalog.glossary.partial_update_glossary_term 
@term_guid='{{ term_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="create_glossary_terms">

Create glossary terms in bulk.

```sql
EXEC azure.purview_catalog.glossary.create_glossary_terms 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="partial_update_glossary">

Update the glossary partially. Some properties such as qualifiedName are not allowed to be updated.

```sql
EXEC azure.purview_catalog.glossary.partial_update_glossary 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="export_glossary_terms_as_csv">

Export Glossary Terms as csv file.

```sql
EXEC azure.purview_catalog.glossary.export_glossary_terms_as_csv 
@glossary_guid='{{ glossary_guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
</Tabs>
