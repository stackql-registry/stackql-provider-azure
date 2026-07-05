--- 
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - eventgrid
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

Creates, updates, deletes, gets or lists a <code>topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="topics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid.topics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_event_types"
    values={[
        { label: 'list_event_types', value: 'list_event_types' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_event_types">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the event type.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the event type.</td>
</tr>
<tr>
    <td><CopyableCode code="isInDefaultSet" /></td>
    <td><code>boolean</code></td>
    <td>IsInDefaultSet flag of the event type.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaUrl" /></td>
    <td><code>string</code></td>
    <td>URL of the schema for this event type.</td>
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
    <td><CopyableCode code="dataResidencyBoundary" /></td>
    <td><code>string</code></td>
    <td>Data Residency Boundary of the resource. Known values are: "WithinGeopair" and "WithinRegion". (WithinGeopair, WithinRegion)</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Key encryption configuration properties of the topic resource. This is an optional property. When not specified, no key encryption is used.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type Information for the user topic. This information is provided by the publisher and can be used by the subscriber to view different types of events that are published.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchema" /></td>
    <td><code>string</code></td>
    <td>This determines the format that Event Grid should expect for incoming events published to the topic. Known values are: "EventGridSchema", "CustomEventSchema", and "CloudEventSchemaV1_0". (EventGridSchema, CustomEventSchema, CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchemaMapping" /></td>
    <td><code>object</code></td>
    <td>This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource. Known values are: "Azure" and "AzureArc". (Azure, AzureArc)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricResourceId" /></td>
    <td><code>string</code></td>
    <td>Metric resource id for the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this topic. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="platformCapabilities" /></td>
    <td><code>object</code></td>
    <td>Represents the platform capabilities of the resource, including Azure Confidential Compute related properties.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the topic. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku pricing tier for the topic.</td>
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
    <td><CopyableCode code="dataResidencyBoundary" /></td>
    <td><code>string</code></td>
    <td>Data Residency Boundary of the resource. Known values are: "WithinGeopair" and "WithinRegion". (WithinGeopair, WithinRegion)</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Key encryption configuration properties of the topic resource. This is an optional property. When not specified, no key encryption is used.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type Information for the user topic. This information is provided by the publisher and can be used by the subscriber to view different types of events that are published.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchema" /></td>
    <td><code>string</code></td>
    <td>This determines the format that Event Grid should expect for incoming events published to the topic. Known values are: "EventGridSchema", "CustomEventSchema", and "CloudEventSchemaV1_0". (EventGridSchema, CustomEventSchema, CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchemaMapping" /></td>
    <td><code>object</code></td>
    <td>This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource. Known values are: "Azure" and "AzureArc". (Azure, AzureArc)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricResourceId" /></td>
    <td><code>string</code></td>
    <td>Metric resource id for the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this topic. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="platformCapabilities" /></td>
    <td><code>object</code></td>
    <td>Represents the platform capabilities of the resource, including Azure Confidential Compute related properties.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the topic. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku pricing tier for the topic.</td>
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
    <td><CopyableCode code="dataResidencyBoundary" /></td>
    <td><code>string</code></td>
    <td>Data Residency Boundary of the resource. Known values are: "WithinGeopair" and "WithinRegion". (WithinGeopair, WithinRegion)</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Key encryption configuration properties of the topic resource. This is an optional property. When not specified, no key encryption is used.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type Information for the user topic. This information is provided by the publisher and can be used by the subscriber to view different types of events that are published.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchema" /></td>
    <td><code>string</code></td>
    <td>This determines the format that Event Grid should expect for incoming events published to the topic. Known values are: "EventGridSchema", "CustomEventSchema", and "CloudEventSchemaV1_0". (EventGridSchema, CustomEventSchema, CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchemaMapping" /></td>
    <td><code>object</code></td>
    <td>This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource. Known values are: "Azure" and "AzureArc". (Azure, AzureArc)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricResourceId" /></td>
    <td><code>string</code></td>
    <td>Metric resource id for the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this topic. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="platformCapabilities" /></td>
    <td><code>object</code></td>
    <td>Represents the platform capabilities of the resource, including Azure Confidential Compute related properties.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the topic. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku pricing tier for the topic.</td>
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
    <td><a href="#list_event_types"><CopyableCode code="list_event_types" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_namespace"><code>provider_namespace</code></a>, <a href="#parameter-resource_type_name"><code>resource_type_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List topic event types. List event types for a topic.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a topic. Get properties of a topic.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List topics under a resource group. List all the topics under a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List topics under an Azure subscription. List all the topics under an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a topic. Asynchronously creates a new topic with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a topic. Asynchronously updates a topic with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a topic. Asynchronously creates a new topic with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a topic. Delete existing topic.</td>
</tr>
<tr>
    <td><a href="#list_shared_access_keys"><CopyableCode code="list_shared_access_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List keys for a topic. List the two keys used to publish to a topic.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyName"><code>keyName</code></a></td>
    <td></td>
    <td>Regenerate key for a topic. Regenerate a shared access key for a topic.</td>
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
<tr id="parameter-provider_namespace">
    <td><CopyableCode code="provider_namespace" /></td>
    <td><code>string</code></td>
    <td>the provider namespace. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Name of the topic. Required.</td>
</tr>
<tr id="parameter-resource_type_name">
    <td><CopyableCode code="resource_type_name" /></td>
    <td><code>string</code></td>
    <td>Name of the topic type. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-topic_name">
    <td><CopyableCode code="topic_name" /></td>
    <td><code>string</code></td>
    <td>Name of the topic. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_event_types"
    values={[
        { label: 'list_event_types', value: 'list_event_types' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_event_types">

List topic event types. List event types for a topic.

```sql
SELECT
id,
name,
description,
displayName,
isInDefaultSet,
schemaUrl,
systemData,
type
FROM azure.eventgrid.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provider_namespace = '{{ provider_namespace }}' -- required
AND resource_type_name = '{{ resource_type_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a topic. Get properties of a topic.

```sql
SELECT
id,
name,
dataResidencyBoundary,
disableLocalAuth,
encryption,
endpoint,
eventTypeInfo,
extendedLocation,
identity,
inboundIpRules,
inputSchema,
inputSchemaMapping,
kind,
location,
metricResourceId,
minimumTlsVersionAllowed,
platformCapabilities,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
type
FROM azure.eventgrid.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List topics under a resource group. List all the topics under a resource group.

```sql
SELECT
id,
name,
dataResidencyBoundary,
disableLocalAuth,
encryption,
endpoint,
eventTypeInfo,
extendedLocation,
identity,
inboundIpRules,
inputSchema,
inputSchemaMapping,
kind,
location,
metricResourceId,
minimumTlsVersionAllowed,
platformCapabilities,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
type
FROM azure.eventgrid.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

List topics under an Azure subscription. List all the topics under an Azure subscription.

```sql
SELECT
id,
name,
dataResidencyBoundary,
disableLocalAuth,
encryption,
endpoint,
eventTypeInfo,
extendedLocation,
identity,
inboundIpRules,
inputSchema,
inputSchemaMapping,
kind,
location,
metricResourceId,
minimumTlsVersionAllowed,
platformCapabilities,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
type
FROM azure.eventgrid.topics
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create a topic. Asynchronously creates a new topic with the specified parameters.

```sql
INSERT INTO azure.eventgrid.topics (
tags,
location,
properties,
sku,
identity,
kind,
extendedLocation,
resource_group_name,
topic_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ kind }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ topic_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
identity,
kind,
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
- name: topics
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the topics resource.
    - name: topic_name
      value: "{{ topic_name }}"
      description: Required parameter for the topics resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the topics resource.
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
        Properties of the topic.
      value:
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
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
              groupIds:
                - "{{ groupIds }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        provisioningState: "{{ provisioningState }}"
        endpoint: "{{ endpoint }}"
        eventTypeInfo:
          kind: "{{ kind }}"
          inlineEventTypes: "{{ inlineEventTypes }}"
        minimumTlsVersionAllowed: "{{ minimumTlsVersionAllowed }}"
        inputSchema: "{{ inputSchema }}"
        inputSchemaMapping:
          inputSchemaMappingType: "{{ inputSchemaMappingType }}"
        metricResourceId: "{{ metricResourceId }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        inboundIpRules:
          - ipMask: "{{ ipMask }}"
            action: "{{ action }}"
        disableLocalAuth: {{ disableLocalAuth }}
        dataResidencyBoundary: "{{ dataResidencyBoundary }}"
        encryption:
          customerManagedKeyEncryption:
            - keyEncryptionKeyUrl: "{{ keyEncryptionKeyUrl }}"
              keyEncryptionKeyIdentity:
                type: "{{ type }}"
                userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
              keyEncryptionKeyStatus: "{{ keyEncryptionKeyStatus }}"
              keyEncryptionKeyStatusFriendlyDescription: "{{ keyEncryptionKeyStatusFriendlyDescription }}"
        platformCapabilities:
          confidentialCompute:
            mode: "{{ mode }}"
    - name: sku
      description: |
        The Sku pricing tier for the topic.
      value:
        name: "{{ name }}"
    - name: identity
      description: |
        Identity information for the resource.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of the resource. Known values are: "Azure" and "AzureArc".
      valid_values: ['Azure', 'AzureArc']
    - name: extendedLocation
      description: |
        Extended location of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Update a topic. Asynchronously updates a topic with the specified parameters.

```sql
UPDATE azure.eventgrid.topics
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
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

Create a topic. Asynchronously creates a new topic with the specified parameters.

```sql
REPLACE azure.eventgrid.topics
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
kind = '{{ kind }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
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

Delete a topic. Delete existing topic.

```sql
DELETE FROM azure.eventgrid.topics
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_shared_access_keys"
    values={[
        { label: 'list_shared_access_keys', value: 'list_shared_access_keys' },
        { label: 'regenerate_key', value: 'regenerate_key' }
    ]}
>
<TabItem value="list_shared_access_keys">

List keys for a topic. List the two keys used to publish to a topic.

```sql
EXEC azure.eventgrid.topics.list_shared_access_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerate key for a topic. Regenerate a shared access key for a topic.

```sql
EXEC azure.eventgrid.topics.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}"
}'
;
```
</TabItem>
</Tabs>
