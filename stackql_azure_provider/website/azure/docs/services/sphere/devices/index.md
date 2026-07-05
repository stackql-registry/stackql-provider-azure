--- 
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - sphere
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.devices" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_device_group', value: 'list_by_device_group' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="chipSku" /></td>
    <td><code>string</code></td>
    <td>SKU of the chip.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>Device ID.</td>
</tr>
<tr>
    <td><CopyableCode code="lastAvailableOsVersion" /></td>
    <td><code>string</code></td>
    <td>OS version available for installation when update requested.</td>
</tr>
<tr>
    <td><CopyableCode code="lastInstalledOsVersion" /></td>
    <td><code>string</code></td>
    <td>OS version running on device when update requested.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOsUpdateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when update requested and new OS version available.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateRequestUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when update was last requested.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
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
<TabItem value="list_by_device_group">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="chipSku" /></td>
    <td><code>string</code></td>
    <td>SKU of the chip.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>Device ID.</td>
</tr>
<tr>
    <td><CopyableCode code="lastAvailableOsVersion" /></td>
    <td><code>string</code></td>
    <td>OS version available for installation when update requested.</td>
</tr>
<tr>
    <td><CopyableCode code="lastInstalledOsVersion" /></td>
    <td><code>string</code></td>
    <td>OS version running on device when update requested.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOsUpdateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when update requested and new OS version available.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateRequestUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when update was last requested.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Device. Use '.unassigned' or '.default' for the device group and product names when a device does not belong to a device group and product.</td>
</tr>
<tr>
    <td><a href="#list_by_device_group"><CopyableCode code="list_by_device_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Device. Use '.unassigned' or '.default' for the device group and product names to claim a device to the catalog only.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Device. Use '.unassigned' or '.default' for the device group and product names to move a device to the catalog level.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Device. Use '.unassigned' or '.default' for the device group and product names to claim a device to the catalog only.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Device.</td>
</tr>
<tr>
    <td><a href="#generate_capability_image"><CopyableCode code="generate_capability_image" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-capabilities"><code>capabilities</code></a></td>
    <td></td>
    <td>Generates the capability image for the device. Use '.unassigned' or '.default' for the device group and product names to generate the image for a device that does not belong to a specific device group and product.</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>Name of catalog. Required.</td>
</tr>
<tr id="parameter-device_group_name">
    <td><CopyableCode code="device_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of device group. Required.</td>
</tr>
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>Device name. Required.</td>
</tr>
<tr id="parameter-product_name">
    <td><CopyableCode code="product_name" /></td>
    <td><code>string</code></td>
    <td>Name of product. Required.</td>
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
        { label: 'list_by_device_group', value: 'list_by_device_group' }
    ]}
>
<TabItem value="get">

Get a Device. Use '.unassigned' or '.default' for the device group and product names when a device does not belong to a device group and product.

```sql
SELECT
id,
name,
chipSku,
deviceId,
lastAvailableOsVersion,
lastInstalledOsVersion,
lastOsUpdateUtc,
lastUpdateRequestUtc,
provisioningState,
systemData,
type
FROM azure.sphere.devices
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND product_name = '{{ product_name }}' -- required
AND device_group_name = '{{ device_group_name }}' -- required
AND device_name = '{{ device_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_device_group">

List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
SELECT
id,
name,
chipSku,
deviceId,
lastAvailableOsVersion,
lastInstalledOsVersion,
lastOsUpdateUtc,
lastUpdateRequestUtc,
provisioningState,
systemData,
type
FROM azure.sphere.devices
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND product_name = '{{ product_name }}' -- required
AND device_group_name = '{{ device_group_name }}' -- required
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

Create a Device. Use '.unassigned' or '.default' for the device group and product names to claim a device to the catalog only.

```sql
INSERT INTO azure.sphere.devices (
properties,
resource_group_name,
catalog_name,
product_name,
device_group_name,
device_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ catalog_name }}',
'{{ product_name }}',
'{{ device_group_name }}',
'{{ device_name }}',
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
- name: devices
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the devices resource.
    - name: catalog_name
      value: "{{ catalog_name }}"
      description: Required parameter for the devices resource.
    - name: product_name
      value: "{{ product_name }}"
      description: Required parameter for the devices resource.
    - name: device_group_name
      value: "{{ device_group_name }}"
      description: Required parameter for the devices resource.
    - name: device_name
      value: "{{ device_name }}"
      description: Required parameter for the devices resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the devices resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        deviceId: "{{ deviceId }}"
        chipSku: "{{ chipSku }}"
        lastAvailableOsVersion: "{{ lastAvailableOsVersion }}"
        lastInstalledOsVersion: "{{ lastInstalledOsVersion }}"
        lastOsUpdateUtc: "{{ lastOsUpdateUtc }}"
        lastUpdateRequestUtc: "{{ lastUpdateRequestUtc }}"
        provisioningState: "{{ provisioningState }}"
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

Update a Device. Use '.unassigned' or '.default' for the device group and product names to move a device to the catalog level.

```sql
UPDATE azure.sphere.devices
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
AND device_name = '{{ device_name }}' --required
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

Create a Device. Use '.unassigned' or '.default' for the device group and product names to claim a device to the catalog only.

```sql
REPLACE azure.sphere.devices
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
AND device_name = '{{ device_name }}' --required
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

Delete a Device.

```sql
DELETE FROM azure.sphere.devices
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
AND device_name = '{{ device_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_capability_image"
    values={[
        { label: 'generate_capability_image', value: 'generate_capability_image' }
    ]}
>
<TabItem value="generate_capability_image">

Generates the capability image for the device. Use '.unassigned' or '.default' for the device group and product names to generate the image for a device that does not belong to a specific device group and product.

```sql
EXEC azure.sphere.devices.generate_capability_image 
@resource_group_name='{{ resource_group_name }}' --required, 
@catalog_name='{{ catalog_name }}' --required, 
@product_name='{{ product_name }}' --required, 
@device_group_name='{{ device_group_name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"capabilities": "{{ capabilities }}"
}'
;
```
</TabItem>
</Tabs>
