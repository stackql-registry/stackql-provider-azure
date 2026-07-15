--- 
title: deleted_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_workspaces
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>deleted_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deleted_workspaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.deleted_workspaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Workspace creation date.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>This is a read-only property. Represents the ID associated with the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDataCollectionRuleResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the default Data Collection Rule to use for this workspace. Expected format is - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Insights/dataCollectionRules/&#123;dcrName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="failover" /></td>
    <td><code>object</code></td>
    <td>workspace failover properties.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>object</code></td>
    <td>Workspace features.</td>
</tr>
<tr>
    <td><CopyableCode code="forceCmkForQuery" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether customer managed storage is mandatory for query management.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Workspace modification date.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of linked private link scope resources.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the workspace. Known values are: "Creating", "Succeeded", "Failed", "Canceled", "Deleting", "ProvisioningAccount", and "Updating". (Creating, Succeeded, Failed, Canceled, Deleting, ProvisioningAccount, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForIngestion" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Log Analytics ingestion. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForQuery" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Log Analytics query. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="replication" /></td>
    <td><code>object</code></td>
    <td>workspace replication properties.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the workspace.</td>
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
    <td><CopyableCode code="workspaceCapping" /></td>
    <td><code>object</code></td>
    <td>The daily volume cap for ingestion.</td>
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
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Workspace creation date.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>This is a read-only property. Represents the ID associated with the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDataCollectionRuleResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the default Data Collection Rule to use for this workspace. Expected format is - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Insights/dataCollectionRules/&#123;dcrName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="failover" /></td>
    <td><code>object</code></td>
    <td>workspace failover properties.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>object</code></td>
    <td>Workspace features.</td>
</tr>
<tr>
    <td><CopyableCode code="forceCmkForQuery" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether customer managed storage is mandatory for query management.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Workspace modification date.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of linked private link scope resources.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the workspace. Known values are: "Creating", "Succeeded", "Failed", "Canceled", "Deleting", "ProvisioningAccount", and "Updating". (Creating, Succeeded, Failed, Canceled, Deleting, ProvisioningAccount, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForIngestion" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Log Analytics ingestion. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForQuery" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Log Analytics query. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="replication" /></td>
    <td><code>object</code></td>
    <td>workspace replication properties.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the workspace.</td>
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
    <td><CopyableCode code="workspaceCapping" /></td>
    <td><code>object</code></td>
    <td>The daily volume cap for ingestion.</td>
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
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets recently deleted workspaces in a resource group, available for recovery.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets recently deleted workspaces in a subscription, available for recovery.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_by_resource_group">

Gets recently deleted workspaces in a resource group, available for recovery.

```sql
SELECT
id,
name,
createdDate,
customerId,
defaultDataCollectionRuleResourceId,
etag,
failover,
features,
forceCmkForQuery,
identity,
location,
modifiedDate,
privateLinkScopedResources,
provisioningState,
publicNetworkAccessForIngestion,
publicNetworkAccessForQuery,
replication,
retentionInDays,
sku,
systemData,
tags,
type,
workspaceCapping
FROM azure.log_analytics.deleted_workspaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets recently deleted workspaces in a subscription, available for recovery.

```sql
SELECT
id,
name,
createdDate,
customerId,
defaultDataCollectionRuleResourceId,
etag,
failover,
features,
forceCmkForQuery,
identity,
location,
modifiedDate,
privateLinkScopedResources,
provisioningState,
publicNetworkAccessForIngestion,
publicNetworkAccessForQuery,
replication,
retentionInDays,
sku,
systemData,
tags,
type,
workspaceCapping
FROM azure.log_analytics.deleted_workspaces
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
