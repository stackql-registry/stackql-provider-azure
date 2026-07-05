--- 
title: management_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - management_associations
  - operationsmanagement
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

Creates, updates, deletes, gets or lists a <code>management_associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="management_associations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operationsmanagement.management_associations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationId" /></td>
    <td><code>string</code></td>
    <td>The applicationId of the appliance for this association. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationId" /></td>
    <td><code>string</code></td>
    <td>The applicationId of the appliance for this association. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-management_association_name"><code>management_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve ManagementAssociation. Retrieves the user ManagementAssociation.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the ManagementAssociations list for the subscription. Retrieves the ManagementAssociations list.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-management_association_name"><code>management_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create/Update ManagementAssociation. Creates or updates the ManagementAssociation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-management_association_name"><code>management_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create/Update ManagementAssociation. Creates or updates the ManagementAssociation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-management_association_name"><code>management_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the ManagementAssociation. Deletes the ManagementAssociation in the subscription.</td>
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
<tr id="parameter-management_association_name">
    <td><CopyableCode code="management_association_name" /></td>
    <td><code>string</code></td>
    <td>User ManagementAssociation Name. Required.</td>
</tr>
<tr id="parameter-provider_name">
    <td><CopyableCode code="provider_name" /></td>
    <td><code>string</code></td>
    <td>Provider name for the parent resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group to get. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Parent resource name. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>Resource type for the parent resource. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Retrieve ManagementAssociation. Retrieves the user ManagementAssociation.

```sql
SELECT
id,
name,
applicationId,
location,
type
FROM azure.operationsmanagement.management_associations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provider_name = '{{ provider_name }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND management_association_name = '{{ management_association_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Retrieves the ManagementAssociations list for the subscription. Retrieves the ManagementAssociations list.

```sql
SELECT
id,
name,
applicationId,
location,
type
FROM azure.operationsmanagement.management_associations
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create/Update ManagementAssociation. Creates or updates the ManagementAssociation.

```sql
INSERT INTO azure.operationsmanagement.management_associations (
location,
properties,
resource_group_name,
provider_name,
resource_type,
resource_name,
management_association_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ provider_name }}',
'{{ resource_type }}',
'{{ resource_name }}',
'{{ management_association_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: management_associations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the management_associations resource.
    - name: provider_name
      value: "{{ provider_name }}"
      description: Required parameter for the management_associations resource.
    - name: resource_type
      value: "{{ resource_type }}"
      description: Required parameter for the management_associations resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the management_associations resource.
    - name: management_association_name
      value: "{{ management_association_name }}"
      description: Required parameter for the management_associations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the management_associations resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: properties
      description: |
        Properties for ManagementAssociation object supported by the OperationsManagement resource provider.
      value:
        applicationId: "{{ applicationId }}"
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

Create/Update ManagementAssociation. Creates or updates the ManagementAssociation.

```sql
REPLACE azure.operationsmanagement.management_associations
SET 
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND provider_name = '{{ provider_name }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND management_association_name = '{{ management_association_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Deletes the ManagementAssociation. Deletes the ManagementAssociation in the subscription.

```sql
DELETE FROM azure.operationsmanagement.management_associations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND provider_name = '{{ provider_name }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND management_association_name = '{{ management_association_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
