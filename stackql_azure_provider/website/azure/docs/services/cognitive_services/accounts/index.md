--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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

Creates, updates, deletes, gets or lists an <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a Cognitive Services account specified by the parameters.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Cognitive Services Account. Accounts is a resource group wide resource type. It holds the keys for developer to access intelligent APIs. It's also the resource type for billing.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Cognitive Services account from the resource group.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the account keys for the specified Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List available SKUs for the requested Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#list_usages"><CopyableCode code="list_usages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get usages for the requested Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#list_models"><CopyableCode code="list_models" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List available Models for the requested Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyName"><code>keyName</code></a></td>
    <td></td>
    <td>Regenerates the specified account key for the specified Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#evaluate_deployment_policies"><CopyableCode code="evaluate_deployment_policies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-deployments"><code>deployments</code></a></td>
    <td></td>
    <td>Evaluate Azure Policy compliance for a set of hypothetical deployments without creating them.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
FROM azure.cognitive_services.accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns all the resources of a particular type belonging to a resource group.

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
FROM azure.cognitive_services.accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
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
FROM azure.cognitive_services.accounts
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create Cognitive Services Account. Accounts is a resource group wide resource type. It holds the keys for developer to access intelligent APIs. It's also the resource type for billing.

```sql
INSERT INTO azure.cognitive_services.accounts (
properties,
tags,
location,
kind,
sku,
identity,
resource_group_name,
account_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ kind }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: accounts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the accounts resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the accounts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the accounts resource.
    - name: properties
      description: |
        Properties of Cognitive Services account.
      value:
        provisioningState: "{{ provisioningState }}"
        endpoint: "{{ endpoint }}"
        internalId: "{{ internalId }}"
        capabilities:
          - name: "{{ name }}"
            value: "{{ value }}"
        isMigrated: {{ isMigrated }}
        migrationToken: "{{ migrationToken }}"
        skuChangeInfo:
          countOfDowngrades: {{ countOfDowngrades }}
          countOfUpgradesAfterDowngrades: {{ countOfUpgradesAfterDowngrades }}
          lastChangeDate: "{{ lastChangeDate }}"
        customSubDomainName: "{{ customSubDomainName }}"
        networkAcls:
          defaultAction: "{{ defaultAction }}"
          bypass: "{{ bypass }}"
          ipRules:
            - value: "{{ value }}"
          virtualNetworkRules:
            - id: "{{ id }}"
              state: "{{ state }}"
              ignoreMissingVnetServiceEndpoint: {{ ignoreMissingVnetServiceEndpoint }}
        encryption:
          keyVaultProperties:
            keyName: "{{ keyName }}"
            keyVersion: "{{ keyVersion }}"
            keyVaultUri: "{{ keyVaultUri }}"
            identityClientId: "{{ identityClientId }}"
          keySource: "{{ keySource }}"
        userOwnedStorage:
          - resourceId: "{{ resourceId }}"
            identityClientId: "{{ identityClientId }}"
        amlWorkspace:
          resourceId: "{{ resourceId }}"
          identityClientId: "{{ identityClientId }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
              groupIds:
                - "{{ groupIds }}"
            etag: "{{ etag }}"
            location: "{{ location }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        apiProperties:
          qnaRuntimeEndpoint: "{{ qnaRuntimeEndpoint }}"
          qnaAzureSearchEndpointKey: "{{ qnaAzureSearchEndpointKey }}"
          qnaAzureSearchEndpointId: "{{ qnaAzureSearchEndpointId }}"
          statisticsEnabled: {{ statisticsEnabled }}
          eventHubConnectionString: "{{ eventHubConnectionString }}"
          storageAccountConnectionString: "{{ storageAccountConnectionString }}"
          aadClientId: "{{ aadClientId }}"
          aadTenantId: "{{ aadTenantId }}"
          superUser: "{{ superUser }}"
          websiteName: "{{ websiteName }}"
        dateCreated: "{{ dateCreated }}"
        callRateLimit:
          count: {{ count }}
          renewalPeriod: {{ renewalPeriod }}
          rules:
            - key: "{{ key }}"
              renewalPeriod: {{ renewalPeriod }}
              count: {{ count }}
              minCount: {{ minCount }}
              dynamicThrottlingEnabled: {{ dynamicThrottlingEnabled }}
              matchPatterns: "{{ matchPatterns }}"
        dynamicThrottlingEnabled: {{ dynamicThrottlingEnabled }}
        storedCompletionsDisabled: {{ storedCompletionsDisabled }}
        quotaLimit:
          count: {{ count }}
          renewalPeriod: {{ renewalPeriod }}
          rules:
            - key: "{{ key }}"
              renewalPeriod: {{ renewalPeriod }}
              count: {{ count }}
              minCount: {{ minCount }}
              dynamicThrottlingEnabled: {{ dynamicThrottlingEnabled }}
              matchPatterns: "{{ matchPatterns }}"
        restrictOutboundNetworkAccess: {{ restrictOutboundNetworkAccess }}
        allowedFqdnList:
          - "{{ allowedFqdnList }}"
        disableLocalAuth: {{ disableLocalAuth }}
        endpoints: "{{ endpoints }}"
        restore: {{ restore }}
        deletionDate: "{{ deletionDate }}"
        scheduledPurgeDate: "{{ scheduledPurgeDate }}"
        locations:
          routingMethod: "{{ routingMethod }}"
          regions:
            - name: "{{ name }}"
              value: {{ value }}
              customsubdomain: "{{ customsubdomain }}"
        commitmentPlanAssociations:
          - commitmentPlanId: "{{ commitmentPlanId }}"
            commitmentPlanLocation: "{{ commitmentPlanLocation }}"
        abusePenalty:
          action: "{{ action }}"
          rateLimitPercentage: {{ rateLimitPercentage }}
          expiration: "{{ expiration }}"
        raiMonitorConfig:
          adxStorageResourceId: "{{ adxStorageResourceId }}"
          identityClientId: "{{ identityClientId }}"
        networkInjections:
          - scenario: "{{ scenario }}"
            subnetArmId: "{{ subnetArmId }}"
            useMicrosoftManagedNetwork: {{ useMicrosoftManagedNetwork }}
        foundryAutoUpgrade:
          mode: "{{ mode }}"
          plannedByMicrosoft: {{ plannedByMicrosoft }}
          statusReason: "{{ statusReason }}"
          scheduledAt: "{{ scheduledAt }}"
        allowProjectManagement: {{ allowProjectManagement }}
        defaultProject: "{{ defaultProject }}"
        associatedProjects:
          - "{{ associatedProjects }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind (type) of cognitive service account.
    - name: sku
      description: |
        The resource model definition representing SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Identity for the resource.
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
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a Cognitive Services account.

```sql
UPDATE azure.cognitive_services.accounts
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
kind = '{{ kind }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a Cognitive Services account from the resource group.

```sql
DELETE FROM azure.cognitive_services.accounts
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
        { label: 'list_skus', value: 'list_skus' },
        { label: 'list_usages', value: 'list_usages' },
        { label: 'list_models', value: 'list_models' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'evaluate_deployment_policies', value: 'evaluate_deployment_policies' }
    ]}
>
<TabItem value="list_keys">

Lists the account keys for the specified Cognitive Services account.

```sql
EXEC azure.cognitive_services.accounts.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_skus">

List available SKUs for the requested Cognitive Services account.

```sql
EXEC azure.cognitive_services.accounts.list_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_usages">

Get usages for the requested Cognitive Services account.

```sql
EXEC azure.cognitive_services.accounts.list_usages 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_models">

List available Models for the requested Cognitive Services account.

```sql
EXEC azure.cognitive_services.accounts.list_models 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerates the specified account key for the specified Cognitive Services account.

```sql
EXEC azure.cognitive_services.accounts.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}"
}'
;
```
</TabItem>
<TabItem value="evaluate_deployment_policies">

Evaluate Azure Policy compliance for a set of hypothetical deployments without creating them.

```sql
EXEC azure.cognitive_services.accounts.evaluate_deployment_policies 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"deployments": "{{ deployments }}"
}'
;
```
</TabItem>
</Tabs>
