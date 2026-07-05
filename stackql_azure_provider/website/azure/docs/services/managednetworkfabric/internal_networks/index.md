--- 
title: internal_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - internal_networks
  - managednetworkfabric
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

Creates, updates, deletes, gets or lists an <code>internal_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="internal_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managednetworkfabric.internal_networks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_l3_isolation_domain', value: 'list_by_l3_isolation_domain' }
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
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpConfiguration" /></td>
    <td><code>object</code></td>
    <td>BGP configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="connectedIPv4Subnets" /></td>
    <td><code>array</code></td>
    <td>List of Connected IPv4 Subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="connectedIPv6Subnets" /></td>
    <td><code>array</code></td>
    <td>List of connected IPv6 Subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="egressAclId" /></td>
    <td><code>string</code></td>
    <td>Egress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="exportRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Export Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="extension" /></td>
    <td><code>string</code></td>
    <td>Extension. Example: NoExtension | NPB. Known values are: "NoExtension" and "NPB". (NoExtension, NPB)</td>
</tr>
<tr>
    <td><CopyableCode code="importRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Import Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressAclId" /></td>
    <td><code>string</code></td>
    <td>Ingress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="isMonitoringEnabled" /></td>
    <td><code>string</code></td>
    <td>To check whether monitoring of internal network is enabled or not. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="mtu" /></td>
    <td><code>integer</code></td>
    <td>Maximum transmission unit. Default value is 1500.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeIpv4PrefixLimit" /></td>
    <td><code>object</code></td>
    <td>Native IPv4 Prefix Limit Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeIpv6PrefixLimit" /></td>
    <td><code>object</code></td>
    <td>Native IPv6 Prefix Limit Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="staticRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Static Route Configuration properties.</td>
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
    <td><CopyableCode code="vlanId" /></td>
    <td><code>integer</code></td>
    <td>Vlan identifier. Example: 1001. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_l3_isolation_domain">

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
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpConfiguration" /></td>
    <td><code>object</code></td>
    <td>BGP configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="connectedIPv4Subnets" /></td>
    <td><code>array</code></td>
    <td>List of Connected IPv4 Subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="connectedIPv6Subnets" /></td>
    <td><code>array</code></td>
    <td>List of connected IPv6 Subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="egressAclId" /></td>
    <td><code>string</code></td>
    <td>Egress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="exportRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Export Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="extension" /></td>
    <td><code>string</code></td>
    <td>Extension. Example: NoExtension | NPB. Known values are: "NoExtension" and "NPB". (NoExtension, NPB)</td>
</tr>
<tr>
    <td><CopyableCode code="importRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Import Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressAclId" /></td>
    <td><code>string</code></td>
    <td>Ingress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="isMonitoringEnabled" /></td>
    <td><code>string</code></td>
    <td>To check whether monitoring of internal network is enabled or not. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="mtu" /></td>
    <td><code>integer</code></td>
    <td>Maximum transmission unit. Default value is 1500.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeIpv4PrefixLimit" /></td>
    <td><code>object</code></td>
    <td>Native IPv4 Prefix Limit Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeIpv6PrefixLimit" /></td>
    <td><code>object</code></td>
    <td>Native IPv6 Prefix Limit Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="staticRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Static Route Configuration properties.</td>
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
    <td><CopyableCode code="vlanId" /></td>
    <td><code>integer</code></td>
    <td>Vlan identifier. Example: 1001. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a InternalNetworks.</td>
</tr>
<tr>
    <td><a href="#list_by_l3_isolation_domain"><CopyableCode code="list_by_l3_isolation_domain" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Displays InternalNetworks list by resource group GET method.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates InternalNetwork PUT method.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a InternalNetworks.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements InternalNetworks DELETE method.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Executes update operation to enable or disable administrative State for InternalNetwork.</td>
</tr>
<tr>
    <td><a href="#update_bgp_administrative_state"><CopyableCode code="update_bgp_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update BGP state for internalNetwork. Allowed only on edge devices.</td>
</tr>
<tr>
    <td><a href="#update_static_route_bfd_administrative_state"><CopyableCode code="update_static_route_bfd_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update Static Route BFD administrative state for internalNetwork.</td>
</tr>
<tr>
    <td><a href="#update_bfd_administrative_state"><CopyableCode code="update_bfd_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-internal_network_name"><code>internal_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>BFD administrative state for either static or bgp for internalNetwork.</td>
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
<tr id="parameter-internal_network_name">
    <td><CopyableCode code="internal_network_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Internal Network. Required.</td>
</tr>
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
        { label: 'list_by_l3_isolation_domain', value: 'list_by_l3_isolation_domain' }
    ]}
>
<TabItem value="get">

Gets a InternalNetworks.

```sql
SELECT
id,
name,
administrativeState,
annotation,
bgpConfiguration,
configurationState,
connectedIPv4Subnets,
connectedIPv6Subnets,
egressAclId,
exportRoutePolicy,
extension,
importRoutePolicy,
ingressAclId,
isMonitoringEnabled,
lastOperation,
mtu,
nativeIpv4PrefixLimit,
nativeIpv6PrefixLimit,
networkFabricId,
provisioningState,
staticRouteConfiguration,
systemData,
type,
vlanId
FROM azure.managednetworkfabric.internal_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' -- required
AND internal_network_name = '{{ internal_network_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_l3_isolation_domain">

Displays InternalNetworks list by resource group GET method.

```sql
SELECT
id,
name,
administrativeState,
annotation,
bgpConfiguration,
configurationState,
connectedIPv4Subnets,
connectedIPv6Subnets,
egressAclId,
exportRoutePolicy,
extension,
importRoutePolicy,
ingressAclId,
isMonitoringEnabled,
lastOperation,
mtu,
nativeIpv4PrefixLimit,
nativeIpv6PrefixLimit,
networkFabricId,
provisioningState,
staticRouteConfiguration,
systemData,
type,
vlanId
FROM azure.managednetworkfabric.internal_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates InternalNetwork PUT method.

```sql
INSERT INTO azure.managednetworkfabric.internal_networks (
properties,
resource_group_name,
l3_isolation_domain_name,
internal_network_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ l3_isolation_domain_name }}',
'{{ internal_network_name }}',
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
- name: internal_networks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the internal_networks resource.
    - name: l3_isolation_domain_name
      value: "{{ l3_isolation_domain_name }}"
      description: Required parameter for the internal_networks resource.
    - name: internal_network_name
      value: "{{ internal_network_name }}"
      description: Required parameter for the internal_networks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the internal_networks resource.
    - name: properties
      description: |
        The Internal Network Properties. Required.
      value:
        annotation: "{{ annotation }}"
        extension: "{{ extension }}"
        mtu: {{ mtu }}
        connectedIPv4Subnets:
          - annotation: "{{ annotation }}"
            prefix: "{{ prefix }}"
        connectedIPv6Subnets:
          - annotation: "{{ annotation }}"
            prefix: "{{ prefix }}"
        importRoutePolicy:
          importIpv4RoutePolicyId: "{{ importIpv4RoutePolicyId }}"
          importIpv6RoutePolicyId: "{{ importIpv6RoutePolicyId }}"
        exportRoutePolicy:
          exportIpv4RoutePolicyId: "{{ exportIpv4RoutePolicyId }}"
          exportIpv6RoutePolicyId: "{{ exportIpv6RoutePolicyId }}"
        ingressAclId: "{{ ingressAclId }}"
        egressAclId: "{{ egressAclId }}"
        isMonitoringEnabled: "{{ isMonitoringEnabled }}"
        vlanId: {{ vlanId }}
        bgpConfiguration:
          annotation: "{{ annotation }}"
          bfdConfiguration:
            administrativeState: "{{ administrativeState }}"
            intervalInMilliSeconds: {{ intervalInMilliSeconds }}
            multiplier: {{ multiplier }}
          defaultRouteOriginate: "{{ defaultRouteOriginate }}"
          allowAS: {{ allowAS }}
          allowASOverride: "{{ allowASOverride }}"
          fabricASN: {{ fabricASN }}
          peerASN: {{ peerASN }}
          ipv4ListenRangePrefixes:
            - "{{ ipv4ListenRangePrefixes }}"
          ipv6ListenRangePrefixes:
            - "{{ ipv6ListenRangePrefixes }}"
          ipv4NeighborAddress:
            - address: "{{ address }}"
              bfdAdministrativeState: "{{ bfdAdministrativeState }}"
              bgpAdministrativeState: "{{ bgpAdministrativeState }}"
              configurationState: "{{ configurationState }}"
          ipv6NeighborAddress:
            - address: "{{ address }}"
              bfdAdministrativeState: "{{ bfdAdministrativeState }}"
              bgpAdministrativeState: "{{ bgpAdministrativeState }}"
              configurationState: "{{ configurationState }}"
          bmpConfiguration:
            neighborIpExclusions:
              - "{{ neighborIpExclusions }}"
            bmpConfigurationState: "{{ bmpConfigurationState }}"
            exportPolicyConfiguration:
              exportPolicies:
                - "{{ exportPolicies }}"
          v4OverV6BgpSession: "{{ v4OverV6BgpSession }}"
          v6OverV4BgpSession: "{{ v6OverV4BgpSession }}"
        staticRouteConfiguration:
          bfdConfiguration:
            administrativeState: "{{ administrativeState }}"
            intervalInMilliSeconds: {{ intervalInMilliSeconds }}
            multiplier: {{ multiplier }}
          ipv4Routes:
            - prefix: "{{ prefix }}"
              nextHop: "{{ nextHop }}"
          ipv6Routes:
            - prefix: "{{ prefix }}"
              nextHop: "{{ nextHop }}"
          extension: "{{ extension }}"
        nativeIpv4PrefixLimit:
          prefixLimits:
            - maximumRoutes: {{ maximumRoutes }}
              threshold: {{ threshold }}
              idleTimeExpiry: {{ idleTimeExpiry }}
        nativeIpv6PrefixLimit:
          prefixLimits:
            - maximumRoutes: {{ maximumRoutes }}
              threshold: {{ threshold }}
              idleTimeExpiry: {{ idleTimeExpiry }}
        lastOperation:
          details: "{{ details }}"
        networkFabricId: "{{ networkFabricId }}"
        configurationState: "{{ configurationState }}"
        provisioningState: "{{ provisioningState }}"
        administrativeState: "{{ administrativeState }}"
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

Updates a InternalNetworks.

```sql
UPDATE azure.managednetworkfabric.internal_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' --required
AND internal_network_name = '{{ internal_network_name }}' --required
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

Implements InternalNetworks DELETE method.

```sql
DELETE FROM azure.managednetworkfabric.internal_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' --required
AND internal_network_name = '{{ internal_network_name }}' --required
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
        { label: 'update_bgp_administrative_state', value: 'update_bgp_administrative_state' },
        { label: 'update_static_route_bfd_administrative_state', value: 'update_static_route_bfd_administrative_state' },
        { label: 'update_bfd_administrative_state', value: 'update_bfd_administrative_state' }
    ]}
>
<TabItem value="update_administrative_state">

Executes update operation to enable or disable administrative State for InternalNetwork.

```sql
EXEC azure.managednetworkfabric.internal_networks.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@internal_network_name='{{ internal_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="update_bgp_administrative_state">

Update BGP state for internalNetwork. Allowed only on edge devices.

```sql
EXEC azure.managednetworkfabric.internal_networks.update_bgp_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@internal_network_name='{{ internal_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"neighborAddress": "{{ neighborAddress }}", 
"administrativeState": "{{ administrativeState }}"
}'
;
```
</TabItem>
<TabItem value="update_static_route_bfd_administrative_state">

Update Static Route BFD administrative state for internalNetwork.

```sql
EXEC azure.managednetworkfabric.internal_networks.update_static_route_bfd_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@internal_network_name='{{ internal_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="update_bfd_administrative_state">

BFD administrative state for either static or bgp for internalNetwork.

```sql
EXEC azure.managednetworkfabric.internal_networks.update_bfd_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@internal_network_name='{{ internal_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"routeType": "{{ routeType }}", 
"neighborAddress": "{{ neighborAddress }}", 
"administrativeState": "{{ administrativeState }}"
}'
;
```
</TabItem>
</Tabs>
