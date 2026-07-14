--- 
title: time_series_database_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - time_series_database_connections
  - digital_twins
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

Creates, updates, deletes, gets or lists a <code>time_series_database_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="time_series_database_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digital_twins.time_series_database_connections" /></td></tr>
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
    <td>The resource identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Extension resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionType" /></td>
    <td><code>string</code></td>
    <td>The type of time series connection resource. Required. "AzureDataExplorer"</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed identity properties for the time series database connection resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Provisioning", "Deleting", "Updating", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring", "Moving", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td>The resource identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Extension resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionType" /></td>
    <td><code>string</code></td>
    <td>The type of time series connection resource. Required. "AzureDataExplorer"</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed identity properties for the time series database connection resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Provisioning", "Deleting", "Updating", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring", "Moving", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-time_series_database_connection_name"><code>time_series_database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the description of an existing time series database connection.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all existing time series database connections for this DigitalTwins instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-time_series_database_connection_name"><code>time_series_database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a time series database connection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-time_series_database_connection_name"><code>time_series_database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a time series database connection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-time_series_database_connection_name"><code>time_series_database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-cleanupConnectionArtifacts"><code>cleanupConnectionArtifacts</code></a></td>
    <td>Delete a time series database connection.</td>
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
    <td>The name of the resource group that contains the DigitalTwinsInstance. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DigitalTwinsInstance. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-time_series_database_connection_name">
    <td><CopyableCode code="time_series_database_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name of time series database connection. Required.</td>
</tr>
<tr id="parameter-cleanupConnectionArtifacts">
    <td><CopyableCode code="cleanupConnectionArtifacts" /></td>
    <td><code>string</code></td>
    <td>Specifies whether or not to attempt to clean up artifacts that were created in order to establish a connection to the time series database. This is a best-effort attempt that will fail if appropriate permissions are not in place. Setting this to 'true' does not delete any recorded data. Known values are: "true" and "false". Default value is None.</td>
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

Get the description of an existing time series database connection.

```sql
SELECT
id,
name,
connectionType,
identity,
provisioningState,
systemData,
type
FROM azure.digital_twins.time_series_database_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND time_series_database_connection_name = '{{ time_series_database_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all existing time series database connections for this DigitalTwins instance.

```sql
SELECT
id,
name,
connectionType,
identity,
provisioningState,
systemData,
type
FROM azure.digital_twins.time_series_database_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Create or update a time series database connection.

```sql
INSERT INTO azure.digital_twins.time_series_database_connections (
properties,
resource_group_name,
resource_name,
time_series_database_connection_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ time_series_database_connection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: time_series_database_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the time_series_database_connections resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the time_series_database_connections resource.
    - name: time_series_database_connection_name
      value: "{{ time_series_database_connection_name }}"
      description: Required parameter for the time_series_database_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the time_series_database_connections resource.
    - name: properties
      description: |
        Properties of a specific time series database connection.
      value:
        connectionType: "{{ connectionType }}"
        provisioningState: "{{ provisioningState }}"
        identity:
          type: "{{ type }}"
          userAssignedIdentity: "{{ userAssignedIdentity }}"
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

Create or update a time series database connection.

```sql
REPLACE azure.digital_twins.time_series_database_connections
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND time_series_database_connection_name = '{{ time_series_database_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete a time series database connection.

```sql
DELETE FROM azure.digital_twins.time_series_database_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND time_series_database_connection_name = '{{ time_series_database_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND cleanupConnectionArtifacts = '{{ cleanupConnectionArtifacts }}'
;
```
</TabItem>
</Tabs>
