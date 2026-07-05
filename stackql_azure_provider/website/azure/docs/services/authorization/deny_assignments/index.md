--- 
title: deny_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - deny_assignments
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

Creates, updates, deletes, gets or lists a <code>deny_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deny_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.deny_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_for_resource"
    values={[
        { label: 'list_for_resource', value: 'list_for_resource' },
        { label: 'get', value: 'get' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'list_for_scope', value: 'list_for_scope' },
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
    <td>The conditions on the deny assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition.</td>
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
    <td><CopyableCode code="denyAssignmentEffect" /></td>
    <td><code>string</code></td>
    <td>The effect of the deny assignment. 'enforced' blocks access, 'audit' logs without blocking. Known values are: "enforced" and "audit". (enforced, audit)</td>
</tr>
<tr>
    <td><CopyableCode code="denyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>The display name of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotApplyToChildScopes" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the deny assignment applies to child scopes. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="excludePrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment does not apply.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemProtected" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this deny assignment was created by Azure and cannot be edited or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>An array of permissions that are denied by the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment applies.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The deny assignment scope.</td>
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
    <td>The conditions on the deny assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition.</td>
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
    <td><CopyableCode code="denyAssignmentEffect" /></td>
    <td><code>string</code></td>
    <td>The effect of the deny assignment. 'enforced' blocks access, 'audit' logs without blocking. Known values are: "enforced" and "audit". (enforced, audit)</td>
</tr>
<tr>
    <td><CopyableCode code="denyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>The display name of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotApplyToChildScopes" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the deny assignment applies to child scopes. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="excludePrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment does not apply.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemProtected" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this deny assignment was created by Azure and cannot be edited or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>An array of permissions that are denied by the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment applies.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The deny assignment scope.</td>
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
    <td>The conditions on the deny assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition.</td>
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
    <td><CopyableCode code="denyAssignmentEffect" /></td>
    <td><code>string</code></td>
    <td>The effect of the deny assignment. 'enforced' blocks access, 'audit' logs without blocking. Known values are: "enforced" and "audit". (enforced, audit)</td>
</tr>
<tr>
    <td><CopyableCode code="denyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>The display name of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotApplyToChildScopes" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the deny assignment applies to child scopes. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="excludePrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment does not apply.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemProtected" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this deny assignment was created by Azure and cannot be edited or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>An array of permissions that are denied by the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment applies.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The deny assignment scope.</td>
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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the deny assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition.</td>
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
    <td><CopyableCode code="denyAssignmentEffect" /></td>
    <td><code>string</code></td>
    <td>The effect of the deny assignment. 'enforced' blocks access, 'audit' logs without blocking. Known values are: "enforced" and "audit". (enforced, audit)</td>
</tr>
<tr>
    <td><CopyableCode code="denyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>The display name of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotApplyToChildScopes" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the deny assignment applies to child scopes. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="excludePrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment does not apply.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemProtected" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this deny assignment was created by Azure and cannot be edited or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>An array of permissions that are denied by the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment applies.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The deny assignment scope.</td>
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
    <td>The conditions on the deny assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition.</td>
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
    <td><CopyableCode code="denyAssignmentEffect" /></td>
    <td><code>string</code></td>
    <td>The effect of the deny assignment. 'enforced' blocks access, 'audit' logs without blocking. Known values are: "enforced" and "audit". (enforced, audit)</td>
</tr>
<tr>
    <td><CopyableCode code="denyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>The display name of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotApplyToChildScopes" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the deny assignment applies to child scopes. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="excludePrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment does not apply.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemProtected" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this deny assignment was created by Azure and cannot be edited or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>An array of permissions that are denied by the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment applies.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The deny assignment scope.</td>
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
    <td>The conditions on the deny assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition.</td>
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
    <td><CopyableCode code="denyAssignmentEffect" /></td>
    <td><code>string</code></td>
    <td>The effect of the deny assignment. 'enforced' blocks access, 'audit' logs without blocking. Known values are: "enforced" and "audit". (enforced, audit)</td>
</tr>
<tr>
    <td><CopyableCode code="denyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>The display name of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotApplyToChildScopes" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the deny assignment applies to child scopes. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="excludePrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment does not apply.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemProtected" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this deny assignment was created by Azure and cannot be edited or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>An array of permissions that are denied by the deny assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="principals" /></td>
    <td><code>array</code></td>
    <td>Array of principals to which the deny assignment applies.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The deny assignment scope.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets deny assignments for a resource.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deny_assignment_id"><code>deny_assignment_id</code></a></td>
    <td></td>
    <td>Get the specified deny assignment.</td>
</tr>
<tr>
    <td><a href="#list_for_resource_group"><CopyableCode code="list_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets deny assignments for a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all deny assignments for the subscription.</td>
</tr>
<tr>
    <td><a href="#list_for_scope"><CopyableCode code="list_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets deny assignments for a scope.</td>
</tr>
<tr>
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deny_assignment_id"><code>deny_assignment_id</code></a></td>
    <td></td>
    <td>Gets a deny assignment by ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deny_assignment_id"><code>deny_assignment_id</code></a></td>
    <td></td>
    <td>Create or update a deny assignment by scope and name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deny_assignment_id"><code>deny_assignment_id</code></a></td>
    <td></td>
    <td>Create or update a deny assignment by scope and name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deny_assignment_id"><code>deny_assignment_id</code></a></td>
    <td></td>
    <td>Delete a deny assignment by scope and name.</td>
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
<tr id="parameter-deny_assignment_id">
    <td><CopyableCode code="deny_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the deny assignment to get. Required.</td>
</tr>
<tr id="parameter-parent_resource_path">
    <td><CopyableCode code="parent_resource_path" /></td>
    <td><code>string</code></td>
    <td>The parent resource identity. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource to get deny assignments for. Required.</td>
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
    <td>The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '&#123;name&#125;' to search deny assignments by name at specified scope. Use $filter=principalId eq '&#123;id&#125;' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '&#123;id&#125;' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. Default value is None.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_for_scope', value: 'list_for_scope' },
        { label: 'get_by_id', value: 'get_by_id' }
    ]}
>
<TabItem value="list_for_resource">

Gets deny assignments for a resource.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
denyAssignmentEffect,
denyAssignmentName,
description,
doNotApplyToChildScopes,
excludePrincipals,
isSystemProtected,
permissions,
principals,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.deny_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_path = '{{ parent_resource_path }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get">

Get the specified deny assignment.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
denyAssignmentEffect,
denyAssignmentName,
description,
doNotApplyToChildScopes,
excludePrincipals,
isSystemProtected,
permissions,
principals,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.deny_assignments
WHERE scope = '{{ scope }}' -- required
AND deny_assignment_id = '{{ deny_assignment_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_resource_group">

Gets deny assignments for a resource group.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
denyAssignmentEffect,
denyAssignmentName,
description,
doNotApplyToChildScopes,
excludePrincipals,
isSystemProtected,
permissions,
principals,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.deny_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

Gets all deny assignments for the subscription.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
denyAssignmentEffect,
denyAssignmentName,
description,
doNotApplyToChildScopes,
excludePrincipals,
isSystemProtected,
permissions,
principals,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.deny_assignments
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_for_scope">

Gets deny assignments for a scope.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
denyAssignmentEffect,
denyAssignmentName,
description,
doNotApplyToChildScopes,
excludePrincipals,
isSystemProtected,
permissions,
principals,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.deny_assignments
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get_by_id">

Gets a deny assignment by ID.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdBy,
createdOn,
denyAssignmentEffect,
denyAssignmentName,
description,
doNotApplyToChildScopes,
excludePrincipals,
isSystemProtected,
permissions,
principals,
scope,
systemData,
type,
updatedBy,
updatedOn
FROM azure.authorization.deny_assignments
WHERE deny_assignment_id = '{{ deny_assignment_id }}' -- required
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

Create or update a deny assignment by scope and name.

```sql
INSERT INTO azure.authorization.deny_assignments (
properties,
scope,
deny_assignment_id
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ deny_assignment_id }}'
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
- name: deny_assignments
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the deny_assignments resource.
    - name: deny_assignment_id
      value: "{{ deny_assignment_id }}"
      description: Required parameter for the deny_assignments resource.
    - name: properties
      description: |
        Deny assignment properties.
      value:
        denyAssignmentName: "{{ denyAssignmentName }}"
        description: "{{ description }}"
        permissions:
          - actions: "{{ actions }}"
            notActions: "{{ notActions }}"
            dataActions: "{{ dataActions }}"
            notDataActions: "{{ notDataActions }}"
            condition: "{{ condition }}"
            conditionVersion: "{{ conditionVersion }}"
        scope: "{{ scope }}"
        doNotApplyToChildScopes: {{ doNotApplyToChildScopes }}
        principals:
          - id: "{{ id }}"
            type: "{{ type }}"
        excludePrincipals:
          - id: "{{ id }}"
            type: "{{ type }}"
        isSystemProtected: {{ isSystemProtected }}
        denyAssignmentEffect: "{{ denyAssignmentEffect }}"
        condition: "{{ condition }}"
        conditionVersion: "{{ conditionVersion }}"
        createdOn: "{{ createdOn }}"
        updatedOn: "{{ updatedOn }}"
        createdBy: "{{ createdBy }}"
        updatedBy: "{{ updatedBy }}"
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

Create or update a deny assignment by scope and name.

```sql
REPLACE azure.authorization.deny_assignments
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND deny_assignment_id = '{{ deny_assignment_id }}' --required
RETURNING
id,
name,
properties,
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

Delete a deny assignment by scope and name.

```sql
DELETE FROM azure.authorization.deny_assignments
WHERE scope = '{{ scope }}' --required
AND deny_assignment_id = '{{ deny_assignment_id }}' --required
;
```
</TabItem>
</Tabs>
