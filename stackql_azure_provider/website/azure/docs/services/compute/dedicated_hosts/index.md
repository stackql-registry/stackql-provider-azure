--- 
title: dedicated_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hosts
  - compute
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

Creates, updates, deletes, gets or lists a <code>dedicated_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dedicated_hosts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.dedicated_hosts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_host_group', value: 'list_by_host_group' }
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
    <td><CopyableCode code="autoReplaceOnFailure" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the dedicated host should be replaced automatically in case of a failure. The value is defaulted to 'true' when not provided.</td>
</tr>
<tr>
    <td><CopyableCode code="hostId" /></td>
    <td><code>string</code></td>
    <td>A unique id generated and assigned to the dedicated host by the platform. Does not change throughout the lifetime of the host.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The dedicated host instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>Specifies the software license type that will be applied to the VMs deployed on the dedicated host. Possible values are: **None,** **Windows_Server_Hybrid,** **Windows_Server_Perpetual.** The default value is: **None.**. Known values are: "None", "Windows_Server_Hybrid", and "Windows_Server_Perpetual". (None, Windows_Server_Hybrid, Windows_Server_Perpetual)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomain" /></td>
    <td><code>integer</code></td>
    <td>Fault domain of the dedicated host within a dedicated host group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the host was first provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the dedicated host for Hardware Generation and VM family. Only name is required to be set. List Microsoft.Compute SKUs for a list of possible values. Required.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Dedicated Host resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the Dedicated Host.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_host_group">

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
    <td><CopyableCode code="autoReplaceOnFailure" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the dedicated host should be replaced automatically in case of a failure. The value is defaulted to 'true' when not provided.</td>
</tr>
<tr>
    <td><CopyableCode code="hostId" /></td>
    <td><code>string</code></td>
    <td>A unique id generated and assigned to the dedicated host by the platform. Does not change throughout the lifetime of the host.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The dedicated host instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>Specifies the software license type that will be applied to the VMs deployed on the dedicated host. Possible values are: **None,** **Windows_Server_Hybrid,** **Windows_Server_Perpetual.** The default value is: **None.**. Known values are: "None", "Windows_Server_Hybrid", and "Windows_Server_Perpetual". (None, Windows_Server_Hybrid, Windows_Server_Perpetual)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomain" /></td>
    <td><code>integer</code></td>
    <td>Fault domain of the dedicated host within a dedicated host group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the host was first provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the dedicated host for Hardware Generation and VM family. Only name is required to be set. List Microsoft.Compute SKUs for a list of possible values. Required.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Dedicated Host resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the Dedicated Host.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieves information about a dedicated host.</td>
</tr>
<tr>
    <td><a href="#list_by_host_group"><CopyableCode code="list_by_host_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update a dedicated host .</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a dedicated host .</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update a dedicated host .</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a dedicated host.</td>
</tr>
<tr>
    <td><a href="#list_available_sizes"><CopyableCode code="list_available_sizes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available dedicated host sizes to which the specified dedicated host can be resized. NOTE: The dedicated host sizes provided can be used to only scale up the existing dedicated host.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Redeploy the dedicated host. The operation will complete successfully once the dedicated host has migrated to a new node and is running. To determine the health of VMs deployed on the dedicated host after the redeploy check the Resource Health Center in the Azure Portal. Please refer to `https://docs.microsoft.com/azure/service-health/resource-health-overview `_ for more details.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_group_name"><code>host_group_name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restart the dedicated host. The operation will complete successfully once the dedicated host has restarted and is running. To determine the health of VMs deployed on the dedicated host after the restart check the Resource Health Center in the Azure Portal. Please refer to `https://docs.microsoft.com/azure/service-health/resource-health-overview `_ for more details.</td>
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
<tr id="parameter-host_group_name">
    <td><CopyableCode code="host_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the dedicated host group. Required.</td>
</tr>
<tr id="parameter-host_name">
    <td><CopyableCode code="host_name" /></td>
    <td><code>string</code></td>
    <td>The name of the dedicated host. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the dedicated host. 'UserData' is not supported for dedicated host. Known values are: "instanceView", "userData", and "resiliencyView". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_host_group', value: 'list_by_host_group' }
    ]}
>
<TabItem value="get">

Retrieves information about a dedicated host.

```sql
SELECT
id,
name,
autoReplaceOnFailure,
hostId,
instanceView,
licenseType,
location,
platformFaultDomain,
provisioningState,
provisioningTime,
sku,
systemData,
tags,
timeCreated,
type,
virtualMachines
FROM azure.compute.dedicated_hosts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_group_name = '{{ host_group_name }}' -- required
AND host_name = '{{ host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_host_group">

Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts.

```sql
SELECT
id,
name,
autoReplaceOnFailure,
hostId,
instanceView,
licenseType,
location,
platformFaultDomain,
provisioningState,
provisioningTime,
sku,
systemData,
tags,
timeCreated,
type,
virtualMachines
FROM azure.compute.dedicated_hosts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_group_name = '{{ host_group_name }}' -- required
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

Create or update a dedicated host .

```sql
INSERT INTO azure.compute.dedicated_hosts (
tags,
location,
properties,
sku,
resource_group_name,
host_group_name,
host_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ resource_group_name }}',
'{{ host_group_name }}',
'{{ host_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
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
- name: dedicated_hosts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dedicated_hosts resource.
    - name: host_group_name
      value: "{{ host_group_name }}"
      description: Required parameter for the dedicated_hosts resource.
    - name: host_name
      value: "{{ host_name }}"
      description: Required parameter for the dedicated_hosts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dedicated_hosts resource.
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
        Properties of the dedicated host.
      value:
        platformFaultDomain: {{ platformFaultDomain }}
        autoReplaceOnFailure: {{ autoReplaceOnFailure }}
        hostId: "{{ hostId }}"
        virtualMachines:
          - id: "{{ id }}"
        licenseType: "{{ licenseType }}"
        provisioningTime: "{{ provisioningTime }}"
        provisioningState: "{{ provisioningState }}"
        instanceView:
          assetId: "{{ assetId }}"
          availableCapacity:
            allocatableVMs:
              - vmSize: "{{ vmSize }}"
                count: {{ count }}
          statuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        timeCreated: "{{ timeCreated }}"
    - name: sku
      description: |
        SKU of the dedicated host for Hardware Generation and VM family. Only name is required to be set. List Microsoft.Compute SKUs for a list of possible values. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
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

Update a dedicated host .

```sql
UPDATE azure.compute.dedicated_hosts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND host_group_name = '{{ host_group_name }}' --required
AND host_name = '{{ host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Create or update a dedicated host .

```sql
REPLACE azure.compute.dedicated_hosts
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND host_group_name = '{{ host_group_name }}' --required
AND host_name = '{{ host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
location,
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

Delete a dedicated host.

```sql
DELETE FROM azure.compute.dedicated_hosts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND host_group_name = '{{ host_group_name }}' --required
AND host_name = '{{ host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_available_sizes"
    values={[
        { label: 'list_available_sizes', value: 'list_available_sizes' },
        { label: 'redeploy', value: 'redeploy' },
        { label: 'restart', value: 'restart' }
    ]}
>
<TabItem value="list_available_sizes">

Lists all available dedicated host sizes to which the specified dedicated host can be resized. NOTE: The dedicated host sizes provided can be used to only scale up the existing dedicated host.

```sql
EXEC azure.compute.dedicated_hosts.list_available_sizes 
@resource_group_name='{{ resource_group_name }}' --required, 
@host_group_name='{{ host_group_name }}' --required, 
@host_name='{{ host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="redeploy">

Redeploy the dedicated host. The operation will complete successfully once the dedicated host has migrated to a new node and is running. To determine the health of VMs deployed on the dedicated host after the redeploy check the Resource Health Center in the Azure Portal. Please refer to `https://docs.microsoft.com/azure/service-health/resource-health-overview `_ for more details.

```sql
EXEC azure.compute.dedicated_hosts.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@host_group_name='{{ host_group_name }}' --required, 
@host_name='{{ host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restart the dedicated host. The operation will complete successfully once the dedicated host has restarted and is running. To determine the health of VMs deployed on the dedicated host after the restart check the Resource Health Center in the Azure Portal. Please refer to `https://docs.microsoft.com/azure/service-health/resource-health-overview `_ for more details.

```sql
EXEC azure.compute.dedicated_hosts.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@host_group_name='{{ host_group_name }}' --required, 
@host_name='{{ host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
