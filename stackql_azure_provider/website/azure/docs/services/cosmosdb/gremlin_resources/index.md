--- 
title: gremlin_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - gremlin_resources
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

Creates, updates, deletes, gets or lists a <code>gremlin_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gremlin_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.gremlin_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_gremlin_graph_throughput"
    values={[
        { label: 'get_gremlin_graph_throughput', value: 'get_gremlin_graph_throughput' },
        { label: 'list_gremlin_graphs', value: 'list_gremlin_graphs' },
        { label: 'get_gremlin_role_definition', value: 'get_gremlin_role_definition' },
        { label: 'get_gremlin_role_assignment', value: 'get_gremlin_role_assignment' },
        { label: 'list_gremlin_databases', value: 'list_gremlin_databases' }
    ]}
>
<TabItem value="get_gremlin_graph_throughput">

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
<TabItem value="list_gremlin_graphs">

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
    <td>:vartype options: ~azure.mgmt.cosmosdb.models.GremlinGraphGetPropertiesOptions</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.GremlinGraphGetPropertiesResource</td>
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
<TabItem value="get_gremlin_role_definition">

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
    <td><CopyableCode code="assignableScopes" /></td>
    <td><code>array</code></td>
    <td>A set of fully qualified Scopes at or below which Gremlin Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>The set of operations allowed through this Role Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the Role Definition. Must be unique for the database account.</td>
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
<TabItem value="get_gremlin_role_assignment">

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
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Gremlin Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated Role Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The data plane resource path for which access is being granted through this Gremlin Role Assignment.</td>
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
<TabItem value="list_gremlin_databases">

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
    <td>:vartype options: ~azure.mgmt.cosmosdb.models.GremlinDatabaseGetPropertiesOptions</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.GremlinDatabaseGetPropertiesResource</td>
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
    <td><a href="#get_gremlin_graph_throughput"><CopyableCode code="get_gremlin_graph_throughput" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Gremlin graph throughput under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#list_gremlin_graphs"><CopyableCode code="list_gremlin_graphs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Gremlin graph under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#get_gremlin_role_definition"><CopyableCode code="get_gremlin_role_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB Gremlin Role Definition with the given Id.</td>
</tr>
<tr>
    <td><a href="#get_gremlin_role_assignment"><CopyableCode code="get_gremlin_role_assignment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB Gremlin Role Assignment with the given Id.</td>
</tr>
<tr>
    <td><a href="#list_gremlin_databases"><CopyableCode code="list_gremlin_databases" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Gremlin databases under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#create_update_gremlin_graph"><CopyableCode code="create_update_gremlin_graph" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB Gremlin graph.</td>
</tr>
<tr>
    <td><a href="#create_update_gremlin_database"><CopyableCode code="create_update_gremlin_database" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB Gremlin database.</td>
</tr>
<tr>
    <td><a href="#create_update_gremlin_role_definition"><CopyableCode code="create_update_gremlin_role_definition" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB Gremlin Role Definition.</td>
</tr>
<tr>
    <td><a href="#create_update_gremlin_role_assignment"><CopyableCode code="create_update_gremlin_role_assignment" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB Gremlin Role Assignment.</td>
</tr>
<tr>
    <td><a href="#update_gremlin_graph_throughput"><CopyableCode code="update_gremlin_graph_throughput" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update RUs per second of an Azure Cosmos DB Gremlin graph.</td>
</tr>
<tr>
    <td><a href="#update_gremlin_database_throughput"><CopyableCode code="update_gremlin_database_throughput" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update RUs per second of an Azure Cosmos DB Gremlin database.</td>
</tr>
<tr>
    <td><a href="#delete_gremlin_graph"><CopyableCode code="delete_gremlin_graph" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Gremlin graph.</td>
</tr>
<tr>
    <td><a href="#delete_gremlin_database"><CopyableCode code="delete_gremlin_database" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Gremlin database.</td>
</tr>
<tr>
    <td><a href="#delete_gremlin_role_definition"><CopyableCode code="delete_gremlin_role_definition" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Gremlin Role Definition.</td>
</tr>
<tr>
    <td><a href="#delete_gremlin_role_assignment"><CopyableCode code="delete_gremlin_role_assignment" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Gremlin Role Assignment.</td>
</tr>
<tr>
    <td><a href="#list_gremlin_role_definitions"><CopyableCode code="list_gremlin_role_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB Gremlin Role Definitions.</td>
</tr>
<tr>
    <td><a href="#list_gremlin_role_assignments"><CopyableCode code="list_gremlin_role_assignments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB Gremlin Role Assignments.</td>
</tr>
<tr>
    <td><a href="#get_gremlin_database_throughput"><CopyableCode code="get_gremlin_database_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#get_gremlin_database"><CopyableCode code="get_gremlin_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Gremlin databases under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#get_gremlin_graph"><CopyableCode code="get_gremlin_graph" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Gremlin graph under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#migrate_gremlin_database_to_autoscale"><CopyableCode code="migrate_gremlin_database_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Gremlin database from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_gremlin_database_to_manual_throughput"><CopyableCode code="migrate_gremlin_database_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Gremlin database from autoscale to manual throughput.</td>
</tr>
<tr>
    <td><a href="#migrate_gremlin_graph_to_autoscale"><CopyableCode code="migrate_gremlin_graph_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Gremlin graph from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_gremlin_graph_to_manual_throughput"><CopyableCode code="migrate_gremlin_graph_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Gremlin graph from autoscale to manual throughput.</td>
</tr>
<tr>
    <td><a href="#retrieve_continuous_backup_information"><CopyableCode code="retrieve_continuous_backup_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-graph_name"><code>graph_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves continuous backup information for a gremlin graph.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database name. Required.</td>
</tr>
<tr id="parameter-graph_name">
    <td><CopyableCode code="graph_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB graph name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-role_assignment_id">
    <td><CopyableCode code="role_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The GUID for the Role Assignment. Required.</td>
</tr>
<tr id="parameter-role_definition_id">
    <td><CopyableCode code="role_definition_id" /></td>
    <td><code>string</code></td>
    <td>The GUID for the Role Definition. Required.</td>
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
    defaultValue="get_gremlin_graph_throughput"
    values={[
        { label: 'get_gremlin_graph_throughput', value: 'get_gremlin_graph_throughput' },
        { label: 'list_gremlin_graphs', value: 'list_gremlin_graphs' },
        { label: 'get_gremlin_role_definition', value: 'get_gremlin_role_definition' },
        { label: 'get_gremlin_role_assignment', value: 'get_gremlin_role_assignment' },
        { label: 'list_gremlin_databases', value: 'list_gremlin_databases' }
    ]}
>
<TabItem value="get_gremlin_graph_throughput">

Gets the Gremlin graph throughput under an existing Azure Cosmos DB database account with the provided name.

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
FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND graph_name = '{{ graph_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_gremlin_graphs">

Lists the Gremlin graph under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_gremlin_role_definition">

Retrieves the properties of an existing Azure Cosmos DB Gremlin Role Definition with the given Id.

```sql
SELECT
id,
name,
assignableScopes,
permissions,
roleName,
systemData,
type
FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND role_definition_id = '{{ role_definition_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_gremlin_role_assignment">

Retrieves the properties of an existing Azure Cosmos DB Gremlin Role Assignment with the given Id.

```sql
SELECT
id,
name,
principalId,
provisioningState,
roleDefinitionId,
scope,
systemData,
type
FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND role_assignment_id = '{{ role_assignment_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_gremlin_databases">

Lists the Gremlin databases under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_update_gremlin_graph"
    values={[
        { label: 'create_update_gremlin_graph', value: 'create_update_gremlin_graph' },
        { label: 'create_update_gremlin_database', value: 'create_update_gremlin_database' },
        { label: 'create_update_gremlin_role_definition', value: 'create_update_gremlin_role_definition' },
        { label: 'create_update_gremlin_role_assignment', value: 'create_update_gremlin_role_assignment' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_update_gremlin_graph">

Create or update an Azure Cosmos DB Gremlin graph.

```sql
INSERT INTO azure.cosmosdb.gremlin_resources (
location,
tags,
identity,
properties,
resource_group_name,
account_name,
database_name,
graph_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ database_name }}',
'{{ graph_name }}',
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
<TabItem value="create_update_gremlin_database">

Create or update an Azure Cosmos DB Gremlin database.

```sql
INSERT INTO azure.cosmosdb.gremlin_resources (
location,
tags,
identity,
properties,
resource_group_name,
account_name,
database_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ database_name }}',
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
<TabItem value="create_update_gremlin_role_definition">

Creates or updates an Azure Cosmos DB Gremlin Role Definition.

```sql
INSERT INTO azure.cosmosdb.gremlin_resources (
properties,
resource_group_name,
account_name,
role_definition_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ role_definition_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_update_gremlin_role_assignment">

Creates or updates an Azure Cosmos DB Gremlin Role Assignment.

```sql
INSERT INTO azure.cosmosdb.gremlin_resources (
properties,
resource_group_name,
account_name,
role_assignment_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ role_assignment_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: gremlin_resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the gremlin_resources resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the gremlin_resources resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the gremlin_resources resource.
    - name: graph_name
      value: "{{ graph_name }}"
      description: Required parameter for the gremlin_resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the gremlin_resources resource.
    - name: role_definition_id
      value: "{{ role_definition_id }}"
      description: Required parameter for the gremlin_resources resource.
    - name: role_assignment_id
      value: "{{ role_assignment_id }}"
      description: Required parameter for the gremlin_resources resource.
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
    - name: properties
      description: |
        Properties to create and update an Azure Cosmos DB Gremlin Role Assignment.
      value:
        roleDefinitionId: "{{ roleDefinitionId }}"
        scope: "{{ scope }}"
        principalId: "{{ principalId }}"
        provisioningState: "{{ provisioningState }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_gremlin_graph_throughput"
    values={[
        { label: 'update_gremlin_graph_throughput', value: 'update_gremlin_graph_throughput' },
        { label: 'update_gremlin_database_throughput', value: 'update_gremlin_database_throughput' }
    ]}
>
<TabItem value="update_gremlin_graph_throughput">

Update RUs per second of an Azure Cosmos DB Gremlin graph.

```sql
UPDATE azure.cosmosdb.gremlin_resources
SET 
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND database_name = '{{ database_name }}' --required
AND graph_name = '{{ graph_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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
<TabItem value="update_gremlin_database_throughput">

Update RUs per second of an Azure Cosmos DB Gremlin database.

```sql
UPDATE azure.cosmosdb.gremlin_resources
SET 
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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
    defaultValue="delete_gremlin_graph"
    values={[
        { label: 'delete_gremlin_graph', value: 'delete_gremlin_graph' },
        { label: 'delete_gremlin_database', value: 'delete_gremlin_database' },
        { label: 'delete_gremlin_role_definition', value: 'delete_gremlin_role_definition' },
        { label: 'delete_gremlin_role_assignment', value: 'delete_gremlin_role_assignment' }
    ]}
>
<TabItem value="delete_gremlin_graph">

Deletes an existing Azure Cosmos DB Gremlin graph.

```sql
DELETE FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND database_name = '{{ database_name }}' --required
AND graph_name = '{{ graph_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_gremlin_database">

Deletes an existing Azure Cosmos DB Gremlin database.

```sql
DELETE FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_gremlin_role_definition">

Deletes an existing Azure Cosmos DB Gremlin Role Definition.

```sql
DELETE FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND role_definition_id = '{{ role_definition_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_gremlin_role_assignment">

Deletes an existing Azure Cosmos DB Gremlin Role Assignment.

```sql
DELETE FROM azure.cosmosdb.gremlin_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND role_assignment_id = '{{ role_assignment_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_gremlin_role_definitions"
    values={[
        { label: 'list_gremlin_role_definitions', value: 'list_gremlin_role_definitions' },
        { label: 'list_gremlin_role_assignments', value: 'list_gremlin_role_assignments' },
        { label: 'get_gremlin_database_throughput', value: 'get_gremlin_database_throughput' },
        { label: 'get_gremlin_database', value: 'get_gremlin_database' },
        { label: 'get_gremlin_graph', value: 'get_gremlin_graph' },
        { label: 'migrate_gremlin_database_to_autoscale', value: 'migrate_gremlin_database_to_autoscale' },
        { label: 'migrate_gremlin_database_to_manual_throughput', value: 'migrate_gremlin_database_to_manual_throughput' },
        { label: 'migrate_gremlin_graph_to_autoscale', value: 'migrate_gremlin_graph_to_autoscale' },
        { label: 'migrate_gremlin_graph_to_manual_throughput', value: 'migrate_gremlin_graph_to_manual_throughput' },
        { label: 'retrieve_continuous_backup_information', value: 'retrieve_continuous_backup_information' }
    ]}
>
<TabItem value="list_gremlin_role_definitions">

Retrieves the list of all Azure Cosmos DB Gremlin Role Definitions.

```sql
EXEC azure.cosmosdb.gremlin_resources.list_gremlin_role_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_gremlin_role_assignments">

Retrieves the list of all Azure Cosmos DB Gremlin Role Assignments.

```sql
EXEC azure.cosmosdb.gremlin_resources.list_gremlin_role_assignments 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_gremlin_database_throughput">

Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.gremlin_resources.get_gremlin_database_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_gremlin_database">

Gets the Gremlin databases under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.gremlin_resources.get_gremlin_database 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_gremlin_graph">

Gets the Gremlin graph under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.gremlin_resources.get_gremlin_graph 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@graph_name='{{ graph_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_gremlin_database_to_autoscale">

Migrate an Azure Cosmos DB Gremlin database from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.gremlin_resources.migrate_gremlin_database_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_gremlin_database_to_manual_throughput">

Migrate an Azure Cosmos DB Gremlin database from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.gremlin_resources.migrate_gremlin_database_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_gremlin_graph_to_autoscale">

Migrate an Azure Cosmos DB Gremlin graph from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.gremlin_resources.migrate_gremlin_graph_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@graph_name='{{ graph_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_gremlin_graph_to_manual_throughput">

Migrate an Azure Cosmos DB Gremlin graph from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.gremlin_resources.migrate_gremlin_graph_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@graph_name='{{ graph_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="retrieve_continuous_backup_information">

Retrieves continuous backup information for a gremlin graph.

```sql
EXEC azure.cosmosdb.gremlin_resources.retrieve_continuous_backup_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@graph_name='{{ graph_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}"
}'
;
```
</TabItem>
</Tabs>
