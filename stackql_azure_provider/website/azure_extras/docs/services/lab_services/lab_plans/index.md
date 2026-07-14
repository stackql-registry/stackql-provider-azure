--- 
title: lab_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - lab_plans
  - lab_services
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

Creates, updates, deletes, gets or lists a <code>lab_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lab_plans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.lab_services.lab_plans" /></td></tr>
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
    <td><CopyableCode code="allowedRegions" /></td>
    <td><code>array</code></td>
    <td>The allowed regions for the lab creator to use when creating labs using this lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultAutoShutdownProfile" /></td>
    <td><code>object</code></td>
    <td>The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultConnectionProfile" /></td>
    <td><code>object</code></td>
    <td>The default lab connection profile. This can be changed on a lab resource and only provides a default profile.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed Identity Information.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedLmsInstance" /></td>
    <td><code>string</code></td>
    <td>Base Url of the lms instance this lab plan can link lab rosters against.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the lab plan. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="sharedGalleryId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.</td>
</tr>
<tr>
    <td><CopyableCode code="supportInfo" /></td>
    <td><code>object</code></td>
    <td>Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the lab plan.</td>
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
    <td><CopyableCode code="allowedRegions" /></td>
    <td><code>array</code></td>
    <td>The allowed regions for the lab creator to use when creating labs using this lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultAutoShutdownProfile" /></td>
    <td><code>object</code></td>
    <td>The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultConnectionProfile" /></td>
    <td><code>object</code></td>
    <td>The default lab connection profile. This can be changed on a lab resource and only provides a default profile.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed Identity Information.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedLmsInstance" /></td>
    <td><code>string</code></td>
    <td>Base Url of the lms instance this lab plan can link lab rosters against.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the lab plan. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="sharedGalleryId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.</td>
</tr>
<tr>
    <td><CopyableCode code="supportInfo" /></td>
    <td><code>object</code></td>
    <td>Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the lab plan.</td>
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
    <td><CopyableCode code="allowedRegions" /></td>
    <td><code>array</code></td>
    <td>The allowed regions for the lab creator to use when creating labs using this lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultAutoShutdownProfile" /></td>
    <td><code>object</code></td>
    <td>The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultConnectionProfile" /></td>
    <td><code>object</code></td>
    <td>The default lab connection profile. This can be changed on a lab resource and only provides a default profile.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed Identity Information.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedLmsInstance" /></td>
    <td><code>string</code></td>
    <td>Base Url of the lms instance this lab plan can link lab rosters against.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the lab plan. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="sharedGalleryId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.</td>
</tr>
<tr>
    <td><CopyableCode code="supportInfo" /></td>
    <td><code>object</code></td>
    <td>Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the lab plan.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a Lab Plan resource. Retrieves the properties of a Lab Plan.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all lab plans for a subscription and resource group. Returns a list of all lab plans for a subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all lab plans for a subscription. Returns a list of all lab plans within a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Updates or creates a Lab Plan resource. Operation to create or update a Lab Plan resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a Lab Plan resource. Operation to update a Lab Plan resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Updates or creates a Lab Plan resource. Operation to create or update a Lab Plan resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Lab Plan resource. Operation to delete a Lab Plan resource. Deleting a lab plan does not delete labs associated with a lab plan, nor does it delete shared images added to a gallery via the lab plan permission container.</td>
</tr>
<tr>
    <td><a href="#save_image"><CopyableCode code="save_image" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Save an image from a lab VM to the attached shared image gallery. Saves an image from a lab VM to the attached shared image gallery.</td>
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
<tr id="parameter-lab_plan_name">
    <td><CopyableCode code="lab_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply to the operation. Default value is None.</td>
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

Retrieves a Lab Plan resource. Retrieves the properties of a Lab Plan.

```sql
SELECT
id,
name,
allowedRegions,
defaultAutoShutdownProfile,
defaultConnectionProfile,
defaultNetworkProfile,
identity,
linkedLmsInstance,
location,
provisioningState,
sharedGalleryId,
supportInfo,
systemData,
tags,
type
FROM azure_extras.lab_services.lab_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_plan_name = '{{ lab_plan_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all lab plans for a subscription and resource group. Returns a list of all lab plans for a subscription and resource group.

```sql
SELECT
id,
name,
allowedRegions,
defaultAutoShutdownProfile,
defaultConnectionProfile,
defaultNetworkProfile,
identity,
linkedLmsInstance,
location,
provisioningState,
sharedGalleryId,
supportInfo,
systemData,
tags,
type
FROM azure_extras.lab_services.lab_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get all lab plans for a subscription. Returns a list of all lab plans within a subscription.

```sql
SELECT
id,
name,
allowedRegions,
defaultAutoShutdownProfile,
defaultConnectionProfile,
defaultNetworkProfile,
identity,
linkedLmsInstance,
location,
provisioningState,
sharedGalleryId,
supportInfo,
systemData,
tags,
type
FROM azure_extras.lab_services.lab_plans
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Updates or creates a Lab Plan resource. Operation to create or update a Lab Plan resource.

```sql
INSERT INTO azure_extras.lab_services.lab_plans (
tags,
location,
identity,
properties,
resource_group_name,
lab_plan_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ lab_plan_name }}',
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
- name: lab_plans
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the lab_plans resource.
    - name: lab_plan_name
      value: "{{ lab_plan_name }}"
      description: Required parameter for the lab_plans resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the lab_plans resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: identity
      description: |
        Managed Identity Information.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: properties
      value:
        defaultConnectionProfile:
          webSshAccess: "{{ webSshAccess }}"
          webRdpAccess: "{{ webRdpAccess }}"
          clientSshAccess: "{{ clientSshAccess }}"
          clientRdpAccess: "{{ clientRdpAccess }}"
        defaultAutoShutdownProfile:
          shutdownOnDisconnect: "{{ shutdownOnDisconnect }}"
          shutdownWhenNotConnected: "{{ shutdownWhenNotConnected }}"
          shutdownOnIdle: "{{ shutdownOnIdle }}"
          disconnectDelay: "{{ disconnectDelay }}"
          noConnectDelay: "{{ noConnectDelay }}"
          idleDelay: "{{ idleDelay }}"
        defaultNetworkProfile:
          subnetId: "{{ subnetId }}"
        allowedRegions:
          - "{{ allowedRegions }}"
        sharedGalleryId: "{{ sharedGalleryId }}"
        supportInfo:
          url: "{{ url }}"
          email: "{{ email }}"
          phone: "{{ phone }}"
          instructions: "{{ instructions }}"
        linkedLmsInstance: "{{ linkedLmsInstance }}"
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

Updates a Lab Plan resource. Operation to update a Lab Plan resource.

```sql
UPDATE azure_extras.lab_services.lab_plans
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_plan_name = '{{ lab_plan_name }}' --required
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

Updates or creates a Lab Plan resource. Operation to create or update a Lab Plan resource.

```sql
REPLACE azure_extras.lab_services.lab_plans
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_plan_name = '{{ lab_plan_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Deletes a Lab Plan resource. Operation to delete a Lab Plan resource. Deleting a lab plan does not delete labs associated with a lab plan, nor does it delete shared images added to a gallery via the lab plan permission container.

```sql
DELETE FROM azure_extras.lab_services.lab_plans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND lab_plan_name = '{{ lab_plan_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="save_image"
    values={[
        { label: 'save_image', value: 'save_image' }
    ]}
>
<TabItem value="save_image">

Save an image from a lab VM to the attached shared image gallery. Saves an image from a lab VM to the attached shared image gallery.

```sql
EXEC azure_extras.lab_services.lab_plans.save_image 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_plan_name='{{ lab_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"labVirtualMachineId": "{{ labVirtualMachineId }}"
}'
;
```
</TabItem>
</Tabs>
