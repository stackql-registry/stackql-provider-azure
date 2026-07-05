--- 
title: integration_account_batch_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_batch_configurations
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

Creates, updates, deletes, gets or lists an <code>integration_account_batch_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_account_batch_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.integration_account_batch_configurations" /></td></tr>
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
    <td><CopyableCode code="batchGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the batch group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The artifact changed time.</td>
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
    <td><CopyableCode code="releaseCriteria" /></td>
    <td><code>object</code></td>
    <td>The batch release criteria. Required.</td>
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
    <td><CopyableCode code="batchGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the batch group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The artifact changed time.</td>
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
    <td><CopyableCode code="releaseCriteria" /></td>
    <td><code>object</code></td>
    <td>The batch release criteria. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-batch_configuration_name"><code>batch_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a batch configuration for an integration account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the batch configurations for an integration account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-batch_configuration_name"><code>batch_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a batch configuration for an integration account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-batch_configuration_name"><code>batch_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a batch configuration for an integration account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-batch_configuration_name"><code>batch_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a batch configuration for an integration account.</td>
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
<tr id="parameter-batch_configuration_name">
    <td><CopyableCode code="batch_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The batch configuration name. Required.</td>
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

Get a batch configuration for an integration account.

```sql
SELECT
id,
name,
batchGroupName,
changedTime,
createdTime,
location,
metadata,
releaseCriteria,
tags,
type
FROM azure.logic.integration_account_batch_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND integration_account_name = '{{ integration_account_name }}' -- required
AND batch_configuration_name = '{{ batch_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the batch configurations for an integration account.

```sql
SELECT
id,
name,
batchGroupName,
changedTime,
createdTime,
location,
metadata,
releaseCriteria,
tags,
type
FROM azure.logic.integration_account_batch_configurations
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

Create or update a batch configuration for an integration account.

```sql
INSERT INTO azure.logic.integration_account_batch_configurations (
location,
tags,
properties,
resource_group_name,
integration_account_name,
batch_configuration_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ integration_account_name }}',
'{{ batch_configuration_name }}',
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
- name: integration_account_batch_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the integration_account_batch_configurations resource.
    - name: integration_account_name
      value: "{{ integration_account_name }}"
      description: Required parameter for the integration_account_batch_configurations resource.
    - name: batch_configuration_name
      value: "{{ batch_configuration_name }}"
      description: Required parameter for the integration_account_batch_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the integration_account_batch_configurations resource.
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
        The batch configuration properties. Required.
      value:
        createdTime: "{{ createdTime }}"
        changedTime: "{{ changedTime }}"
        metadata: "{{ metadata }}"
        batchGroupName: "{{ batchGroupName }}"
        releaseCriteria:
          messageCount: {{ messageCount }}
          batchSize: {{ batchSize }}
          recurrence:
            frequency: "{{ frequency }}"
            interval: {{ interval }}
            startTime: "{{ startTime }}"
            endTime: "{{ endTime }}"
            timeZone: "{{ timeZone }}"
            schedule:
              minutes:
                - {{ minutes }}
              hours:
                - {{ hours }}
              weekDays:
                - "{{ weekDays }}"
              monthDays:
                - {{ monthDays }}
              monthlyOccurrences:
                - day: "{{ day }}"
                  occurrence: {{ occurrence }}
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

Create or update a batch configuration for an integration account.

```sql
REPLACE azure.logic.integration_account_batch_configurations
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND integration_account_name = '{{ integration_account_name }}' --required
AND batch_configuration_name = '{{ batch_configuration_name }}' --required
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

Delete a batch configuration for an integration account.

```sql
DELETE FROM azure.logic.integration_account_batch_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND integration_account_name = '{{ integration_account_name }}' --required
AND batch_configuration_name = '{{ batch_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
