--- 
title: azure_dev_ops_orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_dev_ops_orgs
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

Creates, updates, deletes, gets or lists an <code>azure_dev_ops_orgs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="azure_dev_ops_orgs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.azure_dev_ops_orgs" /></td></tr>
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
    <td><CopyableCode code="actionableRemediation" /></td>
    <td><code>object</code></td>
    <td>Configuration payload for PR Annotations.</td>
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
    <td><CopyableCode code="actionableRemediation" /></td>
    <td><code>object</code></td>
    <td>Configuration payload for PR Annotations.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-org_name"><code>org_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a monitored Azure DevOps organization resource. Returns a monitored Azure DevOps organization resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of Azure DevOps organizations onboarded to the connector. Returns a list of Azure DevOps organizations onboarded to the connector.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-org_name"><code>org_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates monitored Azure DevOps organization details. Creates or updates monitored Azure DevOps organization details.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-org_name"><code>org_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates monitored Azure DevOps organization details. Updates monitored Azure DevOps organization details.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-org_name"><code>org_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates monitored Azure DevOps organization details. Creates or updates monitored Azure DevOps organization details.</td>
</tr>
<tr>
    <td><a href="#list_available"><CopyableCode code="list_available" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of all Azure DevOps organizations accessible by the user token consumed by the connector. Returns a list of all Azure DevOps organizations accessible by the user token consumed by the connector.</td>
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
<tr id="parameter-org_name">
    <td><CopyableCode code="org_name" /></td>
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

Returns a monitored Azure DevOps organization resource. Returns a monitored Azure DevOps organization resource.

```sql
SELECT
id,
name,
actionableRemediation,
onboardingState,
provisioningState,
provisioningStatusMessage,
provisioningStatusUpdateTimeUtc,
systemData,
type
FROM azure.security.azure_dev_ops_orgs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND security_connector_name = '{{ security_connector_name }}' -- required
AND org_name = '{{ org_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of Azure DevOps organizations onboarded to the connector. Returns a list of Azure DevOps organizations onboarded to the connector.

```sql
SELECT
id,
name,
actionableRemediation,
onboardingState,
provisioningState,
provisioningStatusMessage,
provisioningStatusUpdateTimeUtc,
systemData,
type
FROM azure.security.azure_dev_ops_orgs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND security_connector_name = '{{ security_connector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates monitored Azure DevOps organization details. Creates or updates monitored Azure DevOps organization details.

```sql
INSERT INTO azure.security.azure_dev_ops_orgs (
properties,
resource_group_name,
security_connector_name,
org_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ security_connector_name }}',
'{{ org_name }}',
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
- name: azure_dev_ops_orgs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the azure_dev_ops_orgs resource.
    - name: security_connector_name
      value: "{{ security_connector_name }}"
      description: Required parameter for the azure_dev_ops_orgs resource.
    - name: org_name
      value: "{{ org_name }}"
      description: Required parameter for the azure_dev_ops_orgs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the azure_dev_ops_orgs resource.
    - name: properties
      description: |
        Azure DevOps Organization properties.
      value:
        provisioningStatusMessage: "{{ provisioningStatusMessage }}"
        provisioningStatusUpdateTimeUtc: "{{ provisioningStatusUpdateTimeUtc }}"
        provisioningState: "{{ provisioningState }}"
        onboardingState: "{{ onboardingState }}"
        actionableRemediation:
          state: "{{ state }}"
          categoryConfigurations:
            - minimumSeverityLevel: "{{ minimumSeverityLevel }}"
              category: "{{ category }}"
          branchConfiguration:
            branchNames:
              - "{{ branchNames }}"
            annotateDefaultBranch: "{{ annotateDefaultBranch }}"
          inheritFromParentState: "{{ inheritFromParentState }}"
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

Updates monitored Azure DevOps organization details. Updates monitored Azure DevOps organization details.

```sql
UPDATE azure.security.azure_dev_ops_orgs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND security_connector_name = '{{ security_connector_name }}' --required
AND org_name = '{{ org_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates monitored Azure DevOps organization details. Creates or updates monitored Azure DevOps organization details.

```sql
REPLACE azure.security.azure_dev_ops_orgs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND security_connector_name = '{{ security_connector_name }}' --required
AND org_name = '{{ org_name }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="list_available"
    values={[
        { label: 'list_available', value: 'list_available' }
    ]}
>
<TabItem value="list_available">

Returns a list of all Azure DevOps organizations accessible by the user token consumed by the connector. Returns a list of all Azure DevOps organizations accessible by the user token consumed by the connector.

```sql
EXEC azure.security.azure_dev_ops_orgs.list_available 
@resource_group_name='{{ resource_group_name }}' --required, 
@security_connector_name='{{ security_connector_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
