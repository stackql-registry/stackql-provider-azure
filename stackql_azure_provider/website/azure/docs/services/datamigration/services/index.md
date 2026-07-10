--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - datamigration
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datamigration.services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
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
    <td><CopyableCode code="autoStopDelay" /></td>
    <td><code>string</code></td>
    <td>The time delay before the service is auto-stopped when idle.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteResourcesOnStop" /></td>
    <td><code>boolean</code></td>
    <td>Whether service resources should be deleted when stopped. (Turned on by default).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. Ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The resource kind. Only 'vm' (the default) is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource's provisioning state. Known values are: "Accepted", "Deleting", "Deploying", "Stopped", "Stopping", "Starting", "FailedToStart", "FailedToStop", "Succeeded", and "Failed". (Accepted, Deleting, Deploying, Stopped, Stopping, Starting, FailedToStart, FailedToStop, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicKey" /></td>
    <td><code>string</code></td>
    <td>The public key of the service, used to encrypt secrets sent to the service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Service SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNicId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Microsoft.Network/networkInterfaces resource which the service have.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualSubnetId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined.</td>
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
    <td><CopyableCode code="autoStopDelay" /></td>
    <td><code>string</code></td>
    <td>The time delay before the service is auto-stopped when idle.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteResourcesOnStop" /></td>
    <td><code>boolean</code></td>
    <td>Whether service resources should be deleted when stopped. (Turned on by default).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. Ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The resource kind. Only 'vm' (the default) is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource's provisioning state. Known values are: "Accepted", "Deleting", "Deploying", "Stopped", "Stopping", "Starting", "FailedToStart", "FailedToStop", "Succeeded", and "Failed". (Accepted, Deleting, Deploying, Stopped, Stopping, Starting, FailedToStart, FailedToStop, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicKey" /></td>
    <td><code>string</code></td>
    <td>The public key of the service, used to encrypt secrets sent to the service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Service SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNicId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Microsoft.Network/networkInterfaces resource which the service have.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualSubnetId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>The localized reason why the name is not available, if nameAvailable is false.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>If true, the name is valid and available. If false, 'reason' describes why not.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason why the name is not available, if nameAvailable is false. Known values are: "AlreadyExists" and "Invalid". (AlreadyExists, Invalid)</td>
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
    <td><CopyableCode code="autoStopDelay" /></td>
    <td><code>string</code></td>
    <td>The time delay before the service is auto-stopped when idle.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteResourcesOnStop" /></td>
    <td><code>boolean</code></td>
    <td>Whether service resources should be deleted when stopped. (Turned on by default).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. Ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The resource kind. Only 'vm' (the default) is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource's provisioning state. Known values are: "Accepted", "Deleting", "Deploying", "Stopped", "Stopping", "Starting", "FailedToStart", "FailedToStop", "Succeeded", and "Failed". (Accepted, Deleting, Deploying, Stopped, Stopping, Starting, FailedToStart, FailedToStop, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicKey" /></td>
    <td><code>string</code></td>
    <td>The public key of the service, used to encrypt secrets sent to the service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Service SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNicId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Microsoft.Network/networkInterfaces resource which the service have.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualSubnetId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined.</td>
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
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get DMS (classic) Service Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The GET method retrieves information about a service instance.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get services in resource group. The Services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a resource group.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check name validity and availability. This method checks whether a proposed top-level resource name is valid and available.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get services in subscription. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update DMS (classic) Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update DMS (classic) Service Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy").</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update DMS (classic) Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteRunningTasks"><code>deleteRunningTasks</code></a></td>
    <td>Delete DMS (classic) Service Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The DELETE method deletes a service. Any running tasks will be canceled.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get compatible SKUs. The services resource is the top-level resource that represents the Database Migration Service (classic). The skus action returns the list of SKUs that a service resource can be updated to.</td>
</tr>
<tr>
    <td><a href="#check_status"><CopyableCode code="check_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check service health status. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action performs a health check and returns the status of the service and virtual machine size.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start service. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action starts the service and the service can be used for data migration.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop service. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action stops the service and the service cannot be used for data migration. The service owner won't be billed when the service is stopped.</td>
</tr>
<tr>
    <td><a href="#check_children_name_availability"><CopyableCode code="check_children_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check nested resource name validity and availability. This method checks whether a proposed nested resource name is valid and available.</td>
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
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>Name of the service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-deleteRunningTasks">
    <td><CopyableCode code="deleteRunningTasks" /></td>
    <td><code>boolean</code></td>
    <td>Delete the resource even if it contains running tasks. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get DMS (classic) Service Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The GET method retrieves information about a service instance.

```sql
SELECT
id,
name,
autoStopDelay,
deleteResourcesOnStop,
etag,
kind,
location,
provisioningState,
publicKey,
sku,
systemData,
tags,
type,
virtualNicId,
virtualSubnetId
FROM azure.datamigration.services
WHERE group_name = '{{ group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get services in resource group. The Services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a resource group.

```sql
SELECT
id,
name,
autoStopDelay,
deleteResourcesOnStop,
etag,
kind,
location,
provisioningState,
publicKey,
sku,
systemData,
tags,
type,
virtualNicId,
virtualSubnetId
FROM azure.datamigration.services
WHERE group_name = '{{ group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Check name validity and availability. This method checks whether a proposed top-level resource name is valid and available.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.datamigration.services
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get services in subscription. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a subscription.

```sql
SELECT
id,
name,
autoStopDelay,
deleteResourcesOnStop,
etag,
kind,
location,
provisioningState,
publicKey,
sku,
systemData,
tags,
type,
virtualNicId,
virtualSubnetId
FROM azure.datamigration.services
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

Create or update DMS (classic) Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.

```sql
INSERT INTO azure.datamigration.services (
properties,
etag,
kind,
sku,
location,
tags,
group_name,
service_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ kind }}',
'{{ sku }}',
'{{ location }}',
'{{ tags }}',
'{{ group_name }}',
'{{ service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: services
  props:
    - name: group_name
      value: "{{ group_name }}"
      description: Required parameter for the services resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the services resource.
    - name: properties
      description: |
        Custom service properties.
      value:
        provisioningState: "{{ provisioningState }}"
        publicKey: "{{ publicKey }}"
        virtualSubnetId: "{{ virtualSubnetId }}"
        virtualNicId: "{{ virtualNicId }}"
        autoStopDelay: "{{ autoStopDelay }}"
        deleteResourcesOnStop: {{ deleteResourcesOnStop }}
    - name: etag
      value: "{{ etag }}"
      description: |
        HTTP strong entity tag value. Ignored if submitted.
    - name: kind
      value: "{{ kind }}"
      description: |
        The resource kind. Only 'vm' (the default) is supported.
    - name: sku
      description: |
        Service SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        family: "{{ family }}"
        size: "{{ size }}"
        capacity: {{ capacity }}
    - name: location
      value: "{{ location }}"
      description: |
        :vartype location: str
    - name: tags
      value: "{{ tags }}"
      description: |
        :vartype tags: dict[str, str]
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

Create or update DMS (classic) Service Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy").

```sql
UPDATE azure.datamigration.services
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
kind = '{{ kind }}',
sku = '{{ sku }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
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

Create or update DMS (classic) Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.

```sql
REPLACE azure.datamigration.services
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
kind = '{{ kind }}',
sku = '{{ sku }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
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

Delete DMS (classic) Service Instance. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The DELETE method deletes a service. Any running tasks will be canceled.

```sql
DELETE FROM azure.datamigration.services
WHERE group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteRunningTasks = '{{ deleteRunningTasks }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_skus"
    values={[
        { label: 'list_skus', value: 'list_skus' },
        { label: 'check_status', value: 'check_status' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'check_children_name_availability', value: 'check_children_name_availability' }
    ]}
>
<TabItem value="list_skus">

Get compatible SKUs. The services resource is the top-level resource that represents the Database Migration Service (classic). The skus action returns the list of SKUs that a service resource can be updated to.

```sql
EXEC azure.datamigration.services.list_skus 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_status">

Check service health status. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action performs a health check and returns the status of the service and virtual machine size.

```sql
EXEC azure.datamigration.services.check_status 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start service. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action starts the service and the service can be used for data migration.

```sql
EXEC azure.datamigration.services.start 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop service. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action stops the service and the service cannot be used for data migration. The service owner won't be billed when the service is stopped.

```sql
EXEC azure.datamigration.services.stop 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_children_name_availability">

Check nested resource name validity and availability. This method checks whether a proposed nested resource name is valid and available.

```sql
EXEC azure.datamigration.services.check_children_name_availability 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
