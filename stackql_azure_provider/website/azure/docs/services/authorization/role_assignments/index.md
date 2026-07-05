--- 
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
  - authorization
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

Creates, updates, deletes, gets or lists a <code>role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_for_resource"
    values={[
        { label: 'list_for_resource', value: 'list_for_resource' },
        { label: 'get', value: 'get' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'list_for_scope', value: 'list_for_scope' },
        { label: 'list_for_subscription', value: 'list_for_subscription' },
        { label: 'get_by_id', value: 'get_by_id' }
    ]}
>
<TabItem value="list_for_resource">

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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently the only accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the delegated managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment scope.</td>
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
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who updated the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was updated.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently the only accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the delegated managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment scope.</td>
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
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who updated the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_for_resource_group">

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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently the only accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the delegated managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment scope.</td>
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
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who updated the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_for_scope">

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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently the only accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the delegated managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment scope.</td>
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
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who updated the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_for_subscription">

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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently the only accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the delegated managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment scope.</td>
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
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who updated the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_id">

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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently the only accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagedIdentityResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the delegated managed identity resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment scope.</td>
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
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>Id of the user who updated the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time it was updated.</td>
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
    <td><a href="#list_for_resource"><CopyableCode code="list_for_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td>List all role assignments that apply to a resource.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_assignment_name"><code>role_assignment_name</code></a></td>
    <td><a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td>Get a role assignment by scope and name.</td>
</tr>
<tr>
    <td><a href="#list_for_resource_group"><CopyableCode code="list_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td>List all role assignments that apply to a resource group.</td>
</tr>
<tr>
    <td><a href="#list_for_scope"><CopyableCode code="list_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-tenantId"><code>tenantId</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List all role assignments that apply to a scope.</td>
</tr>
<tr>
    <td><a href="#list_for_subscription"><CopyableCode code="list_for_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td>List all role assignments that apply to a subscription.</td>
</tr>
<tr>
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a></td>
    <td><a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td>Get a role assignment by ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_assignment_name"><code>role_assignment_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a role assignment by scope and name.</td>
</tr>
<tr>
    <td><a href="#create_by_id"><CopyableCode code="create_by_id" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a role assignment by ID.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_assignment_name"><code>role_assignment_name</code></a></td>
    <td><a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td>Delete a role assignment by scope and name.</td>
</tr>
<tr>
    <td><a href="#delete_by_id"><CopyableCode code="delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a></td>
    <td><a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td>Delete a role assignment by ID.</td>
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
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource to get role assignments for. Required.</td>
</tr>
<tr id="parameter-resource_provider_namespace">
    <td><CopyableCode code="resource_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the resource. Required.</td>
</tr>
<tr id="parameter-role_assignment_id">
    <td><CopyableCode code="role_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the role assignment including scope, resource name, and resource type. Format: /&#123;scope&#125;/providers/Microsoft.Authorization/roleAssignments/&#123;roleAssignmentName&#125;. Example: /subscriptions//resourcegroups//providers/Microsoft.Authorization/roleAssignments/. Required.</td>
</tr>
<tr id="parameter-role_assignment_name">
    <td><CopyableCode code="role_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the role assignment. It can be any valid GUID. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq &#123;id&#125; to return all role assignments at, above or below the scope for the specified principal. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The skipToken to apply on the operation. Use $skipToken=&#123;skiptoken&#125; to return paged role assignments following the skipToken passed. Only supported on provider level calls. Default value is None.</td>
</tr>
<tr id="parameter-tenantId">
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for cross-tenant request. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_for_resource"
    values={[
        { label: 'list_for_resource', value: 'list_for_resource' },
        { label: 'get', value: 'get' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'list_for_scope', value: 'list_for_scope' },
        { label: 'list_for_subscription', value: 'list_for_subscription' },
        { label: 'get_by_id', value: 'get_by_id' }
    ]}
>
<TabItem value="list_for_resource">

List all role assignments that apply to a resource.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
delegatedManagedIdentityResourceId,
description,
principalId,
principalType,
roleDefinitionId,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.role_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND tenantId = '{{ tenantId }}'
;
```
</TabItem>
<TabItem value="get">

Get a role assignment by scope and name.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
delegatedManagedIdentityResourceId,
description,
principalId,
principalType,
roleDefinitionId,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.role_assignments
WHERE scope = '{{ scope }}' -- required
AND role_assignment_name = '{{ role_assignment_name }}' -- required
AND tenantId = '{{ tenantId }}'
;
```
</TabItem>
<TabItem value="list_for_resource_group">

List all role assignments that apply to a resource group.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
delegatedManagedIdentityResourceId,
description,
principalId,
principalType,
roleDefinitionId,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.role_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND tenantId = '{{ tenantId }}'
;
```
</TabItem>
<TabItem value="list_for_scope">

List all role assignments that apply to a scope.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
delegatedManagedIdentityResourceId,
description,
principalId,
principalType,
roleDefinitionId,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.role_assignments
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
AND tenantId = '{{ tenantId }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_for_subscription">

List all role assignments that apply to a subscription.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
delegatedManagedIdentityResourceId,
description,
principalId,
principalType,
roleDefinitionId,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.role_assignments
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND tenantId = '{{ tenantId }}'
;
```
</TabItem>
<TabItem value="get_by_id">

Get a role assignment by ID.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
delegatedManagedIdentityResourceId,
description,
principalId,
principalType,
roleDefinitionId,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.role_assignments
WHERE role_assignment_id = '{{ role_assignment_id }}' -- required
AND tenantId = '{{ tenantId }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'create_by_id', value: 'create_by_id' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create or update a role assignment by scope and name.

```sql
INSERT INTO azure.authorization.role_assignments (
properties,
scope,
role_assignment_name
)
SELECT 
'{{ properties }}' /* required */,
'{{ scope }}',
'{{ role_assignment_name }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_by_id">

Create or update a role assignment by ID.

```sql
INSERT INTO azure.authorization.role_assignments (
properties,
role_assignment_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ role_assignment_id }}'
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
- name: role_assignments
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the role_assignments resource.
    - name: role_assignment_name
      value: "{{ role_assignment_name }}"
      description: Required parameter for the role_assignments resource.
    - name: role_assignment_id
      value: "{{ role_assignment_id }}"
      description: Required parameter for the role_assignments resource.
    - name: properties
      description: |
        Role assignment properties. Required.
      value:
        scope: "{{ scope }}"
        roleDefinitionId: "{{ roleDefinitionId }}"
        principalId: "{{ principalId }}"
        principalType: "{{ principalType }}"
        description: "{{ description }}"
        condition: "{{ condition }}"
        conditionVersion: "{{ conditionVersion }}"
        createdOn: "{{ createdOn }}"
        updatedOn: "{{ updatedOn }}"
        createdBy: "{{ createdBy }}"
        updatedBy: "{{ updatedBy }}"
        delegatedManagedIdentityResourceId: "{{ delegatedManagedIdentityResourceId }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_by_id', value: 'delete_by_id' }
    ]}
>
<TabItem value="delete">

Delete a role assignment by scope and name.

```sql
DELETE FROM azure.authorization.role_assignments
WHERE scope = '{{ scope }}' --required
AND role_assignment_name = '{{ role_assignment_name }}' --required
AND tenantId = '{{ tenantId }}'
;
```
</TabItem>
<TabItem value="delete_by_id">

Delete a role assignment by ID.

```sql
DELETE FROM azure.authorization.role_assignments
WHERE role_assignment_id = '{{ role_assignment_id }}' --required
AND tenantId = '{{ tenantId }}'
;
```
</TabItem>
</Tabs>
