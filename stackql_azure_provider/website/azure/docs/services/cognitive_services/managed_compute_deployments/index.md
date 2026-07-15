--- 
title: managed_compute_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_compute_deployments
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

Creates, updates, deletes, gets or lists a <code>managed_compute_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_compute_deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.managed_compute_deployments" /></td></tr>
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
    <td><CopyableCode code="acceleratorType" /></td>
    <td><code>string</code></td>
    <td>Accelerator type (e.g., H100_80GB). Optional on creation; immutable after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="acceleratorsPerInstance" /></td>
    <td><code>integer</code></td>
    <td>Read-only. Number of accelerators (GPUs) consumed by each model instance, sourced from the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>Deployment capabilities represented as key-value pairs. Example: &#123; assetsV2: "true" &#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="computeId" /></td>
    <td><code>string</code></td>
    <td>Foundry compute ARM resource ID for VM-backed managed compute deployments. Required when sku.name is VmManagedCompute; immutable after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentTemplate" /></td>
    <td><code>string</code></td>
    <td>Deployment template identifier. Optional on creation. Accepts an AzureML Registry deployment template URI or a project-scoped deployment template path for VmManagedCompute. Examples: azureml://registries/&#123;registry&#125;/deploymenttemplates/&#123;template&#125;/versions/&#123;version&#125;, projects/&#123;project&#125;/deploymentTemplates/&#123;template&#125;/versions/&#123;version&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>AzureML Registry model asset URI. Required on creation; immutable after creation. Example: azureml://registries/&#123;registry&#125;/models/&#123;model&#125;/versions/&#123;version&#125;. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>Scheduling priority for VM-backed managed compute deployments. Immutable after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningDetails" /></td>
    <td><code>object</code></td>
    <td>Read-only. Status message and timestamp from the last provisioning operation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Read-only. Current provisioning state. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", "Canceled", and "ResolvingDNS". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled, ResolvingDNS)</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>object</code></td>
    <td>Read-only. Inference route paths relative to the account endpoint. Populated when provisioningState is Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAccelerators" /></td>
    <td><code>integer</code></td>
    <td>Read-only. Total accelerators allocated: sku.capacity (instances) x acceleratorsPerInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="versionUpgradeOption" /></td>
    <td><code>string</code></td>
    <td>Template auto-upgrade policy. Defaults to OnceNewDefaultVersionAvailable. Known values are: "OnceNewDefaultVersionAvailable", "OnceCurrentVersionExpired", and "NoAutoUpgrade". (OnceNewDefaultVersionAvailable, OnceCurrentVersionExpired, NoAutoUpgrade)</td>
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
    <td><CopyableCode code="acceleratorType" /></td>
    <td><code>string</code></td>
    <td>Accelerator type (e.g., H100_80GB). Optional on creation; immutable after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="acceleratorsPerInstance" /></td>
    <td><code>integer</code></td>
    <td>Read-only. Number of accelerators (GPUs) consumed by each model instance, sourced from the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>Deployment capabilities represented as key-value pairs. Example: &#123; assetsV2: "true" &#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="computeId" /></td>
    <td><code>string</code></td>
    <td>Foundry compute ARM resource ID for VM-backed managed compute deployments. Required when sku.name is VmManagedCompute; immutable after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentTemplate" /></td>
    <td><code>string</code></td>
    <td>Deployment template identifier. Optional on creation. Accepts an AzureML Registry deployment template URI or a project-scoped deployment template path for VmManagedCompute. Examples: azureml://registries/&#123;registry&#125;/deploymenttemplates/&#123;template&#125;/versions/&#123;version&#125;, projects/&#123;project&#125;/deploymentTemplates/&#123;template&#125;/versions/&#123;version&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>AzureML Registry model asset URI. Required on creation; immutable after creation. Example: azureml://registries/&#123;registry&#125;/models/&#123;model&#125;/versions/&#123;version&#125;. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>Scheduling priority for VM-backed managed compute deployments. Immutable after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningDetails" /></td>
    <td><code>object</code></td>
    <td>Read-only. Status message and timestamp from the last provisioning operation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Read-only. Current provisioning state. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", "Canceled", and "ResolvingDNS". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled, ResolvingDNS)</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>object</code></td>
    <td>Read-only. Inference route paths relative to the account endpoint. Populated when provisioningState is Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAccelerators" /></td>
    <td><code>integer</code></td>
    <td>Read-only. Total accelerators allocated: sku.capacity (instances) x acceleratorsPerInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="versionUpgradeOption" /></td>
    <td><code>string</code></td>
    <td>Template auto-upgrade policy. Defaults to OnceNewDefaultVersionAvailable. Known values are: "OnceNewDefaultVersionAvailable", "OnceCurrentVersionExpired", and "NoAutoUpgrade". (OnceNewDefaultVersionAvailable, OnceCurrentVersionExpired, NoAutoUpgrade)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified managed compute deployment associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the managed compute deployments associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a managed compute deployment associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specified managed compute deployment associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a managed compute deployment associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified managed compute deployment associated with the Cognitive Services account.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed compute deployment associated with the Cognitive Services Account. Required.</td>
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

Gets the specified managed compute deployment associated with the Cognitive Services account.

```sql
SELECT
id,
name,
acceleratorType,
acceleratorsPerInstance,
capabilities,
computeId,
deploymentTemplate,
etag,
model,
priority,
provisioningDetails,
provisioningState,
routes,
sku,
systemData,
totalAccelerators,
type,
versionUpgradeOption
FROM azure.cognitive_services.managed_compute_deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the managed compute deployments associated with the Cognitive Services account.

```sql
SELECT
id,
name,
acceleratorType,
acceleratorsPerInstance,
capabilities,
computeId,
deploymentTemplate,
etag,
model,
priority,
provisioningDetails,
provisioningState,
routes,
sku,
systemData,
totalAccelerators,
type,
versionUpgradeOption
FROM azure.cognitive_services.managed_compute_deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
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

Creates or updates a managed compute deployment associated with the Cognitive Services account.

```sql
INSERT INTO azure.cognitive_services.managed_compute_deployments (
properties,
sku,
resource_group_name,
account_name,
deployment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ deployment_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
sku,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: managed_compute_deployments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_compute_deployments resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the managed_compute_deployments resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the managed_compute_deployments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_compute_deployments resource.
    - name: properties
      description: |
        Properties of the Cognitive Services managed compute deployment.
      value:
        model: "{{ model }}"
        deploymentTemplate: "{{ deploymentTemplate }}"
        acceleratorType: "{{ acceleratorType }}"
        versionUpgradeOption: "{{ versionUpgradeOption }}"
        capabilities: "{{ capabilities }}"
        computeId: "{{ computeId }}"
        priority: "{{ priority }}"
        acceleratorsPerInstance: {{ acceleratorsPerInstance }}
        totalAccelerators: {{ totalAccelerators }}
        provisioningState: "{{ provisioningState }}"
        provisioningDetails:
          message: "{{ message }}"
          lastOperationTimestamp: "{{ lastOperationTimestamp }}"
        routes:
          chatCompletionsScoringPath: "{{ chatCompletionsScoringPath }}"
          swagger: "{{ swagger }}"
          messagesApiScoringPath: "{{ messagesApiScoringPath }}"
    - name: sku
      description: |
        The resource model definition representing SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
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

Updates the specified managed compute deployment associated with the Cognitive Services account.

```sql
UPDATE azure.cognitive_services.managed_compute_deployments
SET 
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
sku,
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

Creates or updates a managed compute deployment associated with the Cognitive Services account.

```sql
REPLACE azure.cognitive_services.managed_compute_deployments
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
sku,
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

Deletes the specified managed compute deployment associated with the Cognitive Services account.

```sql
DELETE FROM azure.cognitive_services.managed_compute_deployments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
