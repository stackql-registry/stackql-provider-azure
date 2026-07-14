--- 
title: tenant_access_git
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access_git
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tenant_access_git</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tenant_access_git" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_access_git" /></td></tr>
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
    <td><a href="#regenerate_primary_key"><CopyableCode code="regenerate_primary_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-access_name"><code>access_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerate primary access key for GIT.</td>
</tr>
<tr>
    <td><a href="#regenerate_secondary_key"><CopyableCode code="regenerate_secondary_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-access_name"><code>access_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerate secondary access key for GIT.</td>
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
<tr id="parameter-access_name">
    <td><CopyableCode code="access_name" /></td>
    <td><code>string</code></td>
    <td>The identifier of the Access configuration. Known values are: "access" and "gitAccess". Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="regenerate_primary_key"
    values={[
        { label: 'regenerate_primary_key', value: 'regenerate_primary_key' },
        { label: 'regenerate_secondary_key', value: 'regenerate_secondary_key' }
    ]}
>
<TabItem value="regenerate_primary_key">

Regenerate primary access key for GIT.

```sql
EXEC azure.api_management.tenant_access_git.regenerate_primary_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@access_name='{{ access_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_secondary_key">

Regenerate secondary access key for GIT.

```sql
EXEC azure.api_management.tenant_access_git.regenerate_secondary_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@access_name='{{ access_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
