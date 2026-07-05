--- 
title: api_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - api_collections
  - security
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

Creates, updates, deletes, gets or lists an <code>api_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="api_collections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.api_collections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_azure_api_management_service"
    values={[
        { label: 'get_by_azure_api_management_service', value: 'get_by_azure_api_management_service' },
        { label: 'list_by_azure_api_management_service', value: 'list_by_azure_api_management_service' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_by_azure_api_management_service">

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
    <td><CopyableCode code="baseUrl" /></td>
    <td><code>string</code></td>
    <td>The base URI for this API collection. All endpoints of this API collection extend this base URI.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveredVia" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the resource from where this API collection was discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints discovered in this API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpointsWithSensitiveDataExposed" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection which are exposing sensitive data in their requests and/or responses.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfExternalApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection for which API traffic from the internet was observed.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInactiveApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that have not received any API traffic in the last 30 days.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfUnauthenticatedApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that are unauthenticated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the API collection. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Failed", "Canceled", and "InProgress". (Succeeded, Creating, Updating, Deleting, Failed, Canceled, InProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="sensitivityLabel" /></td>
    <td><code>string</code></td>
    <td>The highest priority sensitivity label from Microsoft Purview in this API collection.</td>
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
<TabItem value="list_by_azure_api_management_service">

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
    <td><CopyableCode code="baseUrl" /></td>
    <td><code>string</code></td>
    <td>The base URI for this API collection. All endpoints of this API collection extend this base URI.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveredVia" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the resource from where this API collection was discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints discovered in this API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpointsWithSensitiveDataExposed" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection which are exposing sensitive data in their requests and/or responses.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfExternalApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection for which API traffic from the internet was observed.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInactiveApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that have not received any API traffic in the last 30 days.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfUnauthenticatedApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that are unauthenticated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the API collection. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Failed", "Canceled", and "InProgress". (Succeeded, Creating, Updating, Deleting, Failed, Canceled, InProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="sensitivityLabel" /></td>
    <td><code>string</code></td>
    <td>The highest priority sensitivity label from Microsoft Purview in this API collection.</td>
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
    <td><CopyableCode code="baseUrl" /></td>
    <td><code>string</code></td>
    <td>The base URI for this API collection. All endpoints of this API collection extend this base URI.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveredVia" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the resource from where this API collection was discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints discovered in this API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpointsWithSensitiveDataExposed" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection which are exposing sensitive data in their requests and/or responses.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfExternalApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection for which API traffic from the internet was observed.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInactiveApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that have not received any API traffic in the last 30 days.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfUnauthenticatedApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that are unauthenticated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the API collection. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Failed", "Canceled", and "InProgress". (Succeeded, Creating, Updating, Deleting, Failed, Canceled, InProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="sensitivityLabel" /></td>
    <td><code>string</code></td>
    <td>The highest priority sensitivity label from Microsoft Purview in this API collection.</td>
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
    <td><CopyableCode code="baseUrl" /></td>
    <td><code>string</code></td>
    <td>The base URI for this API collection. All endpoints of this API collection extend this base URI.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveredVia" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the resource from where this API collection was discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints discovered in this API collection.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfApiEndpointsWithSensitiveDataExposed" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection which are exposing sensitive data in their requests and/or responses.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfExternalApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection for which API traffic from the internet was observed.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInactiveApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that have not received any API traffic in the last 30 days.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfUnauthenticatedApiEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The number of API endpoints in this API collection that are unauthenticated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the API collection. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Failed", "Canceled", and "InProgress". (Succeeded, Creating, Updating, Deleting, Failed, Canceled, InProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="sensitivityLabel" /></td>
    <td><code>string</code></td>
    <td>The highest priority sensitivity label from Microsoft Purview in this API collection.</td>
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
    <td><a href="#get_by_azure_api_management_service"><CopyableCode code="get_by_azure_api_management_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an onboarded Azure API Management API. Gets an Azure API Management API if it has been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.</td>
</tr>
<tr>
    <td><a href="#list_by_azure_api_management_service"><CopyableCode code="list_by_azure_api_management_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of onboarded Azure API Management APIs. Gets a list of Azure API Management APIs that have been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of API collections within a resource group. Gets a list of API collections within a resource group that have been onboarded to Microsoft Defender for APIs.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of API collections within a subscription. Gets a list of API collections within a subscription that have been onboarded to Microsoft Defender for APIs.</td>
</tr>
<tr>
    <td><a href="#offboard_azure_api_management_api"><CopyableCode code="offboard_azure_api_management_api" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Offboard an Azure API Management API from Microsoft Defender for APIs. Offboard an Azure API Management API from Microsoft Defender for APIs. The system will stop monitoring the operations within the Azure API Management API for intrusive behaviors.</td>
</tr>
<tr>
    <td><a href="#onboard_azure_api_management_api"><CopyableCode code="onboard_azure_api_management_api" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Onboard an Azure API Management API to Microsoft Defender for APIs. Onboard an Azure API Management API to Microsoft Defender for APIs. The system will start monitoring the operations within the Azure Management API for intrusive behaviors and provide alerts for attacks that have been detected.</td>
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
<tr id="parameter-api_id">
    <td><CopyableCode code="api_id" /></td>
    <td><code>string</code></td>
    <td>API revision identifier. Must be unique in the API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
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
    defaultValue="get_by_azure_api_management_service"
    values={[
        { label: 'get_by_azure_api_management_service', value: 'get_by_azure_api_management_service' },
        { label: 'list_by_azure_api_management_service', value: 'list_by_azure_api_management_service' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_by_azure_api_management_service">

Gets an onboarded Azure API Management API. Gets an Azure API Management API if it has been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.

```sql
SELECT
id,
name,
baseUrl,
discoveredVia,
displayName,
numberOfApiEndpoints,
numberOfApiEndpointsWithSensitiveDataExposed,
numberOfExternalApiEndpoints,
numberOfInactiveApiEndpoints,
numberOfUnauthenticatedApiEndpoints,
provisioningState,
sensitivityLabel,
systemData,
type
FROM azure.security.api_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND api_id = '{{ api_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_azure_api_management_service">

Gets a list of onboarded Azure API Management APIs. Gets a list of Azure API Management APIs that have been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.

```sql
SELECT
id,
name,
baseUrl,
discoveredVia,
displayName,
numberOfApiEndpoints,
numberOfApiEndpointsWithSensitiveDataExposed,
numberOfExternalApiEndpoints,
numberOfInactiveApiEndpoints,
numberOfUnauthenticatedApiEndpoints,
provisioningState,
sensitivityLabel,
systemData,
type
FROM azure.security.api_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of API collections within a resource group. Gets a list of API collections within a resource group that have been onboarded to Microsoft Defender for APIs.

```sql
SELECT
id,
name,
baseUrl,
discoveredVia,
displayName,
numberOfApiEndpoints,
numberOfApiEndpointsWithSensitiveDataExposed,
numberOfExternalApiEndpoints,
numberOfInactiveApiEndpoints,
numberOfUnauthenticatedApiEndpoints,
provisioningState,
sensitivityLabel,
systemData,
type
FROM azure.security.api_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of API collections within a subscription. Gets a list of API collections within a subscription that have been onboarded to Microsoft Defender for APIs.

```sql
SELECT
id,
name,
baseUrl,
discoveredVia,
displayName,
numberOfApiEndpoints,
numberOfApiEndpointsWithSensitiveDataExposed,
numberOfExternalApiEndpoints,
numberOfInactiveApiEndpoints,
numberOfUnauthenticatedApiEndpoints,
provisioningState,
sensitivityLabel,
systemData,
type
FROM azure.security.api_collections
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="offboard_azure_api_management_api"
    values={[
        { label: 'offboard_azure_api_management_api', value: 'offboard_azure_api_management_api' }
    ]}
>
<TabItem value="offboard_azure_api_management_api">

Offboard an Azure API Management API from Microsoft Defender for APIs. Offboard an Azure API Management API from Microsoft Defender for APIs. The system will stop monitoring the operations within the Azure API Management API for intrusive behaviors.

```sql
DELETE FROM azure.security.api_collections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND api_id = '{{ api_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="onboard_azure_api_management_api"
    values={[
        { label: 'onboard_azure_api_management_api', value: 'onboard_azure_api_management_api' }
    ]}
>
<TabItem value="onboard_azure_api_management_api">

Onboard an Azure API Management API to Microsoft Defender for APIs. Onboard an Azure API Management API to Microsoft Defender for APIs. The system will start monitoring the operations within the Azure Management API for intrusive behaviors and provide alerts for attacks that have been detected.

```sql
EXEC azure.security.api_collections.onboard_azure_api_management_api 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@api_id='{{ api_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
