--- 
title: vpn_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_sites
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

Creates, updates, deletes, gets or lists a <code>vpn_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vpn_sites" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_sites" /></td></tr>
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
    <td><CopyableCode code="addressSpace" /></td>
    <td><code>object</code></td>
    <td>The AddressSpace that contains an array of IP address ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpProperties" /></td>
    <td><code>object</code></td>
    <td>The set of bgp properties.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceProperties" /></td>
    <td><code>object</code></td>
    <td>The device properties.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The ip-address for the vpn-site.</td>
</tr>
<tr>
    <td><CopyableCode code="isSecuritySite" /></td>
    <td><code>boolean</code></td>
    <td>IsSecuritySite flag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="o365Policy" /></td>
    <td><code>object</code></td>
    <td>Office365 Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN site resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="siteKey" /></td>
    <td><code>string</code></td>
    <td>The key for vpn-site that can be used for connections.</td>
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
    <td><CopyableCode code="virtualWan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnSiteLinks" /></td>
    <td><code>array</code></td>
    <td>List of all vpn site links.</td>
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
    <td><CopyableCode code="addressSpace" /></td>
    <td><code>object</code></td>
    <td>The AddressSpace that contains an array of IP address ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpProperties" /></td>
    <td><code>object</code></td>
    <td>The set of bgp properties.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceProperties" /></td>
    <td><code>object</code></td>
    <td>The device properties.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The ip-address for the vpn-site.</td>
</tr>
<tr>
    <td><CopyableCode code="isSecuritySite" /></td>
    <td><code>boolean</code></td>
    <td>IsSecuritySite flag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="o365Policy" /></td>
    <td><code>object</code></td>
    <td>Office365 Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN site resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="siteKey" /></td>
    <td><code>string</code></td>
    <td>The key for vpn-site that can be used for connections.</td>
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
    <td><CopyableCode code="virtualWan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnSiteLinks" /></td>
    <td><code>array</code></td>
    <td>List of all vpn site links.</td>
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
    <td><CopyableCode code="addressSpace" /></td>
    <td><code>object</code></td>
    <td>The AddressSpace that contains an array of IP address ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpProperties" /></td>
    <td><code>object</code></td>
    <td>The set of bgp properties.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceProperties" /></td>
    <td><code>object</code></td>
    <td>The device properties.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The ip-address for the vpn-site.</td>
</tr>
<tr>
    <td><CopyableCode code="isSecuritySite" /></td>
    <td><code>boolean</code></td>
    <td>IsSecuritySite flag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="o365Policy" /></td>
    <td><code>object</code></td>
    <td>Office365 Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN site resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="siteKey" /></td>
    <td><code>string</code></td>
    <td>The key for vpn-site that can be used for connections.</td>
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
    <td><CopyableCode code="virtualWan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnSiteLinks" /></td>
    <td><code>array</code></td>
    <td>List of all vpn site links.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_site_name"><code>vpn_site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a VPN site.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the vpnSites in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the VpnSites in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_site_name"><code>vpn_site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VpnSite resource if it doesn't exist else updates the existing VpnSite.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_site_name"><code>vpn_site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates VpnSite tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_site_name"><code>vpn_site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VpnSite resource if it doesn't exist else updates the existing VpnSite.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vpn_site_name"><code>vpn_site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a VpnSite.</td>
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
<tr id="parameter-vpn_site_name">
    <td><CopyableCode code="vpn_site_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VpnSite being retrieved. Required.</td>
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

Retrieves the details of a VPN site.

```sql
SELECT
id,
name,
addressSpace,
bgpProperties,
deviceProperties,
etag,
ipAddress,
isSecuritySite,
location,
o365Policy,
provisioningState,
siteKey,
tags,
type,
virtualWan,
vpnSiteLinks
FROM azure.network.vpn_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vpn_site_name = '{{ vpn_site_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the vpnSites in a resource group.

```sql
SELECT
id,
name,
addressSpace,
bgpProperties,
deviceProperties,
etag,
ipAddress,
isSecuritySite,
location,
o365Policy,
provisioningState,
siteKey,
tags,
type,
virtualWan,
vpnSiteLinks
FROM azure.network.vpn_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the VpnSites in a subscription.

```sql
SELECT
id,
name,
addressSpace,
bgpProperties,
deviceProperties,
etag,
ipAddress,
isSecuritySite,
location,
o365Policy,
provisioningState,
siteKey,
tags,
type,
virtualWan,
vpnSiteLinks
FROM azure.network.vpn_sites
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

Creates a VpnSite resource if it doesn't exist else updates the existing VpnSite.

```sql
INSERT INTO azure.network.vpn_sites (
id,
location,
tags,
properties,
resource_group_name,
vpn_site_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ vpn_site_name }}',
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
- name: vpn_sites
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the vpn_sites resource.
    - name: vpn_site_name
      value: "{{ vpn_site_name }}"
      description: Required parameter for the vpn_sites resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the vpn_sites resource.
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
        Properties of the VPN site.
      value:
        virtualWan:
          id: "{{ id }}"
        deviceProperties:
          deviceVendor: "{{ deviceVendor }}"
          deviceModel: "{{ deviceModel }}"
          linkSpeedInMbps: {{ linkSpeedInMbps }}
        ipAddress: "{{ ipAddress }}"
        siteKey: "{{ siteKey }}"
        addressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        bgpProperties:
          asn: {{ asn }}
          bgpPeeringAddress: "{{ bgpPeeringAddress }}"
          peerWeight: {{ peerWeight }}
          bgpPeeringAddresses:
            - ipconfigurationId: "{{ ipconfigurationId }}"
              defaultBgpIpAddresses: "{{ defaultBgpIpAddresses }}"
              customBgpIpAddresses: "{{ customBgpIpAddresses }}"
              tunnelIpAddresses: "{{ tunnelIpAddresses }}"
        provisioningState: "{{ provisioningState }}"
        isSecuritySite: {{ isSecuritySite }}
        vpnSiteLinks:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              linkProperties:
                linkProviderName: "{{ linkProviderName }}"
                linkSpeedInMbps: {{ linkSpeedInMbps }}
              ipAddress: "{{ ipAddress }}"
              fqdn: "{{ fqdn }}"
              bgpProperties:
                asn: {{ asn }}
                bgpPeeringAddress: "{{ bgpPeeringAddress }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        o365Policy:
          breakOutCategories:
            allow: {{ allow }}
            optimize: {{ optimize }}
            default: {{ default }}
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

Updates VpnSite tags.

```sql
UPDATE azure.network.vpn_sites
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vpn_site_name = '{{ vpn_site_name }}' --required
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

Creates a VpnSite resource if it doesn't exist else updates the existing VpnSite.

```sql
REPLACE azure.network.vpn_sites
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vpn_site_name = '{{ vpn_site_name }}' --required
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

Deletes a VpnSite.

```sql
DELETE FROM azure.network.vpn_sites
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vpn_site_name = '{{ vpn_site_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
