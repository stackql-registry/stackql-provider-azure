--- 
title: elastic_sans
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_sans
  - elasticsan
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

Creates, updates, deletes, gets or lists an <code>elastic_sans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="elastic_sans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elasticsan.elastic_sans" /></td></tr>
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
    <td><CopyableCode code="autoScaleProperties" /></td>
    <td><code>object</code></td>
    <td>Auto Scale Properties for Elastic San Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>Logical zone for Elastic San resource; example: ["1"].</td>
</tr>
<tr>
    <td><CopyableCode code="baseSizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Base size of the Elastic San appliance in TiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedCapacitySizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Extended size of the Elastic San appliance in TiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of Private Endpoint Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Allow or disallow public network access to ElasticSan. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>resource sku. Required.</td>
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
    <td><CopyableCode code="totalIops" /></td>
    <td><code>integer</code></td>
    <td>Total Provisioned IOPS of the Elastic San appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMBps" /></td>
    <td><code>integer</code></td>
    <td>Total Provisioned MBps Elastic San appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="totalSizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Total size of the Elastic San appliance in TB.</td>
</tr>
<tr>
    <td><CopyableCode code="totalVolumeSizeGiB" /></td>
    <td><code>integer</code></td>
    <td>Total size of the provisioned Volumes in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumeGroupCount" /></td>
    <td><code>integer</code></td>
    <td>Total number of volume groups in this Elastic San appliance.</td>
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
    <td><CopyableCode code="autoScaleProperties" /></td>
    <td><code>object</code></td>
    <td>Auto Scale Properties for Elastic San Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>Logical zone for Elastic San resource; example: ["1"].</td>
</tr>
<tr>
    <td><CopyableCode code="baseSizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Base size of the Elastic San appliance in TiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedCapacitySizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Extended size of the Elastic San appliance in TiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of Private Endpoint Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Allow or disallow public network access to ElasticSan. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>resource sku. Required.</td>
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
    <td><CopyableCode code="totalIops" /></td>
    <td><code>integer</code></td>
    <td>Total Provisioned IOPS of the Elastic San appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMBps" /></td>
    <td><code>integer</code></td>
    <td>Total Provisioned MBps Elastic San appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="totalSizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Total size of the Elastic San appliance in TB.</td>
</tr>
<tr>
    <td><CopyableCode code="totalVolumeSizeGiB" /></td>
    <td><code>integer</code></td>
    <td>Total size of the provisioned Volumes in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumeGroupCount" /></td>
    <td><code>integer</code></td>
    <td>Total number of volume groups in this Elastic San appliance.</td>
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
    <td><CopyableCode code="autoScaleProperties" /></td>
    <td><code>object</code></td>
    <td>Auto Scale Properties for Elastic San Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>Logical zone for Elastic San resource; example: ["1"].</td>
</tr>
<tr>
    <td><CopyableCode code="baseSizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Base size of the Elastic San appliance in TiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedCapacitySizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Extended size of the Elastic San appliance in TiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of Private Endpoint Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Allow or disallow public network access to ElasticSan. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>resource sku. Required.</td>
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
    <td><CopyableCode code="totalIops" /></td>
    <td><code>integer</code></td>
    <td>Total Provisioned IOPS of the Elastic San appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMBps" /></td>
    <td><code>integer</code></td>
    <td>Total Provisioned MBps Elastic San appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="totalSizeTiB" /></td>
    <td><code>integer</code></td>
    <td>Total size of the Elastic San appliance in TB.</td>
</tr>
<tr>
    <td><CopyableCode code="totalVolumeSizeGiB" /></td>
    <td><code>integer</code></td>
    <td>Total size of the provisioned Volumes in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumeGroupCount" /></td>
    <td><code>integer</code></td>
    <td>Total number of volume groups in this Elastic San appliance.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ElasticSan.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of ElasticSan in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of ElasticSans in a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create ElasticSan.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Elastic San.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Elastic San.</td>
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
<tr id="parameter-elastic_san_name">
    <td><CopyableCode code="elastic_san_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticSan. Required.</td>
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

Get a ElasticSan.

```sql
SELECT
id,
name,
autoScaleProperties,
availabilityZones,
baseSizeTiB,
extendedCapacitySizeTiB,
location,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
totalIops,
totalMBps,
totalSizeTiB,
totalVolumeSizeGiB,
type,
volumeGroupCount
FROM azure.elasticsan.elastic_sans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND elastic_san_name = '{{ elastic_san_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of ElasticSan in a resource group.

```sql
SELECT
id,
name,
autoScaleProperties,
availabilityZones,
baseSizeTiB,
extendedCapacitySizeTiB,
location,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
totalIops,
totalMBps,
totalSizeTiB,
totalVolumeSizeGiB,
type,
volumeGroupCount
FROM azure.elasticsan.elastic_sans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of ElasticSans in a subscription.

```sql
SELECT
id,
name,
autoScaleProperties,
availabilityZones,
baseSizeTiB,
extendedCapacitySizeTiB,
location,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
totalIops,
totalMBps,
totalSizeTiB,
totalVolumeSizeGiB,
type,
volumeGroupCount
FROM azure.elasticsan.elastic_sans
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create ElasticSan.

```sql
INSERT INTO azure.elasticsan.elastic_sans (
tags,
location,
properties,
resource_group_name,
elastic_san_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ elastic_san_name }}',
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
- name: elastic_sans
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the elastic_sans resource.
    - name: elastic_san_name
      value: "{{ elastic_san_name }}"
      description: Required parameter for the elastic_sans resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the elastic_sans resource.
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
        Properties of ElasticSan. Required.
      value:
        sku:
          name: "{{ name }}"
          tier: "{{ tier }}"
        availabilityZones:
          - "{{ availabilityZones }}"
        provisioningState: "{{ provisioningState }}"
        baseSizeTiB: {{ baseSizeTiB }}
        extendedCapacitySizeTiB: {{ extendedCapacitySizeTiB }}
        totalVolumeSizeGiB: {{ totalVolumeSizeGiB }}
        volumeGroupCount: {{ volumeGroupCount }}
        totalIops: {{ totalIops }}
        totalMBps: {{ totalMBps }}
        totalSizeTiB: {{ totalSizeTiB }}
        privateEndpointConnections:
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
              provisioningState: "{{ provisioningState }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              groupIds:
                - "{{ groupIds }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        autoScaleProperties:
          scaleUpProperties:
            unusedSizeTiB: {{ unusedSizeTiB }}
            increaseCapacityUnitByTiB: {{ increaseCapacityUnitByTiB }}
            capacityUnitScaleUpLimitTiB: {{ capacityUnitScaleUpLimitTiB }}
            autoScalePolicyEnforcement: "{{ autoScalePolicyEnforcement }}"
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

Update a Elastic San.

```sql
UPDATE azure.elasticsan.elastic_sans
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND elastic_san_name = '{{ elastic_san_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a Elastic San.

```sql
DELETE FROM azure.elasticsan.elastic_sans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND elastic_san_name = '{{ elastic_san_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
