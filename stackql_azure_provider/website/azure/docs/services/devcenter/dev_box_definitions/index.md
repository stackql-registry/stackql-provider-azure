--- 
title: dev_box_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_box_definitions
  - devcenter
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

Creates, updates, deletes, gets or lists a <code>dev_box_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dev_box_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devcenter.dev_box_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_by_project', value: 'get_by_project' },
        { label: 'list_by_dev_center', value: 'list_by_dev_center' },
        { label: 'list_by_project', value: 'list_by_project' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activeImageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information for the currently active image (only populated during updates).</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationErrorDetails" /></td>
    <td><code>object</code></td>
    <td>Details for image validator error. Populated when the image validation is not successful.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status of the configured image. Known values are: "Unknown", "Pending", "Succeeded", "Failed", and "TimedOut".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osStorageType" /></td>
    <td><code>string</code></td>
    <td>The storage type used for the Operating System disk of Dev Boxes created using this definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU for Dev Boxes created using this definition.</td>
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
    <td><CopyableCode code="validationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status for the Dev Box Definition. Known values are: "Unknown", "Pending", "Succeeded", and "Failed".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_project">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activeImageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information for the currently active image (only populated during updates).</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationErrorDetails" /></td>
    <td><code>object</code></td>
    <td>Details for image validator error. Populated when the image validation is not successful.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status of the configured image. Known values are: "Unknown", "Pending", "Succeeded", "Failed", and "TimedOut".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osStorageType" /></td>
    <td><code>string</code></td>
    <td>The storage type used for the Operating System disk of Dev Boxes created using this definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU for Dev Boxes created using this definition.</td>
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
    <td><CopyableCode code="validationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status for the Dev Box Definition. Known values are: "Unknown", "Pending", "Succeeded", and "Failed".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_dev_center">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activeImageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information for the currently active image (only populated during updates).</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationErrorDetails" /></td>
    <td><code>object</code></td>
    <td>Details for image validator error. Populated when the image validation is not successful.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status of the configured image. Known values are: "Unknown", "Pending", "Succeeded", "Failed", and "TimedOut".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osStorageType" /></td>
    <td><code>string</code></td>
    <td>The storage type used for the Operating System disk of Dev Boxes created using this definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU for Dev Boxes created using this definition.</td>
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
    <td><CopyableCode code="validationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status for the Dev Box Definition. Known values are: "Unknown", "Pending", "Succeeded", and "Failed".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_project">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activeImageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information for the currently active image (only populated during updates).</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Image reference information.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationErrorDetails" /></td>
    <td><code>object</code></td>
    <td>Details for image validator error. Populated when the image validation is not successful.</td>
</tr>
<tr>
    <td><CopyableCode code="imageValidationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status of the configured image. Known values are: "Unknown", "Pending", "Succeeded", "Failed", and "TimedOut".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osStorageType" /></td>
    <td><code>string</code></td>
    <td>The storage type used for the Operating System disk of Dev Boxes created using this definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU for Dev Boxes created using this definition.</td>
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
    <td><CopyableCode code="validationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status for the Dev Box Definition. Known values are: "Unknown", "Pending", "Succeeded", and "Failed".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-dev_box_definition_name"><code>dev_box_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Dev Box definition.</td>
</tr>
<tr>
    <td><a href="#get_by_project"><CopyableCode code="get_by_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-dev_box_definition_name"><code>dev_box_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Dev Box definition configured for a project.</td>
</tr>
<tr>
    <td><a href="#list_by_dev_center"><CopyableCode code="list_by_dev_center" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>List Dev Box definitions for a devcenter.</td>
</tr>
<tr>
    <td><a href="#list_by_project"><CopyableCode code="list_by_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>List Dev Box definitions configured for a project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-dev_box_definition_name"><code>dev_box_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Dev Box definition.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-dev_box_definition_name"><code>dev_box_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Partially updates a Dev Box definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-dev_box_definition_name"><code>dev_box_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Dev Box definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-dev_box_definition_name"><code>dev_box_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Dev Box definition.</td>
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
<tr id="parameter-dev_box_definition_name">
    <td><CopyableCode code="dev_box_definition_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Dev Box definition. Required.</td>
</tr>
<tr id="parameter-dev_center_name">
    <td><CopyableCode code="dev_center_name" /></td>
    <td><code>string</code></td>
    <td>The name of the devcenter. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of the project. Required.</td>
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
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_by_project', value: 'get_by_project' },
        { label: 'list_by_dev_center', value: 'list_by_dev_center' },
        { label: 'list_by_project', value: 'list_by_project' }
    ]}
>
<TabItem value="get">

Gets a Dev Box definition.

```sql
SELECT
id,
name,
activeImageReference,
hibernateSupport,
imageReference,
imageValidationErrorDetails,
imageValidationStatus,
location,
osStorageType,
provisioningState,
sku,
systemData,
tags,
type,
validationStatus
FROM azure.devcenter.dev_box_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND dev_box_definition_name = '{{ dev_box_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_project">

Gets a Dev Box definition configured for a project.

```sql
SELECT
id,
name,
activeImageReference,
hibernateSupport,
imageReference,
imageValidationErrorDetails,
imageValidationStatus,
location,
osStorageType,
provisioningState,
sku,
systemData,
tags,
type,
validationStatus
FROM azure.devcenter.dev_box_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND dev_box_definition_name = '{{ dev_box_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_dev_center">

List Dev Box definitions for a devcenter.

```sql
SELECT
id,
name,
activeImageReference,
hibernateSupport,
imageReference,
imageValidationErrorDetails,
imageValidationStatus,
location,
osStorageType,
provisioningState,
sku,
systemData,
tags,
type,
validationStatus
FROM azure.devcenter.dev_box_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_project">

List Dev Box definitions configured for a project.

```sql
SELECT
id,
name,
activeImageReference,
hibernateSupport,
imageReference,
imageValidationErrorDetails,
imageValidationStatus,
location,
osStorageType,
provisioningState,
sku,
systemData,
tags,
type,
validationStatus
FROM azure.devcenter.dev_box_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
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

Creates or updates a Dev Box definition.

```sql
INSERT INTO azure.devcenter.dev_box_definitions (
tags,
location,
properties,
resource_group_name,
dev_center_name,
dev_box_definition_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ dev_center_name }}',
'{{ dev_box_definition_name }}',
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
- name: dev_box_definitions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dev_box_definitions resource.
    - name: dev_center_name
      value: "{{ dev_center_name }}"
      description: Required parameter for the dev_box_definitions resource.
    - name: dev_box_definition_name
      value: "{{ dev_box_definition_name }}"
      description: Required parameter for the dev_box_definitions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dev_box_definitions resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        imageReference:
          id: "{{ id }}"
          exactVersion: "{{ exactVersion }}"
        sku:
          name: "{{ name }}"
          tier: "{{ tier }}"
          size: "{{ size }}"
          family: "{{ family }}"
          capacity: {{ capacity }}
        osStorageType: "{{ osStorageType }}"
        hibernateSupport: "{{ hibernateSupport }}"
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

Partially updates a Dev Box definition.

```sql
UPDATE azure.devcenter.dev_box_definitions
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND dev_box_definition_name = '{{ dev_box_definition_name }}' --required
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

Creates or updates a Dev Box definition.

```sql
REPLACE azure.devcenter.dev_box_definitions
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND dev_box_definition_name = '{{ dev_box_definition_name }}' --required
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

Deletes a Dev Box definition.

```sql
DELETE FROM azure.devcenter.dev_box_definitions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND dev_box_definition_name = '{{ dev_box_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
