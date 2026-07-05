--- 
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets
  - consumption
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

Creates, updates, deletes, gets or lists a <code>budgets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="budgets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.budgets" /></td></tr>
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
    <td><CopyableCode code="amount" /></td>
    <td><code>number</code></td>
    <td>The total amount of cost to track with the budget. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the budget, whether the budget tracks cost or usage. Required. "Cost" (Cost)</td>
</tr>
<tr>
    <td><CopyableCode code="currentSpend" /></td>
    <td><code>object</code></td>
    <td>The current amount of cost which is being tracked for a budget.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="filter" /></td>
    <td><code>object</code></td>
    <td>May be used to filter budgets by user-specified dimensions and/or tags.</td>
</tr>
<tr>
    <td><CopyableCode code="forecastSpend" /></td>
    <td><code>object</code></td>
    <td>The forecasted cost which is being tracked for a budget.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>object</code></td>
    <td>Dictionary of notifications associated with the budget. Budget can have up to five notifications.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGrain" /></td>
    <td><code>string</code></td>
    <td>The time covered by a budget. Tracking of the amount will be reset based on the time grain. BillingMonth, BillingQuarter, and BillingAnnual are only supported by WD customers. Required. Known values are: "Monthly", "Quarterly", "Annually", "BillingMonth", "BillingQuarter", and "BillingAnnual". (Monthly, Quarterly, Annually, BillingMonth, BillingQuarter, BillingAnnual)</td>
</tr>
<tr>
    <td><CopyableCode code="timePeriod" /></td>
    <td><code>object</code></td>
    <td>Has start and end date of the budget. The start date must be first of the month and should be less than the end date. Budget start date must be on or after June 1, 2017. Future start date should not be more than twelve months. Past start date should be selected within the timegrain period. There are no restrictions on the end date. Required.</td>
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
    <td><CopyableCode code="amount" /></td>
    <td><code>number</code></td>
    <td>The total amount of cost to track with the budget. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the budget, whether the budget tracks cost or usage. Required. "Cost" (Cost)</td>
</tr>
<tr>
    <td><CopyableCode code="currentSpend" /></td>
    <td><code>object</code></td>
    <td>The current amount of cost which is being tracked for a budget.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="filter" /></td>
    <td><code>object</code></td>
    <td>May be used to filter budgets by user-specified dimensions and/or tags.</td>
</tr>
<tr>
    <td><CopyableCode code="forecastSpend" /></td>
    <td><code>object</code></td>
    <td>The forecasted cost which is being tracked for a budget.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>object</code></td>
    <td>Dictionary of notifications associated with the budget. Budget can have up to five notifications.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGrain" /></td>
    <td><code>string</code></td>
    <td>The time covered by a budget. Tracking of the amount will be reset based on the time grain. BillingMonth, BillingQuarter, and BillingAnnual are only supported by WD customers. Required. Known values are: "Monthly", "Quarterly", "Annually", "BillingMonth", "BillingQuarter", and "BillingAnnual". (Monthly, Quarterly, Annually, BillingMonth, BillingQuarter, BillingAnnual)</td>
</tr>
<tr>
    <td><CopyableCode code="timePeriod" /></td>
    <td><code>object</code></td>
    <td>Has start and end date of the budget. The start date must be first of the month and should be less than the end date. Budget start date must be on or after June 1, 2017. Future start date should not be more than twelve months. Past start date should be selected within the timegrain period. There are no restrictions on the end date. Required.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-budget_name"><code>budget_name</code></a></td>
    <td></td>
    <td>Gets the budget for the scope by budget name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Lists all budgets for the defined scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-budget_name"><code>budget_name</code></a></td>
    <td></td>
    <td>The operation to create or update a budget. You can optionally provide an eTag if desired as a form of concurrency control. To obtain the latest eTag for a given budget, perform a get operation prior to your put operation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-budget_name"><code>budget_name</code></a></td>
    <td></td>
    <td>The operation to create or update a budget. You can optionally provide an eTag if desired as a form of concurrency control. To obtain the latest eTag for a given budget, perform a get operation prior to your put operation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-budget_name"><code>budget_name</code></a></td>
    <td></td>
    <td>The operation to delete a budget.</td>
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
<tr id="parameter-budget_name">
    <td><CopyableCode code="budget_name" /></td>
    <td><code>string</code></td>
    <td>Budget Name. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
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

Gets the budget for the scope by budget name.

```sql
SELECT
id,
name,
amount,
category,
currentSpend,
eTag,
filter,
forecastSpend,
notifications,
systemData,
timeGrain,
timePeriod,
type
FROM azure.consumption.budgets
WHERE scope = '{{ scope }}' -- required
AND budget_name = '{{ budget_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all budgets for the defined scope.

```sql
SELECT
id,
name,
amount,
category,
currentSpend,
eTag,
filter,
forecastSpend,
notifications,
systemData,
timeGrain,
timePeriod,
type
FROM azure.consumption.budgets
WHERE scope = '{{ scope }}' -- required
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

The operation to create or update a budget. You can optionally provide an eTag if desired as a form of concurrency control. To obtain the latest eTag for a given budget, perform a get operation prior to your put operation.

```sql
INSERT INTO azure.consumption.budgets (
properties,
eTag,
scope,
budget_name
)
SELECT 
'{{ properties }}',
'{{ eTag }}',
'{{ scope }}',
'{{ budget_name }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: budgets
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the budgets resource.
    - name: budget_name
      value: "{{ budget_name }}"
      description: Required parameter for the budgets resource.
    - name: properties
      description: |
        The properties of the budget.
      value:
        category: "{{ category }}"
        amount: {{ amount }}
        timeGrain: "{{ timeGrain }}"
        timePeriod:
          startDate: "{{ startDate }}"
          endDate: "{{ endDate }}"
        filter:
          and:
            - dimensions:
                name: "{{ name }}"
                operator: "{{ operator }}"
                values:
                  - "{{ values }}"
              tags:
                name: "{{ name }}"
                operator: "{{ operator }}"
                values:
                  - "{{ values }}"
          dimensions:
            name: "{{ name }}"
            operator: "{{ operator }}"
            values:
              - "{{ values }}"
          tags:
            name: "{{ name }}"
            operator: "{{ operator }}"
            values:
              - "{{ values }}"
        currentSpend:
          amount: {{ amount }}
          unit: "{{ unit }}"
        notifications: "{{ notifications }}"
        forecastSpend:
          amount: {{ amount }}
          unit: "{{ unit }}"
    - name: eTag
      value: "{{ eTag }}"
      description: |
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
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

The operation to create or update a budget. You can optionally provide an eTag if desired as a form of concurrency control. To obtain the latest eTag for a given budget, perform a get operation prior to your put operation.

```sql
REPLACE azure.consumption.budgets
SET 
properties = '{{ properties }}',
eTag = '{{ eTag }}'
WHERE 
scope = '{{ scope }}' --required
AND budget_name = '{{ budget_name }}' --required
RETURNING
id,
name,
eTag,
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

The operation to delete a budget.

```sql
DELETE FROM azure.consumption.budgets
WHERE scope = '{{ scope }}' --required
AND budget_name = '{{ budget_name }}' --required
;
```
</TabItem>
</Tabs>
