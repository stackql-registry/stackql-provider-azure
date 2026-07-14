--- 
title: alert_rule_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rule_resources
  - database_watcher
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

Creates, updates, deletes, gets or lists an <code>alert_rule_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alert_rule_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.database_watcher.alert_rule_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="alertRuleResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the alert rule resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="alertRuleTemplateId" /></td>
    <td><code>string</code></td>
    <td>The template ID associated with alert rule resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="alertRuleTemplateVersion" /></td>
    <td><code>string</code></td>
    <td>The alert rule template version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdWithProperties" /></td>
    <td><code>string</code></td>
    <td>The properties with which the alert rule resource was created. Required. Known values are: "CreatedWithActionGroup" and "None". (CreatedWithActionGroup, None)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the alert rule resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the alert rule resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_parent">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="alertRuleResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the alert rule resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="alertRuleTemplateId" /></td>
    <td><code>string</code></td>
    <td>The template ID associated with alert rule resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="alertRuleTemplateVersion" /></td>
    <td><code>string</code></td>
    <td>The alert rule template version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdWithProperties" /></td>
    <td><code>string</code></td>
    <td>The properties with which the alert rule resource was created. Required. Known values are: "CreatedWithActionGroup" and "None". (CreatedWithActionGroup, None)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the alert rule resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the alert rule resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-alert_rule_resource_name"><code>alert_rule_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AlertRuleResource.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AlertRuleResource resources by Watcher.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-alert_rule_resource_name"><code>alert_rule_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a AlertRuleResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-alert_rule_resource_name"><code>alert_rule_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a AlertRuleResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-alert_rule_resource_name"><code>alert_rule_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a AlertRuleResource.</td>
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
<tr id="parameter-alert_rule_resource_name">
    <td><CopyableCode code="alert_rule_resource_name" /></td>
    <td><code>string</code></td>
    <td>The alert rule proxy resource name. Required.</td>
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
<tr id="parameter-watcher_name">
    <td><CopyableCode code="watcher_name" /></td>
    <td><code>string</code></td>
    <td>The database watcher name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
<TabItem value="get">

Get a AlertRuleResource.

```sql
SELECT
id,
name,
alertRuleResourceId,
alertRuleTemplateId,
alertRuleTemplateVersion,
createdWithProperties,
creationTime,
provisioningState,
systemData,
type
FROM azure.database_watcher.alert_rule_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND watcher_name = '{{ watcher_name }}' -- required
AND alert_rule_resource_name = '{{ alert_rule_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

List AlertRuleResource resources by Watcher.

```sql
SELECT
id,
name,
alertRuleResourceId,
alertRuleTemplateId,
alertRuleTemplateVersion,
createdWithProperties,
creationTime,
provisioningState,
systemData,
type
FROM azure.database_watcher.alert_rule_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND watcher_name = '{{ watcher_name }}' -- required
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

Create a AlertRuleResource.

```sql
INSERT INTO azure.database_watcher.alert_rule_resources (
properties,
resource_group_name,
watcher_name,
alert_rule_resource_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ watcher_name }}',
'{{ alert_rule_resource_name }}',
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
- name: alert_rule_resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the alert_rule_resources resource.
    - name: watcher_name
      value: "{{ watcher_name }}"
      description: Required parameter for the alert_rule_resources resource.
    - name: alert_rule_resource_name
      value: "{{ alert_rule_resource_name }}"
      description: Required parameter for the alert_rule_resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the alert_rule_resources resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        alertRuleResourceId: "{{ alertRuleResourceId }}"
        createdWithProperties: "{{ createdWithProperties }}"
        creationTime: "{{ creationTime }}"
        provisioningState: "{{ provisioningState }}"
        alertRuleTemplateId: "{{ alertRuleTemplateId }}"
        alertRuleTemplateVersion: "{{ alertRuleTemplateVersion }}"
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

Create a AlertRuleResource.

```sql
REPLACE azure.database_watcher.alert_rule_resources
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND watcher_name = '{{ watcher_name }}' --required
AND alert_rule_resource_name = '{{ alert_rule_resource_name }}' --required
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

Delete a AlertRuleResource.

```sql
DELETE FROM azure.database_watcher.alert_rule_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND watcher_name = '{{ watcher_name }}' --required
AND alert_rule_resource_name = '{{ alert_rule_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
