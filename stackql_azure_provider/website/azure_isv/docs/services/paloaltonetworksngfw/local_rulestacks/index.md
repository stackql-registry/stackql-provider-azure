--- 
title: local_rulestacks
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks
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

Creates, updates, deletes, gets or lists a <code>local_rulestacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="local_rulestacks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworksngfw.local_rulestacks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_advanced_security_objects"
    values={[
        { label: 'list_advanced_security_objects', value: 'list_advanced_security_objects' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_advanced_security_objects">

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
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>next link.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>object</code></td>
    <td>response value. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="associatedSubscriptions" /></td>
    <td><code>array</code></td>
    <td>subscription scope of global rulestack.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultMode" /></td>
    <td><code>string</code></td>
    <td>Mode for default rules creation. Known values are: "IPS", "FIREWALL", and "NONE".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>rulestack description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minAppIdVersion" /></td>
    <td><code>string</code></td>
    <td>minimum version.</td>
</tr>
<tr>
    <td><CopyableCode code="panEtag" /></td>
    <td><code>string</code></td>
    <td>PanEtag info.</td>
</tr>
<tr>
    <td><CopyableCode code="panLocation" /></td>
    <td><code>string</code></td>
    <td>Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Rulestack Type. Known values are: "LOCAL", "GLOBAL", and "GLOBAL".</td>
</tr>
<tr>
    <td><CopyableCode code="securityServices" /></td>
    <td><code>object</code></td>
    <td>Security Profile.</td>
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
    <td><CopyableCode code="associatedSubscriptions" /></td>
    <td><code>array</code></td>
    <td>subscription scope of global rulestack.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultMode" /></td>
    <td><code>string</code></td>
    <td>Mode for default rules creation. Known values are: "IPS", "FIREWALL", and "NONE".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>rulestack description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minAppIdVersion" /></td>
    <td><code>string</code></td>
    <td>minimum version.</td>
</tr>
<tr>
    <td><CopyableCode code="panEtag" /></td>
    <td><code>string</code></td>
    <td>PanEtag info.</td>
</tr>
<tr>
    <td><CopyableCode code="panLocation" /></td>
    <td><code>string</code></td>
    <td>Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Rulestack Type. Known values are: "LOCAL", "GLOBAL", and "GLOBAL".</td>
</tr>
<tr>
    <td><CopyableCode code="securityServices" /></td>
    <td><code>object</code></td>
    <td>Security Profile.</td>
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
    <td><CopyableCode code="associatedSubscriptions" /></td>
    <td><code>array</code></td>
    <td>subscription scope of global rulestack.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultMode" /></td>
    <td><code>string</code></td>
    <td>Mode for default rules creation. Known values are: "IPS", "FIREWALL", and "NONE".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>rulestack description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minAppIdVersion" /></td>
    <td><code>string</code></td>
    <td>minimum version.</td>
</tr>
<tr>
    <td><CopyableCode code="panEtag" /></td>
    <td><code>string</code></td>
    <td>PanEtag info.</td>
</tr>
<tr>
    <td><CopyableCode code="panLocation" /></td>
    <td><code>string</code></td>
    <td>Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Rulestack Type. Known values are: "LOCAL", "GLOBAL", and "GLOBAL".</td>
</tr>
<tr>
    <td><CopyableCode code="securityServices" /></td>
    <td><code>object</code></td>
    <td>Security Profile.</td>
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
    <td><a href="#list_advanced_security_objects"><CopyableCode code="list_advanced_security_objects" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>Get the list of advanced security objects.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a LocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List LocalRulestackResource resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List LocalRulestackResource resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a LocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a LocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a LocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a LocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#list_app_ids"><CopyableCode code="list_app_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-appIdVersion"><code>appIdVersion</code></a>, <a href="#parameter-appPrefix"><code>appPrefix</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>List of AppIds for LocalRulestack ApiVersion.</td>
</tr>
<tr>
    <td><a href="#list_countries"><CopyableCode code="list_countries" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>List of countries for Rulestack.</td>
</tr>
<tr>
    <td><a href="#list_firewalls"><CopyableCode code="list_firewalls" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List of Firewalls associated with Rulestack.</td>
</tr>
<tr>
    <td><a href="#list_predefined_url_categories"><CopyableCode code="list_predefined_url_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>List predefined URL categories for rulestack.</td>
</tr>
<tr>
    <td><a href="#list_security_services"><CopyableCode code="list_security_services" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>List the security services for rulestack.</td>
</tr>
<tr>
    <td><a href="#get_change_log"><CopyableCode code="get_change_log" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get changelog.</td>
</tr>
<tr>
    <td><a href="#get_support_info"><CopyableCode code="get_support_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-email"><code>email</code></a></td>
    <td>support info for rulestack.</td>
</tr>
<tr>
    <td><a href="#commit"><CopyableCode code="commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Commit rulestack configuration.</td>
</tr>
<tr>
    <td><a href="#revert"><CopyableCode code="revert" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revert rulestack configuration.</td>
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
<tr id="parameter-local_rulestack_name">
    <td><CopyableCode code="local_rulestack_name" /></td>
    <td><code>string</code></td>
    <td>LocalRulestack resource name. Required.</td>
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
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Known values are: "antiSpyware", "antiVirus", "ipsVulnerability", "urlFiltering", "fileBlocking", and "dnsSubscription". Required.</td>
</tr>
<tr id="parameter-appIdVersion">
    <td><CopyableCode code="appIdVersion" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
<tr id="parameter-appPrefix">
    <td><CopyableCode code="appPrefix" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
<tr id="parameter-email">
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>email address on behalf of which this API called. Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_advanced_security_objects"
    values={[
        { label: 'list_advanced_security_objects', value: 'list_advanced_security_objects' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_advanced_security_objects">

Get the list of advanced security objects.

```sql
SELECT
nextLink,
value
FROM azure_isv.paloaltonetworksngfw.local_rulestacks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND local_rulestack_name = '{{ local_rulestack_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND type = '{{ type }}' -- required
AND skip = '{{ skip }}'
AND top = '{{ top }}'
;
```
</TabItem>
<TabItem value="get">

Get a LocalRulestackResource.

```sql
SELECT
id,
name,
associatedSubscriptions,
defaultMode,
description,
identity,
location,
minAppIdVersion,
panEtag,
panLocation,
provisioningState,
scope,
securityServices,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.local_rulestacks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND local_rulestack_name = '{{ local_rulestack_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List LocalRulestackResource resources by resource group.

```sql
SELECT
id,
name,
associatedSubscriptions,
defaultMode,
description,
identity,
location,
minAppIdVersion,
panEtag,
panLocation,
provisioningState,
scope,
securityServices,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.local_rulestacks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List LocalRulestackResource resources by subscription ID.

```sql
SELECT
id,
name,
associatedSubscriptions,
defaultMode,
description,
identity,
location,
minAppIdVersion,
panEtag,
panLocation,
provisioningState,
scope,
securityServices,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.local_rulestacks
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

Create a LocalRulestackResource.

```sql
INSERT INTO azure_isv.paloaltonetworksngfw.local_rulestacks (
tags,
location,
identity,
properties,
resource_group_name,
local_rulestack_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ local_rulestack_name }}',
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
- name: local_rulestacks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the local_rulestacks resource.
    - name: local_rulestack_name
      value: "{{ local_rulestack_name }}"
      description: Required parameter for the local_rulestacks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the local_rulestacks resource.
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
        panLocation: "{{ panLocation }}"
        scope: "{{ scope }}"
        associatedSubscriptions:
          - "{{ associatedSubscriptions }}"
        description: "{{ description }}"
        defaultMode: "{{ defaultMode }}"
        minAppIdVersion: "{{ minAppIdVersion }}"
        securityServices:
          vulnerabilityProfile: "{{ vulnerabilityProfile }}"
          antiSpywareProfile: "{{ antiSpywareProfile }}"
          antiVirusProfile: "{{ antiVirusProfile }}"
          urlFilteringProfile: "{{ urlFilteringProfile }}"
          fileBlockingProfile: "{{ fileBlockingProfile }}"
          dnsSubscription: "{{ dnsSubscription }}"
          outboundUnTrustCertificate: "{{ outboundUnTrustCertificate }}"
          outboundTrustCertificate: "{{ outboundTrustCertificate }}"
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

Update a LocalRulestackResource.

```sql
UPDATE azure_isv.paloaltonetworksngfw.local_rulestacks
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND local_rulestack_name = '{{ local_rulestack_name }}' --required
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

Create a LocalRulestackResource.

```sql
REPLACE azure_isv.paloaltonetworksngfw.local_rulestacks
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND local_rulestack_name = '{{ local_rulestack_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Delete a LocalRulestackResource.

```sql
DELETE FROM azure_isv.paloaltonetworksngfw.local_rulestacks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND local_rulestack_name = '{{ local_rulestack_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_app_ids"
    values={[
        { label: 'list_app_ids', value: 'list_app_ids' },
        { label: 'list_countries', value: 'list_countries' },
        { label: 'list_firewalls', value: 'list_firewalls' },
        { label: 'list_predefined_url_categories', value: 'list_predefined_url_categories' },
        { label: 'list_security_services', value: 'list_security_services' },
        { label: 'get_change_log', value: 'get_change_log' },
        { label: 'get_support_info', value: 'get_support_info' },
        { label: 'commit', value: 'commit' },
        { label: 'revert', value: 'revert' }
    ]}
>
<TabItem value="list_app_ids">

List of AppIds for LocalRulestack ApiVersion.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.list_app_ids 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@appIdVersion='{{ appIdVersion }}', 
@appPrefix='{{ appPrefix }}', 
@skip='{{ skip }}', 
@top='{{ top }}'
;
```
</TabItem>
<TabItem value="list_countries">

List of countries for Rulestack.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.list_countries 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@skip='{{ skip }}', 
@top='{{ top }}'
;
```
</TabItem>
<TabItem value="list_firewalls">

List of Firewalls associated with Rulestack.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.list_firewalls 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_predefined_url_categories">

List predefined URL categories for rulestack.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.list_predefined_url_categories 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@skip='{{ skip }}', 
@top='{{ top }}'
;
```
</TabItem>
<TabItem value="list_security_services">

List the security services for rulestack.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.list_security_services 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@type='{{ type }}' --required, 
@skip='{{ skip }}', 
@top='{{ top }}'
;
```
</TabItem>
<TabItem value="get_change_log">

Get changelog.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.get_change_log 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_support_info">

support info for rulestack.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.get_support_info 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@email='{{ email }}'
;
```
</TabItem>
<TabItem value="commit">

Commit rulestack configuration.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.commit 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="revert">

Revert rulestack configuration.

```sql
EXEC azure_isv.paloaltonetworksngfw.local_rulestacks.revert 
@resource_group_name='{{ resource_group_name }}' --required, 
@local_rulestack_name='{{ local_rulestack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
