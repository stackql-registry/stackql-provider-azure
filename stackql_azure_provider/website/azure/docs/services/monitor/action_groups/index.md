--- 
title: action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups
  - monitor
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

Creates, updates, deletes, gets or lists an <code>action_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="action_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.action_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_test_notifications_at_action_group_resource_level"
    values={[
        { label: 'get_test_notifications_at_action_group_resource_level', value: 'get_test_notifications_at_action_group_resource_level' },
        { label: 'get_nsp', value: 'get_nsp' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
    ]}
>
<TabItem value="get_test_notifications_at_action_group_resource_level">

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
    <td><CopyableCode code="actionDetails" /></td>
    <td><code>array</code></td>
    <td>The list of action detail.</td>
</tr>
<tr>
    <td><CopyableCode code="completedTime" /></td>
    <td><code>string</code></td>
    <td>The completed time.</td>
</tr>
<tr>
    <td><CopyableCode code="context" /></td>
    <td><code>object</code></td>
    <td>The context info.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string</code></td>
    <td>The created time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The overall state. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_nsp">

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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>Information about a network security perimeter (NSP).</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>:vartype profile: ~azure.mgmt.monitor.models.NetworkSecurityProfile</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>List of provisioning issues, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "Canceled". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>:vartype resource_association: ~azure.mgmt.monitor.models.ResourceAssociation</td>
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
    <td><CopyableCode code="armRoleReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of ARM role receivers that are part of this action group. Roles are Azure RBAC roles and only built-in roles are supported.</td>
</tr>
<tr>
    <td><CopyableCode code="automationRunbookReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of AutomationRunbook receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="azureAppPushReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of AzureAppPush receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="azureFunctionReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of azure function receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="emailReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of email receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of event hub receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="groupShortName" /></td>
    <td><code>string</code></td>
    <td>The short name of the action group. This will be used in SMS messages. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of incident receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="itsmReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of ITSM receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logicAppReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of logic app receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="smsReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of SMS receivers that are part of this action group.</td>
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
    <td><CopyableCode code="voiceReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of voice receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="webhookReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of webhook receivers that are part of this action group.</td>
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
    <td><CopyableCode code="armRoleReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of ARM role receivers that are part of this action group. Roles are Azure RBAC roles and only built-in roles are supported.</td>
</tr>
<tr>
    <td><CopyableCode code="automationRunbookReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of AutomationRunbook receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="azureAppPushReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of AzureAppPush receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="azureFunctionReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of azure function receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="emailReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of email receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of event hub receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="groupShortName" /></td>
    <td><code>string</code></td>
    <td>The short name of the action group. This will be used in SMS messages. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of incident receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="itsmReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of ITSM receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logicAppReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of logic app receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="smsReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of SMS receivers that are part of this action group.</td>
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
    <td><CopyableCode code="voiceReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of voice receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="webhookReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of webhook receivers that are part of this action group.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription_id">

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
    <td><CopyableCode code="armRoleReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of ARM role receivers that are part of this action group. Roles are Azure RBAC roles and only built-in roles are supported.</td>
</tr>
<tr>
    <td><CopyableCode code="automationRunbookReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of AutomationRunbook receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="azureAppPushReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of AzureAppPush receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="azureFunctionReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of azure function receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="emailReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of email receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of event hub receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="groupShortName" /></td>
    <td><code>string</code></td>
    <td>The short name of the action group. This will be used in SMS messages. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of incident receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="itsmReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of ITSM receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logicAppReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of logic app receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="smsReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of SMS receivers that are part of this action group.</td>
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
    <td><CopyableCode code="voiceReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of voice receivers that are part of this action group.</td>
</tr>
<tr>
    <td><CopyableCode code="webhookReceivers" /></td>
    <td><code>array</code></td>
    <td>The list of webhook receivers that are part of this action group.</td>
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
    <td><a href="#get_test_notifications_at_action_group_resource_level"><CopyableCode code="get_test_notifications_at_action_group_resource_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-notification_id"><code>notification_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the test notifications by the notification id.</td>
</tr>
<tr>
    <td><a href="#get_nsp"><CopyableCode code="get_nsp" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a specified NSP configuration for specified action group.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an action group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of all action groups in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription_id"><CopyableCode code="list_by_subscription_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of all action groups in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a new action group or update an existing one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing action group's tags. To update other fields use the CreateOrUpdate method.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a new action group or update an existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an action group.</td>
</tr>
<tr>
    <td><a href="#list_nsp"><CopyableCode code="list_nsp" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of NSP configurations for specified action group.</td>
</tr>
<tr>
    <td><a href="#create_notifications_at_action_group_resource_level"><CopyableCode code="create_notifications_at_action_group_resource_level" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-alertType"><code>alertType</code></a></td>
    <td></td>
    <td>Send test notifications to a set of provided receivers.</td>
</tr>
<tr>
    <td><a href="#enable_receiver"><CopyableCode code="enable_receiver" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-receiverName"><code>receiverName</code></a></td>
    <td></td>
    <td>Enable a receiver in an action group. This changes the receiver's status from Disabled to Enabled. This operation is only supported for Email or SMS receivers.</td>
</tr>
<tr>
    <td><a href="#reconcile_nsp"><CopyableCode code="reconcile_nsp" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-action_group_name"><code>action_group_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reconciles a specified NSP configuration for specified action group.</td>
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
<tr id="parameter-action_group_name">
    <td><CopyableCode code="action_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the action group. Required.</td>
</tr>
<tr id="parameter-network_security_perimeter_configuration_name">
    <td><CopyableCode code="network_security_perimeter_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name for a network security perimeter configuration. Required.</td>
</tr>
<tr id="parameter-notification_id">
    <td><CopyableCode code="notification_id" /></td>
    <td><code>string</code></td>
    <td>The notification id. Required.</td>
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
    defaultValue="get_test_notifications_at_action_group_resource_level"
    values={[
        { label: 'get_test_notifications_at_action_group_resource_level', value: 'get_test_notifications_at_action_group_resource_level' },
        { label: 'get_nsp', value: 'get_nsp' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
    ]}
>
<TabItem value="get_test_notifications_at_action_group_resource_level">

Get the test notifications by the notification id.

```sql
SELECT
actionDetails,
completedTime,
context,
createdTime,
state
FROM azure.monitor.action_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND action_group_name = '{{ action_group_name }}' -- required
AND notification_id = '{{ notification_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_nsp">

Gets a specified NSP configuration for specified action group.

```sql
SELECT
id,
name,
networkSecurityPerimeter,
profile,
provisioningIssues,
provisioningState,
resourceAssociation,
systemData,
type
FROM azure.monitor.action_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND action_group_name = '{{ action_group_name }}' -- required
AND network_security_perimeter_configuration_name = '{{ network_security_perimeter_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get an action group.

```sql
SELECT
id,
name,
armRoleReceivers,
automationRunbookReceivers,
azureAppPushReceivers,
azureFunctionReceivers,
emailReceivers,
enabled,
eventHubReceivers,
groupShortName,
identity,
incidentReceivers,
itsmReceivers,
location,
logicAppReceivers,
smsReceivers,
systemData,
tags,
type,
voiceReceivers,
webhookReceivers
FROM azure.monitor.action_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND action_group_name = '{{ action_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of all action groups in a resource group.

```sql
SELECT
id,
name,
armRoleReceivers,
automationRunbookReceivers,
azureAppPushReceivers,
azureFunctionReceivers,
emailReceivers,
enabled,
eventHubReceivers,
groupShortName,
identity,
incidentReceivers,
itsmReceivers,
location,
logicAppReceivers,
smsReceivers,
systemData,
tags,
type,
voiceReceivers,
webhookReceivers
FROM azure.monitor.action_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription_id">

Get a list of all action groups in a subscription.

```sql
SELECT
id,
name,
armRoleReceivers,
automationRunbookReceivers,
azureAppPushReceivers,
azureFunctionReceivers,
emailReceivers,
enabled,
eventHubReceivers,
groupShortName,
identity,
incidentReceivers,
itsmReceivers,
location,
logicAppReceivers,
smsReceivers,
systemData,
tags,
type,
voiceReceivers,
webhookReceivers
FROM azure.monitor.action_groups
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

Create a new action group or update an existing one.

```sql
INSERT INTO azure.monitor.action_groups (
tags,
location,
properties,
identity,
resource_group_name,
action_group_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ action_group_name }}',
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
- name: action_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the action_groups resource.
    - name: action_group_name
      value: "{{ action_group_name }}"
      description: Required parameter for the action_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the action_groups resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The action groups properties of the resource.
      value:
        groupShortName: "{{ groupShortName }}"
        enabled: {{ enabled }}
        emailReceivers:
          - name: "{{ name }}"
            emailAddress: "{{ emailAddress }}"
            useCommonAlertSchema: {{ useCommonAlertSchema }}
            status: "{{ status }}"
        smsReceivers:
          - name: "{{ name }}"
            countryCode: "{{ countryCode }}"
            phoneNumber: "{{ phoneNumber }}"
            status: "{{ status }}"
        webhookReceivers:
          - name: "{{ name }}"
            serviceUri: "{{ serviceUri }}"
            useCommonAlertSchema: {{ useCommonAlertSchema }}
            useAadAuth: {{ useAadAuth }}
            objectId: "{{ objectId }}"
            identifierUri: "{{ identifierUri }}"
            tenantId: "{{ tenantId }}"
            managedIdentity: "{{ managedIdentity }}"
        itsmReceivers:
          - name: "{{ name }}"
            workspaceId: "{{ workspaceId }}"
            connectionId: "{{ connectionId }}"
            ticketConfiguration: "{{ ticketConfiguration }}"
            region: "{{ region }}"
        azureAppPushReceivers:
          - name: "{{ name }}"
            emailAddress: "{{ emailAddress }}"
        automationRunbookReceivers:
          - automationAccountId: "{{ automationAccountId }}"
            runbookName: "{{ runbookName }}"
            webhookResourceId: "{{ webhookResourceId }}"
            isGlobalRunbook: {{ isGlobalRunbook }}
            name: "{{ name }}"
            serviceUri: "{{ serviceUri }}"
            useCommonAlertSchema: {{ useCommonAlertSchema }}
            managedIdentity: "{{ managedIdentity }}"
        voiceReceivers:
          - name: "{{ name }}"
            countryCode: "{{ countryCode }}"
            phoneNumber: "{{ phoneNumber }}"
        logicAppReceivers:
          - name: "{{ name }}"
            resourceId: "{{ resourceId }}"
            callbackUrl: "{{ callbackUrl }}"
            useCommonAlertSchema: {{ useCommonAlertSchema }}
            managedIdentity: "{{ managedIdentity }}"
        azureFunctionReceivers:
          - name: "{{ name }}"
            functionAppResourceId: "{{ functionAppResourceId }}"
            functionName: "{{ functionName }}"
            httpTriggerUrl: "{{ httpTriggerUrl }}"
            useCommonAlertSchema: {{ useCommonAlertSchema }}
            managedIdentity: "{{ managedIdentity }}"
        armRoleReceivers:
          - name: "{{ name }}"
            roleId: "{{ roleId }}"
            useCommonAlertSchema: {{ useCommonAlertSchema }}
        eventHubReceivers:
          - name: "{{ name }}"
            eventHubNameSpace: "{{ eventHubNameSpace }}"
            eventHubName: "{{ eventHubName }}"
            useCommonAlertSchema: {{ useCommonAlertSchema }}
            tenantId: "{{ tenantId }}"
            subscriptionId: "{{ subscriptionId }}"
            managedIdentity: "{{ managedIdentity }}"
        incidentReceivers:
          - name: "{{ name }}"
            connection:
              name: "{{ name }}"
              id: "{{ id }}"
            incidentManagementService: "{{ incidentManagementService }}"
            mappings: "{{ mappings }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates an existing action group's tags. To update other fields use the CreateOrUpdate method.

```sql
UPDATE azure.monitor.action_groups
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND action_group_name = '{{ action_group_name }}' --required
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

Create a new action group or update an existing one.

```sql
REPLACE azure.monitor.action_groups
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND action_group_name = '{{ action_group_name }}' --required
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

Delete an action group.

```sql
DELETE FROM azure.monitor.action_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND action_group_name = '{{ action_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_nsp"
    values={[
        { label: 'list_nsp', value: 'list_nsp' },
        { label: 'create_notifications_at_action_group_resource_level', value: 'create_notifications_at_action_group_resource_level' },
        { label: 'enable_receiver', value: 'enable_receiver' },
        { label: 'reconcile_nsp', value: 'reconcile_nsp' }
    ]}
>
<TabItem value="list_nsp">

Gets a list of NSP configurations for specified action group.

```sql
EXEC azure.monitor.action_groups.list_nsp 
@resource_group_name='{{ resource_group_name }}' --required, 
@action_group_name='{{ action_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_notifications_at_action_group_resource_level">

Send test notifications to a set of provided receivers.

```sql
EXEC azure.monitor.action_groups.create_notifications_at_action_group_resource_level 
@resource_group_name='{{ resource_group_name }}' --required, 
@action_group_name='{{ action_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"alertType": "{{ alertType }}", 
"emailReceivers": "{{ emailReceivers }}", 
"smsReceivers": "{{ smsReceivers }}", 
"webhookReceivers": "{{ webhookReceivers }}", 
"itsmReceivers": "{{ itsmReceivers }}", 
"azureAppPushReceivers": "{{ azureAppPushReceivers }}", 
"automationRunbookReceivers": "{{ automationRunbookReceivers }}", 
"voiceReceivers": "{{ voiceReceivers }}", 
"logicAppReceivers": "{{ logicAppReceivers }}", 
"azureFunctionReceivers": "{{ azureFunctionReceivers }}", 
"armRoleReceivers": "{{ armRoleReceivers }}", 
"eventHubReceivers": "{{ eventHubReceivers }}", 
"incidentReceivers": "{{ incidentReceivers }}"
}'
;
```
</TabItem>
<TabItem value="enable_receiver">

Enable a receiver in an action group. This changes the receiver's status from Disabled to Enabled. This operation is only supported for Email or SMS receivers.

```sql
EXEC azure.monitor.action_groups.enable_receiver 
@resource_group_name='{{ resource_group_name }}' --required, 
@action_group_name='{{ action_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"receiverName": "{{ receiverName }}"
}'
;
```
</TabItem>
<TabItem value="reconcile_nsp">

Reconciles a specified NSP configuration for specified action group.

```sql
EXEC azure.monitor.action_groups.reconcile_nsp 
@resource_group_name='{{ resource_group_name }}' --required, 
@action_group_name='{{ action_group_name }}' --required, 
@network_security_perimeter_configuration_name='{{ network_security_perimeter_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
