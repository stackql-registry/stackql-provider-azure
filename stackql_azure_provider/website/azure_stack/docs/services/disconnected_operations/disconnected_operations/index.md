--- 
title: disconnected_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - disconnected_operations
  - disconnected_operations
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>disconnected_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disconnected_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.disconnected_operations.disconnected_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="benefitPlans" /></td>
    <td><code>object</code></td>
    <td>The benefit plans.</td>
</tr>
<tr>
    <td><CopyableCode code="billingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The billing configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="billingModel" /></td>
    <td><code>string</code></td>
    <td>The billing model. Required. "Capacity" (Capacity)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionIntent" /></td>
    <td><code>string</code></td>
    <td>The connection intent. Required. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>The connection status. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="deviceVersion" /></td>
    <td><code>string</code></td>
    <td>The device version.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>The registration intent. Known values are: "Registered" and "Unregistered". (Registered, Unregistered)</td>
</tr>
<tr>
    <td><CopyableCode code="stampId" /></td>
    <td><code>string</code></td>
    <td>The unique GUID of the stamp. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="benefitPlans" /></td>
    <td><code>object</code></td>
    <td>The benefit plans.</td>
</tr>
<tr>
    <td><CopyableCode code="billingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The billing configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="billingModel" /></td>
    <td><code>string</code></td>
    <td>The billing model. Required. "Capacity" (Capacity)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionIntent" /></td>
    <td><code>string</code></td>
    <td>The connection intent. Required. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>The connection status. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="deviceVersion" /></td>
    <td><code>string</code></td>
    <td>The device version.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>The registration intent. Known values are: "Registered" and "Unregistered". (Registered, Unregistered)</td>
</tr>
<tr>
    <td><CopyableCode code="stampId" /></td>
    <td><code>string</code></td>
    <td>The unique GUID of the stamp. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="benefitPlans" /></td>
    <td><code>object</code></td>
    <td>The benefit plans.</td>
</tr>
<tr>
    <td><CopyableCode code="billingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The billing configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="billingModel" /></td>
    <td><code>string</code></td>
    <td>The billing model. Required. "Capacity" (Capacity)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionIntent" /></td>
    <td><code>string</code></td>
    <td>The connection intent. Required. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>The connection status. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="deviceVersion" /></td>
    <td><code>string</code></td>
    <td>The device version.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>The registration intent. Known values are: "Registered" and "Unregistered". (Registered, Unregistered)</td>
</tr>
<tr>
    <td><CopyableCode code="stampId" /></td>
    <td><code>string</code></td>
    <td>The unique GUID of the stamp. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DisconnectedOperation.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DisconnectedOperation resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DisconnectedOperation resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a DisconnectedOperation.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a DisconnectedOperation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a DisconnectedOperation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a DisconnectedOperation.</td>
</tr>
<tr>
    <td><a href="#list_deployment_manifest"><CopyableCode code="list_deployment_manifest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>get deployment manifest.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a DisconnectedOperation.

```sql
SELECT
id,
name,
benefitPlans,
billingConfiguration,
billingModel,
connectionIntent,
connectionStatus,
deviceVersion,
location,
provisioningState,
registrationStatus,
stampId,
systemData,
tags,
type
FROM azure_stack.disconnected_operations.disconnected_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List DisconnectedOperation resources by resource group.

```sql
SELECT
id,
name,
benefitPlans,
billingConfiguration,
billingModel,
connectionIntent,
connectionStatus,
deviceVersion,
location,
provisioningState,
registrationStatus,
stampId,
systemData,
tags,
type
FROM azure_stack.disconnected_operations.disconnected_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List DisconnectedOperation resources by subscription ID.

```sql
SELECT
id,
name,
benefitPlans,
billingConfiguration,
billingModel,
connectionIntent,
connectionStatus,
deviceVersion,
location,
provisioningState,
registrationStatus,
stampId,
systemData,
tags,
type
FROM azure_stack.disconnected_operations.disconnected_operations
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

Create a DisconnectedOperation.

```sql
INSERT INTO azure_stack.disconnected_operations.disconnected_operations (
tags,
location,
properties,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: disconnected_operations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the disconnected_operations resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the disconnected_operations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the disconnected_operations resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        stampId: "{{ stampId }}"
        billingModel: "{{ billingModel }}"
        connectionIntent: "{{ connectionIntent }}"
        connectionStatus: "{{ connectionStatus }}"
        registrationStatus: "{{ registrationStatus }}"
        deviceVersion: "{{ deviceVersion }}"
        billingConfiguration:
          autoRenew: "{{ autoRenew }}"
          billingStatus: "{{ billingStatus }}"
          current:
            cores: {{ cores }}
            pricingModel: "{{ pricingModel }}"
            startDate: "{{ startDate }}"
            endDate: "{{ endDate }}"
          upcoming:
            cores: {{ cores }}
            pricingModel: "{{ pricingModel }}"
            startDate: "{{ startDate }}"
            endDate: "{{ endDate }}"
        benefitPlans:
          azureHybridWindowsServerBenefit: "{{ azureHybridWindowsServerBenefit }}"
          windowsServerVmCount: {{ windowsServerVmCount }}
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

Update a DisconnectedOperation.

```sql
UPDATE azure_stack.disconnected_operations.disconnected_operations
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Create a DisconnectedOperation.

```sql
REPLACE azure_stack.disconnected_operations.disconnected_operations
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Delete a DisconnectedOperation.

```sql
DELETE FROM azure_stack.disconnected_operations.disconnected_operations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_deployment_manifest"
    values={[
        { label: 'list_deployment_manifest', value: 'list_deployment_manifest' }
    ]}
>
<TabItem value="list_deployment_manifest">

get deployment manifest.

```sql
EXEC azure_stack.disconnected_operations.disconnected_operations.list_deployment_manifest 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
