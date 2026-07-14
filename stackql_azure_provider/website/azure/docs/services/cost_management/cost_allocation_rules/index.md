--- 
title: cost_allocation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cost_allocation_rules
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>cost_allocation_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cost_allocation_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.cost_allocation_rules" /></td></tr>
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
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the rule was created. Rules that change cost for the same resource are applied in order of creation.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of a cost allocation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Resource information for the cost allocation rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the rule. Required. Known values are: "NotActive", "Active", and "Processing". (NotActive, Active, Processing)</td>
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
<tr>
    <td><CopyableCode code="updatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the rule was last updated.</td>
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
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the rule was created. Rules that change cost for the same resource are applied in order of creation.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of a cost allocation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Resource information for the cost allocation rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the rule. Required. Known values are: "NotActive", "Active", and "Processing". (NotActive, Active, Processing)</td>
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
<tr>
    <td><CopyableCode code="updatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the rule was last updated.</td>
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
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a></td>
    <td></td>
    <td>Get a cost allocation rule by rule name and billing account or enterprise enrollment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td></td>
    <td>Get the list of all cost allocation rules for a billing account or enterprise enrollment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a></td>
    <td></td>
    <td>Create/Update a rule to allocate cost between different resources within a billing account or enterprise enrollment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a></td>
    <td></td>
    <td>Create/Update a rule to allocate cost between different resources within a billing account or enterprise enrollment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a></td>
    <td></td>
    <td>Delete cost allocation rule for billing account or enterprise enrollment.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td></td>
    <td>Checks availability and correctness of a name for a cost allocation rule.</td>
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
<tr id="parameter-billing_account_id">
    <td><CopyableCode code="billing_account_id" /></td>
    <td><code>string</code></td>
    <td>BillingAccount ID. Required.</td>
</tr>
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>Cost allocation rule name. The name cannot include spaces or any non alphanumeric characters other than '_' and '-'. The max length is 260 characters. Required.</td>
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

Get a cost allocation rule by rule name and billing account or enterprise enrollment.

```sql
SELECT
id,
name,
createdDate,
description,
details,
status,
systemData,
type,
updatedDate
FROM azure.cost_management.cost_allocation_rules
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND rule_name = '{{ rule_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the list of all cost allocation rules for a billing account or enterprise enrollment.

```sql
SELECT
id,
name,
createdDate,
description,
details,
status,
systemData,
type,
updatedDate
FROM azure.cost_management.cost_allocation_rules
WHERE billing_account_id = '{{ billing_account_id }}' -- required
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

Create/Update a rule to allocate cost between different resources within a billing account or enterprise enrollment.

```sql
INSERT INTO azure.cost_management.cost_allocation_rules (
properties,
billing_account_id,
rule_name
)
SELECT 
'{{ properties }}',
'{{ billing_account_id }}',
'{{ rule_name }}'
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
- name: cost_allocation_rules
  props:
    - name: billing_account_id
      value: "{{ billing_account_id }}"
      description: Required parameter for the cost_allocation_rules resource.
    - name: rule_name
      value: "{{ rule_name }}"
      description: Required parameter for the cost_allocation_rules resource.
    - name: properties
      description: |
        Cost allocation rule properties.
      value:
        description: "{{ description }}"
        details:
          sourceResources:
            - resourceType: "{{ resourceType }}"
              name: "{{ name }}"
              values: "{{ values }}"
          targetResources:
            - resourceType: "{{ resourceType }}"
              name: "{{ name }}"
              values: "{{ values }}"
              policyType: "{{ policyType }}"
        status: "{{ status }}"
        createdDate: "{{ createdDate }}"
        updatedDate: "{{ updatedDate }}"
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

Create/Update a rule to allocate cost between different resources within a billing account or enterprise enrollment.

```sql
REPLACE azure.cost_management.cost_allocation_rules
SET 
properties = '{{ properties }}'
WHERE 
billing_account_id = '{{ billing_account_id }}' --required
AND rule_name = '{{ rule_name }}' --required
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

Delete cost allocation rule for billing account or enterprise enrollment.

```sql
DELETE FROM azure.cost_management.cost_allocation_rules
WHERE billing_account_id = '{{ billing_account_id }}' --required
AND rule_name = '{{ rule_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="check_name_availability">

Checks availability and correctness of a name for a cost allocation rule.

```sql
EXEC azure.cost_management.cost_allocation_rules.check_name_availability 
@billing_account_id='{{ billing_account_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
