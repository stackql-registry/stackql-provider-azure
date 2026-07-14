--- 
title: outbound_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_rule
  - cognitive_services
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

Creates, updates, deletes, gets or lists an <code>outbound_rule</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="outbound_rule" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.outbound_rule" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of a managed network Outbound Rule of a cognitive services account. Known values are: "Required", "Recommended", "UserDefined", and "Dependency". (Required, Recommended, UserDefined, Dependency)</td>
</tr>
<tr>
    <td><CopyableCode code="errorInformation" /></td>
    <td><code>string</code></td>
    <td>Error information about an outbound rule of a cognitive services account if RuleStatus is failed.</td>
</tr>
<tr>
    <td><CopyableCode code="parentRuleNames" /></td>
    <td><code>array</code></td>
    <td>:vartype parent_rule_names: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Type of a managed network Outbound Rule of a cognitive services account. Known values are: "Inactive", "Active", "Provisioning", "Deleting", and "Failed". (Inactive, Active, Provisioning, Deleting, Failed)</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of a managed network Outbound Rule of a cognitive services account. Known values are: "Required", "Recommended", "UserDefined", and "Dependency". (Required, Recommended, UserDefined, Dependency)</td>
</tr>
<tr>
    <td><CopyableCode code="errorInformation" /></td>
    <td><code>string</code></td>
    <td>Error information about an outbound rule of a cognitive services account if RuleStatus is failed.</td>
</tr>
<tr>
    <td><CopyableCode code="parentRuleNames" /></td>
    <td><code>array</code></td>
    <td>:vartype parent_rule_names: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Type of a managed network Outbound Rule of a cognitive services account. Known values are: "Inactive", "Active", "Provisioning", "Deleting", and "Failed". (Inactive, Active, Provisioning, Deleting, Failed)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-managed_network_name"><code>managed_network_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The GET API for retrieving a single outbound rule of the managed network associated with the cognitive services account. The GET API for retrieving a single outbound rule of the managed network associated with the cognitive services account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-managed_network_name"><code>managed_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The GET API for retrieving the list of outbound rules of the managed network associated with the cognitive services account. The GET API for retrieving the list of outbound rules of the managed network associated with the cognitive services account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-managed_network_name"><code>managed_network_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account. The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-managed_network_name"><code>managed_network_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account. The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-managed_network_name"><code>managed_network_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The DELETE API for deleting a single outbound rule of the managed network associated with the cognitive services account. The DELETE API for deleting a single outbound rule of the managed network associated with the cognitive services account.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of Cognitive Services account. Required.</td>
</tr>
<tr id="parameter-managed_network_name">
    <td><CopyableCode code="managed_network_name" /></td>
    <td><code>string</code></td>
    <td>Name of the managedNetwork associated with the cognitive services account. Only 'default' is supported. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>Name of the cognitive services account managed network outbound rule. Required.</td>
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

The GET API for retrieving a single outbound rule of the managed network associated with the cognitive services account. The GET API for retrieving a single outbound rule of the managed network associated with the cognitive services account.

```sql
SELECT
id,
name,
category,
errorInformation,
parentRuleNames,
status,
systemData,
type
FROM azure.cognitive_services.outbound_rule
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND managed_network_name = '{{ managed_network_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The GET API for retrieving the list of outbound rules of the managed network associated with the cognitive services account. The GET API for retrieving the list of outbound rules of the managed network associated with the cognitive services account.

```sql
SELECT
id,
name,
category,
errorInformation,
parentRuleNames,
status,
systemData,
type
FROM azure.cognitive_services.outbound_rule
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND managed_network_name = '{{ managed_network_name }}' -- required
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

The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account. The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account.

```sql
INSERT INTO azure.cognitive_services.outbound_rule (
properties,
resource_group_name,
account_name,
managed_network_name,
rule_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ managed_network_name }}',
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
- name: outbound_rule
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the outbound_rule resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the outbound_rule resource.
    - name: managed_network_name
      value: "{{ managed_network_name }}"
      description: Required parameter for the outbound_rule resource.
    - name: rule_name
      value: "{{ rule_name }}"
      description: Required parameter for the outbound_rule resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the outbound_rule resource.
    - name: properties
      description: |
        Outbound Rule for the managed network of a cognitive services account. Required.
      value:
        category: "{{ category }}"
        status: "{{ status }}"
        type: "{{ type }}"
        errorInformation: "{{ errorInformation }}"
        parentRuleNames:
          - "{{ parentRuleNames }}"
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

The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account. The PUT API for creating or updating a single outbound rule of the managed network associated with the cognitive services account.

```sql
REPLACE azure.cognitive_services.outbound_rule
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND managed_network_name = '{{ managed_network_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

The DELETE API for deleting a single outbound rule of the managed network associated with the cognitive services account. The DELETE API for deleting a single outbound rule of the managed network associated with the cognitive services account.

```sql
DELETE FROM azure.cognitive_services.outbound_rule
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND managed_network_name = '{{ managed_network_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
