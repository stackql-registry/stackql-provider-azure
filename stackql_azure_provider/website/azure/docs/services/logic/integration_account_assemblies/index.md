--- 
title: integration_account_assemblies
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_assemblies
  - logic
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

Creates, updates, deletes, gets or lists an <code>integration_account_assemblies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_account_assemblies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.integration_account_assemblies" /></td></tr>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyCulture" /></td>
    <td><code>string</code></td>
    <td>The assembly culture.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyName" /></td>
    <td><code>string</code></td>
    <td>The assembly name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyPublicKeyToken" /></td>
    <td><code>string</code></td>
    <td>The assembly public key token.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyVersion" /></td>
    <td><code>string</code></td>
    <td>The assembly version.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The artifact changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>Anything.</td>
</tr>
<tr>
    <td><CopyableCode code="contentLink" /></td>
    <td><code>object</code></td>
    <td>The content link.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The artifact creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Anything.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyCulture" /></td>
    <td><code>string</code></td>
    <td>The assembly culture.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyName" /></td>
    <td><code>string</code></td>
    <td>The assembly name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyPublicKeyToken" /></td>
    <td><code>string</code></td>
    <td>The assembly public key token.</td>
</tr>
<tr>
    <td><CopyableCode code="assemblyVersion" /></td>
    <td><code>string</code></td>
    <td>The assembly version.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The artifact changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>Anything.</td>
</tr>
<tr>
    <td><CopyableCode code="contentLink" /></td>
    <td><code>object</code></td>
    <td>The content link.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The artifact creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Anything.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-assembly_artifact_name"><code>assembly_artifact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an assembly for an integration account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the assemblies for an integration account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-assembly_artifact_name"><code>assembly_artifact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an assembly for an integration account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-assembly_artifact_name"><code>assembly_artifact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an assembly for an integration account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-assembly_artifact_name"><code>assembly_artifact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an assembly for an integration account.</td>
</tr>
<tr>
    <td><a href="#list_content_callback_url"><CopyableCode code="list_content_callback_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-assembly_artifact_name"><code>assembly_artifact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the content callback url for an integration account assembly.</td>
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
<tr id="parameter-assembly_artifact_name">
    <td><CopyableCode code="assembly_artifact_name" /></td>
    <td><code>string</code></td>
    <td>The assembly artifact name. Required.</td>
</tr>
<tr id="parameter-integration_account_name">
    <td><CopyableCode code="integration_account_name" /></td>
    <td><code>string</code></td>
    <td>The integration account name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get an assembly for an integration account.

```sql
SELECT
id,
name,
assemblyCulture,
assemblyName,
assemblyPublicKeyToken,
assemblyVersion,
changedTime,
content,
contentLink,
contentType,
createdTime,
location,
metadata,
tags,
type
FROM azure.logic.integration_account_assemblies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND integration_account_name = '{{ integration_account_name }}' -- required
AND assembly_artifact_name = '{{ assembly_artifact_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the assemblies for an integration account.

```sql
SELECT
id,
name,
assemblyCulture,
assemblyName,
assemblyPublicKeyToken,
assemblyVersion,
changedTime,
content,
contentLink,
contentType,
createdTime,
location,
metadata,
tags,
type
FROM azure.logic.integration_account_assemblies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND integration_account_name = '{{ integration_account_name }}' -- required
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

Create or update an assembly for an integration account.

```sql
INSERT INTO azure.logic.integration_account_assemblies (
location,
tags,
properties,
resource_group_name,
integration_account_name,
assembly_artifact_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ integration_account_name }}',
'{{ assembly_artifact_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: integration_account_assemblies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the integration_account_assemblies resource.
    - name: integration_account_name
      value: "{{ integration_account_name }}"
      description: Required parameter for the integration_account_assemblies resource.
    - name: assembly_artifact_name
      value: "{{ assembly_artifact_name }}"
      description: Required parameter for the integration_account_assemblies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the integration_account_assemblies resource.
    - name: location
      value: "{{ location }}"
      description: |
        The resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: properties
      description: |
        The assembly properties. Required.
      value:
        createdTime: "{{ createdTime }}"
        changedTime: "{{ changedTime }}"
        metadata: "{{ metadata }}"
        content: "{{ content }}"
        contentType: "{{ contentType }}"
        contentLink:
          uri: "{{ uri }}"
          contentVersion: "{{ contentVersion }}"
          contentSize: {{ contentSize }}
          contentHash:
            algorithm: "{{ algorithm }}"
            value: "{{ value }}"
          metadata: "{{ metadata }}"
        assemblyName: "{{ assemblyName }}"
        assemblyVersion: "{{ assemblyVersion }}"
        assemblyCulture: "{{ assemblyCulture }}"
        assemblyPublicKeyToken: "{{ assemblyPublicKeyToken }}"
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

Create or update an assembly for an integration account.

```sql
REPLACE azure.logic.integration_account_assemblies
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND integration_account_name = '{{ integration_account_name }}' --required
AND assembly_artifact_name = '{{ assembly_artifact_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
location,
properties,
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

Delete an assembly for an integration account.

```sql
DELETE FROM azure.logic.integration_account_assemblies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND integration_account_name = '{{ integration_account_name }}' --required
AND assembly_artifact_name = '{{ assembly_artifact_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_content_callback_url"
    values={[
        { label: 'list_content_callback_url', value: 'list_content_callback_url' }
    ]}
>
<TabItem value="list_content_callback_url">

Get the content callback url for an integration account assembly.

```sql
EXEC azure.logic.integration_account_assemblies.list_content_callback_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@integration_account_name='{{ integration_account_name }}' --required, 
@assembly_artifact_name='{{ assembly_artifact_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
