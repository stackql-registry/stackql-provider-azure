--- 
title: restorable_database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_database_accounts
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

Creates, updates, deletes, gets or lists a <code>restorable_database_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="restorable_database_accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.restorable_database_accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_location"
    values={[
        { label: 'get_by_location', value: 'get_by_location' },
        { label: 'list_by_location', value: 'list_by_location' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_location">

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
    <td><CopyableCode code="accountName" /></td>
    <td><code>string</code></td>
    <td>The name of the global database account.</td>
</tr>
<tr>
    <td><CopyableCode code="apiType" /></td>
    <td><code>string</code></td>
    <td>The API type of the restorable database account. Known values are: "MongoDB", "Gremlin", "Cassandra", "Table", "Sql", and "GremlinV2". (MongoDB, Gremlin, Cassandra, Table, Sql, GremlinV2)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the restorable database account (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="deletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the restorable database account has been deleted (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="oldestRestorableTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The least recent time at which the database account can be restored to (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="restorableLocations" /></td>
    <td><code>array</code></td>
    <td>List of regions where the of the database account can be restored from.</td>
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
<TabItem value="list_by_location">

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
    <td><CopyableCode code="accountName" /></td>
    <td><code>string</code></td>
    <td>The name of the global database account.</td>
</tr>
<tr>
    <td><CopyableCode code="apiType" /></td>
    <td><code>string</code></td>
    <td>The API type of the restorable database account. Known values are: "MongoDB", "Gremlin", "Cassandra", "Table", "Sql", and "GremlinV2". (MongoDB, Gremlin, Cassandra, Table, Sql, GremlinV2)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the restorable database account (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="deletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the restorable database account has been deleted (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="oldestRestorableTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The least recent time at which the database account can be restored to (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="restorableLocations" /></td>
    <td><code>array</code></td>
    <td>List of regions where the of the database account can be restored from.</td>
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
    <td><CopyableCode code="accountName" /></td>
    <td><code>string</code></td>
    <td>The name of the global database account.</td>
</tr>
<tr>
    <td><CopyableCode code="apiType" /></td>
    <td><code>string</code></td>
    <td>The API type of the restorable database account. Known values are: "MongoDB", "Gremlin", "Cassandra", "Table", "Sql", and "GremlinV2". (MongoDB, Gremlin, Cassandra, Table, Sql, GremlinV2)</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the restorable database account (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="deletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the restorable database account has been deleted (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="oldestRestorableTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The least recent time at which the database account can be restored to (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="restorableLocations" /></td>
    <td><code>array</code></td>
    <td>List of regions where the of the database account can be restored from.</td>
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
    <td><a href="#get_by_location"><CopyableCode code="get_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB restorable database account. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read/*' permission.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the restorable Azure Cosmos DB database accounts available under the subscription and in a region. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the restorable Azure Cosmos DB database accounts available under the subscription. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission.</td>
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
<tr id="parameter-instance_id">
    <td><CopyableCode code="instance_id" /></td>
    <td><code>string</code></td>
    <td>The instanceId GUID of a restorable database account. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB region, with spaces between words and each word capitalized. Required.</td>
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
    defaultValue="get_by_location"
    values={[
        { label: 'get_by_location', value: 'get_by_location' },
        { label: 'list_by_location', value: 'list_by_location' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_location">

Retrieves the properties of an existing Azure Cosmos DB restorable database account. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read/*' permission.

```sql
SELECT
id,
name,
accountName,
apiType,
creationTime,
deletionTime,
location,
oldestRestorableTime,
restorableLocations,
systemData,
type
FROM azure.cosmosdb.restorable_database_accounts
WHERE location = '{{ location }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_location">

Lists all the restorable Azure Cosmos DB database accounts available under the subscription and in a region. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission.

```sql
SELECT
id,
name,
accountName,
apiType,
creationTime,
deletionTime,
location,
oldestRestorableTime,
restorableLocations,
systemData,
type
FROM azure.cosmosdb.restorable_database_accounts
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the restorable Azure Cosmos DB database accounts available under the subscription. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission.

```sql
SELECT
id,
name,
accountName,
apiType,
creationTime,
deletionTime,
location,
oldestRestorableTime,
restorableLocations,
systemData,
type
FROM azure.cosmosdb.restorable_database_accounts
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
