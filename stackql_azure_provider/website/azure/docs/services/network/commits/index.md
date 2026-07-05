--- 
title: commits
hide_title: false
hide_table_of_contents: false
keywords:
  - commits
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

Creates, updates, deletes, gets or lists a <code>commits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="commits" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.commits" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="activeLocations" /></td>
    <td><code>array</code></td>
    <td>List of active locations.</td>
</tr>
<tr>
    <td><CopyableCode code="commitType" /></td>
    <td><code>string</code></td>
    <td>Commit Type. Required. Known values are: "SecurityAdmin", "Connectivity", "SecurityUser", and "Routing". (SecurityAdmin, Connectivity, SecurityUser, Routing)</td>
</tr>
<tr>
    <td><CopyableCode code="configurationIds" /></td>
    <td><code>array</code></td>
    <td>List of configuration IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the commit.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>A value that, when changed, forces the commit to be re-evaluated and redeployed.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata related to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetLocations" /></td>
    <td><code>array</code></td>
    <td>List of target locations. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="activeLocations" /></td>
    <td><code>array</code></td>
    <td>List of active locations.</td>
</tr>
<tr>
    <td><CopyableCode code="commitType" /></td>
    <td><code>string</code></td>
    <td>Commit Type. Required. Known values are: "SecurityAdmin", "Connectivity", "SecurityUser", and "Routing". (SecurityAdmin, Connectivity, SecurityUser, Routing)</td>
</tr>
<tr>
    <td><CopyableCode code="configurationIds" /></td>
    <td><code>array</code></td>
    <td>List of configuration IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the commit.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>A value that, when changed, forces the commit to be re-evaluated and redeployed.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata related to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetLocations" /></td>
    <td><code>array</code></td>
    <td>List of target locations. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-commit_name"><code>commit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified commit.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists all commits for the specified network manager.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-commit_name"><code>commit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a commit.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-commit_name"><code>commit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a commit.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-commit_name"><code>commit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a commit.</td>
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
<tr id="parameter-commit_name">
    <td><CopyableCode code="commit_name" /></td>
    <td><code>string</code></td>
    <td>The name of the commit. Required.</td>
</tr>
<tr id="parameter-network_manager_name">
    <td><CopyableCode code="network_manager_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network manager. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>SkipToken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>An optional query parameter which specifies the maximum number of records to be returned by the server. Default value is None.</td>
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

Gets the specified commit.

```sql
SELECT
id,
name,
activeLocations,
commitType,
configurationIds,
description,
etag,
forceUpdateTag,
provisioningState,
resourceGuid,
systemData,
targetLocations,
type
FROM azure.network.commits
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_manager_name = '{{ network_manager_name }}' -- required
AND commit_name = '{{ commit_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all commits for the specified network manager.

```sql
SELECT
id,
name,
activeLocations,
commitType,
configurationIds,
description,
etag,
forceUpdateTag,
provisioningState,
resourceGuid,
systemData,
targetLocations,
type
FROM azure.network.commits
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_manager_name = '{{ network_manager_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Creates or updates a commit.

```sql
INSERT INTO azure.network.commits (
properties,
resource_group_name,
network_manager_name,
commit_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_manager_name }}',
'{{ commit_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: commits
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the commits resource.
    - name: network_manager_name
      value: "{{ network_manager_name }}"
      description: Required parameter for the commits resource.
    - name: commit_name
      value: "{{ commit_name }}"
      description: Required parameter for the commits resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the commits resource.
    - name: properties
      description: |
        The Commit properties.
      value:
        description: "{{ description }}"
        provisioningState: "{{ provisioningState }}"
        resourceGuid: "{{ resourceGuid }}"
        commitType: "{{ commitType }}"
        configurationIds:
          - "{{ configurationIds }}"
        targetLocations:
          - "{{ targetLocations }}"
        activeLocations:
          - "{{ activeLocations }}"
        forceUpdateTag: "{{ forceUpdateTag }}"
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

Creates or updates a commit.

```sql
REPLACE azure.network.commits
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_manager_name = '{{ network_manager_name }}' --required
AND commit_name = '{{ commit_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
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

Deletes a commit.

```sql
DELETE FROM azure.network.commits
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_manager_name = '{{ network_manager_name }}' --required
AND commit_name = '{{ commit_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
