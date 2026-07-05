--- 
title: notification_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_hubs
  - notificationhubs
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

Creates, updates, deletes, gets or lists a <code>notification_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="notification_hubs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notificationhubs.notification_hubs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_authorization_rule"
    values={[
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_authorization_rule">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="claimType" /></td>
    <td><code>string</code></td>
    <td>Gets a string that describes the claim type.</td>
</tr>
<tr>
    <td><CopyableCode code="claimValue" /></td>
    <td><code>string</code></td>
    <td>Gets a string that describes the claim value.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the created time for this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="keyName" /></td>
    <td><code>string</code></td>
    <td>Gets a string that describes the authorization rule.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Deprecated - only for compatibility.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the last modified time for this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryKey" /></td>
    <td><code>string</code></td>
    <td>Gets a base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>Gets the revision number for the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="rights" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the rights associated with the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryKey" /></td>
    <td><code>string</code></td>
    <td>Gets a base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deprecated - only for compatibility.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="admCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub AdmCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="apnsCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub ApnsCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationRules" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the AuthorizationRules of the created NotificationHub.</td>
</tr>
<tr>
    <td><CopyableCode code="baiduCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub BaiduCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="browserCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub BrowserCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="dailyMaxActiveDevices" /></td>
    <td><code>integer</code></td>
    <td>:vartype daily_max_active_devices: int</td>
</tr>
<tr>
    <td><CopyableCode code="fcmV1Credential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub FcmV1Credential.</td>
</tr>
<tr>
    <td><CopyableCode code="gcmCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub GcmCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mpnsCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub MpnsCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationTtl" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the RegistrationTtl of the created NotificationHub.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku description for a namespace.</td>
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
<tr>
    <td><CopyableCode code="wnsCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub WnsCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="xiaomiCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub XiaomiCredential.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="admCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub AdmCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="apnsCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub ApnsCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationRules" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the AuthorizationRules of the created NotificationHub.</td>
</tr>
<tr>
    <td><CopyableCode code="baiduCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub BaiduCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="browserCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub BrowserCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="dailyMaxActiveDevices" /></td>
    <td><code>integer</code></td>
    <td>:vartype daily_max_active_devices: int</td>
</tr>
<tr>
    <td><CopyableCode code="fcmV1Credential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub FcmV1Credential.</td>
</tr>
<tr>
    <td><CopyableCode code="gcmCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub GcmCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mpnsCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub MpnsCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationTtl" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the RegistrationTtl of the created NotificationHub.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku description for a namespace.</td>
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
<tr>
    <td><CopyableCode code="wnsCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub WnsCredential.</td>
</tr>
<tr>
    <td><CopyableCode code="xiaomiCredential" /></td>
    <td><code>object</code></td>
    <td>Description of a NotificationHub XiaomiCredential.</td>
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
    <td><a href="#get_authorization_rule"><CopyableCode code="get_authorization_rule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an authorization rule for a NotificationHub by name. Gets an authorization rule for a NotificationHub by name.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the notification hub. Gets the notification hub.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the notification hubs associated with a namespace. Lists the notification hubs associated with a namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates/Update a NotificationHub in a namespace. Creates/Update a NotificationHub in a namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update_authorization_rule"><CopyableCode code="create_or_update_authorization_rule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates/Updates an authorization rule for a NotificationHub. Creates/Updates an authorization rule for a NotificationHub.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a NotificationHub in a namespace. Patch a NotificationHub in a namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates/Update a NotificationHub in a namespace. Creates/Update a NotificationHub in a namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update_authorization_rule"><CopyableCode code="create_or_update_authorization_rule" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates/Updates an authorization rule for a NotificationHub. Creates/Updates an authorization rule for a NotificationHub.</td>
</tr>
<tr>
    <td><a href="#delete_authorization_rule"><CopyableCode code="delete_authorization_rule" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a notificationHub authorization rule. Deletes a notificationHub authorization rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a notification hub associated with a namespace. Deletes a notification hub associated with a namespace.</td>
</tr>
<tr>
    <td><a href="#list_authorization_rules"><CopyableCode code="list_authorization_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the authorization rules for a NotificationHub. Gets the authorization rules for a NotificationHub.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Primary and Secondary ConnectionStrings to the NotificationHub. Gets the Primary and Secondary ConnectionStrings to the NotificationHub.</td>
</tr>
<tr>
    <td><a href="#get_pns_credentials"><CopyableCode code="get_pns_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the PNS Credentials associated with a notification hub. Lists the PNS Credentials associated with a notification hub.</td>
</tr>
<tr>
    <td><a href="#check_notification_hub_availability"><CopyableCode code="check_notification_hub_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Checks the availability of the given notificationHub in a namespace. Checks the availability of the given notificationHub in a namespace.</td>
</tr>
<tr>
    <td><a href="#debug_send"><CopyableCode code="debug_send" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Test send a push notification. Test send a push notification.</td>
</tr>
<tr>
    <td><a href="#regenerate_keys"><CopyableCode code="regenerate_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-notification_hub_name"><code>notification_hub_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policyKey"><code>policyKey</code></a></td>
    <td></td>
    <td>Regenerates the Primary/Secondary Keys to the NotificationHub Authorization Rule. Regenerates the Primary/Secondary Keys to the NotificationHub Authorization Rule.</td>
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
<tr id="parameter-authorization_rule_name">
    <td><CopyableCode code="authorization_rule_name" /></td>
    <td><code>string</code></td>
    <td>Authorization Rule Name. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Namespace name. Required.</td>
</tr>
<tr id="parameter-notification_hub_name">
    <td><CopyableCode code="notification_hub_name" /></td>
    <td><code>string</code></td>
    <td>Notification Hub name. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Continuation token. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Page size. Default value is 100.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_authorization_rule"
    values={[
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_authorization_rule">

Gets an authorization rule for a NotificationHub by name. Gets an authorization rule for a NotificationHub by name.

```sql
SELECT
id,
name,
claimType,
claimValue,
createdTime,
keyName,
location,
modifiedTime,
primaryKey,
revision,
rights,
secondaryKey,
systemData,
tags,
type
FROM azure.notificationhubs.notification_hubs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND notification_hub_name = '{{ notification_hub_name }}' -- required
AND authorization_rule_name = '{{ authorization_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the notification hub. Gets the notification hub.

```sql
SELECT
id,
name,
admCredential,
apnsCredential,
authorizationRules,
baiduCredential,
browserCredential,
dailyMaxActiveDevices,
fcmV1Credential,
gcmCredential,
location,
mpnsCredential,
registrationTtl,
sku,
systemData,
tags,
type,
wnsCredential,
xiaomiCredential
FROM azure.notificationhubs.notification_hubs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND notification_hub_name = '{{ notification_hub_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the notification hubs associated with a namespace. Lists the notification hubs associated with a namespace.

```sql
SELECT
id,
name,
admCredential,
apnsCredential,
authorizationRules,
baiduCredential,
browserCredential,
dailyMaxActiveDevices,
fcmV1Credential,
gcmCredential,
location,
mpnsCredential,
registrationTtl,
sku,
systemData,
tags,
type,
wnsCredential,
xiaomiCredential
FROM azure.notificationhubs.notification_hubs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_authorization_rule', value: 'create_or_update_authorization_rule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates/Update a NotificationHub in a namespace. Creates/Update a NotificationHub in a namespace.

```sql
INSERT INTO azure.notificationhubs.notification_hubs (
tags,
location,
sku,
properties,
resource_group_name,
namespace_name,
notification_hub_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ sku }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ notification_hub_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_authorization_rule">

Creates/Updates an authorization rule for a NotificationHub. Creates/Updates an authorization rule for a NotificationHub.

```sql
INSERT INTO azure.notificationhubs.notification_hubs (
location,
tags,
properties,
resource_group_name,
namespace_name,
notification_hub_name,
authorization_rule_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ notification_hub_name }}',
'{{ authorization_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: notification_hubs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the notification_hubs resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the notification_hubs resource.
    - name: notification_hub_name
      value: "{{ notification_hub_name }}"
      description: Required parameter for the notification_hubs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the notification_hubs resource.
    - name: authorization_rule_name
      value: "{{ authorization_rule_name }}"
      description: Required parameter for the notification_hubs resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Deprecated - only for compatibility.
    - name: location
      value: "{{ location }}"
      description: |
        Deprecated - only for compatibility.
    - name: sku
      description: |
        The Sku description for a namespace.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: properties
      value:
        rights:
          - "{{ rights }}"
        primaryKey: "{{ primaryKey }}"
        secondaryKey: "{{ secondaryKey }}"
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

Patch a NotificationHub in a namespace. Patch a NotificationHub in a namespace.

```sql
UPDATE azure.notificationhubs.notification_hubs
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND notification_hub_name = '{{ notification_hub_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
sku,
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
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_authorization_rule', value: 'create_or_update_authorization_rule' }
    ]}
>
<TabItem value="create_or_update">

Creates/Update a NotificationHub in a namespace. Creates/Update a NotificationHub in a namespace.

```sql
REPLACE azure.notificationhubs.notification_hubs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND notification_hub_name = '{{ notification_hub_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_authorization_rule">

Creates/Updates an authorization rule for a NotificationHub. Creates/Updates an authorization rule for a NotificationHub.

```sql
REPLACE azure.notificationhubs.notification_hubs
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND notification_hub_name = '{{ notification_hub_name }}' --required
AND authorization_rule_name = '{{ authorization_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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
    defaultValue="delete_authorization_rule"
    values={[
        { label: 'delete_authorization_rule', value: 'delete_authorization_rule' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_authorization_rule">

Deletes a notificationHub authorization rule. Deletes a notificationHub authorization rule.

```sql
DELETE FROM azure.notificationhubs.notification_hubs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND notification_hub_name = '{{ notification_hub_name }}' --required
AND authorization_rule_name = '{{ authorization_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a notification hub associated with a namespace. Deletes a notification hub associated with a namespace.

```sql
DELETE FROM azure.notificationhubs.notification_hubs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND notification_hub_name = '{{ notification_hub_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_authorization_rules"
    values={[
        { label: 'list_authorization_rules', value: 'list_authorization_rules' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get_pns_credentials', value: 'get_pns_credentials' },
        { label: 'check_notification_hub_availability', value: 'check_notification_hub_availability' },
        { label: 'debug_send', value: 'debug_send' },
        { label: 'regenerate_keys', value: 'regenerate_keys' }
    ]}
>
<TabItem value="list_authorization_rules">

Gets the authorization rules for a NotificationHub. Gets the authorization rules for a NotificationHub.

```sql
EXEC azure.notificationhubs.notification_hubs.list_authorization_rules 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@notification_hub_name='{{ notification_hub_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_keys">

Gets the Primary and Secondary ConnectionStrings to the NotificationHub. Gets the Primary and Secondary ConnectionStrings to the NotificationHub.

```sql
EXEC azure.notificationhubs.notification_hubs.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@notification_hub_name='{{ notification_hub_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_pns_credentials">

Lists the PNS Credentials associated with a notification hub. Lists the PNS Credentials associated with a notification hub.

```sql
EXEC azure.notificationhubs.notification_hubs.get_pns_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@notification_hub_name='{{ notification_hub_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_notification_hub_availability">

Checks the availability of the given notificationHub in a namespace. Checks the availability of the given notificationHub in a namespace.

```sql
EXEC azure.notificationhubs.notification_hubs.check_notification_hub_availability 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"isAvailiable": {{ isAvailiable }}, 
"sku": "{{ sku }}"
}'
;
```
</TabItem>
<TabItem value="debug_send">

Test send a push notification. Test send a push notification.

```sql
EXEC azure.notificationhubs.notification_hubs.debug_send 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@notification_hub_name='{{ notification_hub_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_keys">

Regenerates the Primary/Secondary Keys to the NotificationHub Authorization Rule. Regenerates the Primary/Secondary Keys to the NotificationHub Authorization Rule.

```sql
EXEC azure.notificationhubs.notification_hubs.regenerate_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@notification_hub_name='{{ notification_hub_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"policyKey": "{{ policyKey }}"
}'
;
```
</TabItem>
</Tabs>
