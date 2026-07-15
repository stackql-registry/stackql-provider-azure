--- 
title: external_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - external_networks
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

Creates, updates, deletes, gets or lists an <code>external_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="external_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.managed_network_fabric.external_networks" /></td></tr>
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
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="exportRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Export Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="importRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Import Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="networkToNetworkInterconnectId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource ID of the networkToNetworkInterconnectId of the ExternalNetwork resource.</td>
</tr>
<tr>
    <td><CopyableCode code="optionAProperties" /></td>
    <td><code>object</code></td>
    <td>option A properties object.</td>
</tr>
<tr>
    <td><CopyableCode code="optionBProperties" /></td>
    <td><code>object</code></td>
    <td>option B properties object.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringOption" /></td>
    <td><code>string</code></td>
    <td>Peering option list. Required. Known values are: "OptionA" and "OptionB". (OptionA, OptionB)</td>
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
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="exportRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Export Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="importRoutePolicy" /></td>
    <td><code>object</code></td>
    <td>Import Route Policy either IPv4 or IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="networkToNetworkInterconnectId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource ID of the networkToNetworkInterconnectId of the ExternalNetwork resource.</td>
</tr>
<tr>
    <td><CopyableCode code="optionAProperties" /></td>
    <td><code>object</code></td>
    <td>option A properties object.</td>
</tr>
<tr>
    <td><CopyableCode code="optionBProperties" /></td>
    <td><code>object</code></td>
    <td>option B properties object.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringOption" /></td>
    <td><code>string</code></td>
    <td>Peering option list. Required. Known values are: "OptionA" and "OptionB". (OptionA, OptionB)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-external_network_name"><code>external_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements ExternalNetworks GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_l3_isolation_domain"><CopyableCode code="list_by_l3_isolation_domain" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements External Networks list by resource group GET method.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-external_network_name"><code>external_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates ExternalNetwork PUT method.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-external_network_name"><code>external_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>API to update certain properties of the ExternalNetworks resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-external_network_name"><code>external_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements ExternalNetworks DELETE method.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-external_network_name"><code>external_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Executes update operation to enable or disable administrative State for externalNetwork.</td>
</tr>
<tr>
    <td><a href="#update_static_route_bfd_administrative_state"><CopyableCode code="update_static_route_bfd_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-external_network_name"><code>external_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update Static Route BFD for external Network.</td>
</tr>
<tr>
    <td><a href="#update_bfd_administrative_state"><CopyableCode code="update_bfd_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-l3_isolation_domain_name"><code>l3_isolation_domain_name</code></a>, <a href="#parameter-external_network_name"><code>external_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
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
<tr id="parameter-external_network_name">
    <td><CopyableCode code="external_network_name" /></td>
    <td><code>string</code></td>
    <td>Name of the External Network. Required.</td>
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

Implements ExternalNetworks GET method.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
exportRoutePolicy,
importRoutePolicy,
lastOperation,
networkFabricId,
networkToNetworkInterconnectId,
optionAProperties,
optionBProperties,
peeringOption,
provisioningState,
staticRouteConfiguration,
systemData,
type
FROM azure_extras.managed_network_fabric.external_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' -- required
AND external_network_name = '{{ external_network_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_l3_isolation_domain">

Implements External Networks list by resource group GET method.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
exportRoutePolicy,
importRoutePolicy,
lastOperation,
networkFabricId,
networkToNetworkInterconnectId,
optionAProperties,
optionBProperties,
peeringOption,
provisioningState,
staticRouteConfiguration,
systemData,
type
FROM azure_extras.managed_network_fabric.external_networks
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

Creates ExternalNetwork PUT method.

```sql
INSERT INTO azure_extras.managed_network_fabric.external_networks (
properties,
resource_group_name,
l3_isolation_domain_name,
external_network_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ l3_isolation_domain_name }}',
'{{ external_network_name }}',
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
- name: external_networks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the external_networks resource.
    - name: l3_isolation_domain_name
      value: "{{ l3_isolation_domain_name }}"
      description: Required parameter for the external_networks resource.
    - name: external_network_name
      value: "{{ external_network_name }}"
      description: Required parameter for the external_networks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the external_networks resource.
    - name: properties
      description: |
        External Network Properties. Required.
      value:
        annotation: "{{ annotation }}"
        networkToNetworkInterconnectId: "{{ networkToNetworkInterconnectId }}"
        importRoutePolicy:
          importIpv4RoutePolicyId: "{{ importIpv4RoutePolicyId }}"
          importIpv6RoutePolicyId: "{{ importIpv6RoutePolicyId }}"
        exportRoutePolicy:
          exportIpv4RoutePolicyId: "{{ exportIpv4RoutePolicyId }}"
          exportIpv6RoutePolicyId: "{{ exportIpv6RoutePolicyId }}"
        peeringOption: "{{ peeringOption }}"
        optionBProperties:
          importRouteTargets:
            - "{{ importRouteTargets }}"
          exportRouteTargets:
            - "{{ exportRouteTargets }}"
          routeTargets:
            importIpv4RouteTargets:
              - "{{ importIpv4RouteTargets }}"
            importIpv6RouteTargets:
              - "{{ importIpv6RouteTargets }}"
            exportIpv4RouteTargets:
              - "{{ exportIpv4RouteTargets }}"
            exportIpv6RouteTargets:
              - "{{ exportIpv6RouteTargets }}"
        optionAProperties:
          primaryIpv4Prefix: "{{ primaryIpv4Prefix }}"
          primaryIpv6Prefix: "{{ primaryIpv6Prefix }}"
          secondaryIpv4Prefix: "{{ secondaryIpv4Prefix }}"
          secondaryIpv6Prefix: "{{ secondaryIpv6Prefix }}"
          mtu: {{ mtu }}
          vlanId: {{ vlanId }}
          fabricASN: {{ fabricASN }}
          peerASN: {{ peerASN }}
          bfdConfiguration:
            administrativeState: "{{ administrativeState }}"
            intervalInMilliSeconds: {{ intervalInMilliSeconds }}
            multiplier: {{ multiplier }}
          ingressAclId: "{{ ingressAclId }}"
          bmpConfiguration:
            configurationState: "{{ configurationState }}"
          egressAclId: "{{ egressAclId }}"
          v4OverV6BgpSession: "{{ v4OverV6BgpSession }}"
          v6OverV4BgpSession: "{{ v6OverV4BgpSession }}"
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

API to update certain properties of the ExternalNetworks resource.

```sql
UPDATE azure_extras.managed_network_fabric.external_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' --required
AND external_network_name = '{{ external_network_name }}' --required
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

Implements ExternalNetworks DELETE method.

```sql
DELETE FROM azure_extras.managed_network_fabric.external_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND l3_isolation_domain_name = '{{ l3_isolation_domain_name }}' --required
AND external_network_name = '{{ external_network_name }}' --required
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
        { label: 'update_static_route_bfd_administrative_state', value: 'update_static_route_bfd_administrative_state' },
        { label: 'update_bfd_administrative_state', value: 'update_bfd_administrative_state' }
    ]}
>
<TabItem value="update_administrative_state">

Executes update operation to enable or disable administrative State for externalNetwork.

```sql
EXEC azure_extras.managed_network_fabric.external_networks.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@external_network_name='{{ external_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="update_static_route_bfd_administrative_state">

Update Static Route BFD for external Network.

```sql
EXEC azure_extras.managed_network_fabric.external_networks.update_static_route_bfd_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@external_network_name='{{ external_network_name }}' --required, 
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
EXEC azure_extras.managed_network_fabric.external_networks.update_bfd_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@l3_isolation_domain_name='{{ l3_isolation_domain_name }}' --required, 
@external_network_name='{{ external_network_name }}' --required, 
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
