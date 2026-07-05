--- 
title: database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts
  - cosmosdb
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

Creates, updates, deletes, gets or lists a <code>database_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database_accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.database_accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_metrics"
    values={[
        { label: 'list_metrics', value: 'list_metrics' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_metrics">

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
    <td><CopyableCode code="name" /></td>
    <td><code>object</code></td>
    <td>The name information for the metric.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time for the metric (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="metricValues" /></td>
    <td><code>array</code></td>
    <td>The metric values for the specified time window and timestep.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the metric (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="timeGrain" /></td>
    <td><code>string</code></td>
    <td>The time grain to be used to summarize the metric values.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>The unit of the metric. Known values are: "Count", "Bytes", "Seconds", "Percent", "CountPerSecond", "BytesPerSecond", and "Milliseconds". (Count, Bytes, Seconds, Percent, CountPerSecond, BytesPerSecond, Milliseconds)</td>
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
    <td><CopyableCode code="analyticalStorageConfiguration" /></td>
    <td><code>object</code></td>
    <td>Analytical storage specific properties.</td>
</tr>
<tr>
    <td><CopyableCode code="apiProperties" /></td>
    <td><code>object</code></td>
    <td>API specific properties.</td>
</tr>
<tr>
    <td><CopyableCode code="backupPolicy" /></td>
    <td><code>object</code></td>
    <td>The object representing the policy for taking backups on an account.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>List of Cosmos DB capabilities for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>The object that represents all properties related to capacity enforcement on an account.</td>
</tr>
<tr>
    <td><CopyableCode code="connectorOffer" /></td>
    <td><code>string</code></td>
    <td>The cassandra connector offer type for the Cosmos DB database C* account. "Small" (Small)</td>
</tr>
<tr>
    <td><CopyableCode code="consistencyPolicy" /></td>
    <td><code>object</code></td>
    <td>The consistency policy for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="cors" /></td>
    <td><code>array</code></td>
    <td>The CORS policy for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Enum to indicate the mode of account creation. Known values are: "Default" and "Restore". (Default, Restore)</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeyStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates the status of the Customer Managed Key feature on the account. In case there are errors, the property provides troubleshooting guidance.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseAccountOfferType" /></td>
    <td><code>string</code></td>
    <td>The offer type for the Cosmos DB database account. Default value: Standard. Default value is "Standard".</td>
</tr>
<tr>
    <td><CopyableCode code="defaultIdentity" /></td>
    <td><code>string</code></td>
    <td>The default identity for accessing key vault used in features like customer managed keys. The default identity needs to be explicitly set by the users. It can be "FirstPartyIdentity", "SystemAssignedIdentity" and more.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPriorityLevel" /></td>
    <td><code>string</code></td>
    <td>Enum to indicate default Priority Level of request for Priority Based Execution. Known values are: "High" and "Low". (High, Low)</td>
</tr>
<tr>
    <td><CopyableCode code="disableKeyBasedMetadataWriteAccess" /></td>
    <td><code>boolean</code></td>
    <td>Disable write operations on metadata resources (databases, containers, throughput) via account keys.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="documentEndpoint" /></td>
    <td><code>string</code></td>
    <td>The connection endpoint for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAnalyticalStorage" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether to enable storage analytics.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticFailover" /></td>
    <td><code>boolean</code></td>
    <td>Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBurstCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Burst Capacity Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableCassandraConnector" /></td>
    <td><code>boolean</code></td>
    <td>Enables the cassandra connector on the Cosmos DB C* account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFreeTier" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether Free Tier is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableMultipleWriteLocations" /></td>
    <td><code>boolean</code></td>
    <td>Enables the account to write in multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePartitionMerge" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Partition Merge feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePerRegionPerPartitionAutoscale" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Per-Region Per-partition autoscale Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePriorityBasedExecution" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Priority Based Execution Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enforceHierarchicalPartitionKeyIdLastLevel" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of hierarchical partition key ID last level enforcement on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverPolicies" /></td>
    <td><code>array</code></td>
    <td>An array that contains the regions ordered by their failover priorities.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier assigned to the database account.</td>
</tr>
<tr>
    <td><CopyableCode code="ipRules" /></td>
    <td><code>array</code></td>
    <td>List of IpRules.</td>
</tr>
<tr>
    <td><CopyableCode code="isVirtualNetworkFilterEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether to enable/disable Virtual Network ACL rules.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultKeyUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultKeyUriVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Customer Managed Key currently being used by the account.</td>
</tr>
<tr>
    <td><CopyableCode code="keysMetadata" /></td>
    <td><code>object</code></td>
    <td>The object that represents the metadata for the Account Keys of the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of database account. This can only be set at database account creation. Known values are: "GlobalDocumentDB", "MongoDB", and "Parse". (GlobalDocumentDB, MongoDB, Parse)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>An array that contains all of the locations enabled for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Indicates the minimum allowed Tls version. The default is Tls 1.0, except for Cassandra and Mongo API's, which only work with Tls 1.2. Known values are: "Tls", "Tls11", and "Tls12". (Tls, Tls11, Tls12)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAclBypass" /></td>
    <td><code>string</code></td>
    <td>Indicates what services are allowed to bypass firewall checks. Known values are: "None" and "AzureServices". (None, AzureServices)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAclBypassResourceIds" /></td>
    <td><code>array</code></td>
    <td>An array that contains the Resource Ids for Network Acl Bypass for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections configured for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="readLocations" /></td>
    <td><code>array</code></td>
    <td>An array that contains of the read locations enabled for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreParameters" /></td>
    <td><code>object</code></td>
    <td>Parameters to indicate the information about the restore.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \"defaultExperience\": \"Cassandra\". Current \"defaultExperience\" values also include \"Table\", \"Graph\", \"DocumentDB\", and \"MongoDB\".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkRules" /></td>
    <td><code>array</code></td>
    <td>List of Virtual Network ACL rules configured for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="writeLocations" /></td>
    <td><code>array</code></td>
    <td>An array that contains the write location for the Cosmos DB account.</td>
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
    <td><CopyableCode code="analyticalStorageConfiguration" /></td>
    <td><code>object</code></td>
    <td>Analytical storage specific properties.</td>
</tr>
<tr>
    <td><CopyableCode code="apiProperties" /></td>
    <td><code>object</code></td>
    <td>API specific properties.</td>
</tr>
<tr>
    <td><CopyableCode code="backupPolicy" /></td>
    <td><code>object</code></td>
    <td>The object representing the policy for taking backups on an account.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>List of Cosmos DB capabilities for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>The object that represents all properties related to capacity enforcement on an account.</td>
</tr>
<tr>
    <td><CopyableCode code="connectorOffer" /></td>
    <td><code>string</code></td>
    <td>The cassandra connector offer type for the Cosmos DB database C* account. "Small" (Small)</td>
</tr>
<tr>
    <td><CopyableCode code="consistencyPolicy" /></td>
    <td><code>object</code></td>
    <td>The consistency policy for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="cors" /></td>
    <td><code>array</code></td>
    <td>The CORS policy for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Enum to indicate the mode of account creation. Known values are: "Default" and "Restore". (Default, Restore)</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeyStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates the status of the Customer Managed Key feature on the account. In case there are errors, the property provides troubleshooting guidance.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseAccountOfferType" /></td>
    <td><code>string</code></td>
    <td>The offer type for the Cosmos DB database account. Default value: Standard. Default value is "Standard".</td>
</tr>
<tr>
    <td><CopyableCode code="defaultIdentity" /></td>
    <td><code>string</code></td>
    <td>The default identity for accessing key vault used in features like customer managed keys. The default identity needs to be explicitly set by the users. It can be "FirstPartyIdentity", "SystemAssignedIdentity" and more.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPriorityLevel" /></td>
    <td><code>string</code></td>
    <td>Enum to indicate default Priority Level of request for Priority Based Execution. Known values are: "High" and "Low". (High, Low)</td>
</tr>
<tr>
    <td><CopyableCode code="disableKeyBasedMetadataWriteAccess" /></td>
    <td><code>boolean</code></td>
    <td>Disable write operations on metadata resources (databases, containers, throughput) via account keys.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="documentEndpoint" /></td>
    <td><code>string</code></td>
    <td>The connection endpoint for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAnalyticalStorage" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether to enable storage analytics.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticFailover" /></td>
    <td><code>boolean</code></td>
    <td>Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBurstCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Burst Capacity Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableCassandraConnector" /></td>
    <td><code>boolean</code></td>
    <td>Enables the cassandra connector on the Cosmos DB C* account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFreeTier" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether Free Tier is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableMultipleWriteLocations" /></td>
    <td><code>boolean</code></td>
    <td>Enables the account to write in multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePartitionMerge" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Partition Merge feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePerRegionPerPartitionAutoscale" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Per-Region Per-partition autoscale Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePriorityBasedExecution" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Priority Based Execution Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enforceHierarchicalPartitionKeyIdLastLevel" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of hierarchical partition key ID last level enforcement on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverPolicies" /></td>
    <td><code>array</code></td>
    <td>An array that contains the regions ordered by their failover priorities.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier assigned to the database account.</td>
</tr>
<tr>
    <td><CopyableCode code="ipRules" /></td>
    <td><code>array</code></td>
    <td>List of IpRules.</td>
</tr>
<tr>
    <td><CopyableCode code="isVirtualNetworkFilterEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether to enable/disable Virtual Network ACL rules.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultKeyUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultKeyUriVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Customer Managed Key currently being used by the account.</td>
</tr>
<tr>
    <td><CopyableCode code="keysMetadata" /></td>
    <td><code>object</code></td>
    <td>The object that represents the metadata for the Account Keys of the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of database account. This can only be set at database account creation. Known values are: "GlobalDocumentDB", "MongoDB", and "Parse". (GlobalDocumentDB, MongoDB, Parse)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>An array that contains all of the locations enabled for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Indicates the minimum allowed Tls version. The default is Tls 1.0, except for Cassandra and Mongo API's, which only work with Tls 1.2. Known values are: "Tls", "Tls11", and "Tls12". (Tls, Tls11, Tls12)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAclBypass" /></td>
    <td><code>string</code></td>
    <td>Indicates what services are allowed to bypass firewall checks. Known values are: "None" and "AzureServices". (None, AzureServices)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAclBypassResourceIds" /></td>
    <td><code>array</code></td>
    <td>An array that contains the Resource Ids for Network Acl Bypass for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections configured for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="readLocations" /></td>
    <td><code>array</code></td>
    <td>An array that contains of the read locations enabled for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreParameters" /></td>
    <td><code>object</code></td>
    <td>Parameters to indicate the information about the restore.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \"defaultExperience\": \"Cassandra\". Current \"defaultExperience\" values also include \"Table\", \"Graph\", \"DocumentDB\", and \"MongoDB\".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkRules" /></td>
    <td><code>array</code></td>
    <td>List of Virtual Network ACL rules configured for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="writeLocations" /></td>
    <td><code>array</code></td>
    <td>An array that contains the write location for the Cosmos DB account.</td>
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
    <td><CopyableCode code="analyticalStorageConfiguration" /></td>
    <td><code>object</code></td>
    <td>Analytical storage specific properties.</td>
</tr>
<tr>
    <td><CopyableCode code="apiProperties" /></td>
    <td><code>object</code></td>
    <td>API specific properties.</td>
</tr>
<tr>
    <td><CopyableCode code="backupPolicy" /></td>
    <td><code>object</code></td>
    <td>The object representing the policy for taking backups on an account.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>List of Cosmos DB capabilities for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>The object that represents all properties related to capacity enforcement on an account.</td>
</tr>
<tr>
    <td><CopyableCode code="connectorOffer" /></td>
    <td><code>string</code></td>
    <td>The cassandra connector offer type for the Cosmos DB database C* account. "Small" (Small)</td>
</tr>
<tr>
    <td><CopyableCode code="consistencyPolicy" /></td>
    <td><code>object</code></td>
    <td>The consistency policy for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="cors" /></td>
    <td><code>array</code></td>
    <td>The CORS policy for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Enum to indicate the mode of account creation. Known values are: "Default" and "Restore". (Default, Restore)</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeyStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates the status of the Customer Managed Key feature on the account. In case there are errors, the property provides troubleshooting guidance.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseAccountOfferType" /></td>
    <td><code>string</code></td>
    <td>The offer type for the Cosmos DB database account. Default value: Standard. Default value is "Standard".</td>
</tr>
<tr>
    <td><CopyableCode code="defaultIdentity" /></td>
    <td><code>string</code></td>
    <td>The default identity for accessing key vault used in features like customer managed keys. The default identity needs to be explicitly set by the users. It can be "FirstPartyIdentity", "SystemAssignedIdentity" and more.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPriorityLevel" /></td>
    <td><code>string</code></td>
    <td>Enum to indicate default Priority Level of request for Priority Based Execution. Known values are: "High" and "Low". (High, Low)</td>
</tr>
<tr>
    <td><CopyableCode code="disableKeyBasedMetadataWriteAccess" /></td>
    <td><code>boolean</code></td>
    <td>Disable write operations on metadata resources (databases, containers, throughput) via account keys.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="documentEndpoint" /></td>
    <td><code>string</code></td>
    <td>The connection endpoint for the Cosmos DB database account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAnalyticalStorage" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether to enable storage analytics.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticFailover" /></td>
    <td><code>boolean</code></td>
    <td>Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBurstCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Burst Capacity Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableCassandraConnector" /></td>
    <td><code>boolean</code></td>
    <td>Enables the cassandra connector on the Cosmos DB C* account.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFreeTier" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether Free Tier is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableMultipleWriteLocations" /></td>
    <td><code>boolean</code></td>
    <td>Enables the account to write in multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePartitionMerge" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Partition Merge feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePerRegionPerPartitionAutoscale" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Per-Region Per-partition autoscale Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePriorityBasedExecution" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of Priority Based Execution Preview feature on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="enforceHierarchicalPartitionKeyIdLastLevel" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate enabling/disabling of hierarchical partition key ID last level enforcement on the account.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverPolicies" /></td>
    <td><code>array</code></td>
    <td>An array that contains the regions ordered by their failover priorities.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier assigned to the database account.</td>
</tr>
<tr>
    <td><CopyableCode code="ipRules" /></td>
    <td><code>array</code></td>
    <td>List of IpRules.</td>
</tr>
<tr>
    <td><CopyableCode code="isVirtualNetworkFilterEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether to enable/disable Virtual Network ACL rules.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultKeyUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultKeyUriVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Customer Managed Key currently being used by the account.</td>
</tr>
<tr>
    <td><CopyableCode code="keysMetadata" /></td>
    <td><code>object</code></td>
    <td>The object that represents the metadata for the Account Keys of the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of database account. This can only be set at database account creation. Known values are: "GlobalDocumentDB", "MongoDB", and "Parse". (GlobalDocumentDB, MongoDB, Parse)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>An array that contains all of the locations enabled for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Indicates the minimum allowed Tls version. The default is Tls 1.0, except for Cassandra and Mongo API's, which only work with Tls 1.2. Known values are: "Tls", "Tls11", and "Tls12". (Tls, Tls11, Tls12)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAclBypass" /></td>
    <td><code>string</code></td>
    <td>Indicates what services are allowed to bypass firewall checks. Known values are: "None" and "AzureServices". (None, AzureServices)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAclBypassResourceIds" /></td>
    <td><code>array</code></td>
    <td>An array that contains the Resource Ids for Network Acl Bypass for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections configured for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="readLocations" /></td>
    <td><code>array</code></td>
    <td>An array that contains of the read locations enabled for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreParameters" /></td>
    <td><code>object</code></td>
    <td>Parameters to indicate the information about the restore.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \"defaultExperience\": \"Cassandra\". Current \"defaultExperience\" values also include \"Table\", \"Graph\", \"DocumentDB\", and \"MongoDB\".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkRules" /></td>
    <td><code>array</code></td>
    <td>List of Virtual Network ACL rules configured for the Cosmos DB account.</td>
</tr>
<tr>
    <td><CopyableCode code="writeLocations" /></td>
    <td><code>array</code></td>
    <td>An array that contains the write location for the Cosmos DB account.</td>
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
    <td><a href="#list_metrics"><CopyableCode code="list_metrics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td></td>
    <td>Retrieves the metrics determined by the given filter for the given database account.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the Azure Cosmos DB database accounts available under the given resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the Azure Cosmos DB database accounts available under the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the properties of an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the access keys for the specified Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_connection_strings"><CopyableCode code="list_connection_strings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the connection strings for the specified Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_read_only_keys"><CopyableCode code="list_read_only_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the read-only access keys for the specified Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#get_read_only_keys"><CopyableCode code="get_read_only_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the read-only access keys for the specified Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_usages"><CopyableCode code="list_usages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves the usages (most recent data) for the given database account.</td>
</tr>
<tr>
    <td><a href="#list_metric_definitions"><CopyableCode code="list_metric_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves metric definitions for the given database account.</td>
</tr>
<tr>
    <td><a href="#failover_priority_change"><CopyableCode code="failover_priority_change" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-failoverPolicies"><code>failoverPolicies</code></a></td>
    <td></td>
    <td>Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists.</td>
</tr>
<tr>
    <td><a href="#offline_region"><CopyableCode code="offline_region" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td></td>
    <td>Offline the specified region for the specified Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#online_region"><CopyableCode code="online_region" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td></td>
    <td>Online the specified region for the specified Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyKind"><code>keyKind</code></a></td>
    <td></td>
    <td>Regenerates an access key for the specified Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#check_name_exists"><CopyableCode code="check_name_exists" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_name"><code>account_name</code></a></td>
    <td></td>
    <td>Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 50 characters.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. Required.</td>
</tr>
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database account name. Required.</td>
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
    <td>An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_metrics"
    values={[
        { label: 'list_metrics', value: 'list_metrics' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_metrics">

Retrieves the metrics determined by the given filter for the given database account.

```sql
SELECT
name,
endTime,
metricValues,
startTime,
timeGrain,
unit
FROM azure.cosmosdb.database_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}' -- required
;
```
</TabItem>
<TabItem value="get">

Retrieves the properties of an existing Azure Cosmos DB database account.

```sql
SELECT
id,
name,
analyticalStorageConfiguration,
apiProperties,
backupPolicy,
capabilities,
capacity,
connectorOffer,
consistencyPolicy,
cors,
createMode,
customerManagedKeyStatus,
databaseAccountOfferType,
defaultIdentity,
defaultPriorityLevel,
disableKeyBasedMetadataWriteAccess,
disableLocalAuth,
documentEndpoint,
enableAnalyticalStorage,
enableAutomaticFailover,
enableBurstCapacity,
enableCassandraConnector,
enableFreeTier,
enableMultipleWriteLocations,
enablePartitionMerge,
enablePerRegionPerPartitionAutoscale,
enablePriorityBasedExecution,
enforceHierarchicalPartitionKeyIdLastLevel,
failoverPolicies,
identity,
instanceId,
ipRules,
isVirtualNetworkFilterEnabled,
keyVaultKeyUri,
keyVaultKeyUriVersion,
keysMetadata,
kind,
location,
locations,
minimalTlsVersion,
networkAclBypass,
networkAclBypassResourceIds,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
readLocations,
restoreParameters,
systemData,
tags,
type,
virtualNetworkRules,
writeLocations
FROM azure.cosmosdb.database_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the Azure Cosmos DB database accounts available under the given resource group.

```sql
SELECT
id,
name,
analyticalStorageConfiguration,
apiProperties,
backupPolicy,
capabilities,
capacity,
connectorOffer,
consistencyPolicy,
cors,
createMode,
customerManagedKeyStatus,
databaseAccountOfferType,
defaultIdentity,
defaultPriorityLevel,
disableKeyBasedMetadataWriteAccess,
disableLocalAuth,
documentEndpoint,
enableAnalyticalStorage,
enableAutomaticFailover,
enableBurstCapacity,
enableCassandraConnector,
enableFreeTier,
enableMultipleWriteLocations,
enablePartitionMerge,
enablePerRegionPerPartitionAutoscale,
enablePriorityBasedExecution,
enforceHierarchicalPartitionKeyIdLastLevel,
failoverPolicies,
identity,
instanceId,
ipRules,
isVirtualNetworkFilterEnabled,
keyVaultKeyUri,
keyVaultKeyUriVersion,
keysMetadata,
kind,
location,
locations,
minimalTlsVersion,
networkAclBypass,
networkAclBypassResourceIds,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
readLocations,
restoreParameters,
systemData,
tags,
type,
virtualNetworkRules,
writeLocations
FROM azure.cosmosdb.database_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the Azure Cosmos DB database accounts available under the subscription.

```sql
SELECT
id,
name,
analyticalStorageConfiguration,
apiProperties,
backupPolicy,
capabilities,
capacity,
connectorOffer,
consistencyPolicy,
cors,
createMode,
customerManagedKeyStatus,
databaseAccountOfferType,
defaultIdentity,
defaultPriorityLevel,
disableKeyBasedMetadataWriteAccess,
disableLocalAuth,
documentEndpoint,
enableAnalyticalStorage,
enableAutomaticFailover,
enableBurstCapacity,
enableCassandraConnector,
enableFreeTier,
enableMultipleWriteLocations,
enablePartitionMerge,
enablePerRegionPerPartitionAutoscale,
enablePriorityBasedExecution,
enforceHierarchicalPartitionKeyIdLastLevel,
failoverPolicies,
identity,
instanceId,
ipRules,
isVirtualNetworkFilterEnabled,
keyVaultKeyUri,
keyVaultKeyUriVersion,
keysMetadata,
kind,
location,
locations,
minimalTlsVersion,
networkAclBypass,
networkAclBypassResourceIds,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
readLocations,
restoreParameters,
systemData,
tags,
type,
virtualNetworkRules,
writeLocations
FROM azure.cosmosdb.database_accounts
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

Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account.

```sql
INSERT INTO azure.cosmosdb.database_accounts (
location,
tags,
identity,
kind,
properties,
resource_group_name,
account_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ kind }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: database_accounts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the database_accounts resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the database_accounts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the database_accounts resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location of the resource group to which the resource belongs.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
    - name: identity
      description: |
        Identity for the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Indicates the type of database account. This can only be set at database account creation. Known values are: "GlobalDocumentDB", "MongoDB", and "Parse".
      valid_values: ['GlobalDocumentDB', 'MongoDB', 'Parse']
    - name: properties
      description: |
        Properties to create and update Azure Cosmos DB database accounts. Required.
      value:
        consistencyPolicy:
          defaultConsistencyLevel: "{{ defaultConsistencyLevel }}"
          maxStalenessPrefix: {{ maxStalenessPrefix }}
          maxIntervalInSeconds: {{ maxIntervalInSeconds }}
        locations:
          - id: "{{ id }}"
            locationName: "{{ locationName }}"
            documentEndpoint: "{{ documentEndpoint }}"
            provisioningState: "{{ provisioningState }}"
            failoverPriority: {{ failoverPriority }}
            isZoneRedundant: {{ isZoneRedundant }}
        databaseAccountOfferType: "{{ databaseAccountOfferType }}"
        ipRules:
          - ipAddressOrRange: "{{ ipAddressOrRange }}"
        isVirtualNetworkFilterEnabled: {{ isVirtualNetworkFilterEnabled }}
        enableAutomaticFailover: {{ enableAutomaticFailover }}
        capabilities:
          - name: "{{ name }}"
        virtualNetworkRules:
          - id: "{{ id }}"
            ignoreMissingVNetServiceEndpoint: {{ ignoreMissingVNetServiceEndpoint }}
        enableMultipleWriteLocations: {{ enableMultipleWriteLocations }}
        enableCassandraConnector: {{ enableCassandraConnector }}
        connectorOffer: "{{ connectorOffer }}"
        disableKeyBasedMetadataWriteAccess: {{ disableKeyBasedMetadataWriteAccess }}
        keyVaultKeyUri: "{{ keyVaultKeyUri }}"
        defaultIdentity: "{{ defaultIdentity }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        enableFreeTier: {{ enableFreeTier }}
        apiProperties:
          serverVersion: "{{ serverVersion }}"
        enableAnalyticalStorage: {{ enableAnalyticalStorage }}
        analyticalStorageConfiguration:
          schemaType: "{{ schemaType }}"
        createMode: "{{ createMode }}"
        backupPolicy:
          type: "{{ type }}"
          migrationState:
            status: "{{ status }}"
            targetType: "{{ targetType }}"
            startTime: "{{ startTime }}"
        cors:
          - allowedOrigins: "{{ allowedOrigins }}"
            allowedMethods: "{{ allowedMethods }}"
            allowedHeaders: "{{ allowedHeaders }}"
            exposedHeaders: "{{ exposedHeaders }}"
            maxAgeInSeconds: {{ maxAgeInSeconds }}
        networkAclBypass: "{{ networkAclBypass }}"
        networkAclBypassResourceIds:
          - "{{ networkAclBypassResourceIds }}"
        disableLocalAuth: {{ disableLocalAuth }}
        restoreParameters:
          restoreSource: "{{ restoreSource }}"
          restoreTimestampInUtc: "{{ restoreTimestampInUtc }}"
          restoreWithTtlDisabled: {{ restoreWithTtlDisabled }}
          restoreMode: "{{ restoreMode }}"
          databasesToRestore:
            - databaseName: "{{ databaseName }}"
              collectionNames: "{{ collectionNames }}"
          gremlinDatabasesToRestore:
            - databaseName: "{{ databaseName }}"
              graphNames: "{{ graphNames }}"
          tablesToRestore:
            - "{{ tablesToRestore }}"
          sourceBackupLocation: "{{ sourceBackupLocation }}"
        capacity:
          totalThroughputLimit: {{ totalThroughputLimit }}
        keysMetadata:
          primaryMasterKey:
            generationTime: "{{ generationTime }}"
          secondaryMasterKey:
            generationTime: "{{ generationTime }}"
          primaryReadonlyMasterKey:
            generationTime: "{{ generationTime }}"
          secondaryReadonlyMasterKey:
            generationTime: "{{ generationTime }}"
        enablePartitionMerge: {{ enablePartitionMerge }}
        enableBurstCapacity: {{ enableBurstCapacity }}
        minimalTlsVersion: "{{ minimalTlsVersion }}"
        customerManagedKeyStatus: "{{ customerManagedKeyStatus }}"
        enablePriorityBasedExecution: {{ enablePriorityBasedExecution }}
        defaultPriorityLevel: "{{ defaultPriorityLevel }}"
        enablePerRegionPerPartitionAutoscale: {{ enablePerRegionPerPartitionAutoscale }}
        enforceHierarchicalPartitionKeyIdLastLevel: {{ enforceHierarchicalPartitionKeyIdLastLevel }}
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

Updates the properties of an existing Azure Cosmos DB database account.

```sql
UPDATE azure.cosmosdb.database_accounts
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account.

```sql
REPLACE azure.cosmosdb.database_accounts
SET 
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
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

Deletes an existing Azure Cosmos DB database account.

```sql
DELETE FROM azure.cosmosdb.database_accounts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'list_connection_strings', value: 'list_connection_strings' },
        { label: 'list_read_only_keys', value: 'list_read_only_keys' },
        { label: 'get_read_only_keys', value: 'get_read_only_keys' },
        { label: 'list_usages', value: 'list_usages' },
        { label: 'list_metric_definitions', value: 'list_metric_definitions' },
        { label: 'failover_priority_change', value: 'failover_priority_change' },
        { label: 'offline_region', value: 'offline_region' },
        { label: 'online_region', value: 'online_region' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'check_name_exists', value: 'check_name_exists' }
    ]}
>
<TabItem value="list_keys">

Lists the access keys for the specified Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.database_accounts.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_connection_strings">

Lists the connection strings for the specified Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.database_accounts.list_connection_strings 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_read_only_keys">

Lists the read-only access keys for the specified Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.database_accounts.list_read_only_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_read_only_keys">

Lists the read-only access keys for the specified Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.database_accounts.get_read_only_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_usages">

Retrieves the usages (most recent data) for the given database account.

```sql
EXEC azure.cosmosdb.database_accounts.list_usages 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_metric_definitions">

Retrieves metric definitions for the given database account.

```sql
EXEC azure.cosmosdb.database_accounts.list_metric_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="failover_priority_change">

Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists.

```sql
EXEC azure.cosmosdb.database_accounts.failover_priority_change 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"failoverPolicies": "{{ failoverPolicies }}"
}'
;
```
</TabItem>
<TabItem value="offline_region">

Offline the specified region for the specified Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.database_accounts.offline_region 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"region": "{{ region }}"
}'
;
```
</TabItem>
<TabItem value="online_region">

Online the specified region for the specified Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.database_accounts.online_region 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"region": "{{ region }}"
}'
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerates an access key for the specified Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.database_accounts.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyKind": "{{ keyKind }}"
}'
;
```
</TabItem>
<TabItem value="check_name_exists">

Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 50 characters.

```sql
EXEC azure.cosmosdb.database_accounts.check_name_exists 
@account_name='{{ account_name }}' --required
;
```
</TabItem>
</Tabs>
