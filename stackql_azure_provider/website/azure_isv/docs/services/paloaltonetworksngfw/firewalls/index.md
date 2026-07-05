--- 
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - paloaltonetworksngfw
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

Creates, updates, deletes, gets or lists a <code>firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewalls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworksngfw.firewalls" /></td></tr>
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
    <td><CopyableCode code="associatedRulestack" /></td>
    <td><code>object</code></td>
    <td>Associated Rulestack.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>DNS settings for Firewall. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="frontEndSettings" /></td>
    <td><code>array</code></td>
    <td>Frontend settings for Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isPanoramaManaged" /></td>
    <td><code>string</code></td>
    <td>Panorama Managed: Default is False. Default will be CloudSec managed. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="isStrataCloudManaged" /></td>
    <td><code>string</code></td>
    <td>Strata Cloud Managed: Default is False. Default will be CloudSec managed. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceDetails" /></td>
    <td><code>object</code></td>
    <td>Marketplace details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network settings. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="panEtag" /></td>
    <td><code>string</code></td>
    <td>panEtag info.</td>
</tr>
<tr>
    <td><CopyableCode code="panoramaConfig" /></td>
    <td><code>object</code></td>
    <td>Panorama Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Billing plan information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="strataCloudManagerConfig" /></td>
    <td><code>object</code></td>
    <td>Strata Cloud Manager Configuration, only applicable if Strata Cloud Manager is selected.</td>
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
    <td><CopyableCode code="associatedRulestack" /></td>
    <td><code>object</code></td>
    <td>Associated Rulestack.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>DNS settings for Firewall. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="frontEndSettings" /></td>
    <td><code>array</code></td>
    <td>Frontend settings for Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isPanoramaManaged" /></td>
    <td><code>string</code></td>
    <td>Panorama Managed: Default is False. Default will be CloudSec managed. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="isStrataCloudManaged" /></td>
    <td><code>string</code></td>
    <td>Strata Cloud Managed: Default is False. Default will be CloudSec managed. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceDetails" /></td>
    <td><code>object</code></td>
    <td>Marketplace details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network settings. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="panEtag" /></td>
    <td><code>string</code></td>
    <td>panEtag info.</td>
</tr>
<tr>
    <td><CopyableCode code="panoramaConfig" /></td>
    <td><code>object</code></td>
    <td>Panorama Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Billing plan information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="strataCloudManagerConfig" /></td>
    <td><code>object</code></td>
    <td>Strata Cloud Manager Configuration, only applicable if Strata Cloud Manager is selected.</td>
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
    <td><CopyableCode code="associatedRulestack" /></td>
    <td><code>object</code></td>
    <td>Associated Rulestack.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>DNS settings for Firewall. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="frontEndSettings" /></td>
    <td><code>array</code></td>
    <td>Frontend settings for Firewall.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isPanoramaManaged" /></td>
    <td><code>string</code></td>
    <td>Panorama Managed: Default is False. Default will be CloudSec managed. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="isStrataCloudManaged" /></td>
    <td><code>string</code></td>
    <td>Strata Cloud Managed: Default is False. Default will be CloudSec managed. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceDetails" /></td>
    <td><code>object</code></td>
    <td>Marketplace details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network settings. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="panEtag" /></td>
    <td><code>string</code></td>
    <td>panEtag info.</td>
</tr>
<tr>
    <td><CopyableCode code="panoramaConfig" /></td>
    <td><code>object</code></td>
    <td>Panorama Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Billing plan information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="strataCloudManagerConfig" /></td>
    <td><code>object</code></td>
    <td>Strata Cloud Manager Configuration, only applicable if Strata Cloud Manager is selected.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a FirewallResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FirewallResource resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FirewallResource resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a FirewallResource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a FirewallResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a FirewallResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a FirewallResource.</td>
</tr>
<tr>
    <td><a href="#get_global_rulestack"><CopyableCode code="get_global_rulestack" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Global Rulestack associated with the Firewall.</td>
</tr>
<tr>
    <td><a href="#get_log_profile"><CopyableCode code="get_log_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Log Profile for Firewall.</td>
</tr>
<tr>
    <td><a href="#get_support_info"><CopyableCode code="get_support_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-email"><code>email</code></a></td>
    <td>support info for firewall.</td>
</tr>
<tr>
    <td><a href="#save_log_profile"><CopyableCode code="save_log_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_name"><code>firewall_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Log Profile for Firewall.</td>
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
<tr id="parameter-firewall_name">
    <td><CopyableCode code="firewall_name" /></td>
    <td><code>string</code></td>
    <td>Firewall resource name. Required.</td>
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
<tr id="parameter-email">
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>email address on behalf of which this API called. Default value is None.</td>
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

Get a FirewallResource.

```sql
SELECT
id,
name,
associatedRulestack,
dnsSettings,
frontEndSettings,
identity,
isPanoramaManaged,
isStrataCloudManaged,
location,
marketplaceDetails,
networkProfile,
panEtag,
panoramaConfig,
planData,
provisioningState,
strataCloudManagerConfig,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.firewalls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND firewall_name = '{{ firewall_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List FirewallResource resources by resource group.

```sql
SELECT
id,
name,
associatedRulestack,
dnsSettings,
frontEndSettings,
identity,
isPanoramaManaged,
isStrataCloudManaged,
location,
marketplaceDetails,
networkProfile,
panEtag,
panoramaConfig,
planData,
provisioningState,
strataCloudManagerConfig,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.firewalls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List FirewallResource resources by subscription ID.

```sql
SELECT
id,
name,
associatedRulestack,
dnsSettings,
frontEndSettings,
identity,
isPanoramaManaged,
isStrataCloudManaged,
location,
marketplaceDetails,
networkProfile,
panEtag,
panoramaConfig,
planData,
provisioningState,
strataCloudManagerConfig,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.firewalls
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

Create a FirewallResource.

```sql
INSERT INTO azure_isv.paloaltonetworksngfw.firewalls (
tags,
location,
identity,
properties,
resource_group_name,
firewall_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ firewall_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: firewalls
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the firewalls resource.
    - name: firewall_name
      value: "{{ firewall_name }}"
      description: Required parameter for the firewalls resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the firewalls resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        panEtag: "{{ panEtag }}"
        networkProfile:
          vnetConfiguration:
            vnet:
              resourceId: "{{ resourceId }}"
              addressSpace: "{{ addressSpace }}"
            trustSubnet:
              resourceId: "{{ resourceId }}"
              addressSpace: "{{ addressSpace }}"
            unTrustSubnet:
              resourceId: "{{ resourceId }}"
              addressSpace: "{{ addressSpace }}"
            ipOfTrustSubnetForUdr:
              resourceId: "{{ resourceId }}"
              address: "{{ address }}"
          vwanConfiguration:
            networkVirtualApplianceId: "{{ networkVirtualApplianceId }}"
            vHub:
              resourceId: "{{ resourceId }}"
              addressSpace: "{{ addressSpace }}"
            trustSubnet:
              resourceId: "{{ resourceId }}"
              addressSpace: "{{ addressSpace }}"
            unTrustSubnet:
              resourceId: "{{ resourceId }}"
              addressSpace: "{{ addressSpace }}"
            ipOfTrustSubnetForUdr:
              resourceId: "{{ resourceId }}"
              address: "{{ address }}"
          networkType: "{{ networkType }}"
          publicIps:
            - resourceId: "{{ resourceId }}"
              address: "{{ address }}"
          enableEgressNat: "{{ enableEgressNat }}"
          egressNatIp:
            - resourceId: "{{ resourceId }}"
              address: "{{ address }}"
          trustedRanges:
            - "{{ trustedRanges }}"
          privateSourceNatRulesDestination:
            - "{{ privateSourceNatRulesDestination }}"
        isPanoramaManaged: "{{ isPanoramaManaged }}"
        isStrataCloudManaged: "{{ isStrataCloudManaged }}"
        panoramaConfig:
          configString: "{{ configString }}"
          vmAuthKey: "{{ vmAuthKey }}"
          panoramaServer: "{{ panoramaServer }}"
          panoramaServer2: "{{ panoramaServer2 }}"
          dgName: "{{ dgName }}"
          tplName: "{{ tplName }}"
          cgName: "{{ cgName }}"
          hostName: "{{ hostName }}"
        strataCloudManagerConfig:
          cloudManagerName: "{{ cloudManagerName }}"
        associatedRulestack:
          resourceId: "{{ resourceId }}"
          rulestackId: "{{ rulestackId }}"
          location: "{{ location }}"
        dnsSettings:
          enableDnsProxy: "{{ enableDnsProxy }}"
          enabledDnsType: "{{ enabledDnsType }}"
          dnsServers:
            - resourceId: "{{ resourceId }}"
              address: "{{ address }}"
        frontEndSettings:
          - name: "{{ name }}"
            protocol: "{{ protocol }}"
            frontendConfiguration:
              port: "{{ port }}"
              address:
                resourceId: "{{ resourceId }}"
                address: "{{ address }}"
            backendConfiguration:
              port: "{{ port }}"
              address:
                resourceId: "{{ resourceId }}"
                address: "{{ address }}"
        planData:
          usageType: "{{ usageType }}"
          billingCycle: "{{ billingCycle }}"
          planId: "{{ planId }}"
          effectiveDate: "{{ effectiveDate }}"
        marketplaceDetails:
          marketplaceSubscriptionId: "{{ marketplaceSubscriptionId }}"
          offerId: "{{ offerId }}"
          publisherId: "{{ publisherId }}"
          marketplaceSubscriptionStatus: "{{ marketplaceSubscriptionStatus }}"
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

Update a FirewallResource.

```sql
UPDATE azure_isv.paloaltonetworksngfw.firewalls
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND firewall_name = '{{ firewall_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
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

Create a FirewallResource.

```sql
REPLACE azure_isv.paloaltonetworksngfw.firewalls
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND firewall_name = '{{ firewall_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
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

Delete a FirewallResource.

```sql
DELETE FROM azure_isv.paloaltonetworksngfw.firewalls
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND firewall_name = '{{ firewall_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_global_rulestack"
    values={[
        { label: 'get_global_rulestack', value: 'get_global_rulestack' },
        { label: 'get_log_profile', value: 'get_log_profile' },
        { label: 'get_support_info', value: 'get_support_info' },
        { label: 'save_log_profile', value: 'save_log_profile' }
    ]}
>
<TabItem value="get_global_rulestack">

Get Global Rulestack associated with the Firewall.

```sql
EXEC azure_isv.paloaltonetworksngfw.firewalls.get_global_rulestack 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_name='{{ firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_log_profile">

Log Profile for Firewall.

```sql
EXEC azure_isv.paloaltonetworksngfw.firewalls.get_log_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_name='{{ firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_support_info">

support info for firewall.

```sql
EXEC azure_isv.paloaltonetworksngfw.firewalls.get_support_info 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_name='{{ firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@email='{{ email }}'
;
```
</TabItem>
<TabItem value="save_log_profile">

Log Profile for Firewall.

```sql
EXEC azure_isv.paloaltonetworksngfw.firewalls.save_log_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_name='{{ firewall_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"logType": "{{ logType }}", 
"logOption": "{{ logOption }}", 
"applicationInsights": "{{ applicationInsights }}", 
"commonDestination": "{{ commonDestination }}", 
"trafficLogDestination": "{{ trafficLogDestination }}", 
"threatLogDestination": "{{ threatLogDestination }}", 
"decryptLogDestination": "{{ decryptLogDestination }}"
}'
;
```
</TabItem>
</Tabs>
