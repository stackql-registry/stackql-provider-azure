--- 
title: monitored_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_subscriptions
  - newrelicobservability
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelicobservability.monitored_subscriptions" /></td></tr>
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
    <td><CopyableCode code="patchOperation" /></td>
    <td><code>string</code></td>
    <td>The operation for the patch on the resource. Known values are: "AddBegin", "AddComplete", "DeleteBegin", "DeleteComplete", and "Active".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
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
    <td><CopyableCode code="patchOperation" /></td>
    <td><code>string</code></td>
    <td>The operation for the patch on the resource. Known values are: "AddBegin", "AddComplete", "DeleteBegin", "DeleteComplete", and "Active".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
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
    <td>Lists all the subscriptions currently being monitored by the NewRelic monitor resource. Lists all the subscriptions currently being monitored by the NewRelic monitor resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the subscriptions currently being monitored by the NewRelic monitor resource. Lists all the subscriptions currently being monitored by the NewRelic monitor resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring. Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update subscriptions to be monitored by the New Relic monitor resource, ensuring optimal observability and performance. Update subscriptions to be monitored by the New Relic monitor resource, ensuring optimal observability and performance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring. Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete subscriptions being monitored by the New Relic monitor resource, removing their observability and monitoring capabilities. Delete subscriptions being monitored by the New Relic monitor resource, removing their observability and monitoring capabilities.</td>
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
    <td>The configuration name. Only 'default' value is supported. "default" Required.</td>
</tr>
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Monitors resource. Required.</td>
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

Lists all the subscriptions currently being monitored by the NewRelic monitor resource. Lists all the subscriptions currently being monitored by the NewRelic monitor resource.

```sql
SELECT
id,
name,
monitoredSubscriptionList,
patchOperation,
provisioningState,
type
FROM azure_isv.newrelicobservability.monitored_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND configuration_name = '{{ configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the subscriptions currently being monitored by the NewRelic monitor resource. Lists all the subscriptions currently being monitored by the NewRelic monitor resource.

```sql
SELECT
id,
name,
monitoredSubscriptionList,
patchOperation,
provisioningState,
type
FROM azure_isv.newrelicobservability.monitored_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
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

Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring. Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring.

```sql
INSERT INTO azure_isv.newrelicobservability.monitored_subscriptions (
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
        The request to update subscriptions needed to be monitored by the NewRelic monitor resource.
      value:
        patchOperation: "{{ patchOperation }}"
        monitoredSubscriptionList:
          - subscriptionId: "{{ subscriptionId }}"
            status: "{{ status }}"
            error: "{{ error }}"
            tagRules:
              provisioningState: "{{ provisioningState }}"
              logRules:
                sendAadLogs: "{{ sendAadLogs }}"
                sendSubscriptionLogs: "{{ sendSubscriptionLogs }}"
                sendActivityLogs: "{{ sendActivityLogs }}"
                filteringTags:
                  - name: "{{ name }}"
                    value: "{{ value }}"
                    action: "{{ action }}"
              metricRules:
                sendMetrics: "{{ sendMetrics }}"
                filteringTags:
                  - name: "{{ name }}"
                    value: "{{ value }}"
                    action: "{{ action }}"
                userEmail: "{{ userEmail }}"
        provisioningState: "{{ provisioningState }}"
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

Update subscriptions to be monitored by the New Relic monitor resource, ensuring optimal observability and performance. Update subscriptions to be monitored by the New Relic monitor resource, ensuring optimal observability and performance.

```sql
UPDATE azure_isv.newrelicobservability.monitored_subscriptions
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring. Add subscriptions to be monitored by the New Relic monitor resource, enabling observability and monitoring.

```sql
REPLACE azure_isv.newrelicobservability.monitored_subscriptions
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

Delete subscriptions being monitored by the New Relic monitor resource, removing their observability and monitoring capabilities. Delete subscriptions being monitored by the New Relic monitor resource, removing their observability and monitoring capabilities.

```sql
DELETE FROM azure_isv.newrelicobservability.monitored_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND configuration_name = '{{ configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
