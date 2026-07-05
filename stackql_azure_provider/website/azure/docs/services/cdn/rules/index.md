--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - cdn
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

Creates, updates, deletes, gets or lists a <code>rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_rule_set', value: 'list_by_rule_set' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>A list of actions that are executed when all the conditions of a rule are satisfied.</td>
</tr>
<tr>
    <td><CopyableCode code="conditions" /></td>
    <td><code>array</code></td>
    <td>A list of conditions that must be matched for the actions to be executed.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="matchProcessingBehavior" /></td>
    <td><code>string</code></td>
    <td>If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue. Known values are: "Continue" and "Stop". (Continue, Stop)</td>
</tr>
<tr>
    <td><CopyableCode code="order" /></td>
    <td><code>integer</code></td>
    <td>The order in which the rules are applied for the endpoint. Possible values &#123;0,1,2,3,………&#125;. A rule with a lesser order will be applied before a rule with a greater order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleSetName" /></td>
    <td><code>string</code></td>
    <td>The name of the rule set containing the rule.</td>
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
<TabItem value="list_by_rule_set">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>A list of actions that are executed when all the conditions of a rule are satisfied.</td>
</tr>
<tr>
    <td><CopyableCode code="conditions" /></td>
    <td><code>array</code></td>
    <td>A list of conditions that must be matched for the actions to be executed.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="matchProcessingBehavior" /></td>
    <td><code>string</code></td>
    <td>If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue. Known values are: "Continue" and "Stop". (Continue, Stop)</td>
</tr>
<tr>
    <td><CopyableCode code="order" /></td>
    <td><code>integer</code></td>
    <td>The order in which the rules are applied for the endpoint. Possible values &#123;0,1,2,3,………&#125;. A rule with a lesser order will be applied before a rule with a greater order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleSetName" /></td>
    <td><code>string</code></td>
    <td>The name of the rule set containing the rule.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing delivery rule within a rule set.</td>
</tr>
<tr>
    <td><a href="#list_by_rule_set"><CopyableCode code="list_by_rule_set" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the existing delivery rules within a rule set.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new delivery rule within the specified rule set.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing delivery rule within a rule set.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing delivery rule within a rule set.</td>
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
    <td>Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>Name of the delivery rule which is unique within the endpoint. Required.</td>
</tr>
<tr id="parameter-rule_set_name">
    <td><CopyableCode code="rule_set_name" /></td>
    <td><code>string</code></td>
    <td>Name of the rule set under the profile which is unique globally. Required.</td>
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
        { label: 'list_by_rule_set', value: 'list_by_rule_set' }
    ]}
>
<TabItem value="get">

Gets an existing delivery rule within a rule set.

```sql
SELECT
id,
name,
actions,
conditions,
deploymentStatus,
matchProcessingBehavior,
order,
provisioningState,
ruleSetName,
systemData,
type
FROM azure.cdn.rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND rule_set_name = '{{ rule_set_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_rule_set">

Lists all of the existing delivery rules within a rule set.

```sql
SELECT
id,
name,
actions,
conditions,
deploymentStatus,
matchProcessingBehavior,
order,
provisioningState,
ruleSetName,
systemData,
type
FROM azure.cdn.rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND rule_set_name = '{{ rule_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new delivery rule within the specified rule set.

```sql
INSERT INTO azure.cdn.rules (
properties,
resource_group_name,
profile_name,
rule_set_name,
rule_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ rule_set_name }}',
'{{ rule_name }}',
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
- name: rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the rules resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the rules resource.
    - name: rule_set_name
      value: "{{ rule_set_name }}"
      description: Required parameter for the rules resource.
    - name: rule_name
      value: "{{ rule_name }}"
      description: Required parameter for the rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the rules resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the Rules to create.
      value:
        ruleSetName: "{{ ruleSetName }}"
        order: {{ order }}
        conditions:
          - name: "{{ name }}"
        actions:
          - name: "{{ name }}"
        matchProcessingBehavior: "{{ matchProcessingBehavior }}"
        provisioningState: "{{ provisioningState }}"
        deploymentStatus: "{{ deploymentStatus }}"
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

Updates an existing delivery rule within a rule set.

```sql
UPDATE azure.cdn.rules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND rule_set_name = '{{ rule_set_name }}' --required
AND rule_name = '{{ rule_name }}' --required
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

Deletes an existing delivery rule within a rule set.

```sql
DELETE FROM azure.cdn.rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND rule_set_name = '{{ rule_set_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
