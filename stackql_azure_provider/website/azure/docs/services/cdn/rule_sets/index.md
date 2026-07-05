--- 
title: rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_sets
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

Creates, updates, deletes, gets or lists a <code>rule_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rule_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.rule_sets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_profile', value: 'list_by_profile' }
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
    <td><CopyableCode code="batchMode" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether rule set is in batch mode. When batch mode is enabled, rules will be processed in a batch along with the rule set. When batch mode is disabled, rules would need to be processed independently. This property can only be set during rule set creation and cannot be updated later. For switching modes, a new rule set needs to be created with the desired mode and rules need to be migrated to the new rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="profileName" /></td>
    <td><code>string</code></td>
    <td>The name of the profile which holds the rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>A list of rules that are part of this rule set provided the rule set is in batch mode. This property will be ignored if the rule set is not in batch mode.</td>
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
<TabItem value="list_by_profile">

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
    <td><CopyableCode code="batchMode" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether rule set is in batch mode. When batch mode is enabled, rules will be processed in a batch along with the rule set. When batch mode is disabled, rules would need to be processed independently. This property can only be set during rule set creation and cannot be updated later. For switching modes, a new rule set needs to be created with the desired mode and rules need to be migrated to the new rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="profileName" /></td>
    <td><code>string</code></td>
    <td>The name of the profile which holds the rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>A list of rules that are part of this rule set provided the rule set is in batch mode. This property will be ignored if the rule set is not in batch mode.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile.</td>
</tr>
<tr>
    <td><a href="#list_by_profile"><CopyableCode code="list_by_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists existing AzureFrontDoor rule sets within a profile.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or update a batch rule set within the specified profile along with the rules associate to it.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile.</td>
</tr>
<tr>
    <td><a href="#list_resource_usage"><CopyableCode code="list_resource_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the quota and actual usage of endpoints under the given Azure Front Door profile.</td>
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
        { label: 'list_by_profile', value: 'list_by_profile' }
    ]}
>
<TabItem value="get">

Gets an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile.

```sql
SELECT
id,
name,
batchMode,
deploymentStatus,
profileName,
provisioningState,
rules,
systemData,
type
FROM azure.cdn.rule_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND rule_set_name = '{{ rule_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_profile">

Lists existing AzureFrontDoor rule sets within a profile.

```sql
SELECT
id,
name,
batchMode,
deploymentStatus,
profileName,
provisioningState,
rules,
systemData,
type
FROM azure.cdn.rule_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
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

Creates or update a batch rule set within the specified profile along with the rules associate to it.

```sql
INSERT INTO azure.cdn.rule_sets (
properties,
resource_group_name,
profile_name,
rule_set_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ rule_set_name }}',
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
- name: rule_sets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the rule_sets resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the rule_sets resource.
    - name: rule_set_name
      value: "{{ rule_set_name }}"
      description: Required parameter for the rule_sets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the rule_sets resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the Rule Set to create.
      value:
        provisioningState: "{{ provisioningState }}"
        deploymentStatus: "{{ deploymentStatus }}"
        profileName: "{{ profileName }}"
        batchMode: {{ batchMode }}
        rules:
          - ruleName: "{{ ruleName }}"
            ruleSetName: "{{ ruleSetName }}"
            order: {{ order }}
            conditions: "{{ conditions }}"
            actions: "{{ actions }}"
            matchProcessingBehavior: "{{ matchProcessingBehavior }}"
`}</CodeBlock>

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

Deletes an existing AzureFrontDoor rule set with the specified rule set name under the specified subscription, resource group and profile.

```sql
DELETE FROM azure.cdn.rule_sets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND rule_set_name = '{{ rule_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_resource_usage"
    values={[
        { label: 'list_resource_usage', value: 'list_resource_usage' }
    ]}
>
<TabItem value="list_resource_usage">

Checks the quota and actual usage of endpoints under the given Azure Front Door profile.

```sql
EXEC azure.cdn.rule_sets.list_resource_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@rule_set_name='{{ rule_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
