--- 
title: external_user
hide_title: false
hide_table_of_contents: false
keywords:
  - external_user
  - elastic
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>external_user</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="external_user" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.external_user" /></td></tr>
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
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users. Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users. Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users.</td>
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
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Monitor resource name. Required.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users. Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users.

```sql
INSERT INTO azure_isv.elastic.external_user (
userName,
fullName,
password,
emailId,
roles,
resource_group_name,
monitor_name,
subscription_id
)
SELECT 
'{{ userName }}',
'{{ fullName }}',
'{{ password }}',
'{{ emailId }}',
'{{ roles }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
'{{ subscription_id }}'
RETURNING
created
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: external_user
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the external_user resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the external_user resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the external_user resource.
    - name: userName
      value: "{{ userName }}"
      description: |
        Username of the user to be created or updated.
    - name: fullName
      value: "{{ fullName }}"
      description: |
        Full name of the user to be created or updated.
    - name: password
      value: "{{ password }}"
      description: |
        Password of the user to be created or updated.
    - name: emailId
      value: "{{ emailId }}"
      description: |
        Email id of the user to be created or updated.
    - name: roles
      value:
        - "{{ roles }}"
      description: |
        Roles to be assigned for created or updated user.
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

Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users. Create or update external user configurations for your Elastic monitor resource, enabling access and management by external users.

```sql
REPLACE azure_isv.elastic.external_user
SET 
userName = '{{ userName }}',
fullName = '{{ fullName }}',
password = '{{ password }}',
emailId = '{{ emailId }}',
roles = '{{ roles }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
created;
```
</TabItem>
</Tabs>
