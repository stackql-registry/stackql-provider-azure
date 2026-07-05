--- 
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - advisor
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.advisor.configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
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
    <td>The resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="digests" /></td>
    <td><code>array</code></td>
    <td>Advisor digest configuration. Valid only for subscriptions.</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>boolean</code></td>
    <td>Exclude the resource from Advisor evaluations. Valid values: False (default) or True.</td>
</tr>
<tr>
    <td><CopyableCode code="lowCpuThreshold" /></td>
    <td><code>string</code></td>
    <td>Minimum percentage threshold for Advisor low CPU utilization evaluation. Valid only for subscriptions. Valid values: 5 (default), 10, 15 or 20. Known values are: "5", "10", "15", and "20".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>The resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="digests" /></td>
    <td><code>array</code></td>
    <td>Advisor digest configuration. Valid only for subscriptions.</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>boolean</code></td>
    <td>Exclude the resource from Advisor evaluations. Valid values: False (default) or True.</td>
</tr>
<tr>
    <td><CopyableCode code="lowCpuThreshold" /></td>
    <td><code>string</code></td>
    <td>Minimum percentage threshold for Advisor low CPU utilization evaluation. Valid only for subscriptions. Valid values: 5 (default), 10, 15 or 20. Known values are: "5", "10", "15", and "20".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve Azure Advisor configurations. Retrieve Azure Advisor configurations.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve Azure Advisor configurations. Retrieve Azure Advisor configurations and also retrieve configurations of contained resource groups.</td>
</tr>
<tr>
    <td><a href="#create_in_resource_group"><CopyableCode code="create_in_resource_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create/Overwrite Azure Advisor configuration. Create/Overwrite Azure Advisor configuration.</td>
</tr>
<tr>
    <td><a href="#create_in_subscription"><CopyableCode code="create_in_subscription" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create/Overwrite Azure Advisor configuration. Create/Overwrite Azure Advisor configuration and also delete all configurations of contained resource groups.</td>
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
<tr id="parameter-configuration_name">
    <td><CopyableCode code="configuration_name" /></td>
    <td><code>string</code></td>
    <td>Advisor configuration name. Value must be 'default'. "default" Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure resource group. Required.</td>
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
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_by_resource_group">

Retrieve Azure Advisor configurations. Retrieve Azure Advisor configurations.

```sql
SELECT
id,
name,
digests,
exclude,
lowCpuThreshold,
type
FROM azure.advisor.configurations
WHERE resource_group = '{{ resource_group }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Retrieve Azure Advisor configurations. Retrieve Azure Advisor configurations and also retrieve configurations of contained resource groups.

```sql
SELECT
id,
name,
digests,
exclude,
lowCpuThreshold,
type
FROM azure.advisor.configurations
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_in_resource_group"
    values={[
        { label: 'create_in_resource_group', value: 'create_in_resource_group' },
        { label: 'create_in_subscription', value: 'create_in_subscription' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_in_resource_group">

Create/Overwrite Azure Advisor configuration. Create/Overwrite Azure Advisor configuration.

```sql
INSERT INTO azure.advisor.configurations (
properties,
configuration_name,
resource_group,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ configuration_name }}',
'{{ resource_group }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="create_in_subscription">

Create/Overwrite Azure Advisor configuration. Create/Overwrite Azure Advisor configuration and also delete all configurations of contained resource groups.

```sql
INSERT INTO azure.advisor.configurations (
properties,
configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ configuration_name }}',
'{{ subscription_id }}'
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
- name: configurations
  props:
    - name: configuration_name
      value: "{{ configuration_name }}"
      description: Required parameter for the configurations resource.
    - name: resource_group
      value: "{{ resource_group }}"
      description: Required parameter for the configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the configurations resource.
    - name: properties
      value:
        exclude: {{ exclude }}
        lowCpuThreshold: "{{ lowCpuThreshold }}"
        digests:
          - name: "{{ name }}"
            actionGroupResourceId: "{{ actionGroupResourceId }}"
            frequency: {{ frequency }}
            categories: "{{ categories }}"
            language: "{{ language }}"
            state: "{{ state }}"
`}</CodeBlock>

</TabItem>
</Tabs>
