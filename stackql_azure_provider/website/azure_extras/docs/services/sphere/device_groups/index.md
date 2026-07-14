--- 
title: device_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_groups
  - sphere
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>device_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="device_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.sphere.device_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_product', value: 'list_by_product' }
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
    <td><CopyableCode code="allowCrashDumpsCollection" /></td>
    <td><code>string</code></td>
    <td>Flag to define if the user allows for crash dump collection. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the device group.</td>
</tr>
<tr>
    <td><CopyableCode code="hasDeployment" /></td>
    <td><code>boolean</code></td>
    <td>Deployment status for the device group.</td>
</tr>
<tr>
    <td><CopyableCode code="osFeedType" /></td>
    <td><code>string</code></td>
    <td>Operating system feed type of the device group. Known values are: "Retail" and "RetailEval".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="regionalDataBoundary" /></td>
    <td><code>string</code></td>
    <td>Regional data boundary for the device group. Known values are: "None" and "EU".</td>
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
    <td><CopyableCode code="updatePolicy" /></td>
    <td><code>string</code></td>
    <td>Update policy of the device group. Known values are: "UpdateAll" and "No3rdPartyAppUpdates".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_product">

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
    <td><CopyableCode code="allowCrashDumpsCollection" /></td>
    <td><code>string</code></td>
    <td>Flag to define if the user allows for crash dump collection. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the device group.</td>
</tr>
<tr>
    <td><CopyableCode code="hasDeployment" /></td>
    <td><code>boolean</code></td>
    <td>Deployment status for the device group.</td>
</tr>
<tr>
    <td><CopyableCode code="osFeedType" /></td>
    <td><code>string</code></td>
    <td>Operating system feed type of the device group. Known values are: "Retail" and "RetailEval".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="regionalDataBoundary" /></td>
    <td><code>string</code></td>
    <td>Regional data boundary for the device group. Known values are: "None" and "EU".</td>
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
    <td><CopyableCode code="updatePolicy" /></td>
    <td><code>string</code></td>
    <td>Update policy of the device group. Known values are: "UpdateAll" and "No3rdPartyAppUpdates".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#list_by_product"><CopyableCode code="list_by_product" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$maxpagesize"><code>$maxpagesize</code></a></td>
    <td>List DeviceGroup resources by Product. '.default' and '.unassigned' are system defined values and cannot be used for product name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#claim_devices"><CopyableCode code="claim_devices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-deviceIdentifiers"><code>deviceIdentifiers</code></a></td>
    <td></td>
    <td>Bulk claims the devices. Use '.unassigned' or '.default' for the device group and product names when bulk claiming devices to a catalog only.</td>
</tr>
<tr>
    <td><a href="#count_devices"><CopyableCode code="count_devices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Counts devices in device group. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter the result list using the given expression. Default value is None.</td>
</tr>
<tr id="parameter-$maxpagesize">
    <td><CopyableCode code="$maxpagesize" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of result items per page. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_product', value: 'list_by_product' }
    ]}
>
<TabItem value="get">

Get a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
SELECT
id,
name,
allowCrashDumpsCollection,
description,
hasDeployment,
osFeedType,
provisioningState,
regionalDataBoundary,
systemData,
type,
updatePolicy
FROM azure_extras.sphere.device_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND product_name = '{{ product_name }}' -- required
AND device_group_name = '{{ device_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_product">

List DeviceGroup resources by Product. '.default' and '.unassigned' are system defined values and cannot be used for product name.

```sql
SELECT
id,
name,
allowCrashDumpsCollection,
description,
hasDeployment,
osFeedType,
provisioningState,
regionalDataBoundary,
systemData,
type,
updatePolicy
FROM azure_extras.sphere.device_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND product_name = '{{ product_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $maxpagesize = '{{ $maxpagesize }}'
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

Create a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
INSERT INTO azure_extras.sphere.device_groups (
properties,
resource_group_name,
catalog_name,
product_name,
device_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ catalog_name }}',
'{{ product_name }}',
'{{ device_group_name }}',
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
- name: device_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the device_groups resource.
    - name: catalog_name
      value: "{{ catalog_name }}"
      description: Required parameter for the device_groups resource.
    - name: product_name
      value: "{{ product_name }}"
      description: Required parameter for the device_groups resource.
    - name: device_group_name
      value: "{{ device_group_name }}"
      description: Required parameter for the device_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the device_groups resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        description: "{{ description }}"
        osFeedType: "{{ osFeedType }}"
        updatePolicy: "{{ updatePolicy }}"
        allowCrashDumpsCollection: "{{ allowCrashDumpsCollection }}"
        regionalDataBoundary: "{{ regionalDataBoundary }}"
        hasDeployment: {{ hasDeployment }}
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

Update a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
UPDATE azure_extras.sphere.device_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
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

Create a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
REPLACE azure_extras.sphere.device_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
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

Delete a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
DELETE FROM azure_extras.sphere.device_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="claim_devices"
    values={[
        { label: 'claim_devices', value: 'claim_devices' },
        { label: 'count_devices', value: 'count_devices' }
    ]}
>
<TabItem value="claim_devices">

Bulk claims the devices. Use '.unassigned' or '.default' for the device group and product names when bulk claiming devices to a catalog only.

```sql
EXEC azure_extras.sphere.device_groups.claim_devices 
@resource_group_name='{{ resource_group_name }}' --required, 
@catalog_name='{{ catalog_name }}' --required, 
@product_name='{{ product_name }}' --required, 
@device_group_name='{{ device_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"deviceIdentifiers": "{{ deviceIdentifiers }}"
}'
;
```
</TabItem>
<TabItem value="count_devices">

Counts devices in device group. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
EXEC azure_extras.sphere.device_groups.count_devices 
@resource_group_name='{{ resource_group_name }}' --required, 
@catalog_name='{{ catalog_name }}' --required, 
@product_name='{{ product_name }}' --required, 
@device_group_name='{{ device_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
