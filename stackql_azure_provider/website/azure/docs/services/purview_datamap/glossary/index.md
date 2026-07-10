--- 
title: glossary
hide_title: false
hide_table_of_contents: false
keywords:
  - glossary
  - purview_datamap
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_datamap.glossary" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_category', value: 'get_category' },
        { label: 'get_term', value: 'get_term' }
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the glossary object.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>An array of categories.</td>
</tr>
<tr>
    <td><CopyableCode code="classifications" /></td>
    <td><code>array</code></td>
    <td>An array of classifications.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>integer</code></td>
    <td>The created time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user who created the record.</td>
</tr>
<tr>
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>The language of the glossary.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTS" /></td>
    <td><code>string</code></td>
    <td>ETag for concurrency control.</td>
</tr>
<tr>
    <td><CopyableCode code="longDescription" /></td>
    <td><code>string</code></td>
    <td>The long version description.</td>
</tr>
<tr>
    <td><CopyableCode code="qualifiedName" /></td>
    <td><code>string</code></td>
    <td>The qualified name of the glossary object.</td>
</tr>
<tr>
    <td><CopyableCode code="shortDescription" /></td>
    <td><code>string</code></td>
    <td>The short version of description.</td>
</tr>
<tr>
    <td><CopyableCode code="terms" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers.</td>
</tr>
<tr>
    <td><CopyableCode code="updateTime" /></td>
    <td><code>integer</code></td>
    <td>The update time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>The user who updated the record.</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>string</code></td>
    <td>The usage of the glossary.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_category">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the glossary object.</td>
</tr>
<tr>
    <td><CopyableCode code="anchor" /></td>
    <td><code>object</code></td>
    <td>The glossary header with basic information.</td>
</tr>
<tr>
    <td><CopyableCode code="childrenCategories" /></td>
    <td><code>array</code></td>
    <td>An array of children categories.</td>
</tr>
<tr>
    <td><CopyableCode code="classifications" /></td>
    <td><code>array</code></td>
    <td>An array of classifications.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>integer</code></td>
    <td>The created time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user who created the record.</td>
</tr>
<tr>
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTS" /></td>
    <td><code>string</code></td>
    <td>ETag for concurrency control.</td>
</tr>
<tr>
    <td><CopyableCode code="longDescription" /></td>
    <td><code>string</code></td>
    <td>The long version description.</td>
</tr>
<tr>
    <td><CopyableCode code="parentCategory" /></td>
    <td><code>object</code></td>
    <td>The header of the related category.</td>
</tr>
<tr>
    <td><CopyableCode code="qualifiedName" /></td>
    <td><code>string</code></td>
    <td>The qualified name of the glossary object.</td>
</tr>
<tr>
    <td><CopyableCode code="shortDescription" /></td>
    <td><code>string</code></td>
    <td>The short version of description.</td>
</tr>
<tr>
    <td><CopyableCode code="terms" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers.</td>
</tr>
<tr>
    <td><CopyableCode code="updateTime" /></td>
    <td><code>integer</code></td>
    <td>The update time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>The user who updated the record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_term">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the glossary object.</td>
</tr>
<tr>
    <td><CopyableCode code="abbreviation" /></td>
    <td><code>string</code></td>
    <td>The abbreviation of the term.</td>
</tr>
<tr>
    <td><CopyableCode code="anchor" /></td>
    <td><code>object</code></td>
    <td>The glossary header with basic information.</td>
</tr>
<tr>
    <td><CopyableCode code="antonyms" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers as antonyms.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedEntities" /></td>
    <td><code>array</code></td>
    <td>An array of related object IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The custom attributes of the term, which is map&gt;. The key of the first layer map is term template name.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>An array of term categorization headers.</td>
</tr>
<tr>
    <td><CopyableCode code="classifications" /></td>
    <td><code>array</code></td>
    <td>An array of classifications.</td>
</tr>
<tr>
    <td><CopyableCode code="classifies" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers.</td>
</tr>
<tr>
    <td><CopyableCode code="contacts" /></td>
    <td><code>object</code></td>
    <td>The dictionary of contacts for terms. Key could be Expert or Steward.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>integer</code></td>
    <td>The created time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user who created the record.</td>
</tr>
<tr>
    <td><CopyableCode code="examples" /></td>
    <td><code>array</code></td>
    <td>An array of examples.</td>
</tr>
<tr>
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="hierarchyInfo" /></td>
    <td><code>array</code></td>
    <td>The hierarchy information of the term.</td>
</tr>
<tr>
    <td><CopyableCode code="isA" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers indicating the is-a relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTS" /></td>
    <td><code>string</code></td>
    <td>ETag for concurrency control.</td>
</tr>
<tr>
    <td><CopyableCode code="longDescription" /></td>
    <td><code>string</code></td>
    <td>The long version description.</td>
</tr>
<tr>
    <td><CopyableCode code="nickName" /></td>
    <td><code>string</code></td>
    <td>The nick name of the term.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredTerms" /></td>
    <td><code>array</code></td>
    <td>An array of preferred related term headers.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredToTerms" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers that are preferred to.</td>
</tr>
<tr>
    <td><CopyableCode code="qualifiedName" /></td>
    <td><code>string</code></td>
    <td>The qualified name of the glossary object.</td>
</tr>
<tr>
    <td><CopyableCode code="replacedBy" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers that are replaced by.</td>
</tr>
<tr>
    <td><CopyableCode code="replacementTerms" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers for replacement.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>An array of resource link for term.</td>
</tr>
<tr>
    <td><CopyableCode code="seeAlso" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers for see also.</td>
</tr>
<tr>
    <td><CopyableCode code="shortDescription" /></td>
    <td><code>string</code></td>
    <td>The short version of description.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the AtlasGlossaryTerm. Known values are: "Draft", "Approved", "Alert", and "Expired". (Draft, Approved, Alert, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="synonyms" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers as synonyms.</td>
</tr>
<tr>
    <td><CopyableCode code="templateName" /></td>
    <td><code>array</code></td>
    <td>The name of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="translatedTerms" /></td>
    <td><code>array</code></td>
    <td>An array of translated related term headers.</td>
</tr>
<tr>
    <td><CopyableCode code="translationTerms" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers for translation.</td>
</tr>
<tr>
    <td><CopyableCode code="updateTime" /></td>
    <td><code>integer</code></td>
    <td>The update time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>The user who updated the record.</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>string</code></td>
    <td>The usage of the term.</td>
</tr>
<tr>
    <td><CopyableCode code="validValues" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers as valid values.</td>
</tr>
<tr>
    <td><CopyableCode code="validValuesFor" /></td>
    <td><code>array</code></td>
    <td>An array of related term headers as valid values for other records.</td>
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
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a specific Glossary by its GUID.</td>
</tr>
<tr>
    <td><a href="#get_category"><CopyableCode code="get_category" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-category_id"><code>category_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get specific glossary category by its GUID.</td>
</tr>
<tr>
    <td><a href="#get_term"><CopyableCode code="get_term" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a specific glossary term by its GUID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a glossary.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ignoreTermsAndCategories"><code>ignoreTermsAndCategories</code></a></td>
    <td>Update the given glossary.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a glossary. Will delete underlying terms/categories together. Recommend separate delete terms and categories.</td>
</tr>
<tr>
    <td><a href="#update_category"><CopyableCode code="update_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_id"><code>category_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the given glossary category by its GUID.</td>
</tr>
<tr>
    <td><a href="#delete_category"><CopyableCode code="delete_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_id"><code>category_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a glossary category.</td>
</tr>
<tr>
    <td><a href="#get_related_categories"><CopyableCode code="get_related_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_id"><code>category_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get all related categories (parent and children). Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.</td>
</tr>
<tr>
    <td><a href="#get_category_terms"><CopyableCode code="get_category_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_id"><code>category_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get all terms associated with the specific category.</td>
</tr>
<tr>
    <td><a href="#update_term"><CopyableCode code="update_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Update the given glossary term by its GUID.</td>
</tr>
<tr>
    <td><a href="#get_entities_assigned_with_term"><CopyableCode code="get_entities_assigned_with_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>List all related objects assigned with the specified term. Recommend using limit/offset to get pagination result.</td>
</tr>
<tr>
    <td><a href="#assign_term_to_entities"><CopyableCode code="assign_term_to_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Assign the given term to the provided list of related objects. Recommend using small batches with multiple API calls. `Entities Create Or Update operation `_ is an alternative to assign a term to multiple entities.</td>
</tr>
<tr>
    <td><a href="#delete_term_assignment_from_entities"><CopyableCode code="delete_term_assignment_from_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the term assignment for the given list of related objects.</td>
</tr>
<tr>
    <td><a href="#get_related_terms"><CopyableCode code="get_related_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get all related terms for a specific term by its GUID. Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.</td>
</tr>
<tr>
    <td><a href="#get_categories"><CopyableCode code="get_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get the categories belonging to a specific glossary. Recommend using limit/offset to get pagination result.</td>
</tr>
<tr>
    <td><a href="#get_categories_headers"><CopyableCode code="get_categories_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get the category headers belonging to a specific glossary. Recommend using limit/offset to get pagination result.</td>
</tr>
<tr>
    <td><a href="#get_detailed"><CopyableCode code="get_detailed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a specific glossary with detailed information. This API is not recommend. Recommend to fetch terms/categories details separately using GET /datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/terms and GET /datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/categories.</td>
</tr>
<tr>
    <td><a href="#get_terms"><CopyableCode code="get_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get terms belonging to a specific glossary. Recommend using limit/offset to get pagination result.</td>
</tr>
<tr>
    <td><a href="#get_term_headers"><CopyableCode code="get_term_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a></td>
    <td>Get term headers belonging to a specific glossary. Recommend using limit/offset to get pagination result.</td>
</tr>
<tr>
    <td><a href="#batch_get"><CopyableCode code="batch_get" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-sort"><code>sort</code></a>, <a href="#parameter-ignoreTermsAndCategories"><code>ignoreTermsAndCategories</code></a></td>
    <td>Get all glossaries. Recommend using limit/offset to get pagination result. Recommend using 'ignoreTermsAndCategories=true' and fetch terms/categories separately using 'GET /datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/terms' and 'GET '/datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/categories'.</td>
</tr>
<tr>
    <td><a href="#create_categories"><CopyableCode code="create_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create glossary category in bulk.</td>
</tr>
<tr>
    <td><a href="#create_category"><CopyableCode code="create_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a glossary category.</td>
</tr>
<tr>
    <td><a href="#partial_update_category"><CopyableCode code="partial_update_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-category_id"><code>category_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the glossary category partially. So far we only supports partial updating shortDescription and longDescription for category.</td>
</tr>
<tr>
    <td><a href="#create_term"><CopyableCode code="create_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Create a glossary term.</td>
</tr>
<tr>
    <td><a href="#delete_term"><CopyableCode code="delete_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a glossary term.</td>
</tr>
<tr>
    <td><a href="#partial_update_term"><CopyableCode code="partial_update_term" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-term_id"><code>term_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Update the glossary term partially. So far we only supports partial updating shortDescription, longDescription, abbreviation, usage and status for term.</td>
</tr>
<tr>
    <td><a href="#create_terms"><CopyableCode code="create_terms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermHierarchy"><code>includeTermHierarchy</code></a></td>
    <td>Create glossary terms in bulk.</td>
</tr>
<tr>
    <td><a href="#partial_update"><CopyableCode code="partial_update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-glossary_id"><code>glossary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ignoreTermsAndCategories"><code>ignoreTermsAndCategories</code></a></td>
    <td>Update the glossary partially. Some properties such as qualifiedName are not allowed to be updated. So far we only supports partial updating shortDescription, longDescription, language and usage for glossary. Recommend using 'ignoreTermsAndCategories=true' to reduce response body size.</td>
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
<tr id="parameter-category_id">
    <td><CopyableCode code="category_id" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the category. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-glossary_id">
    <td><CopyableCode code="glossary_id" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier for glossary. Required.</td>
</tr>
<tr id="parameter-term_id">
    <td><CopyableCode code="term_id" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier for glossary term. Required.</td>
</tr>
<tr id="parameter-ignoreTermsAndCategories">
    <td><CopyableCode code="ignoreTermsAndCategories" /></td>
    <td><code>boolean</code></td>
    <td>Whether ignore terms and categories. Default value is None.</td>
</tr>
<tr id="parameter-includeTermHierarchy">
    <td><CopyableCode code="includeTermHierarchy" /></td>
    <td><code>boolean</code></td>
    <td>Whether include term hierarchy. Default value is None.</td>
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
    <td>The sort order, ASC (default) or DESC. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_category', value: 'get_category' },
        { label: 'get_term', value: 'get_term' }
    ]}
>
<TabItem value="get">

Get a specific Glossary by its GUID.

```sql
SELECT
name,
categories,
classifications,
createTime,
createdBy,
guid,
language,
lastModifiedTS,
longDescription,
qualifiedName,
shortDescription,
terms,
updateTime,
updatedBy,
usage
FROM azure.purview_datamap.glossary
WHERE glossary_id = '{{ glossary_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_category">

Get specific glossary category by its GUID.

```sql
SELECT
name,
anchor,
childrenCategories,
classifications,
createTime,
createdBy,
guid,
lastModifiedTS,
longDescription,
parentCategory,
qualifiedName,
shortDescription,
terms,
updateTime,
updatedBy
FROM azure.purview_datamap.glossary
WHERE category_id = '{{ category_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_term">

Get a specific glossary term by its GUID.

```sql
SELECT
name,
abbreviation,
anchor,
antonyms,
assignedEntities,
attributes,
categories,
classifications,
classifies,
contacts,
createTime,
createdBy,
examples,
guid,
hierarchyInfo,
isA,
lastModifiedTS,
longDescription,
nickName,
preferredTerms,
preferredToTerms,
qualifiedName,
replacedBy,
replacementTerms,
resources,
seeAlso,
shortDescription,
status,
synonyms,
templateName,
translatedTerms,
translationTerms,
updateTime,
updatedBy,
usage,
validValues,
validValuesFor
FROM azure.purview_datamap.glossary
WHERE term_id = '{{ term_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
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

Create a glossary.

```sql
INSERT INTO azure.purview_datamap.glossary (
guid,
classifications,
longDescription,
name,
qualifiedName,
shortDescription,
lastModifiedTS,
createTime,
createdBy,
updateTime,
updatedBy,
categories,
language,
terms,
usage,
endpoint
)
SELECT 
'{{ guid }}',
'{{ classifications }}',
'{{ longDescription }}',
'{{ name }}',
'{{ qualifiedName }}',
'{{ shortDescription }}',
'{{ lastModifiedTS }}',
{{ createTime }},
'{{ createdBy }}',
{{ updateTime }},
'{{ updatedBy }}',
'{{ categories }}',
'{{ language }}',
'{{ terms }}',
'{{ usage }}',
'{{ endpoint }}'
RETURNING
name,
categories,
classifications,
createTime,
createdBy,
guid,
language,
lastModifiedTS,
longDescription,
qualifiedName,
shortDescription,
terms,
updateTime,
updatedBy,
usage
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
    - name: guid
      value: "{{ guid }}"
      description: |
        The GUID of the object.
    - name: classifications
      description: |
        An array of classifications.
      value:
        - attributes: "{{ attributes }}"
          typeName: "{{ typeName }}"
          lastModifiedTS: "{{ lastModifiedTS }}"
          entityGuid: "{{ entityGuid }}"
          entityStatus: "{{ entityStatus }}"
          removePropagationsOnEntityDelete: {{ removePropagationsOnEntityDelete }}
          validityPeriods: "{{ validityPeriods }}"
    - name: longDescription
      value: "{{ longDescription }}"
      description: |
        The long version description.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the glossary object.
    - name: qualifiedName
      value: "{{ qualifiedName }}"
      description: |
        The qualified name of the glossary object.
    - name: shortDescription
      value: "{{ shortDescription }}"
      description: |
        The short version of description.
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
    - name: updateTime
      value: {{ updateTime }}
      description: |
        The update time of the record.
    - name: updatedBy
      value: "{{ updatedBy }}"
      description: |
        The user who updated the record.
    - name: categories
      description: |
        An array of categories.
      value:
        - categoryGuid: "{{ categoryGuid }}"
          description: "{{ description }}"
          displayText: "{{ displayText }}"
          parentCategoryGuid: "{{ parentCategoryGuid }}"
          relationGuid: "{{ relationGuid }}"
    - name: language
      value: "{{ language }}"
      description: |
        The language of the glossary.
    - name: terms
      description: |
        An array of related term headers.
      value:
        - description: "{{ description }}"
          displayText: "{{ displayText }}"
          expression: "{{ expression }}"
          relationGuid: "{{ relationGuid }}"
          status: "{{ status }}"
          steward: "{{ steward }}"
          termGuid: "{{ termGuid }}"
    - name: usage
      value: "{{ usage }}"
      description: |
        The usage of the glossary.
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

Update the given glossary.

```sql
UPDATE azure.purview_datamap.glossary
SET 
guid = '{{ guid }}',
classifications = '{{ classifications }}',
longDescription = '{{ longDescription }}',
name = '{{ name }}',
qualifiedName = '{{ qualifiedName }}',
shortDescription = '{{ shortDescription }}',
lastModifiedTS = '{{ lastModifiedTS }}',
createTime = {{ createTime }},
createdBy = '{{ createdBy }}',
updateTime = {{ updateTime }},
updatedBy = '{{ updatedBy }}',
categories = '{{ categories }}',
language = '{{ language }}',
terms = '{{ terms }}',
usage = '{{ usage }}'
WHERE 
glossary_id = '{{ glossary_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ignoreTermsAndCategories = {{ ignoreTermsAndCategories}}
RETURNING
name,
categories,
classifications,
createTime,
createdBy,
guid,
language,
lastModifiedTS,
longDescription,
qualifiedName,
shortDescription,
terms,
updateTime,
updatedBy,
usage;
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

Delete a glossary. Will delete underlying terms/categories together. Recommend separate delete terms and categories.

```sql
DELETE FROM azure.purview_datamap.glossary
WHERE glossary_id = '{{ glossary_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_category"
    values={[
        { label: 'update_category', value: 'update_category' },
        { label: 'delete_category', value: 'delete_category' },
        { label: 'get_related_categories', value: 'get_related_categories' },
        { label: 'get_category_terms', value: 'get_category_terms' },
        { label: 'update_term', value: 'update_term' },
        { label: 'get_entities_assigned_with_term', value: 'get_entities_assigned_with_term' },
        { label: 'assign_term_to_entities', value: 'assign_term_to_entities' },
        { label: 'delete_term_assignment_from_entities', value: 'delete_term_assignment_from_entities' },
        { label: 'get_related_terms', value: 'get_related_terms' },
        { label: 'get_categories', value: 'get_categories' },
        { label: 'get_categories_headers', value: 'get_categories_headers' },
        { label: 'get_detailed', value: 'get_detailed' },
        { label: 'get_terms', value: 'get_terms' },
        { label: 'get_term_headers', value: 'get_term_headers' },
        { label: 'batch_get', value: 'batch_get' },
        { label: 'create_categories', value: 'create_categories' },
        { label: 'create_category', value: 'create_category' },
        { label: 'partial_update_category', value: 'partial_update_category' },
        { label: 'create_term', value: 'create_term' },
        { label: 'delete_term', value: 'delete_term' },
        { label: 'partial_update_term', value: 'partial_update_term' },
        { label: 'create_terms', value: 'create_terms' },
        { label: 'partial_update', value: 'partial_update' }
    ]}
>
<TabItem value="update_category">

Update the given glossary category by its GUID.

```sql
EXEC azure.purview_datamap.glossary.update_category 
@category_id='{{ category_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"guid": "{{ guid }}", 
"classifications": "{{ classifications }}", 
"longDescription": "{{ longDescription }}", 
"name": "{{ name }}", 
"qualifiedName": "{{ qualifiedName }}", 
"shortDescription": "{{ shortDescription }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"createTime": {{ createTime }}, 
"createdBy": "{{ createdBy }}", 
"updateTime": {{ updateTime }}, 
"updatedBy": "{{ updatedBy }}", 
"anchor": "{{ anchor }}", 
"childrenCategories": "{{ childrenCategories }}", 
"parentCategory": "{{ parentCategory }}", 
"terms": "{{ terms }}"
}'
;
```
</TabItem>
<TabItem value="delete_category">

Delete a glossary category.

```sql
EXEC azure.purview_datamap.glossary.delete_category 
@category_id='{{ category_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_related_categories">

Get all related categories (parent and children). Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.

```sql
EXEC azure.purview_datamap.glossary.get_related_categories 
@category_id='{{ category_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="get_category_terms">

Get all terms associated with the specific category.

```sql
EXEC azure.purview_datamap.glossary.get_category_terms 
@category_id='{{ category_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="update_term">

Update the given glossary term by its GUID.

```sql
EXEC azure.purview_datamap.glossary.update_term 
@term_id='{{ term_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }} 
@@json=
'{
"guid": "{{ guid }}", 
"classifications": "{{ classifications }}", 
"longDescription": "{{ longDescription }}", 
"name": "{{ name }}", 
"qualifiedName": "{{ qualifiedName }}", 
"shortDescription": "{{ shortDescription }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"createTime": {{ createTime }}, 
"createdBy": "{{ createdBy }}", 
"updateTime": {{ updateTime }}, 
"updatedBy": "{{ updatedBy }}", 
"abbreviation": "{{ abbreviation }}", 
"templateName": "{{ templateName }}", 
"anchor": "{{ anchor }}", 
"antonyms": "{{ antonyms }}", 
"status": "{{ status }}", 
"nickName": "{{ nickName }}", 
"hierarchyInfo": "{{ hierarchyInfo }}", 
"resources": "{{ resources }}", 
"contacts": "{{ contacts }}", 
"attributes": "{{ attributes }}", 
"assignedEntities": "{{ assignedEntities }}", 
"categories": "{{ categories }}", 
"classifies": "{{ classifies }}", 
"examples": "{{ examples }}", 
"isA": "{{ isA }}", 
"preferredTerms": "{{ preferredTerms }}", 
"preferredToTerms": "{{ preferredToTerms }}", 
"replacedBy": "{{ replacedBy }}", 
"replacementTerms": "{{ replacementTerms }}", 
"seeAlso": "{{ seeAlso }}", 
"synonyms": "{{ synonyms }}", 
"translatedTerms": "{{ translatedTerms }}", 
"translationTerms": "{{ translationTerms }}", 
"usage": "{{ usage }}", 
"validValues": "{{ validValues }}", 
"validValuesFor": "{{ validValuesFor }}"
}'
;
```
</TabItem>
<TabItem value="get_entities_assigned_with_term">

List all related objects assigned with the specified term. Recommend using limit/offset to get pagination result.

```sql
EXEC azure.purview_datamap.glossary.get_entities_assigned_with_term 
@term_id='{{ term_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="assign_term_to_entities">

Assign the given term to the provided list of related objects. Recommend using small batches with multiple API calls. `Entities Create Or Update operation `_ is an alternative to assign a term to multiple entities.

```sql
EXEC azure.purview_datamap.glossary.assign_term_to_entities 
@term_id='{{ term_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"guid": "{{ guid }}", 
"typeName": "{{ typeName }}", 
"uniqueAttributes": "{{ uniqueAttributes }}", 
"displayText": "{{ displayText }}", 
"entityStatus": "{{ entityStatus }}", 
"relationshipType": "{{ relationshipType }}", 
"relationshipAttributes": "{{ relationshipAttributes }}", 
"relationshipGuid": "{{ relationshipGuid }}", 
"relationshipStatus": "{{ relationshipStatus }}"
}'
;
```
</TabItem>
<TabItem value="delete_term_assignment_from_entities">

Delete the term assignment for the given list of related objects.

```sql
EXEC azure.purview_datamap.glossary.delete_term_assignment_from_entities 
@term_id='{{ term_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"guid": "{{ guid }}", 
"typeName": "{{ typeName }}", 
"uniqueAttributes": "{{ uniqueAttributes }}", 
"displayText": "{{ displayText }}", 
"entityStatus": "{{ entityStatus }}", 
"relationshipType": "{{ relationshipType }}", 
"relationshipAttributes": "{{ relationshipAttributes }}", 
"relationshipGuid": "{{ relationshipGuid }}", 
"relationshipStatus": "{{ relationshipStatus }}"
}'
;
```
</TabItem>
<TabItem value="get_related_terms">

Get all related terms for a specific term by its GUID. Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.

```sql
EXEC azure.purview_datamap.glossary.get_related_terms 
@term_id='{{ term_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="get_categories">

Get the categories belonging to a specific glossary. Recommend using limit/offset to get pagination result.

```sql
EXEC azure.purview_datamap.glossary.get_categories 
@glossary_id='{{ glossary_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="get_categories_headers">

Get the category headers belonging to a specific glossary. Recommend using limit/offset to get pagination result.

```sql
EXEC azure.purview_datamap.glossary.get_categories_headers 
@glossary_id='{{ glossary_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="get_detailed">

Get a specific glossary with detailed information. This API is not recommend. Recommend to fetch terms/categories details separately using GET /datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/terms and GET /datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/categories.

```sql
EXEC azure.purview_datamap.glossary.get_detailed 
@glossary_id='{{ glossary_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_terms">

Get terms belonging to a specific glossary. Recommend using limit/offset to get pagination result.

```sql
EXEC azure.purview_datamap.glossary.get_terms 
@glossary_id='{{ glossary_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="get_term_headers">

Get term headers belonging to a specific glossary. Recommend using limit/offset to get pagination result.

```sql
EXEC azure.purview_datamap.glossary.get_term_headers 
@glossary_id='{{ glossary_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}'
;
```
</TabItem>
<TabItem value="batch_get">

Get all glossaries. Recommend using limit/offset to get pagination result. Recommend using 'ignoreTermsAndCategories=true' and fetch terms/categories separately using 'GET /datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/terms' and 'GET '/datamap/api/atlas/v2/glossary/&#123;glossaryId&#125;/categories'.

```sql
EXEC azure.purview_datamap.glossary.batch_get 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@offset='{{ offset }}', 
@sort='{{ sort }}', 
@ignoreTermsAndCategories={{ ignoreTermsAndCategories }}
;
```
</TabItem>
<TabItem value="create_categories">

Create glossary category in bulk.

```sql
EXEC azure.purview_datamap.glossary.create_categories 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"guid": "{{ guid }}", 
"classifications": "{{ classifications }}", 
"longDescription": "{{ longDescription }}", 
"name": "{{ name }}", 
"qualifiedName": "{{ qualifiedName }}", 
"shortDescription": "{{ shortDescription }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"createTime": {{ createTime }}, 
"createdBy": "{{ createdBy }}", 
"updateTime": {{ updateTime }}, 
"updatedBy": "{{ updatedBy }}", 
"anchor": "{{ anchor }}", 
"childrenCategories": "{{ childrenCategories }}", 
"parentCategory": "{{ parentCategory }}", 
"terms": "{{ terms }}"
}'
;
```
</TabItem>
<TabItem value="create_category">

Create a glossary category.

```sql
EXEC azure.purview_datamap.glossary.create_category 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"guid": "{{ guid }}", 
"classifications": "{{ classifications }}", 
"longDescription": "{{ longDescription }}", 
"name": "{{ name }}", 
"qualifiedName": "{{ qualifiedName }}", 
"shortDescription": "{{ shortDescription }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"createTime": {{ createTime }}, 
"createdBy": "{{ createdBy }}", 
"updateTime": {{ updateTime }}, 
"updatedBy": "{{ updatedBy }}", 
"anchor": "{{ anchor }}", 
"childrenCategories": "{{ childrenCategories }}", 
"parentCategory": "{{ parentCategory }}", 
"terms": "{{ terms }}"
}'
;
```
</TabItem>
<TabItem value="partial_update_category">

Update the glossary category partially. So far we only supports partial updating shortDescription and longDescription for category.

```sql
EXEC azure.purview_datamap.glossary.partial_update_category 
@category_id='{{ category_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_term">

Create a glossary term.

```sql
EXEC azure.purview_datamap.glossary.create_term 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }} 
@@json=
'{
"guid": "{{ guid }}", 
"classifications": "{{ classifications }}", 
"longDescription": "{{ longDescription }}", 
"name": "{{ name }}", 
"qualifiedName": "{{ qualifiedName }}", 
"shortDescription": "{{ shortDescription }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"createTime": {{ createTime }}, 
"createdBy": "{{ createdBy }}", 
"updateTime": {{ updateTime }}, 
"updatedBy": "{{ updatedBy }}", 
"abbreviation": "{{ abbreviation }}", 
"templateName": "{{ templateName }}", 
"anchor": "{{ anchor }}", 
"antonyms": "{{ antonyms }}", 
"status": "{{ status }}", 
"nickName": "{{ nickName }}", 
"hierarchyInfo": "{{ hierarchyInfo }}", 
"resources": "{{ resources }}", 
"contacts": "{{ contacts }}", 
"attributes": "{{ attributes }}", 
"assignedEntities": "{{ assignedEntities }}", 
"categories": "{{ categories }}", 
"classifies": "{{ classifies }}", 
"examples": "{{ examples }}", 
"isA": "{{ isA }}", 
"preferredTerms": "{{ preferredTerms }}", 
"preferredToTerms": "{{ preferredToTerms }}", 
"replacedBy": "{{ replacedBy }}", 
"replacementTerms": "{{ replacementTerms }}", 
"seeAlso": "{{ seeAlso }}", 
"synonyms": "{{ synonyms }}", 
"translatedTerms": "{{ translatedTerms }}", 
"translationTerms": "{{ translationTerms }}", 
"usage": "{{ usage }}", 
"validValues": "{{ validValues }}", 
"validValuesFor": "{{ validValuesFor }}"
}'
;
```
</TabItem>
<TabItem value="delete_term">

Delete a glossary term.

```sql
EXEC azure.purview_datamap.glossary.delete_term 
@term_id='{{ term_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="partial_update_term">

Update the glossary term partially. So far we only supports partial updating shortDescription, longDescription, abbreviation, usage and status for term.

```sql
EXEC azure.purview_datamap.glossary.partial_update_term 
@term_id='{{ term_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }}
;
```
</TabItem>
<TabItem value="create_terms">

Create glossary terms in bulk.

```sql
EXEC azure.purview_datamap.glossary.create_terms 
@endpoint='{{ endpoint }}' --required, 
@includeTermHierarchy={{ includeTermHierarchy }} 
@@json=
'{
"guid": "{{ guid }}", 
"classifications": "{{ classifications }}", 
"longDescription": "{{ longDescription }}", 
"name": "{{ name }}", 
"qualifiedName": "{{ qualifiedName }}", 
"shortDescription": "{{ shortDescription }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"createTime": {{ createTime }}, 
"createdBy": "{{ createdBy }}", 
"updateTime": {{ updateTime }}, 
"updatedBy": "{{ updatedBy }}", 
"abbreviation": "{{ abbreviation }}", 
"templateName": "{{ templateName }}", 
"anchor": "{{ anchor }}", 
"antonyms": "{{ antonyms }}", 
"status": "{{ status }}", 
"nickName": "{{ nickName }}", 
"hierarchyInfo": "{{ hierarchyInfo }}", 
"resources": "{{ resources }}", 
"contacts": "{{ contacts }}", 
"attributes": "{{ attributes }}", 
"assignedEntities": "{{ assignedEntities }}", 
"categories": "{{ categories }}", 
"classifies": "{{ classifies }}", 
"examples": "{{ examples }}", 
"isA": "{{ isA }}", 
"preferredTerms": "{{ preferredTerms }}", 
"preferredToTerms": "{{ preferredToTerms }}", 
"replacedBy": "{{ replacedBy }}", 
"replacementTerms": "{{ replacementTerms }}", 
"seeAlso": "{{ seeAlso }}", 
"synonyms": "{{ synonyms }}", 
"translatedTerms": "{{ translatedTerms }}", 
"translationTerms": "{{ translationTerms }}", 
"usage": "{{ usage }}", 
"validValues": "{{ validValues }}", 
"validValuesFor": "{{ validValuesFor }}"
}'
;
```
</TabItem>
<TabItem value="partial_update">

Update the glossary partially. Some properties such as qualifiedName are not allowed to be updated. So far we only supports partial updating shortDescription, longDescription, language and usage for glossary. Recommend using 'ignoreTermsAndCategories=true' to reduce response body size.

```sql
EXEC azure.purview_datamap.glossary.partial_update 
@glossary_id='{{ glossary_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ignoreTermsAndCategories={{ ignoreTermsAndCategories }}
;
```
</TabItem>
</Tabs>
