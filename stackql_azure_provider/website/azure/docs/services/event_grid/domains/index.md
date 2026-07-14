--- 
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domains" /></td></tr>
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
    <td><CopyableCode code="autoCreateTopicWithFirstSubscription" /></td>
    <td><code>boolean</code></td>
    <td>This Boolean is used to specify the creation mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource. In this context, creation of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true. When this property is null or set to true, Event Grid is responsible of automatically creating the domain topic when the first event subscription is created at the scope of the domain topic. If this property is set to false, then creating the first event subscription will require creating a domain topic by the user. The self-management mode can be used if the user wants full control of when the domain topic is created, while auto-managed mode provides the flexibility to perform less operations and manage fewer resources by the user. Also, note that in auto-managed creation mode, user is allowed to create the domain topic on demand if needed.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDeleteTopicWithLastSubscription" /></td>
    <td><code>boolean</code></td>
    <td>This Boolean is used to specify the deletion mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource. In this context, deletion of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true. When this property is set to true, Event Grid is responsible of automatically deleting the domain topic when the last event subscription at the scope of the domain topic is deleted. If this property is set to false, then the user needs to manually delete the domain topic when it is no longer needed (e.g., when last event subscription is deleted and the resource needs to be cleaned up). The self-management mode can be used if the user wants full control of when the domain topic needs to be deleted, while auto-managed mode provides the flexibility to perform less operations and manage fewer resources by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="dataResidencyBoundary" /></td>
    <td><code>string</code></td>
    <td>Data Residency Boundary of the resource. Known values are: "WithinGeopair" and "WithinRegion". (WithinGeopair, WithinRegion)</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the Event Grid Domain Resource which is used for publishing the events.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type Information for the domain. This information is provided by the publisher and can be used by the subscriber to view different types of events that are published.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Event Grid Domain resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchema" /></td>
    <td><code>string</code></td>
    <td>This determines the format that Event Grid should expect for incoming events published to the Event Grid Domain Resource. Known values are: "EventGridSchema", "CustomEventSchema", and "CloudEventSchemaV1_0". (EventGridSchema, CustomEventSchema, CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchemaMapping" /></td>
    <td><code>object</code></td>
    <td>Information about the InputSchemaMapping which specified the info about mapping event payload.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricResourceId" /></td>
    <td><code>string</code></td>
    <td>Metric resource id for the Event Grid Domain Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this domain. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Event Grid Domain Resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku pricing tier for the Event Grid Domain resource.</td>
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
    <td><CopyableCode code="autoCreateTopicWithFirstSubscription" /></td>
    <td><code>boolean</code></td>
    <td>This Boolean is used to specify the creation mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource. In this context, creation of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true. When this property is null or set to true, Event Grid is responsible of automatically creating the domain topic when the first event subscription is created at the scope of the domain topic. If this property is set to false, then creating the first event subscription will require creating a domain topic by the user. The self-management mode can be used if the user wants full control of when the domain topic is created, while auto-managed mode provides the flexibility to perform less operations and manage fewer resources by the user. Also, note that in auto-managed creation mode, user is allowed to create the domain topic on demand if needed.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDeleteTopicWithLastSubscription" /></td>
    <td><code>boolean</code></td>
    <td>This Boolean is used to specify the deletion mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource. In this context, deletion of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true. When this property is set to true, Event Grid is responsible of automatically deleting the domain topic when the last event subscription at the scope of the domain topic is deleted. If this property is set to false, then the user needs to manually delete the domain topic when it is no longer needed (e.g., when last event subscription is deleted and the resource needs to be cleaned up). The self-management mode can be used if the user wants full control of when the domain topic needs to be deleted, while auto-managed mode provides the flexibility to perform less operations and manage fewer resources by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="dataResidencyBoundary" /></td>
    <td><code>string</code></td>
    <td>Data Residency Boundary of the resource. Known values are: "WithinGeopair" and "WithinRegion". (WithinGeopair, WithinRegion)</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the Event Grid Domain Resource which is used for publishing the events.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type Information for the domain. This information is provided by the publisher and can be used by the subscriber to view different types of events that are published.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Event Grid Domain resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchema" /></td>
    <td><code>string</code></td>
    <td>This determines the format that Event Grid should expect for incoming events published to the Event Grid Domain Resource. Known values are: "EventGridSchema", "CustomEventSchema", and "CloudEventSchemaV1_0". (EventGridSchema, CustomEventSchema, CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchemaMapping" /></td>
    <td><code>object</code></td>
    <td>Information about the InputSchemaMapping which specified the info about mapping event payload.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricResourceId" /></td>
    <td><code>string</code></td>
    <td>Metric resource id for the Event Grid Domain Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this domain. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Event Grid Domain Resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku pricing tier for the Event Grid Domain resource.</td>
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
    <td><CopyableCode code="autoCreateTopicWithFirstSubscription" /></td>
    <td><code>boolean</code></td>
    <td>This Boolean is used to specify the creation mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource. In this context, creation of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true. When this property is null or set to true, Event Grid is responsible of automatically creating the domain topic when the first event subscription is created at the scope of the domain topic. If this property is set to false, then creating the first event subscription will require creating a domain topic by the user. The self-management mode can be used if the user wants full control of when the domain topic is created, while auto-managed mode provides the flexibility to perform less operations and manage fewer resources by the user. Also, note that in auto-managed creation mode, user is allowed to create the domain topic on demand if needed.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDeleteTopicWithLastSubscription" /></td>
    <td><code>boolean</code></td>
    <td>This Boolean is used to specify the deletion mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource. In this context, deletion of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true. When this property is set to true, Event Grid is responsible of automatically deleting the domain topic when the last event subscription at the scope of the domain topic is deleted. If this property is set to false, then the user needs to manually delete the domain topic when it is no longer needed (e.g., when last event subscription is deleted and the resource needs to be cleaned up). The self-management mode can be used if the user wants full control of when the domain topic needs to be deleted, while auto-managed mode provides the flexibility to perform less operations and manage fewer resources by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="dataResidencyBoundary" /></td>
    <td><code>string</code></td>
    <td>Data Residency Boundary of the resource. Known values are: "WithinGeopair" and "WithinRegion". (WithinGeopair, WithinRegion)</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the Event Grid Domain Resource which is used for publishing the events.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type Information for the domain. This information is provided by the publisher and can be used by the subscriber to view different types of events that are published.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Event Grid Domain resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchema" /></td>
    <td><code>string</code></td>
    <td>This determines the format that Event Grid should expect for incoming events published to the Event Grid Domain Resource. Known values are: "EventGridSchema", "CustomEventSchema", and "CloudEventSchemaV1_0". (EventGridSchema, CustomEventSchema, CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="inputSchemaMapping" /></td>
    <td><code>object</code></td>
    <td>Information about the InputSchemaMapping which specified the info about mapping event payload.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricResourceId" /></td>
    <td><code>string</code></td>
    <td>Metric resource id for the Event Grid Domain Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this domain. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Event Grid Domain Resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku pricing tier for the Event Grid Domain resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a domain. Get properties of a domain.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List domains under a resource group. List all the domains under a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List domains under an Azure subscription. List all the domains under an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a domain. Asynchronously creates or updates a new domain with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a domain. Asynchronously updates a domain with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a domain. Asynchronously creates or updates a new domain with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a domain. Delete existing domain.</td>
</tr>
<tr>
    <td><a href="#list_shared_access_keys"><CopyableCode code="list_shared_access_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List keys for a domain. List the two keys used to publish to a domain.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyName"><code>keyName</code></a></td>
    <td></td>
    <td>Regenerate key for a domain. Regenerate a shared access key for a domain.</td>
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
<tr id="parameter-domain_name">
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>Name of the domain. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a domain. Get properties of a domain.

```sql
SELECT
id,
name,
autoCreateTopicWithFirstSubscription,
autoDeleteTopicWithLastSubscription,
dataResidencyBoundary,
disableLocalAuth,
endpoint,
eventTypeInfo,
identity,
inboundIpRules,
inputSchema,
inputSchemaMapping,
location,
metricResourceId,
minimumTlsVersionAllowed,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
type
FROM azure.event_grid.domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND domain_name = '{{ domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List domains under a resource group. List all the domains under a resource group.

```sql
SELECT
id,
name,
autoCreateTopicWithFirstSubscription,
autoDeleteTopicWithLastSubscription,
dataResidencyBoundary,
disableLocalAuth,
endpoint,
eventTypeInfo,
identity,
inboundIpRules,
inputSchema,
inputSchemaMapping,
location,
metricResourceId,
minimumTlsVersionAllowed,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
type
FROM azure.event_grid.domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

List domains under an Azure subscription. List all the domains under an Azure subscription.

```sql
SELECT
id,
name,
autoCreateTopicWithFirstSubscription,
autoDeleteTopicWithLastSubscription,
dataResidencyBoundary,
disableLocalAuth,
endpoint,
eventTypeInfo,
identity,
inboundIpRules,
inputSchema,
inputSchemaMapping,
location,
metricResourceId,
minimumTlsVersionAllowed,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
type
FROM azure.event_grid.domains
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

Create or update a domain. Asynchronously creates or updates a new domain with the specified parameters.

```sql
INSERT INTO azure.event_grid.domains (
tags,
location,
properties,
sku,
identity,
resource_group_name,
domain_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ domain_name }}',
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
- name: domains
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the domains resource.
    - name: domain_name
      value: "{{ domain_name }}"
      description: Required parameter for the domains resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the domains resource.
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
        Properties of the Event Grid Domain resource.
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
        minimumTlsVersionAllowed: "{{ minimumTlsVersionAllowed }}"
        endpoint: "{{ endpoint }}"
        inputSchema: "{{ inputSchema }}"
        eventTypeInfo:
          kind: "{{ kind }}"
          inlineEventTypes: "{{ inlineEventTypes }}"
        inputSchemaMapping:
          inputSchemaMappingType: "{{ inputSchemaMappingType }}"
        metricResourceId: "{{ metricResourceId }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        inboundIpRules:
          - ipMask: "{{ ipMask }}"
            action: "{{ action }}"
        disableLocalAuth: {{ disableLocalAuth }}
        autoCreateTopicWithFirstSubscription: {{ autoCreateTopicWithFirstSubscription }}
        autoDeleteTopicWithLastSubscription: {{ autoDeleteTopicWithLastSubscription }}
        dataResidencyBoundary: "{{ dataResidencyBoundary }}"
    - name: sku
      description: |
        The Sku pricing tier for the Event Grid Domain resource.
      value:
        name: "{{ name }}"
    - name: identity
      description: |
        Identity information for the Event Grid Domain resource.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
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

Update a domain. Asynchronously updates a domain with the specified parameters.

```sql
UPDATE azure.event_grid.domains
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
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

Create or update a domain. Asynchronously creates or updates a new domain with the specified parameters.

```sql
REPLACE azure.event_grid.domains
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Delete a domain. Delete existing domain.

```sql
DELETE FROM azure.event_grid.domains
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
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

List keys for a domain. List the two keys used to publish to a domain.

```sql
EXEC azure.event_grid.domains.list_shared_access_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerate key for a domain. Regenerate a shared access key for a domain.

```sql
EXEC azure.event_grid.domains.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}"
}'
;
```
</TabItem>
</Tabs>
