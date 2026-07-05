--- 
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
  - web
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

Creates, updates, deletes, gets or lists a <code>recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recommendations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.recommendations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_rule_details_by_web_app"
    values={[
        { label: 'get_rule_details_by_web_app', value: 'get_rule_details_by_web_app' },
        { label: 'get_rule_details_by_hosting_environment', value: 'get_rule_details_by_hosting_environment' },
        { label: 'list_history_for_hosting_environment', value: 'list_history_for_hosting_environment' },
        { label: 'list_history_for_web_app', value: 'list_history_for_web_app' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_rule_details_by_web_app">

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
    <td><CopyableCode code="actionName" /></td>
    <td><code>string</code></td>
    <td>Name of action that is recommended by this rule in string.</td>
</tr>
<tr>
    <td><CopyableCode code="bladeName" /></td>
    <td><code>string</code></td>
    <td>Deep link to a blade on the portal. Applicable to dynamic rule only.</td>
</tr>
<tr>
    <td><CopyableCode code="categoryTags" /></td>
    <td><code>array</code></td>
    <td>The list of category tags that this recommendation rule belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="channels" /></td>
    <td><code>string</code></td>
    <td>List of available channels that this rule applies. Known values are: "Notification", "Api", "Email", "Webhook", and "All". (Notification, Api, Email, Webhook, All)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Localized detailed description of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>UI friendly name of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionName" /></td>
    <td><code>string</code></td>
    <td>Extension name of the portal if exists. Applicable to dynamic rule only.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardLink" /></td>
    <td><code>string</code></td>
    <td>Forward link to an external document associated with the rule. Applicable to dynamic rule only.</td>
</tr>
<tr>
    <td><CopyableCode code="isDynamic" /></td>
    <td><code>boolean</code></td>
    <td>True if this is associated with a dynamically added rule.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level of impact indicating how critical this rule is. Known values are: "Critical", "Warning", "Information", and "NonUrgentSuggestion". (Critical, Warning, Information, NonUrgentSuggestion)</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Localized name of the rule (Good for UI).</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationId" /></td>
    <td><code>string</code></td>
    <td>Recommendation ID of an associated recommendation object tied to the rule, if exists. If such an object doesn't exist, it is set to null.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationName" /></td>
    <td><code>string</code></td>
    <td>Unique name of the rule.</td>
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
<TabItem value="get_rule_details_by_hosting_environment">

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
    <td><CopyableCode code="actionName" /></td>
    <td><code>string</code></td>
    <td>Name of action that is recommended by this rule in string.</td>
</tr>
<tr>
    <td><CopyableCode code="bladeName" /></td>
    <td><code>string</code></td>
    <td>Deep link to a blade on the portal. Applicable to dynamic rule only.</td>
</tr>
<tr>
    <td><CopyableCode code="categoryTags" /></td>
    <td><code>array</code></td>
    <td>The list of category tags that this recommendation rule belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="channels" /></td>
    <td><code>string</code></td>
    <td>List of available channels that this rule applies. Known values are: "Notification", "Api", "Email", "Webhook", and "All". (Notification, Api, Email, Webhook, All)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Localized detailed description of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>UI friendly name of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionName" /></td>
    <td><code>string</code></td>
    <td>Extension name of the portal if exists. Applicable to dynamic rule only.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardLink" /></td>
    <td><code>string</code></td>
    <td>Forward link to an external document associated with the rule. Applicable to dynamic rule only.</td>
</tr>
<tr>
    <td><CopyableCode code="isDynamic" /></td>
    <td><code>boolean</code></td>
    <td>True if this is associated with a dynamically added rule.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level of impact indicating how critical this rule is. Known values are: "Critical", "Warning", "Information", and "NonUrgentSuggestion". (Critical, Warning, Information, NonUrgentSuggestion)</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Localized name of the rule (Good for UI).</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationId" /></td>
    <td><code>string</code></td>
    <td>Recommendation ID of an associated recommendation object tied to the rule, if exists. If such an object doesn't exist, it is set to null.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationName" /></td>
    <td><code>string</code></td>
    <td>Unique name of the rule.</td>
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
<TabItem value="list_history_for_hosting_environment">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="actionName" /></td>
    <td><code>string</code></td>
    <td>Name of action recommended by this object.</td>
</tr>
<tr>
    <td><CopyableCode code="bladeName" /></td>
    <td><code>string</code></td>
    <td>Deep link to a blade on the portal.</td>
</tr>
<tr>
    <td><CopyableCode code="categoryTags" /></td>
    <td><code>array</code></td>
    <td>The list of category tags that this recommendation belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="channels" /></td>
    <td><code>string</code></td>
    <td>List of channels that this recommendation can apply. Known values are: "Notification", "Api", "Email", "Webhook", and "All". (Notification, Api, Email, Webhook, All)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this instance was created.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>UI friendly name of the rule (may not be unique).</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>integer</code></td>
    <td>True if this recommendation is still valid (i.e. "actionable"). False if it is invalid.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time in UTC of a range that the recommendation refers to.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionName" /></td>
    <td><code>string</code></td>
    <td>Extension name of the portal if exists.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardLink" /></td>
    <td><code>string</code></td>
    <td>Forward link to an external document associated with the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isDynamic" /></td>
    <td><code>boolean</code></td>
    <td>True if this is associated with a dynamically added rule.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level indicating how critical this recommendation can impact. Known values are: "Critical", "Warning", "Information", and "NonUrgentSuggestion". (Critical, Warning, Information, NonUrgentSuggestion)</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Recommendation text.</td>
</tr>
<tr>
    <td><CopyableCode code="nextNotificationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When to notify this recommendation next in UTC. Null means that this will never be notified anymore.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC when this notification expires.</td>
</tr>
<tr>
    <td><CopyableCode code="notifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last timestamp in UTC this instance was actually notified. Null means that this recommendation hasn't been notified yet.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationId" /></td>
    <td><code>string</code></td>
    <td>A GUID value that each recommendation object is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Full ARM resource ID string that this recommendation object is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceScope" /></td>
    <td><code>string</code></td>
    <td>Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site. Known values are: "ServerFarm", "Subscription", and "WebSite". (ServerFarm, Subscription, WebSite)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleName" /></td>
    <td><code>string</code></td>
    <td>Unique name of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="score" /></td>
    <td><code>number</code></td>
    <td>A metric value measured by the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The beginning time in UTC of a range that the recommendation refers to.</td>
</tr>
<tr>
    <td><CopyableCode code="states" /></td>
    <td><code>array</code></td>
    <td>The list of states of this recommendation. If it's null then it should be considered "Active".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_history_for_web_app">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="actionName" /></td>
    <td><code>string</code></td>
    <td>Name of action recommended by this object.</td>
</tr>
<tr>
    <td><CopyableCode code="bladeName" /></td>
    <td><code>string</code></td>
    <td>Deep link to a blade on the portal.</td>
</tr>
<tr>
    <td><CopyableCode code="categoryTags" /></td>
    <td><code>array</code></td>
    <td>The list of category tags that this recommendation belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="channels" /></td>
    <td><code>string</code></td>
    <td>List of channels that this recommendation can apply. Known values are: "Notification", "Api", "Email", "Webhook", and "All". (Notification, Api, Email, Webhook, All)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this instance was created.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>UI friendly name of the rule (may not be unique).</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>integer</code></td>
    <td>True if this recommendation is still valid (i.e. "actionable"). False if it is invalid.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time in UTC of a range that the recommendation refers to.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionName" /></td>
    <td><code>string</code></td>
    <td>Extension name of the portal if exists.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardLink" /></td>
    <td><code>string</code></td>
    <td>Forward link to an external document associated with the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isDynamic" /></td>
    <td><code>boolean</code></td>
    <td>True if this is associated with a dynamically added rule.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level indicating how critical this recommendation can impact. Known values are: "Critical", "Warning", "Information", and "NonUrgentSuggestion". (Critical, Warning, Information, NonUrgentSuggestion)</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Recommendation text.</td>
</tr>
<tr>
    <td><CopyableCode code="nextNotificationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When to notify this recommendation next in UTC. Null means that this will never be notified anymore.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC when this notification expires.</td>
</tr>
<tr>
    <td><CopyableCode code="notifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last timestamp in UTC this instance was actually notified. Null means that this recommendation hasn't been notified yet.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationId" /></td>
    <td><code>string</code></td>
    <td>A GUID value that each recommendation object is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Full ARM resource ID string that this recommendation object is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceScope" /></td>
    <td><code>string</code></td>
    <td>Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site. Known values are: "ServerFarm", "Subscription", and "WebSite". (ServerFarm, Subscription, WebSite)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleName" /></td>
    <td><code>string</code></td>
    <td>Unique name of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="score" /></td>
    <td><code>number</code></td>
    <td>A metric value measured by the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The beginning time in UTC of a range that the recommendation refers to.</td>
</tr>
<tr>
    <td><CopyableCode code="states" /></td>
    <td><code>array</code></td>
    <td>The list of states of this recommendation. If it's null then it should be considered "Active".</td>
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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="actionName" /></td>
    <td><code>string</code></td>
    <td>Name of action recommended by this object.</td>
</tr>
<tr>
    <td><CopyableCode code="bladeName" /></td>
    <td><code>string</code></td>
    <td>Deep link to a blade on the portal.</td>
</tr>
<tr>
    <td><CopyableCode code="categoryTags" /></td>
    <td><code>array</code></td>
    <td>The list of category tags that this recommendation belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="channels" /></td>
    <td><code>string</code></td>
    <td>List of channels that this recommendation can apply. Known values are: "Notification", "Api", "Email", "Webhook", and "All". (Notification, Api, Email, Webhook, All)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this instance was created.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>UI friendly name of the rule (may not be unique).</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>integer</code></td>
    <td>True if this recommendation is still valid (i.e. "actionable"). False if it is invalid.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time in UTC of a range that the recommendation refers to.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionName" /></td>
    <td><code>string</code></td>
    <td>Extension name of the portal if exists.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardLink" /></td>
    <td><code>string</code></td>
    <td>Forward link to an external document associated with the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isDynamic" /></td>
    <td><code>boolean</code></td>
    <td>True if this is associated with a dynamically added rule.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level indicating how critical this recommendation can impact. Known values are: "Critical", "Warning", "Information", and "NonUrgentSuggestion". (Critical, Warning, Information, NonUrgentSuggestion)</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Recommendation text.</td>
</tr>
<tr>
    <td><CopyableCode code="nextNotificationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When to notify this recommendation next in UTC. Null means that this will never be notified anymore.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC when this notification expires.</td>
</tr>
<tr>
    <td><CopyableCode code="notifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last timestamp in UTC this instance was actually notified. Null means that this recommendation hasn't been notified yet.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationId" /></td>
    <td><code>string</code></td>
    <td>A GUID value that each recommendation object is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Full ARM resource ID string that this recommendation object is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceScope" /></td>
    <td><code>string</code></td>
    <td>Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site. Known values are: "ServerFarm", "Subscription", and "WebSite". (ServerFarm, Subscription, WebSite)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleName" /></td>
    <td><code>string</code></td>
    <td>Unique name of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="score" /></td>
    <td><code>number</code></td>
    <td>A metric value measured by the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The beginning time in UTC of a range that the recommendation refers to.</td>
</tr>
<tr>
    <td><CopyableCode code="states" /></td>
    <td><code>array</code></td>
    <td>The list of states of this recommendation. If it's null then it should be considered "Active".</td>
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
    <td><a href="#get_rule_details_by_web_app"><CopyableCode code="get_rule_details_by_web_app" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-updateSeen"><code>updateSeen</code></a>, <a href="#parameter-recommendationId"><code>recommendationId</code></a></td>
    <td>Get a recommendation rule for an app. Description for Get a recommendation rule for an app.</td>
</tr>
<tr>
    <td><a href="#get_rule_details_by_hosting_environment"><CopyableCode code="get_rule_details_by_hosting_environment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-hosting_environment_name"><code>hosting_environment_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-updateSeen"><code>updateSeen</code></a>, <a href="#parameter-recommendationId"><code>recommendationId</code></a></td>
    <td>Get a recommendation rule for an app. Description for Get a recommendation rule for an app.</td>
</tr>
<tr>
    <td><a href="#list_history_for_hosting_environment"><CopyableCode code="list_history_for_hosting_environment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-hosting_environment_name"><code>hosting_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-expiredOnly"><code>expiredOnly</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get past recommendations for an app, optionally specified by the time range. Description for Get past recommendations for an app, optionally specified by the time range.</td>
</tr>
<tr>
    <td><a href="#list_history_for_web_app"><CopyableCode code="list_history_for_web_app" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-expiredOnly"><code>expiredOnly</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get past recommendations for an app, optionally specified by the time range. Description for Get past recommendations for an app, optionally specified by the time range.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-featured"><code>featured</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>List all recommendations for a subscription. Description for List all recommendations for a subscription.</td>
</tr>
<tr>
    <td><a href="#list_recommended_rules_for_hosting_environment"><CopyableCode code="list_recommended_rules_for_hosting_environment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-hosting_environment_name"><code>hosting_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-featured"><code>featured</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all recommendations for a hosting environment. Description for Get all recommendations for a hosting environment.</td>
</tr>
<tr>
    <td><a href="#list_recommended_rules_for_web_app"><CopyableCode code="list_recommended_rules_for_web_app" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-featured"><code>featured</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all recommendations for an app. Description for Get all recommendations for an app.</td>
</tr>
<tr>
    <td><a href="#disable_recommendation_for_site"><CopyableCode code="disable_recommendation_for_site" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables the specific rule for a web site permanently. Description for Disables the specific rule for a web site permanently.</td>
</tr>
<tr>
    <td><a href="#disable_all_for_hosting_environment"><CopyableCode code="disable_all_for_hosting_environment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-hosting_environment_name"><code>hosting_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-environmentName"><code>environmentName</code></a></td>
    <td></td>
    <td>Disable all recommendations for an app. Description for Disable all recommendations for an app.</td>
</tr>
<tr>
    <td><a href="#reset_all_filters_for_hosting_environment"><CopyableCode code="reset_all_filters_for_hosting_environment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-hosting_environment_name"><code>hosting_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-environmentName"><code>environmentName</code></a></td>
    <td></td>
    <td>Reset all recommendation opt-out settings for an app. Description for Reset all recommendation opt-out settings for an app.</td>
</tr>
<tr>
    <td><a href="#disable_recommendation_for_hosting_environment"><CopyableCode code="disable_recommendation_for_hosting_environment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-hosting_environment_name"><code>hosting_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-environmentName"><code>environmentName</code></a></td>
    <td></td>
    <td>Disables the specific rule for a web site permanently. Description for Disables the specific rule for a web site permanently.</td>
</tr>
<tr>
    <td><a href="#disable_all_for_web_app"><CopyableCode code="disable_all_for_web_app" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable all recommendations for an app. Description for Disable all recommendations for an app.</td>
</tr>
<tr>
    <td><a href="#reset_all_filters_for_web_app"><CopyableCode code="reset_all_filters_for_web_app" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reset all recommendation opt-out settings for an app. Description for Reset all recommendation opt-out settings for an app.</td>
</tr>
<tr>
    <td><a href="#reset_all_filters"><CopyableCode code="reset_all_filters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reset all recommendation opt-out settings for a subscription. Description for Reset all recommendation opt-out settings for a subscription.</td>
</tr>
<tr>
    <td><a href="#disable_recommendation_for_subscription"><CopyableCode code="disable_recommendation_for_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables the specified rule so it will not apply to a subscription in the future. Description for Disables the specified rule so it will not apply to a subscription in the future.</td>
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
<tr id="parameter-environmentName">
    <td><CopyableCode code="environmentName" /></td>
    <td><code>string</code></td>
    <td>Site name. Required.</td>
</tr>
<tr id="parameter-hosting_environment_name">
    <td><CopyableCode code="hosting_environment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the hosting environment. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Rule name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-site_name">
    <td><CopyableCode code="site_name" /></td>
    <td><code>string</code></td>
    <td>Name of the app. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter=channel eq 'Api' or channel eq 'Notification'. Default value is None.</td>
</tr>
<tr id="parameter-expiredOnly">
    <td><CopyableCode code="expiredOnly" /></td>
    <td><code>boolean</code></td>
    <td>Specify false to return all recommendations. The default is true, which returns only expired recommendations. Default value is None.</td>
</tr>
<tr id="parameter-featured">
    <td><CopyableCode code="featured" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to return only the most critical recommendations. The default is false, which returns all recommendations. Default value is None.</td>
</tr>
<tr id="parameter-recommendationId">
    <td><CopyableCode code="recommendationId" /></td>
    <td><code>string</code></td>
    <td>The GUID of the recommendation object if you query an expired one. You don't need to specify it to query an active entry. Default value is None.</td>
</tr>
<tr id="parameter-updateSeen">
    <td><CopyableCode code="updateSeen" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to update the last-seen timestamp of the recommendation object. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_rule_details_by_web_app"
    values={[
        { label: 'get_rule_details_by_web_app', value: 'get_rule_details_by_web_app' },
        { label: 'get_rule_details_by_hosting_environment', value: 'get_rule_details_by_hosting_environment' },
        { label: 'list_history_for_hosting_environment', value: 'list_history_for_hosting_environment' },
        { label: 'list_history_for_web_app', value: 'list_history_for_web_app' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_rule_details_by_web_app">

Get a recommendation rule for an app. Description for Get a recommendation rule for an app.

```sql
SELECT
id,
name,
actionName,
bladeName,
categoryTags,
channels,
description,
displayName,
extensionName,
forwardLink,
isDynamic,
kind,
level,
message,
recommendationId,
recommendationName,
systemData,
type
FROM azure.web.recommendations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND updateSeen = '{{ updateSeen }}'
AND recommendationId = '{{ recommendationId }}'
;
```
</TabItem>
<TabItem value="get_rule_details_by_hosting_environment">

Get a recommendation rule for an app. Description for Get a recommendation rule for an app.

```sql
SELECT
id,
name,
actionName,
bladeName,
categoryTags,
channels,
description,
displayName,
extensionName,
forwardLink,
isDynamic,
kind,
level,
message,
recommendationId,
recommendationName,
systemData,
type
FROM azure.web.recommendations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND hosting_environment_name = '{{ hosting_environment_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND updateSeen = '{{ updateSeen }}'
AND recommendationId = '{{ recommendationId }}'
;
```
</TabItem>
<TabItem value="list_history_for_hosting_environment">

Get past recommendations for an app, optionally specified by the time range. Description for Get past recommendations for an app, optionally specified by the time range.

```sql
SELECT
id,
name,
actionName,
bladeName,
categoryTags,
channels,
creationTime,
displayName,
enabled,
endTime,
extensionName,
forwardLink,
isDynamic,
kind,
level,
message,
nextNotificationTime,
notificationExpirationTime,
notifiedTime,
recommendationId,
resourceId,
resourceScope,
ruleName,
score,
startTime,
states,
type
FROM azure.web.recommendations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND hosting_environment_name = '{{ hosting_environment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND expiredOnly = '{{ expiredOnly }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_history_for_web_app">

Get past recommendations for an app, optionally specified by the time range. Description for Get past recommendations for an app, optionally specified by the time range.

```sql
SELECT
id,
name,
actionName,
bladeName,
categoryTags,
channels,
creationTime,
displayName,
enabled,
endTime,
extensionName,
forwardLink,
isDynamic,
kind,
level,
message,
nextNotificationTime,
notificationExpirationTime,
notifiedTime,
recommendationId,
resourceId,
resourceScope,
ruleName,
score,
startTime,
states,
type
FROM azure.web.recommendations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND expiredOnly = '{{ expiredOnly }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

List all recommendations for a subscription. Description for List all recommendations for a subscription.

```sql
SELECT
id,
name,
actionName,
bladeName,
categoryTags,
channels,
creationTime,
displayName,
enabled,
endTime,
extensionName,
forwardLink,
isDynamic,
kind,
level,
message,
nextNotificationTime,
notificationExpirationTime,
notifiedTime,
recommendationId,
resourceId,
resourceScope,
ruleName,
score,
startTime,
states,
type
FROM azure.web.recommendations
WHERE subscription_id = '{{ subscription_id }}' -- required
AND featured = '{{ featured }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_recommended_rules_for_hosting_environment"
    values={[
        { label: 'list_recommended_rules_for_hosting_environment', value: 'list_recommended_rules_for_hosting_environment' },
        { label: 'list_recommended_rules_for_web_app', value: 'list_recommended_rules_for_web_app' },
        { label: 'disable_recommendation_for_site', value: 'disable_recommendation_for_site' },
        { label: 'disable_all_for_hosting_environment', value: 'disable_all_for_hosting_environment' },
        { label: 'reset_all_filters_for_hosting_environment', value: 'reset_all_filters_for_hosting_environment' },
        { label: 'disable_recommendation_for_hosting_environment', value: 'disable_recommendation_for_hosting_environment' },
        { label: 'disable_all_for_web_app', value: 'disable_all_for_web_app' },
        { label: 'reset_all_filters_for_web_app', value: 'reset_all_filters_for_web_app' },
        { label: 'reset_all_filters', value: 'reset_all_filters' },
        { label: 'disable_recommendation_for_subscription', value: 'disable_recommendation_for_subscription' }
    ]}
>
<TabItem value="list_recommended_rules_for_hosting_environment">

Get all recommendations for a hosting environment. Description for Get all recommendations for a hosting environment.

```sql
EXEC azure.web.recommendations.list_recommended_rules_for_hosting_environment 
@resource_group_name='{{ resource_group_name }}' --required, 
@hosting_environment_name='{{ hosting_environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@featured={{ featured }}, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_recommended_rules_for_web_app">

Get all recommendations for an app. Description for Get all recommendations for an app.

```sql
EXEC azure.web.recommendations.list_recommended_rules_for_web_app 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@featured={{ featured }}, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="disable_recommendation_for_site">

Disables the specific rule for a web site permanently. Description for Disables the specific rule for a web site permanently.

```sql
EXEC azure.web.recommendations.disable_recommendation_for_site 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="disable_all_for_hosting_environment">

Disable all recommendations for an app. Description for Disable all recommendations for an app.

```sql
EXEC azure.web.recommendations.disable_all_for_hosting_environment 
@resource_group_name='{{ resource_group_name }}' --required, 
@hosting_environment_name='{{ hosting_environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@environmentName='{{ environmentName }}' --required
;
```
</TabItem>
<TabItem value="reset_all_filters_for_hosting_environment">

Reset all recommendation opt-out settings for an app. Description for Reset all recommendation opt-out settings for an app.

```sql
EXEC azure.web.recommendations.reset_all_filters_for_hosting_environment 
@resource_group_name='{{ resource_group_name }}' --required, 
@hosting_environment_name='{{ hosting_environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@environmentName='{{ environmentName }}' --required
;
```
</TabItem>
<TabItem value="disable_recommendation_for_hosting_environment">

Disables the specific rule for a web site permanently. Description for Disables the specific rule for a web site permanently.

```sql
EXEC azure.web.recommendations.disable_recommendation_for_hosting_environment 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@hosting_environment_name='{{ hosting_environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@environmentName='{{ environmentName }}' --required
;
```
</TabItem>
<TabItem value="disable_all_for_web_app">

Disable all recommendations for an app. Description for Disable all recommendations for an app.

```sql
EXEC azure.web.recommendations.disable_all_for_web_app 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_all_filters_for_web_app">

Reset all recommendation opt-out settings for an app. Description for Reset all recommendation opt-out settings for an app.

```sql
EXEC azure.web.recommendations.reset_all_filters_for_web_app 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_all_filters">

Reset all recommendation opt-out settings for a subscription. Description for Reset all recommendation opt-out settings for a subscription.

```sql
EXEC azure.web.recommendations.reset_all_filters 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="disable_recommendation_for_subscription">

Disables the specified rule so it will not apply to a subscription in the future. Description for Disables the specified rule so it will not apply to a subscription in the future.

```sql
EXEC azure.web.recommendations.disable_recommendation_for_subscription 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
