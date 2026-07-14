--- 
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.deployments" /></td></tr>
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
    <td><CopyableCode code="callRateLimit" /></td>
    <td><code>object</code></td>
    <td>The call rate limit Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>The capabilities.</td>
</tr>
<tr>
    <td><CopyableCode code="capacitySettings" /></td>
    <td><code>object</code></td>
    <td>Internal use only.</td>
</tr>
<tr>
    <td><CopyableCode code="currentCapacity" /></td>
    <td><code>integer</code></td>
    <td>The current capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentState" /></td>
    <td><code>string</code></td>
    <td>The state of the deployment. Controls whether the deployment is accepting inference requests. Use 'Running' for active deployments that process requests, or 'Paused' to temporarily stop inference while preserving the deployment configuration. Known values are: "Running" and "Paused". (Running, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicThrottlingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If the dynamic throttling is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>object</code></td>
    <td>Properties of Cognitive Services account deployment model.</td>
</tr>
<tr>
    <td><CopyableCode code="parentDeploymentName" /></td>
    <td><code>string</code></td>
    <td>The name of parent deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the resource at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", "Disabled", and "Canceled". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Disabled, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="raiPolicyName" /></td>
    <td><code>string</code></td>
    <td>The name of RAI policy.</td>
</tr>
<tr>
    <td><CopyableCode code="rateLimits" /></td>
    <td><code>array</code></td>
    <td>:vartype rate_limits: list[~azure.mgmt.cognitiveservices.models.ThrottlingRule]</td>
</tr>
<tr>
    <td><CopyableCode code="routing" /></td>
    <td><code>object</code></td>
    <td>Routing configuration for the model-router deployment. This property is only applicable when the deployed model is 'model-router' version 2025-11-18 or later. Allows you to select the models subset for routing and the routing mode (balanced, quality, cost) for routing across all supported models or the model subset.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSettings" /></td>
    <td><code>object</code></td>
    <td>Properties of Cognitive Services account deployment model. (Deprecated, please use Deployment.sku instead.).</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTier" /></td>
    <td><code>string</code></td>
    <td>The service tier for the deployment. Determines the pricing and performance level for request processing. Use 'Default' for standard pricing or 'Priority' for higher-priority processing with premium pricing. Note: Pause operations are only supported on Standard, DataZoneStandard, and GlobalStandard SKUs. Known values are: "Default" and "Priority". (Default, Priority)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="speculativeDecoding" /></td>
    <td><code>object</code></td>
    <td>Speculative decoding settings for the deployment. This configuration applies to Fireworks model formats.</td>
</tr>
<tr>
    <td><CopyableCode code="spilloverDeploymentName" /></td>
    <td><code>string</code></td>
    <td>Specifies the deployment name that should serve requests when the request would have otherwise been throttled due to reaching current deployment throughput limit.</td>
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
    <td><CopyableCode code="versionUpgradeOption" /></td>
    <td><code>string</code></td>
    <td>Deployment model version upgrade option. Known values are: "OnceNewDefaultVersionAvailable", "OnceCurrentVersionExpired", and "NoAutoUpgrade". (OnceNewDefaultVersionAvailable, OnceCurrentVersionExpired, NoAutoUpgrade)</td>
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
    <td><CopyableCode code="callRateLimit" /></td>
    <td><code>object</code></td>
    <td>The call rate limit Cognitive Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>The capabilities.</td>
</tr>
<tr>
    <td><CopyableCode code="capacitySettings" /></td>
    <td><code>object</code></td>
    <td>Internal use only.</td>
</tr>
<tr>
    <td><CopyableCode code="currentCapacity" /></td>
    <td><code>integer</code></td>
    <td>The current capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentState" /></td>
    <td><code>string</code></td>
    <td>The state of the deployment. Controls whether the deployment is accepting inference requests. Use 'Running' for active deployments that process requests, or 'Paused' to temporarily stop inference while preserving the deployment configuration. Known values are: "Running" and "Paused". (Running, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicThrottlingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If the dynamic throttling is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>object</code></td>
    <td>Properties of Cognitive Services account deployment model.</td>
</tr>
<tr>
    <td><CopyableCode code="parentDeploymentName" /></td>
    <td><code>string</code></td>
    <td>The name of parent deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the resource at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", "Disabled", and "Canceled". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Disabled, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="raiPolicyName" /></td>
    <td><code>string</code></td>
    <td>The name of RAI policy.</td>
</tr>
<tr>
    <td><CopyableCode code="rateLimits" /></td>
    <td><code>array</code></td>
    <td>:vartype rate_limits: list[~azure.mgmt.cognitiveservices.models.ThrottlingRule]</td>
</tr>
<tr>
    <td><CopyableCode code="routing" /></td>
    <td><code>object</code></td>
    <td>Routing configuration for the model-router deployment. This property is only applicable when the deployed model is 'model-router' version 2025-11-18 or later. Allows you to select the models subset for routing and the routing mode (balanced, quality, cost) for routing across all supported models or the model subset.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSettings" /></td>
    <td><code>object</code></td>
    <td>Properties of Cognitive Services account deployment model. (Deprecated, please use Deployment.sku instead.).</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTier" /></td>
    <td><code>string</code></td>
    <td>The service tier for the deployment. Determines the pricing and performance level for request processing. Use 'Default' for standard pricing or 'Priority' for higher-priority processing with premium pricing. Note: Pause operations are only supported on Standard, DataZoneStandard, and GlobalStandard SKUs. Known values are: "Default" and "Priority". (Default, Priority)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="speculativeDecoding" /></td>
    <td><code>object</code></td>
    <td>Speculative decoding settings for the deployment. This configuration applies to Fireworks model formats.</td>
</tr>
<tr>
    <td><CopyableCode code="spilloverDeploymentName" /></td>
    <td><code>string</code></td>
    <td>Specifies the deployment name that should serve requests when the request would have otherwise been throttled due to reaching current deployment throughput limit.</td>
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
    <td><CopyableCode code="versionUpgradeOption" /></td>
    <td><code>string</code></td>
    <td>Deployment model version upgrade option. Known values are: "OnceNewDefaultVersionAvailable", "OnceCurrentVersionExpired", and "NoAutoUpgrade". (OnceNewDefaultVersionAvailable, OnceCurrentVersionExpired, NoAutoUpgrade)</td>
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
    <td>Gets the specified deployments associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the deployments associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified deployments associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update specified deployments associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified deployments associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified deployment associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the specified deployments skus associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Pause a deployment. Pauses inferencing on a deployment by setting the deploymentState to 'Paused' (see #/definitions/DeploymentProperties/properties/deploymentState). Only Standard, DataZoneStandard, and GlobalStandard SKUs support this operation. Inference requests to the paused deployment endpoint will receive HTTP 423 (Locked). This operation is idempotent.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resume a deployment. Resumes inferencing on a previously paused deployment by setting the deploymentState to 'Running' (see #/definitions/DeploymentProperties/properties/deploymentState). This operation is idempotent and can be safely called on already running deployments.</td>
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
    <td>The name of the deployment associated with the Cognitive Services Account. Required.</td>
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

Gets the specified deployments associated with the Cognitive Services account.

```sql
SELECT
id,
name,
callRateLimit,
capabilities,
capacitySettings,
currentCapacity,
deploymentState,
dynamicThrottlingEnabled,
etag,
model,
parentDeploymentName,
provisioningState,
raiPolicyName,
rateLimits,
routing,
scaleSettings,
serviceTier,
sku,
speculativeDecoding,
spilloverDeploymentName,
systemData,
tags,
type,
versionUpgradeOption
FROM azure.cognitive_services.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the deployments associated with the Cognitive Services account.

```sql
SELECT
id,
name,
callRateLimit,
capabilities,
capacitySettings,
currentCapacity,
deploymentState,
dynamicThrottlingEnabled,
etag,
model,
parentDeploymentName,
provisioningState,
raiPolicyName,
rateLimits,
routing,
scaleSettings,
serviceTier,
sku,
speculativeDecoding,
spilloverDeploymentName,
systemData,
tags,
type,
versionUpgradeOption
FROM azure.cognitive_services.deployments
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

Update the state of specified deployments associated with the Cognitive Services account.

```sql
INSERT INTO azure.cognitive_services.deployments (
properties,
sku,
tags,
resource_group_name,
account_name,
deployment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ sku }}',
'{{ tags }}',
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
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: deployments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the deployments resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the deployments resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the deployments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the deployments resource.
    - name: properties
      description: |
        Properties of Cognitive Services account deployment.
      value:
        provisioningState: "{{ provisioningState }}"
        model:
          publisher: "{{ publisher }}"
          format: "{{ format }}"
          name: "{{ name }}"
          version: "{{ version }}"
          source: "{{ source }}"
          sourceAccount: "{{ sourceAccount }}"
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
        speculativeDecoding:
          draftModel:
            publisher: "{{ publisher }}"
            format: "{{ format }}"
            name: "{{ name }}"
            version: "{{ version }}"
            source: "{{ source }}"
            sourceAccount: "{{ sourceAccount }}"
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
          draftTokenCount: {{ draftTokenCount }}
        scaleSettings:
          scaleType: "{{ scaleType }}"
          capacity: {{ capacity }}
          activeCapacity: {{ activeCapacity }}
        capabilities: "{{ capabilities }}"
        raiPolicyName: "{{ raiPolicyName }}"
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
        rateLimits:
          - key: "{{ key }}"
            renewalPeriod: {{ renewalPeriod }}
            count: {{ count }}
            minCount: {{ minCount }}
            dynamicThrottlingEnabled: {{ dynamicThrottlingEnabled }}
            matchPatterns: "{{ matchPatterns }}"
        versionUpgradeOption: "{{ versionUpgradeOption }}"
        dynamicThrottlingEnabled: {{ dynamicThrottlingEnabled }}
        currentCapacity: {{ currentCapacity }}
        capacitySettings:
          designatedCapacity: {{ designatedCapacity }}
          priority: {{ priority }}
        parentDeploymentName: "{{ parentDeploymentName }}"
        spilloverDeploymentName: "{{ spilloverDeploymentName }}"
        serviceTier: "{{ serviceTier }}"
        deploymentState: "{{ deploymentState }}"
        routing:
          mode: "{{ mode }}"
          models:
            - publisher: "{{ publisher }}"
              format: "{{ format }}"
              name: "{{ name }}"
              version: "{{ version }}"
              source: "{{ source }}"
              sourceAccount: "{{ sourceAccount }}"
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
    - name: sku
      description: |
        The resource model definition representing SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
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

Update specified deployments associated with the Cognitive Services account.

```sql
UPDATE azure.cognitive_services.deployments
SET 
tags = '{{ tags }}',
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
tags,
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

Update the state of specified deployments associated with the Cognitive Services account.

```sql
REPLACE azure.cognitive_services.deployments
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
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

Deletes the specified deployment associated with the Cognitive Services account.

```sql
DELETE FROM azure.cognitive_services.deployments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_skus"
    values={[
        { label: 'list_skus', value: 'list_skus' },
        { label: 'pause', value: 'pause' },
        { label: 'resume', value: 'resume' }
    ]}
>
<TabItem value="list_skus">

Lists the specified deployments skus associated with the Cognitive Services account.

```sql
EXEC azure.cognitive_services.deployments.list_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="pause">

Pause a deployment. Pauses inferencing on a deployment by setting the deploymentState to 'Paused' (see #/definitions/DeploymentProperties/properties/deploymentState). Only Standard, DataZoneStandard, and GlobalStandard SKUs support this operation. Inference requests to the paused deployment endpoint will receive HTTP 423 (Locked). This operation is idempotent.

```sql
EXEC azure.cognitive_services.deployments.pause 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resume a deployment. Resumes inferencing on a previously paused deployment by setting the deploymentState to 'Running' (see #/definitions/DeploymentProperties/properties/deploymentState). This operation is idempotent and can be safely called on already running deployments.

```sql
EXEC azure.cognitive_services.deployments.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
