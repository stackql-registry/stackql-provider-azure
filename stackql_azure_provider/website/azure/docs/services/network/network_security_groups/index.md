--- 
title: network_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_groups
  - network
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

Creates, updates, deletes, gets or lists a <code>network_security_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_security_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_security_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecurityRules" /></td>
    <td><code>array</code></td>
    <td>The default security rules of network security group.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="flowLogs" /></td>
    <td><code>array</code></td>
    <td>A collection of references to flow log resources.</td>
</tr>
<tr>
    <td><CopyableCode code="flushConnection" /></td>
    <td><code>boolean</code></td>
    <td>When enabled, flows created from Network Security Group connections will be re-evaluated when rules are updates. Initial enablement will trigger re-evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>A collection of references to network interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network security group resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network security group resource.</td>
</tr>
<tr>
    <td><CopyableCode code="securityRules" /></td>
    <td><code>array</code></td>
    <td>A collection of security rules of the network security group.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A collection of references to subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecurityRules" /></td>
    <td><code>array</code></td>
    <td>The default security rules of network security group.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="flowLogs" /></td>
    <td><code>array</code></td>
    <td>A collection of references to flow log resources.</td>
</tr>
<tr>
    <td><CopyableCode code="flushConnection" /></td>
    <td><code>boolean</code></td>
    <td>When enabled, flows created from Network Security Group connections will be re-evaluated when rules are updates. Initial enablement will trigger re-evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>A collection of references to network interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network security group resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network security group resource.</td>
</tr>
<tr>
    <td><CopyableCode code="securityRules" /></td>
    <td><code>array</code></td>
    <td>A collection of security rules of the network security group.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A collection of references to subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecurityRules" /></td>
    <td><code>array</code></td>
    <td>The default security rules of network security group.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="flowLogs" /></td>
    <td><code>array</code></td>
    <td>A collection of references to flow log resources.</td>
</tr>
<tr>
    <td><CopyableCode code="flushConnection" /></td>
    <td><code>boolean</code></td>
    <td>When enabled, flows created from Network Security Group connections will be re-evaluated when rules are updates. Initial enablement will trigger re-evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>A collection of references to network interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network security group resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network security group resource.</td>
</tr>
<tr>
    <td><CopyableCode code="securityRules" /></td>
    <td><code>array</code></td>
    <td>A collection of security rules of the network security group.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A collection of references to subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified network security group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network security groups in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network security groups in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network security group in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a network security group tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network security group in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified network security group.</td>
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
<tr id="parameter-network_security_group_name">
    <td><CopyableCode code="network_security_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network security group. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands referenced resources. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets the specified network security group.

```sql
SELECT
id,
name,
defaultSecurityRules,
etag,
flowLogs,
flushConnection,
location,
networkInterfaces,
provisioningState,
resourceGuid,
securityRules,
subnets,
tags,
type
FROM azure.network.network_security_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_group_name = '{{ network_security_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all network security groups in a resource group.

```sql
SELECT
id,
name,
defaultSecurityRules,
etag,
flowLogs,
flushConnection,
location,
networkInterfaces,
provisioningState,
resourceGuid,
securityRules,
subnets,
tags,
type
FROM azure.network.network_security_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all network security groups in a subscription.

```sql
SELECT
id,
name,
defaultSecurityRules,
etag,
flowLogs,
flushConnection,
location,
networkInterfaces,
provisioningState,
resourceGuid,
securityRules,
subnets,
tags,
type
FROM azure.network.network_security_groups
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

Creates or updates a network security group in the specified resource group.

```sql
INSERT INTO azure.network.network_security_groups (
id,
location,
tags,
properties,
resource_group_name,
network_security_group_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_security_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_security_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_security_groups resource.
    - name: network_security_group_name
      value: "{{ network_security_group_name }}"
      description: Required parameter for the network_security_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_security_groups resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the network security group.
      value:
        flushConnection: {{ flushConnection }}
        securityRules:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              description: "{{ description }}"
              protocol: "{{ protocol }}"
              sourcePortRange: "{{ sourcePortRange }}"
              destinationPortRange: "{{ destinationPortRange }}"
              sourceAddressPrefix: "{{ sourceAddressPrefix }}"
              sourceAddressPrefixes:
                - "{{ sourceAddressPrefixes }}"
              sourceApplicationSecurityGroups:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              destinationAddressPrefix: "{{ destinationAddressPrefix }}"
              destinationAddressPrefixes:
                - "{{ destinationAddressPrefixes }}"
              destinationApplicationSecurityGroups:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              sourcePortRanges:
                - "{{ sourcePortRanges }}"
              destinationPortRanges:
                - "{{ destinationPortRanges }}"
              access: "{{ access }}"
              priority: {{ priority }}
              direction: "{{ direction }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        defaultSecurityRules:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              description: "{{ description }}"
              protocol: "{{ protocol }}"
              sourcePortRange: "{{ sourcePortRange }}"
              destinationPortRange: "{{ destinationPortRange }}"
              sourceAddressPrefix: "{{ sourceAddressPrefix }}"
              sourceAddressPrefixes:
                - "{{ sourceAddressPrefixes }}"
              sourceApplicationSecurityGroups:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              destinationAddressPrefix: "{{ destinationAddressPrefix }}"
              destinationAddressPrefixes:
                - "{{ destinationAddressPrefixes }}"
              destinationApplicationSecurityGroups:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              sourcePortRanges:
                - "{{ sourcePortRanges }}"
              destinationPortRanges:
                - "{{ destinationPortRanges }}"
              access: "{{ access }}"
              priority: {{ priority }}
              direction: "{{ direction }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        networkInterfaces:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              virtualMachine:
                id: "{{ id }}"
              networkSecurityGroup:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  flushConnection: {{ flushConnection }}
                  securityRules: "{{ securityRules }}"
                  defaultSecurityRules: "{{ defaultSecurityRules }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  subnets: "{{ subnets }}"
                  flowLogs: "{{ flowLogs }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
              privateEndpoint:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  subnet: "{{ subnet }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  provisioningState: "{{ provisioningState }}"
                  ipVersionType: "{{ ipVersionType }}"
                  privateLinkServiceConnections: "{{ privateLinkServiceConnections }}"
                  manualPrivateLinkServiceConnections: "{{ manualPrivateLinkServiceConnections }}"
                  customDnsConfigs: "{{ customDnsConfigs }}"
                  applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
                  billingSku: "{{ billingSku }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
              ipConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                    virtualNetworkTaps: "{{ virtualNetworkTaps }}"
                    applicationGatewayBackendAddressPools: "{{ applicationGatewayBackendAddressPools }}"
                    loadBalancerBackendAddressPools: "{{ loadBalancerBackendAddressPools }}"
                    loadBalancerInboundNatRules: "{{ loadBalancerInboundNatRules }}"
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAddressPrefixLength: {{ privateIPAddressPrefixLength }}
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                    subnet: "{{ subnet }}"
                    primary: {{ primary }}
                    publicIPAddress: "{{ publicIPAddress }}"
                    applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                    provisioningState: "{{ provisioningState }}"
                    privateLinkConnectionProperties: "{{ privateLinkConnectionProperties }}"
                  etag: "{{ etag }}"
              tapConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    virtualNetworkTap: "{{ virtualNetworkTap }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              dnsSettings:
                dnsServers:
                  - "{{ dnsServers }}"
                appliedDnsServers:
                  - "{{ appliedDnsServers }}"
                internalDnsNameLabel: "{{ internalDnsNameLabel }}"
                internalFqdn: "{{ internalFqdn }}"
                internalDomainNameSuffix: "{{ internalDomainNameSuffix }}"
              macAddress: "{{ macAddress }}"
              primary: {{ primary }}
              vnetEncryptionSupported: {{ vnetEncryptionSupported }}
              defaultOutboundConnectivityEnabled: {{ defaultOutboundConnectivityEnabled }}
              enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
              disableTcpStateTracking: {{ disableTcpStateTracking }}
              enableIPForwarding: {{ enableIPForwarding }}
              hostedWorkloads:
                - "{{ hostedWorkloads }}"
              dscpConfiguration:
                id: "{{ id }}"
              resourceGuid: "{{ resourceGuid }}"
              provisioningState: "{{ provisioningState }}"
              workloadType: "{{ workloadType }}"
              nicType: "{{ nicType }}"
              privateLinkService:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  loadBalancerFrontendIpConfigurations: "{{ loadBalancerFrontendIpConfigurations }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  destinationIPAddress: "{{ destinationIPAddress }}"
                  accessMode: "{{ accessMode }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  provisioningState: "{{ provisioningState }}"
                  privateEndpointConnections: "{{ privateEndpointConnections }}"
                  visibility: "{{ visibility }}"
                  autoApproval: "{{ autoApproval }}"
                  fqdns: "{{ fqdns }}"
                  alias: "{{ alias }}"
                  enableProxyProtocol: {{ enableProxyProtocol }}
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
              migrationPhase: "{{ migrationPhase }}"
              auxiliaryMode: "{{ auxiliaryMode }}"
              auxiliarySku: "{{ auxiliarySku }}"
            extendedLocation:
              name: "{{ name }}"
              type: "{{ type }}"
            etag: "{{ etag }}"
        subnets:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              addressPrefix: "{{ addressPrefix }}"
              addressPrefixes:
                - "{{ addressPrefixes }}"
              networkSecurityGroup:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  flushConnection: {{ flushConnection }}
                  securityRules: "{{ securityRules }}"
                  defaultSecurityRules: "{{ defaultSecurityRules }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  subnets: "{{ subnets }}"
                  flowLogs: "{{ flowLogs }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
              routeTable:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  routes: "{{ routes }}"
                  subnets: "{{ subnets }}"
                  disableBgpRoutePropagation: {{ disableBgpRoutePropagation }}
                  disablePeeringRoute: "{{ disablePeeringRoute }}"
                  provisioningState: "{{ provisioningState }}"
                  resourceGuid: "{{ resourceGuid }}"
                etag: "{{ etag }}"
              natGateway:
                id: "{{ id }}"
              serviceEndpoints:
                - service: "{{ service }}"
                  networkIdentifier:
                    id: "{{ id }}"
                  locations: "{{ locations }}"
                  provisioningState: "{{ provisioningState }}"
              serviceEndpointPolicies:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    serviceEndpointPolicyDefinitions: "{{ serviceEndpointPolicyDefinitions }}"
                    subnets: "{{ subnets }}"
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                    serviceAlias: "{{ serviceAlias }}"
                    contextualServiceEndpointPolicies: "{{ contextualServiceEndpointPolicies }}"
                  etag: "{{ etag }}"
                  kind: "{{ kind }}"
              privateEndpoints:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    subnet: "{{ subnet }}"
                    networkInterfaces: "{{ networkInterfaces }}"
                    provisioningState: "{{ provisioningState }}"
                    ipVersionType: "{{ ipVersionType }}"
                    privateLinkServiceConnections: "{{ privateLinkServiceConnections }}"
                    manualPrivateLinkServiceConnections: "{{ manualPrivateLinkServiceConnections }}"
                    customDnsConfigs: "{{ customDnsConfigs }}"
                    applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                    ipConfigurations: "{{ ipConfigurations }}"
                    customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
                    billingSku: "{{ billingSku }}"
                  extendedLocation:
                    name: "{{ name }}"
                    type: "{{ type }}"
                  etag: "{{ etag }}"
              ipConfigurations:
                - id: "{{ id }}"
                  properties:
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    subnet: "{{ subnet }}"
                    publicIPAddress: "{{ publicIPAddress }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
              ipConfigurationProfiles:
                - id: "{{ id }}"
                  properties:
                    subnet: "{{ subnet }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  etag: "{{ etag }}"
              ipAllocations:
                - id: "{{ id }}"
              resourceNavigationLinks:
                - id: "{{ id }}"
                  properties:
                    linkedResourceType: "{{ linkedResourceType }}"
                    link: "{{ link }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              serviceAssociationLinks:
                - id: "{{ id }}"
                  properties:
                    linkedResourceType: "{{ linkedResourceType }}"
                    link: "{{ link }}"
                    provisioningState: "{{ provisioningState }}"
                    allowDelete: {{ allowDelete }}
                    locations: "{{ locations }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              delegations:
                - id: "{{ id }}"
                  properties:
                    serviceName: "{{ serviceName }}"
                    actions: "{{ actions }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              purpose: "{{ purpose }}"
              provisioningState: "{{ provisioningState }}"
              privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
              privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
              applicationGatewayIPConfigurations:
                - id: "{{ id }}"
                  properties:
                    subnet: "{{ subnet }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              sharingScope: "{{ sharingScope }}"
              defaultOutboundAccess: {{ defaultOutboundAccess }}
              ipamPoolPrefixAllocations:
                - pool:
                    id: "{{ id }}"
                  numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                  allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
              serviceGateway:
                id: "{{ id }}"
            etag: "{{ etag }}"
        flowLogs:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              targetResourceId: "{{ targetResourceId }}"
              targetResourceGuid: "{{ targetResourceGuid }}"
              storageId: "{{ storageId }}"
              enabledFilteringCriteria: "{{ enabledFilteringCriteria }}"
              recordTypes: "{{ recordTypes }}"
              enabled: {{ enabled }}
              retentionPolicy:
                days: {{ days }}
                enabled: {{ enabled }}
              format:
                type: "{{ type }}"
                version: {{ version }}
              flowAnalyticsConfiguration:
                networkWatcherFlowAnalyticsConfiguration:
                  enabled: {{ enabled }}
                  workspaceId: "{{ workspaceId }}"
                  workspaceRegion: "{{ workspaceRegion }}"
                  workspaceResourceId: "{{ workspaceResourceId }}"
                  trafficAnalyticsInterval: {{ trafficAnalyticsInterval }}
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
            identity:
              principalId: "{{ principalId }}"
              tenantId: "{{ tenantId }}"
              type: "{{ type }}"
              userAssignedIdentities: "{{ userAssignedIdentities }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates a network security group tags.

```sql
UPDATE azure.network.network_security_groups
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_security_group_name = '{{ network_security_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
tags,
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

Creates or updates a network security group in the specified resource group.

```sql
REPLACE azure.network.network_security_groups
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_security_group_name = '{{ network_security_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Deletes the specified network security group.

```sql
DELETE FROM azure.network.network_security_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_security_group_name = '{{ network_security_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
