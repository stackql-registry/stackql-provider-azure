--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - search
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
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
    <td><CopyableCode code="authOptions" /></td>
    <td><code>object</code></td>
    <td>Defines the options for how the data plane API of a search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="computeType" /></td>
    <td><code>string</code></td>
    <td>Configure this property to support the search service using either the Default Compute or Azure Confidential Compute. Known values are: "Default" and "Confidential". (Default, Confidential)</td>
</tr>
<tr>
    <td><CopyableCode code="dataExfiltrationProtections" /></td>
    <td><code>array</code></td>
    <td>A list of data exfiltration scenarios that are explicitly disallowed for the search service. Currently, the only supported value is 'All' to disable all possible data export scenarios with more fine grained controls planned for the future.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, calls to the search service will not be permitted to utilize API keys for authentication. This cannot be set to true if 'dataPlaneAuthOptions' are defined.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>A system generated property representing the service's etag that can be for optimistic concurrency control during updates.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionWithCmk" /></td>
    <td><code>object</code></td>
    <td>Specifies any policy regarding encryption of resources (such as indexes) using customer manager keys within a search service.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingMode" /></td>
    <td><code>string</code></td>
    <td>Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'Default' or 'HighDensity'. For all other SKUs, this value must be 'Default'. Known values are: "Default" and "HighDensity". (Default, HighDensity)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="knowledgeRetrieval" /></td>
    <td><code>string</code></td>
    <td>Specifies the billing plan for agentic retrieval on the Azure AI Search service. This configuration is only available for certain pricing tiers in certain regions. Known values are: "free" and "standard". (free, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleSet" /></td>
    <td><code>object</code></td>
    <td>Network specific rules that determine how the Azure AI Search service may be reached.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionCount" /></td>
    <td><code>integer</code></td>
    <td>The number of partitions in the dedicated search service; if specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only valid for standard SKUs. For 'standard3' services with hostingMode set to 'highDensity', the allowed values are between 1 and 3.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections to the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the last provisioning operation performed on the search service. Provisioning is an intermediate state that occurs while service capacity is being established. After capacity is set up, provisioningState changes to either 'Succeeded' or 'Failed'. Client applications can poll provisioning status (the recommended polling interval is from 30 seconds to one minute) by using the Get Search Service operation to see when an operation is completed. If you are using the free service, this value tends to come back as 'Succeeded' directly in the call to Create search service. This is because the free service uses capacity that is already set up. Known values are: "succeeded", "provisioning", and "failed". (succeeded, provisioning, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This value can be set to 'Enabled' to avoid breaking changes on existing customer resources and templates. If set to 'Disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas in the dedicated search service. If specified, it must be a value between 1 and 12 inclusive for standard SKUs or between 1 and 3 inclusive for basic SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="semanticSearch" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability and billing plan for semantic search on the Azure AI Search service. This configuration is only available for certain pricing tiers in certain regions. Known values are: "disabled", "free", and "standard". (disabled, free, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceUpgradedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the search service was last upgraded. This field will be null until the service gets upgraded for the first time.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources managed by the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the search service. Possible values include: 'running': The search service is running and no provisioning operations are underway. 'provisioning': The search service is being provisioned or scaled up or down. 'deleting': The search service is being deleted. 'degraded': The search service is degraded. This can occur when the underlying search units are not healthy. The search service is most likely operational, but performance might be slow and some requests might be dropped. 'disabled': The search service is disabled. In this state, the service will reject all API requests. 'error': The search service is in an error state. 'stopped': The search service is in a subscription that's disabled. If your service is in the degraded, disabled, or error states, it means the Azure AI Search team is actively investigating the underlying issue. Dedicated services in these states are still chargeable based on the number of search units provisioned. Known values are: "running", "provisioning", "deleting", "degraded", "disabled", "error", and "stopped". (running, provisioning, deleting, degraded, disabled, error, stopped)</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>The details of the search service status.</td>
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
    <td><CopyableCode code="upgradeAvailable" /></td>
    <td><code>string</code></td>
    <td>Indicates if the search service has an upgrade available. Known values are: "notAvailable" and "available". (notAvailable, available)</td>
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
    <td>A message that explains why the name is invalid and provides resource naming requirements. Available only if 'Invalid' is returned in the 'reason' property.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether the name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason why the name is not available. 'Invalid' indicates the name provided does not match the naming requirements (incorrect length, unsupported characters, etc.). 'AlreadyExists' indicates that the name is already in use and is therefore unavailable. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
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
    <td><CopyableCode code="authOptions" /></td>
    <td><code>object</code></td>
    <td>Defines the options for how the data plane API of a search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="computeType" /></td>
    <td><code>string</code></td>
    <td>Configure this property to support the search service using either the Default Compute or Azure Confidential Compute. Known values are: "Default" and "Confidential". (Default, Confidential)</td>
</tr>
<tr>
    <td><CopyableCode code="dataExfiltrationProtections" /></td>
    <td><code>array</code></td>
    <td>A list of data exfiltration scenarios that are explicitly disallowed for the search service. Currently, the only supported value is 'All' to disable all possible data export scenarios with more fine grained controls planned for the future.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, calls to the search service will not be permitted to utilize API keys for authentication. This cannot be set to true if 'dataPlaneAuthOptions' are defined.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>A system generated property representing the service's etag that can be for optimistic concurrency control during updates.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionWithCmk" /></td>
    <td><code>object</code></td>
    <td>Specifies any policy regarding encryption of resources (such as indexes) using customer manager keys within a search service.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingMode" /></td>
    <td><code>string</code></td>
    <td>Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'Default' or 'HighDensity'. For all other SKUs, this value must be 'Default'. Known values are: "Default" and "HighDensity". (Default, HighDensity)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="knowledgeRetrieval" /></td>
    <td><code>string</code></td>
    <td>Specifies the billing plan for agentic retrieval on the Azure AI Search service. This configuration is only available for certain pricing tiers in certain regions. Known values are: "free" and "standard". (free, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleSet" /></td>
    <td><code>object</code></td>
    <td>Network specific rules that determine how the Azure AI Search service may be reached.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionCount" /></td>
    <td><code>integer</code></td>
    <td>The number of partitions in the dedicated search service; if specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only valid for standard SKUs. For 'standard3' services with hostingMode set to 'highDensity', the allowed values are between 1 and 3.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections to the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the last provisioning operation performed on the search service. Provisioning is an intermediate state that occurs while service capacity is being established. After capacity is set up, provisioningState changes to either 'Succeeded' or 'Failed'. Client applications can poll provisioning status (the recommended polling interval is from 30 seconds to one minute) by using the Get Search Service operation to see when an operation is completed. If you are using the free service, this value tends to come back as 'Succeeded' directly in the call to Create search service. This is because the free service uses capacity that is already set up. Known values are: "succeeded", "provisioning", and "failed". (succeeded, provisioning, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This value can be set to 'Enabled' to avoid breaking changes on existing customer resources and templates. If set to 'Disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas in the dedicated search service. If specified, it must be a value between 1 and 12 inclusive for standard SKUs or between 1 and 3 inclusive for basic SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="semanticSearch" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability and billing plan for semantic search on the Azure AI Search service. This configuration is only available for certain pricing tiers in certain regions. Known values are: "disabled", "free", and "standard". (disabled, free, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceUpgradedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the search service was last upgraded. This field will be null until the service gets upgraded for the first time.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources managed by the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the search service. Possible values include: 'running': The search service is running and no provisioning operations are underway. 'provisioning': The search service is being provisioned or scaled up or down. 'deleting': The search service is being deleted. 'degraded': The search service is degraded. This can occur when the underlying search units are not healthy. The search service is most likely operational, but performance might be slow and some requests might be dropped. 'disabled': The search service is disabled. In this state, the service will reject all API requests. 'error': The search service is in an error state. 'stopped': The search service is in a subscription that's disabled. If your service is in the degraded, disabled, or error states, it means the Azure AI Search team is actively investigating the underlying issue. Dedicated services in these states are still chargeable based on the number of search units provisioned. Known values are: "running", "provisioning", "deleting", "degraded", "disabled", "error", and "stopped". (running, provisioning, deleting, degraded, disabled, error, stopped)</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>The details of the search service status.</td>
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
    <td><CopyableCode code="upgradeAvailable" /></td>
    <td><code>string</code></td>
    <td>Indicates if the search service has an upgrade available. Known values are: "notAvailable" and "available". (notAvailable, available)</td>
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
    <td><CopyableCode code="authOptions" /></td>
    <td><code>object</code></td>
    <td>Defines the options for how the data plane API of a search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="computeType" /></td>
    <td><code>string</code></td>
    <td>Configure this property to support the search service using either the Default Compute or Azure Confidential Compute. Known values are: "Default" and "Confidential". (Default, Confidential)</td>
</tr>
<tr>
    <td><CopyableCode code="dataExfiltrationProtections" /></td>
    <td><code>array</code></td>
    <td>A list of data exfiltration scenarios that are explicitly disallowed for the search service. Currently, the only supported value is 'All' to disable all possible data export scenarios with more fine grained controls planned for the future.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, calls to the search service will not be permitted to utilize API keys for authentication. This cannot be set to true if 'dataPlaneAuthOptions' are defined.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>A system generated property representing the service's etag that can be for optimistic concurrency control during updates.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionWithCmk" /></td>
    <td><code>object</code></td>
    <td>Specifies any policy regarding encryption of resources (such as indexes) using customer manager keys within a search service.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingMode" /></td>
    <td><code>string</code></td>
    <td>Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'Default' or 'HighDensity'. For all other SKUs, this value must be 'Default'. Known values are: "Default" and "HighDensity". (Default, HighDensity)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="knowledgeRetrieval" /></td>
    <td><code>string</code></td>
    <td>Specifies the billing plan for agentic retrieval on the Azure AI Search service. This configuration is only available for certain pricing tiers in certain regions. Known values are: "free" and "standard". (free, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleSet" /></td>
    <td><code>object</code></td>
    <td>Network specific rules that determine how the Azure AI Search service may be reached.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionCount" /></td>
    <td><code>integer</code></td>
    <td>The number of partitions in the dedicated search service; if specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only valid for standard SKUs. For 'standard3' services with hostingMode set to 'highDensity', the allowed values are between 1 and 3.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections to the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the last provisioning operation performed on the search service. Provisioning is an intermediate state that occurs while service capacity is being established. After capacity is set up, provisioningState changes to either 'Succeeded' or 'Failed'. Client applications can poll provisioning status (the recommended polling interval is from 30 seconds to one minute) by using the Get Search Service operation to see when an operation is completed. If you are using the free service, this value tends to come back as 'Succeeded' directly in the call to Create search service. This is because the free service uses capacity that is already set up. Known values are: "succeeded", "provisioning", and "failed". (succeeded, provisioning, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This value can be set to 'Enabled' to avoid breaking changes on existing customer resources and templates. If set to 'Disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas in the dedicated search service. If specified, it must be a value between 1 and 12 inclusive for standard SKUs or between 1 and 3 inclusive for basic SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="semanticSearch" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability and billing plan for semantic search on the Azure AI Search service. This configuration is only available for certain pricing tiers in certain regions. Known values are: "disabled", "free", and "standard". (disabled, free, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceUpgradedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the search service was last upgraded. This field will be null until the service gets upgraded for the first time.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources managed by the Azure AI Search service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the search service. Possible values include: 'running': The search service is running and no provisioning operations are underway. 'provisioning': The search service is being provisioned or scaled up or down. 'deleting': The search service is being deleted. 'degraded': The search service is degraded. This can occur when the underlying search units are not healthy. The search service is most likely operational, but performance might be slow and some requests might be dropped. 'disabled': The search service is disabled. In this state, the service will reject all API requests. 'error': The search service is in an error state. 'stopped': The search service is in a subscription that's disabled. If your service is in the degraded, disabled, or error states, it means the Azure AI Search team is actively investigating the underlying issue. Dedicated services in these states are still chargeable based on the number of search units provisioned. Known values are: "running", "provisioning", "deleting", "degraded", "disabled", "error", and "stopped". (running, provisioning, deleting, degraded, disabled, error, stopped)</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>The details of the search service status.</td>
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
    <td><CopyableCode code="upgradeAvailable" /></td>
    <td><code>string</code></td>
    <td>Indicates if the search service has an upgrade available. Known values are: "notAvailable" and "available". (notAvailable, available)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the search service with the given name in the given resource group.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks whether or not the given search service name is available for use. Search service names must be globally unique since they are part of the service URI (https://.search.windows.net).</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all search services in the given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all search services in the given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing search service in the given resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a search service in the given resource group, along with its associated resources. Returns 200 (OK) on successful deletion, or 204 (No Content) if the service is not found.</td>
</tr>
<tr>
    <td><a href="#upgrade"><CopyableCode code="upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrades the Azure AI Search service to the latest version available.</td>
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
<tr id="parameter-search_service_name">
    <td><CopyableCode code="search_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure AI Search service associated with the specified resource group. Required.</td>
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
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the search service with the given name in the given resource group.

```sql
SELECT
id,
name,
authOptions,
computeType,
dataExfiltrationProtections,
disableLocalAuth,
eTag,
encryptionWithCmk,
endpoint,
hostingMode,
identity,
knowledgeRetrieval,
location,
networkRuleSet,
partitionCount,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
replicaCount,
semanticSearch,
serviceUpgradedAt,
sharedPrivateLinkResources,
sku,
status,
statusDetails,
systemData,
tags,
type,
upgradeAvailable
FROM azure.search.services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND search_service_name = '{{ search_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks whether or not the given search service name is available for use. Search service names must be globally unique since they are part of the service URI (https://.search.windows.net).

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.search.services
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of all search services in the given resource group.

```sql
SELECT
id,
name,
authOptions,
computeType,
dataExfiltrationProtections,
disableLocalAuth,
eTag,
encryptionWithCmk,
endpoint,
hostingMode,
identity,
knowledgeRetrieval,
location,
networkRuleSet,
partitionCount,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
replicaCount,
semanticSearch,
serviceUpgradedAt,
sharedPrivateLinkResources,
sku,
status,
statusDetails,
systemData,
tags,
type,
upgradeAvailable
FROM azure.search.services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of all search services in the given subscription.

```sql
SELECT
id,
name,
authOptions,
computeType,
dataExfiltrationProtections,
disableLocalAuth,
eTag,
encryptionWithCmk,
endpoint,
hostingMode,
identity,
knowledgeRetrieval,
location,
networkRuleSet,
partitionCount,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
replicaCount,
semanticSearch,
serviceUpgradedAt,
sharedPrivateLinkResources,
sku,
status,
statusDetails,
systemData,
tags,
type,
upgradeAvailable
FROM azure.search.services
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

Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values.

```sql
INSERT INTO azure.search.services (
tags,
location,
properties,
sku,
identity,
resource_group_name,
search_service_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ search_service_name }}',
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
- name: services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the services resource.
    - name: search_service_name
      value: "{{ search_service_name }}"
      description: Required parameter for the services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the services resource.
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
        Properties of the search service.
      value:
        replicaCount: {{ replicaCount }}
        partitionCount: {{ partitionCount }}
        endpoint: "{{ endpoint }}"
        hostingMode: "{{ hostingMode }}"
        computeType: "{{ computeType }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        status: "{{ status }}"
        statusDetails: "{{ statusDetails }}"
        provisioningState: "{{ provisioningState }}"
        networkRuleSet:
          ipRules:
            - value: "{{ value }}"
          bypass: "{{ bypass }}"
        dataExfiltrationProtections:
          - "{{ dataExfiltrationProtections }}"
        encryptionWithCmk:
          enforcement: "{{ enforcement }}"
          encryptionComplianceStatus: "{{ encryptionComplianceStatus }}"
          serviceLevelEncryptionKey:
            keyVaultKeyName: "{{ keyVaultKeyName }}"
            keyVaultKeyVersion: "{{ keyVaultKeyVersion }}"
            keyVaultUri: "{{ keyVaultUri }}"
            identity:
              @odata:
                type: "{{ type }}"
            accessCredentials:
              applicationId: "{{ applicationId }}"
              applicationSecret: "{{ applicationSecret }}"
        disableLocalAuth: {{ disableLocalAuth }}
        authOptions:
          apiKeyOnly: "{{ apiKeyOnly }}"
          aadOrApiKey:
            aadAuthFailureMode: "{{ aadAuthFailureMode }}"
        semanticSearch: "{{ semanticSearch }}"
        knowledgeRetrieval: "{{ knowledgeRetrieval }}"
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
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              groupId: "{{ groupId }}"
              provisioningState: "{{ provisioningState }}"
        sharedPrivateLinkResources:
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
              privateLinkResourceId: "{{ privateLinkResourceId }}"
              groupId: "{{ groupId }}"
              requestMessage: "{{ requestMessage }}"
              resourceRegion: "{{ resourceRegion }}"
              status: "{{ status }}"
              provisioningState: "{{ provisioningState }}"
        eTag: "{{ eTag }}"
        upgradeAvailable: "{{ upgradeAvailable }}"
        serviceUpgradedAt: "{{ serviceUpgradedAt }}"
    - name: sku
      description: |
        The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.
      value:
        name: "{{ name }}"
    - name: identity
      description: |
        The identity of the resource.
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

Updates an existing search service in the given resource group.

```sql
UPDATE azure.search.services
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND search_service_name = '{{ search_service_name }}' --required
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

Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values.

```sql
REPLACE azure.search.services
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND search_service_name = '{{ search_service_name }}' --required
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

Deletes a search service in the given resource group, along with its associated resources. Returns 200 (OK) on successful deletion, or 204 (No Content) if the service is not found.

```sql
DELETE FROM azure.search.services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND search_service_name = '{{ search_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upgrade"
    values={[
        { label: 'upgrade', value: 'upgrade' }
    ]}
>
<TabItem value="upgrade">

Upgrades the Azure AI Search service to the latest version available.

```sql
EXEC azure.search.services.upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
