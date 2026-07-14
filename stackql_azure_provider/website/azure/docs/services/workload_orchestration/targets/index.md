--- 
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - workload_orchestration
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

Creates, updates, deletes, gets or lists a <code>targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="targets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.workload_orchestration.targets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>List of capabilities. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contextId" /></td>
    <td><code>string</code></td>
    <td>ArmId of Context. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of target. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of target. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_location: ~azure.mgmt.workloadorchestration.models.ExtendedLocation</td>
</tr>
<tr>
    <td><CopyableCode code="hierarchyLevel" /></td>
    <td><code>string</code></td>
    <td>Hierarchy Level. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of resource. Known values are: "Succeeded", "Failed", "Canceled", "Initialized", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, Initialized, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="solutionScope" /></td>
    <td><code>string</code></td>
    <td>Scope of the target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of resource. Known values are: "active" and "inactive". (active, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of target.</td>
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
    <td><CopyableCode code="targetSpecification" /></td>
    <td><code>object</code></td>
    <td>target spec. Required.</td>
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
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>List of capabilities. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contextId" /></td>
    <td><code>string</code></td>
    <td>ArmId of Context. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of target. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of target. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_location: ~azure.mgmt.workloadorchestration.models.ExtendedLocation</td>
</tr>
<tr>
    <td><CopyableCode code="hierarchyLevel" /></td>
    <td><code>string</code></td>
    <td>Hierarchy Level. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of resource. Known values are: "Succeeded", "Failed", "Canceled", "Initialized", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, Initialized, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="solutionScope" /></td>
    <td><code>string</code></td>
    <td>Scope of the target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of resource. Known values are: "active" and "inactive". (active, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of target.</td>
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
    <td><CopyableCode code="targetSpecification" /></td>
    <td><code>object</code></td>
    <td>target spec. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>List of capabilities. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contextId" /></td>
    <td><code>string</code></td>
    <td>ArmId of Context. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of target. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of target. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_location: ~azure.mgmt.workloadorchestration.models.ExtendedLocation</td>
</tr>
<tr>
    <td><CopyableCode code="hierarchyLevel" /></td>
    <td><code>string</code></td>
    <td>Hierarchy Level. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of resource. Known values are: "Succeeded", "Failed", "Canceled", "Initialized", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, Initialized, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="solutionScope" /></td>
    <td><code>string</code></td>
    <td>Scope of the target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of resource. Known values are: "active" and "inactive". (active, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of target.</td>
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
    <td><CopyableCode code="targetSpecification" /></td>
    <td><code>object</code></td>
    <td>target spec. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Target Resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List by specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List by subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a Target Resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>update a Target Resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a Target Resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDelete"><code>forceDelete</code></a></td>
    <td>Delete a Target Resource.</td>
</tr>
<tr>
    <td><a href="#install_solution"><CopyableCode code="install_solution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solutionVersionId"><code>solutionVersionId</code></a></td>
    <td></td>
    <td>Post request to deploy.</td>
</tr>
<tr>
    <td><a href="#uninstall_solution"><CopyableCode code="uninstall_solution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solutionTemplateId"><code>solutionTemplateId</code></a></td>
    <td></td>
    <td>Post request to uninstall.</td>
</tr>
<tr>
    <td><a href="#remove_revision"><CopyableCode code="remove_revision" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solutionTemplateId"><code>solutionTemplateId</code></a>, <a href="#parameter-solutionVersion"><code>solutionVersion</code></a></td>
    <td></td>
    <td>Post request to remove solution version revision.</td>
</tr>
<tr>
    <td><a href="#resolve_configuration"><CopyableCode code="resolve_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solutionTemplateVersionId"><code>solutionTemplateVersionId</code></a></td>
    <td></td>
    <td>Post request to resolve configuration.</td>
</tr>
<tr>
    <td><a href="#review_solution_version"><CopyableCode code="review_solution_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solutionTemplateVersionId"><code>solutionTemplateVersionId</code></a></td>
    <td></td>
    <td>Post request to review configuration.</td>
</tr>
<tr>
    <td><a href="#publish_solution_version"><CopyableCode code="publish_solution_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solutionVersionId"><code>solutionVersionId</code></a></td>
    <td></td>
    <td>Post request to publish.</td>
</tr>
<tr>
    <td><a href="#update_external_validation_status"><CopyableCode code="update_external_validation_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solutionVersionId"><code>solutionVersionId</code></a>, <a href="#parameter-externalValidationId"><code>externalValidationId</code></a>, <a href="#parameter-validationStatus"><code>validationStatus</code></a></td>
    <td></td>
    <td>Post request to update external validation status.</td>
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
<tr id="parameter-target_name">
    <td><CopyableCode code="target_name" /></td>
    <td><code>string</code></td>
    <td>Name of the target. Required.</td>
</tr>
<tr id="parameter-forceDelete">
    <td><CopyableCode code="forceDelete" /></td>
    <td><code>boolean</code></td>
    <td>Force delete. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a Target Resource.

```sql
SELECT
id,
name,
capabilities,
contextId,
description,
displayName,
eTag,
extendedLocation,
hierarchyLevel,
location,
provisioningState,
solutionScope,
state,
status,
systemData,
tags,
targetSpecification,
type
FROM azure.workload_orchestration.targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND target_name = '{{ target_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List by specified resource group.

```sql
SELECT
id,
name,
capabilities,
contextId,
description,
displayName,
eTag,
extendedLocation,
hierarchyLevel,
location,
provisioningState,
solutionScope,
state,
status,
systemData,
tags,
targetSpecification,
type
FROM azure.workload_orchestration.targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List by subscription.

```sql
SELECT
id,
name,
capabilities,
contextId,
description,
displayName,
eTag,
extendedLocation,
hierarchyLevel,
location,
provisioningState,
solutionScope,
state,
status,
systemData,
tags,
targetSpecification,
type
FROM azure.workload_orchestration.targets
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

Create or update a Target Resource.

```sql
INSERT INTO azure.workload_orchestration.targets (
tags,
location,
properties,
extendedLocation,
resource_group_name,
target_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ target_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
extendedLocation,
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
- name: targets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the targets resource.
    - name: target_name
      value: "{{ target_name }}"
      description: Required parameter for the targets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the targets resource.
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
        The resource-specific properties for this resource.
      value:
        description: "{{ description }}"
        displayName: "{{ displayName }}"
        contextId: "{{ contextId }}"
        targetSpecification: "{{ targetSpecification }}"
        capabilities:
          - "{{ capabilities }}"
        hierarchyLevel: "{{ hierarchyLevel }}"
        status:
          lastModified: "{{ lastModified }}"
          deployed: {{ deployed }}
          expectedRunningJobId: {{ expectedRunningJobId }}
          runningJobId: {{ runningJobId }}
          status: "{{ status }}"
          statusDetails: "{{ statusDetails }}"
          generation: {{ generation }}
          targetStatuses:
            - name: "{{ name }}"
              status: "{{ status }}"
              componentStatuses: "{{ componentStatuses }}"
        solutionScope: "{{ solutionScope }}"
        state: "{{ state }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        :vartype extended_location: ~azure.mgmt.workloadorchestration.models.ExtendedLocation
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

update a Target Resource.

```sql
UPDATE azure.workload_orchestration.targets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND target_name = '{{ target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
eTag,
extendedLocation,
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

Create or update a Target Resource.

```sql
REPLACE azure.workload_orchestration.targets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND target_name = '{{ target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
eTag,
extendedLocation,
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

Delete a Target Resource.

```sql
DELETE FROM azure.workload_orchestration.targets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND target_name = '{{ target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDelete = '{{ forceDelete }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="install_solution"
    values={[
        { label: 'install_solution', value: 'install_solution' },
        { label: 'uninstall_solution', value: 'uninstall_solution' },
        { label: 'remove_revision', value: 'remove_revision' },
        { label: 'resolve_configuration', value: 'resolve_configuration' },
        { label: 'review_solution_version', value: 'review_solution_version' },
        { label: 'publish_solution_version', value: 'publish_solution_version' },
        { label: 'update_external_validation_status', value: 'update_external_validation_status' }
    ]}
>
<TabItem value="install_solution">

Post request to deploy.

```sql
EXEC azure.workload_orchestration.targets.install_solution 
@resource_group_name='{{ resource_group_name }}' --required, 
@target_name='{{ target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"solutionVersionId": "{{ solutionVersionId }}"
}'
;
```
</TabItem>
<TabItem value="uninstall_solution">

Post request to uninstall.

```sql
EXEC azure.workload_orchestration.targets.uninstall_solution 
@resource_group_name='{{ resource_group_name }}' --required, 
@target_name='{{ target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"solutionTemplateId": "{{ solutionTemplateId }}", 
"solutionInstanceName": "{{ solutionInstanceName }}"
}'
;
```
</TabItem>
<TabItem value="remove_revision">

Post request to remove solution version revision.

```sql
EXEC azure.workload_orchestration.targets.remove_revision 
@resource_group_name='{{ resource_group_name }}' --required, 
@target_name='{{ target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"solutionTemplateId": "{{ solutionTemplateId }}", 
"solutionVersion": "{{ solutionVersion }}"
}'
;
```
</TabItem>
<TabItem value="resolve_configuration">

Post request to resolve configuration.

```sql
EXEC azure.workload_orchestration.targets.resolve_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@target_name='{{ target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"solutionTemplateVersionId": "{{ solutionTemplateVersionId }}", 
"solutionInstanceName": "{{ solutionInstanceName }}", 
"solutionDependencies": "{{ solutionDependencies }}"
}'
;
```
</TabItem>
<TabItem value="review_solution_version">

Post request to review configuration.

```sql
EXEC azure.workload_orchestration.targets.review_solution_version 
@resource_group_name='{{ resource_group_name }}' --required, 
@target_name='{{ target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"solutionTemplateVersionId": "{{ solutionTemplateVersionId }}", 
"solutionInstanceName": "{{ solutionInstanceName }}", 
"solutionDependencies": "{{ solutionDependencies }}"
}'
;
```
</TabItem>
<TabItem value="publish_solution_version">

Post request to publish.

```sql
EXEC azure.workload_orchestration.targets.publish_solution_version 
@resource_group_name='{{ resource_group_name }}' --required, 
@target_name='{{ target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"solutionVersionId": "{{ solutionVersionId }}"
}'
;
```
</TabItem>
<TabItem value="update_external_validation_status">

Post request to update external validation status.

```sql
EXEC azure.workload_orchestration.targets.update_external_validation_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@target_name='{{ target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"solutionVersionId": "{{ solutionVersionId }}", 
"errorDetails": "{{ errorDetails }}", 
"externalValidationId": "{{ externalValidationId }}", 
"validationStatus": "{{ validationStatus }}"
}'
;
```
</TabItem>
</Tabs>
