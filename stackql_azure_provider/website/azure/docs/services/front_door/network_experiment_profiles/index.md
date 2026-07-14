--- 
title: network_experiment_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - network_experiment_profiles
  - front_door
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

Creates, updates, deletes, gets or lists a <code>network_experiment_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_experiment_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.network_experiment_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>The state of the Experiment. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets a unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>The state of the Experiment. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets a unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>The state of the Experiment. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets a unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an NetworkExperiment Profile by ProfileName. Gets an NetworkExperiment Profile by ProfileName.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Network Experiment Profiles within a resource group under a subscription. Gets a list of Network Experiment Profiles within a resource group under a subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Network Experiment Profiles under a subscription. Gets a list of Network Experiment Profiles under a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an NetworkExperiment Profile. Creates an NetworkExperiment Profile.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an NetworkExperimentProfiles by NetworkExperimentProfile name. Updates an NetworkExperimentProfiles.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an NetworkExperiment Profile. Creates an NetworkExperiment Profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an NetworkExperiment Profile by ProfileName. Deletes an NetworkExperiment Profile by ProfileName.</td>
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
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>The Profile identifier associated with the Tenant and Partner. Required.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets an NetworkExperiment Profile by ProfileName. Gets an NetworkExperiment Profile by ProfileName.

```sql
SELECT
id,
name,
enabledState,
etag,
location,
resourceState,
tags,
type
FROM azure.front_door.network_experiment_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of Network Experiment Profiles within a resource group under a subscription. Gets a list of Network Experiment Profiles within a resource group under a subscription.

```sql
SELECT
id,
name,
enabledState,
etag,
location,
resourceState,
tags,
type
FROM azure.front_door.network_experiment_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of Network Experiment Profiles under a subscription. Gets a list of Network Experiment Profiles under a subscription.

```sql
SELECT
id,
name,
enabledState,
etag,
location,
resourceState,
tags,
type
FROM azure.front_door.network_experiment_profiles
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

Creates an NetworkExperiment Profile. Creates an NetworkExperiment Profile.

```sql
INSERT INTO azure.front_door.network_experiment_profiles (
location,
tags,
properties,
etag,
profile_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ etag }}',
'{{ profile_name }}',
'{{ resource_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_experiment_profiles
  props:
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the network_experiment_profiles resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_experiment_profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_experiment_profiles resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        The properties of a Profile.
      value:
        resourceState: "{{ resourceState }}"
        enabledState: "{{ enabledState }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Gets a unique read-only string that changes whenever the resource is updated.
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

Updates an NetworkExperimentProfiles by NetworkExperimentProfile name. Updates an NetworkExperimentProfiles.

```sql
UPDATE azure.front_door.network_experiment_profiles
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Creates an NetworkExperiment Profile. Creates an NetworkExperiment Profile.

```sql
REPLACE azure.front_door.network_experiment_profiles
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
profile_name = '{{ profile_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Deletes an NetworkExperiment Profile by ProfileName. Deletes an NetworkExperiment Profile by ProfileName.

```sql
DELETE FROM azure.front_door.network_experiment_profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
