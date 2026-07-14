--- 
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - event_hub
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hub.namespaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_keys">

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
    <td><CopyableCode code="aliasPrimaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Primary connection string of the alias if GEO DR is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="aliasSecondaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Secondary connection string of the alias if GEO DR is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="keyName" /></td>
    <td><code>string</code></td>
    <td>A string that describes the AuthorizationRule.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Primary connection string of the created namespace AuthorizationRule.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryKey" /></td>
    <td><code>string</code></td>
    <td>A base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Secondary connection string of the created namespace AuthorizationRule.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryKey" /></td>
    <td><code>string</code></td>
    <td>A base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
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
    <td><CopyableCode code="alternateName" /></td>
    <td><code>string</code></td>
    <td>Alternate name specified when alias and namespace names are same.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterArmId" /></td>
    <td><code>string</code></td>
    <td>Cluster ARM ID of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the Namespace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This property disables SAS authentication for the Event Hubs namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Properties of BYOK Encryption description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Properties of BYOK Identity description.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoInflateEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether AutoInflate is enabled for eventhub namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether Kafka is enabled for eventhub namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumThroughputUnits" /></td>
    <td><code>integer</code></td>
    <td>Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true).</td>
</tr>
<tr>
    <td><CopyableCode code="metricId" /></td>
    <td><code>string</code></td>
    <td>Identifier for Azure Insights metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimum TLS version for the cluster to support, e.g. '1.2'. Known values are: "1.0", "1.1", and "1.2".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint you can use to perform Service Bus operations.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Properties of sku resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
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
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the Namespace was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.</td>
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
    <td><CopyableCode code="alternateName" /></td>
    <td><code>string</code></td>
    <td>Alternate name specified when alias and namespace names are same.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterArmId" /></td>
    <td><code>string</code></td>
    <td>Cluster ARM ID of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the Namespace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This property disables SAS authentication for the Event Hubs namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Properties of BYOK Encryption description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Properties of BYOK Identity description.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoInflateEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether AutoInflate is enabled for eventhub namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether Kafka is enabled for eventhub namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumThroughputUnits" /></td>
    <td><code>integer</code></td>
    <td>Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true).</td>
</tr>
<tr>
    <td><CopyableCode code="metricId" /></td>
    <td><code>string</code></td>
    <td>Identifier for Azure Insights metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimum TLS version for the cluster to support, e.g. '1.2'. Known values are: "1.0", "1.1", and "1.2".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint you can use to perform Service Bus operations.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Properties of sku resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
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
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the Namespace was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>The detailed info regarding the reason associated with the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Value indicating Namespace is availability, true if the Namespace is available; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for unavailability of a Namespace. Known values are: "None", "InvalidName", "SubscriptionIsDisabled", "NameInUse", "NameInLockdown", and "TooManyNamespaceInCurrentSubscription".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="alternateName" /></td>
    <td><code>string</code></td>
    <td>Alternate name specified when alias and namespace names are same.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterArmId" /></td>
    <td><code>string</code></td>
    <td>Cluster ARM ID of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the Namespace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This property disables SAS authentication for the Event Hubs namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Properties of BYOK Encryption description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Properties of BYOK Identity description.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoInflateEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether AutoInflate is enabled for eventhub namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether Kafka is enabled for eventhub namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumThroughputUnits" /></td>
    <td><code>integer</code></td>
    <td>Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true).</td>
</tr>
<tr>
    <td><CopyableCode code="metricId" /></td>
    <td><code>string</code></td>
    <td>Identifier for Azure Insights metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimum TLS version for the cluster to support, e.g. '1.2'. Known values are: "1.0", "1.1", and "1.2".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint you can use to perform Service Bus operations.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Properties of sku resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
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
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the Namespace was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.</td>
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
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the primary and secondary connection strings for the Namespace.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the description of the specified namespace.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the available Namespaces within a resource group.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check the give Namespace name availability.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the available Namespaces within a subscription, irrespective of the resource groups.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing namespace. This operation also removes all associated resources under the namespace.</td>
</tr>
<tr>
    <td><a href="#list_network_rule_set"><CopyableCode code="list_network_rule_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets NetworkRuleSet for a Namespace.</td>
</tr>
<tr>
    <td><a href="#list_authorization_rules"><CopyableCode code="list_authorization_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of authorization rules for a Namespace.</td>
</tr>
<tr>
    <td><a href="#get_network_rule_set"><CopyableCode code="get_network_rule_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets NetworkRuleSet for a Namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update_network_rule_set"><CopyableCode code="create_or_update_network_rule_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update NetworkRuleSet for a Namespace.</td>
</tr>
<tr>
    <td><a href="#get_authorization_rule"><CopyableCode code="get_authorization_rule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an AuthorizationRule for a Namespace by rule name.</td>
</tr>
<tr>
    <td><a href="#create_or_update_authorization_rule"><CopyableCode code="create_or_update_authorization_rule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an AuthorizationRule for a Namespace.</td>
</tr>
<tr>
    <td><a href="#delete_authorization_rule"><CopyableCode code="delete_authorization_rule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an AuthorizationRule for a Namespace.</td>
</tr>
<tr>
    <td><a href="#regenerate_keys"><CopyableCode code="regenerate_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyType"><code>keyType</code></a></td>
    <td></td>
    <td>Regenerates the primary or secondary connection strings for the specified Namespace.</td>
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
    <td>The authorization rule name. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The Namespace name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group within the azure subscription. Required.</td>
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
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_keys">

Gets the primary and secondary connection strings for the Namespace.

```sql
SELECT
aliasPrimaryConnectionString,
aliasSecondaryConnectionString,
keyName,
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.event_hub.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND authorization_rule_name = '{{ authorization_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the description of the specified namespace.

```sql
SELECT
id,
name,
alternateName,
clusterArmId,
createdAt,
disableLocalAuth,
encryption,
identity,
isAutoInflateEnabled,
kafkaEnabled,
location,
maximumThroughputUnits,
metricId,
minimumTlsVersion,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
serviceBusEndpoint,
sku,
status,
systemData,
tags,
type,
updatedAt,
zoneRedundant
FROM azure.event_hub.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the available Namespaces within a resource group.

```sql
SELECT
id,
name,
alternateName,
clusterArmId,
createdAt,
disableLocalAuth,
encryption,
identity,
isAutoInflateEnabled,
kafkaEnabled,
location,
maximumThroughputUnits,
metricId,
minimumTlsVersion,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
serviceBusEndpoint,
sku,
status,
systemData,
tags,
type,
updatedAt,
zoneRedundant
FROM azure.event_hub.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Check the give Namespace name availability.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.event_hub.namespaces
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the available Namespaces within a subscription, irrespective of the resource groups.

```sql
SELECT
id,
name,
alternateName,
clusterArmId,
createdAt,
disableLocalAuth,
encryption,
identity,
isAutoInflateEnabled,
kafkaEnabled,
location,
maximumThroughputUnits,
metricId,
minimumTlsVersion,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
serviceBusEndpoint,
sku,
status,
systemData,
tags,
type,
updatedAt,
zoneRedundant
FROM azure.event_hub.namespaces
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

Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.

```sql
INSERT INTO azure.event_hub.namespaces (
location,
tags,
sku,
identity,
properties,
resource_group_name,
namespace_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: namespaces
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the namespaces resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the namespaces resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the namespaces resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: sku
      description: |
        Properties of sku resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Properties of BYOK Identity description.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        minimumTlsVersion: "{{ minimumTlsVersion }}"
        clusterArmId: "{{ clusterArmId }}"
        isAutoInflateEnabled: {{ isAutoInflateEnabled }}
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        maximumThroughputUnits: {{ maximumThroughputUnits }}
        kafkaEnabled: {{ kafkaEnabled }}
        zoneRedundant: {{ zoneRedundant }}
        encryption:
          keyVaultProperties:
            - keyName: "{{ keyName }}"
              keyVaultUri: "{{ keyVaultUri }}"
              keyVersion: "{{ keyVersion }}"
              identity:
                userAssignedIdentity: "{{ userAssignedIdentity }}"
          keySource: "{{ keySource }}"
          requireInfrastructureEncryption: {{ requireInfrastructureEncryption }}
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
              provisioningState: "{{ provisioningState }}"
        disableLocalAuth: {{ disableLocalAuth }}
        alternateName: "{{ alternateName }}"
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

Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.

```sql
UPDATE azure.event_hub.namespaces
SET 
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.

```sql
REPLACE azure.event_hub.namespaces
SET 
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Deletes an existing namespace. This operation also removes all associated resources under the namespace.

```sql
DELETE FROM azure.event_hub.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_network_rule_set"
    values={[
        { label: 'list_network_rule_set', value: 'list_network_rule_set' },
        { label: 'list_authorization_rules', value: 'list_authorization_rules' },
        { label: 'get_network_rule_set', value: 'get_network_rule_set' },
        { label: 'create_or_update_network_rule_set', value: 'create_or_update_network_rule_set' },
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'create_or_update_authorization_rule', value: 'create_or_update_authorization_rule' },
        { label: 'delete_authorization_rule', value: 'delete_authorization_rule' },
        { label: 'regenerate_keys', value: 'regenerate_keys' }
    ]}
>
<TabItem value="list_network_rule_set">

Gets NetworkRuleSet for a Namespace.

```sql
EXEC azure.event_hub.namespaces.list_network_rule_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_authorization_rules">

Gets a list of authorization rules for a Namespace.

```sql
EXEC azure.event_hub.namespaces.list_authorization_rules 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_network_rule_set">

Gets NetworkRuleSet for a Namespace.

```sql
EXEC azure.event_hub.namespaces.get_network_rule_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_network_rule_set">

Create or update NetworkRuleSet for a Namespace.

```sql
EXEC azure.event_hub.namespaces.create_or_update_network_rule_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_authorization_rule">

Gets an AuthorizationRule for a Namespace by rule name.

```sql
EXEC azure.event_hub.namespaces.get_authorization_rule 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_authorization_rule">

Creates or updates an AuthorizationRule for a Namespace.

```sql
EXEC azure.event_hub.namespaces.create_or_update_authorization_rule 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_authorization_rule">

Deletes an AuthorizationRule for a Namespace.

```sql
EXEC azure.event_hub.namespaces.delete_authorization_rule 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_keys">

Regenerates the primary or secondary connection strings for the specified Namespace.

```sql
EXEC azure.event_hub.namespaces.regenerate_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyType": "{{ keyType }}", 
"key": "{{ key }}"
}'
;
```
</TabItem>
</Tabs>
