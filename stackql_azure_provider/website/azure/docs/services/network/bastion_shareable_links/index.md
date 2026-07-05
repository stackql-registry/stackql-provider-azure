--- 
title: bastion_shareable_links
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_shareable_links
  - network
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

Creates, updates, deletes, gets or lists a <code>bastion_shareable_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bastion_shareable_links" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.bastion_shareable_links" /></td></tr>
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
    <td><a href="#delete_bastion_shareable_link"><CopyableCode code="delete_bastion_shareable_link" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the Bastion Shareable Links for all the VMs specified in the request.</td>
</tr>
<tr>
    <td><a href="#get_bastion_shareable_link"><CopyableCode code="get_bastion_shareable_link" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Return the Bastion Shareable Links for all the VMs specified in the request.</td>
</tr>
<tr>
    <td><a href="#put_bastion_shareable_link"><CopyableCode code="put_bastion_shareable_link" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a Bastion Shareable Links for all the VMs specified in the request.</td>
</tr>
<tr>
    <td><a href="#delete_bastion_shareable_link_by_token"><CopyableCode code="delete_bastion_shareable_link_by_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the Bastion Shareable Links for all the tokens specified in the request.</td>
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
<tr id="parameter-bastion_host_name">
    <td><CopyableCode code="bastion_host_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bastion Host. Required.</td>
</tr>
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
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="delete_bastion_shareable_link"
    values={[
        { label: 'delete_bastion_shareable_link', value: 'delete_bastion_shareable_link' }
    ]}
>
<TabItem value="delete_bastion_shareable_link">

Deletes the Bastion Shareable Links for all the VMs specified in the request.

```sql
DELETE FROM azure.network.bastion_shareable_links
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND bastion_host_name = '{{ bastion_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_bastion_shareable_link"
    values={[
        { label: 'get_bastion_shareable_link', value: 'get_bastion_shareable_link' },
        { label: 'put_bastion_shareable_link', value: 'put_bastion_shareable_link' },
        { label: 'delete_bastion_shareable_link_by_token', value: 'delete_bastion_shareable_link_by_token' }
    ]}
>
<TabItem value="get_bastion_shareable_link">

Return the Bastion Shareable Links for all the VMs specified in the request.

```sql
EXEC azure.network.bastion_shareable_links.get_bastion_shareable_link 
@resource_group_name='{{ resource_group_name }}' --required, 
@bastion_host_name='{{ bastion_host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vms": "{{ vms }}"
}'
;
```
</TabItem>
<TabItem value="put_bastion_shareable_link">

Creates a Bastion Shareable Links for all the VMs specified in the request.

```sql
EXEC azure.network.bastion_shareable_links.put_bastion_shareable_link 
@resource_group_name='{{ resource_group_name }}' --required, 
@bastion_host_name='{{ bastion_host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vms": "{{ vms }}"
}'
;
```
</TabItem>
<TabItem value="delete_bastion_shareable_link_by_token">

Deletes the Bastion Shareable Links for all the tokens specified in the request.

```sql
EXEC azure.network.bastion_shareable_links.delete_bastion_shareable_link_by_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@bastion_host_name='{{ bastion_host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tokens": "{{ tokens }}"
}'
;
```
</TabItem>
</Tabs>
