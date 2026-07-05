--- 
title: monitored_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_subscriptions
  - datadog
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

Creates, updates, deletes, gets or lists a <code>monitored_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="monitored_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.monitored_subscriptions" /></td></tr>
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
    <td>The id of the monitored subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the monitored subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoredSubscriptionList" /></td>
    <td><code>array</code></td>
    <td>List of subscriptions and the state of the monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The operation for the patch on the resource. Known values are: "AddBegin", "AddComplete", "DeleteBegin", "DeleteComplete", and "Active".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitored subscription resource.</td>
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
    <td>The id of the monitored subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the monitored subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoredSubscriptionList" /></td>
    <td><code>array</code></td>
    <td>List of subscriptions and the state of the monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The operation for the patch on the resource. Known values are: "AddBegin", "AddComplete", "DeleteBegin", "DeleteComplete", and "Active".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitored subscription resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the subscriptions currently being monitored by the Datadog monitor resource. List the subscriptions currently being monitored by the Datadog monitor resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the subscriptions currently being monitored by the Datadog monitor resource. List the subscriptions currently being monitored by the Datadog monitor resource.</td>
</tr>
<tr>
    <td><a href="#createor_update"><CopyableCode code="createor_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add the subscriptions that should be monitored by the Datadog monitor resource. Add the subscriptions that should be monitored by the Datadog monitor resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the subscriptions that are being monitored by the Datadog monitor resource. Updates the subscriptions that are being monitored by the Datadog monitor resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the subscriptions that are being monitored by the Datadog monitor resource. Updates the subscriptions that are being monitored by the Datadog monitor resource.</td>
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
    <td>Configuration name. Required.</td>
</tr>
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

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

List the subscriptions currently being monitored by the Datadog monitor resource. List the subscriptions currently being monitored by the Datadog monitor resource.

```sql
SELECT
id,
name,
monitoredSubscriptionList,
operation,
type
FROM azure_isv.datadog.monitored_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND configuration_name = '{{ configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the subscriptions currently being monitored by the Datadog monitor resource. List the subscriptions currently being monitored by the Datadog monitor resource.

```sql
SELECT
id,
name,
monitoredSubscriptionList,
operation,
type
FROM azure_isv.datadog.monitored_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createor_update"
    values={[
        { label: 'createor_update', value: 'createor_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createor_update">

Add the subscriptions that should be monitored by the Datadog monitor resource. Add the subscriptions that should be monitored by the Datadog monitor resource.

```sql
INSERT INTO azure_isv.datadog.monitored_subscriptions (
properties,
resource_group_name,
monitor_name,
configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
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
- name: monitored_subscriptions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the monitored_subscriptions resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the monitored_subscriptions resource.
    - name: configuration_name
      value: "{{ configuration_name }}"
      description: Required parameter for the monitored_subscriptions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the monitored_subscriptions resource.
    - name: properties
      description: |
        The request to update subscriptions needed to be monitored by the Datadog monitor resource.
      value:
        operation: "{{ operation }}"
        monitoredSubscriptionList:
          - subscriptionId: "{{ subscriptionId }}"
            status: "{{ status }}"
            error: "{{ error }}"
            tagRules:
              provisioningState: "{{ provisioningState }}"
              logRules:
                sendAadLogs: {{ sendAadLogs }}
                sendSubscriptionLogs: {{ sendSubscriptionLogs }}
                sendResourceLogs: {{ sendResourceLogs }}
                filteringTags:
                  - name: "{{ name }}"
                    value: "{{ value }}"
                    action: "{{ action }}"
              metricRules:
                filteringTags:
                  - name: "{{ name }}"
                    value: "{{ value }}"
                    action: "{{ action }}"
              automuting: {{ automuting }}
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

Updates the subscriptions that are being monitored by the Datadog monitor resource. Updates the subscriptions that are being monitored by the Datadog monitor resource.

```sql
UPDATE azure_isv.datadog.monitored_subscriptions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND configuration_name = '{{ configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Updates the subscriptions that are being monitored by the Datadog monitor resource. Updates the subscriptions that are being monitored by the Datadog monitor resource.

```sql
DELETE FROM azure_isv.datadog.monitored_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND configuration_name = '{{ configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
