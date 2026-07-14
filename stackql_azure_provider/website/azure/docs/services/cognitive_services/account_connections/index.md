--- 
title: account_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - account_connections
  - cognitive_services
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

Creates, updates, deletes, gets or lists an <code>account_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.account_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>Authentication type of the connection target. Required. Known values are: "PAT", "ManagedIdentity", "UsernamePassword", "None", "SAS", "AccountKey", "ServicePrincipal", "AccessKey", "ApiKey", "CustomKeys", "OAuth2", "AAD", "DelegatedSAS", "ProjectManagedIdentity", "AccountManagedIdentity", "UserEntraToken", "AgentUserImpersonation", "AgenticIdentityToken", and "AgenticUser".</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of the connection. Known values are: "PythonFeed", "ContainerRegistry", "Git", "S3", "Snowflake", "AzureKeyVault", "AzureSqlDb", "AzureSynapseAnalytics", "AzureMySqlDb", "AzurePostgresDb", "ADLSGen2", "AzureContainerAppEnvironment", "Redis", "ApiKey", "AzureOpenAI", "AIServices", "CognitiveSearch", "CognitiveService", "CustomKeys", "AzureBlob", "AzureStorageAccount", "AzureOneLake", "CosmosDb", "CosmosDbMongoDbApi", "AzureDataExplorer", "AzureMariaDb", "AzureDatabricksDeltaLake", "AzureSqlMi", "AzureTableStorage", "AmazonRdsForOracle", "AmazonRdsForSqlServer", "AmazonRedshift", "Db2", "Drill", "GoogleBigQuery", "Greenplum", "Hbase", "Hive", "Impala", "Informix", "MariaDb", "MicrosoftAccess", "MySql", "Netezza", "Oracle", "Phoenix", "PostgreSql", "Presto", "SapOpenHub", "SapBw", "SapHana", "SapTable", "Spark", "SqlServer", "Sybase", "Teradata", "Vertica", "Pinecone", "Databricks", "Cassandra", "Couchbase", "MongoDbV2", "MongoDbAtlas", "AmazonS3Compatible", "FileServer", "FtpServer", "GoogleCloudStorage", "Hdfs", "OracleCloudStorage", "Sftp", "GenericHttp", "ODataRest", "Odbc", "GenericRest", "RemoteTool", "AmazonMws", "Concur", "Dynamics", "DynamicsAx", "DynamicsCrm", "GoogleAdWords", "Hubspot", "Jira", "Magento", "Marketo", "Office365", "Eloqua", "Responsys", "OracleServiceCloud", "PayPal", "QuickBooks", "Salesforce", "SalesforceServiceCloud", "SalesforceMarketingCloud", "SapCloudForCustomer", "SapEcc", "ServiceNow", "SharePointOnlineList", "Shopify", "Square", "WebTable", "Xero", "Zoho", "GenericContainerRegistry", "Elasticsearch", "AppInsights", "AppConfig", "OpenAI", "Serp", "BingLLMSearch", "Serverless", "ManagedOnlineEndpoint", "ApiManagement", "ModelGateway", "GroundingWithBingSearch", "GroundingWithCustomSearch", "Sharepoint", "MicrosoftFabric", "PowerPlatformEnvironment", and "RemoteA2A". (PythonFeed, ContainerRegistry, Git, S3, Snowflake, AzureKeyVault, AzureSqlDb, AzureSynapseAnalytics, AzureMySqlDb, AzurePostgresDb, ADLSGen2, AzureContainerAppEnvironment, Redis, ApiKey, AzureOpenAI, AIServices, CognitiveSearch, CognitiveService, CustomKeys, AzureBlob, AzureStorageAccount, AzureOneLake, CosmosDb, CosmosDbMongoDbApi, AzureDataExplorer, AzureMariaDb, AzureDatabricksDeltaLake, AzureSqlMi, AzureTableStorage, AmazonRdsForOracle, AmazonRdsForSqlServer, AmazonRedshift, Db2, Drill, GoogleBigQuery, Greenplum, Hbase, Hive, Impala, Informix, MariaDb, MicrosoftAccess, MySql, Netezza, Oracle, Phoenix, PostgreSql, Presto, SapOpenHub, SapBw, SapHana, SapTable, Spark, SqlServer, Sybase, Teradata, Vertica, Pinecone, Databricks, Cassandra, Couchbase, MongoDbV2, MongoDbAtlas, AmazonS3Compatible, FileServer, FtpServer, GoogleCloudStorage, Hdfs, OracleCloudStorage, Sftp, GenericHttp, ODataRest, Odbc, GenericRest, RemoteTool, AmazonMws, Concur, Dynamics, DynamicsAx, DynamicsCrm, GoogleAdWords, Hubspot, Jira, Magento, Marketo, Office365, Eloqua, Responsys, OracleServiceCloud, PayPal, QuickBooks, Salesforce, SalesforceServiceCloud, SalesforceMarketingCloud, SapCloudForCustomer, SapEcc, ServiceNow, SharePointOnlineList, Shopify, Square, WebTable, Xero, Zoho, GenericContainerRegistry, Elasticsearch, AppInsights, AppConfig, OpenAI, Serp, BingLLMSearch, Serverless, ManagedOnlineEndpoint, ApiManagement, ModelGateway, GroundingWithBingSearch, GroundingWithCustomSearch, Sharepoint, MicrosoftFabric, PowerPlatformEnvironment, RemoteA2A)</td>
</tr>
<tr>
    <td><CopyableCode code="createdByWorkspaceArmId" /></td>
    <td><code>string</code></td>
    <td>:vartype created_by_workspace_arm_id: str</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Provides the error message if the connection fails.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>:vartype expiry_time: ~datetime.datetime</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code>string</code></td>
    <td>Group based on connection category. Known values are: "Azure", "AzureAI", "Database", "NoSQL", "File", "GenericProtocol", and "ServicesAndApps". (Azure, AzureAI, Database, NoSQL, File, GenericProtocol, ServicesAndApps)</td>
</tr>
<tr>
    <td><CopyableCode code="isSharedToAll" /></td>
    <td><code>boolean</code></td>
    <td>:vartype is_shared_to_all: bool</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Store user metadata for this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="peRequirement" /></td>
    <td><code>string</code></td>
    <td>Specifies how private endpoints are used with this connection: 'Required', 'NotRequired', or 'NotApplicable'. Known values are: "Required", "NotRequired", and "NotApplicable". (Required, NotRequired, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="peStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies the status of private endpoints for this connection: 'Inactive', 'Active', or 'NotApplicable'. Known values are: "Inactive", "Active", and "NotApplicable". (Inactive, Active, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="sharedUserList" /></td>
    <td><code>array</code></td>
    <td>:vartype shared_user_list: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>The connection URL to be used.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useWorkspaceManagedIdentity" /></td>
    <td><code>boolean</code></td>
    <td>:vartype use_workspace_managed_identity: bool</td>
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
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>Authentication type of the connection target. Required. Known values are: "PAT", "ManagedIdentity", "UsernamePassword", "None", "SAS", "AccountKey", "ServicePrincipal", "AccessKey", "ApiKey", "CustomKeys", "OAuth2", "AAD", "DelegatedSAS", "ProjectManagedIdentity", "AccountManagedIdentity", "UserEntraToken", "AgentUserImpersonation", "AgenticIdentityToken", and "AgenticUser".</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of the connection. Known values are: "PythonFeed", "ContainerRegistry", "Git", "S3", "Snowflake", "AzureKeyVault", "AzureSqlDb", "AzureSynapseAnalytics", "AzureMySqlDb", "AzurePostgresDb", "ADLSGen2", "AzureContainerAppEnvironment", "Redis", "ApiKey", "AzureOpenAI", "AIServices", "CognitiveSearch", "CognitiveService", "CustomKeys", "AzureBlob", "AzureStorageAccount", "AzureOneLake", "CosmosDb", "CosmosDbMongoDbApi", "AzureDataExplorer", "AzureMariaDb", "AzureDatabricksDeltaLake", "AzureSqlMi", "AzureTableStorage", "AmazonRdsForOracle", "AmazonRdsForSqlServer", "AmazonRedshift", "Db2", "Drill", "GoogleBigQuery", "Greenplum", "Hbase", "Hive", "Impala", "Informix", "MariaDb", "MicrosoftAccess", "MySql", "Netezza", "Oracle", "Phoenix", "PostgreSql", "Presto", "SapOpenHub", "SapBw", "SapHana", "SapTable", "Spark", "SqlServer", "Sybase", "Teradata", "Vertica", "Pinecone", "Databricks", "Cassandra", "Couchbase", "MongoDbV2", "MongoDbAtlas", "AmazonS3Compatible", "FileServer", "FtpServer", "GoogleCloudStorage", "Hdfs", "OracleCloudStorage", "Sftp", "GenericHttp", "ODataRest", "Odbc", "GenericRest", "RemoteTool", "AmazonMws", "Concur", "Dynamics", "DynamicsAx", "DynamicsCrm", "GoogleAdWords", "Hubspot", "Jira", "Magento", "Marketo", "Office365", "Eloqua", "Responsys", "OracleServiceCloud", "PayPal", "QuickBooks", "Salesforce", "SalesforceServiceCloud", "SalesforceMarketingCloud", "SapCloudForCustomer", "SapEcc", "ServiceNow", "SharePointOnlineList", "Shopify", "Square", "WebTable", "Xero", "Zoho", "GenericContainerRegistry", "Elasticsearch", "AppInsights", "AppConfig", "OpenAI", "Serp", "BingLLMSearch", "Serverless", "ManagedOnlineEndpoint", "ApiManagement", "ModelGateway", "GroundingWithBingSearch", "GroundingWithCustomSearch", "Sharepoint", "MicrosoftFabric", "PowerPlatformEnvironment", and "RemoteA2A". (PythonFeed, ContainerRegistry, Git, S3, Snowflake, AzureKeyVault, AzureSqlDb, AzureSynapseAnalytics, AzureMySqlDb, AzurePostgresDb, ADLSGen2, AzureContainerAppEnvironment, Redis, ApiKey, AzureOpenAI, AIServices, CognitiveSearch, CognitiveService, CustomKeys, AzureBlob, AzureStorageAccount, AzureOneLake, CosmosDb, CosmosDbMongoDbApi, AzureDataExplorer, AzureMariaDb, AzureDatabricksDeltaLake, AzureSqlMi, AzureTableStorage, AmazonRdsForOracle, AmazonRdsForSqlServer, AmazonRedshift, Db2, Drill, GoogleBigQuery, Greenplum, Hbase, Hive, Impala, Informix, MariaDb, MicrosoftAccess, MySql, Netezza, Oracle, Phoenix, PostgreSql, Presto, SapOpenHub, SapBw, SapHana, SapTable, Spark, SqlServer, Sybase, Teradata, Vertica, Pinecone, Databricks, Cassandra, Couchbase, MongoDbV2, MongoDbAtlas, AmazonS3Compatible, FileServer, FtpServer, GoogleCloudStorage, Hdfs, OracleCloudStorage, Sftp, GenericHttp, ODataRest, Odbc, GenericRest, RemoteTool, AmazonMws, Concur, Dynamics, DynamicsAx, DynamicsCrm, GoogleAdWords, Hubspot, Jira, Magento, Marketo, Office365, Eloqua, Responsys, OracleServiceCloud, PayPal, QuickBooks, Salesforce, SalesforceServiceCloud, SalesforceMarketingCloud, SapCloudForCustomer, SapEcc, ServiceNow, SharePointOnlineList, Shopify, Square, WebTable, Xero, Zoho, GenericContainerRegistry, Elasticsearch, AppInsights, AppConfig, OpenAI, Serp, BingLLMSearch, Serverless, ManagedOnlineEndpoint, ApiManagement, ModelGateway, GroundingWithBingSearch, GroundingWithCustomSearch, Sharepoint, MicrosoftFabric, PowerPlatformEnvironment, RemoteA2A)</td>
</tr>
<tr>
    <td><CopyableCode code="createdByWorkspaceArmId" /></td>
    <td><code>string</code></td>
    <td>:vartype created_by_workspace_arm_id: str</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Provides the error message if the connection fails.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>:vartype expiry_time: ~datetime.datetime</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code>string</code></td>
    <td>Group based on connection category. Known values are: "Azure", "AzureAI", "Database", "NoSQL", "File", "GenericProtocol", and "ServicesAndApps". (Azure, AzureAI, Database, NoSQL, File, GenericProtocol, ServicesAndApps)</td>
</tr>
<tr>
    <td><CopyableCode code="isSharedToAll" /></td>
    <td><code>boolean</code></td>
    <td>:vartype is_shared_to_all: bool</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Store user metadata for this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="peRequirement" /></td>
    <td><code>string</code></td>
    <td>Specifies how private endpoints are used with this connection: 'Required', 'NotRequired', or 'NotApplicable'. Known values are: "Required", "NotRequired", and "NotApplicable". (Required, NotRequired, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="peStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies the status of private endpoints for this connection: 'Inactive', 'Active', or 'NotApplicable'. Known values are: "Inactive", "Active", and "NotApplicable". (Inactive, Active, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="sharedUserList" /></td>
    <td><code>array</code></td>
    <td>:vartype shared_user_list: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>The connection URL to be used.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useWorkspaceManagedIdentity" /></td>
    <td><code>boolean</code></td>
    <td>:vartype use_workspace_managed_identity: bool</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists Cognitive Services account connection by name. Lists Cognitive Services account connection by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-target"><code>target</code></a>, <a href="#parameter-category"><code>category</code></a>, <a href="#parameter-includeAll"><code>includeAll</code></a></td>
    <td>Lists all the available Cognitive Services account connections under the specified account. Lists all the available Cognitive Services account connections under the specified account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update Cognitive Services account connection under the specified account. Create or update Cognitive Services account connection under the specified account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update Cognitive Services account connection under the specified account. Update Cognitive Services account connection under the specified account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Cognitive Services account connection by name. Delete Cognitive Services account connection by name.</td>
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
    <td>The name of Cognitive Services account. Required.</td>
</tr>
<tr id="parameter-connection_name">
    <td><CopyableCode code="connection_name" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the connection. Required.</td>
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
<tr id="parameter-category">
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of the connection. Default value is None.</td>
</tr>
<tr id="parameter-includeAll">
    <td><CopyableCode code="includeAll" /></td>
    <td><code>boolean</code></td>
    <td>query parameter that indicates if get connection call should return both connections and datastores. Default value is False.</td>
</tr>
<tr id="parameter-target">
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>Target of the connection. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Lists Cognitive Services account connection by name. Lists Cognitive Services account connection by name.

```sql
SELECT
id,
name,
authType,
category,
createdByWorkspaceArmId,
error,
expiryTime,
group,
isSharedToAll,
metadata,
peRequirement,
peStatus,
sharedUserList,
systemData,
target,
type,
useWorkspaceManagedIdentity
FROM azure.cognitive_services.account_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the available Cognitive Services account connections under the specified account. Lists all the available Cognitive Services account connections under the specified account.

```sql
SELECT
id,
name,
authType,
category,
createdByWorkspaceArmId,
error,
expiryTime,
group,
isSharedToAll,
metadata,
peRequirement,
peStatus,
sharedUserList,
systemData,
target,
type,
useWorkspaceManagedIdentity
FROM azure.cognitive_services.account_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND target = '{{ target }}'
AND category = '{{ category }}'
AND includeAll = '{{ includeAll }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create or update Cognitive Services account connection under the specified account. Create or update Cognitive Services account connection under the specified account.

```sql
INSERT INTO azure.cognitive_services.account_connections (
properties,
resource_group_name,
account_name,
connection_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ connection_name }}',
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
- name: account_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the account_connections resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the account_connections resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the account_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the account_connections resource.
    - name: properties
      description: |
        Connection property base schema. Required.
      value:
        authType: "{{ authType }}"
        category: "{{ category }}"
        createdByWorkspaceArmId: "{{ createdByWorkspaceArmId }}"
        error: "{{ error }}"
        expiryTime: "{{ expiryTime }}"
        group: "{{ group }}"
        isSharedToAll: {{ isSharedToAll }}
        metadata: "{{ metadata }}"
        peRequirement: "{{ peRequirement }}"
        peStatus: "{{ peStatus }}"
        sharedUserList:
          - "{{ sharedUserList }}"
        target: "{{ target }}"
        useWorkspaceManagedIdentity: {{ useWorkspaceManagedIdentity }}
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

Update Cognitive Services account connection under the specified account. Update Cognitive Services account connection under the specified account.

```sql
UPDATE azure.cognitive_services.account_connections
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Delete Cognitive Services account connection by name. Delete Cognitive Services account connection by name.

```sql
DELETE FROM azure.cognitive_services.account_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
