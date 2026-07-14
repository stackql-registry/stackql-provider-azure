--- 
title: cloud_hsm_cluster_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_cluster_private_link_resources
  - hardware_security_modules
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

Creates, updates, deletes, gets or lists a <code>cloud_hsm_cluster_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloud_hsm_cluster_private_link_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.cloud_hsm_cluster_private_link_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_cloud_hsm_cluster"
    values={[
        { label: 'list_by_cloud_hsm_cluster', value: 'list_by_cloud_hsm_cluster' }
    ]}
>
<TabItem value="list_by_cloud_hsm_cluster">

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
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The private link resource group id.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredMembers" /></td>
    <td><code>array</code></td>
    <td>The private link resource required member names.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredZoneNames" /></td>
    <td><code>array</code></td>
    <td>The private link resource private link DNS zone name.</td>
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
    <td><a href="#list_by_cloud_hsm_cluster"><CopyableCode code="list_by_cloud_hsm_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_hsm_cluster_name"><code>cloud_hsm_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the private link resources supported for the Cloud Hsm Cluster.</td>
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
<tr id="parameter-cloud_hsm_cluster_name">
    <td><CopyableCode code="cloud_hsm_cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Cloud HSM Cluster within the specified resource group. Cloud HSM Cluster names must be between 3 and 23 characters in length. Required.</td>
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
    defaultValue="list_by_cloud_hsm_cluster"
    values={[
        { label: 'list_by_cloud_hsm_cluster', value: 'list_by_cloud_hsm_cluster' }
    ]}
>
<TabItem value="list_by_cloud_hsm_cluster">

Gets the private link resources supported for the Cloud Hsm Cluster.

```sql
SELECT
id,
name,
groupId,
requiredMembers,
requiredZoneNames,
systemData,
type
FROM azure.hardware_security_modules.cloud_hsm_cluster_private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_hsm_cluster_name = '{{ cloud_hsm_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
