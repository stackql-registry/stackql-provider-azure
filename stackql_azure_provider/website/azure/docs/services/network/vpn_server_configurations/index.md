--- 
title: vpn_server_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_server_configurations
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

Creates, updates, deletes, gets or lists a <code>vpn_server_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vpn_server_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_server_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="aadAuthenticationParameters" /></td>
    <td><code>object</code></td>
    <td>The set of aad vpn authentication parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationPolicyGroups" /></td>
    <td><code>array</code></td>
    <td>List of all VpnServerConfigurationPolicyGroups.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SVpnGateways" /></td>
    <td><code>array</code></td>
    <td>List of references to P2SVpnGateways.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VpnServerConfiguration resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusClientRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Radius client root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerAddress" /></td>
    <td><code>string</code></td>
    <td>The radius server address property of the VpnServerConfiguration resource for point to site client connection.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Radius Server root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerSecret" /></td>
    <td><code>string</code></td>
    <td>The radius secret property of the VpnServerConfiguration resource for point to site client connection. We will no longer return radiusServerSecret in VpnServerConfiguration Create/Update/Get/List/UpdateTags APIs response. Please use VpnServerConfiguration ListRadiusSecrets API to fetch radius server secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServers" /></td>
    <td><code>array</code></td>
    <td>Multiple Radius Server configuration for VpnServerConfiguration.</td>
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
<tr>
    <td><CopyableCode code="vpnAuthenticationTypes" /></td>
    <td><code>array</code></td>
    <td>VPN authentication types for the VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientIpsecPolicies" /></td>
    <td><code>array</code></td>
    <td>VpnClientIpsecPolicies for VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientRevokedCertificates" /></td>
    <td><code>array</code></td>
    <td>VPN client revoked certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientRootCertificates" /></td>
    <td><code>array</code></td>
    <td>VPN client root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnProtocols" /></td>
    <td><code>array</code></td>
    <td>VPN protocols for the VpnServerConfiguration.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="aadAuthenticationParameters" /></td>
    <td><code>object</code></td>
    <td>The set of aad vpn authentication parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationPolicyGroups" /></td>
    <td><code>array</code></td>
    <td>List of all VpnServerConfigurationPolicyGroups.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SVpnGateways" /></td>
    <td><code>array</code></td>
    <td>List of references to P2SVpnGateways.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VpnServerConfiguration resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusClientRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Radius client root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerAddress" /></td>
    <td><code>string</code></td>
    <td>The radius server address property of the VpnServerConfiguration resource for point to site client connection.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Radius Server root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerSecret" /></td>
    <td><code>string</code></td>
    <td>The radius secret property of the VpnServerConfiguration resource for point to site client connection. We will no longer return radiusServerSecret in VpnServerConfiguration Create/Update/Get/List/UpdateTags APIs response. Please use VpnServerConfiguration ListRadiusSecrets API to fetch radius server secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServers" /></td>
    <td><code>array</code></td>
    <td>Multiple Radius Server configuration for VpnServerConfiguration.</td>
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
<tr>
    <td><CopyableCode code="vpnAuthenticationTypes" /></td>
    <td><code>array</code></td>
    <td>VPN authentication types for the VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientIpsecPolicies" /></td>
    <td><code>array</code></td>
    <td>VpnClientIpsecPolicies for VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientRevokedCertificates" /></td>
    <td><code>array</code></td>
    <td>VPN client revoked certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientRootCertificates" /></td>
    <td><code>array</code></td>
    <td>VPN client root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnProtocols" /></td>
    <td><code>array</code></td>
    <td>VPN protocols for the VpnServerConfiguration.</td>
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
    <td><CopyableCode code="aadAuthenticationParameters" /></td>
    <td><code>object</code></td>
    <td>The set of aad vpn authentication parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationPolicyGroups" /></td>
    <td><code>array</code></td>
    <td>List of all VpnServerConfigurationPolicyGroups.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SVpnGateways" /></td>
    <td><code>array</code></td>
    <td>List of references to P2SVpnGateways.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VpnServerConfiguration resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusClientRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Radius client root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerAddress" /></td>
    <td><code>string</code></td>
    <td>The radius server address property of the VpnServerConfiguration resource for point to site client connection.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Radius Server root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServerSecret" /></td>
    <td><code>string</code></td>
    <td>The radius secret property of the VpnServerConfiguration resource for point to site client connection. We will no longer return radiusServerSecret in VpnServerConfiguration Create/Update/Get/List/UpdateTags APIs response. Please use VpnServerConfiguration ListRadiusSecrets API to fetch radius server secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="radiusServers" /></td>
    <td><code>array</code></td>
    <td>Multiple Radius Server configuration for VpnServerConfiguration.</td>
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
<tr>
    <td><CopyableCode code="vpnAuthenticationTypes" /></td>
    <td><code>array</code></td>
    <td>VPN authentication types for the VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientIpsecPolicies" /></td>
    <td><code>array</code></td>
    <td>VpnClientIpsecPolicies for VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientRevokedCertificates" /></td>
    <td><code>array</code></td>
    <td>VPN client revoked certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientRootCertificates" /></td>
    <td><code>array</code></td>
    <td>VPN client root certificate of VpnServerConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnProtocols" /></td>
    <td><code>array</code></td>
    <td>VPN protocols for the VpnServerConfiguration.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_server_configuration_name"><code>vpn_server_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a VpnServerConfiguration.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the vpnServerConfigurations in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the VpnServerConfigurations in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_server_configuration_name"><code>vpn_server_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VpnServerConfiguration resource if it doesn't exist else updates the existing VpnServerConfiguration.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_server_configuration_name"><code>vpn_server_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates VpnServerConfiguration tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_server_configuration_name"><code>vpn_server_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VpnServerConfiguration resource if it doesn't exist else updates the existing VpnServerConfiguration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_server_configuration_name"><code>vpn_server_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a VpnServerConfiguration.</td>
</tr>
<tr>
    <td><a href="#list_radius_secrets"><CopyableCode code="list_radius_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_server_configuration_name"><code>vpn_server_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Radius servers with respective radius secrets from VpnServerConfiguration.</td>
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
<tr id="parameter-vpn_server_configuration_name">
    <td><CopyableCode code="vpn_server_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the details of a VpnServerConfiguration.

```sql
SELECT
id,
name,
aadAuthenticationParameters,
configurationPolicyGroups,
etag,
location,
p2SVpnGateways,
provisioningState,
radiusClientRootCertificates,
radiusServerAddress,
radiusServerRootCertificates,
radiusServerSecret,
radiusServers,
tags,
type,
vpnAuthenticationTypes,
vpnClientIpsecPolicies,
vpnClientRevokedCertificates,
vpnClientRootCertificates,
vpnProtocols
FROM azure.network.vpn_server_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vpn_server_configuration_name = '{{ vpn_server_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the vpnServerConfigurations in a resource group.

```sql
SELECT
id,
name,
aadAuthenticationParameters,
configurationPolicyGroups,
etag,
location,
p2SVpnGateways,
provisioningState,
radiusClientRootCertificates,
radiusServerAddress,
radiusServerRootCertificates,
radiusServerSecret,
radiusServers,
tags,
type,
vpnAuthenticationTypes,
vpnClientIpsecPolicies,
vpnClientRevokedCertificates,
vpnClientRootCertificates,
vpnProtocols
FROM azure.network.vpn_server_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the VpnServerConfigurations in a subscription.

```sql
SELECT
id,
name,
aadAuthenticationParameters,
configurationPolicyGroups,
etag,
location,
p2SVpnGateways,
provisioningState,
radiusClientRootCertificates,
radiusServerAddress,
radiusServerRootCertificates,
radiusServerSecret,
radiusServers,
tags,
type,
vpnAuthenticationTypes,
vpnClientIpsecPolicies,
vpnClientRevokedCertificates,
vpnClientRootCertificates,
vpnProtocols
FROM azure.network.vpn_server_configurations
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

Creates a VpnServerConfiguration resource if it doesn't exist else updates the existing VpnServerConfiguration.

```sql
INSERT INTO azure.network.vpn_server_configurations (
id,
name,
location,
tags,
properties,
resource_group_name,
vpn_server_configuration_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ vpn_server_configuration_name }}',
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
- name: vpn_server_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the vpn_server_configurations resource.
    - name: vpn_server_configuration_name
      value: "{{ vpn_server_configuration_name }}"
      description: Required parameter for the vpn_server_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the vpn_server_configurations resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name.
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
        Properties of the P2SVpnServer configuration.
      value:
        name: "{{ name }}"
        vpnProtocols:
          - "{{ vpnProtocols }}"
        vpnAuthenticationTypes:
          - "{{ vpnAuthenticationTypes }}"
        vpnClientRootCertificates:
          - name: "{{ name }}"
            publicCertData: "{{ publicCertData }}"
        vpnClientRevokedCertificates:
          - name: "{{ name }}"
            thumbprint: "{{ thumbprint }}"
        radiusServerRootCertificates:
          - name: "{{ name }}"
            publicCertData: "{{ publicCertData }}"
        radiusClientRootCertificates:
          - name: "{{ name }}"
            thumbprint: "{{ thumbprint }}"
        vpnClientIpsecPolicies:
          - saLifeTimeSeconds: {{ saLifeTimeSeconds }}
            saDataSizeKilobytes: {{ saDataSizeKilobytes }}
            ipsecEncryption: "{{ ipsecEncryption }}"
            ipsecIntegrity: "{{ ipsecIntegrity }}"
            ikeEncryption: "{{ ikeEncryption }}"
            ikeIntegrity: "{{ ikeIntegrity }}"
            dhGroup: "{{ dhGroup }}"
            pfsGroup: "{{ pfsGroup }}"
        radiusServerAddress: "{{ radiusServerAddress }}"
        radiusServerSecret: "{{ radiusServerSecret }}"
        radiusServers:
          - radiusServerAddress: "{{ radiusServerAddress }}"
            radiusServerScore: {{ radiusServerScore }}
            radiusServerSecret: "{{ radiusServerSecret }}"
        aadAuthenticationParameters:
          aadTenant: "{{ aadTenant }}"
          aadAudience: "{{ aadAudience }}"
          aadIssuer: "{{ aadIssuer }}"
        provisioningState: "{{ provisioningState }}"
        p2SVpnGateways:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              virtualHub:
                id: "{{ id }}"
              p2SConnectionConfigurations:
                - id: "{{ id }}"
                  properties:
                    vpnClientAddressPool: "{{ vpnClientAddressPool }}"
                    routingConfiguration: "{{ routingConfiguration }}"
                    enableInternetSecurity: {{ enableInternetSecurity }}
                    configurationPolicyGroupAssociations: "{{ configurationPolicyGroupAssociations }}"
                    previousConfigurationPolicyGroupAssociations: "{{ previousConfigurationPolicyGroupAssociations }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
              provisioningState: "{{ provisioningState }}"
              vpnGatewayScaleUnit: {{ vpnGatewayScaleUnit }}
              vpnServerConfiguration:
                id: "{{ id }}"
              vpnClientConnectionHealth:
                totalIngressBytesTransferred: {{ totalIngressBytesTransferred }}
                totalEgressBytesTransferred: {{ totalEgressBytesTransferred }}
                vpnClientConnectionsCount: {{ vpnClientConnectionsCount }}
                allocatedIpAddresses:
                  - "{{ allocatedIpAddresses }}"
              customDnsServers:
                - "{{ customDnsServers }}"
              isRoutingPreferenceInternet: {{ isRoutingPreferenceInternet }}
            etag: "{{ etag }}"
        configurationPolicyGroups:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              isDefault: {{ isDefault }}
              priority: {{ priority }}
              policyMembers:
                - name: "{{ name }}"
                  attributeType: "{{ attributeType }}"
                  attributeValue: "{{ attributeValue }}"
              p2SConnectionConfigurations:
                - id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        etag: "{{ etag }}"
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

Updates VpnServerConfiguration tags.

```sql
UPDATE azure.network.vpn_server_configurations
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vpn_server_configuration_name = '{{ vpn_server_configuration_name }}' --required
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

Creates a VpnServerConfiguration resource if it doesn't exist else updates the existing VpnServerConfiguration.

```sql
REPLACE azure.network.vpn_server_configurations
SET 
id = '{{ id }}',
name = '{{ name }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vpn_server_configuration_name = '{{ vpn_server_configuration_name }}' --required
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

Deletes a VpnServerConfiguration.

```sql
DELETE FROM azure.network.vpn_server_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vpn_server_configuration_name = '{{ vpn_server_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_radius_secrets"
    values={[
        { label: 'list_radius_secrets', value: 'list_radius_secrets' }
    ]}
>
<TabItem value="list_radius_secrets">

List all Radius servers with respective radius secrets from VpnServerConfiguration.

```sql
EXEC azure.network.vpn_server_configurations.list_radius_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@vpn_server_configuration_name='{{ vpn_server_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
