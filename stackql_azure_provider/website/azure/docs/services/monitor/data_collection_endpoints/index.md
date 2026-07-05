--- 
title: data_collection_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_endpoints
  - monitor
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

Creates, updates, deletes, gets or lists a <code>data_collection_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_collection_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.data_collection_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_nsp"
    values={[
        { label: 'get_nsp', value: 'get_nsp' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_nsp">

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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>Information about a network security perimeter (NSP).</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>:vartype profile: ~azure.mgmt.monitor.models.NetworkSecurityProfile</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>List of provisioning issues, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "Canceled". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>:vartype resource_association: ~azure.mgmt.monitor.models.ResourceAssociation</td>
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
    <td><CopyableCode code="configurationAccess" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to access their configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the data collection endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="failoverConfiguration" /></td>
    <td><code>object</code></td>
    <td>Metadata for the resource. This property can only be updated by Log Analytics Control Plane for Data Collection Endpoint with Log Analytics Destination.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableId" /></td>
    <td><code>string</code></td>
    <td>The immutable ID of this data collection endpoint resource. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logsIngestion" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to ingest logs.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata for the resource. This property can only be updated by Log Analytics Control Plane for Data Collection Endpoint with Log Analytics Destination.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsIngestion" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to ingest metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Network access control rules for the endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of Azure Monitor Private Link Scope Resources to which this data collection endpoint resource is associated. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. This property is READ-ONLY. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
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
    <td><CopyableCode code="configurationAccess" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to access their configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the data collection endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="failoverConfiguration" /></td>
    <td><code>object</code></td>
    <td>Metadata for the resource. This property can only be updated by Log Analytics Control Plane for Data Collection Endpoint with Log Analytics Destination.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableId" /></td>
    <td><code>string</code></td>
    <td>The immutable ID of this data collection endpoint resource. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logsIngestion" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to ingest logs.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata for the resource. This property can only be updated by Log Analytics Control Plane for Data Collection Endpoint with Log Analytics Destination.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsIngestion" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to ingest metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Network access control rules for the endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of Azure Monitor Private Link Scope Resources to which this data collection endpoint resource is associated. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. This property is READ-ONLY. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
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
    <td><CopyableCode code="configurationAccess" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to access their configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the data collection endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="failoverConfiguration" /></td>
    <td><code>object</code></td>
    <td>Metadata for the resource. This property can only be updated by Log Analytics Control Plane for Data Collection Endpoint with Log Analytics Destination.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableId" /></td>
    <td><code>string</code></td>
    <td>The immutable ID of this data collection endpoint resource. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logsIngestion" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to ingest logs.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata for the resource. This property can only be updated by Log Analytics Control Plane for Data Collection Endpoint with Log Analytics Destination.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsIngestion" /></td>
    <td><code>object</code></td>
    <td>The endpoint used by clients to ingest metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Network access control rules for the endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of Azure Monitor Private Link Scope Resources to which this data collection endpoint resource is associated. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. This property is READ-ONLY. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
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
    <td><a href="#get_nsp"><CopyableCode code="get_nsp" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified NSP configuration for the specified data collection endpoint. Gets the specified NSP configuration for the specified data collection endpoint.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the specified data collection endpoint. Returns the specified data collection endpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all data collection endpoints in the specified resource group. Lists all data collection endpoints in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all data collection endpoints in the specified subscription. Lists all data collection endpoints in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a data collection endpoint. Creates or updates a data collection endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates part of a data collection endpoint. Updates part of a data collection endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a data collection endpoint. Deletes a data collection endpoint.</td>
</tr>
<tr>
    <td><a href="#list_nsp"><CopyableCode code="list_nsp" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of NSP configurations for the specified data collection endpoint. Gets a list of NSP configurations for the specified data collection endpoint.</td>
</tr>
<tr>
    <td><a href="#reconcile_nsp"><CopyableCode code="reconcile_nsp" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reconciles the specified NSP configuration for the specified data collection endpoint. Reconciles the specified NSP configuration for the specified data collection endpoint.</td>
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
<tr id="parameter-data_collection_endpoint_name">
    <td><CopyableCode code="data_collection_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the data collection endpoint. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-network_security_perimeter_configuration_name">
    <td><CopyableCode code="network_security_perimeter_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name for a network security perimeter configuration. Required.</td>
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
    defaultValue="get_nsp"
    values={[
        { label: 'get_nsp', value: 'get_nsp' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_nsp">

Gets the specified NSP configuration for the specified data collection endpoint. Gets the specified NSP configuration for the specified data collection endpoint.

```sql
SELECT
id,
name,
networkSecurityPerimeter,
profile,
provisioningIssues,
provisioningState,
resourceAssociation,
systemData,
type
FROM azure.monitor.data_collection_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_collection_endpoint_name = '{{ data_collection_endpoint_name }}' -- required
AND network_security_perimeter_configuration_name = '{{ network_security_perimeter_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Returns the specified data collection endpoint. Returns the specified data collection endpoint.

```sql
SELECT
id,
name,
configurationAccess,
description,
etag,
failoverConfiguration,
identity,
immutableId,
kind,
location,
logsIngestion,
metadata,
metricsIngestion,
networkAcls,
privateLinkScopedResources,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.monitor.data_collection_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_collection_endpoint_name = '{{ data_collection_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all data collection endpoints in the specified resource group. Lists all data collection endpoints in the specified resource group.

```sql
SELECT
id,
name,
configurationAccess,
description,
etag,
failoverConfiguration,
identity,
immutableId,
kind,
location,
logsIngestion,
metadata,
metricsIngestion,
networkAcls,
privateLinkScopedResources,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.monitor.data_collection_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all data collection endpoints in the specified subscription. Lists all data collection endpoints in the specified subscription.

```sql
SELECT
id,
name,
configurationAccess,
description,
etag,
failoverConfiguration,
identity,
immutableId,
kind,
location,
logsIngestion,
metadata,
metricsIngestion,
networkAcls,
privateLinkScopedResources,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.monitor.data_collection_endpoints
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

Creates or updates a data collection endpoint. Creates or updates a data collection endpoint.

```sql
INSERT INTO azure.monitor.data_collection_endpoints (
tags,
location,
properties,
kind,
sku,
identity,
resource_group_name,
data_collection_endpoint_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ data_collection_endpoint_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
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
- name: data_collection_endpoints
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_collection_endpoints resource.
    - name: data_collection_endpoint_name
      value: "{{ data_collection_endpoint_name }}"
      description: Required parameter for the data_collection_endpoints resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_collection_endpoints resource.
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
        :vartype properties: ~azure.mgmt.monitor.models.DataCollectionEndpointResourceProperties
      value:
        description: "{{ description }}"
        immutableId: "{{ immutableId }}"
        configurationAccess:
          endpoint: "{{ endpoint }}"
        logsIngestion:
          endpoint: "{{ endpoint }}"
        metricsIngestion:
          endpoint: "{{ endpoint }}"
        networkAcls:
          publicNetworkAccess: "{{ publicNetworkAccess }}"
        provisioningState: "{{ provisioningState }}"
        privateLinkScopedResources:
          - resourceId: "{{ resourceId }}"
            scopeId: "{{ scopeId }}"
        failoverConfiguration:
          activeLocation: "{{ activeLocation }}"
          locations:
            - location: "{{ location }}"
              provisioningStatus: "{{ provisioningStatus }}"
        metadata:
          provisionedBy: "{{ provisionedBy }}"
          provisionedByResourceId: "{{ provisionedByResourceId }}"
          provisionedByImmutableId: "{{ provisionedByImmutableId }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the resource. Known values are: "Linux" and "Windows".
      valid_values: ['Linux', 'Windows']
    - name: sku
      description: |
        The SKU of the resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Managed service identity of the resource.
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

Updates part of a data collection endpoint. Updates part of a data collection endpoint.

```sql
UPDATE azure.monitor.data_collection_endpoints
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND data_collection_endpoint_name = '{{ data_collection_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
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

Deletes a data collection endpoint. Deletes a data collection endpoint.

```sql
DELETE FROM azure.monitor.data_collection_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND data_collection_endpoint_name = '{{ data_collection_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_nsp"
    values={[
        { label: 'list_nsp', value: 'list_nsp' },
        { label: 'reconcile_nsp', value: 'reconcile_nsp' }
    ]}
>
<TabItem value="list_nsp">

Gets a list of NSP configurations for the specified data collection endpoint. Gets a list of NSP configurations for the specified data collection endpoint.

```sql
EXEC azure.monitor.data_collection_endpoints.list_nsp 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_collection_endpoint_name='{{ data_collection_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reconcile_nsp">

Reconciles the specified NSP configuration for the specified data collection endpoint. Reconciles the specified NSP configuration for the specified data collection endpoint.

```sql
EXEC azure.monitor.data_collection_endpoints.reconcile_nsp 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_collection_endpoint_name='{{ data_collection_endpoint_name }}' --required, 
@network_security_perimeter_configuration_name='{{ network_security_perimeter_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
