--- 
title: l3_isolation_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - l3_isolation_domains
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>l3_isolation_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="l3_isolation_domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.managed_network_fabric.l3_isolation_domains" /></td></tr>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="aggregateRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Aggregate route configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="connectedSubnetRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Connected Subnet RoutePolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="exportPolicyConfiguration" /></td>
    <td><code>object</code></td>
    <td>BMP Export Policy configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource ID of the Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="redistributeConnectedSubnets" /></td>
    <td><code>string</code></td>
    <td>Advertise Connected Subnets. Ex: "True" | "False". Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="redistributeStaticRoutes" /></td>
    <td><code>string</code></td>
    <td>Advertise Static Routes. Ex: "True" | "False". Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="staticRouteRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Static Route - route policy.</td>
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
<tr>
    <td><CopyableCode code="uniqueRdConfiguration" /></td>
    <td><code>object</code></td>
    <td>Unique Route Distinguisher configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="v4routePrefixLimit" /></td>
    <td><code>object</code></td>
    <td>IPv4 VRF Limit configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="v6routePrefixLimit" /></td>
    <td><code>object</code></td>
    <td>IPv6 VRF Limit configuration.</td>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="aggregateRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Aggregate route configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="connectedSubnetRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Connected Subnet RoutePolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="exportPolicyConfiguration" /></td>
    <td><code>object</code></td>
    <td>BMP Export Policy configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource ID of the Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="redistributeConnectedSubnets" /></td>
    <td><code>string</code></td>
    <td>Advertise Connected Subnets. Ex: "True" | "False". Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="redistributeStaticRoutes" /></td>
    <td><code>string</code></td>
    <td>Advertise Static Routes. Ex: "True" | "False". Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="staticRouteRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Static Route - route policy.</td>
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
<tr>
    <td><CopyableCode code="uniqueRdConfiguration" /></td>
    <td><code>object</code></td>
    <td>Unique Route Distinguisher configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="v4routePrefixLimit" /></td>
    <td><code>object</code></td>
    <td>IPv4 VRF Limit configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="v6routePrefixLimit" /></td>
    <td><code>object</code></td>
    <td>IPv6 VRF Limit configuration.</td>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="aggregateRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Aggregate route configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="connectedSubnetRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Connected Subnet RoutePolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="exportPolicyConfiguration" /></td>
    <td><code>object</code></td>
    <td>BMP Export Policy configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource ID of the Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="redistributeConnectedSubnets" /></td>
    <td><code>string</code></td>
    <td>Advertise Connected Subnets. Ex: "True" | "False". Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="redistributeStaticRoutes" /></td>
    <td><code>string</code></td>
    <td>Advertise Static Routes. Ex: "True" | "False". Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="staticRouteRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Static Route - route policy.</td>
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
<tr>
    <td><CopyableCode code="uniqueRdConfiguration" /></td>
    <td><code>object</code></td>
    <td>Unique Route Distinguisher configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="v4routePrefixLimit" /></td>
    <td><code>object</code></td>
    <td>IPv4 VRF Limit configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="v6routePrefixLimit" /></td>
    <td><code>object</code></td>
    <td>IPv6 VRF Limit configuration.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves details of this L3 Isolation Domain.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Displays L3IsolationDomains list by resource group GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Displays L3IsolationDomains list by subscription GET method.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create isolation domain resources for layer 3 connectivity between compute nodes and for communication with external services .This configuration is applied on the devices only after the creation of networks is completed and isolation domain is enabled.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>API to update certain properties of the L3 Isolation Domain resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes layer 3 connectivity between compute nodes by managed by named L3 Isolation name.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the administrative state of the L3 Isolation Domain resource.</td>
</tr>
<tr>
    <td><a href="#validate_configuration"><CopyableCode code="validate_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates the configuration of the resources.</td>
</tr>
<tr>
    <td><a href="#commit_configuration"><CopyableCode code="commit_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Commits the configuration of the given resources.</td>
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
<tr id="parameter-l3_isolation_domain_name">
    <td><CopyableCode code="l3_isolation_domain_name" /></td>
    <td><code>string</code></td>
    <td>Name of the L3 Isolation Domain. Required.</td>
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

Retrieves details of this L3 Isolation Domain.

```sql
SELECT
id,
name,
administrativeState,
aggregateRouteConfiguration,
annotation,
configurationState,
connectedSubnetRoutePolicy,
exportPolicyConfiguration,
identity,
lastOperation,
location,
networkFabricId,
provisioningState,
redistributeConnectedSubnets,
redistributeStaticRoutes,
staticRouteRoutePolicy,
systemData,
tags,
type,
uniqueRdConfiguration,
v4routePrefixLimit,
v6routePrefixLimit
FROM azure_extras.managed_network_fabric.l3_isolation_domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Displays L3IsolationDomains list by resource group GET method.

```sql
SELECT
id,
name,
administrativeState,
aggregateRouteConfiguration,
annotation,
configurationState,
connectedSubnetRoutePolicy,
exportPolicyConfiguration,
identity,
lastOperation,
location,
networkFabricId,
provisioningState,
redistributeConnectedSubnets,
redistributeStaticRoutes,
staticRouteRoutePolicy,
systemData,
tags,
type,
uniqueRdConfiguration,
v4routePrefixLimit,
v6routePrefixLimit
FROM azure_extras.managed_network_fabric.l3_isolation_domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Displays L3IsolationDomains list by subscription GET method.

```sql
SELECT
id,
name,
administrativeState,
aggregateRouteConfiguration,
annotation,
configurationState,
connectedSubnetRoutePolicy,
exportPolicyConfiguration,
identity,
lastOperation,
location,
networkFabricId,
provisioningState,
redistributeConnectedSubnets,
redistributeStaticRoutes,
staticRouteRoutePolicy,
systemData,
tags,
type,
uniqueRdConfiguration,
v4routePrefixLimit,
v6routePrefixLimit
FROM azure_extras.managed_network_fabric.l3_isolation_domains
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

Create isolation domain resources for layer 3 connectivity between compute nodes and for communication with external services .This configuration is applied on the devices only after the creation of networks is completed and isolation domain is enabled.

```sql
INSERT INTO azure_extras.managed_network_fabric.l3_isolation_domains (
tags,
location,
properties,
identity,
resource_group_name,
l3_isolation_domain_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ l3_isolation_domain_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: l3_isolation_domains
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the l3_isolation_domains resource.
    - name: l3_isolation_domain_name
      value: "{{ l3_isolation_domain_name }}"
      description: Required parameter for the l3_isolation_domains resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the l3_isolation_domains resource.
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
        The L3 Isolation Domain Properties. Required.
      value:
        annotation: "{{ annotation }}"
        redistributeConnectedSubnets: "{{ redistributeConnectedSubnets }}"
        redistributeStaticRoutes: "{{ redistributeStaticRoutes }}"
        aggregateRouteConfiguration:
          ipv4Routes:
            - prefix: "{{ prefix }}"
          ipv6Routes:
            - prefix: "{{ prefix }}"
        connectedSubnetRoutePolicy:
          exportRoutePolicy:
            exportIpv4RoutePolicyId: "{{ exportIpv4RoutePolicyId }}"
            exportIpv6RoutePolicyId: "{{ exportIpv6RoutePolicyId }}"
        networkFabricId: "{{ networkFabricId }}"
        staticRouteRoutePolicy:
          exportRoutePolicy:
            exportIpv4RoutePolicyId: "{{ exportIpv4RoutePolicyId }}"
            exportIpv6RoutePolicyId: "{{ exportIpv6RoutePolicyId }}"
        uniqueRdConfiguration:
          uniqueRds:
            - "{{ uniqueRds }}"
        v4routePrefixLimit:
          hardLimit: {{ hardLimit }}
          threshold: {{ threshold }}
        v6routePrefixLimit:
          hardLimit: {{ hardLimit }}
          threshold: {{ threshold }}
        lastOperation:
          details: "{{ details }}"
        exportPolicyConfiguration:
          exportPolicies:
            - "{{ exportPolicies }}"
        configurationState: "{{ configurationState }}"
        provisioningState: "{{ provisioningState }}"
        administrativeState: "{{ administrativeState }}"
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

API to update certain properties of the L3 Isolation Domain resource.

```sql
UPDATE azure_extras.managed_network_fabric.l3_isolation_domains
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Deletes layer 3 connectivity between compute nodes by managed by named L3 Isolation name.

```sql
DELETE FROM azure_extras.managed_network_fabric.l3_isolation_domains
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_administrative_state"
    values={[
        { label: 'update_administrative_state', value: 'update_administrative_state' },
        { label: 'validate_configuration', value: 'validate_configuration' },
        { label: 'commit_configuration', value: 'commit_configuration' }
    ]}
>
<TabItem value="update_administrative_state">

Updates the administrative state of the L3 Isolation Domain resource.

```sql
EXEC azure_extras.managed_network_fabric.l3_isolation_domains.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="validate_configuration">

Validates the configuration of the resources.

```sql
EXEC azure_extras.managed_network_fabric.l3_isolation_domains.validate_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="commit_configuration">

Commits the configuration of the given resources.

```sql
EXEC azure_extras.managed_network_fabric.l3_isolation_domains.commit_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
