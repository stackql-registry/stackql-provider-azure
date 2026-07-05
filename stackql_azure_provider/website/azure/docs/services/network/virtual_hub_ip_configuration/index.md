--- 
title: virtual_hub_ip_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_ip_configuration
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

Creates, updates, deletes, gets or lists a <code>virtual_hub_ip_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_hub_ip_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hub_ip_configuration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>The private IP address of the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The private IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the IP configuration resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The reference to the public IP resource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>The private IP address of the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The private IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the IP configuration resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The reference to the public IP resource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-ip_config_name"><code>ip_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a Virtual Hub Ip configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of all VirtualHubIpConfigurations.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-ip_config_name"><code>ip_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VirtualHubIpConfiguration resource if it doesn't exist else updates the existing VirtualHubIpConfiguration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-ip_config_name"><code>ip_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VirtualHubIpConfiguration resource if it doesn't exist else updates the existing VirtualHubIpConfiguration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-ip_config_name"><code>ip_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a VirtualHubIpConfiguration.</td>
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
<tr id="parameter-ip_config_name">
    <td><CopyableCode code="ip_config_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
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
<tr id="parameter-virtual_hub_name">
    <td><CopyableCode code="virtual_hub_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VirtualHub. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the details of a Virtual Hub Ip configuration.

```sql
SELECT
id,
name,
etag,
privateIPAddress,
privateIPAllocationMethod,
provisioningState,
publicIPAddress,
subnet,
type
FROM azure.network.virtual_hub_ip_configuration
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hub_name = '{{ virtual_hub_name }}' -- required
AND ip_config_name = '{{ ip_config_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves the details of all VirtualHubIpConfigurations.

```sql
SELECT
id,
name,
etag,
privateIPAddress,
privateIPAllocationMethod,
provisioningState,
publicIPAddress,
subnet,
type
FROM azure.network.virtual_hub_ip_configuration
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hub_name = '{{ virtual_hub_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates a VirtualHubIpConfiguration resource if it doesn't exist else updates the existing VirtualHubIpConfiguration.

```sql
INSERT INTO azure.network.virtual_hub_ip_configuration (
id,
name,
properties,
resource_group_name,
virtual_hub_name,
ip_config_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_hub_name }}',
'{{ ip_config_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_hub_ip_configuration
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_hub_ip_configuration resource.
    - name: virtual_hub_name
      value: "{{ virtual_hub_name }}"
      description: Required parameter for the virtual_hub_ip_configuration resource.
    - name: ip_config_name
      value: "{{ ip_config_name }}"
      description: Required parameter for the virtual_hub_ip_configuration resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_hub_ip_configuration resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the resource.
    - name: properties
      description: |
        The properties of the Virtual Hub IPConfigurations.
      value:
        privateIPAddress: "{{ privateIPAddress }}"
        privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
        subnet:
          id: "{{ id }}"
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
        publicIPAddress:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
            publicIPAddressVersion: "{{ publicIPAddressVersion }}"
            ipConfiguration:
              id: "{{ id }}"
              properties:
                privateIPAddress: "{{ privateIPAddress }}"
                privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                subnet: "{{ subnet }}"
                publicIPAddress: "{{ publicIPAddress }}"
                provisioningState: "{{ provisioningState }}"
              name: "{{ name }}"
              etag: "{{ etag }}"
            dnsSettings:
              domainNameLabel: "{{ domainNameLabel }}"
              domainNameLabelScope: "{{ domainNameLabelScope }}"
              fqdn: "{{ fqdn }}"
              reverseFqdn: "{{ reverseFqdn }}"
            ddosSettings:
              protectionMode: "{{ protectionMode }}"
              ddosCustomPolicy:
                id: "{{ id }}"
              ddosProtectionPlan:
                id: "{{ id }}"
            ipTags:
              - ipTagType: "{{ ipTagType }}"
                tag: "{{ tag }}"
            ipAddress: "{{ ipAddress }}"
            publicIPPrefix:
              id: "{{ id }}"
            idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
            servicePublicIPAddress:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                ipConfiguration: "{{ ipConfiguration }}"
                dnsSettings: "{{ dnsSettings }}"
                ddosSettings: "{{ ddosSettings }}"
                ipTags: "{{ ipTags }}"
                ipAddress: "{{ ipAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
                servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                natGateway: "{{ natGateway }}"
                migrationPhase: "{{ migrationPhase }}"
                linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                deleteOption: "{{ deleteOption }}"
              extendedLocation:
                name: "{{ name }}"
                type: "{{ type }}"
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            natGateway:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                publicIpAddresses: "{{ publicIpAddresses }}"
                publicIpAddressesV6: "{{ publicIpAddressesV6 }}"
                publicIpPrefixes: "{{ publicIpPrefixes }}"
                publicIpPrefixesV6: "{{ publicIpPrefixesV6 }}"
                subnets: "{{ subnets }}"
                sourceVirtualNetwork: "{{ sourceVirtualNetwork }}"
                serviceGateway: "{{ serviceGateway }}"
                nat64: "{{ nat64 }}"
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
              sku:
                name: "{{ name }}"
              zones:
                - "{{ zones }}"
              etag: "{{ etag }}"
            migrationPhase: "{{ migrationPhase }}"
            linkedPublicIPAddress:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                ipConfiguration: "{{ ipConfiguration }}"
                dnsSettings: "{{ dnsSettings }}"
                ddosSettings: "{{ ddosSettings }}"
                ipTags: "{{ ipTags }}"
                ipAddress: "{{ ipAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
                servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                natGateway: "{{ natGateway }}"
                migrationPhase: "{{ migrationPhase }}"
                linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                deleteOption: "{{ deleteOption }}"
              extendedLocation:
                name: "{{ name }}"
                type: "{{ type }}"
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            deleteOption: "{{ deleteOption }}"
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          sku:
            name: "{{ name }}"
            tier: "{{ tier }}"
          etag: "{{ etag }}"
          zones:
            - "{{ zones }}"
        provisioningState: "{{ provisioningState }}"
`}</CodeBlock>

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

Creates a VirtualHubIpConfiguration resource if it doesn't exist else updates the existing VirtualHubIpConfiguration.

```sql
REPLACE azure.network.virtual_hub_ip_configuration
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND ip_config_name = '{{ ip_config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
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

Deletes a VirtualHubIpConfiguration.

```sql
DELETE FROM azure.network.virtual_hub_ip_configuration
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND ip_config_name = '{{ ip_config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
