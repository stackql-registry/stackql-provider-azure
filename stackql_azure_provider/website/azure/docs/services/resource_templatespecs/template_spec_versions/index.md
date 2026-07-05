--- 
title: template_spec_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - template_spec_versions
  - resource_templatespecs
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

Creates, updates, deletes, gets or lists a <code>template_spec_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="template_spec_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_templatespecs.template_spec_versions" /></td></tr>
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
    <td>String Id used to locate any resource on Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Template Spec version description.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedTemplates" /></td>
    <td><code>array</code></td>
    <td>An array of linked template artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the Template Spec Version. It must match the location of the parent Template Spec. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mainTemplate" /></td>
    <td><code>object</code></td>
    <td>The main Azure Resource Manager template content.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The version metadata. Metadata is an open-ended object and is typically a collection of key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uiFormDefinition" /></td>
    <td><code>object</code></td>
    <td>The Azure Resource Manager template UI definition content.</td>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>String Id used to locate any resource on Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Template Spec version description.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedTemplates" /></td>
    <td><code>array</code></td>
    <td>An array of linked template artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the Template Spec Version. It must match the location of the parent Template Spec. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mainTemplate" /></td>
    <td><code>object</code></td>
    <td>The main Azure Resource Manager template content.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The version metadata. Metadata is an open-ended object and is typically a collection of key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uiFormDefinition" /></td>
    <td><code>object</code></td>
    <td>The Azure Resource Manager template UI definition content.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-template_spec_name"><code>template_spec_name</code></a>, <a href="#parameter-template_spec_version"><code>template_spec_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Template Spec version from a specific Template Spec.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-template_spec_name"><code>template_spec_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the Template Spec versions in the specified Template Spec.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-template_spec_name"><code>template_spec_name</code></a>, <a href="#parameter-template_spec_version"><code>template_spec_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Template Spec version.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-template_spec_name"><code>template_spec_name</code></a>, <a href="#parameter-template_spec_version"><code>template_spec_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates Template Spec Version tags with specified values.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-template_spec_name"><code>template_spec_name</code></a>, <a href="#parameter-template_spec_version"><code>template_spec_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Template Spec version.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-template_spec_name"><code>template_spec_name</code></a>, <a href="#parameter-template_spec_version"><code>template_spec_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specific version from a Template Spec. When operation completes, status code 200 returned without content.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-template_spec_name">
    <td><CopyableCode code="template_spec_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Template Spec. Required.</td>
</tr>
<tr id="parameter-template_spec_version">
    <td><CopyableCode code="template_spec_version" /></td>
    <td><code>string</code></td>
    <td>The version of the Template Spec. Required.</td>
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

Gets a Template Spec version from a specific Template Spec.

```sql
SELECT
id,
name,
description,
linkedTemplates,
location,
mainTemplate,
metadata,
systemData,
tags,
type,
uiFormDefinition
FROM azure.resource_templatespecs.template_spec_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND template_spec_name = '{{ template_spec_name }}' -- required
AND template_spec_version = '{{ template_spec_version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the Template Spec versions in the specified Template Spec.

```sql
SELECT
id,
name,
description,
linkedTemplates,
location,
mainTemplate,
metadata,
systemData,
tags,
type,
uiFormDefinition
FROM azure.resource_templatespecs.template_spec_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND template_spec_name = '{{ template_spec_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a Template Spec version.

```sql
INSERT INTO azure.resource_templatespecs.template_spec_versions (
location,
tags,
properties,
resource_group_name,
template_spec_name,
template_spec_version,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ template_spec_name }}',
'{{ template_spec_version }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: template_spec_versions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the template_spec_versions resource.
    - name: template_spec_name
      value: "{{ template_spec_name }}"
      description: Required parameter for the template_spec_versions resource.
    - name: template_spec_version
      value: "{{ template_spec_version }}"
      description: Required parameter for the template_spec_versions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the template_spec_versions resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location of the Template Spec Version. It must match the location of the parent Template Spec. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      value:
        description: "{{ description }}"
        linkedTemplates:
          - path: "{{ path }}"
            template: "{{ template }}"
        metadata: "{{ metadata }}"
        mainTemplate: "{{ mainTemplate }}"
        uiFormDefinition: "{{ uiFormDefinition }}"
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

Updates Template Spec Version tags with specified values.

```sql
UPDATE azure.resource_templatespecs.template_spec_versions
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND template_spec_name = '{{ template_spec_name }}' --required
AND template_spec_version = '{{ template_spec_version }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Creates or updates a Template Spec version.

```sql
REPLACE azure.resource_templatespecs.template_spec_versions
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND template_spec_name = '{{ template_spec_name }}' --required
AND template_spec_version = '{{ template_spec_version }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Deletes a specific version from a Template Spec. When operation completes, status code 200 returned without content.

```sql
DELETE FROM azure.resource_templatespecs.template_spec_versions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND template_spec_name = '{{ template_spec_name }}' --required
AND template_spec_version = '{{ template_spec_version }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
