--- 
title: resource_links
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_links
  - resource
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

Creates, updates, deletes, gets or lists a <code>resource_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_links" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.resource_links" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_at_subscription', value: 'list_at_subscription' },
        { label: 'list_at_source_scope', value: 'list_at_source_scope' }
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
    <td>The fully qualified ID of the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the source resource in the link.</td>
</tr>
<tr>
    <td><CopyableCode code="targetId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the target resource in the link. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>object</code></td>
    <td>The resource link object.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_subscription">

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
    <td>The fully qualified ID of the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the source resource in the link.</td>
</tr>
<tr>
    <td><CopyableCode code="targetId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the target resource in the link. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>object</code></td>
    <td>The resource link object.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_source_scope">

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
    <td>The fully qualified ID of the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the resource link.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the source resource in the link.</td>
</tr>
<tr>
    <td><CopyableCode code="targetId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the target resource in the link. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>object</code></td>
    <td>The resource link object.</td>
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
    <td><a href="#parameter-link_id"><code>link_id</code></a></td>
    <td></td>
    <td>Gets a resource link with the specified ID.</td>
</tr>
<tr>
    <td><a href="#list_at_subscription"><CopyableCode code="list_at_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all the linked resources for the subscription.</td>
</tr>
<tr>
    <td><a href="#list_at_source_scope"><CopyableCode code="list_at_source_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a list of resource links at and below the specified source scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-link_id"><code>link_id</code></a></td>
    <td></td>
    <td>Creates or updates a resource link between the specified resources.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-link_id"><code>link_id</code></a></td>
    <td></td>
    <td>Creates or updates a resource link between the specified resources.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-link_id"><code>link_id</code></a></td>
    <td></td>
    <td>Deletes a resource link with the specified ID.</td>
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
<tr id="parameter-link_id">
    <td><CopyableCode code="link_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the resource link. Use the format, /subscriptions/&#123;subscription-id&#125;/resourceGroups/&#123;resource-group-name&#125;/&#123;provider-namespace&#125;/&#123;resource-type&#125;/&#123;resource-name&#125;/Microsoft.Resources/links/&#123;link-name&#125;. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the scope for getting the resource links. For example, to list resource links at and under a resource group, set the scope to /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply when getting resource links. To get links only at the specified scope (not below the scope), use Filter.atScope(). Known values are "atScope()" and None. Default value is "atScope()".</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_at_subscription', value: 'list_at_subscription' },
        { label: 'list_at_source_scope', value: 'list_at_source_scope' }
    ]}
>
<TabItem value="get">

Gets a resource link with the specified ID.

```sql
SELECT
id,
name,
notes,
sourceId,
targetId,
type
FROM azure.resource.resource_links
WHERE link_id = '{{ link_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_subscription">

Gets all the linked resources for the subscription.

```sql
SELECT
id,
name,
notes,
sourceId,
targetId,
type
FROM azure.resource.resource_links
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_at_source_scope">

Gets a list of resource links at and below the specified source scope.

```sql
SELECT
id,
name,
notes,
sourceId,
targetId,
type
FROM azure.resource.resource_links
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
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

Creates or updates a resource link between the specified resources.

```sql
INSERT INTO azure.resource.resource_links (
properties,
link_id
)
SELECT 
'{{ properties }}',
'{{ link_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: resource_links
  props:
    - name: link_id
      value: "{{ link_id }}"
      description: Required parameter for the resource_links resource.
    - name: properties
      description: |
        Properties for resource link.
      value:
        sourceId: "{{ sourceId }}"
        targetId: "{{ targetId }}"
        notes: "{{ notes }}"
`}</CodeBlock>

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

Creates or updates a resource link between the specified resources.

```sql
REPLACE azure.resource.resource_links
SET 
properties = '{{ properties }}'
WHERE 
link_id = '{{ link_id }}' --required
RETURNING
id,
name,
properties,
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

Deletes a resource link with the specified ID.

```sql
DELETE FROM azure.resource.resource_links
WHERE link_id = '{{ link_id }}' --required
;
```
</TabItem>
</Tabs>
