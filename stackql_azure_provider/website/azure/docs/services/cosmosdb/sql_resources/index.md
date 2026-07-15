--- 
title: sql_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_resources
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

Creates, updates, deletes, gets or lists a <code>sql_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.sql_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_sql_stored_procedure"
    values={[
        { label: 'get_sql_stored_procedure', value: 'get_sql_stored_procedure' },
        { label: 'get_sql_user_defined_function', value: 'get_sql_user_defined_function' },
        { label: 'get_sql_trigger', value: 'get_sql_trigger' },
        { label: 'list_sql_stored_procedures', value: 'list_sql_stored_procedures' },
        { label: 'get_client_encryption_key', value: 'get_client_encryption_key' },
        { label: 'list_client_encryption_keys', value: 'list_client_encryption_keys' },
        { label: 'get_sql_role_definition', value: 'get_sql_role_definition' },
        { label: 'get_sql_role_assignment', value: 'get_sql_role_assignment' },
        { label: 'list_sql_databases', value: 'list_sql_databases' }
    ]}
>
<TabItem value="get_sql_stored_procedure">

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
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.SqlStoredProcedureGetPropertiesResource</td>
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
<TabItem value="get_sql_user_defined_function">

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
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.SqlUserDefinedFunctionGetPropertiesResource</td>
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
<TabItem value="get_sql_trigger">

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
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.SqlTriggerGetPropertiesResource</td>
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
<TabItem value="list_sql_stored_procedures">

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
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.SqlStoredProcedureGetPropertiesResource</td>
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
<TabItem value="get_client_encryption_key">

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
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.ClientEncryptionKeyGetPropertiesResource</td>
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
<TabItem value="list_client_encryption_keys">

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
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.ClientEncryptionKeyGetPropertiesResource</td>
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
<TabItem value="get_sql_role_definition">

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
    <td>A set of fully qualified Scopes at or below which Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.</td>
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
<TabItem value="get_sql_role_assignment">

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
    <td>The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated Role Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The data plane resource path for which access is being granted through this Role Assignment.</td>
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
<TabItem value="list_sql_databases">

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
    <td>:vartype options: ~azure.mgmt.cosmosdb.models.SqlDatabaseGetPropertiesOptions</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>:vartype resource: ~azure.mgmt.cosmosdb.models.SqlDatabaseGetPropertiesResource</td>
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
    <td><a href="#get_sql_stored_procedure"><CopyableCode code="get_sql_stored_procedure" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-stored_procedure_name"><code>stored_procedure_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the SQL storedProcedure under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#get_sql_user_defined_function"><CopyableCode code="get_sql_user_defined_function" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-user_defined_function_name"><code>user_defined_function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#get_sql_trigger"><CopyableCode code="get_sql_trigger" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the SQL trigger under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_sql_stored_procedures"><CopyableCode code="list_sql_stored_procedures" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the SQL storedProcedure under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#get_client_encryption_key"><CopyableCode code="get_client_encryption_key" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-client_encryption_key_name"><code>client_encryption_key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the ClientEncryptionKey under an existing Azure Cosmos DB SQL database.</td>
</tr>
<tr>
    <td><a href="#list_client_encryption_keys"><CopyableCode code="list_client_encryption_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the ClientEncryptionKeys under an existing Azure Cosmos DB SQL database.</td>
</tr>
<tr>
    <td><a href="#get_sql_role_definition"><CopyableCode code="get_sql_role_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB SQL Role Definition with the given Id.</td>
</tr>
<tr>
    <td><a href="#get_sql_role_assignment"><CopyableCode code="get_sql_role_assignment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB SQL Role Assignment with the given Id.</td>
</tr>
<tr>
    <td><a href="#list_sql_databases"><CopyableCode code="list_sql_databases" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the SQL databases under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_sql_containers"><CopyableCode code="list_sql_containers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the SQL container under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_sql_user_defined_functions"><CopyableCode code="list_sql_user_defined_functions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the SQL userDefinedFunction under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_sql_triggers"><CopyableCode code="list_sql_triggers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the SQL trigger under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#list_sql_role_definitions"><CopyableCode code="list_sql_role_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB SQL Role Definitions.</td>
</tr>
<tr>
    <td><a href="#list_sql_role_assignments"><CopyableCode code="list_sql_role_assignments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB SQL Role Assignments.</td>
</tr>
<tr>
    <td><a href="#get_sql_database"><CopyableCode code="get_sql_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the SQL database under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#create_update_sql_database"><CopyableCode code="create_update_sql_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB SQL database.</td>
</tr>
<tr>
    <td><a href="#delete_sql_database"><CopyableCode code="delete_sql_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB SQL database.</td>
</tr>
<tr>
    <td><a href="#get_sql_database_throughput"><CopyableCode code="get_sql_database_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the RUs per second of the SQL database under an existing Azure Cosmos DB database account with the provided name.</td>
</tr>
<tr>
    <td><a href="#update_sql_database_throughput"><CopyableCode code="update_sql_database_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update RUs per second of an Azure Cosmos DB SQL database.</td>
</tr>
<tr>
    <td><a href="#get_sql_container_throughput"><CopyableCode code="get_sql_container_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the RUs per second of the SQL container under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#update_sql_container_throughput"><CopyableCode code="update_sql_container_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update RUs per second of an Azure Cosmos DB SQL container.</td>
</tr>
<tr>
    <td><a href="#create_update_client_encryption_key"><CopyableCode code="create_update_client_encryption_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-client_encryption_key_name"><code>client_encryption_key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a ClientEncryptionKey. This API is meant to be invoked via tools such as the Azure Powershell (instead of directly).</td>
</tr>
<tr>
    <td><a href="#get_sql_container"><CopyableCode code="get_sql_container" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the SQL container under an existing Azure Cosmos DB database account.</td>
</tr>
<tr>
    <td><a href="#create_update_sql_container"><CopyableCode code="create_update_sql_container" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB SQL container.</td>
</tr>
<tr>
    <td><a href="#delete_sql_container"><CopyableCode code="delete_sql_container" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB SQL container.</td>
</tr>
<tr>
    <td><a href="#create_update_sql_stored_procedure"><CopyableCode code="create_update_sql_stored_procedure" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-stored_procedure_name"><code>stored_procedure_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB SQL storedProcedure.</td>
</tr>
<tr>
    <td><a href="#delete_sql_stored_procedure"><CopyableCode code="delete_sql_stored_procedure" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-stored_procedure_name"><code>stored_procedure_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB SQL storedProcedure.</td>
</tr>
<tr>
    <td><a href="#create_update_sql_user_defined_function"><CopyableCode code="create_update_sql_user_defined_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-user_defined_function_name"><code>user_defined_function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB SQL userDefinedFunction.</td>
</tr>
<tr>
    <td><a href="#delete_sql_user_defined_function"><CopyableCode code="delete_sql_user_defined_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-user_defined_function_name"><code>user_defined_function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB SQL userDefinedFunction.</td>
</tr>
<tr>
    <td><a href="#create_update_sql_trigger"><CopyableCode code="create_update_sql_trigger" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an Azure Cosmos DB SQL trigger.</td>
</tr>
<tr>
    <td><a href="#delete_sql_trigger"><CopyableCode code="delete_sql_trigger" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB SQL trigger.</td>
</tr>
<tr>
    <td><a href="#create_update_sql_role_definition"><CopyableCode code="create_update_sql_role_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB SQL Role Definition.</td>
</tr>
<tr>
    <td><a href="#delete_sql_role_definition"><CopyableCode code="delete_sql_role_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB SQL Role Definition.</td>
</tr>
<tr>
    <td><a href="#create_update_sql_role_assignment"><CopyableCode code="create_update_sql_role_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB SQL Role Assignment.</td>
</tr>
<tr>
    <td><a href="#delete_sql_role_assignment"><CopyableCode code="delete_sql_role_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB SQL Role Assignment.</td>
</tr>
<tr>
    <td><a href="#migrate_sql_database_to_autoscale"><CopyableCode code="migrate_sql_database_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB SQL database from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_sql_database_to_manual_throughput"><CopyableCode code="migrate_sql_database_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB SQL database from autoscale to manual throughput.</td>
</tr>
<tr>
    <td><a href="#migrate_sql_container_to_autoscale"><CopyableCode code="migrate_sql_container_to_autoscale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB SQL container from manual throughput to autoscale.</td>
</tr>
<tr>
    <td><a href="#migrate_sql_container_to_manual_throughput"><CopyableCode code="migrate_sql_container_to_manual_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate an Azure Cosmos DB SQL container from autoscale to manual throughput.</td>
</tr>
<tr>
    <td><a href="#retrieve_continuous_backup_information"><CopyableCode code="retrieve_continuous_backup_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves continuous backup information for a container resource.</td>
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
<tr id="parameter-client_encryption_key_name">
    <td><CopyableCode code="client_encryption_key_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB ClientEncryptionKey name. Required.</td>
</tr>
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB container name. Required.</td>
</tr>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database name. Required.</td>
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
<tr id="parameter-stored_procedure_name">
    <td><CopyableCode code="stored_procedure_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB storedProcedure name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-trigger_name">
    <td><CopyableCode code="trigger_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB trigger name. Required.</td>
</tr>
<tr id="parameter-user_defined_function_name">
    <td><CopyableCode code="user_defined_function_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB userDefinedFunction name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_sql_stored_procedure"
    values={[
        { label: 'get_sql_stored_procedure', value: 'get_sql_stored_procedure' },
        { label: 'get_sql_user_defined_function', value: 'get_sql_user_defined_function' },
        { label: 'get_sql_trigger', value: 'get_sql_trigger' },
        { label: 'list_sql_stored_procedures', value: 'list_sql_stored_procedures' },
        { label: 'get_client_encryption_key', value: 'get_client_encryption_key' },
        { label: 'list_client_encryption_keys', value: 'list_client_encryption_keys' },
        { label: 'get_sql_role_definition', value: 'get_sql_role_definition' },
        { label: 'get_sql_role_assignment', value: 'get_sql_role_assignment' },
        { label: 'list_sql_databases', value: 'list_sql_databases' }
    ]}
>
<TabItem value="get_sql_stored_procedure">

Gets the SQL storedProcedure under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.sql_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND stored_procedure_name = '{{ stored_procedure_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_sql_user_defined_function">

Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.sql_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND user_defined_function_name = '{{ user_defined_function_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_sql_trigger">

Gets the SQL trigger under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.sql_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND trigger_name = '{{ trigger_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_sql_stored_procedures">

Lists the SQL storedProcedure under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.sql_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_client_encryption_key">

Gets the ClientEncryptionKey under an existing Azure Cosmos DB SQL database.

```sql
SELECT
id,
name,
resource,
systemData,
type
FROM azure.cosmosdb.sql_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND client_encryption_key_name = '{{ client_encryption_key_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_client_encryption_keys">

Lists the ClientEncryptionKeys under an existing Azure Cosmos DB SQL database.

```sql
SELECT
id,
name,
resource,
systemData,
type
FROM azure.cosmosdb.sql_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_sql_role_definition">

Retrieves the properties of an existing Azure Cosmos DB SQL Role Definition with the given Id.

```sql
SELECT
id,
name,
assignableScopes,
permissions,
roleName,
systemData,
type
FROM azure.cosmosdb.sql_resources
WHERE role_definition_id = '{{ role_definition_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_sql_role_assignment">

Retrieves the properties of an existing Azure Cosmos DB SQL Role Assignment with the given Id.

```sql
SELECT
id,
name,
principalId,
roleDefinitionId,
scope,
systemData,
type
FROM azure.cosmosdb.sql_resources
WHERE role_assignment_id = '{{ role_assignment_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_sql_databases">

Lists the SQL databases under an existing Azure Cosmos DB database account.

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
FROM azure.cosmosdb.sql_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_sql_containers"
    values={[
        { label: 'list_sql_containers', value: 'list_sql_containers' },
        { label: 'list_sql_user_defined_functions', value: 'list_sql_user_defined_functions' },
        { label: 'list_sql_triggers', value: 'list_sql_triggers' },
        { label: 'list_sql_role_definitions', value: 'list_sql_role_definitions' },
        { label: 'list_sql_role_assignments', value: 'list_sql_role_assignments' },
        { label: 'get_sql_database', value: 'get_sql_database' },
        { label: 'create_update_sql_database', value: 'create_update_sql_database' },
        { label: 'delete_sql_database', value: 'delete_sql_database' },
        { label: 'get_sql_database_throughput', value: 'get_sql_database_throughput' },
        { label: 'update_sql_database_throughput', value: 'update_sql_database_throughput' },
        { label: 'get_sql_container_throughput', value: 'get_sql_container_throughput' },
        { label: 'update_sql_container_throughput', value: 'update_sql_container_throughput' },
        { label: 'create_update_client_encryption_key', value: 'create_update_client_encryption_key' },
        { label: 'get_sql_container', value: 'get_sql_container' },
        { label: 'create_update_sql_container', value: 'create_update_sql_container' },
        { label: 'delete_sql_container', value: 'delete_sql_container' },
        { label: 'create_update_sql_stored_procedure', value: 'create_update_sql_stored_procedure' },
        { label: 'delete_sql_stored_procedure', value: 'delete_sql_stored_procedure' },
        { label: 'create_update_sql_user_defined_function', value: 'create_update_sql_user_defined_function' },
        { label: 'delete_sql_user_defined_function', value: 'delete_sql_user_defined_function' },
        { label: 'create_update_sql_trigger', value: 'create_update_sql_trigger' },
        { label: 'delete_sql_trigger', value: 'delete_sql_trigger' },
        { label: 'create_update_sql_role_definition', value: 'create_update_sql_role_definition' },
        { label: 'delete_sql_role_definition', value: 'delete_sql_role_definition' },
        { label: 'create_update_sql_role_assignment', value: 'create_update_sql_role_assignment' },
        { label: 'delete_sql_role_assignment', value: 'delete_sql_role_assignment' },
        { label: 'migrate_sql_database_to_autoscale', value: 'migrate_sql_database_to_autoscale' },
        { label: 'migrate_sql_database_to_manual_throughput', value: 'migrate_sql_database_to_manual_throughput' },
        { label: 'migrate_sql_container_to_autoscale', value: 'migrate_sql_container_to_autoscale' },
        { label: 'migrate_sql_container_to_manual_throughput', value: 'migrate_sql_container_to_manual_throughput' },
        { label: 'retrieve_continuous_backup_information', value: 'retrieve_continuous_backup_information' }
    ]}
>
<TabItem value="list_sql_containers">

Lists the SQL container under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.sql_resources.list_sql_containers 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sql_user_defined_functions">

Lists the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.sql_resources.list_sql_user_defined_functions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sql_triggers">

Lists the SQL trigger under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.sql_resources.list_sql_triggers 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sql_role_definitions">

Retrieves the list of all Azure Cosmos DB SQL Role Definitions.

```sql
EXEC azure.cosmosdb.sql_resources.list_sql_role_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sql_role_assignments">

Retrieves the list of all Azure Cosmos DB SQL Role Assignments.

```sql
EXEC azure.cosmosdb.sql_resources.list_sql_role_assignments 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_sql_database">

Gets the SQL database under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.sql_resources.get_sql_database 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_sql_database">

Create or update an Azure Cosmos DB SQL database.

```sql
EXEC azure.cosmosdb.sql_resources.create_update_sql_database 
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
<TabItem value="delete_sql_database">

Deletes an existing Azure Cosmos DB SQL database.

```sql
EXEC azure.cosmosdb.sql_resources.delete_sql_database 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_sql_database_throughput">

Gets the RUs per second of the SQL database under an existing Azure Cosmos DB database account with the provided name.

```sql
EXEC azure.cosmosdb.sql_resources.get_sql_database_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_sql_database_throughput">

Update RUs per second of an Azure Cosmos DB SQL database.

```sql
EXEC azure.cosmosdb.sql_resources.update_sql_database_throughput 
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
<TabItem value="get_sql_container_throughput">

Gets the RUs per second of the SQL container under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.sql_resources.get_sql_container_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_sql_container_throughput">

Update RUs per second of an Azure Cosmos DB SQL container.

```sql
EXEC azure.cosmosdb.sql_resources.update_sql_container_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
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
<TabItem value="create_update_client_encryption_key">

Create or update a ClientEncryptionKey. This API is meant to be invoked via tools such as the Azure Powershell (instead of directly).

```sql
EXEC azure.cosmosdb.sql_resources.create_update_client_encryption_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@client_encryption_key_name='{{ client_encryption_key_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_sql_container">

Gets the SQL container under an existing Azure Cosmos DB database account.

```sql
EXEC azure.cosmosdb.sql_resources.get_sql_container 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_sql_container">

Create or update an Azure Cosmos DB SQL container.

```sql
EXEC azure.cosmosdb.sql_resources.create_update_sql_container 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
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
<TabItem value="delete_sql_container">

Deletes an existing Azure Cosmos DB SQL container.

```sql
EXEC azure.cosmosdb.sql_resources.delete_sql_container 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_sql_stored_procedure">

Create or update an Azure Cosmos DB SQL storedProcedure.

```sql
EXEC azure.cosmosdb.sql_resources.create_update_sql_stored_procedure 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@stored_procedure_name='{{ stored_procedure_name }}' --required, 
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
<TabItem value="delete_sql_stored_procedure">

Deletes an existing Azure Cosmos DB SQL storedProcedure.

```sql
EXEC azure.cosmosdb.sql_resources.delete_sql_stored_procedure 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@stored_procedure_name='{{ stored_procedure_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_sql_user_defined_function">

Create or update an Azure Cosmos DB SQL userDefinedFunction.

```sql
EXEC azure.cosmosdb.sql_resources.create_update_sql_user_defined_function 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@user_defined_function_name='{{ user_defined_function_name }}' --required, 
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
<TabItem value="delete_sql_user_defined_function">

Deletes an existing Azure Cosmos DB SQL userDefinedFunction.

```sql
EXEC azure.cosmosdb.sql_resources.delete_sql_user_defined_function 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@user_defined_function_name='{{ user_defined_function_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_sql_trigger">

Create or update an Azure Cosmos DB SQL trigger.

```sql
EXEC azure.cosmosdb.sql_resources.create_update_sql_trigger 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
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
<TabItem value="delete_sql_trigger">

Deletes an existing Azure Cosmos DB SQL trigger.

```sql
EXEC azure.cosmosdb.sql_resources.delete_sql_trigger 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_sql_role_definition">

Creates or updates an Azure Cosmos DB SQL Role Definition.

```sql
EXEC azure.cosmosdb.sql_resources.create_update_sql_role_definition 
@role_definition_id='{{ role_definition_id }}' --required, 
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
<TabItem value="delete_sql_role_definition">

Deletes an existing Azure Cosmos DB SQL Role Definition.

```sql
EXEC azure.cosmosdb.sql_resources.delete_sql_role_definition 
@role_definition_id='{{ role_definition_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_update_sql_role_assignment">

Creates or updates an Azure Cosmos DB SQL Role Assignment.

```sql
EXEC azure.cosmosdb.sql_resources.create_update_sql_role_assignment 
@role_assignment_id='{{ role_assignment_id }}' --required, 
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
<TabItem value="delete_sql_role_assignment">

Deletes an existing Azure Cosmos DB SQL Role Assignment.

```sql
EXEC azure.cosmosdb.sql_resources.delete_sql_role_assignment 
@role_assignment_id='{{ role_assignment_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_sql_database_to_autoscale">

Migrate an Azure Cosmos DB SQL database from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.sql_resources.migrate_sql_database_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_sql_database_to_manual_throughput">

Migrate an Azure Cosmos DB SQL database from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.sql_resources.migrate_sql_database_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_sql_container_to_autoscale">

Migrate an Azure Cosmos DB SQL container from manual throughput to autoscale.

```sql
EXEC azure.cosmosdb.sql_resources.migrate_sql_container_to_autoscale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_sql_container_to_manual_throughput">

Migrate an Azure Cosmos DB SQL container from autoscale to manual throughput.

```sql
EXEC azure.cosmosdb.sql_resources.migrate_sql_container_to_manual_throughput 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="retrieve_continuous_backup_information">

Retrieves continuous backup information for a container resource.

```sql
EXEC azure.cosmosdb.sql_resources.retrieve_continuous_backup_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}"
}'
;
```
</TabItem>
</Tabs>
