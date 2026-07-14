--- 
title: goal_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - goal_templates
  - resilience_management
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

Creates, updates, deletes, gets or lists a <code>goal_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="goal_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resilience_management.goal_templates" /></td></tr>
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
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors encountered during the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="goalType" /></td>
    <td><code>string</code></td>
    <td>Type of Goal Template created by customer. Required. "Resiliency" (Resiliency)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="regionalRecoveryPointObjective" /></td>
    <td><code>string</code></td>
    <td>Regional recovery point objective specified by customer. eg, PT15M for 15 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="regionalRecoveryTimeObjective" /></td>
    <td><code>string</code></td>
    <td>Regional recovery time objective specified by customer. eg, PT15M for 15 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="requireDisasterRecovery" /></td>
    <td><code>string</code></td>
    <td>Option specified by customer under disaster recovery section of goal template. Known values are: "NotRequired" and "Required". (NotRequired, Required)</td>
</tr>
<tr>
    <td><CopyableCode code="requireHighAvailability" /></td>
    <td><code>string</code></td>
    <td>Option specified by customer under high availability section of goal template. Known values are: "NotRequired" and "Required". (NotRequired, Required)</td>
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
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors encountered during the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="goalType" /></td>
    <td><code>string</code></td>
    <td>Type of Goal Template created by customer. Required. "Resiliency" (Resiliency)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="regionalRecoveryPointObjective" /></td>
    <td><code>string</code></td>
    <td>Regional recovery point objective specified by customer. eg, PT15M for 15 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="regionalRecoveryTimeObjective" /></td>
    <td><code>string</code></td>
    <td>Regional recovery time objective specified by customer. eg, PT15M for 15 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="requireDisasterRecovery" /></td>
    <td><code>string</code></td>
    <td>Option specified by customer under disaster recovery section of goal template. Known values are: "NotRequired" and "Required". (NotRequired, Required)</td>
</tr>
<tr>
    <td><CopyableCode code="requireHighAvailability" /></td>
    <td><code>string</code></td>
    <td>Option specified by customer under high availability section of goal template. Known values are: "NotRequired" and "Required". (NotRequired, Required)</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_template_name"><code>goal_template_name</code></a></td>
    <td></td>
    <td>Get a GoalTemplate.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List GoalTemplate resources by tenant.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_template_name"><code>goal_template_name</code></a></td>
    <td></td>
    <td>Create a GoalTemplate.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_template_name"><code>goal_template_name</code></a></td>
    <td></td>
    <td>Update a GoalTemplate.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_template_name"><code>goal_template_name</code></a></td>
    <td></td>
    <td>Create a GoalTemplate.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_template_name"><code>goal_template_name</code></a></td>
    <td></td>
    <td>Delete a GoalTemplate.</td>
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
<tr id="parameter-goal_template_name">
    <td><CopyableCode code="goal_template_name" /></td>
    <td><code>string</code></td>
    <td>The name of the goalTemplate. Required.</td>
</tr>
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip over when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Default value is None.</td>
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

Get a GoalTemplate.

```sql
SELECT
id,
name,
errorDetails,
goalType,
provisioningState,
regionalRecoveryPointObjective,
regionalRecoveryTimeObjective,
requireDisasterRecovery,
requireHighAvailability,
systemData,
type
FROM azure.resilience_management.goal_templates
WHERE service_group_name = '{{ service_group_name }}' -- required
AND goal_template_name = '{{ goal_template_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List GoalTemplate resources by tenant.

```sql
SELECT
id,
name,
errorDetails,
goalType,
provisioningState,
regionalRecoveryPointObjective,
regionalRecoveryTimeObjective,
requireDisasterRecovery,
requireHighAvailability,
systemData,
type
FROM azure.resilience_management.goal_templates
WHERE service_group_name = '{{ service_group_name }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
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

Create a GoalTemplate.

```sql
INSERT INTO azure.resilience_management.goal_templates (
properties,
service_group_name,
goal_template_name
)
SELECT 
'{{ properties }}',
'{{ service_group_name }}',
'{{ goal_template_name }}'
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
- name: goal_templates
  props:
    - name: service_group_name
      value: "{{ service_group_name }}"
      description: Required parameter for the goal_templates resource.
    - name: goal_template_name
      value: "{{ goal_template_name }}"
      description: Required parameter for the goal_templates resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        requireHighAvailability: "{{ requireHighAvailability }}"
        requireDisasterRecovery: "{{ requireDisasterRecovery }}"
        regionalRecoveryPointObjective: "{{ regionalRecoveryPointObjective }}"
        regionalRecoveryTimeObjective: "{{ regionalRecoveryTimeObjective }}"
        goalType: "{{ goalType }}"
        provisioningState: "{{ provisioningState }}"
        errorDetails:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          details:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
          additionalInfo:
            - type: "{{ type }}"
              info: "{{ info }}"
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

Update a GoalTemplate.

```sql
UPDATE azure.resilience_management.goal_templates
SET 
properties = '{{ properties }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND goal_template_name = '{{ goal_template_name }}' --required;
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

Create a GoalTemplate.

```sql
REPLACE azure.resilience_management.goal_templates
SET 
properties = '{{ properties }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND goal_template_name = '{{ goal_template_name }}' --required
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

Delete a GoalTemplate.

```sql
DELETE FROM azure.resilience_management.goal_templates
WHERE service_group_name = '{{ service_group_name }}' --required
AND goal_template_name = '{{ goal_template_name }}' --required
;
```
</TabItem>
</Tabs>
