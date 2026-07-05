--- 
title: git_lab_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - git_lab_projects
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

Creates, updates, deletes, gets or lists a <code>git_lab_projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="git_lab_projects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.git_lab_projects" /></td></tr>
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
    <td><CopyableCode code="fullyQualifiedFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the human readable fully-qualified name of the Project object. This contains the entire namespace hierarchy as seen on GitLab UI where entities are separated by the '/' character.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fully-qualified name of the project object. This contains the entire hierarchy where entities are separated by the '$' character.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedParentGroupName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fully-qualified name of the project's parent group object. This contains the entire hierarchy where namespaces are separated by the '$' character.</td>
</tr>
<tr>
    <td><CopyableCode code="onboardingState" /></td>
    <td><code>string</code></td>
    <td>Details about resource onboarding status across all connectors. OnboardedByOtherConnector - this resource has already been onboarded to another connector. This is only applicable to top-level resources. Onboarded - this resource has already been onboarded by the specified connector. NotOnboarded - this resource has not been onboarded to any connector. NotApplicable - the onboarding state is not applicable to the current endpoint. Known values are: "NotApplicable", "OnboardedByOtherConnector", "Onboarded", and "NotOnboarded". (NotApplicable, OnboardedByOtherConnector, Onboarded, NotOnboarded)</td>
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
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the url of the GitLab Project.</td>
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
    <td><CopyableCode code="fullyQualifiedFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the human readable fully-qualified name of the Project object. This contains the entire namespace hierarchy as seen on GitLab UI where entities are separated by the '/' character.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fully-qualified name of the project object. This contains the entire hierarchy where entities are separated by the '$' character.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedParentGroupName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fully-qualified name of the project's parent group object. This contains the entire hierarchy where namespaces are separated by the '$' character.</td>
</tr>
<tr>
    <td><CopyableCode code="onboardingState" /></td>
    <td><code>string</code></td>
    <td>Details about resource onboarding status across all connectors. OnboardedByOtherConnector - this resource has already been onboarded to another connector. This is only applicable to top-level resources. Onboarded - this resource has already been onboarded by the specified connector. NotOnboarded - this resource has not been onboarded to any connector. NotApplicable - the onboarding state is not applicable to the current endpoint. Known values are: "NotApplicable", "OnboardedByOtherConnector", "Onboarded", and "NotOnboarded". (NotApplicable, OnboardedByOtherConnector, Onboarded, NotOnboarded)</td>
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
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the url of the GitLab Project.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-group_fq_name"><code>group_fq_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a monitored GitLab Project resource for a given fully-qualified group name and project name. Returns a monitored GitLab Project resource for a given fully-qualified group name and project name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-group_fq_name"><code>group_fq_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of GitLab projects that are directly owned by given group and onboarded to the connector. Gets a list of GitLab projects that are directly owned by given group and onboarded to the connector.</td>
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
<tr id="parameter-group_fq_name">
    <td><CopyableCode code="group_fq_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
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

Returns a monitored GitLab Project resource for a given fully-qualified group name and project name. Returns a monitored GitLab Project resource for a given fully-qualified group name and project name.

```sql
SELECT
id,
name,
fullyQualifiedFriendlyName,
fullyQualifiedName,
fullyQualifiedParentGroupName,
onboardingState,
provisioningState,
provisioningStatusMessage,
provisioningStatusUpdateTimeUtc,
systemData,
type,
url
FROM azure.security.git_lab_projects
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND security_connector_name = '{{ security_connector_name }}' -- required
AND group_fq_name = '{{ group_fq_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of GitLab projects that are directly owned by given group and onboarded to the connector. Gets a list of GitLab projects that are directly owned by given group and onboarded to the connector.

```sql
SELECT
id,
name,
fullyQualifiedFriendlyName,
fullyQualifiedName,
fullyQualifiedParentGroupName,
onboardingState,
provisioningState,
provisioningStatusMessage,
provisioningStatusUpdateTimeUtc,
systemData,
type,
url
FROM azure.security.git_lab_projects
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND security_connector_name = '{{ security_connector_name }}' -- required
AND group_fq_name = '{{ group_fq_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
