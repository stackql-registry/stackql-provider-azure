--- 
title: network_to_network_interconnects
hide_title: false
hide_table_of_contents: false
keywords:
  - network_to_network_interconnects
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

Creates, updates, deletes, gets or lists a <code>network_to_network_interconnects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_to_network_interconnects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managednetworkfabric.network_to_network_interconnects" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_network_fabric', value: 'list_by_network_fabric' }
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
    <td><CopyableCode code="conditionalDefaultRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Conditional Default Route Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="egressAclId" /></td>
    <td><code>string</code></td>
    <td>Egress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="exportRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Export Route Policy information.</td>
</tr>
<tr>
    <td><CopyableCode code="importRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Import Route Policy information.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressAclId" /></td>
    <td><code>string</code></td>
    <td>Ingress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementType" /></td>
    <td><code>string</code></td>
    <td>Configuration to use NNI for Infrastructure Management. Example: True/False. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="layer2Configuration" /></td>
    <td><code>object</code></td>
    <td>Common properties for Layer2 Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="microBfdState" /></td>
    <td><code>string</code></td>
    <td>Micro Bidirectional Forwarding Detection (BFD) enabled/disabled state. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nniType" /></td>
    <td><code>string</code></td>
    <td>Type of NNI used. Example: CE | NPB. Known values are: "CE" and "NPB". (CE, NPB)</td>
</tr>
<tr>
    <td><CopyableCode code="npbStaticRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>NPB Static Route Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="optionBLayer3Configuration" /></td>
    <td><code>object</code></td>
    <td>Common properties for Layer3Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="staticRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Static Route Configuration.</td>
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
    <td><CopyableCode code="useOptionB" /></td>
    <td><code>string</code></td>
    <td>Based on this option layer3 parameters are mandatory. Example: True/False. Required. Known values are: "True" and "False". (True, False)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_network_fabric">

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
    <td><CopyableCode code="conditionalDefaultRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Conditional Default Route Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="egressAclId" /></td>
    <td><code>string</code></td>
    <td>Egress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="exportRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Export Route Policy information.</td>
</tr>
<tr>
    <td><CopyableCode code="importRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Import Route Policy information.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressAclId" /></td>
    <td><code>string</code></td>
    <td>Ingress Acl. ARM resource ID of Access Control Lists.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementType" /></td>
    <td><code>string</code></td>
    <td>Configuration to use NNI for Infrastructure Management. Example: True/False. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="layer2Configuration" /></td>
    <td><code>object</code></td>
    <td>Common properties for Layer2 Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="microBfdState" /></td>
    <td><code>string</code></td>
    <td>Micro Bidirectional Forwarding Detection (BFD) enabled/disabled state. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nniType" /></td>
    <td><code>string</code></td>
    <td>Type of NNI used. Example: CE | NPB. Known values are: "CE" and "NPB". (CE, NPB)</td>
</tr>
<tr>
    <td><CopyableCode code="npbStaticRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>NPB Static Route Configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="optionBLayer3Configuration" /></td>
    <td><code>object</code></td>
    <td>Common properties for Layer3Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="staticRouteConfiguration" /></td>
    <td><code>object</code></td>
    <td>Static Route Configuration.</td>
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
    <td><CopyableCode code="useOptionB" /></td>
    <td><code>string</code></td>
    <td>Based on this option layer3 parameters are mandatory. Example: True/False. Required. Known values are: "True" and "False". (True, False)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-network_to_network_interconnect_name"><code>network_to_network_interconnect_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements NetworkToNetworkInterconnects GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_network_fabric"><CopyableCode code="list_by_network_fabric" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements Network To Network Interconnects list by Network Fabric GET method.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-network_to_network_interconnect_name"><code>network_to_network_interconnect_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Configuration used to setup CE-PE connectivity PUT Method.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-network_to_network_interconnect_name"><code>network_to_network_interconnect_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update certain properties of the Network To NetworkInterconnects resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-network_to_network_interconnect_name"><code>network_to_network_interconnect_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements NetworkToNetworkInterconnects DELETE method.</td>
</tr>
<tr>
    <td><a href="#update_npb_static_route_bfd_administrative_state"><CopyableCode code="update_npb_static_route_bfd_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-network_to_network_interconnect_name"><code>network_to_network_interconnect_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the NPB Static Route BFD Administrative State.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-network_to_network_interconnect_name"><code>network_to_network_interconnect_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Admin State.</td>
</tr>
<tr>
    <td><a href="#update_bfd_administrative_state"><CopyableCode code="update_bfd_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-network_to_network_interconnect_name"><code>network_to_network_interconnect_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Admin State.</td>
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
<tr id="parameter-network_fabric_name">
    <td><CopyableCode code="network_fabric_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Fabric. Required.</td>
</tr>
<tr id="parameter-network_to_network_interconnect_name">
    <td><CopyableCode code="network_to_network_interconnect_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network to Network Interconnect. Required.</td>
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
        { label: 'list_by_network_fabric', value: 'list_by_network_fabric' }
    ]}
>
<TabItem value="get">

Implements NetworkToNetworkInterconnects GET method.

```sql
SELECT
id,
name,
administrativeState,
conditionalDefaultRouteConfiguration,
configurationState,
egressAclId,
exportRoutePolicy,
importRoutePolicy,
ingressAclId,
isManagementType,
lastOperation,
layer2Configuration,
microBfdState,
nniType,
npbStaticRouteConfiguration,
optionBLayer3Configuration,
provisioningState,
staticRouteConfiguration,
systemData,
type,
useOptionB
FROM azure.managednetworkfabric.network_to_network_interconnects
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_fabric_name = '{{ network_fabric_name }}' -- required
AND network_to_network_interconnect_name = '{{ network_to_network_interconnect_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_network_fabric">

Implements Network To Network Interconnects list by Network Fabric GET method.

```sql
SELECT
id,
name,
administrativeState,
conditionalDefaultRouteConfiguration,
configurationState,
egressAclId,
exportRoutePolicy,
importRoutePolicy,
ingressAclId,
isManagementType,
lastOperation,
layer2Configuration,
microBfdState,
nniType,
npbStaticRouteConfiguration,
optionBLayer3Configuration,
provisioningState,
staticRouteConfiguration,
systemData,
type,
useOptionB
FROM azure.managednetworkfabric.network_to_network_interconnects
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_fabric_name = '{{ network_fabric_name }}' -- required
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

Configuration used to setup CE-PE connectivity PUT Method.

```sql
INSERT INTO azure.managednetworkfabric.network_to_network_interconnects (
properties,
resource_group_name,
network_fabric_name,
network_to_network_interconnect_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ network_fabric_name }}',
'{{ network_to_network_interconnect_name }}',
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
- name: network_to_network_interconnects
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_to_network_interconnects resource.
    - name: network_fabric_name
      value: "{{ network_fabric_name }}"
      description: Required parameter for the network_to_network_interconnects resource.
    - name: network_to_network_interconnect_name
      value: "{{ network_to_network_interconnect_name }}"
      description: Required parameter for the network_to_network_interconnects resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_to_network_interconnects resource.
    - name: properties
      description: |
        The NetworkToNetworkInterconnect Properties. Required.
      value:
        nniType: "{{ nniType }}"
        isManagementType: "{{ isManagementType }}"
        useOptionB: "{{ useOptionB }}"
        layer2Configuration:
          mtu: {{ mtu }}
          interfaces:
            - "{{ interfaces }}"
        optionBLayer3Configuration:
          primaryIpv4Prefix: "{{ primaryIpv4Prefix }}"
          primaryIpv6Prefix: "{{ primaryIpv6Prefix }}"
          secondaryIpv4Prefix: "{{ secondaryIpv4Prefix }}"
          secondaryIpv6Prefix: "{{ secondaryIpv6Prefix }}"
          peerASN: {{ peerASN }}
          vlanId: {{ vlanId }}
          fabricASN: {{ fabricASN }}
          peLoopbackIpAddress:
            - "{{ peLoopbackIpAddress }}"
          bmpConfiguration:
            configurationState: "{{ configurationState }}"
          prefixLimits:
            - maximumRoutes: {{ maximumRoutes }}
        npbStaticRouteConfiguration:
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
        importRoutePolicy:
          importIpv4RoutePolicyId: "{{ importIpv4RoutePolicyId }}"
          importIpv6RoutePolicyId: "{{ importIpv6RoutePolicyId }}"
        exportRoutePolicy:
          exportIpv4RoutePolicyId: "{{ exportIpv4RoutePolicyId }}"
          exportIpv6RoutePolicyId: "{{ exportIpv6RoutePolicyId }}"
        egressAclId: "{{ egressAclId }}"
        ingressAclId: "{{ ingressAclId }}"
        microBfdState: "{{ microBfdState }}"
        conditionalDefaultRouteConfiguration:
          ipv4Routes:
            - prefix: "{{ prefix }}"
              nextHop: "{{ nextHop }}"
          ipv6Routes:
            - prefix: "{{ prefix }}"
              nextHop: "{{ nextHop }}"
        lastOperation:
          details: "{{ details }}"
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

Update certain properties of the Network To NetworkInterconnects resource.

```sql
UPDATE azure.managednetworkfabric.network_to_network_interconnects
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_fabric_name = '{{ network_fabric_name }}' --required
AND network_to_network_interconnect_name = '{{ network_to_network_interconnect_name }}' --required
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

Implements NetworkToNetworkInterconnects DELETE method.

```sql
DELETE FROM azure.managednetworkfabric.network_to_network_interconnects
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_fabric_name = '{{ network_fabric_name }}' --required
AND network_to_network_interconnect_name = '{{ network_to_network_interconnect_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_npb_static_route_bfd_administrative_state"
    values={[
        { label: 'update_npb_static_route_bfd_administrative_state', value: 'update_npb_static_route_bfd_administrative_state' },
        { label: 'update_administrative_state', value: 'update_administrative_state' },
        { label: 'update_bfd_administrative_state', value: 'update_bfd_administrative_state' }
    ]}
>
<TabItem value="update_npb_static_route_bfd_administrative_state">

Updates the NPB Static Route BFD Administrative State.

```sql
EXEC azure.managednetworkfabric.network_to_network_interconnects.update_npb_static_route_bfd_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@network_to_network_interconnect_name='{{ network_to_network_interconnect_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="update_administrative_state">

Updates the Admin State.

```sql
EXEC azure.managednetworkfabric.network_to_network_interconnects.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@network_to_network_interconnect_name='{{ network_to_network_interconnect_name }}' --required, 
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

Updates the Admin State.

```sql
EXEC azure.managednetworkfabric.network_to_network_interconnects.update_bfd_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@network_to_network_interconnect_name='{{ network_to_network_interconnect_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"routeType": "{{ routeType }}", 
"administrativeState": "{{ administrativeState }}"
}'
;
```
</TabItem>
</Tabs>
