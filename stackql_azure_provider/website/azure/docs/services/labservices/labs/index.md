--- 
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - labservices
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

Creates, updates, deletes, gets or lists a <code>labs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="labs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.labservices.labs" /></td></tr>
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
    <td><CopyableCode code="autoShutdownProfile" /></td>
    <td><code>object</code></td>
    <td>The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionProfile" /></td>
    <td><code>object</code></td>
    <td>The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="labPlanId" /></td>
    <td><code>string</code></td>
    <td>The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the lab. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="rosterProfile" /></td>
    <td><code>object</code></td>
    <td>The lab user list management profile.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The lab security profile.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The lab state. Known values are: "Draft", "Publishing", "Scaling", "Syncing", and "Published".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineProfile" /></td>
    <td><code>object</code></td>
    <td>The profile used for creating lab virtual machines.</td>
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
    <td><CopyableCode code="autoShutdownProfile" /></td>
    <td><code>object</code></td>
    <td>The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionProfile" /></td>
    <td><code>object</code></td>
    <td>The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="labPlanId" /></td>
    <td><code>string</code></td>
    <td>The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the lab. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="rosterProfile" /></td>
    <td><code>object</code></td>
    <td>The lab user list management profile.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The lab security profile.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The lab state. Known values are: "Draft", "Publishing", "Scaling", "Syncing", and "Published".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineProfile" /></td>
    <td><code>object</code></td>
    <td>The profile used for creating lab virtual machines.</td>
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
    <td><CopyableCode code="autoShutdownProfile" /></td>
    <td><code>object</code></td>
    <td>The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionProfile" /></td>
    <td><code>object</code></td>
    <td>The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="labPlanId" /></td>
    <td><code>string</code></td>
    <td>The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the lab. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="rosterProfile" /></td>
    <td><code>object</code></td>
    <td>The lab user list management profile.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The lab security profile.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The lab state. Known values are: "Draft", "Publishing", "Scaling", "Syncing", and "Published".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineProfile" /></td>
    <td><code>object</code></td>
    <td>The profile used for creating lab virtual machines.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a lab resource. Returns the properties of a lab resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all labs for a subscription and resource group. Returns a list of all labs in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all labs for a subscription. Returns a list of all labs for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a lab resource. Operation to create or update a lab resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a lab resource. Operation to update a lab resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a lab resource. Operation to create or update a lab resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a lab resource. Operation to delete a lab resource.</td>
</tr>
<tr>
    <td><a href="#publish"><CopyableCode code="publish" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Publish or re-publish a lab. Publish or re-publish a lab. This will create or update all lab resources, such as virtual machines.</td>
</tr>
<tr>
    <td><a href="#sync_group"><CopyableCode code="sync_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Manually sync the lab group. Action used to manually kick off an AAD group sync job.</td>
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
<tr id="parameter-lab_name">
    <td><CopyableCode code="lab_name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs. Required.</td>
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

Get a lab resource. Returns the properties of a lab resource.

```sql
SELECT
id,
name,
autoShutdownProfile,
connectionProfile,
description,
labPlanId,
location,
networkProfile,
provisioningState,
rosterProfile,
securityProfile,
state,
systemData,
tags,
title,
type,
virtualMachineProfile
FROM azure.labservices.labs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all labs for a subscription and resource group. Returns a list of all labs in a resource group.

```sql
SELECT
id,
name,
autoShutdownProfile,
connectionProfile,
description,
labPlanId,
location,
networkProfile,
provisioningState,
rosterProfile,
securityProfile,
state,
systemData,
tags,
title,
type,
virtualMachineProfile
FROM azure.labservices.labs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get all labs for a subscription. Returns a list of all labs for a subscription.

```sql
SELECT
id,
name,
autoShutdownProfile,
connectionProfile,
description,
labPlanId,
location,
networkProfile,
provisioningState,
rosterProfile,
securityProfile,
state,
systemData,
tags,
title,
type,
virtualMachineProfile
FROM azure.labservices.labs
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

Create or update a lab resource. Operation to create or update a lab resource.

```sql
INSERT INTO azure.labservices.labs (
tags,
location,
properties,
resource_group_name,
lab_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ lab_name }}',
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
- name: labs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the labs resource.
    - name: lab_name
      value: "{{ lab_name }}"
      description: Required parameter for the labs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the labs resource.
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
        autoShutdownProfile:
          shutdownOnDisconnect: "{{ shutdownOnDisconnect }}"
          shutdownWhenNotConnected: "{{ shutdownWhenNotConnected }}"
          shutdownOnIdle: "{{ shutdownOnIdle }}"
          disconnectDelay: "{{ disconnectDelay }}"
          noConnectDelay: "{{ noConnectDelay }}"
          idleDelay: "{{ idleDelay }}"
        connectionProfile:
          webSshAccess: "{{ webSshAccess }}"
          webRdpAccess: "{{ webRdpAccess }}"
          clientSshAccess: "{{ clientSshAccess }}"
          clientRdpAccess: "{{ clientRdpAccess }}"
        virtualMachineProfile:
          createOption: "{{ createOption }}"
          imageReference:
            id: "{{ id }}"
            offer: "{{ offer }}"
            publisher: "{{ publisher }}"
            sku: "{{ sku }}"
            version: "{{ version }}"
            exactVersion: "{{ exactVersion }}"
          osType: "{{ osType }}"
          sku:
            name: "{{ name }}"
            tier: "{{ tier }}"
            size: "{{ size }}"
            family: "{{ family }}"
            capacity: {{ capacity }}
          additionalCapabilities:
            installGpuDrivers: "{{ installGpuDrivers }}"
          usageQuota: "{{ usageQuota }}"
          useSharedPassword: "{{ useSharedPassword }}"
          adminUser:
            username: "{{ username }}"
            password: "{{ password }}"
          nonAdminUser:
            username: "{{ username }}"
            password: "{{ password }}"
        securityProfile:
          registrationCode: "{{ registrationCode }}"
          openAccess: "{{ openAccess }}"
        rosterProfile:
          activeDirectoryGroupId: "{{ activeDirectoryGroupId }}"
          ltiContextId: "{{ ltiContextId }}"
          lmsInstance: "{{ lmsInstance }}"
          ltiClientId: "{{ ltiClientId }}"
          ltiRosterEndpoint: "{{ ltiRosterEndpoint }}"
        labPlanId: "{{ labPlanId }}"
        title: "{{ title }}"
        description: "{{ description }}"
        networkProfile:
          subnetId: "{{ subnetId }}"
          loadBalancerId: "{{ loadBalancerId }}"
          publicIpId: "{{ publicIpId }}"
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

Update a lab resource. Operation to update a lab resource.

```sql
UPDATE azure.labservices.labs
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
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

Create or update a lab resource. Operation to create or update a lab resource.

```sql
REPLACE azure.labservices.labs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
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

Deletes a lab resource. Operation to delete a lab resource.

```sql
DELETE FROM azure.labservices.labs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="publish"
    values={[
        { label: 'publish', value: 'publish' },
        { label: 'sync_group', value: 'sync_group' }
    ]}
>
<TabItem value="publish">

Publish or re-publish a lab. Publish or re-publish a lab. This will create or update all lab resources, such as virtual machines.

```sql
EXEC azure.labservices.labs.publish 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="sync_group">

Manually sync the lab group. Action used to manually kick off an AAD group sync job.

```sql
EXEC azure.labservices.labs.sync_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
