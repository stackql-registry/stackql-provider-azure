--- 
title: static_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites
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

Creates, updates, deletes, gets or lists a <code>static_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="static_sites" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.static_sites" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_build_database_connection"
    values={[
        { label: 'get_build_database_connection', value: 'get_build_database_connection' },
        { label: 'get_user_provided_function_app_for_static_site_build', value: 'get_user_provided_function_app_for_static_site_build' },
        { label: 'get_linked_backend_for_build', value: 'get_linked_backend_for_build' },
        { label: 'list_static_site_build_functions', value: 'list_static_site_build_functions' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get_database_connection', value: 'get_database_connection' },
        { label: 'get_user_provided_function_app_for_static_site', value: 'get_user_provided_function_app_for_static_site' },
        { label: 'get_basic_auth', value: 'get_basic_auth' },
        { label: 'get_static_site_custom_domain', value: 'get_static_site_custom_domain' },
        { label: 'get_linked_backend', value: 'get_linked_backend' },
        { label: 'list_static_site_functions', value: 'list_static_site_functions' },
        { label: 'get_static_sites_by_resource_group', value: 'get_static_sites_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_build_database_connection">

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
    <td><CopyableCode code="configurationFiles" /></td>
    <td><code>array</code></td>
    <td>A list of configuration files associated with this database connection.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionIdentity" /></td>
    <td><code>string</code></td>
    <td>If present, the identity is used in conjunction with connection string to connect to the database. Use of the system-assigned managed identity is indicated with the string 'SystemAssigned', while use of a user-assigned managed identity is indicated with the resource id of the managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionString" /></td>
    <td><code>string</code></td>
    <td>The connection string to use to connect to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region of the database resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the database. Required.</td>
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
<TabItem value="get_user_provided_function_app_for_static_site_build">

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
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time on which the function app was registered with the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppRegion" /></td>
    <td><code>string</code></td>
    <td>The region of the function app registered with the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the function app registered with the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_linked_backend_for_build">

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
    <td><CopyableCode code="backendResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the backend linked to the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time on which the backend was linked to the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the linking process.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region of the backend linked to the static site.</td>
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
<TabItem value="list_static_site_build_functions">

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
    <td><CopyableCode code="functionName" /></td>
    <td><code>string</code></td>
    <td>The name for the function.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerType" /></td>
    <td><code>string</code></td>
    <td>The trigger type of the function. Known values are: "HttpTrigger" and "Unknown". (HttpTrigger, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_private_endpoint_connection">

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
    <td><CopyableCode code="ipAddresses" /></td>
    <td><code>array</code></td>
    <td>Private IPAddresses mapped to the remote private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>PrivateEndpoint of a remote private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>The state of a private link connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>:vartype provisioning_state: str</td>
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
<TabItem value="get_database_connection">

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
    <td><CopyableCode code="configurationFiles" /></td>
    <td><code>array</code></td>
    <td>A list of configuration files associated with this database connection.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionIdentity" /></td>
    <td><code>string</code></td>
    <td>If present, the identity is used in conjunction with connection string to connect to the database. Use of the system-assigned managed identity is indicated with the string 'SystemAssigned', while use of a user-assigned managed identity is indicated with the resource id of the managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionString" /></td>
    <td><code>string</code></td>
    <td>The connection string to use to connect to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region of the database resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the database. Required.</td>
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
<TabItem value="get_user_provided_function_app_for_static_site">

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
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time on which the function app was registered with the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppRegion" /></td>
    <td><code>string</code></td>
    <td>The region of the function app registered with the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the function app registered with the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_basic_auth">

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
    <td><CopyableCode code="applicableEnvironmentsMode" /></td>
    <td><code>string</code></td>
    <td>State indicating if basic auth is enabled and for what environments it is active. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environments" /></td>
    <td><code>array</code></td>
    <td>The list of enabled environments for Basic Auth if ApplicableEnvironmentsMode is set to SpecifiedEnvironments.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>The password for basic auth.</td>
</tr>
<tr>
    <td><CopyableCode code="secretState" /></td>
    <td><code>string</code></td>
    <td>State indicating if basic auth has a secret and what type it is.</td>
</tr>
<tr>
    <td><CopyableCode code="secretUrl" /></td>
    <td><code>string</code></td>
    <td>Url to the secret in Key Vault.</td>
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
<TabItem value="get_static_site_custom_domain">

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
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time on which the custom domain was created for the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="domainName" /></td>
    <td><code>string</code></td>
    <td>The domain name for the static site custom domain.</td>
</tr>
<tr>
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>:vartype error_message: str</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the custom domain. Known values are: "RetrievingValidationToken", "Validating", "Adding", "Ready", "Failed", "Deleting", and "Unhealthy". (RetrievingValidationToken, Validating, Adding, Ready, Failed, Deleting, Unhealthy)</td>
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
<tr>
    <td><CopyableCode code="validationToken" /></td>
    <td><code>string</code></td>
    <td>The TXT record validation token.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_linked_backend">

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
    <td><CopyableCode code="backendResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the backend linked to the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time on which the backend was linked to the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the linking process.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region of the backend linked to the static site.</td>
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
<TabItem value="list_static_site_functions">

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
    <td><CopyableCode code="functionName" /></td>
    <td><code>string</code></td>
    <td>The name for the function.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerType" /></td>
    <td><code>string</code></td>
    <td>The trigger type of the function. Known values are: "HttpTrigger" and "Unknown". (HttpTrigger, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_static_sites_by_resource_group">

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
    <td><CopyableCode code="allowConfigFileUpdates" /></td>
    <td><code>boolean</code></td>
    <td>false if config file is locked for this static web app; otherwise, true.</td>
</tr>
<tr>
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>The target branch in the repository.</td>
</tr>
<tr>
    <td><CopyableCode code="buildProperties" /></td>
    <td><code>object</code></td>
    <td>Build properties to configure on the repository.</td>
</tr>
<tr>
    <td><CopyableCode code="contentDistributionEndpoint" /></td>
    <td><code>string</code></td>
    <td>The content distribution endpoint for the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomains" /></td>
    <td><code>array</code></td>
    <td>The custom domains associated with this static site.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseConnections" /></td>
    <td><code>array</code></td>
    <td>Database connections for the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultHostname" /></td>
    <td><code>string</code></td>
    <td>The default autogenerated hostname for the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="enterpriseGradeCdnStatus" /></td>
    <td><code>string</code></td>
    <td>State indicating the status of the enterprise grade CDN serving traffic to the static web app. Known values are: "Enabled", "Enabling", "Disabled", and "Disabling". (Enabled, Enabling, Disabled, Disabling)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReferenceIdentity" /></td>
    <td><code>string</code></td>
    <td>Identity to use for Key Vault Reference authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedBackends" /></td>
    <td><code>array</code></td>
    <td>Backends linked to the static side.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>The provider that submitted the last deployment to the primary environment of the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>State indicating whether public traffic are allowed or not for a static web app. Allowed Values: 'Enabled', 'Disabled' or an empty string.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryToken" /></td>
    <td><code>string</code></td>
    <td>A user's github repository token. This is used to setup the Github Actions workflow file and API secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryUrl" /></td>
    <td><code>string</code></td>
    <td>URL for the repository of the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Description of a SKU for a scalable resource.</td>
</tr>
<tr>
    <td><CopyableCode code="stagingEnvironmentPolicy" /></td>
    <td><code>string</code></td>
    <td>State indicating whether staging environments are allowed or not allowed for a static web app. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
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
    <td><CopyableCode code="templateProperties" /></td>
    <td><code>object</code></td>
    <td>Template options for generating a new repository.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userProvidedFunctionApps" /></td>
    <td><code>array</code></td>
    <td>User provided function apps registered with the static site.</td>
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
    <td><CopyableCode code="allowConfigFileUpdates" /></td>
    <td><code>boolean</code></td>
    <td>false if config file is locked for this static web app; otherwise, true.</td>
</tr>
<tr>
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>The target branch in the repository.</td>
</tr>
<tr>
    <td><CopyableCode code="buildProperties" /></td>
    <td><code>object</code></td>
    <td>Build properties to configure on the repository.</td>
</tr>
<tr>
    <td><CopyableCode code="contentDistributionEndpoint" /></td>
    <td><code>string</code></td>
    <td>The content distribution endpoint for the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomains" /></td>
    <td><code>array</code></td>
    <td>The custom domains associated with this static site.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseConnections" /></td>
    <td><code>array</code></td>
    <td>Database connections for the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultHostname" /></td>
    <td><code>string</code></td>
    <td>The default autogenerated hostname for the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="enterpriseGradeCdnStatus" /></td>
    <td><code>string</code></td>
    <td>State indicating the status of the enterprise grade CDN serving traffic to the static web app. Known values are: "Enabled", "Enabling", "Disabled", and "Disabling". (Enabled, Enabling, Disabled, Disabling)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReferenceIdentity" /></td>
    <td><code>string</code></td>
    <td>Identity to use for Key Vault Reference authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedBackends" /></td>
    <td><code>array</code></td>
    <td>Backends linked to the static side.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>The provider that submitted the last deployment to the primary environment of the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>State indicating whether public traffic are allowed or not for a static web app. Allowed Values: 'Enabled', 'Disabled' or an empty string.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryToken" /></td>
    <td><code>string</code></td>
    <td>A user's github repository token. This is used to setup the Github Actions workflow file and API secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryUrl" /></td>
    <td><code>string</code></td>
    <td>URL for the repository of the static site.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Description of a SKU for a scalable resource.</td>
</tr>
<tr>
    <td><CopyableCode code="stagingEnvironmentPolicy" /></td>
    <td><code>string</code></td>
    <td>State indicating whether staging environments are allowed or not allowed for a static web app. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
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
    <td><CopyableCode code="templateProperties" /></td>
    <td><code>object</code></td>
    <td>Template options for generating a new repository.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userProvidedFunctionApps" /></td>
    <td><code>array</code></td>
    <td>User provided function apps registered with the static site.</td>
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
    <td><a href="#get_build_database_connection"><CopyableCode code="get_build_database_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns overview of a database connection for a static site build by name. Returns overview of a database connection for a static site build by name.</td>
</tr>
<tr>
    <td><a href="#get_user_provided_function_app_for_static_site_build"><CopyableCode code="get_user_provided_function_app_for_static_site_build" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-function_app_name"><code>function_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the user provided function app registered with a static site build. Description for Gets the details of the user provided function app registered with a static site build.</td>
</tr>
<tr>
    <td><a href="#get_linked_backend_for_build"><CopyableCode code="get_linked_backend_for_build" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the details of a linked backend linked to a static site build by name. Returns the details of a linked backend linked to a static site build by name.</td>
</tr>
<tr>
    <td><a href="#list_static_site_build_functions"><CopyableCode code="list_static_site_build_functions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the functions of a particular static site build. Description for Gets the functions of a particular static site build.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection"><CopyableCode code="get_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a private endpoint connection. Description for Gets a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get_database_connection"><CopyableCode code="get_database_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns overview of a database connection for a static site by name. Returns overview of a database connection for a static site by name.</td>
</tr>
<tr>
    <td><a href="#get_user_provided_function_app_for_static_site"><CopyableCode code="get_user_provided_function_app_for_static_site" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_app_name"><code>function_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the user provided function app registered with a static site. Description for Gets the details of the user provided function app registered with a static site.</td>
</tr>
<tr>
    <td><a href="#get_basic_auth"><CopyableCode code="get_basic_auth" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-basic_auth_name"><code>basic_auth_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the basic auth properties for a static site. Description for Gets the basic auth properties for a static site.</td>
</tr>
<tr>
    <td><a href="#get_static_site_custom_domain"><CopyableCode code="get_static_site_custom_domain" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing custom domain for a particular static site. Description for Gets an existing custom domain for a particular static site.</td>
</tr>
<tr>
    <td><a href="#get_linked_backend"><CopyableCode code="get_linked_backend" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the details of a linked backend linked to a static site by name. Returns the details of a linked backend linked to a static site by name.</td>
</tr>
<tr>
    <td><a href="#list_static_site_functions"><CopyableCode code="list_static_site_functions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the functions of a static site. Description for Gets the functions of a static site.</td>
</tr>
<tr>
    <td><a href="#get_static_sites_by_resource_group"><CopyableCode code="get_static_sites_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all static sites in the specified resource group. Description for Gets all static sites in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Static Sites for a subscription. Description for Get all Static Sites for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update_static_site"><CopyableCode code="create_or_update_static_site" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new static site in an existing resource group, or updates an existing static site. Description for Creates a new static site in an existing resource group, or updates an existing static site.</td>
</tr>
<tr>
    <td><a href="#update_static_site"><CopyableCode code="update_static_site" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new static site in an existing resource group, or updates an existing static site. Description for Creates a new static site in an existing resource group, or updates an existing static site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_static_site"><CopyableCode code="create_or_update_static_site" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new static site in an existing resource group, or updates an existing static site. Description for Creates a new static site in an existing resource group, or updates an existing static site.</td>
</tr>
<tr>
    <td><a href="#detach_user_provided_function_app_from_static_site_build"><CopyableCode code="detach_user_provided_function_app_from_static_site_build" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-function_app_name"><code>function_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Detach the user provided function app from the static site build. Description for Detach the user provided function app from the static site build.</td>
</tr>
<tr>
    <td><a href="#unlink_backend_from_build"><CopyableCode code="unlink_backend_from_build" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-isCleaningAuthConfig"><code>isCleaningAuthConfig</code></a></td>
    <td>Unlink a backend from a static site build. Unlink a backend from a static site build.</td>
</tr>
<tr>
    <td><a href="#detach_user_provided_function_app_from_static_site"><CopyableCode code="detach_user_provided_function_app_from_static_site" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_app_name"><code>function_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Detach the user provided function app from the static site. Description for Detach the user provided function app from the static site.</td>
</tr>
<tr>
    <td><a href="#unlink_backend"><CopyableCode code="unlink_backend" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-isCleaningAuthConfig"><code>isCleaningAuthConfig</code></a></td>
    <td>Unlink a backend from a static site. Unlink a backend from a static site.</td>
</tr>
<tr>
    <td><a href="#delete_static_site"><CopyableCode code="delete_static_site" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a static site. Description for Deletes a static site.</td>
</tr>
<tr>
    <td><a href="#list_static_site_users"><CopyableCode code="list_static_site_users" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-authprovider"><code>authprovider</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of users of a static site. Description for Gets the list of users of a static site.</td>
</tr>
<tr>
    <td><a href="#list_static_site_app_settings"><CopyableCode code="list_static_site_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the application settings of a static site. Description for Gets the application settings of a static site.</td>
</tr>
<tr>
    <td><a href="#list_static_site_configured_roles"><CopyableCode code="list_static_site_configured_roles" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the roles configured for the static site. Description for Lists the roles configured for the static site.</td>
</tr>
<tr>
    <td><a href="#list_static_site_function_app_settings"><CopyableCode code="list_static_site_function_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the application settings of a static site. Description for Gets the application settings of a static site.</td>
</tr>
<tr>
    <td><a href="#list_static_site_secrets"><CopyableCode code="list_static_site_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the secrets for an existing static site. Description for Lists the secrets for an existing static site.</td>
</tr>
<tr>
    <td><a href="#list_static_site_build_app_settings"><CopyableCode code="list_static_site_build_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the application settings of a static site build. Description for Gets the application settings of a static site build.</td>
</tr>
<tr>
    <td><a href="#list_static_site_build_function_app_settings"><CopyableCode code="list_static_site_build_function_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the application settings of a static site build. Description for Gets the application settings of a static site build.</td>
</tr>
<tr>
    <td><a href="#list_basic_auth"><CopyableCode code="list_basic_auth" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the basic auth properties for a static site as a collection. Description for Gets the basic auth properties for a static site as a collection.</td>
</tr>
<tr>
    <td><a href="#list_static_site_custom_domains"><CopyableCode code="list_static_site_custom_domains" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all static site custom domains for a particular static site. Description for Gets all static site custom domains for a particular static site.</td>
</tr>
<tr>
    <td><a href="#approve_or_reject_private_endpoint_connection"><CopyableCode code="approve_or_reject_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#delete_private_endpoint_connection"><CopyableCode code="delete_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a private endpoint connection. Description for Deletes a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection_list"><CopyableCode code="get_private_endpoint_connection_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of private endpoint connections associated with a static site. Description for Gets the list of private endpoint connections associated with a static site.</td>
</tr>
<tr>
    <td><a href="#get_static_site"><CopyableCode code="get_static_site" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a static site. Description for Gets the details of a static site.</td>
</tr>
<tr>
    <td><a href="#get_private_link_resources"><CopyableCode code="get_private_link_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the private link resources. Description for Gets the private link resources.</td>
</tr>
<tr>
    <td><a href="#get_database_connections_with_details"><CopyableCode code="get_database_connections_with_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns details of database connections for a static site. Returns details of database connections for a static site.</td>
</tr>
<tr>
    <td><a href="#get_static_site_build"><CopyableCode code="get_static_site_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a static site build. Description for Gets the details of a static site build.</td>
</tr>
<tr>
    <td><a href="#delete_static_site_build"><CopyableCode code="delete_static_site_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a static site build. Description for Deletes a static site build.</td>
</tr>
<tr>
    <td><a href="#get_static_site_builds"><CopyableCode code="get_static_site_builds" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all static site builds for a particular static site. Description for Gets all static site builds for a particular static site.</td>
</tr>
<tr>
    <td><a href="#get_build_database_connections_with_details"><CopyableCode code="get_build_database_connections_with_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns details of database connections for a static site build. Returns details of database connections for a static site build.</td>
</tr>
<tr>
    <td><a href="#create_or_update_build_database_connection"><CopyableCode code="create_or_update_build_database_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a database connection for a static site build. Description for Create or update a database connection for a static site build.</td>
</tr>
<tr>
    <td><a href="#update_build_database_connection"><CopyableCode code="update_build_database_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a database connection for a static site build. Description for Create or update a database connection for a static site build.</td>
</tr>
<tr>
    <td><a href="#delete_build_database_connection"><CopyableCode code="delete_build_database_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a database connection for a static site build. Delete a database connection for a static site build.</td>
</tr>
<tr>
    <td><a href="#get_build_database_connections"><CopyableCode code="get_build_database_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns overviews of database connections for a static site build. Returns overviews of database connections for a static site build.</td>
</tr>
<tr>
    <td><a href="#get_build_database_connection_with_details"><CopyableCode code="get_build_database_connection_with_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns details of a database connection for a static site build by name. Returns details of a database connection for a static site build by name.</td>
</tr>
<tr>
    <td><a href="#create_or_update_database_connection"><CopyableCode code="create_or_update_database_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a database connection for a static site. Description for Create or update a database connection for a static site.</td>
</tr>
<tr>
    <td><a href="#update_database_connection"><CopyableCode code="update_database_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a database connection for a static site. Description for Create or update a database connection for a static site.</td>
</tr>
<tr>
    <td><a href="#delete_database_connection"><CopyableCode code="delete_database_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a database connection for a static site. Delete a database connection for a static site.</td>
</tr>
<tr>
    <td><a href="#get_database_connections"><CopyableCode code="get_database_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns overviews of database connections for a static site. Returns overviews of database connections for a static site.</td>
</tr>
<tr>
    <td><a href="#get_database_connection_with_details"><CopyableCode code="get_database_connection_with_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-database_connection_name"><code>database_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns details of a database connection for a static site by name. Returns details of a database connection for a static site by name.</td>
</tr>
<tr>
    <td><a href="#register_user_provided_function_app_with_static_site_build"><CopyableCode code="register_user_provided_function_app_with_static_site_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-function_app_name"><code>function_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-isForced"><code>isForced</code></a></td>
    <td>Register a user provided function app with a static site build. Description for Register a user provided function app with a static site build.</td>
</tr>
<tr>
    <td><a href="#get_user_provided_function_apps_for_static_site_build"><CopyableCode code="get_user_provided_function_apps_for_static_site_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the user provided function apps registered with a static site build. Description for Gets the details of the user provided function apps registered with a static site build.</td>
</tr>
<tr>
    <td><a href="#register_user_provided_function_app_with_static_site"><CopyableCode code="register_user_provided_function_app_with_static_site" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_app_name"><code>function_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-isForced"><code>isForced</code></a></td>
    <td>Register a user provided function app with a static site. Description for Register a user provided function app with a static site.</td>
</tr>
<tr>
    <td><a href="#get_user_provided_function_apps_for_static_site"><CopyableCode code="get_user_provided_function_apps_for_static_site" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the user provided function apps registered with a static site. Description for Gets the details of the user provided function apps registered with a static site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_basic_auth"><CopyableCode code="create_or_update_basic_auth" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-basic_auth_name"><code>basic_auth_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds or updates basic auth for a static site. Description for Adds or updates basic auth for a static site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_static_site_custom_domain"><CopyableCode code="create_or_update_static_site_custom_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new static site custom domain in an existing resource group and static site. Description for Creates a new static site custom domain in an existing resource group and static site.</td>
</tr>
<tr>
    <td><a href="#delete_static_site_custom_domain"><CopyableCode code="delete_static_site_custom_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a custom domain. Description for Deletes a custom domain.</td>
</tr>
<tr>
    <td><a href="#link_backend"><CopyableCode code="link_backend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Link backend to a static site. Link backend to a static site.</td>
</tr>
<tr>
    <td><a href="#get_linked_backends"><CopyableCode code="get_linked_backends" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns details of all backends linked to a static site. Returns details of all backends linked to a static site.</td>
</tr>
<tr>
    <td><a href="#link_backend_to_build"><CopyableCode code="link_backend_to_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Link backend to a static site build. Link backend to a static site build.</td>
</tr>
<tr>
    <td><a href="#get_linked_backends_for_build"><CopyableCode code="get_linked_backends_for_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns details of all backends linked to a static site build. Returns details of all backends linked to a static site build.</td>
</tr>
<tr>
    <td><a href="#delete_static_site_user"><CopyableCode code="delete_static_site_user" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-authprovider"><code>authprovider</code></a>, <a href="#parameter-userid"><code>userid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the user entry from the static site. Description for Deletes the user entry from the static site.</td>
</tr>
<tr>
    <td><a href="#update_static_site_user"><CopyableCode code="update_static_site_user" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-authprovider"><code>authprovider</code></a>, <a href="#parameter-userid"><code>userid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a user entry with the listed roles. Description for Updates a user entry with the listed roles.</td>
</tr>
<tr>
    <td><a href="#create_or_update_static_site_app_settings"><CopyableCode code="create_or_update_static_site_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the app settings of a static site. Description for Creates or updates the app settings of a static site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_static_site_function_app_settings"><CopyableCode code="create_or_update_static_site_function_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the function app settings of a static site. Description for Creates or updates the function app settings of a static site.</td>
</tr>
<tr>
    <td><a href="#create_user_roles_invitation_link"><CopyableCode code="create_user_roles_invitation_link" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an invitation link for a user with the role. Description for Creates an invitation link for a user with the role.</td>
</tr>
<tr>
    <td><a href="#detach_static_site"><CopyableCode code="detach_static_site" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Detaches a static site. Description for Detaches a static site.</td>
</tr>
<tr>
    <td><a href="#reset_static_site_api_key"><CopyableCode code="reset_static_site_api_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets the api key for an existing static site. Description for Resets the api key for an existing static site.</td>
</tr>
<tr>
    <td><a href="#create_zip_deployment_for_static_site"><CopyableCode code="create_zip_deployment_for_static_site" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deploys zipped content to a static site. Description for Deploys zipped content to a static site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_static_site_build_app_settings"><CopyableCode code="create_or_update_static_site_build_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the app settings of a static site build. Description for Creates or updates the app settings of a static site build.</td>
</tr>
<tr>
    <td><a href="#create_or_update_static_site_build_function_app_settings"><CopyableCode code="create_or_update_static_site_build_function_app_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the function app settings of a static site build. Description for Creates or updates the function app settings of a static site build.</td>
</tr>
<tr>
    <td><a href="#create_zip_deployment_for_static_site_build"><CopyableCode code="create_zip_deployment_for_static_site_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deploys zipped content to a specific environment of a static site. Description for Deploys zipped content to a specific environment of a static site.</td>
</tr>
<tr>
    <td><a href="#validate_custom_domain_can_be_added_to_static_site"><CopyableCode code="validate_custom_domain_can_be_added_to_static_site" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates a particular custom domain can be added to a static site. Description for Validates a particular custom domain can be added to a static site.</td>
</tr>
<tr>
    <td><a href="#validate_backend"><CopyableCode code="validate_backend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates that a backend can be linked to a static site. Validates that a backend can be linked to a static site.</td>
</tr>
<tr>
    <td><a href="#validate_backend_for_build"><CopyableCode code="validate_backend_for_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-linked_backend_name"><code>linked_backend_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates that a backend can be linked to a static site build. Validates that a backend can be linked to a static site build.</td>
</tr>
<tr>
    <td><a href="#preview_workflow"><CopyableCode code="preview_workflow" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates a preview workflow file for the static site. Description for Generates a preview workflow file for the static site.</td>
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
<tr id="parameter-authprovider">
    <td><CopyableCode code="authprovider" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-basic_auth_name">
    <td><CopyableCode code="basic_auth_name" /></td>
    <td><code>string</code></td>
    <td>name of the basic auth entry. "default" Required.</td>
</tr>
<tr id="parameter-database_connection_name">
    <td><CopyableCode code="database_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name of the database connection. Required.</td>
</tr>
<tr id="parameter-domain_name">
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>The custom domain name. Required.</td>
</tr>
<tr id="parameter-environment_name">
    <td><CopyableCode code="environment_name" /></td>
    <td><code>string</code></td>
    <td>The stage site identifier. Required.</td>
</tr>
<tr id="parameter-function_app_name">
    <td><CopyableCode code="function_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the function app registered with the static site. Required.</td>
</tr>
<tr id="parameter-linked_backend_name">
    <td><CopyableCode code="linked_backend_name" /></td>
    <td><code>string</code></td>
    <td>Name of the linked backend that should be retrieved. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the static site. Required.</td>
</tr>
<tr id="parameter-private_endpoint_connection_name">
    <td><CopyableCode code="private_endpoint_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private endpoint connection. Required.</td>
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
<tr id="parameter-userid">
    <td><CopyableCode code="userid" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-isCleaningAuthConfig">
    <td><CopyableCode code="isCleaningAuthConfig" /></td>
    <td><code>boolean</code></td>
    <td>Decides if Easy Auth configuration will be removed from backend configuration. Default value is None.</td>
</tr>
<tr id="parameter-isForced">
    <td><CopyableCode code="isForced" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to force the update of the auth configuration on the function app even if an AzureStaticWebApps provider is already configured on the function app. The default is false. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_build_database_connection"
    values={[
        { label: 'get_build_database_connection', value: 'get_build_database_connection' },
        { label: 'get_user_provided_function_app_for_static_site_build', value: 'get_user_provided_function_app_for_static_site_build' },
        { label: 'get_linked_backend_for_build', value: 'get_linked_backend_for_build' },
        { label: 'list_static_site_build_functions', value: 'list_static_site_build_functions' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get_database_connection', value: 'get_database_connection' },
        { label: 'get_user_provided_function_app_for_static_site', value: 'get_user_provided_function_app_for_static_site' },
        { label: 'get_basic_auth', value: 'get_basic_auth' },
        { label: 'get_static_site_custom_domain', value: 'get_static_site_custom_domain' },
        { label: 'get_linked_backend', value: 'get_linked_backend' },
        { label: 'list_static_site_functions', value: 'list_static_site_functions' },
        { label: 'get_static_sites_by_resource_group', value: 'get_static_sites_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_build_database_connection">

Returns overview of a database connection for a static site build by name. Returns overview of a database connection for a static site build by name.

```sql
SELECT
id,
name,
configurationFiles,
connectionIdentity,
connectionString,
kind,
region,
resourceId,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
AND database_connection_name = '{{ database_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_user_provided_function_app_for_static_site_build">

Gets the details of the user provided function app registered with a static site build. Description for Gets the details of the user provided function app registered with a static site build.

```sql
SELECT
id,
name,
createdOn,
functionAppRegion,
functionAppResourceId,
kind,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
AND function_app_name = '{{ function_app_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_linked_backend_for_build">

Returns the details of a linked backend linked to a static site build by name. Returns the details of a linked backend linked to a static site build by name.

```sql
SELECT
id,
name,
backendResourceId,
createdOn,
kind,
provisioningState,
region,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
AND linked_backend_name = '{{ linked_backend_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_static_site_build_functions">

Gets the functions of a particular static site build. Description for Gets the functions of a particular static site build.

```sql
SELECT
id,
name,
functionName,
kind,
triggerType,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection">

Gets a private endpoint connection. Description for Gets a private endpoint connection.

```sql
SELECT
id,
name,
ipAddresses,
kind,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_database_connection">

Returns overview of a database connection for a static site by name. Returns overview of a database connection for a static site by name.

```sql
SELECT
id,
name,
configurationFiles,
connectionIdentity,
connectionString,
kind,
region,
resourceId,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND database_connection_name = '{{ database_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_user_provided_function_app_for_static_site">

Gets the details of the user provided function app registered with a static site. Description for Gets the details of the user provided function app registered with a static site.

```sql
SELECT
id,
name,
createdOn,
functionAppRegion,
functionAppResourceId,
kind,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND function_app_name = '{{ function_app_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_basic_auth">

Gets the basic auth properties for a static site. Description for Gets the basic auth properties for a static site.

```sql
SELECT
id,
name,
applicableEnvironmentsMode,
environments,
kind,
password,
secretState,
secretUrl,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND basic_auth_name = '{{ basic_auth_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_static_site_custom_domain">

Gets an existing custom domain for a particular static site. Description for Gets an existing custom domain for a particular static site.

```sql
SELECT
id,
name,
createdOn,
domainName,
errorMessage,
kind,
status,
systemData,
type,
validationToken
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND domain_name = '{{ domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_linked_backend">

Returns the details of a linked backend linked to a static site by name. Returns the details of a linked backend linked to a static site by name.

```sql
SELECT
id,
name,
backendResourceId,
createdOn,
kind,
provisioningState,
region,
systemData,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND linked_backend_name = '{{ linked_backend_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_static_site_functions">

Gets the functions of a static site. Description for Gets the functions of a static site.

```sql
SELECT
id,
name,
functionName,
kind,
triggerType,
type
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_static_sites_by_resource_group">

Gets all static sites in the specified resource group. Description for Gets all static sites in the specified resource group.

```sql
SELECT
id,
name,
allowConfigFileUpdates,
branch,
buildProperties,
contentDistributionEndpoint,
customDomains,
databaseConnections,
defaultHostname,
enterpriseGradeCdnStatus,
identity,
keyVaultReferenceIdentity,
kind,
linkedBackends,
location,
privateEndpointConnections,
provider,
publicNetworkAccess,
repositoryToken,
repositoryUrl,
sku,
stagingEnvironmentPolicy,
systemData,
tags,
templateProperties,
type,
userProvidedFunctionApps
FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all Static Sites for a subscription. Description for Get all Static Sites for a subscription.

```sql
SELECT
id,
name,
allowConfigFileUpdates,
branch,
buildProperties,
contentDistributionEndpoint,
customDomains,
databaseConnections,
defaultHostname,
enterpriseGradeCdnStatus,
identity,
keyVaultReferenceIdentity,
kind,
linkedBackends,
location,
privateEndpointConnections,
provider,
publicNetworkAccess,
repositoryToken,
repositoryUrl,
sku,
stagingEnvironmentPolicy,
systemData,
tags,
templateProperties,
type,
userProvidedFunctionApps
FROM azure.web.static_sites
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_static_site"
    values={[
        { label: 'create_or_update_static_site', value: 'create_or_update_static_site' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_static_site">

Creates a new static site in an existing resource group, or updates an existing static site. Description for Creates a new static site in an existing resource group, or updates an existing static site.

```sql
INSERT INTO azure.web.static_sites (
tags,
location,
properties,
kind,
sku,
identity,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: static_sites
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the static_sites resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the static_sites resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the static_sites resource.
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
        Core resource properties.
      value:
        defaultHostname: "{{ defaultHostname }}"
        repositoryUrl: "{{ repositoryUrl }}"
        branch: "{{ branch }}"
        customDomains:
          - "{{ customDomains }}"
        repositoryToken: "{{ repositoryToken }}"
        buildProperties:
          appLocation: "{{ appLocation }}"
          apiLocation: "{{ apiLocation }}"
          appArtifactLocation: "{{ appArtifactLocation }}"
          outputLocation: "{{ outputLocation }}"
          appBuildCommand: "{{ appBuildCommand }}"
          apiBuildCommand: "{{ apiBuildCommand }}"
          skipGithubActionWorkflowGeneration: {{ skipGithubActionWorkflowGeneration }}
          githubActionSecretNameOverride: "{{ githubActionSecretNameOverride }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            plan:
              name: "{{ name }}"
              publisher: "{{ publisher }}"
              product: "{{ product }}"
              promotionCode: "{{ promotionCode }}"
              version: "{{ version }}"
            properties:
              id: "{{ id }}"
              name: "{{ name }}"
              kind: "{{ kind }}"
              type: "{{ type }}"
              properties:
                provisioningState: "{{ provisioningState }}"
                privateEndpoint:
                  id: "{{ id }}"
                privateLinkServiceConnectionState:
                  status: "{{ status }}"
                  description: "{{ description }}"
                  actionsRequired: "{{ actionsRequired }}"
                ipAddresses:
                  - "{{ ipAddresses }}"
            sku:
              name: "{{ name }}"
              tier: "{{ tier }}"
              size: "{{ size }}"
              family: "{{ family }}"
              capacity: {{ capacity }}
              skuCapacity:
                minimum: {{ minimum }}
                maximum: {{ maximum }}
                elasticMaximum: {{ elasticMaximum }}
                default: {{ default }}
                scaleType: "{{ scaleType }}"
              locations:
                - "{{ locations }}"
              capabilities:
                - name: "{{ name }}"
                  value: "{{ value }}"
                  reason: "{{ reason }}"
            status: "{{ status }}"
            error:
              extendedCode: "{{ extendedCode }}"
              messageTemplate: "{{ messageTemplate }}"
              parameters:
                - "{{ parameters }}"
              innerErrors:
                - extendedCode: "{{ extendedCode }}"
                  messageTemplate: "{{ messageTemplate }}"
                  parameters: "{{ parameters }}"
                  innerErrors: "{{ innerErrors }}"
                  details: "{{ details }}"
                  target: "{{ target }}"
                  code: "{{ code }}"
                  message: "{{ message }}"
              details:
                - extendedCode: "{{ extendedCode }}"
                  messageTemplate: "{{ messageTemplate }}"
                  parameters: "{{ parameters }}"
                  innerErrors: "{{ innerErrors }}"
                  details: "{{ details }}"
                  target: "{{ target }}"
                  code: "{{ code }}"
                  message: "{{ message }}"
              target: "{{ target }}"
              code: "{{ code }}"
              message: "{{ message }}"
            identity:
              type: "{{ type }}"
              tenantId: "{{ tenantId }}"
              principalId: "{{ principalId }}"
              userAssignedIdentities: "{{ userAssignedIdentities }}"
            zones: "{{ zones }}"
        stagingEnvironmentPolicy: "{{ stagingEnvironmentPolicy }}"
        allowConfigFileUpdates: {{ allowConfigFileUpdates }}
        templateProperties:
          templateRepositoryUrl: "{{ templateRepositoryUrl }}"
          owner: "{{ owner }}"
          repositoryName: "{{ repositoryName }}"
          description: "{{ description }}"
          isPrivate: {{ isPrivate }}
        contentDistributionEndpoint: "{{ contentDistributionEndpoint }}"
        keyVaultReferenceIdentity: "{{ keyVaultReferenceIdentity }}"
        userProvidedFunctionApps:
          - id: "{{ id }}"
            name: "{{ name }}"
            kind: "{{ kind }}"
            type: "{{ type }}"
            properties:
              functionAppResourceId: "{{ functionAppResourceId }}"
              functionAppRegion: "{{ functionAppRegion }}"
              createdOn: "{{ createdOn }}"
        linkedBackends:
          - backendResourceId: "{{ backendResourceId }}"
            region: "{{ region }}"
            createdOn: "{{ createdOn }}"
            provisioningState: "{{ provisioningState }}"
        provider: "{{ provider }}"
        enterpriseGradeCdnStatus: "{{ enterpriseGradeCdnStatus }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        databaseConnections:
          - resourceId: "{{ resourceId }}"
            connectionIdentity: "{{ connectionIdentity }}"
            region: "{{ region }}"
            configurationFiles: "{{ configurationFiles }}"
            name: "{{ name }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource.
    - name: sku
      description: |
        Description of a SKU for a scalable resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
        skuCapacity:
          minimum: {{ minimum }}
          maximum: {{ maximum }}
          elasticMaximum: {{ elasticMaximum }}
          default: {{ default }}
          scaleType: "{{ scaleType }}"
        locations:
          - "{{ locations }}"
        capabilities:
          - name: "{{ name }}"
            value: "{{ value }}"
            reason: "{{ reason }}"
    - name: identity
      description: |
        Managed service identity.
      value:
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_static_site"
    values={[
        { label: 'update_static_site', value: 'update_static_site' }
    ]}
>
<TabItem value="update_static_site">

Creates a new static site in an existing resource group, or updates an existing static site. Description for Creates a new static site in an existing resource group, or updates an existing static site.

```sql
UPDATE azure.web.static_sites
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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
    defaultValue="create_or_update_static_site"
    values={[
        { label: 'create_or_update_static_site', value: 'create_or_update_static_site' }
    ]}
>
<TabItem value="create_or_update_static_site">

Creates a new static site in an existing resource group, or updates an existing static site. Description for Creates a new static site in an existing resource group, or updates an existing static site.

```sql
REPLACE azure.web.static_sites
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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
    defaultValue="detach_user_provided_function_app_from_static_site_build"
    values={[
        { label: 'detach_user_provided_function_app_from_static_site_build', value: 'detach_user_provided_function_app_from_static_site_build' },
        { label: 'unlink_backend_from_build', value: 'unlink_backend_from_build' },
        { label: 'detach_user_provided_function_app_from_static_site', value: 'detach_user_provided_function_app_from_static_site' },
        { label: 'unlink_backend', value: 'unlink_backend' },
        { label: 'delete_static_site', value: 'delete_static_site' }
    ]}
>
<TabItem value="detach_user_provided_function_app_from_static_site_build">

Detach the user provided function app from the static site build. Description for Detach the user provided function app from the static site build.

```sql
DELETE FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND function_app_name = '{{ function_app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="unlink_backend_from_build">

Unlink a backend from a static site build. Unlink a backend from a static site build.

```sql
DELETE FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND linked_backend_name = '{{ linked_backend_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND isCleaningAuthConfig = '{{ isCleaningAuthConfig }}'
;
```
</TabItem>
<TabItem value="detach_user_provided_function_app_from_static_site">

Detach the user provided function app from the static site. Description for Detach the user provided function app from the static site.

```sql
DELETE FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND function_app_name = '{{ function_app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="unlink_backend">

Unlink a backend from a static site. Unlink a backend from a static site.

```sql
DELETE FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND linked_backend_name = '{{ linked_backend_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND isCleaningAuthConfig = '{{ isCleaningAuthConfig }}'
;
```
</TabItem>
<TabItem value="delete_static_site">

Deletes a static site. Description for Deletes a static site.

```sql
DELETE FROM azure.web.static_sites
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_static_site_users"
    values={[
        { label: 'list_static_site_users', value: 'list_static_site_users' },
        { label: 'list_static_site_app_settings', value: 'list_static_site_app_settings' },
        { label: 'list_static_site_configured_roles', value: 'list_static_site_configured_roles' },
        { label: 'list_static_site_function_app_settings', value: 'list_static_site_function_app_settings' },
        { label: 'list_static_site_secrets', value: 'list_static_site_secrets' },
        { label: 'list_static_site_build_app_settings', value: 'list_static_site_build_app_settings' },
        { label: 'list_static_site_build_function_app_settings', value: 'list_static_site_build_function_app_settings' },
        { label: 'list_basic_auth', value: 'list_basic_auth' },
        { label: 'list_static_site_custom_domains', value: 'list_static_site_custom_domains' },
        { label: 'approve_or_reject_private_endpoint_connection', value: 'approve_or_reject_private_endpoint_connection' },
        { label: 'delete_private_endpoint_connection', value: 'delete_private_endpoint_connection' },
        { label: 'get_private_endpoint_connection_list', value: 'get_private_endpoint_connection_list' },
        { label: 'get_static_site', value: 'get_static_site' },
        { label: 'get_private_link_resources', value: 'get_private_link_resources' },
        { label: 'get_database_connections_with_details', value: 'get_database_connections_with_details' },
        { label: 'get_static_site_build', value: 'get_static_site_build' },
        { label: 'delete_static_site_build', value: 'delete_static_site_build' },
        { label: 'get_static_site_builds', value: 'get_static_site_builds' },
        { label: 'get_build_database_connections_with_details', value: 'get_build_database_connections_with_details' },
        { label: 'create_or_update_build_database_connection', value: 'create_or_update_build_database_connection' },
        { label: 'update_build_database_connection', value: 'update_build_database_connection' },
        { label: 'delete_build_database_connection', value: 'delete_build_database_connection' },
        { label: 'get_build_database_connections', value: 'get_build_database_connections' },
        { label: 'get_build_database_connection_with_details', value: 'get_build_database_connection_with_details' },
        { label: 'create_or_update_database_connection', value: 'create_or_update_database_connection' },
        { label: 'update_database_connection', value: 'update_database_connection' },
        { label: 'delete_database_connection', value: 'delete_database_connection' },
        { label: 'get_database_connections', value: 'get_database_connections' },
        { label: 'get_database_connection_with_details', value: 'get_database_connection_with_details' },
        { label: 'register_user_provided_function_app_with_static_site_build', value: 'register_user_provided_function_app_with_static_site_build' },
        { label: 'get_user_provided_function_apps_for_static_site_build', value: 'get_user_provided_function_apps_for_static_site_build' },
        { label: 'register_user_provided_function_app_with_static_site', value: 'register_user_provided_function_app_with_static_site' },
        { label: 'get_user_provided_function_apps_for_static_site', value: 'get_user_provided_function_apps_for_static_site' },
        { label: 'create_or_update_basic_auth', value: 'create_or_update_basic_auth' },
        { label: 'create_or_update_static_site_custom_domain', value: 'create_or_update_static_site_custom_domain' },
        { label: 'delete_static_site_custom_domain', value: 'delete_static_site_custom_domain' },
        { label: 'link_backend', value: 'link_backend' },
        { label: 'get_linked_backends', value: 'get_linked_backends' },
        { label: 'link_backend_to_build', value: 'link_backend_to_build' },
        { label: 'get_linked_backends_for_build', value: 'get_linked_backends_for_build' },
        { label: 'delete_static_site_user', value: 'delete_static_site_user' },
        { label: 'update_static_site_user', value: 'update_static_site_user' },
        { label: 'create_or_update_static_site_app_settings', value: 'create_or_update_static_site_app_settings' },
        { label: 'create_or_update_static_site_function_app_settings', value: 'create_or_update_static_site_function_app_settings' },
        { label: 'create_user_roles_invitation_link', value: 'create_user_roles_invitation_link' },
        { label: 'detach_static_site', value: 'detach_static_site' },
        { label: 'reset_static_site_api_key', value: 'reset_static_site_api_key' },
        { label: 'create_zip_deployment_for_static_site', value: 'create_zip_deployment_for_static_site' },
        { label: 'create_or_update_static_site_build_app_settings', value: 'create_or_update_static_site_build_app_settings' },
        { label: 'create_or_update_static_site_build_function_app_settings', value: 'create_or_update_static_site_build_function_app_settings' },
        { label: 'create_zip_deployment_for_static_site_build', value: 'create_zip_deployment_for_static_site_build' },
        { label: 'validate_custom_domain_can_be_added_to_static_site', value: 'validate_custom_domain_can_be_added_to_static_site' },
        { label: 'validate_backend', value: 'validate_backend' },
        { label: 'validate_backend_for_build', value: 'validate_backend_for_build' },
        { label: 'preview_workflow', value: 'preview_workflow' }
    ]}
>
<TabItem value="list_static_site_users">

Gets the list of users of a static site. Description for Gets the list of users of a static site.

```sql
EXEC azure.web.static_sites.list_static_site_users 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@authprovider='{{ authprovider }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_static_site_app_settings">

Gets the application settings of a static site. Description for Gets the application settings of a static site.

```sql
EXEC azure.web.static_sites.list_static_site_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_static_site_configured_roles">

Lists the roles configured for the static site. Description for Lists the roles configured for the static site.

```sql
EXEC azure.web.static_sites.list_static_site_configured_roles 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_static_site_function_app_settings">

Gets the application settings of a static site. Description for Gets the application settings of a static site.

```sql
EXEC azure.web.static_sites.list_static_site_function_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_static_site_secrets">

Lists the secrets for an existing static site. Description for Lists the secrets for an existing static site.

```sql
EXEC azure.web.static_sites.list_static_site_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_static_site_build_app_settings">

Gets the application settings of a static site build. Description for Gets the application settings of a static site build.

```sql
EXEC azure.web.static_sites.list_static_site_build_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_static_site_build_function_app_settings">

Gets the application settings of a static site build. Description for Gets the application settings of a static site build.

```sql
EXEC azure.web.static_sites.list_static_site_build_function_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_basic_auth">

Gets the basic auth properties for a static site as a collection. Description for Gets the basic auth properties for a static site as a collection.

```sql
EXEC azure.web.static_sites.list_basic_auth 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_static_site_custom_domains">

Gets all static site custom domains for a particular static site. Description for Gets all static site custom domains for a particular static site.

```sql
EXEC azure.web.static_sites.list_static_site_custom_domains 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="approve_or_reject_private_endpoint_connection">

Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.

```sql
EXEC azure.web.static_sites.approve_or_reject_private_endpoint_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_private_endpoint_connection">

Deletes a private endpoint connection. Description for Deletes a private endpoint connection.

```sql
EXEC azure.web.static_sites.delete_private_endpoint_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection_list">

Gets the list of private endpoint connections associated with a static site. Description for Gets the list of private endpoint connections associated with a static site.

```sql
EXEC azure.web.static_sites.get_private_endpoint_connection_list 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_static_site">

Gets the details of a static site. Description for Gets the details of a static site.

```sql
EXEC azure.web.static_sites.get_static_site 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_link_resources">

Gets the private link resources. Description for Gets the private link resources.

```sql
EXEC azure.web.static_sites.get_private_link_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_database_connections_with_details">

Returns details of database connections for a static site. Returns details of database connections for a static site.

```sql
EXEC azure.web.static_sites.get_database_connections_with_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_static_site_build">

Gets the details of a static site build. Description for Gets the details of a static site build.

```sql
EXEC azure.web.static_sites.get_static_site_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_static_site_build">

Deletes a static site build. Description for Deletes a static site build.

```sql
EXEC azure.web.static_sites.delete_static_site_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_static_site_builds">

Gets all static site builds for a particular static site. Description for Gets all static site builds for a particular static site.

```sql
EXEC azure.web.static_sites.get_static_site_builds 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_build_database_connections_with_details">

Returns details of database connections for a static site build. Returns details of database connections for a static site build.

```sql
EXEC azure.web.static_sites.get_build_database_connections_with_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_build_database_connection">

Create or update a database connection for a static site build. Description for Create or update a database connection for a static site build.

```sql
EXEC azure.web.static_sites.create_or_update_build_database_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_build_database_connection">

Create or update a database connection for a static site build. Description for Create or update a database connection for a static site build.

```sql
EXEC azure.web.static_sites.update_build_database_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_build_database_connection">

Delete a database connection for a static site build. Delete a database connection for a static site build.

```sql
EXEC azure.web.static_sites.delete_build_database_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_build_database_connections">

Returns overviews of database connections for a static site build. Returns overviews of database connections for a static site build.

```sql
EXEC azure.web.static_sites.get_build_database_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_build_database_connection_with_details">

Returns details of a database connection for a static site build by name. Returns details of a database connection for a static site build by name.

```sql
EXEC azure.web.static_sites.get_build_database_connection_with_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_database_connection">

Create or update a database connection for a static site. Description for Create or update a database connection for a static site.

```sql
EXEC azure.web.static_sites.create_or_update_database_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_database_connection">

Create or update a database connection for a static site. Description for Create or update a database connection for a static site.

```sql
EXEC azure.web.static_sites.update_database_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_database_connection">

Delete a database connection for a static site. Delete a database connection for a static site.

```sql
EXEC azure.web.static_sites.delete_database_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_database_connections">

Returns overviews of database connections for a static site. Returns overviews of database connections for a static site.

```sql
EXEC azure.web.static_sites.get_database_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_database_connection_with_details">

Returns details of a database connection for a static site by name. Returns details of a database connection for a static site by name.

```sql
EXEC azure.web.static_sites.get_database_connection_with_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@database_connection_name='{{ database_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="register_user_provided_function_app_with_static_site_build">

Register a user provided function app with a static site build. Description for Register a user provided function app with a static site build.

```sql
EXEC azure.web.static_sites.register_user_provided_function_app_with_static_site_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@function_app_name='{{ function_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@isForced={{ isForced }} 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_user_provided_function_apps_for_static_site_build">

Gets the details of the user provided function apps registered with a static site build. Description for Gets the details of the user provided function apps registered with a static site build.

```sql
EXEC azure.web.static_sites.get_user_provided_function_apps_for_static_site_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="register_user_provided_function_app_with_static_site">

Register a user provided function app with a static site. Description for Register a user provided function app with a static site.

```sql
EXEC azure.web.static_sites.register_user_provided_function_app_with_static_site 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_app_name='{{ function_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@isForced={{ isForced }} 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_user_provided_function_apps_for_static_site">

Gets the details of the user provided function apps registered with a static site. Description for Gets the details of the user provided function apps registered with a static site.

```sql
EXEC azure.web.static_sites.get_user_provided_function_apps_for_static_site 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_basic_auth">

Adds or updates basic auth for a static site. Description for Adds or updates basic auth for a static site.

```sql
EXEC azure.web.static_sites.create_or_update_basic_auth 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@basic_auth_name='{{ basic_auth_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="create_or_update_static_site_custom_domain">

Creates a new static site custom domain in an existing resource group and static site. Description for Creates a new static site custom domain in an existing resource group and static site.

```sql
EXEC azure.web.static_sites.create_or_update_static_site_custom_domain 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_static_site_custom_domain">

Deletes a custom domain. Description for Deletes a custom domain.

```sql
EXEC azure.web.static_sites.delete_static_site_custom_domain 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="link_backend">

Link backend to a static site. Link backend to a static site.

```sql
EXEC azure.web.static_sites.link_backend 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@linked_backend_name='{{ linked_backend_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_linked_backends">

Returns details of all backends linked to a static site. Returns details of all backends linked to a static site.

```sql
EXEC azure.web.static_sites.get_linked_backends 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="link_backend_to_build">

Link backend to a static site build. Link backend to a static site build.

```sql
EXEC azure.web.static_sites.link_backend_to_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@linked_backend_name='{{ linked_backend_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_linked_backends_for_build">

Returns details of all backends linked to a static site build. Returns details of all backends linked to a static site build.

```sql
EXEC azure.web.static_sites.get_linked_backends_for_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_static_site_user">

Deletes the user entry from the static site. Description for Deletes the user entry from the static site.

```sql
EXEC azure.web.static_sites.delete_static_site_user 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@authprovider='{{ authprovider }}' --required, 
@userid='{{ userid }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_static_site_user">

Updates a user entry with the listed roles. Description for Updates a user entry with the listed roles.

```sql
EXEC azure.web.static_sites.update_static_site_user 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@authprovider='{{ authprovider }}' --required, 
@userid='{{ userid }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_or_update_static_site_app_settings">

Creates or updates the app settings of a static site. Description for Creates or updates the app settings of a static site.

```sql
EXEC azure.web.static_sites.create_or_update_static_site_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_or_update_static_site_function_app_settings">

Creates or updates the function app settings of a static site. Description for Creates or updates the function app settings of a static site.

```sql
EXEC azure.web.static_sites.create_or_update_static_site_function_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_user_roles_invitation_link">

Creates an invitation link for a user with the role. Description for Creates an invitation link for a user with the role.

```sql
EXEC azure.web.static_sites.create_user_roles_invitation_link 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="detach_static_site">

Detaches a static site. Description for Detaches a static site.

```sql
EXEC azure.web.static_sites.detach_static_site 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_static_site_api_key">

Resets the api key for an existing static site. Description for Resets the api key for an existing static site.

```sql
EXEC azure.web.static_sites.reset_static_site_api_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_zip_deployment_for_static_site">

Deploys zipped content to a static site. Description for Deploys zipped content to a static site.

```sql
EXEC azure.web.static_sites.create_zip_deployment_for_static_site 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_or_update_static_site_build_app_settings">

Creates or updates the app settings of a static site build. Description for Creates or updates the app settings of a static site build.

```sql
EXEC azure.web.static_sites.create_or_update_static_site_build_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_or_update_static_site_build_function_app_settings">

Creates or updates the function app settings of a static site build. Description for Creates or updates the function app settings of a static site build.

```sql
EXEC azure.web.static_sites.create_or_update_static_site_build_function_app_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_zip_deployment_for_static_site_build">

Deploys zipped content to a specific environment of a static site. Description for Deploys zipped content to a specific environment of a static site.

```sql
EXEC azure.web.static_sites.create_zip_deployment_for_static_site_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="validate_custom_domain_can_be_added_to_static_site">

Validates a particular custom domain can be added to a static site. Description for Validates a particular custom domain can be added to a static site.

```sql
EXEC azure.web.static_sites.validate_custom_domain_can_be_added_to_static_site 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="validate_backend">

Validates that a backend can be linked to a static site. Validates that a backend can be linked to a static site.

```sql
EXEC azure.web.static_sites.validate_backend 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@linked_backend_name='{{ linked_backend_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="validate_backend_for_build">

Validates that a backend can be linked to a static site build. Validates that a backend can be linked to a static site build.

```sql
EXEC azure.web.static_sites.validate_backend_for_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@linked_backend_name='{{ linked_backend_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="preview_workflow">

Generates a preview workflow file for the static site. Description for Generates a preview workflow file for the static site.

```sql
EXEC azure.web.static_sites.preview_workflow 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
