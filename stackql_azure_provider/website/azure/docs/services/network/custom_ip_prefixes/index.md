--- 
title: custom_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_ip_prefixes
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

Creates, updates, deletes, gets or lists a <code>custom_ip_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_ip_prefixes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.custom_ip_prefixes" /></td></tr>
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
    <td><CopyableCode code="asn" /></td>
    <td><code>string</code></td>
    <td>The ASN for CIDR advertising. Should be an integer as string.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationMessage" /></td>
    <td><code>string</code></td>
    <td>Authorization message for WAN validation.</td>
</tr>
<tr>
    <td><CopyableCode code="childCustomIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>The list of all Children for IPv6 /48 CustomIpPrefix.</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>The prefix range in CIDR notation. Should include the start address and the prefix length.</td>
</tr>
<tr>
    <td><CopyableCode code="commissionedState" /></td>
    <td><code>string</code></td>
    <td>The commissioned state of the Custom IP Prefix. Known values are: "Provisioning", "Provisioned", "Commissioning", "CommissionedNoInternetAdvertise", "Commissioned", "Decommissioning", "Deprovisioning", and "Deprovisioned". (Provisioning, Provisioned, Commissioning, CommissionedNoInternetAdvertise, Commissioned, Decommissioning, Deprovisioning, Deprovisioned)</td>
</tr>
<tr>
    <td><CopyableCode code="customIpPrefixParent" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteAdvertise" /></td>
    <td><code>boolean</code></td>
    <td>Whether to do express route advertise.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the custom IP prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="failedReason" /></td>
    <td><code>string</code></td>
    <td>The reason why resource is in failed state.</td>
</tr>
<tr>
    <td><CopyableCode code="geo" /></td>
    <td><code>string</code></td>
    <td>The Geo for CIDR advertising. Should be an Geo code. Known values are: "GLOBAL", "AFRI", "APAC", "EURO", "LATAM", "NAM", "ME", "OCEANIA", and "AQ". (GLOBAL, AFRI, APAC, EURO, LATAM, NAM, ME, OCEANIA, AQ)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="noInternetAdvertise" /></td>
    <td><code>boolean</code></td>
    <td>Whether to Advertise the range to Internet.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixType" /></td>
    <td><code>string</code></td>
    <td>Type of custom IP prefix. Should be Singular, Parent, or Child. Known values are: "Singular", "Parent", and "Child". (Singular, Parent, Child)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the custom IP prefix resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>The list of all referenced PublicIpPrefixes.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the custom IP prefix resource.</td>
</tr>
<tr>
    <td><CopyableCode code="signedMessage" /></td>
    <td><code>string</code></td>
    <td>Signed message for WAN validation.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><CopyableCode code="asn" /></td>
    <td><code>string</code></td>
    <td>The ASN for CIDR advertising. Should be an integer as string.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationMessage" /></td>
    <td><code>string</code></td>
    <td>Authorization message for WAN validation.</td>
</tr>
<tr>
    <td><CopyableCode code="childCustomIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>The list of all Children for IPv6 /48 CustomIpPrefix.</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>The prefix range in CIDR notation. Should include the start address and the prefix length.</td>
</tr>
<tr>
    <td><CopyableCode code="commissionedState" /></td>
    <td><code>string</code></td>
    <td>The commissioned state of the Custom IP Prefix. Known values are: "Provisioning", "Provisioned", "Commissioning", "CommissionedNoInternetAdvertise", "Commissioned", "Decommissioning", "Deprovisioning", and "Deprovisioned". (Provisioning, Provisioned, Commissioning, CommissionedNoInternetAdvertise, Commissioned, Decommissioning, Deprovisioning, Deprovisioned)</td>
</tr>
<tr>
    <td><CopyableCode code="customIpPrefixParent" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteAdvertise" /></td>
    <td><code>boolean</code></td>
    <td>Whether to do express route advertise.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the custom IP prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="failedReason" /></td>
    <td><code>string</code></td>
    <td>The reason why resource is in failed state.</td>
</tr>
<tr>
    <td><CopyableCode code="geo" /></td>
    <td><code>string</code></td>
    <td>The Geo for CIDR advertising. Should be an Geo code. Known values are: "GLOBAL", "AFRI", "APAC", "EURO", "LATAM", "NAM", "ME", "OCEANIA", and "AQ". (GLOBAL, AFRI, APAC, EURO, LATAM, NAM, ME, OCEANIA, AQ)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="noInternetAdvertise" /></td>
    <td><code>boolean</code></td>
    <td>Whether to Advertise the range to Internet.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixType" /></td>
    <td><code>string</code></td>
    <td>Type of custom IP prefix. Should be Singular, Parent, or Child. Known values are: "Singular", "Parent", and "Child". (Singular, Parent, Child)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the custom IP prefix resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>The list of all referenced PublicIpPrefixes.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the custom IP prefix resource.</td>
</tr>
<tr>
    <td><CopyableCode code="signedMessage" /></td>
    <td><code>string</code></td>
    <td>Signed message for WAN validation.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><CopyableCode code="asn" /></td>
    <td><code>string</code></td>
    <td>The ASN for CIDR advertising. Should be an integer as string.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationMessage" /></td>
    <td><code>string</code></td>
    <td>Authorization message for WAN validation.</td>
</tr>
<tr>
    <td><CopyableCode code="childCustomIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>The list of all Children for IPv6 /48 CustomIpPrefix.</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>The prefix range in CIDR notation. Should include the start address and the prefix length.</td>
</tr>
<tr>
    <td><CopyableCode code="commissionedState" /></td>
    <td><code>string</code></td>
    <td>The commissioned state of the Custom IP Prefix. Known values are: "Provisioning", "Provisioned", "Commissioning", "CommissionedNoInternetAdvertise", "Commissioned", "Decommissioning", "Deprovisioning", and "Deprovisioned". (Provisioning, Provisioned, Commissioning, CommissionedNoInternetAdvertise, Commissioned, Decommissioning, Deprovisioning, Deprovisioned)</td>
</tr>
<tr>
    <td><CopyableCode code="customIpPrefixParent" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteAdvertise" /></td>
    <td><code>boolean</code></td>
    <td>Whether to do express route advertise.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the custom IP prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="failedReason" /></td>
    <td><code>string</code></td>
    <td>The reason why resource is in failed state.</td>
</tr>
<tr>
    <td><CopyableCode code="geo" /></td>
    <td><code>string</code></td>
    <td>The Geo for CIDR advertising. Should be an Geo code. Known values are: "GLOBAL", "AFRI", "APAC", "EURO", "LATAM", "NAM", "ME", "OCEANIA", and "AQ". (GLOBAL, AFRI, APAC, EURO, LATAM, NAM, ME, OCEANIA, AQ)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="noInternetAdvertise" /></td>
    <td><code>boolean</code></td>
    <td>Whether to Advertise the range to Internet.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixType" /></td>
    <td><code>string</code></td>
    <td>Type of custom IP prefix. Should be Singular, Parent, or Child. Known values are: "Singular", "Parent", and "Child". (Singular, Parent, Child)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the custom IP prefix resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>The list of all referenced PublicIpPrefixes.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the custom IP prefix resource.</td>
</tr>
<tr>
    <td><CopyableCode code="signedMessage" /></td>
    <td><code>string</code></td>
    <td>Signed message for WAN validation.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-custom_ip_prefix_name"><code>custom_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified custom IP prefix in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all custom IP prefixes in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the custom IP prefixes in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-custom_ip_prefix_name"><code>custom_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a custom IP prefix.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-custom_ip_prefix_name"><code>custom_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates custom IP prefix tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-custom_ip_prefix_name"><code>custom_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a custom IP prefix.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-custom_ip_prefix_name"><code>custom_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified custom IP prefix.</td>
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
<tr id="parameter-custom_ip_prefix_name">
    <td><CopyableCode code="custom_ip_prefix_name" /></td>
    <td><code>string</code></td>
    <td>The name of the custom IP prefix. Required.</td>
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

Gets the specified custom IP prefix in a specified resource group.

```sql
SELECT
id,
name,
asn,
authorizationMessage,
childCustomIpPrefixes,
cidr,
commissionedState,
customIpPrefixParent,
etag,
expressRouteAdvertise,
extendedLocation,
failedReason,
geo,
location,
noInternetAdvertise,
prefixType,
provisioningState,
publicIpPrefixes,
resourceGuid,
signedMessage,
tags,
type,
zones
FROM azure.network.custom_ip_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND custom_ip_prefix_name = '{{ custom_ip_prefix_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all custom IP prefixes in a resource group.

```sql
SELECT
id,
name,
asn,
authorizationMessage,
childCustomIpPrefixes,
cidr,
commissionedState,
customIpPrefixParent,
etag,
expressRouteAdvertise,
extendedLocation,
failedReason,
geo,
location,
noInternetAdvertise,
prefixType,
provisioningState,
publicIpPrefixes,
resourceGuid,
signedMessage,
tags,
type,
zones
FROM azure.network.custom_ip_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the custom IP prefixes in a subscription.

```sql
SELECT
id,
name,
asn,
authorizationMessage,
childCustomIpPrefixes,
cidr,
commissionedState,
customIpPrefixParent,
etag,
expressRouteAdvertise,
extendedLocation,
failedReason,
geo,
location,
noInternetAdvertise,
prefixType,
provisioningState,
publicIpPrefixes,
resourceGuid,
signedMessage,
tags,
type,
zones
FROM azure.network.custom_ip_prefixes
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

Creates or updates a custom IP prefix.

```sql
INSERT INTO azure.network.custom_ip_prefixes (
id,
location,
tags,
properties,
extendedLocation,
zones,
resource_group_name,
custom_ip_prefix_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ custom_ip_prefix_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: custom_ip_prefixes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the custom_ip_prefixes resource.
    - name: custom_ip_prefix_name
      value: "{{ custom_ip_prefix_name }}"
      description: Required parameter for the custom_ip_prefixes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the custom_ip_prefixes resource.
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
        Custom IP prefix properties.
      value:
        asn: "{{ asn }}"
        cidr: "{{ cidr }}"
        signedMessage: "{{ signedMessage }}"
        authorizationMessage: "{{ authorizationMessage }}"
        customIpPrefixParent:
          id: "{{ id }}"
        childCustomIpPrefixes:
          - id: "{{ id }}"
        commissionedState: "{{ commissionedState }}"
        expressRouteAdvertise: {{ expressRouteAdvertise }}
        geo: "{{ geo }}"
        noInternetAdvertise: {{ noInternetAdvertise }}
        prefixType: "{{ prefixType }}"
        publicIpPrefixes:
          - id: "{{ id }}"
        resourceGuid: "{{ resourceGuid }}"
        failedReason: "{{ failedReason }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extended location of the custom IP prefix.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting where the resource needs to come from.
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

Updates custom IP prefix tags.

```sql
UPDATE azure.network.custom_ip_prefixes
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND custom_ip_prefix_name = '{{ custom_ip_prefix_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
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

Creates or updates a custom IP prefix.

```sql
REPLACE azure.network.custom_ip_prefixes
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND custom_ip_prefix_name = '{{ custom_ip_prefix_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
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

Deletes the specified custom IP prefix.

```sql
DELETE FROM azure.network.custom_ip_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND custom_ip_prefix_name = '{{ custom_ip_prefix_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
