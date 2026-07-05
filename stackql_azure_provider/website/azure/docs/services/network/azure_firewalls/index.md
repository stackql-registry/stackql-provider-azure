--- 
title: azure_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewalls
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

Creates, updates, deletes, gets or lists an <code>azure_firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="azure_firewalls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.azure_firewalls" /></td></tr>
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
    <td><CopyableCode code="additionalProperties" /></td>
    <td><code>object</code></td>
    <td>The additional properties used to further config this azure firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="afcConfiguration" /></td>
    <td><code>object</code></td>
    <td>AFC configuration for the Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of application rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="autoscaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Properties to provide a custom autoscale configuration to this azure firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of type local virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallPolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="hubIPAddresses" /></td>
    <td><code>object</code></td>
    <td>IP addresses associated with AzureFirewall.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configuration of the Azure Firewall resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipGroups" /></td>
    <td><code>array</code></td>
    <td>IpGroups associated with AzureFirewall.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration of an Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="natRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of NAT rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of network rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Azure firewall resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Azure Firewall Resource SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelMode" /></td>
    <td><code>string</code></td>
    <td>The operation mode for Threat Intelligence. Known values are: "Alert", "Deny", and "Off". (Alert, Deny, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="additionalProperties" /></td>
    <td><code>object</code></td>
    <td>The additional properties used to further config this azure firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="afcConfiguration" /></td>
    <td><code>object</code></td>
    <td>AFC configuration for the Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of application rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="autoscaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Properties to provide a custom autoscale configuration to this azure firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of type local virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallPolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="hubIPAddresses" /></td>
    <td><code>object</code></td>
    <td>IP addresses associated with AzureFirewall.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configuration of the Azure Firewall resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipGroups" /></td>
    <td><code>array</code></td>
    <td>IpGroups associated with AzureFirewall.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration of an Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="natRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of NAT rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of network rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Azure firewall resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Azure Firewall Resource SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelMode" /></td>
    <td><code>string</code></td>
    <td>The operation mode for Threat Intelligence. Known values are: "Alert", "Deny", and "Off". (Alert, Deny, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="additionalProperties" /></td>
    <td><code>object</code></td>
    <td>The additional properties used to further config this azure firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="afcConfiguration" /></td>
    <td><code>object</code></td>
    <td>AFC configuration for the Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of application rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="autoscaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Properties to provide a custom autoscale configuration to this azure firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of type local virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallPolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="hubIPAddresses" /></td>
    <td><code>object</code></td>
    <td>IP addresses associated with AzureFirewall.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configuration of the Azure Firewall resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipGroups" /></td>
    <td><code>array</code></td>
    <td>IpGroups associated with AzureFirewall.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration of an Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="natRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of NAT rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleCollections" /></td>
    <td><code>array</code></td>
    <td>Collection of network rule collections used by Azure Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Azure firewall resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Azure Firewall Resource SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelMode" /></td>
    <td><code>string</code></td>
    <td>The operation mode for Threat Intelligence. Known values are: "Alert", "Deny", and "Off". (Alert, Deny, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified Azure Firewall.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Azure Firewalls in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the Azure Firewalls in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-createAfcControlPlane"><code>createAfcControlPlane</code></a></td>
    <td>Creates or updates the specified Azure Firewall.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags of an Azure Firewall resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-createAfcControlPlane"><code>createAfcControlPlane</code></a></td>
    <td>Creates or updates the specified Azure Firewall.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Azure Firewall.</td>
</tr>
<tr>
    <td><a href="#list_learned_prefixes"><CopyableCode code="list_learned_prefixes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a list of all IP prefixes that azure firewall has learned to not SNAT.</td>
</tr>
<tr>
    <td><a href="#packet_capture"><CopyableCode code="packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Runs a packet capture on AzureFirewall.</td>
</tr>
<tr>
    <td><a href="#packet_capture_operation"><CopyableCode code="packet_capture_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_firewall_name"><code>azure_firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Runs a packet capture operation on AzureFirewall.</td>
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
<tr id="parameter-azure_firewall_name">
    <td><CopyableCode code="azure_firewall_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure Firewall. Required.</td>
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
<tr id="parameter-createAfcControlPlane">
    <td><CopyableCode code="createAfcControlPlane" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, creates an AFC control plane for the Azure Firewall. Default value is None.</td>
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

Gets the specified Azure Firewall.

```sql
SELECT
id,
name,
additionalProperties,
afcConfiguration,
applicationRuleCollections,
autoscaleConfiguration,
etag,
extendedLocation,
firewallPolicy,
hubIPAddresses,
ipConfigurations,
ipGroups,
location,
managementIpConfiguration,
natRuleCollections,
networkRuleCollections,
provisioningState,
sku,
tags,
threatIntelMode,
type,
virtualHub,
zones
FROM azure.network.azure_firewalls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_firewall_name = '{{ azure_firewall_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Azure Firewalls in a resource group.

```sql
SELECT
id,
name,
additionalProperties,
afcConfiguration,
applicationRuleCollections,
autoscaleConfiguration,
etag,
extendedLocation,
firewallPolicy,
hubIPAddresses,
ipConfigurations,
ipGroups,
location,
managementIpConfiguration,
natRuleCollections,
networkRuleCollections,
provisioningState,
sku,
tags,
threatIntelMode,
type,
virtualHub,
zones
FROM azure.network.azure_firewalls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the Azure Firewalls in a subscription.

```sql
SELECT
id,
name,
additionalProperties,
afcConfiguration,
applicationRuleCollections,
autoscaleConfiguration,
etag,
extendedLocation,
firewallPolicy,
hubIPAddresses,
ipConfigurations,
ipGroups,
location,
managementIpConfiguration,
natRuleCollections,
networkRuleCollections,
provisioningState,
sku,
tags,
threatIntelMode,
type,
virtualHub,
zones
FROM azure.network.azure_firewalls
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

Creates or updates the specified Azure Firewall.

```sql
INSERT INTO azure.network.azure_firewalls (
id,
location,
tags,
properties,
extendedLocation,
zones,
resource_group_name,
azure_firewall_name,
subscription_id,
createAfcControlPlane
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ azure_firewall_name }}',
'{{ subscription_id }}',
'{{ createAfcControlPlane }}'
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
- name: azure_firewalls
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the azure_firewalls resource.
    - name: azure_firewall_name
      value: "{{ azure_firewall_name }}"
      description: Required parameter for the azure_firewalls resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the azure_firewalls resource.
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
        Properties of the azure firewall.
      value:
        applicationRuleCollections:
          - id: "{{ id }}"
            properties:
              priority: {{ priority }}
              action:
                type: "{{ type }}"
              rules:
                - name: "{{ name }}"
                  description: "{{ description }}"
                  sourceAddresses: "{{ sourceAddresses }}"
                  protocols: "{{ protocols }}"
                  targetFqdns: "{{ targetFqdns }}"
                  fqdnTags: "{{ fqdnTags }}"
                  sourceIpGroups: "{{ sourceIpGroups }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        natRuleCollections:
          - id: "{{ id }}"
            properties:
              priority: {{ priority }}
              action:
                type: "{{ type }}"
              rules:
                - name: "{{ name }}"
                  description: "{{ description }}"
                  sourceAddresses: "{{ sourceAddresses }}"
                  destinationAddresses: "{{ destinationAddresses }}"
                  destinationPorts: "{{ destinationPorts }}"
                  protocols: "{{ protocols }}"
                  translatedAddress: "{{ translatedAddress }}"
                  translatedPort: "{{ translatedPort }}"
                  translatedFqdn: "{{ translatedFqdn }}"
                  sourceIpGroups: "{{ sourceIpGroups }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        networkRuleCollections:
          - id: "{{ id }}"
            properties:
              priority: {{ priority }}
              action:
                type: "{{ type }}"
              rules:
                - name: "{{ name }}"
                  description: "{{ description }}"
                  protocols: "{{ protocols }}"
                  sourceAddresses: "{{ sourceAddresses }}"
                  destinationAddresses: "{{ destinationAddresses }}"
                  destinationPorts: "{{ destinationPorts }}"
                  destinationFqdns: "{{ destinationFqdns }}"
                  sourceIpGroups: "{{ sourceIpGroups }}"
                  destinationIpGroups: "{{ destinationIpGroups }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        ipConfigurations:
          - id: "{{ id }}"
            properties:
              privateIPAddress: "{{ privateIPAddress }}"
              subnet:
                id: "{{ id }}"
              publicIPAddress:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        managementIpConfiguration:
          id: "{{ id }}"
          properties:
            privateIPAddress: "{{ privateIPAddress }}"
            subnet:
              id: "{{ id }}"
            publicIPAddress:
              id: "{{ id }}"
            provisioningState: "{{ provisioningState }}"
          name: "{{ name }}"
          etag: "{{ etag }}"
          type: "{{ type }}"
        provisioningState: "{{ provisioningState }}"
        threatIntelMode: "{{ threatIntelMode }}"
        virtualHub:
          id: "{{ id }}"
        firewallPolicy:
          id: "{{ id }}"
        hubIPAddresses:
          publicIPs:
            addresses:
              - address: "{{ address }}"
            count: {{ count }}
          privateIPAddress: "{{ privateIPAddress }}"
        ipGroups:
          - id: "{{ id }}"
            changeNumber: "{{ changeNumber }}"
        sku:
          name: "{{ name }}"
          tier: "{{ tier }}"
        additionalProperties: "{{ additionalProperties }}"
        autoscaleConfiguration:
          minCapacity: {{ minCapacity }}
          maxCapacity: {{ maxCapacity }}
        afcConfiguration:
          serviceEndpoint: "{{ serviceEndpoint }}"
    - name: extendedLocation
      description: |
        The extended location of type local virtual network gateway.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting where the resource needs to come from.
    - name: createAfcControlPlane
      value: {{ createAfcControlPlane }}
      description: When set to true, creates an AFC control plane for the Azure Firewall. Default value is None.
      description: When set to true, creates an AFC control plane for the Azure Firewall. Default value is None.
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

Updates tags of an Azure Firewall resource.

```sql
UPDATE azure.network.azure_firewalls
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_firewall_name = '{{ azure_firewall_name }}' --required
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

Creates or updates the specified Azure Firewall.

```sql
REPLACE azure.network.azure_firewalls
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_firewall_name = '{{ azure_firewall_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND createAfcControlPlane = {{ createAfcControlPlane}}
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

Deletes the specified Azure Firewall.

```sql
DELETE FROM azure.network.azure_firewalls
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND azure_firewall_name = '{{ azure_firewall_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_learned_prefixes"
    values={[
        { label: 'list_learned_prefixes', value: 'list_learned_prefixes' },
        { label: 'packet_capture', value: 'packet_capture' },
        { label: 'packet_capture_operation', value: 'packet_capture_operation' }
    ]}
>
<TabItem value="list_learned_prefixes">

Retrieves a list of all IP prefixes that azure firewall has learned to not SNAT.

```sql
EXEC azure.network.azure_firewalls.list_learned_prefixes 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_firewall_name='{{ azure_firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="packet_capture">

Runs a packet capture on AzureFirewall.

```sql
EXEC azure.network.azure_firewalls.packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_firewall_name='{{ azure_firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"durationInSeconds": {{ durationInSeconds }}, 
"numberOfPacketsToCapture": {{ numberOfPacketsToCapture }}, 
"sasUrl": "{{ sasUrl }}", 
"fileName": "{{ fileName }}", 
"protocol": "{{ protocol }}", 
"flags": "{{ flags }}", 
"filters": "{{ filters }}", 
"operation": "{{ operation }}"
}'
;
```
</TabItem>
<TabItem value="packet_capture_operation">

Runs a packet capture operation on AzureFirewall.

```sql
EXEC azure.network.azure_firewalls.packet_capture_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_firewall_name='{{ azure_firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"durationInSeconds": {{ durationInSeconds }}, 
"numberOfPacketsToCapture": {{ numberOfPacketsToCapture }}, 
"sasUrl": "{{ sasUrl }}", 
"fileName": "{{ fileName }}", 
"protocol": "{{ protocol }}", 
"flags": "{{ flags }}", 
"filters": "{{ filters }}", 
"operation": "{{ operation }}"
}'
;
```
</TabItem>
</Tabs>
