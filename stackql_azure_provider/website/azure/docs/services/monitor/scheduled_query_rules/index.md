--- 
title: scheduled_query_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_query_rules
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

Creates, updates, deletes, gets or lists a <code>scheduled_query_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scheduled_query_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.scheduled_query_rules" /></td></tr>
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
    <td><CopyableCode code="actions" /></td>
    <td><code>object</code></td>
    <td>Actions to invoke when the alert fires.</td>
</tr>
<tr>
    <td><CopyableCode code="autoMitigate" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the alert should be automatically resolved or not. The default is true. Relevant only for rules of kinds LogAlert and SimpleLogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="checkWorkspaceAlertsStorageConfigured" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule should be stored in the customer's storage. The default is false. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="createdWithApiVersion" /></td>
    <td><code>string</code></td>
    <td>The api-version used when creating this alert rule.</td>
</tr>
<tr>
    <td><CopyableCode code="criteria" /></td>
    <td><code>object</code></td>
    <td>The rule criteria that defines the conditions of the scheduled query rule.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the scheduled query rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule is enabled. Value should be true or false.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationFrequency" /></td>
    <td><code>string</code></td>
    <td>How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isLegacyLogAnalyticsRule" /></td>
    <td><code>boolean</code></td>
    <td>True if alert rule is legacy Log Analytic rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isWorkspaceAlertsStorageConfigured" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule has been configured to be stored in the customer's storage. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of scheduled query rule. The default is LogAlert. Known values are: "LogAlert", "SimpleLogAlert", and "LogToMetric". (LogAlert, SimpleLogAlert, LogToMetric)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="muteActionsDuration" /></td>
    <td><code>string</code></td>
    <td>Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="overrideQueryTimeRange" /></td>
    <td><code>string</code></td>
    <td>If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods). Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="resolveConfiguration" /></td>
    <td><code>object</code></td>
    <td>Defines the configuration for resolving fired alerts. Relevant only for rules of kinds LogAlert and SimpleLogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of resource id's that this scheduled query rule is scoped to.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>object</code></td>
    <td>Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert. Known values are: 0, 1, 2, 3, and 4.</td>
</tr>
<tr>
    <td><CopyableCode code="skipQueryValidation" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether the provided query should be validated or not. The default is false. Relevant only for rules of the kind LogAlert.</td>
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
    <td><CopyableCode code="targetResourceTypes" /></td>
    <td><code>array</code></td>
    <td>List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="windowSize" /></td>
    <td><code>string</code></td>
    <td>The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Relevant and required only for rules of the kind LogAlert.</td>
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
    <td><CopyableCode code="actions" /></td>
    <td><code>object</code></td>
    <td>Actions to invoke when the alert fires.</td>
</tr>
<tr>
    <td><CopyableCode code="autoMitigate" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the alert should be automatically resolved or not. The default is true. Relevant only for rules of kinds LogAlert and SimpleLogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="checkWorkspaceAlertsStorageConfigured" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule should be stored in the customer's storage. The default is false. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="createdWithApiVersion" /></td>
    <td><code>string</code></td>
    <td>The api-version used when creating this alert rule.</td>
</tr>
<tr>
    <td><CopyableCode code="criteria" /></td>
    <td><code>object</code></td>
    <td>The rule criteria that defines the conditions of the scheduled query rule.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the scheduled query rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule is enabled. Value should be true or false.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationFrequency" /></td>
    <td><code>string</code></td>
    <td>How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isLegacyLogAnalyticsRule" /></td>
    <td><code>boolean</code></td>
    <td>True if alert rule is legacy Log Analytic rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isWorkspaceAlertsStorageConfigured" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule has been configured to be stored in the customer's storage. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of scheduled query rule. The default is LogAlert. Known values are: "LogAlert", "SimpleLogAlert", and "LogToMetric". (LogAlert, SimpleLogAlert, LogToMetric)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="muteActionsDuration" /></td>
    <td><code>string</code></td>
    <td>Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="overrideQueryTimeRange" /></td>
    <td><code>string</code></td>
    <td>If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods). Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="resolveConfiguration" /></td>
    <td><code>object</code></td>
    <td>Defines the configuration for resolving fired alerts. Relevant only for rules of kinds LogAlert and SimpleLogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of resource id's that this scheduled query rule is scoped to.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>object</code></td>
    <td>Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert. Known values are: 0, 1, 2, 3, and 4.</td>
</tr>
<tr>
    <td><CopyableCode code="skipQueryValidation" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether the provided query should be validated or not. The default is false. Relevant only for rules of the kind LogAlert.</td>
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
    <td><CopyableCode code="targetResourceTypes" /></td>
    <td><code>array</code></td>
    <td>List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="windowSize" /></td>
    <td><code>string</code></td>
    <td>The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Relevant and required only for rules of the kind LogAlert.</td>
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
    <td><CopyableCode code="actions" /></td>
    <td><code>object</code></td>
    <td>Actions to invoke when the alert fires.</td>
</tr>
<tr>
    <td><CopyableCode code="autoMitigate" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the alert should be automatically resolved or not. The default is true. Relevant only for rules of kinds LogAlert and SimpleLogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="checkWorkspaceAlertsStorageConfigured" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule should be stored in the customer's storage. The default is false. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="createdWithApiVersion" /></td>
    <td><code>string</code></td>
    <td>The api-version used when creating this alert rule.</td>
</tr>
<tr>
    <td><CopyableCode code="criteria" /></td>
    <td><code>object</code></td>
    <td>The rule criteria that defines the conditions of the scheduled query rule.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the scheduled query rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule is enabled. Value should be true or false.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationFrequency" /></td>
    <td><code>string</code></td>
    <td>How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isLegacyLogAnalyticsRule" /></td>
    <td><code>boolean</code></td>
    <td>True if alert rule is legacy Log Analytic rule.</td>
</tr>
<tr>
    <td><CopyableCode code="isWorkspaceAlertsStorageConfigured" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether this scheduled query rule has been configured to be stored in the customer's storage. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of scheduled query rule. The default is LogAlert. Known values are: "LogAlert", "SimpleLogAlert", and "LogToMetric". (LogAlert, SimpleLogAlert, LogToMetric)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="muteActionsDuration" /></td>
    <td><code>string</code></td>
    <td>Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="overrideQueryTimeRange" /></td>
    <td><code>string</code></td>
    <td>If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods). Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="resolveConfiguration" /></td>
    <td><code>object</code></td>
    <td>Defines the configuration for resolving fired alerts. Relevant only for rules of kinds LogAlert and SimpleLogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of resource id's that this scheduled query rule is scoped to.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>object</code></td>
    <td>Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert. Known values are: 0, 1, 2, 3, and 4.</td>
</tr>
<tr>
    <td><CopyableCode code="skipQueryValidation" /></td>
    <td><code>boolean</code></td>
    <td>The flag which indicates whether the provided query should be validated or not. The default is false. Relevant only for rules of the kind LogAlert.</td>
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
    <td><CopyableCode code="targetResourceTypes" /></td>
    <td><code>array</code></td>
    <td>List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="windowSize" /></td>
    <td><code>string</code></td>
    <td>The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Relevant and required only for rules of the kind LogAlert.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve an scheduled query rule definition.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve scheduled query rule definitions in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a scheduled query rule definitions in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a scheduled query rule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a scheduled query rule.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a scheduled query rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a scheduled query rule.</td>
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
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the rule. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Retrieve an scheduled query rule definition.

```sql
SELECT
id,
name,
actions,
autoMitigate,
checkWorkspaceAlertsStorageConfigured,
createdWithApiVersion,
criteria,
description,
displayName,
enabled,
etag,
evaluationFrequency,
identity,
isLegacyLogAnalyticsRule,
isWorkspaceAlertsStorageConfigured,
kind,
location,
muteActionsDuration,
overrideQueryTimeRange,
resolveConfiguration,
scopes,
severity,
skipQueryValidation,
systemData,
tags,
targetResourceTypes,
type,
windowSize
FROM azure.monitor.scheduled_query_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieve scheduled query rule definitions in a resource group.

```sql
SELECT
id,
name,
actions,
autoMitigate,
checkWorkspaceAlertsStorageConfigured,
createdWithApiVersion,
criteria,
description,
displayName,
enabled,
etag,
evaluationFrequency,
identity,
isLegacyLogAnalyticsRule,
isWorkspaceAlertsStorageConfigured,
kind,
location,
muteActionsDuration,
overrideQueryTimeRange,
resolveConfiguration,
scopes,
severity,
skipQueryValidation,
systemData,
tags,
targetResourceTypes,
type,
windowSize
FROM azure.monitor.scheduled_query_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Retrieve a scheduled query rule definitions in a subscription.

```sql
SELECT
id,
name,
actions,
autoMitigate,
checkWorkspaceAlertsStorageConfigured,
createdWithApiVersion,
criteria,
description,
displayName,
enabled,
etag,
evaluationFrequency,
identity,
isLegacyLogAnalyticsRule,
isWorkspaceAlertsStorageConfigured,
kind,
location,
muteActionsDuration,
overrideQueryTimeRange,
resolveConfiguration,
scopes,
severity,
skipQueryValidation,
systemData,
tags,
targetResourceTypes,
type,
windowSize
FROM azure.monitor.scheduled_query_rules
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

Creates or updates a scheduled query rule.

```sql
INSERT INTO azure.monitor.scheduled_query_rules (
properties,
identity,
tags,
location,
kind,
resource_group_name,
rule_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ tags }}',
'{{ location }}' /* required */,
'{{ kind }}',
'{{ resource_group_name }}',
'{{ rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
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
- name: scheduled_query_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the scheduled_query_rules resource.
    - name: rule_name
      value: "{{ rule_name }}"
      description: Required parameter for the scheduled_query_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the scheduled_query_rules resource.
    - name: properties
      description: |
        The rule properties of the resource. Required.
      value:
        createdWithApiVersion: "{{ createdWithApiVersion }}"
        isLegacyLogAnalyticsRule: {{ isLegacyLogAnalyticsRule }}
        description: "{{ description }}"
        displayName: "{{ displayName }}"
        severity: "{{ severity }}"
        enabled: {{ enabled }}
        scopes:
          - "{{ scopes }}"
        evaluationFrequency: "{{ evaluationFrequency }}"
        windowSize: "{{ windowSize }}"
        overrideQueryTimeRange: "{{ overrideQueryTimeRange }}"
        targetResourceTypes:
          - "{{ targetResourceTypes }}"
        criteria:
          allOf:
            - criterionType: "{{ criterionType }}"
              query: "{{ query }}"
              timeAggregation: "{{ timeAggregation }}"
              metricMeasureColumn: "{{ metricMeasureColumn }}"
              resourceIdColumn: "{{ resourceIdColumn }}"
              dimensions: "{{ dimensions }}"
              operator: "{{ operator }}"
              threshold: {{ threshold }}
              alertSensitivity: "{{ alertSensitivity }}"
              ignoreDataBefore: "{{ ignoreDataBefore }}"
              failingPeriods:
                numberOfEvaluationPeriods: {{ numberOfEvaluationPeriods }}
                minFailingPeriodsToAlert: {{ minFailingPeriodsToAlert }}
              metricName: "{{ metricName }}"
              minRecurrenceCount: {{ minRecurrenceCount }}
        muteActionsDuration: "{{ muteActionsDuration }}"
        actions:
          actionGroups:
            - "{{ actionGroups }}"
          customProperties: "{{ customProperties }}"
          actionProperties: "{{ actionProperties }}"
        isWorkspaceAlertsStorageConfigured: {{ isWorkspaceAlertsStorageConfigured }}
        checkWorkspaceAlertsStorageConfigured: {{ checkWorkspaceAlertsStorageConfigured }}
        skipQueryValidation: {{ skipQueryValidation }}
        autoMitigate: {{ autoMitigate }}
        resolveConfiguration:
          autoResolved: {{ autoResolved }}
          timeToResolve: "{{ timeToResolve }}"
    - name: identity
      description: |
        The identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: kind
      value: "{{ kind }}"
      description: |
        Indicates the type of scheduled query rule. The default is LogAlert. Known values are: "LogAlert", "SimpleLogAlert", and "LogToMetric".
      valid_values: ['LogAlert', 'SimpleLogAlert', 'LogToMetric']
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

Update a scheduled query rule.

```sql
UPDATE azure.monitor.scheduled_query_rules
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Creates or updates a scheduled query rule.

```sql
REPLACE azure.monitor.scheduled_query_rules
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
tags = '{{ tags }}',
location = '{{ location }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Deletes a scheduled query rule.

```sql
DELETE FROM azure.monitor.scheduled_query_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
