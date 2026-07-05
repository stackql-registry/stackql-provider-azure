--- 
title: virtual_machine_image_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates
  - imagebuilder
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_image_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_image_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.imagebuilder.virtual_machine_image_templates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_run_output"
    values={[
        { label: 'get_run_output', value: 'get_run_output' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_run_output">

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
    <td><CopyableCode code="artifactId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the artifact.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactUri" /></td>
    <td><code>string</code></td>
    <td>The location URI of the artifact.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Succeeded", "Failed", "Deleting", and "Canceled". (Creating, Updating, Succeeded, Failed, Deleting, Canceled)</td>
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
    <td><CopyableCode code="additionalDataDisks" /></td>
    <td><code>array</code></td>
    <td>Optional array of additional data disks to be added to the image.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRun" /></td>
    <td><code>object</code></td>
    <td>Indicates whether or not to automatically run the image template build on template creation or update.</td>
</tr>
<tr>
    <td><CopyableCode code="buildTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Maximum duration to wait while building the image template (includes all customizations, optimization, validations, and distributions). Omit or specify 0 to use the default (4 hours).</td>
</tr>
<tr>
    <td><CopyableCode code="customize" /></td>
    <td><code>array</code></td>
    <td>Specifies the properties used to describe the customization steps of the image, like Image source etc.</td>
</tr>
<tr>
    <td><CopyableCode code="distribute" /></td>
    <td><code>array</code></td>
    <td>The distribution targets where the image output needs to go to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="errorHandling" /></td>
    <td><code>object</code></td>
    <td>Error handling options upon a build failure.</td>
</tr>
<tr>
    <td><CopyableCode code="exactStagingResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The staging resource group id in the same subscription as the image template that will be used to build the image. This read-only field differs from 'stagingResourceGroup' only if the value specified in the 'stagingResourceGroup' field is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the image template, if configured. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRunStatus" /></td>
    <td><code>object</code></td>
    <td>State of 'run' that is currently executing or was last executed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceTags" /></td>
    <td><code>object</code></td>
    <td>Tags that will be applied to the resource group and/or resources created by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="optimize" /></td>
    <td><code>object</code></td>
    <td>Specifies optimization to be performed on image.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningError" /></td>
    <td><code>object</code></td>
    <td>Provisioning error, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Succeeded", "Failed", "Deleting", and "Canceled". (Creating, Updating, Succeeded, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Specifies the properties used to describe the source image. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stagingResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The staging resource group id in the same subscription as the image template that will be used to build the image. If this field is empty, a resource group with a random name will be created. If the resource group specified in this field doesn't exist, it will be created with the same name. If the resource group specified exists, it must be empty and in the same region as the image template. The resource group created will be deleted during template deletion if this field is empty or the resource group specified doesn't exist, but if the resource group specified exists the resources created in the resource group will be deleted during template deletion and the resource group itself will remain.</td>
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
    <td><CopyableCode code="validate" /></td>
    <td><code>object</code></td>
    <td>Configuration options and list of validations to be performed on the resulting image.</td>
</tr>
<tr>
    <td><CopyableCode code="vmProfile" /></td>
    <td><code>object</code></td>
    <td>Describes how virtual machine is set up to build images.</td>
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
    <td><CopyableCode code="additionalDataDisks" /></td>
    <td><code>array</code></td>
    <td>Optional array of additional data disks to be added to the image.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRun" /></td>
    <td><code>object</code></td>
    <td>Indicates whether or not to automatically run the image template build on template creation or update.</td>
</tr>
<tr>
    <td><CopyableCode code="buildTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Maximum duration to wait while building the image template (includes all customizations, optimization, validations, and distributions). Omit or specify 0 to use the default (4 hours).</td>
</tr>
<tr>
    <td><CopyableCode code="customize" /></td>
    <td><code>array</code></td>
    <td>Specifies the properties used to describe the customization steps of the image, like Image source etc.</td>
</tr>
<tr>
    <td><CopyableCode code="distribute" /></td>
    <td><code>array</code></td>
    <td>The distribution targets where the image output needs to go to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="errorHandling" /></td>
    <td><code>object</code></td>
    <td>Error handling options upon a build failure.</td>
</tr>
<tr>
    <td><CopyableCode code="exactStagingResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The staging resource group id in the same subscription as the image template that will be used to build the image. This read-only field differs from 'stagingResourceGroup' only if the value specified in the 'stagingResourceGroup' field is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the image template, if configured. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRunStatus" /></td>
    <td><code>object</code></td>
    <td>State of 'run' that is currently executing or was last executed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceTags" /></td>
    <td><code>object</code></td>
    <td>Tags that will be applied to the resource group and/or resources created by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="optimize" /></td>
    <td><code>object</code></td>
    <td>Specifies optimization to be performed on image.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningError" /></td>
    <td><code>object</code></td>
    <td>Provisioning error, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Succeeded", "Failed", "Deleting", and "Canceled". (Creating, Updating, Succeeded, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Specifies the properties used to describe the source image. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stagingResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The staging resource group id in the same subscription as the image template that will be used to build the image. If this field is empty, a resource group with a random name will be created. If the resource group specified in this field doesn't exist, it will be created with the same name. If the resource group specified exists, it must be empty and in the same region as the image template. The resource group created will be deleted during template deletion if this field is empty or the resource group specified doesn't exist, but if the resource group specified exists the resources created in the resource group will be deleted during template deletion and the resource group itself will remain.</td>
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
    <td><CopyableCode code="validate" /></td>
    <td><code>object</code></td>
    <td>Configuration options and list of validations to be performed on the resulting image.</td>
</tr>
<tr>
    <td><CopyableCode code="vmProfile" /></td>
    <td><code>object</code></td>
    <td>Describes how virtual machine is set up to build images.</td>
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
    <td><CopyableCode code="additionalDataDisks" /></td>
    <td><code>array</code></td>
    <td>Optional array of additional data disks to be added to the image.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRun" /></td>
    <td><code>object</code></td>
    <td>Indicates whether or not to automatically run the image template build on template creation or update.</td>
</tr>
<tr>
    <td><CopyableCode code="buildTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Maximum duration to wait while building the image template (includes all customizations, optimization, validations, and distributions). Omit or specify 0 to use the default (4 hours).</td>
</tr>
<tr>
    <td><CopyableCode code="customize" /></td>
    <td><code>array</code></td>
    <td>Specifies the properties used to describe the customization steps of the image, like Image source etc.</td>
</tr>
<tr>
    <td><CopyableCode code="distribute" /></td>
    <td><code>array</code></td>
    <td>The distribution targets where the image output needs to go to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="errorHandling" /></td>
    <td><code>object</code></td>
    <td>Error handling options upon a build failure.</td>
</tr>
<tr>
    <td><CopyableCode code="exactStagingResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The staging resource group id in the same subscription as the image template that will be used to build the image. This read-only field differs from 'stagingResourceGroup' only if the value specified in the 'stagingResourceGroup' field is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the image template, if configured. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRunStatus" /></td>
    <td><code>object</code></td>
    <td>State of 'run' that is currently executing or was last executed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceTags" /></td>
    <td><code>object</code></td>
    <td>Tags that will be applied to the resource group and/or resources created by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="optimize" /></td>
    <td><code>object</code></td>
    <td>Specifies optimization to be performed on image.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningError" /></td>
    <td><code>object</code></td>
    <td>Provisioning error, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Succeeded", "Failed", "Deleting", and "Canceled". (Creating, Updating, Succeeded, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Specifies the properties used to describe the source image. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stagingResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The staging resource group id in the same subscription as the image template that will be used to build the image. If this field is empty, a resource group with a random name will be created. If the resource group specified in this field doesn't exist, it will be created with the same name. If the resource group specified exists, it must be empty and in the same region as the image template. The resource group created will be deleted during template deletion if this field is empty or the resource group specified doesn't exist, but if the resource group specified exists the resources created in the resource group will be deleted during template deletion and the resource group itself will remain.</td>
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
    <td><CopyableCode code="validate" /></td>
    <td><code>object</code></td>
    <td>Configuration options and list of validations to be performed on the resulting image.</td>
</tr>
<tr>
    <td><CopyableCode code="vmProfile" /></td>
    <td><code>object</code></td>
    <td>Describes how virtual machine is set up to build images.</td>
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
    <td><a href="#get_run_output"><CopyableCode code="get_run_output" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-run_output_name"><code>run_output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified run output for the specified image template resource.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get information about a virtual machine image template.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the VM image templates associated with the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the VM image templates associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-identity"><code>identity</code></a></td>
    <td></td>
    <td>Create or update a virtual machine image template.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the tags for this Virtual Machine Image Template.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-identity"><code>identity</code></a></td>
    <td></td>
    <td>Create or update a virtual machine image template.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a virtual machine image template.</td>
</tr>
<tr>
    <td><a href="#list_run_outputs"><CopyableCode code="list_run_outputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all run outputs for the specified Image Template resource.</td>
</tr>
<tr>
    <td><a href="#run"><CopyableCode code="run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create artifacts from a existing image template.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-image_template_name"><code>image_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel the long running image build based on the image template.</td>
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
<tr id="parameter-image_template_name">
    <td><CopyableCode code="image_template_name" /></td>
    <td><code>string</code></td>
    <td>The name of the image Template. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-run_output_name">
    <td><CopyableCode code="run_output_name" /></td>
    <td><code>string</code></td>
    <td>The name of the run output. Required.</td>
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
    defaultValue="get_run_output"
    values={[
        { label: 'get_run_output', value: 'get_run_output' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_run_output">

Get the specified run output for the specified image template resource.

```sql
SELECT
id,
name,
artifactId,
artifactUri,
provisioningState,
systemData,
type
FROM azure.imagebuilder.virtual_machine_image_templates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND image_template_name = '{{ image_template_name }}' -- required
AND run_output_name = '{{ run_output_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get information about a virtual machine image template.

```sql
SELECT
id,
name,
additionalDataDisks,
autoRun,
buildTimeoutInMinutes,
customize,
distribute,
errorHandling,
exactStagingResourceGroup,
identity,
lastRunStatus,
location,
managedResourceTags,
optimize,
provisioningError,
provisioningState,
source,
stagingResourceGroup,
systemData,
tags,
type,
validate,
vmProfile
FROM azure.imagebuilder.virtual_machine_image_templates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND image_template_name = '{{ image_template_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets information about the VM image templates associated with the specified resource group.

```sql
SELECT
id,
name,
additionalDataDisks,
autoRun,
buildTimeoutInMinutes,
customize,
distribute,
errorHandling,
exactStagingResourceGroup,
identity,
lastRunStatus,
location,
managedResourceTags,
optimize,
provisioningError,
provisioningState,
source,
stagingResourceGroup,
systemData,
tags,
type,
validate,
vmProfile
FROM azure.imagebuilder.virtual_machine_image_templates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets information about the VM image templates associated with the subscription.

```sql
SELECT
id,
name,
additionalDataDisks,
autoRun,
buildTimeoutInMinutes,
customize,
distribute,
errorHandling,
exactStagingResourceGroup,
identity,
lastRunStatus,
location,
managedResourceTags,
optimize,
provisioningError,
provisioningState,
source,
stagingResourceGroup,
systemData,
tags,
type,
validate,
vmProfile
FROM azure.imagebuilder.virtual_machine_image_templates
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

Create or update a virtual machine image template.

```sql
INSERT INTO azure.imagebuilder.virtual_machine_image_templates (
tags,
location,
properties,
identity,
resource_group_name,
image_template_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}' /* required */,
'{{ resource_group_name }}',
'{{ image_template_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: virtual_machine_image_templates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machine_image_templates resource.
    - name: image_template_name
      value: "{{ image_template_name }}"
      description: Required parameter for the virtual_machine_image_templates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machine_image_templates resource.
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
        The properties of the image template.
      value:
        source:
          type: "{{ type }}"
        customize:
          - type: "{{ type }}"
            name: "{{ name }}"
        optimize:
          vmBoot:
            state: "{{ state }}"
          workload:
            state: "{{ state }}"
            scriptUri: "{{ scriptUri }}"
            sha256Checksum: "{{ sha256Checksum }}"
        validate:
          continueDistributeOnFailure: {{ continueDistributeOnFailure }}
          sourceValidationOnly: {{ sourceValidationOnly }}
          inVMValidations:
            - type: "{{ type }}"
              name: "{{ name }}"
        distribute:
          - type: "{{ type }}"
            runOutputName: "{{ runOutputName }}"
            artifactTags: "{{ artifactTags }}"
        errorHandling:
          onCustomizerError: "{{ onCustomizerError }}"
          onValidationError: "{{ onValidationError }}"
        provisioningState: "{{ provisioningState }}"
        provisioningError:
          provisioningErrorCode: "{{ provisioningErrorCode }}"
          message: "{{ message }}"
        lastRunStatus:
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
          runState: "{{ runState }}"
          runSubState: "{{ runSubState }}"
          message: "{{ message }}"
        buildTimeoutInMinutes: {{ buildTimeoutInMinutes }}
        vmProfile:
          vmSize: "{{ vmSize }}"
          osDiskSizeGB: {{ osDiskSizeGB }}
          userAssignedIdentities:
            - "{{ userAssignedIdentities }}"
          vnetConfig:
            subnetId: "{{ subnetId }}"
            containerInstanceSubnetId: "{{ containerInstanceSubnetId }}"
            proxyVmSize: "{{ proxyVmSize }}"
        additionalDataDisks:
          - sizeGB: {{ sizeGB }}
        stagingResourceGroup: "{{ stagingResourceGroup }}"
        exactStagingResourceGroup: "{{ exactStagingResourceGroup }}"
        autoRun:
          state: "{{ state }}"
        managedResourceTags: "{{ managedResourceTags }}"
    - name: identity
      description: |
        The identity of the image template, if configured. Required.
      value:
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update the tags for this Virtual Machine Image Template.

```sql
UPDATE azure.imagebuilder.virtual_machine_image_templates
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND image_template_name = '{{ image_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Create or update a virtual machine image template.

```sql
REPLACE azure.imagebuilder.virtual_machine_image_templates
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND image_template_name = '{{ image_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND identity = '{{ identity }}' --required
RETURNING
id,
name,
identity,
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

Delete a virtual machine image template.

```sql
DELETE FROM azure.imagebuilder.virtual_machine_image_templates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND image_template_name = '{{ image_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_run_outputs"
    values={[
        { label: 'list_run_outputs', value: 'list_run_outputs' },
        { label: 'run', value: 'run' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="list_run_outputs">

List all run outputs for the specified Image Template resource.

```sql
EXEC azure.imagebuilder.virtual_machine_image_templates.list_run_outputs 
@resource_group_name='{{ resource_group_name }}' --required, 
@image_template_name='{{ image_template_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run">

Create artifacts from a existing image template.

```sql
EXEC azure.imagebuilder.virtual_machine_image_templates.run 
@resource_group_name='{{ resource_group_name }}' --required, 
@image_template_name='{{ image_template_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancel the long running image build based on the image template.

```sql
EXEC azure.imagebuilder.virtual_machine_image_templates.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@image_template_name='{{ image_template_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
