--- 
title: deleted_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_accounts
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

Creates, updates, deletes, gets or lists a <code>deleted_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deleted_accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.deleted_accounts" /></td></tr>
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
    <td><CopyableCode code="abusePenalty" /></td>
    <td><code>object</code></td>
    <td>The abuse penalty.</td>
</tr>
<tr>
    <td><CopyableCode code="allowProjectManagement" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this resource support project management as child resources, used as containers for access management, data isolation and cost in AI Foundry.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>:vartype allowed_fqdn_list: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="amlWorkspace" /></td>
    <td><code>object</code></td>
    <td>The user owned AML account properties.</td>
</tr>
<tr>
    <td><CopyableCode code="apiProperties" /></td>
    <td><code>object</code></td>
    <td>The api properties for special APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedProjects" /></td>
    <td><code>array</code></td>
    <td>Specifies the projects, by project name, that are associated with this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="callRateLimit" /></td>
    <td><code>object</code></td>
    <td>The call rate limit Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>Gets the capabilities of the cognitive services account. Each item indicates the capability of a specific feature. The values are read-only and for reference only.</td>
</tr>
<tr>
    <td><CopyableCode code="commitmentPlanAssociations" /></td>
    <td><code>array</code></td>
    <td>The commitment plan associations of Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="customSubDomainName" /></td>
    <td><code>string</code></td>
    <td>Optional subdomain name used for token-based authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="dateCreated" /></td>
    <td><code>string</code></td>
    <td>Gets the date of cognitive services account creation.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultProject" /></td>
    <td><code>string</code></td>
    <td>Specifies the project, by project name, that is targeted when data plane endpoints are called without a project parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="deletionDate" /></td>
    <td><code>string</code></td>
    <td>The deletion date, only available for deleted account.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>:vartype disable_local_auth: bool</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicThrottlingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag to enable dynamic throttling.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint of the created account.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>Dictionary of .</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="foundryAutoUpgrade" /></td>
    <td><code>object</code></td>
    <td>Represents the foundry auto-upgrade configuration for a Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="internalId" /></td>
    <td><code>string</code></td>
    <td>The internal identifier (deprecated, do not use this property).</td>
</tr>
<tr>
    <td><CopyableCode code="isMigrated" /></td>
    <td><code>boolean</code></td>
    <td>If the resource is migrated from an existing key.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind (type) of cognitive service account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>object</code></td>
    <td>The multiregion settings of Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationToken" /></td>
    <td><code>string</code></td>
    <td>Resource migration token.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>A collection of rules governing the accessibility from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInjections" /></td>
    <td><code>array</code></td>
    <td>:vartype network_injections: list[~azure.mgmt.cognitiveservices.models.NetworkInjection]</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The private endpoint connection associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the cognitive services account at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", "Canceled", and "ResolvingDNS". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled, ResolvingDNS)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this account. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="quotaLimit" /></td>
    <td><code>object</code></td>
    <td>:vartype quota_limit: ~azure.mgmt.cognitiveservices.models.QuotaLimit</td>
</tr>
<tr>
    <td><CopyableCode code="raiMonitorConfig" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services Rai Monitor Config.</td>
</tr>
<tr>
    <td><CopyableCode code="restore" /></td>
    <td><code>boolean</code></td>
    <td>:vartype restore: bool</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>:vartype restrict_outbound_network_access: bool</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string</code></td>
    <td>The scheduled purge date, only available for deleted account.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="skuChangeInfo" /></td>
    <td><code>object</code></td>
    <td>Sku change info of account.</td>
</tr>
<tr>
    <td><CopyableCode code="storedCompletionsDisabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag to disable stored completions.</td>
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
    <td><CopyableCode code="userOwnedStorage" /></td>
    <td><code>array</code></td>
    <td>The storage accounts for this resource.</td>
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
    <td><CopyableCode code="abusePenalty" /></td>
    <td><code>object</code></td>
    <td>The abuse penalty.</td>
</tr>
<tr>
    <td><CopyableCode code="allowProjectManagement" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this resource support project management as child resources, used as containers for access management, data isolation and cost in AI Foundry.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>:vartype allowed_fqdn_list: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="amlWorkspace" /></td>
    <td><code>object</code></td>
    <td>The user owned AML account properties.</td>
</tr>
<tr>
    <td><CopyableCode code="apiProperties" /></td>
    <td><code>object</code></td>
    <td>The api properties for special APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedProjects" /></td>
    <td><code>array</code></td>
    <td>Specifies the projects, by project name, that are associated with this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="callRateLimit" /></td>
    <td><code>object</code></td>
    <td>The call rate limit Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>Gets the capabilities of the cognitive services account. Each item indicates the capability of a specific feature. The values are read-only and for reference only.</td>
</tr>
<tr>
    <td><CopyableCode code="commitmentPlanAssociations" /></td>
    <td><code>array</code></td>
    <td>The commitment plan associations of Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="customSubDomainName" /></td>
    <td><code>string</code></td>
    <td>Optional subdomain name used for token-based authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="dateCreated" /></td>
    <td><code>string</code></td>
    <td>Gets the date of cognitive services account creation.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultProject" /></td>
    <td><code>string</code></td>
    <td>Specifies the project, by project name, that is targeted when data plane endpoints are called without a project parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="deletionDate" /></td>
    <td><code>string</code></td>
    <td>The deletion date, only available for deleted account.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>:vartype disable_local_auth: bool</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicThrottlingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag to enable dynamic throttling.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint of the created account.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>Dictionary of .</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="foundryAutoUpgrade" /></td>
    <td><code>object</code></td>
    <td>Represents the foundry auto-upgrade configuration for a Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="internalId" /></td>
    <td><code>string</code></td>
    <td>The internal identifier (deprecated, do not use this property).</td>
</tr>
<tr>
    <td><CopyableCode code="isMigrated" /></td>
    <td><code>boolean</code></td>
    <td>If the resource is migrated from an existing key.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind (type) of cognitive service account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>object</code></td>
    <td>The multiregion settings of Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationToken" /></td>
    <td><code>string</code></td>
    <td>Resource migration token.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>A collection of rules governing the accessibility from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInjections" /></td>
    <td><code>array</code></td>
    <td>:vartype network_injections: list[~azure.mgmt.cognitiveservices.models.NetworkInjection]</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The private endpoint connection associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the cognitive services account at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", "Canceled", and "ResolvingDNS". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled, ResolvingDNS)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this account. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="quotaLimit" /></td>
    <td><code>object</code></td>
    <td>:vartype quota_limit: ~azure.mgmt.cognitiveservices.models.QuotaLimit</td>
</tr>
<tr>
    <td><CopyableCode code="raiMonitorConfig" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services Rai Monitor Config.</td>
</tr>
<tr>
    <td><CopyableCode code="restore" /></td>
    <td><code>boolean</code></td>
    <td>:vartype restore: bool</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>:vartype restrict_outbound_network_access: bool</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string</code></td>
    <td>The scheduled purge date, only available for deleted account.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="skuChangeInfo" /></td>
    <td><code>object</code></td>
    <td>Sku change info of account.</td>
</tr>
<tr>
    <td><CopyableCode code="storedCompletionsDisabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag to disable stored completions.</td>
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
    <td><CopyableCode code="userOwnedStorage" /></td>
    <td><code>array</code></td>
    <td>The storage accounts for this resource.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a Cognitive Services account specified by the parameters.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a subscription.</td>
</tr>
<tr>
    <td><a href="#purge"><CopyableCode code="purge" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Cognitive Services account from the resource group.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns a Cognitive Services account specified by the parameters.

```sql
SELECT
id,
name,
abusePenalty,
allowProjectManagement,
allowedFqdnList,
amlWorkspace,
apiProperties,
associatedProjects,
callRateLimit,
capabilities,
commitmentPlanAssociations,
customSubDomainName,
dateCreated,
defaultProject,
deletionDate,
disableLocalAuth,
dynamicThrottlingEnabled,
encryption,
endpoint,
endpoints,
etag,
foundryAutoUpgrade,
identity,
internalId,
isMigrated,
kind,
location,
locations,
migrationToken,
networkAcls,
networkInjections,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
quotaLimit,
raiMonitorConfig,
restore,
restrictOutboundNetworkAccess,
scheduledPurgeDate,
sku,
skuChangeInfo,
storedCompletionsDisabled,
systemData,
tags,
type,
userOwnedStorage
FROM azure.cognitive_services.deleted_accounts
WHERE location = '{{ location }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns all the resources of a particular type belonging to a subscription.

```sql
SELECT
id,
name,
abusePenalty,
allowProjectManagement,
allowedFqdnList,
amlWorkspace,
apiProperties,
associatedProjects,
callRateLimit,
capabilities,
commitmentPlanAssociations,
customSubDomainName,
dateCreated,
defaultProject,
deletionDate,
disableLocalAuth,
dynamicThrottlingEnabled,
encryption,
endpoint,
endpoints,
etag,
foundryAutoUpgrade,
identity,
internalId,
isMigrated,
kind,
location,
locations,
migrationToken,
networkAcls,
networkInjections,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
quotaLimit,
raiMonitorConfig,
restore,
restrictOutboundNetworkAccess,
scheduledPurgeDate,
sku,
skuChangeInfo,
storedCompletionsDisabled,
systemData,
tags,
type,
userOwnedStorage
FROM azure.cognitive_services.deleted_accounts
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="purge"
    values={[
        { label: 'purge', value: 'purge' }
    ]}
>
<TabItem value="purge">

Deletes a Cognitive Services account from the resource group.

```sql
DELETE FROM azure.cognitive_services.deleted_accounts
WHERE location = '{{ location }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
