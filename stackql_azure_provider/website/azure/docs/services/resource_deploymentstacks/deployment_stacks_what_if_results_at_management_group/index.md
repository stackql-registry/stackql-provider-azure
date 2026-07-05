--- 
title: deployment_stacks_what_if_results_at_management_group
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_stacks_what_if_results_at_management_group
  - resource_deploymentstacks
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

Creates, updates, deletes, gets or lists a <code>deployment_stacks_what_if_results_at_management_group</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployment_stacks_what_if_results_at_management_group" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_deploymentstacks.deployment_stacks_what_if_results_at_management_group" /></td></tr>
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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="changes" /></td>
    <td><code>object</code></td>
    <td>All of the changes predicted by the deployment stack what-if operation.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStackLastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp for when the deployment stack was last modified. This can be used to determine if the what-if data is still current.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStackResourceId" /></td>
    <td><code>string</code></td>
    <td>The deployment stack id to use as the basis for comparison. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>List of resource diagnostics detected by What-If operation.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInterval" /></td>
    <td><code>string</code></td>
    <td>The interval to persist the deployment stack what-if result in ISO 8601 format. Required.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="changes" /></td>
    <td><code>object</code></td>
    <td>All of the changes predicted by the deployment stack what-if operation.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStackLastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp for when the deployment stack was last modified. This can be used to determine if the what-if data is still current.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStackResourceId" /></td>
    <td><code>string</code></td>
    <td>The deployment stack id to use as the basis for comparison. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>List of resource diagnostics detected by What-If operation.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInterval" /></td>
    <td><code>string</code></td>
    <td>The interval to persist the deployment stack what-if result in ISO 8601 format. Required.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
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
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stacks_what_if_result_name"><code>deployment_stacks_what_if_result_name</code></a></td>
    <td></td>
    <td>Gets the Deployment stack with the given name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td></td>
    <td>Lists Deployment stacks at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stacks_what_if_result_name"><code>deployment_stacks_what_if_result_name</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stacks_what_if_result_name"><code>deployment_stacks_what_if_result_name</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stacks_what_if_result_name"><code>deployment_stacks_what_if_result_name</code></a></td>
    <td><a href="#parameter-unmanageAction.Resources"><code>unmanageAction.Resources</code></a>, <a href="#parameter-unmanageAction.ResourceGroups"><code>unmanageAction.ResourceGroups</code></a>, <a href="#parameter-unmanageAction.ManagementGroups"><code>unmanageAction.ManagementGroups</code></a>, <a href="#parameter-unmanageAction.ResourcesWithoutDeleteSupport"><code>unmanageAction.ResourcesWithoutDeleteSupport</code></a>, <a href="#parameter-bypassStackOutOfSyncError"><code>bypassStackOutOfSyncError</code></a></td>
    <td>Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.</td>
</tr>
<tr>
    <td><a href="#what_if"><CopyableCode code="what_if" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stacks_what_if_result_name"><code>deployment_stacks_what_if_result_name</code></a></td>
    <td></td>
    <td>Returns property-level changes that will be made by the deployment if executed.</td>
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
<tr id="parameter-deployment_stacks_what_if_result_name">
    <td><CopyableCode code="deployment_stacks_what_if_result_name" /></td>
    <td><code>string</code></td>
    <td>Name of the deployment stack what-if result. Required.</td>
</tr>
<tr id="parameter-management_group_id">
    <td><CopyableCode code="management_group_id" /></td>
    <td><code>string</code></td>
    <td>The management group ID. Required.</td>
</tr>
<tr id="parameter-bypassStackOutOfSyncError">
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized. Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.ManagementGroups">
    <td><CopyableCode code="unmanageAction.ManagementGroups" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate delete rather than detach for unmanaged management groups. Known values are: "delete" and "detach". Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.ResourceGroups">
    <td><CopyableCode code="unmanageAction.ResourceGroups" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate delete rather than detach for unmanaged resource groups. Known values are: "delete" and "detach". Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.Resources">
    <td><CopyableCode code="unmanageAction.Resources" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate delete rather than detach for unmanaged resources. Known values are: "delete" and "detach". Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.ResourcesWithoutDeleteSupport">
    <td><CopyableCode code="unmanageAction.ResourcesWithoutDeleteSupport" /></td>
    <td><code>string</code></td>
    <td>Some resources do not support deletion. This flag will denote how the stack should handle those resources. Known values are: "detach" and "fail". Default value is None.</td>
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

Gets the Deployment stack with the given name.

```sql
SELECT
id,
name,
actionOnUnmanage,
changes,
correlationId,
debugSetting,
denySettings,
deploymentScope,
deploymentStackLastModified,
deploymentStackResourceId,
description,
diagnostics,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
location,
parameters,
parametersLink,
provisioningState,
retentionInterval,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks_what_if_results_at_management_group
WHERE management_group_id = '{{ management_group_id }}' -- required
AND deployment_stacks_what_if_result_name = '{{ deployment_stacks_what_if_result_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Deployment stacks at the specified scope.

```sql
SELECT
id,
name,
actionOnUnmanage,
changes,
correlationId,
debugSetting,
denySettings,
deploymentScope,
deploymentStackLastModified,
deploymentStackResourceId,
description,
diagnostics,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
location,
parameters,
parametersLink,
provisioningState,
retentionInterval,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks_what_if_results_at_management_group
WHERE management_group_id = '{{ management_group_id }}' -- required
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

Creates or updates a Deployment stack at the specified scope.

```sql
INSERT INTO azure.resource_deploymentstacks.deployment_stacks_what_if_results_at_management_group (
properties,
location,
tags,
management_group_id,
deployment_stacks_what_if_result_name
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ management_group_id }}',
'{{ deployment_stacks_what_if_result_name }}'
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
- name: deployment_stacks_what_if_results_at_management_group
  props:
    - name: management_group_id
      value: "{{ management_group_id }}"
      description: Required parameter for the deployment_stacks_what_if_results_at_management_group resource.
    - name: deployment_stacks_what_if_result_name
      value: "{{ deployment_stacks_what_if_result_name }}"
      description: Required parameter for the deployment_stacks_what_if_results_at_management_group resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        error:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          details:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
          additionalInfo:
            - type: "{{ type }}"
              info: "{{ info }}"
        template: "{{ template }}"
        templateLink:
          uri: "{{ uri }}"
          id: "{{ id }}"
          relativePath: "{{ relativePath }}"
          queryString: "{{ queryString }}"
          contentVersion: "{{ contentVersion }}"
        parameters: "{{ parameters }}"
        parametersLink:
          uri: "{{ uri }}"
          contentVersion: "{{ contentVersion }}"
        extensionConfigs: "{{ extensionConfigs }}"
        externalInputs: "{{ externalInputs }}"
        externalInputDefinitions: "{{ externalInputDefinitions }}"
        actionOnUnmanage:
          resources: "{{ resources }}"
          resourceGroups: "{{ resourceGroups }}"
          managementGroups: "{{ managementGroups }}"
          resourcesWithoutDeleteSupport: "{{ resourcesWithoutDeleteSupport }}"
        debugSetting:
          detailLevel: "{{ detailLevel }}"
        deploymentScope: "{{ deploymentScope }}"
        description: "{{ description }}"
        denySettings:
          mode: "{{ mode }}"
          excludedPrincipals:
            - "{{ excludedPrincipals }}"
          excludedActions:
            - "{{ excludedActions }}"
          applyToChildScopes: {{ applyToChildScopes }}
        provisioningState: "{{ provisioningState }}"
        correlationId: "{{ correlationId }}"
        validationLevel: "{{ validationLevel }}"
        deploymentStackResourceId: "{{ deploymentStackResourceId }}"
        deploymentStackLastModified: "{{ deploymentStackLastModified }}"
        retentionInterval: "{{ retentionInterval }}"
        changes:
          resourceChanges:
            - id: "{{ id }}"
              extension:
                name: "{{ name }}"
                version: "{{ version }}"
                configId: "{{ configId }}"
                config: "{{ config }}"
              type: "{{ type }}"
              identifiers: "{{ identifiers }}"
              apiVersion: "{{ apiVersion }}"
              deploymentId: "{{ deploymentId }}"
              symbolicName: "{{ symbolicName }}"
              changeType: "{{ changeType }}"
              changeCertainty: "{{ changeCertainty }}"
              managementStatusChange:
                before: "{{ before }}"
                after: "{{ after }}"
              denyStatusChange:
                before: "{{ before }}"
                after: "{{ after }}"
              unsupportedReason: "{{ unsupportedReason }}"
              resourceConfigurationChanges:
                before: "{{ before }}"
                after: "{{ after }}"
                delta:
                  - before: "{{ before }}"
                    after: "{{ after }}"
                    path: "{{ path }}"
                    changeType: "{{ changeType }}"
                    children: "{{ children }}"
          denySettingsChange:
            before:
              mode: "{{ mode }}"
              excludedPrincipals:
                - "{{ excludedPrincipals }}"
              excludedActions:
                - "{{ excludedActions }}"
              applyToChildScopes: {{ applyToChildScopes }}
            after:
              mode: "{{ mode }}"
              excludedPrincipals:
                - "{{ excludedPrincipals }}"
              excludedActions:
                - "{{ excludedActions }}"
              applyToChildScopes: {{ applyToChildScopes }}
            delta:
              - before: "{{ before }}"
                after: "{{ after }}"
                path: "{{ path }}"
                changeType: "{{ changeType }}"
                children: "{{ children }}"
          deploymentScopeChange:
            before: "{{ before }}"
            after: "{{ after }}"
        diagnostics:
          - level: "{{ level }}"
            code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            additionalInfo: "{{ additionalInfo }}"
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
`}</CodeBlock>

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

Creates or updates a Deployment stack at the specified scope.

```sql
REPLACE azure.resource_deploymentstacks.deployment_stacks_what_if_results_at_management_group
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
management_group_id = '{{ management_group_id }}' --required
AND deployment_stacks_what_if_result_name = '{{ deployment_stacks_what_if_result_name }}' --required
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

Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.

```sql
DELETE FROM azure.resource_deploymentstacks.deployment_stacks_what_if_results_at_management_group
WHERE management_group_id = '{{ management_group_id }}' --required
AND deployment_stacks_what_if_result_name = '{{ deployment_stacks_what_if_result_name }}' --required
AND unmanageAction.Resources = '{{ unmanageAction.Resources }}'
AND unmanageAction.ResourceGroups = '{{ unmanageAction.ResourceGroups }}'
AND unmanageAction.ManagementGroups = '{{ unmanageAction.ManagementGroups }}'
AND unmanageAction.ResourcesWithoutDeleteSupport = '{{ unmanageAction.ResourcesWithoutDeleteSupport }}'
AND bypassStackOutOfSyncError = '{{ bypassStackOutOfSyncError }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="what_if"
    values={[
        { label: 'what_if', value: 'what_if' }
    ]}
>
<TabItem value="what_if">

Returns property-level changes that will be made by the deployment if executed.

```sql
EXEC azure.resource_deploymentstacks.deployment_stacks_what_if_results_at_management_group.what_if 
@management_group_id='{{ management_group_id }}' --required, 
@deployment_stacks_what_if_result_name='{{ deployment_stacks_what_if_result_name }}' --required
;
```
</TabItem>
</Tabs>
