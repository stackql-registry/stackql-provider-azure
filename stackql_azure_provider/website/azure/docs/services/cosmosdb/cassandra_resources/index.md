--- 
title: cassandra_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_resources
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

Creates, updates, deletes, gets or lists a <code>cassandra_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cassandra_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.cassandra_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_cassandra_table_throughput"
    values={[
        { label: 'get_cassandra_table_throughput', value: 'get_cassandra_table_throughput' },
        { label: 'list_cassandra_tables', value: 'list_cassandra_tables' },
        { label: 'get_cassandra_role_definition', value: 'get_cassandra_role_definition' },
        { label: 'get_cassandra_role_assignment', value: 'get_cassandra_role_assignment' },
        { label: 'list_cassandra_keyspaces', value: 'list_cassandra_keyspaces' }
    ]}
>
<TabItem value="get_cassandra_table_throughput">

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
<TabItem value="list_cassandra_tables">

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
    <td>:vartype options: ~azure.mgmt.cosmosdb.models.CassandraTableGetPropertiesOptions</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.CassandraTableGetPropertiesResource</td>
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
<TabItem value="get_cassandra_role_definition">

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
    <td>A set of fully qualified Scopes at or below which Cassandra Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.</td>
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
<TabItem value="get_cassandra_role_assignment">

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
    <td>The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Cassandra Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.</td>
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
    <td>The data plane resource path for which access is being granted through this Cassandra Role Assignment.</td>
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
<TabItem value="list_cassandra_keyspaces">

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
    <td>:vartype options: ~azure.mgmt.cosmosdb.models.CassandraKeyspaceGetPropertiesOptions</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.CassandraKeyspaceGetPropertiesResource</td>
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
    <td><a href="#get_cassandra_table_throughput"><CopyableCode code="get_cassandra_table_throughput" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the RUs per second of the Cassandra table under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#list_cassandra_tables"><CopyableCode code="list_cassandra_tables" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Cassandra table under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#get_cassandra_role_definition"><CopyableCode code="get_cassandra_role_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB Cassandra Role Definition with the given Id.</td>
</tr>
<tr>
    <td><a href="#get_cassandra_role_assignment"><CopyableCode code="get_cassandra_role_assignment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB Cassandra Role Assignment with the given Id.</td>
</tr>
<tr>
    <td><a href="#list_cassandra_keyspaces"><CopyableCode code="list_cassandra_keyspaces" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Cassandra keyspaces under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_cassandra_role_definitions"><CopyableCode code="list_cassandra_role_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB Cassandra Role Definitions.</td>
</tr>
<tr>
    <td><a href="#list_cassandra_role_assignments"><CopyableCode code="list_cassandra_role_assignments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB Cassandra Role Assignments.</td>
</tr>
<tr>
    <td><a href="#get_cassandra_keyspace_throughput"><CopyableCode code="get_cassandra_keyspace_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the RUs per second of the Cassandra Keyspace under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#update_cassandra_keyspace_throughput"><CopyableCode code="update_cassandra_keyspace_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update RUs per second of an Azure Cosmos DB Cassandra Keyspace.</td>
</tr>
<tr>
    <td><a href="#update_cassandra_table_throughput"><CopyableCode code="update_cassandra_table_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update RUs per second of an Azure Cosmos DB Cassandra table.</td>
</tr>
<tr>
    <td><a href="#get_cassandra_keyspace"><CopyableCode code="get_cassandra_keyspace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Cassandra keyspaces under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#create_update_cassandra_keyspace"><CopyableCode code="create_update_cassandra_keyspace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB Cassandra keyspace.</td>
</tr>
<tr>
    <td><a href="#delete_cassandra_keyspace"><CopyableCode code="delete_cassandra_keyspace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Cassandra keyspace.</td>
</tr>
<tr>
    <td><a href="#get_cassandra_table"><CopyableCode code="get_cassandra_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Cassandra table under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#create_update_cassandra_table"><CopyableCode code="create_update_cassandra_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB Cassandra Table.</td>
</tr>
<tr>
    <td><a href="#delete_cassandra_table"><CopyableCode code="delete_cassandra_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Cassandra table.</td>
</tr>
<tr>
    <td><a href="#create_update_cassandra_role_definition"><CopyableCode code="create_update_cassandra_role_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB Cassandra Role Definition.</td>
</tr>
<tr>
    <td><a href="#delete_cassandra_role_definition"><CopyableCode code="delete_cassandra_role_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Cassandra Role Definition.</td>
</tr>
<tr>
    <td><a href="#create_update_cassandra_role_assignment"><CopyableCode code="create_update_cassandra_role_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB Cassandra Role Assignment.</td>
</tr>
<tr>
    <td><a href="#delete_cassandra_role_assignment"><CopyableCode code="delete_cassandra_role_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB Cassandra Role Assignment.</td>
</tr>
<tr>
    <td><a href="#migrate_cassandra_keyspace_to_autoscale"><CopyableCode code="migrate_cassandra_keyspace_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Cassandra Keyspace from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_cassandra_keyspace_to_manual_throughput"><CopyableCode code="migrate_cassandra_keyspace_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Cassandra Keyspace from autoscale to manual throughput.</td>
</tr>
<tr>
    <td><a href="#migrate_cassandra_table_to_autoscale"><CopyableCode code="migrate_cassandra_table_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Cassandra table from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_cassandra_table_to_manual_throughput"><CopyableCode code="migrate_cassandra_table_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-keyspace_name"><code>keyspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB Cassandra table from autoscale to manual throughput.</td>
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
<tr id="parameter-keyspace_name">
    <td><CopyableCode code="keyspace_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB keyspace name. Required.</td>
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
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB table name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_cassandra_table_throughput"
    values={[
        { label: 'get_cassandra_table_throughput', value: 'get_cassandra_table_throughput' },
        { label: 'list_cassandra_tables', value: 'list_cassandra_tables' },
        { label: 'get_cassandra_role_definition', value: 'get_cassandra_role_definition' },
        { label: 'get_cassandra_role_assignment', value: 'get_cassandra_role_assignment' },
        { label: 'list_cassandra_keyspaces', value: 'list_cassandra_keyspaces' }
    ]}
>
<TabItem value="get_cassandra_table_throughput">

Gets the RUs per second of the Cassandra table under an existing Azure Cosmos DB database account with the provided name.

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
FROM azure.cosmosdb.cassandra_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND keyspace_name = '{{ keyspace_name }}' -- required
AND table_name = '{{ table_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_cassandra_tables">

Lists the Cassandra table under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.cassandra_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND keyspace_name = '{{ keyspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_cassandra_role_definition">

Retrieves the properties of an existing Azure Cosmos DB Cassandra Role Definition with the given Id.

```sql
SELECT
id,
name,
assignableScopes,
permissions,
roleName,
systemData,
type
FROM azure.cosmosdb.cassandra_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND role_definition_id = '{{ role_definition_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_cassandra_role_assignment">

Retrieves the properties of an existing Azure Cosmos DB Cassandra Role Assignment with the given Id.

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
FROM azure.cosmosdb.cassandra_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND role_assignment_id = '{{ role_assignment_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_cassandra_keyspaces">

Lists the Cassandra keyspaces under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.cassandra_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_cassandra_role_definitions"
    values={[
        { label: 'list_cassandra_role_definitions', value: 'list_cassandra_role_definitions' },
        { label: 'list_cassandra_role_assignments', value: 'list_cassandra_role_assignments' },
        { label: 'get_cassandra_keyspace_throughput', value: 'get_cassandra_keyspace_throughput' },
        { label: 'update_cassandra_keyspace_throughput', value: 'update_cassandra_keyspace_throughput' },
        { label: 'update_cassandra_table_throughput', value: 'update_cassandra_table_throughput' },
        { label: 'get_cassandra_keyspace', value: 'get_cassandra_keyspace' },
        { label: 'create_update_cassandra_keyspace', value: 'create_update_cassandra_keyspace' },
        { label: 'delete_cassandra_keyspace', value: 'delete_cassandra_keyspace' },
        { label: 'get_cassandra_table', value: 'get_cassandra_table' },
        { label: 'create_update_cassandra_table', value: 'create_update_cassandra_table' },
        { label: 'delete_cassandra_table', value: 'delete_cassandra_table' },
        { label: 'create_update_cassandra_role_definition', value: 'create_update_cassandra_role_definition' },
        { label: 'delete_cassandra_role_definition', value: 'delete_cassandra_role_definition' },
        { label: 'create_update_cassandra_role_assignment', value: 'create_update_cassandra_role_assignment' },
        { label: 'delete_cassandra_role_assignment', value: 'delete_cassandra_role_assignment' },
        { label: 'migrate_cassandra_keyspace_to_autoscale', value: 'migrate_cassandra_keyspace_to_autoscale' },
        { label: 'migrate_cassandra_keyspace_to_manual_throughput', value: 'migrate_cassandra_keyspace_to_manual_throughput' },
        { label: 'migrate_cassandra_table_to_autoscale', value: 'migrate_cassandra_table_to_autoscale' },
        { label: 'migrate_cassandra_table_to_manual_throughput', value: 'migrate_cassandra_table_to_manual_throughput' }
    ]}
>
<TabItem value="list_cassandra_role_definitions">

Retrieves the list of all Azure Cosmos DB Cassandra Role Definitions.

```sql
EXEC azure.cosmosdb.cassandra_resources.list_cassandra_role_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_cassandra_role_assignments">

Retrieves the list of all Azure Cosmos DB Cassandra Role Assignments.

```sql
EXEC azure.cosmosdb.cassandra_resources.list_cassandra_role_assignments 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_cassandra_keyspace_throughput">

Gets the RUs per second of the Cassandra Keyspace under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.cassandra_resources.get_cassandra_keyspace_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_cassandra_keyspace_throughput">

Update RUs per second of an Azure Cosmos DB Cassandra Keyspace.

```sql
EXEC azure.cosmosdb.cassandra_resources.update_cassandra_keyspace_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
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
<TabItem value="update_cassandra_table_throughput">

Update RUs per second of an Azure Cosmos DB Cassandra table.

```sql
EXEC azure.cosmosdb.cassandra_resources.update_cassandra_table_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
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
<TabItem value="get_cassandra_keyspace">

Gets the Cassandra keyspaces under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.cassandra_resources.get_cassandra_keyspace 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_cassandra_keyspace">

Create or update an Azure Cosmos DB Cassandra keyspace.

```sql
EXEC azure.cosmosdb.cassandra_resources.create_update_cassandra_keyspace 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
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
<TabItem value="delete_cassandra_keyspace">

Deletes an existing Azure Cosmos DB Cassandra keyspace.

```sql
EXEC azure.cosmosdb.cassandra_resources.delete_cassandra_keyspace 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_cassandra_table">

Gets the Cassandra table under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.cassandra_resources.get_cassandra_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_cassandra_table">

Create or update an Azure Cosmos DB Cassandra Table.

```sql
EXEC azure.cosmosdb.cassandra_resources.create_update_cassandra_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
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
<TabItem value="delete_cassandra_table">

Deletes an existing Azure Cosmos DB Cassandra table.

```sql
EXEC azure.cosmosdb.cassandra_resources.delete_cassandra_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_cassandra_role_definition">

Creates or updates an Azure Cosmos DB Cassandra Role Definition.

```sql
EXEC azure.cosmosdb.cassandra_resources.create_update_cassandra_role_definition 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@role_definition_id='{{ role_definition_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_cassandra_role_definition">

Deletes an existing Azure Cosmos DB Cassandra Role Definition.

```sql
EXEC azure.cosmosdb.cassandra_resources.delete_cassandra_role_definition 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@role_definition_id='{{ role_definition_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_cassandra_role_assignment">

Creates or updates an Azure Cosmos DB Cassandra Role Assignment.

```sql
EXEC azure.cosmosdb.cassandra_resources.create_update_cassandra_role_assignment 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@role_assignment_id='{{ role_assignment_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_cassandra_role_assignment">

Deletes an existing Azure Cosmos DB Cassandra Role Assignment.

```sql
EXEC azure.cosmosdb.cassandra_resources.delete_cassandra_role_assignment 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@role_assignment_id='{{ role_assignment_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_cassandra_keyspace_to_autoscale">

Migrate an Azure Cosmos DB Cassandra Keyspace from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.cassandra_resources.migrate_cassandra_keyspace_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_cassandra_keyspace_to_manual_throughput">

Migrate an Azure Cosmos DB Cassandra Keyspace from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.cassandra_resources.migrate_cassandra_keyspace_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_cassandra_table_to_autoscale">

Migrate an Azure Cosmos DB Cassandra table from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.cassandra_resources.migrate_cassandra_table_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_cassandra_table_to_manual_throughput">

Migrate an Azure Cosmos DB Cassandra table from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.cassandra_resources.migrate_cassandra_table_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@keyspace_name='{{ keyspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
