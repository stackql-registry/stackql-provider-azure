--- 
title: network_anchors
hide_title: false
hide_table_of_contents: false
keywords:
  - network_anchors
  - oracle_database
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>network_anchors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_anchors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.network_anchors" /></td></tr>
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
    <td><CopyableCode code="cidrBlock" /></td>
    <td><code>string</code></td>
    <td>Delegated Azure subnet cidr block.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>DNS forwarding endpoint IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingEndpointNsgRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Forwarding endpoint NSG rules.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingRules" /></td>
    <td><code>array</code></td>
    <td>DNS forwarding rules.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Forwarding rules page.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointAllowedCidrs" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of CIDRs that are allowed to send requests to the DNS listening endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>DNS listening endpoint IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointNsgRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Listening endpoint NSG rules.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleDnsForwardingEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Oracle DNS forwarding endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleDnsListeningEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Oracle DNS listening endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleToAzureDnsZoneSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether DNS zone sync from OCI to Azure is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ociBackupCidrBlock" /></td>
    <td><code>string</code></td>
    <td>OCI backup subnet cidr block.</td>
</tr>
<tr>
    <td><CopyableCode code="ociSubnetId" /></td>
    <td><code>string</code></td>
    <td>Oracle Cloud Infrastructure subnet OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="ociVcnDnsLabel" /></td>
    <td><code>string</code></td>
    <td>OCI DNS label. This is optional if DNS config is provided.</td>
</tr>
<tr>
    <td><CopyableCode code="ociVcnId" /></td>
    <td><code>string</code></td>
    <td>Oracle Cloud Infrastructure VCN OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>NetworkAnchor provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAnchorId" /></td>
    <td><code>string</code></td>
    <td>Corresponding resource anchor Azure ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet. Required.</td>
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
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="cidrBlock" /></td>
    <td><code>string</code></td>
    <td>Delegated Azure subnet cidr block.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>DNS forwarding endpoint IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingEndpointNsgRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Forwarding endpoint NSG rules.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingRules" /></td>
    <td><code>array</code></td>
    <td>DNS forwarding rules.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Forwarding rules page.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointAllowedCidrs" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of CIDRs that are allowed to send requests to the DNS listening endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>DNS listening endpoint IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointNsgRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Listening endpoint NSG rules.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleDnsForwardingEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Oracle DNS forwarding endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleDnsListeningEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Oracle DNS listening endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleToAzureDnsZoneSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether DNS zone sync from OCI to Azure is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ociBackupCidrBlock" /></td>
    <td><code>string</code></td>
    <td>OCI backup subnet cidr block.</td>
</tr>
<tr>
    <td><CopyableCode code="ociSubnetId" /></td>
    <td><code>string</code></td>
    <td>Oracle Cloud Infrastructure subnet OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="ociVcnDnsLabel" /></td>
    <td><code>string</code></td>
    <td>OCI DNS label. This is optional if DNS config is provided.</td>
</tr>
<tr>
    <td><CopyableCode code="ociVcnId" /></td>
    <td><code>string</code></td>
    <td>Oracle Cloud Infrastructure VCN OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>NetworkAnchor provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAnchorId" /></td>
    <td><code>string</code></td>
    <td>Corresponding resource anchor Azure ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet. Required.</td>
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
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="cidrBlock" /></td>
    <td><code>string</code></td>
    <td>Delegated Azure subnet cidr block.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>DNS forwarding endpoint IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingEndpointNsgRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Forwarding endpoint NSG rules.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingRules" /></td>
    <td><code>array</code></td>
    <td>DNS forwarding rules.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsForwardingRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Forwarding rules page.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointAllowedCidrs" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of CIDRs that are allowed to send requests to the DNS listening endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>DNS listening endpoint IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsListeningEndpointNsgRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Deep link to OCI console DNS Listening endpoint NSG rules.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleDnsForwardingEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Oracle DNS forwarding endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleDnsListeningEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Oracle DNS listening endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isOracleToAzureDnsZoneSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether DNS zone sync from OCI to Azure is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ociBackupCidrBlock" /></td>
    <td><code>string</code></td>
    <td>OCI backup subnet cidr block.</td>
</tr>
<tr>
    <td><CopyableCode code="ociSubnetId" /></td>
    <td><code>string</code></td>
    <td>Oracle Cloud Infrastructure subnet OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="ociVcnDnsLabel" /></td>
    <td><code>string</code></td>
    <td>OCI DNS label. This is optional if DNS config is provided.</td>
</tr>
<tr>
    <td><CopyableCode code="ociVcnId" /></td>
    <td><code>string</code></td>
    <td>Oracle Cloud Infrastructure VCN OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>NetworkAnchor provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAnchorId" /></td>
    <td><code>string</code></td>
    <td>Corresponding resource anchor Azure ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet. Required.</td>
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
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_anchor_name"><code>network_anchor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a NetworkAnchor.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List NetworkAnchor resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List NetworkAnchor resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_anchor_name"><code>network_anchor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a NetworkAnchor.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_anchor_name"><code>network_anchor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a NetworkAnchor.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_anchor_name"><code>network_anchor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a NetworkAnchor.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_anchor_name"><code>network_anchor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a NetworkAnchor.</td>
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
<tr id="parameter-network_anchor_name">
    <td><CopyableCode code="network_anchor_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NetworkAnchor. Required.</td>
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

Get a NetworkAnchor.

```sql
SELECT
id,
name,
cidrBlock,
dnsForwardingEndpointIpAddress,
dnsForwardingEndpointNsgRulesUrl,
dnsForwardingRules,
dnsForwardingRulesUrl,
dnsListeningEndpointAllowedCidrs,
dnsListeningEndpointIpAddress,
dnsListeningEndpointNsgRulesUrl,
isOracleDnsForwardingEndpointEnabled,
isOracleDnsListeningEndpointEnabled,
isOracleToAzureDnsZoneSyncEnabled,
location,
ociBackupCidrBlock,
ociSubnetId,
ociVcnDnsLabel,
ociVcnId,
provisioningState,
resourceAnchorId,
subnetId,
systemData,
tags,
type,
vnetId,
zones
FROM azure_isv.oracle_database.network_anchors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_anchor_name = '{{ network_anchor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List NetworkAnchor resources by resource group.

```sql
SELECT
id,
name,
cidrBlock,
dnsForwardingEndpointIpAddress,
dnsForwardingEndpointNsgRulesUrl,
dnsForwardingRules,
dnsForwardingRulesUrl,
dnsListeningEndpointAllowedCidrs,
dnsListeningEndpointIpAddress,
dnsListeningEndpointNsgRulesUrl,
isOracleDnsForwardingEndpointEnabled,
isOracleDnsListeningEndpointEnabled,
isOracleToAzureDnsZoneSyncEnabled,
location,
ociBackupCidrBlock,
ociSubnetId,
ociVcnDnsLabel,
ociVcnId,
provisioningState,
resourceAnchorId,
subnetId,
systemData,
tags,
type,
vnetId,
zones
FROM azure_isv.oracle_database.network_anchors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List NetworkAnchor resources by subscription ID.

```sql
SELECT
id,
name,
cidrBlock,
dnsForwardingEndpointIpAddress,
dnsForwardingEndpointNsgRulesUrl,
dnsForwardingRules,
dnsForwardingRulesUrl,
dnsListeningEndpointAllowedCidrs,
dnsListeningEndpointIpAddress,
dnsListeningEndpointNsgRulesUrl,
isOracleDnsForwardingEndpointEnabled,
isOracleDnsListeningEndpointEnabled,
isOracleToAzureDnsZoneSyncEnabled,
location,
ociBackupCidrBlock,
ociSubnetId,
ociVcnDnsLabel,
ociVcnId,
provisioningState,
resourceAnchorId,
subnetId,
systemData,
tags,
type,
vnetId,
zones
FROM azure_isv.oracle_database.network_anchors
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

Create a NetworkAnchor.

```sql
INSERT INTO azure_isv.oracle_database.network_anchors (
tags,
location,
properties,
zones,
resource_group_name,
network_anchor_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ network_anchor_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_anchors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_anchors resource.
    - name: network_anchor_name
      value: "{{ network_anchor_name }}"
      description: Required parameter for the network_anchors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_anchors resource.
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
        resourceAnchorId: "{{ resourceAnchorId }}"
        provisioningState: "{{ provisioningState }}"
        vnetId: "{{ vnetId }}"
        subnetId: "{{ subnetId }}"
        cidrBlock: "{{ cidrBlock }}"
        ociVcnId: "{{ ociVcnId }}"
        ociVcnDnsLabel: "{{ ociVcnDnsLabel }}"
        ociSubnetId: "{{ ociSubnetId }}"
        ociBackupCidrBlock: "{{ ociBackupCidrBlock }}"
        isOracleToAzureDnsZoneSyncEnabled: {{ isOracleToAzureDnsZoneSyncEnabled }}
        isOracleDnsListeningEndpointEnabled: {{ isOracleDnsListeningEndpointEnabled }}
        isOracleDnsForwardingEndpointEnabled: {{ isOracleDnsForwardingEndpointEnabled }}
        dnsForwardingRules:
          - domainNames: "{{ domainNames }}"
            forwardingIpAddress: "{{ forwardingIpAddress }}"
        dnsListeningEndpointAllowedCidrs: "{{ dnsListeningEndpointAllowedCidrs }}"
        dnsListeningEndpointIpAddress: "{{ dnsListeningEndpointIpAddress }}"
        dnsForwardingEndpointIpAddress: "{{ dnsForwardingEndpointIpAddress }}"
        dnsForwardingRulesUrl: "{{ dnsForwardingRulesUrl }}"
        dnsListeningEndpointNsgRulesUrl: "{{ dnsListeningEndpointNsgRulesUrl }}"
        dnsForwardingEndpointNsgRulesUrl: "{{ dnsForwardingEndpointNsgRulesUrl }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
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

Update a NetworkAnchor.

```sql
UPDATE azure_isv.oracle_database.network_anchors
SET 
zones = '{{ zones }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_anchor_name = '{{ network_anchor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones;
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

Create a NetworkAnchor.

```sql
REPLACE azure_isv.oracle_database.network_anchors
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_anchor_name = '{{ network_anchor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones;
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

Delete a NetworkAnchor.

```sql
DELETE FROM azure_isv.oracle_database.network_anchors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_anchor_name = '{{ network_anchor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
