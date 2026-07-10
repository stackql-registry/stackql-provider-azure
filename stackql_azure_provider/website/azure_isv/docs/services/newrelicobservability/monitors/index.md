--- 
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - newrelicobservability
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

Creates, updates, deletes, gets or lists a <code>monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="monitors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelicobservability.monitors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_app_services"
    values={[
        { label: 'list_app_services', value: 'list_app_services' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_app_services">

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
    <td><CopyableCode code="agentStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the NewRelic agent installed on the App service.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the NewRelic agent installed on the App service.</td>
</tr>
<tr>
    <td><CopyableCode code="azureResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure App service resource ID.</td>
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
    <td><CopyableCode code="accountCreationSource" /></td>
    <td><code>string</code></td>
    <td>Source of account creation. Known values are: "LIFTR" and "NEWRELIC".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Liftr resource category. Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>Liftr resource preference. The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Marketplace Subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>NewRelic Organization properties of the resource. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>MonitoringStatus of the resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="newRelicAccountProperties" /></td>
    <td><code>object</code></td>
    <td>MarketplaceSubscriptionStatus of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="orgCreationSource" /></td>
    <td><code>string</code></td>
    <td>Source of org creation. Known values are: "LIFTR" and "NEWRELIC".</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Plan details.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="saaSAzureSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Subscription where Marketplace SaaS is located.</td>
</tr>
<tr>
    <td><CopyableCode code="saaSData" /></td>
    <td><code>object</code></td>
    <td>SaaS details.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure Subscription containing the monitor resource.</td>
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
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User Info.</td>
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
    <td><CopyableCode code="accountCreationSource" /></td>
    <td><code>string</code></td>
    <td>Source of account creation. Known values are: "LIFTR" and "NEWRELIC".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Liftr resource category. Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>Liftr resource preference. The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Marketplace Subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>NewRelic Organization properties of the resource. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>MonitoringStatus of the resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="newRelicAccountProperties" /></td>
    <td><code>object</code></td>
    <td>MarketplaceSubscriptionStatus of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="orgCreationSource" /></td>
    <td><code>string</code></td>
    <td>Source of org creation. Known values are: "LIFTR" and "NEWRELIC".</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Plan details.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="saaSAzureSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Subscription where Marketplace SaaS is located.</td>
</tr>
<tr>
    <td><CopyableCode code="saaSData" /></td>
    <td><code>object</code></td>
    <td>SaaS details.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure Subscription containing the monitor resource.</td>
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
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User Info.</td>
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
    <td><CopyableCode code="accountCreationSource" /></td>
    <td><code>string</code></td>
    <td>Source of account creation. Known values are: "LIFTR" and "NEWRELIC".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Liftr resource category. Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>Liftr resource preference. The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Marketplace Subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>NewRelic Organization properties of the resource. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>MonitoringStatus of the resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="newRelicAccountProperties" /></td>
    <td><code>object</code></td>
    <td>MarketplaceSubscriptionStatus of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="orgCreationSource" /></td>
    <td><code>string</code></td>
    <td>Source of org creation. Known values are: "LIFTR" and "NEWRELIC".</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Plan details.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="saaSAzureSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Subscription where Marketplace SaaS is located.</td>
</tr>
<tr>
    <td><CopyableCode code="saaSData" /></td>
    <td><code>object</code></td>
    <td>SaaS details.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure Subscription containing the monitor resource.</td>
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
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User Info.</td>
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
    <td><a href="#list_app_services"><CopyableCode code="list_app_services" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the app service resources currently being monitored by the New Relic resource, helping you understand which app services are under monitoring.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties and configuration details of a specific New Relic monitor resource, providing insight into its setup and status.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a list of all New Relic monitor resources either a specific resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all New Relic monitor resources either within a specific subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new or updates an existing New Relic monitor resource in your Azure subscription. This sets up the integration between Azure and your New Relic account, enabling observability and monitoring of your Azure resources through New Relic.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing New Relic monitor resource from your Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new or updates an existing New Relic monitor resource in your Azure subscription. This sets up the integration between Azure and your New Relic account, enabling observability and monitoring of your Azure resources through New Relic.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-userEmail"><code>userEmail</code></a></td>
    <td></td>
    <td>Deletes an existing New Relic monitor resource from your Azure subscription, removing the integration and stopping the observability of your Azure resources through New Relic.</td>
</tr>
<tr>
    <td><a href="#list_hosts"><CopyableCode code="list_hosts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-userEmail"><code>userEmail</code></a></td>
    <td></td>
    <td>Lists all VM resources currently being monitored by the New Relic monitor resource, helping you manage observability.</td>
</tr>
<tr>
    <td><a href="#list_monitored_resources"><CopyableCode code="list_monitored_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Azure resources that are currently being monitored by the specified New Relic monitor resource, providing insight into the coverage of your observability setup.</td>
</tr>
<tr>
    <td><a href="#list_linked_resources"><CopyableCode code="list_linked_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Azure resources that are linked to the same New Relic organization as the specified monitor resource, helping you understand the scope of integration. Lists all Azure resources that are linked to the same New Relic organization as the specified monitor resource, helping you understand the scope of integration.</td>
</tr>
<tr>
    <td><a href="#get_metric_rules"><CopyableCode code="get_metric_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-userEmail"><code>userEmail</code></a></td>
    <td></td>
    <td>Retrieves the metric rules that are configured in the New Relic monitor resource.</td>
</tr>
<tr>
    <td><a href="#get_metric_status"><CopyableCode code="get_metric_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-userEmail"><code>userEmail</code></a></td>
    <td></td>
    <td>Retrieves the metric status that are configured in the New Relic monitor resource.</td>
</tr>
<tr>
    <td><a href="#switch_billing"><CopyableCode code="switch_billing" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-userEmail"><code>userEmail</code></a></td>
    <td></td>
    <td>Switches the billing for the New Relic Monitor resource to be billed by Azure Marketplace.</td>
</tr>
<tr>
    <td><a href="#refresh_ingestion_key"><CopyableCode code="refresh_ingestion_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes the ingestion key for all monitors linked to the same account associated to the underlying monitor.</td>
</tr>
<tr>
    <td><a href="#vm_host_payload"><CopyableCode code="vm_host_payload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the payload that needs to be passed in the request body for installing the New Relic agent on a VM, providing the necessary configuration details.</td>
</tr>
<tr>
    <td><a href="#latest_linked_saas"><CopyableCode code="latest_linked_saas" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the latest SaaS linked to the newrelic organization of the underlying monitor.</td>
</tr>
<tr>
    <td><a href="#link_saas"><CopyableCode code="link_saas" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Links a new SaaS to the newrelic organization of the underlying monitor. Links a new SaaS to the newrelic organization of the underlying monitor.</td>
</tr>
<tr>
    <td><a href="#resubscribe"><CopyableCode code="resubscribe" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resubscribes the New Relic Organization of the underline Monitor Resource to be billed by Azure Marketplace. Resubscribes the New Relic Organization of the underline Monitor Resource to be billed by Azure Marketplace.</td>
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
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Monitor resource name. Required.</td>
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
<tr id="parameter-userEmail">
    <td><CopyableCode code="userEmail" /></td>
    <td><code>string</code></td>
    <td>User Email. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_app_services"
    values={[
        { label: 'list_app_services', value: 'list_app_services' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_app_services">

Lists the app service resources currently being monitored by the New Relic resource, helping you understand which app services are under monitoring.

```sql
SELECT
agentStatus,
agentVersion,
azureResourceId
FROM azure_isv.newrelicobservability.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Retrieves the properties and configuration details of a specific New Relic monitor resource, providing insight into its setup and status.

```sql
SELECT
id,
name,
accountCreationSource,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionId,
marketplaceSubscriptionStatus,
monitoringStatus,
newRelicAccountProperties,
orgCreationSource,
planData,
provisioningState,
saaSAzureSubscriptionStatus,
saaSData,
subscriptionState,
systemData,
tags,
type,
userInfo
FROM azure_isv.newrelicobservability.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieves a list of all New Relic monitor resources either a specific resource group.

```sql
SELECT
id,
name,
accountCreationSource,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionId,
marketplaceSubscriptionStatus,
monitoringStatus,
newRelicAccountProperties,
orgCreationSource,
planData,
provisioningState,
saaSAzureSubscriptionStatus,
saaSData,
subscriptionState,
systemData,
tags,
type,
userInfo
FROM azure_isv.newrelicobservability.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all New Relic monitor resources either within a specific subscription.

```sql
SELECT
id,
name,
accountCreationSource,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionId,
marketplaceSubscriptionStatus,
monitoringStatus,
newRelicAccountProperties,
orgCreationSource,
planData,
provisioningState,
saaSAzureSubscriptionStatus,
saaSData,
subscriptionState,
systemData,
tags,
type,
userInfo
FROM azure_isv.newrelicobservability.monitors
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

Creates a new or updates an existing New Relic monitor resource in your Azure subscription. This sets up the integration between Azure and your New Relic account, enabling observability and monitoring of your Azure resources through New Relic.

```sql
INSERT INTO azure_isv.newrelicobservability.monitors (
tags,
location,
identity,
properties,
resource_group_name,
monitor_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
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
- name: monitors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the monitors resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the monitors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the monitors resource.
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
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        newRelicAccountProperties:
          userId: "{{ userId }}"
          accountInfo:
            accountId: "{{ accountId }}"
            ingestionKey: "{{ ingestionKey }}"
            region: "{{ region }}"
          organizationInfo:
            organizationId: "{{ organizationId }}"
          singleSignOnProperties:
            singleSignOnState: "{{ singleSignOnState }}"
            enterpriseAppId: "{{ enterpriseAppId }}"
            singleSignOnUrl: "{{ singleSignOnUrl }}"
            provisioningState: "{{ provisioningState }}"
        userInfo:
          firstName: "{{ firstName }}"
          lastName: "{{ lastName }}"
          emailAddress: "{{ emailAddress }}"
          phoneNumber: "{{ phoneNumber }}"
          country: "{{ country }}"
        planData:
          usageType: "{{ usageType }}"
          billingCycle: "{{ billingCycle }}"
          planDetails: "{{ planDetails }}"
          effectiveDate: "{{ effectiveDate }}"
        saaSData:
          saaSResourceId: "{{ saaSResourceId }}"
        orgCreationSource: "{{ orgCreationSource }}"
        accountCreationSource: "{{ accountCreationSource }}"
        subscriptionState: "{{ subscriptionState }}"
        saaSAzureSubscriptionStatus: "{{ saaSAzureSubscriptionStatus }}"
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

Updates an existing New Relic monitor resource from your Azure subscription.

```sql
UPDATE azure_isv.newrelicobservability.monitors
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
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

Creates a new or updates an existing New Relic monitor resource in your Azure subscription. This sets up the integration between Azure and your New Relic account, enabling observability and monitoring of your Azure resources through New Relic.

```sql
REPLACE azure_isv.newrelicobservability.monitors
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
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

Deletes an existing New Relic monitor resource from your Azure subscription, removing the integration and stopping the observability of your Azure resources through New Relic.

```sql
DELETE FROM azure_isv.newrelicobservability.monitors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND userEmail = '{{ userEmail }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_hosts"
    values={[
        { label: 'list_hosts', value: 'list_hosts' },
        { label: 'list_monitored_resources', value: 'list_monitored_resources' },
        { label: 'list_linked_resources', value: 'list_linked_resources' },
        { label: 'get_metric_rules', value: 'get_metric_rules' },
        { label: 'get_metric_status', value: 'get_metric_status' },
        { label: 'switch_billing', value: 'switch_billing' },
        { label: 'refresh_ingestion_key', value: 'refresh_ingestion_key' },
        { label: 'vm_host_payload', value: 'vm_host_payload' },
        { label: 'latest_linked_saas', value: 'latest_linked_saas' },
        { label: 'link_saas', value: 'link_saas' },
        { label: 'resubscribe', value: 'resubscribe' }
    ]}
>
<TabItem value="list_hosts">

Lists all VM resources currently being monitored by the New Relic monitor resource, helping you manage observability.

```sql
EXEC azure_isv.newrelicobservability.monitors.list_hosts 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vmIds": "{{ vmIds }}", 
"userEmail": "{{ userEmail }}"
}'
;
```
</TabItem>
<TabItem value="list_monitored_resources">

Lists all Azure resources that are currently being monitored by the specified New Relic monitor resource, providing insight into the coverage of your observability setup.

```sql
EXEC azure_isv.newrelicobservability.monitors.list_monitored_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_linked_resources">

Lists all Azure resources that are linked to the same New Relic organization as the specified monitor resource, helping you understand the scope of integration. Lists all Azure resources that are linked to the same New Relic organization as the specified monitor resource, helping you understand the scope of integration.

```sql
EXEC azure_isv.newrelicobservability.monitors.list_linked_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_metric_rules">

Retrieves the metric rules that are configured in the New Relic monitor resource.

```sql
EXEC azure_isv.newrelicobservability.monitors.get_metric_rules 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"userEmail": "{{ userEmail }}"
}'
;
```
</TabItem>
<TabItem value="get_metric_status">

Retrieves the metric status that are configured in the New Relic monitor resource.

```sql
EXEC azure_isv.newrelicobservability.monitors.get_metric_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"azureResourceIds": "{{ azureResourceIds }}", 
"userEmail": "{{ userEmail }}"
}'
;
```
</TabItem>
<TabItem value="switch_billing">

Switches the billing for the New Relic Monitor resource to be billed by Azure Marketplace.

```sql
EXEC azure_isv.newrelicobservability.monitors.switch_billing 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"azureResourceId": "{{ azureResourceId }}", 
"organizationId": "{{ organizationId }}", 
"planData": "{{ planData }}", 
"userEmail": "{{ userEmail }}"
}'
;
```
</TabItem>
<TabItem value="refresh_ingestion_key">

Refreshes the ingestion key for all monitors linked to the same account associated to the underlying monitor.

```sql
EXEC azure_isv.newrelicobservability.monitors.refresh_ingestion_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="vm_host_payload">

Returns the payload that needs to be passed in the request body for installing the New Relic agent on a VM, providing the necessary configuration details.

```sql
EXEC azure_isv.newrelicobservability.monitors.vm_host_payload 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="latest_linked_saas">

Returns the latest SaaS linked to the newrelic organization of the underlying monitor.

```sql
EXEC azure_isv.newrelicobservability.monitors.latest_linked_saas 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="link_saas">

Links a new SaaS to the newrelic organization of the underlying monitor. Links a new SaaS to the newrelic organization of the underlying monitor.

```sql
EXEC azure_isv.newrelicobservability.monitors.link_saas 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"saaSResourceId": "{{ saaSResourceId }}"
}'
;
```
</TabItem>
<TabItem value="resubscribe">

Resubscribes the New Relic Organization of the underline Monitor Resource to be billed by Azure Marketplace. Resubscribes the New Relic Organization of the underline Monitor Resource to be billed by Azure Marketplace.

```sql
EXEC azure_isv.newrelicobservability.monitors.resubscribe 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"planId": "{{ planId }}", 
"termId": "{{ termId }}", 
"subscriptionId": "{{ subscriptionId }}", 
"resourceGroup": "{{ resourceGroup }}", 
"organizationId": "{{ organizationId }}", 
"publisherId": "{{ publisherId }}", 
"offerId": "{{ offerId }}"
}'
;
```
</TabItem>
</Tabs>
