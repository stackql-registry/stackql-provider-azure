--- 
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - costmanagement
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.costmanagement.settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_scope"
    values={[
        { label: 'get_by_scope', value: 'get_by_scope' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_scope">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. "taginheritance"</td>
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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. "taginheritance"</td>
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
    <td><a href="#get_by_scope"><CopyableCode code="get_by_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-type_name"><code>type_name</code></a></td>
    <td></td>
    <td>Get the setting from the given scope by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>List all cost management settings in the requested scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_scope"><CopyableCode code="create_or_update_by_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create or update a setting within the given scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_scope"><CopyableCode code="create_or_update_by_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create or update a setting within the given scope.</td>
</tr>
<tr>
    <td><a href="#delete_by_scope"><CopyableCode code="delete_by_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-type_name"><code>type_name</code></a></td>
    <td></td>
    <td>Delete a setting within the given scope.</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>undefined. Required.</td>
</tr>
<tr id="parameter-type_name">
    <td><CopyableCode code="type_name" /></td>
    <td><code>string</code></td>
    <td>Setting type. "taginheritance" Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_scope"
    values={[
        { label: 'get_by_scope', value: 'get_by_scope' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_scope">

Get the setting from the given scope by name.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.costmanagement.settings
WHERE scope = '{{ scope }}' -- required
AND type_name = '{{ type_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all cost management settings in the requested scope.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.costmanagement.settings
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_by_scope"
    values={[
        { label: 'create_or_update_by_scope', value: 'create_or_update_by_scope' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_by_scope">

Create or update a setting within the given scope.

```sql
INSERT INTO azure.costmanagement.settings (
kind,
scope,
type_name
)
SELECT 
'{{ kind }}' /* required */,
'{{ scope }}',
'{{ type_name }}'
RETURNING
id,
name,
kind,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: settings
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the settings resource.
    - name: type_name
      value: "{{ type_name }}"
      description: Required parameter for the settings resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. "taginheritance"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_by_scope"
    values={[
        { label: 'create_or_update_by_scope', value: 'create_or_update_by_scope' }
    ]}
>
<TabItem value="create_or_update_by_scope">

Create or update a setting within the given scope.

```sql
REPLACE azure.costmanagement.settings
SET 
kind = '{{ kind }}'
WHERE 
scope = '{{ scope }}' --required
AND type_name = '{{ type_name }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
kind,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_scope"
    values={[
        { label: 'delete_by_scope', value: 'delete_by_scope' }
    ]}
>
<TabItem value="delete_by_scope">

Delete a setting within the given scope.

```sql
DELETE FROM azure.costmanagement.settings
WHERE scope = '{{ scope }}' --required
AND type_name = '{{ type_name }}' --required
;
```
</TabItem>
</Tabs>
