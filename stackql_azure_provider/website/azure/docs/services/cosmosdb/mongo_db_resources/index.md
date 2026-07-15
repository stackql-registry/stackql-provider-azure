--- 
title: mongo_db_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_db_resources
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

Creates, updates, deletes, gets or lists a <code>mongo_db_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mongo_db_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.mongo_db_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_mongo_db_collection_throughput"
    values={[
        { label: 'get_mongo_db_collection_throughput', value: 'get_mongo_db_collection_throughput' },
        { label: 'list_mongo_db_collections', value: 'list_mongo_db_collections' },
        { label: 'get_mongo_role_definition', value: 'get_mongo_role_definition' },
        { label: 'get_mongo_user_definition', value: 'get_mongo_user_definition' },
        { label: 'list_mongo_db_databases', value: 'list_mongo_db_databases' }
    ]}
>
<TabItem value="get_mongo_db_collection_throughput">

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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.ThroughputSettingsGetPropertiesResource</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_mongo_db_collections">

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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>object</code></td>
    <td>:vartype options: ~azure.mgmt.cosmosdb.models.MongoDBCollectionGetPropertiesOptions</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.MongoDBCollectionGetPropertiesResource</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="get_mongo_role_definition">

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
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The database name for which access is being granted for this Role Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="privileges" /></td>
    <td><code>array</code></td>
    <td>A set of privileges contained by the Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Scopes higher than Database are not enforceable as privilege.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the Role Definition. Must be unique for the database account.</td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>The set of roles inherited by this Role Definition.</td>
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
<TabItem value="get_mongo_user_definition">

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
    <td><CopyableCode code="customData" /></td>
    <td><code>string</code></td>
    <td>A custom definition for the USer Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The database name for which access is being granted for this User Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="mechanisms" /></td>
    <td><code>string</code></td>
    <td>The Mongo Auth mechanism. For now, we only support auth mechanism SCRAM-SHA-256.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>The password for User Definition. Response does not contain user password.</td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>The set of roles inherited by the User Definition.</td>
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
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>The user name for User Definition.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_mongo_db_databases">

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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>object</code></td>
    <td>:vartype options: ~azure.mgmt.cosmosdb.models.MongoDBDatabaseGetPropertiesOptions</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.MongoDBDatabaseGetPropertiesResource</td>
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
    <td><a href="#get_mongo_db_collection_throughput"><CopyableCode code="get_mongo_db_collection_throughput" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the RUs per second of the MongoDB collection under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#list_mongo_db_collections"><CopyableCode code="list_mongo_db_collections" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the MongoDB collection under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#get_mongo_role_definition"><CopyableCode code="get_mongo_role_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-mongo_role_definition_id"><code>mongo_role_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB Mongo Role Definition with the given Id.</td>
</tr>
<tr>
    <td><a href="#get_mongo_user_definition"><CopyableCode code="get_mongo_user_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-mongo_user_definition_id"><code>mongo_user_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB Mongo User Definition with the given Id.</td>
</tr>
<tr>
    <td><a href="#list_mongo_db_databases"><CopyableCode code="list_mongo_db_databases" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the MongoDB databases under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_mongo_role_definitions"><CopyableCode code="list_mongo_role_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB Mongo Role Definitions.</td>
</tr>
<tr>
    <td><a href="#list_mongo_user_definitions"><CopyableCode code="list_mongo_user_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB Mongo User Definition.</td>
</tr>
<tr>
    <td><a href="#get_mongo_db_database_throughput"><CopyableCode code="get_mongo_db_database_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the RUs per second of the MongoDB database under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#update_mongo_db_database_throughput"><CopyableCode code="update_mongo_db_database_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update RUs per second of the an Azure Cosmos DB MongoDB database.</td>
</tr>
<tr>
    <td><a href="#update_mongo_db_collection_throughput"><CopyableCode code="update_mongo_db_collection_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update the RUs per second of an Azure Cosmos DB MongoDB collection.</td>
</tr>
<tr>
    <td><a href="#get_mongo_db_database"><CopyableCode code="get_mongo_db_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the MongoDB databases under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#create_update_mongo_db_database"><CopyableCode code="create_update_mongo_db_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or updates Azure Cosmos DB MongoDB database.</td>
</tr>
<tr>
    <td><a href="#delete_mongo_db_database"><CopyableCode code="delete_mongo_db_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB MongoDB database.</td>
</tr>
<tr>
    <td><a href="#get_mongo_db_collection"><CopyableCode code="get_mongo_db_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the MongoDB collection under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#create_update_mongo_db_collection"><CopyableCode code="create_update_mongo_db_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB MongoDB Collection.</td>
</tr>
<tr>
    <td><a href="#delete_mongo_db_collection"><CopyableCode code="delete_mongo_db_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB MongoDB Collection.</td>
</tr>
<tr>
    <td><a href="#create_update_mongo_role_definition"><CopyableCode code="create_update_mongo_role_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-mongo_role_definition_id"><code>mongo_role_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB Mongo Role Definition.</td>
</tr>
<tr>
    <td><a href="#delete_mongo_role_definition"><CopyableCode code="delete_mongo_role_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-mongo_role_definition_id"><code>mongo_role_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Mongo Role Definition.</td>
</tr>
<tr>
    <td><a href="#create_update_mongo_user_definition"><CopyableCode code="create_update_mongo_user_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-mongo_user_definition_id"><code>mongo_user_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB Mongo User Definition.</td>
</tr>
<tr>
    <td><a href="#delete_mongo_user_definition"><CopyableCode code="delete_mongo_user_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-mongo_user_definition_id"><code>mongo_user_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Mongo User Definition.</td>
</tr>
<tr>
    <td><a href="#migrate_mongo_db_database_to_autoscale"><CopyableCode code="migrate_mongo_db_database_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB MongoDB database from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_mongo_db_database_to_manual_throughput"><CopyableCode code="migrate_mongo_db_database_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB MongoDB database from autoscale to manual throughput.</td>
</tr>
<tr>
    <td><a href="#migrate_mongo_db_collection_to_autoscale"><CopyableCode code="migrate_mongo_db_collection_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB MongoDB collection from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_mongo_db_collection_to_manual_throughput"><CopyableCode code="migrate_mongo_db_collection_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB MongoDB collection from autoscale to manual throughput.</td>
</tr>
<tr>
    <td><a href="#retrieve_continuous_backup_information"><CopyableCode code="retrieve_continuous_backup_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-collection_name"><code>collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves continuous backup information for a Mongodb collection.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database account name. Required.</td>
</tr>
<tr id="parameter-collection_name">
    <td><CopyableCode code="collection_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB collection name. Required.</td>
</tr>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database name. Required.</td>
</tr>
<tr id="parameter-mongo_role_definition_id">
    <td><CopyableCode code="mongo_role_definition_id" /></td>
    <td><code>string</code></td>
    <td>The ID for the Role Definition &#123;dbName.roleName&#125;. Required.</td>
</tr>
<tr id="parameter-mongo_user_definition_id">
    <td><CopyableCode code="mongo_user_definition_id" /></td>
    <td><code>string</code></td>
    <td>The ID for the User Definition &#123;dbName.userName&#125;. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_mongo_db_collection_throughput"
    values={[
        { label: 'get_mongo_db_collection_throughput', value: 'get_mongo_db_collection_throughput' },
        { label: 'list_mongo_db_collections', value: 'list_mongo_db_collections' },
        { label: 'get_mongo_role_definition', value: 'get_mongo_role_definition' },
        { label: 'get_mongo_user_definition', value: 'get_mongo_user_definition' },
        { label: 'list_mongo_db_databases', value: 'list_mongo_db_databases' }
    ]}
>
<TabItem value="get_mongo_db_collection_throughput">

Gets the RUs per second of the MongoDB collection under an existing Azure Cosmos DB database account with the provided name.

```sql
SELECT
id,
name,
identity,
location,
resource,
systemData,
tags,
type
FROM azure.cosmosdb.mongo_db_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND collection_name = '{{ collection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_mongo_db_collections">

Lists the MongoDB collection under an existing Azure Cosmos DB database account.

```sql
SELECT
id,
name,
identity,
location,
options,
resource,
systemData,
tags,
type
FROM azure.cosmosdb.mongo_db_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_mongo_role_definition">

Retrieves the properties of an existing Azure Cosmos DB Mongo Role Definition with the given Id.

```sql
SELECT
id,
name,
databaseName,
privileges,
roleName,
roles,
systemData,
type
FROM azure.cosmosdb.mongo_db_resources
WHERE mongo_role_definition_id = '{{ mongo_role_definition_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_mongo_user_definition">

Retrieves the properties of an existing Azure Cosmos DB Mongo User Definition with the given Id.

```sql
SELECT
id,
name,
customData,
databaseName,
mechanisms,
password,
roles,
systemData,
type,
userName
FROM azure.cosmosdb.mongo_db_resources
WHERE mongo_user_definition_id = '{{ mongo_user_definition_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_mongo_db_databases">

Lists the MongoDB databases under an existing Azure Cosmos DB database account.

```sql
SELECT
id,
name,
identity,
location,
options,
resource,
systemData,
tags,
type
FROM azure.cosmosdb.mongo_db_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_mongo_role_definitions"
    values={[
        { label: 'list_mongo_role_definitions', value: 'list_mongo_role_definitions' },
        { label: 'list_mongo_user_definitions', value: 'list_mongo_user_definitions' },
        { label: 'get_mongo_db_database_throughput', value: 'get_mongo_db_database_throughput' },
        { label: 'update_mongo_db_database_throughput', value: 'update_mongo_db_database_throughput' },
        { label: 'update_mongo_db_collection_throughput', value: 'update_mongo_db_collection_throughput' },
        { label: 'get_mongo_db_database', value: 'get_mongo_db_database' },
        { label: 'create_update_mongo_db_database', value: 'create_update_mongo_db_database' },
        { label: 'delete_mongo_db_database', value: 'delete_mongo_db_database' },
        { label: 'get_mongo_db_collection', value: 'get_mongo_db_collection' },
        { label: 'create_update_mongo_db_collection', value: 'create_update_mongo_db_collection' },
        { label: 'delete_mongo_db_collection', value: 'delete_mongo_db_collection' },
        { label: 'create_update_mongo_role_definition', value: 'create_update_mongo_role_definition' },
        { label: 'delete_mongo_role_definition', value: 'delete_mongo_role_definition' },
        { label: 'create_update_mongo_user_definition', value: 'create_update_mongo_user_definition' },
        { label: 'delete_mongo_user_definition', value: 'delete_mongo_user_definition' },
        { label: 'migrate_mongo_db_database_to_autoscale', value: 'migrate_mongo_db_database_to_autoscale' },
        { label: 'migrate_mongo_db_database_to_manual_throughput', value: 'migrate_mongo_db_database_to_manual_throughput' },
        { label: 'migrate_mongo_db_collection_to_autoscale', value: 'migrate_mongo_db_collection_to_autoscale' },
        { label: 'migrate_mongo_db_collection_to_manual_throughput', value: 'migrate_mongo_db_collection_to_manual_throughput' },
        { label: 'retrieve_continuous_backup_information', value: 'retrieve_continuous_backup_information' }
    ]}
>
<TabItem value="list_mongo_role_definitions">

Retrieves the list of all Azure Cosmos DB Mongo Role Definitions.

```sql
EXEC azure.cosmosdb.mongo_db_resources.list_mongo_role_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_mongo_user_definitions">

Retrieves the list of all Azure Cosmos DB Mongo User Definition.

```sql
EXEC azure.cosmosdb.mongo_db_resources.list_mongo_user_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_mongo_db_database_throughput">

Gets the RUs per second of the MongoDB database under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.mongo_db_resources.get_mongo_db_database_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_mongo_db_database_throughput">

Update RUs per second of the an Azure Cosmos DB MongoDB database.

```sql
EXEC azure.cosmosdb.mongo_db_resources.update_mongo_db_database_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_mongo_db_collection_throughput">

Update the RUs per second of an Azure Cosmos DB MongoDB collection.

```sql
EXEC azure.cosmosdb.mongo_db_resources.update_mongo_db_collection_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@collection_name='{{ collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_mongo_db_database">

Gets the MongoDB databases under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.mongo_db_resources.get_mongo_db_database 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_mongo_db_database">

Create or updates Azure Cosmos DB MongoDB database.

```sql
EXEC azure.cosmosdb.mongo_db_resources.create_update_mongo_db_database 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_mongo_db_database">

Deletes an existing Azure Cosmos DB MongoDB database.

```sql
EXEC azure.cosmosdb.mongo_db_resources.delete_mongo_db_database 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_mongo_db_collection">

Gets the MongoDB collection under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.mongo_db_resources.get_mongo_db_collection 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@collection_name='{{ collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_mongo_db_collection">

Create or update an Azure Cosmos DB MongoDB Collection.

```sql
EXEC azure.cosmosdb.mongo_db_resources.create_update_mongo_db_collection 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@collection_name='{{ collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_mongo_db_collection">

Deletes an existing Azure Cosmos DB MongoDB Collection.

```sql
EXEC azure.cosmosdb.mongo_db_resources.delete_mongo_db_collection 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@collection_name='{{ collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_mongo_role_definition">

Creates or updates an Azure Cosmos DB Mongo Role Definition.

```sql
EXEC azure.cosmosdb.mongo_db_resources.create_update_mongo_role_definition 
@mongo_role_definition_id='{{ mongo_role_definition_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_mongo_role_definition">

Deletes an existing Azure Cosmos DB Mongo Role Definition.

```sql
EXEC azure.cosmosdb.mongo_db_resources.delete_mongo_role_definition 
@mongo_role_definition_id='{{ mongo_role_definition_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_mongo_user_definition">

Creates or updates an Azure Cosmos DB Mongo User Definition.

```sql
EXEC azure.cosmosdb.mongo_db_resources.create_update_mongo_user_definition 
@mongo_user_definition_id='{{ mongo_user_definition_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_mongo_user_definition">

Deletes an existing Azure Cosmos DB Mongo User Definition.

```sql
EXEC azure.cosmosdb.mongo_db_resources.delete_mongo_user_definition 
@mongo_user_definition_id='{{ mongo_user_definition_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_mongo_db_database_to_autoscale">

Migrate an Azure Cosmos DB MongoDB database from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.mongo_db_resources.migrate_mongo_db_database_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_mongo_db_database_to_manual_throughput">

Migrate an Azure Cosmos DB MongoDB database from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.mongo_db_resources.migrate_mongo_db_database_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_mongo_db_collection_to_autoscale">

Migrate an Azure Cosmos DB MongoDB collection from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.mongo_db_resources.migrate_mongo_db_collection_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@collection_name='{{ collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_mongo_db_collection_to_manual_throughput">

Migrate an Azure Cosmos DB MongoDB collection from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.mongo_db_resources.migrate_mongo_db_collection_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@collection_name='{{ collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="retrieve_continuous_backup_information">

Retrieves continuous backup information for a Mongodb collection.

```sql
EXEC azure.cosmosdb.mongo_db_resources.retrieve_continuous_backup_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@collection_name='{{ collection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}"
}'
;
```
</TabItem>
</Tabs>
