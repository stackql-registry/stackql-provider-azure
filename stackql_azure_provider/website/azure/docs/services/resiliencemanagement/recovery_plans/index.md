--- 
title: recovery_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_plans
  - resiliencemanagement
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

Creates, updates, deletes, gets or lists a <code>recovery_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recovery_plans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resiliencemanagement.recovery_plans" /></td></tr>
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
    <td>Error details associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="latestFailoverStatus" /></td>
    <td><code>object</code></td>
    <td>The status of the most recent failover operation executed.</td>
</tr>
<tr>
    <td><CopyableCode code="latestValidationStatus" /></td>
    <td><code>object</code></td>
    <td>The status of the most recent validation performed.</td>
</tr>
<tr>
    <td><CopyableCode code="planDescription" /></td>
    <td><code>string</code></td>
    <td>A description of the recovery orchestration plan. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="planState" /></td>
    <td><code>string</code></td>
    <td>The current state of the recovery orchestration plan. Known values are: "UnderEdit", "Warning", and "Ready". (UnderEdit, Warning, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="planType" /></td>
    <td><code>string</code></td>
    <td>The type of the recovery orchestration plan, which can be set during creation but cannot be changed afterward. Required. Known values are: "Regional" and "Zonal". (Regional, Zonal)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the recovery orchestration plan. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryGroupsSetting" /></td>
    <td><code>object</code></td>
    <td>Settings for the recovery orchestration groups associated with the recovery orchestration plan. Required.</td>
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
    <td>Error details associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="latestFailoverStatus" /></td>
    <td><code>object</code></td>
    <td>The status of the most recent failover operation executed.</td>
</tr>
<tr>
    <td><CopyableCode code="latestValidationStatus" /></td>
    <td><code>object</code></td>
    <td>The status of the most recent validation performed.</td>
</tr>
<tr>
    <td><CopyableCode code="planDescription" /></td>
    <td><code>string</code></td>
    <td>A description of the recovery orchestration plan. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="planState" /></td>
    <td><code>string</code></td>
    <td>The current state of the recovery orchestration plan. Known values are: "UnderEdit", "Warning", and "Ready". (UnderEdit, Warning, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="planType" /></td>
    <td><code>string</code></td>
    <td>The type of the recovery orchestration plan, which can be set during creation but cannot be changed afterward. Required. Known values are: "Regional" and "Zonal". (Regional, Zonal)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the recovery orchestration plan. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryGroupsSetting" /></td>
    <td><code>object</code></td>
    <td>Settings for the recovery orchestration groups associated with the recovery orchestration plan. Required.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a></td>
    <td></td>
    <td>Get a RecoveryPlan.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List RecoveryPlan resources by tenant.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a></td>
    <td></td>
    <td>Create a RecoveryPlan.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a></td>
    <td></td>
    <td>Update a RecoveryPlan.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a></td>
    <td></td>
    <td>Create a RecoveryPlan.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a></td>
    <td></td>
    <td>Delete a RecoveryPlan.</td>
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
<tr id="parameter-recovery_plan_name">
    <td><CopyableCode code="recovery_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery orchestration plan. Required.</td>
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

Get a RecoveryPlan.

```sql
SELECT
id,
name,
errorDetails,
identity,
latestFailoverStatus,
latestValidationStatus,
planDescription,
planState,
planType,
provisioningState,
recoveryGroupsSetting,
systemData,
type
FROM azure.resiliencemanagement.recovery_plans
WHERE service_group_name = '{{ service_group_name }}' -- required
AND recovery_plan_name = '{{ recovery_plan_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List RecoveryPlan resources by tenant.

```sql
SELECT
id,
name,
errorDetails,
identity,
latestFailoverStatus,
latestValidationStatus,
planDescription,
planState,
planType,
provisioningState,
recoveryGroupsSetting,
systemData,
type
FROM azure.resiliencemanagement.recovery_plans
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

Create a RecoveryPlan.

```sql
INSERT INTO azure.resiliencemanagement.recovery_plans (
properties,
identity,
service_group_name,
recovery_plan_name
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ service_group_name }}',
'{{ recovery_plan_name }}'
RETURNING
id,
name,
identity,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: recovery_plans
  props:
    - name: service_group_name
      value: "{{ service_group_name }}"
      description: Required parameter for the recovery_plans resource.
    - name: recovery_plan_name
      value: "{{ recovery_plan_name }}"
      description: Required parameter for the recovery_plans resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        planType: "{{ planType }}"
        planState: "{{ planState }}"
        planDescription: "{{ planDescription }}"
        recoveryGroupsSetting:
          defaultGroup:
            id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              groupUniqueId: "{{ groupUniqueId }}"
              orderId: {{ orderId }}
              description: "{{ description }}"
              preActions:
                - name: "{{ name }}"
                  description: "{{ description }}"
                  type: "{{ type }}"
                  timeoutInMinutes: {{ timeoutInMinutes }}
              postActions:
                - name: "{{ name }}"
                  description: "{{ description }}"
                  type: "{{ type }}"
                  timeoutInMinutes: {{ timeoutInMinutes }}
          additionalGroups:
            - id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              systemData:
                createdBy: "{{ createdBy }}"
                createdByType: "{{ createdByType }}"
                createdAt: "{{ createdAt }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedByType: "{{ lastModifiedByType }}"
                lastModifiedAt: "{{ lastModifiedAt }}"
              properties:
                groupUniqueId: "{{ groupUniqueId }}"
                orderId: {{ orderId }}
                description: "{{ description }}"
                preActions:
                  - name: "{{ name }}"
                    description: "{{ description }}"
                    type: "{{ type }}"
                    timeoutInMinutes: {{ timeoutInMinutes }}
                postActions:
                  - name: "{{ name }}"
                    description: "{{ description }}"
                    type: "{{ type }}"
                    timeoutInMinutes: {{ timeoutInMinutes }}
        latestFailoverStatus:
          lastExecutedAt: "{{ lastExecutedAt }}"
          operationStatus: "{{ operationStatus }}"
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
          recoveryTimeActual: "{{ recoveryTimeActual }}"
        latestValidationStatus:
          lastExecutedAt: "{{ lastExecutedAt }}"
          operationStatus: "{{ operationStatus }}"
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
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update a RecoveryPlan.

```sql
UPDATE azure.resiliencemanagement.recovery_plans
SET 
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND recovery_plan_name = '{{ recovery_plan_name }}' --required
RETURNING
id,
name,
identity,
properties,
systemData,
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

Create a RecoveryPlan.

```sql
REPLACE azure.resiliencemanagement.recovery_plans
SET 
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND recovery_plan_name = '{{ recovery_plan_name }}' --required
RETURNING
id,
name,
identity,
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

Delete a RecoveryPlan.

```sql
DELETE FROM azure.resiliencemanagement.recovery_plans
WHERE service_group_name = '{{ service_group_name }}' --required
AND recovery_plan_name = '{{ recovery_plan_name }}' --required
;
```
</TabItem>
</Tabs>
