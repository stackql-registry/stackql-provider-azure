--- 
title: github_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - github_repos
  - security
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

Creates, updates, deletes, gets or lists a <code>github_repos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="github_repos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.github_repos" /></td></tr>
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
    <td><CopyableCode code="onboardingState" /></td>
    <td><code>string</code></td>
    <td>Details about resource onboarding status across all connectors. OnboardedByOtherConnector - this resource has already been onboarded to another connector. This is only applicable to top-level resources. Onboarded - this resource has already been onboarded by the specified connector. NotOnboarded - this resource has not been onboarded to any connector. NotApplicable - the onboarding state is not applicable to the current endpoint. Known values are: "NotApplicable", "OnboardedByOtherConnector", "Onboarded", and "NotOnboarded". (NotApplicable, OnboardedByOtherConnector, Onboarded, NotOnboarded)</td>
</tr>
<tr>
    <td><CopyableCode code="parentOwnerName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets parent GitHub Owner name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Pending - Provisioning pending. Failed - Provisioning failed. Succeeded - Successful provisioning. Canceled - Provisioning canceled. PendingDeletion - Deletion pending. DeletionSuccess - Deletion successful. DeletionFailure - Deletion failure. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "PendingDeletion", "DeletionSuccess", and "DeletionFailure". (Succeeded, Failed, Canceled, Pending, PendingDeletion, DeletionSuccess, DeletionFailure)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusMessage" /></td>
    <td><code>string</code></td>
    <td>Gets the resource status message.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusUpdateTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when resource was last checked.</td>
</tr>
<tr>
    <td><CopyableCode code="repoFullName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Full Name. Repository name, prefixed with Owner name. Eg: "my-org/new-repo-1".</td>
</tr>
<tr>
    <td><CopyableCode code="repoId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Repository id. This is a numeric id defined by Github. Eg: "123456".</td>
</tr>
<tr>
    <td><CopyableCode code="repoName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Repository name. Eg: "new-repo-1".</td>
</tr>
<tr>
    <td><CopyableCode code="repoUrl" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Repository url.</td>
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
    <td><CopyableCode code="onboardingState" /></td>
    <td><code>string</code></td>
    <td>Details about resource onboarding status across all connectors. OnboardedByOtherConnector - this resource has already been onboarded to another connector. This is only applicable to top-level resources. Onboarded - this resource has already been onboarded by the specified connector. NotOnboarded - this resource has not been onboarded to any connector. NotApplicable - the onboarding state is not applicable to the current endpoint. Known values are: "NotApplicable", "OnboardedByOtherConnector", "Onboarded", and "NotOnboarded". (NotApplicable, OnboardedByOtherConnector, Onboarded, NotOnboarded)</td>
</tr>
<tr>
    <td><CopyableCode code="parentOwnerName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets parent GitHub Owner name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Pending - Provisioning pending. Failed - Provisioning failed. Succeeded - Successful provisioning. Canceled - Provisioning canceled. PendingDeletion - Deletion pending. DeletionSuccess - Deletion successful. DeletionFailure - Deletion failure. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "PendingDeletion", "DeletionSuccess", and "DeletionFailure". (Succeeded, Failed, Canceled, Pending, PendingDeletion, DeletionSuccess, DeletionFailure)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusMessage" /></td>
    <td><code>string</code></td>
    <td>Gets the resource status message.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusUpdateTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when resource was last checked.</td>
</tr>
<tr>
    <td><CopyableCode code="repoFullName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Full Name. Repository name, prefixed with Owner name. Eg: "my-org/new-repo-1".</td>
</tr>
<tr>
    <td><CopyableCode code="repoId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Repository id. This is a numeric id defined by Github. Eg: "123456".</td>
</tr>
<tr>
    <td><CopyableCode code="repoName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Repository name. Eg: "new-repo-1".</td>
</tr>
<tr>
    <td><CopyableCode code="repoUrl" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Repository url.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-owner_name"><code>owner_name</code></a>, <a href="#parameter-repo_name"><code>repo_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a monitored GitHub repository. Returns a monitored GitHub repository.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-owner_name"><code>owner_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of GitHub repositories onboarded to the connector. Returns a list of GitHub repositories onboarded to the connector.</td>
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
<tr id="parameter-owner_name">
    <td><CopyableCode code="owner_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-repo_name">
    <td><CopyableCode code="repo_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-security_connector_name">
    <td><CopyableCode code="security_connector_name" /></td>
    <td><code>string</code></td>
    <td>The security connector name. Required.</td>
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

Returns a monitored GitHub repository. Returns a monitored GitHub repository.

```sql
SELECT
id,
name,
onboardingState,
parentOwnerName,
provisioningState,
provisioningStatusMessage,
provisioningStatusUpdateTimeUtc,
repoFullName,
repoId,
repoName,
repoUrl,
systemData,
type
FROM azure.security.github_repos
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND security_connector_name = '{{ security_connector_name }}' -- required
AND owner_name = '{{ owner_name }}' -- required
AND repo_name = '{{ repo_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of GitHub repositories onboarded to the connector. Returns a list of GitHub repositories onboarded to the connector.

```sql
SELECT
id,
name,
onboardingState,
parentOwnerName,
provisioningState,
provisioningStatusMessage,
provisioningStatusUpdateTimeUtc,
repoFullName,
repoId,
repoName,
repoUrl,
systemData,
type
FROM azure.security.github_repos
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND security_connector_name = '{{ security_connector_name }}' -- required
AND owner_name = '{{ owner_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
