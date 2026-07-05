--- 
title: managed_ops
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_ops
  - managedops
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

Creates, updates, deletes, gets or lists a <code>managed_ops</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_ops" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managedops.managed_ops" /></td></tr>
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
    <td><CopyableCode code="desiredConfiguration" /></td>
    <td><code>object</code></td>
    <td>Desired configuration input by the user. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentProperties" /></td>
    <td><code>object</code></td>
    <td>Policy assignments created for managing services.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Deleting". (Succeeded, Failed, Canceled, Provisioning, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="services" /></td>
    <td><code>object</code></td>
    <td>Services provisioned by this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Product plan details of this resource.</td>
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
    <td><CopyableCode code="desiredConfiguration" /></td>
    <td><code>object</code></td>
    <td>Desired configuration input by the user. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentProperties" /></td>
    <td><code>object</code></td>
    <td>Policy assignments created for managing services.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Deleting". (Succeeded, Failed, Canceled, Provisioning, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="services" /></td>
    <td><code>object</code></td>
    <td>Services provisioned by this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Product plan details of this resource.</td>
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
    <td><a href="#parameter-managed_ops_name"><code>managed_ops_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the information of the ManagedOps instance.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all ManagedOps instances in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-managed_ops_name"><code>managed_ops_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the ManagedOps instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-managed_ops_name"><code>managed_ops_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the ManagedOps instance with the supplied fields.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-managed_ops_name"><code>managed_ops_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the ManagedOps instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-managed_ops_name"><code>managed_ops_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the ManagedOps instance.</td>
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
<tr id="parameter-managed_ops_name">
    <td><CopyableCode code="managed_ops_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource. Required.</td>
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

Gets the information of the ManagedOps instance.

```sql
SELECT
id,
name,
desiredConfiguration,
policyAssignmentProperties,
provisioningState,
services,
sku,
systemData,
type
FROM azure.managedops.managed_ops
WHERE managed_ops_name = '{{ managed_ops_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all ManagedOps instances in the subscription.

```sql
SELECT
id,
name,
desiredConfiguration,
policyAssignmentProperties,
provisioningState,
services,
sku,
systemData,
type
FROM azure.managedops.managed_ops
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates the ManagedOps instance.

```sql
INSERT INTO azure.managedops.managed_ops (
properties,
managed_ops_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ managed_ops_name }}',
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
- name: managed_ops
  props:
    - name: managed_ops_name
      value: "{{ managed_ops_name }}"
      description: Required parameter for the managed_ops resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_ops resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        sku:
          name: "{{ name }}"
          tier: "{{ tier }}"
        provisioningState: "{{ provisioningState }}"
        desiredConfiguration:
          changeTrackingAndInventory:
            logAnalyticsWorkspaceId: "{{ logAnalyticsWorkspaceId }}"
          azureMonitorInsights:
            azureMonitorWorkspaceId: "{{ azureMonitorWorkspaceId }}"
          userAssignedManagedIdentityId: "{{ userAssignedManagedIdentityId }}"
          defenderForServers: "{{ defenderForServers }}"
          defenderCspm: "{{ defenderCspm }}"
        services:
          changeTrackingAndInventory:
            dcrId: "{{ dcrId }}"
            enablementStatus: "{{ enablementStatus }}"
          azureMonitorInsights:
            dcrId: "{{ dcrId }}"
            enablementStatus: "{{ enablementStatus }}"
          azureUpdateManager:
            enablementStatus: "{{ enablementStatus }}"
          azurePolicyAndMachineConfiguration:
            enablementStatus: "{{ enablementStatus }}"
          defenderForServers:
            enablementStatus: "{{ enablementStatus }}"
          defenderCspm:
            enablementStatus: "{{ enablementStatus }}"
        policyAssignmentProperties:
          policyInitiativeAssignmentId: "{{ policyInitiativeAssignmentId }}"
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

Updates the ManagedOps instance with the supplied fields.

```sql
UPDATE azure.managedops.managed_ops
SET 
properties = '{{ properties }}'
WHERE 
managed_ops_name = '{{ managed_ops_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates the ManagedOps instance.

```sql
REPLACE azure.managedops.managed_ops
SET 
properties = '{{ properties }}'
WHERE 
managed_ops_name = '{{ managed_ops_name }}' --required
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

Deletes the ManagedOps instance.

```sql
DELETE FROM azure.managedops.managed_ops
WHERE managed_ops_name = '{{ managed_ops_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
