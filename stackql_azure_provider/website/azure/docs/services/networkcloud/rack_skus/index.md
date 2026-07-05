--- 
title: rack_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - rack_skus
  - networkcloud
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

Creates, updates, deletes, gets or lists a <code>rack_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rack_skus" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.networkcloud.rack_skus" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="computeMachines" /></td>
    <td><code>array</code></td>
    <td>The list of machine SKUs and associated rack slot for the compute-dedicated machines in this rack model.</td>
</tr>
<tr>
    <td><CopyableCode code="controllerMachines" /></td>
    <td><code>array</code></td>
    <td>The list of machine SKUs and associated rack slot for the control-plane dedicated machines in this rack model.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type supported by the rack SKU. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The free-form text describing the rack.</td>
</tr>
<tr>
    <td><CopyableCode code="maxClusterSlots" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of compute racks supported by an aggregator rack. 0 if this is a compute rack or a rack for a single rack cluster(rackType="Single").</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the rack SKU resource. Known values are: "Canceled", "Failed", and "Succeeded". (Canceled, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="rackType" /></td>
    <td><code>string</code></td>
    <td>The type of the rack. Known values are: "Aggregator", "Compute", and "Single". (Aggregator, Compute, Single)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAppliances" /></td>
    <td><code>array</code></td>
    <td>The list of appliance SKUs and associated rack slot for the storage appliance(s) in this rack model.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedRackSkuIds" /></td>
    <td><code>array</code></td>
    <td>The list of supported SKUs if the rack is an aggregator.</td>
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
    <td><CopyableCode code="computeMachines" /></td>
    <td><code>array</code></td>
    <td>The list of machine SKUs and associated rack slot for the compute-dedicated machines in this rack model.</td>
</tr>
<tr>
    <td><CopyableCode code="controllerMachines" /></td>
    <td><code>array</code></td>
    <td>The list of machine SKUs and associated rack slot for the control-plane dedicated machines in this rack model.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type supported by the rack SKU. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The free-form text describing the rack.</td>
</tr>
<tr>
    <td><CopyableCode code="maxClusterSlots" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of compute racks supported by an aggregator rack. 0 if this is a compute rack or a rack for a single rack cluster(rackType="Single").</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the rack SKU resource. Known values are: "Canceled", "Failed", and "Succeeded". (Canceled, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="rackType" /></td>
    <td><code>string</code></td>
    <td>The type of the rack. Known values are: "Aggregator", "Compute", and "Single". (Aggregator, Compute, Single)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAppliances" /></td>
    <td><code>array</code></td>
    <td>The list of appliance SKUs and associated rack slot for the storage appliance(s) in this rack model.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedRackSkuIds" /></td>
    <td><code>array</code></td>
    <td>The list of supported SKUs if the rack is an aggregator.</td>
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
    <td><a href="#parameter-rack_sku_name"><code>rack_sku_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of the provided rack SKU.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of rack SKUs in the provided subscription.</td>
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
<tr id="parameter-rack_sku_name">
    <td><CopyableCode code="rack_sku_name" /></td>
    <td><code>string</code></td>
    <td>The name of the rack SKU. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get the properties of the provided rack SKU.

```sql
SELECT
id,
name,
computeMachines,
controllerMachines,
deploymentType,
description,
maxClusterSlots,
provisioningState,
rackType,
storageAppliances,
supportedRackSkuIds,
systemData,
type
FROM azure.networkcloud.rack_skus
WHERE rack_sku_name = '{{ rack_sku_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of rack SKUs in the provided subscription.

```sql
SELECT
id,
name,
computeMachines,
controllerMachines,
deploymentType,
description,
maxClusterSlots,
provisioningState,
rackType,
storageAppliances,
supportedRackSkuIds,
systemData,
type
FROM azure.networkcloud.rack_skus
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
