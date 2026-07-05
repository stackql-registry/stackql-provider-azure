--- 
title: workflow
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow
  - devhub
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>workflow</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workflow" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.devhub.workflow" /></td></tr>
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
    <td><CopyableCode code="artifactGenerationProperties" /></td>
    <td><code>object</code></td>
    <td>Properties for generating artifacts like dockerfile and manifests.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePipelineProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of an azure pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="githubWorkflowProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of a github workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
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
    <td><CopyableCode code="templateWorkflowProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of an template workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="artifactGenerationProperties" /></td>
    <td><code>object</code></td>
    <td>Properties for generating artifacts like dockerfile and manifests.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePipelineProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of an azure pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="githubWorkflowProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of a github workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
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
    <td><CopyableCode code="templateWorkflowProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of an template workflow.</td>
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
    <td><CopyableCode code="artifactGenerationProperties" /></td>
    <td><code>object</code></td>
    <td>Properties for generating artifacts like dockerfile and manifests.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePipelineProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of an azure pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="githubWorkflowProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of a github workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
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
    <td><CopyableCode code="templateWorkflowProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of an template workflow.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a workflow. Gets a workflow.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-managedClusterResource"><code>managedClusterResource</code></a></td>
    <td>Gets a list of workflows within a resource group. Gets a list of workflows within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of workflows associated with the specified subscription. Gets a list of workflows associated with the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a workflow. Creates or updates a workflow.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags on a workflow. Updates tags on a workflow.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a workflow. Creates or updates a workflow.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a workflow. Deletes a workflow.</td>
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
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workflow resource. Required.</td>
</tr>
<tr id="parameter-managedClusterResource">
    <td><CopyableCode code="managedClusterResource" /></td>
    <td><code>string</code></td>
    <td>The ManagedCluster resource associated with the workflows. Default value is None.</td>
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

Gets a workflow. Gets a workflow.

```sql
SELECT
id,
name,
artifactGenerationProperties,
azurePipelineProfile,
githubWorkflowProfile,
location,
systemData,
tags,
templateWorkflowProfile,
type
FROM azure_extras.devhub.workflow
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of workflows within a resource group. Gets a list of workflows within a resource group.

```sql
SELECT
id,
name,
artifactGenerationProperties,
azurePipelineProfile,
githubWorkflowProfile,
location,
systemData,
tags,
templateWorkflowProfile,
type
FROM azure_extras.devhub.workflow
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND managedClusterResource = '{{ managedClusterResource }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of workflows associated with the specified subscription. Gets a list of workflows associated with the specified subscription.

```sql
SELECT
id,
name,
artifactGenerationProperties,
azurePipelineProfile,
githubWorkflowProfile,
location,
systemData,
tags,
templateWorkflowProfile,
type
FROM azure_extras.devhub.workflow
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a workflow. Creates or updates a workflow.

```sql
INSERT INTO azure_extras.devhub.workflow (
tags,
location,
properties,
resource_group_name,
workflow_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workflow_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workflow
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workflow resource.
    - name: workflow_name
      value: "{{ workflow_name }}"
      description: Required parameter for the workflow resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workflow resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of a workflow.
      value:
        githubWorkflowProfile:
          repositoryOwner: "{{ repositoryOwner }}"
          repositoryName: "{{ repositoryName }}"
          branchName: "{{ branchName }}"
          dockerfile: "{{ dockerfile }}"
          dockerBuildContext: "{{ dockerBuildContext }}"
          deploymentProperties:
            manifestType: "{{ manifestType }}"
            kubeManifestLocations:
              - "{{ kubeManifestLocations }}"
            helmChartPath: "{{ helmChartPath }}"
            helmValues: "{{ helmValues }}"
            overrides: "{{ overrides }}"
          namespace: "{{ namespace }}"
          acr:
            acrSubscriptionId: "{{ acrSubscriptionId }}"
            acrResourceGroup: "{{ acrResourceGroup }}"
            acrRegistryName: "{{ acrRegistryName }}"
            acrRepositoryName: "{{ acrRepositoryName }}"
          oidcCredentials:
            azureClientId: "{{ azureClientId }}"
            azureTenantId: "{{ azureTenantId }}"
          aksResourceId: "{{ aksResourceId }}"
          prURL: "{{ prURL }}"
          pullNumber: {{ pullNumber }}
          prStatus: "{{ prStatus }}"
          lastWorkflowRun:
            succeeded: {{ succeeded }}
            workflowRunURL: "{{ workflowRunURL }}"
            lastRunAt: "{{ lastRunAt }}"
            workflowRunStatus: "{{ workflowRunStatus }}"
          authStatus: "{{ authStatus }}"
        artifactGenerationProperties:
          generationLanguage: "{{ generationLanguage }}"
          languageVersion: "{{ languageVersion }}"
          builderVersion: "{{ builderVersion }}"
          port: "{{ port }}"
          appName: "{{ appName }}"
          dockerfileOutputDirectory: "{{ dockerfileOutputDirectory }}"
          manifestOutputDirectory: "{{ manifestOutputDirectory }}"
          dockerfileGenerationMode: "{{ dockerfileGenerationMode }}"
          manifestGenerationMode: "{{ manifestGenerationMode }}"
          manifestType: "{{ manifestType }}"
          imageName: "{{ imageName }}"
          namespace: "{{ namespace }}"
          imageTag: "{{ imageTag }}"
        azurePipelineProfile:
          repository:
            repositoryOwner: "{{ repositoryOwner }}"
            repositoryName: "{{ repositoryName }}"
            branchName: "{{ branchName }}"
            adoOrganization: "{{ adoOrganization }}"
            projectName: "{{ projectName }}"
          armServiceConnection: "{{ armServiceConnection }}"
          build:
            dockerfile: "{{ dockerfile }}"
            dockerBuildContext: "{{ dockerBuildContext }}"
          deployment:
            manifestType: "{{ manifestType }}"
            kubeManifestLocations:
              - "{{ kubeManifestLocations }}"
            helmChartPath: "{{ helmChartPath }}"
            helmValues: "{{ helmValues }}"
            overrides: "{{ overrides }}"
          namespace: "{{ namespace }}"
          acr: "{{ acr }}"
          clusterId: "{{ clusterId }}"
          pullRequest:
            prURL: "{{ prURL }}"
            pullNumber: {{ pullNumber }}
            prStatus: "{{ prStatus }}"
          lastWorkflowRun:
            succeeded: {{ succeeded }}
            workflowRunURL: "{{ workflowRunURL }}"
            lastRunAt: "{{ lastRunAt }}"
            workflowRunStatus: "{{ workflowRunStatus }}"
          authStatus: "{{ authStatus }}"
        templateWorkflowProfile:
          repositoryProvider: "{{ repositoryProvider }}"
          workflowTemplate:
            templateId: "{{ templateId }}"
            destination: "{{ destination }}"
            parameters: "{{ parameters }}"
          deploymentTemplate:
            templateId: "{{ templateId }}"
            destination: "{{ destination }}"
            parameters: "{{ parameters }}"
          dockerfileTemplate:
            templateId: "{{ templateId }}"
            destination: "{{ destination }}"
            parameters: "{{ parameters }}"
          manifestTemplates:
            - templateId: "{{ templateId }}"
              destination: "{{ destination }}"
              parameters: "{{ parameters }}"
          gitHubProviderProfile:
            repository:
              repositoryOwner: "{{ repositoryOwner }}"
              repositoryName: "{{ repositoryName }}"
              branchName: "{{ branchName }}"
            oidcCredentials:
              azureClientId: "{{ azureClientId }}"
              azureTenantId: "{{ azureTenantId }}"
          adoProviderProfile:
            repository:
              repositoryOwner: "{{ repositoryOwner }}"
              repositoryName: "{{ repositoryName }}"
              branchName: "{{ branchName }}"
              adoOrganization: "{{ adoOrganization }}"
              projectName: "{{ projectName }}"
            armServiceConnection: "{{ armServiceConnection }}"
          pullRequest:
            prURL: "{{ prURL }}"
            pullNumber: {{ pullNumber }}
            prStatus: "{{ prStatus }}"
          lastWorkflowRun:
            succeeded: {{ succeeded }}
            workflowRunURL: "{{ workflowRunURL }}"
            lastRunAt: "{{ lastRunAt }}"
            workflowRunStatus: "{{ workflowRunStatus }}"
          authStatus: "{{ authStatus }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates tags on a workflow. Updates tags on a workflow.

```sql
UPDATE azure_extras.devhub.workflow
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Creates or updates a workflow. Creates or updates a workflow.

```sql
REPLACE azure_extras.devhub.workflow
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
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

Deletes a workflow. Deletes a workflow.

```sql
DELETE FROM azure_extras.devhub.workflow
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
