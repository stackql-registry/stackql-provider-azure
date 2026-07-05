--- 
title: network_bootstrap_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_bootstrap_interfaces
  - managednetworkfabric
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

Creates, updates, deletes, gets or lists a <code>network_bootstrap_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_bootstrap_interfaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managednetworkfabric.network_bootstrap_interfaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_network_bootstrap_device', value: 'list_by_network_bootstrap_device' }
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
    <td><CopyableCode code="additionalDescription" /></td>
    <td><code>string</code></td>
    <td>Additional description of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="connectedTo" /></td>
    <td><code>string</code></td>
    <td>Connected to information of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="interfaceType" /></td>
    <td><code>string</code></td>
    <td>Type of the interface. Known values are: "Management" and "Data". (Management, Data)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4Address" /></td>
    <td><code>string</code></td>
    <td>IPv4Address of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6Address" /></td>
    <td><code>string</code></td>
    <td>IPv6Address of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="physicalIdentifier" /></td>
    <td><code>string</code></td>
    <td>Physical identifier of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the interface. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.</td>
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
<TabItem value="list_by_network_bootstrap_device">

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
    <td><CopyableCode code="additionalDescription" /></td>
    <td><code>string</code></td>
    <td>Additional description of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="connectedTo" /></td>
    <td><code>string</code></td>
    <td>Connected to information of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="interfaceType" /></td>
    <td><code>string</code></td>
    <td>Type of the interface. Known values are: "Management" and "Data". (Management, Data)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4Address" /></td>
    <td><code>string</code></td>
    <td>IPv4Address of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6Address" /></td>
    <td><code>string</code></td>
    <td>IPv6Address of the interface.</td>
</tr>
<tr>
    <td><CopyableCode code="physicalIdentifier" /></td>
    <td><code>string</code></td>
    <td>Physical identifier of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the interface. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-network_bootstrap_interface_name"><code>network_bootstrap_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Network Bootstrap Interface resource details.</td>
</tr>
<tr>
    <td><a href="#list_by_network_bootstrap_device"><CopyableCode code="list_by_network_bootstrap_device" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Bootstrap Interface resources in a given resource group.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-network_bootstrap_interface_name"><code>network_bootstrap_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a Network Bootstrap Interface resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-network_bootstrap_interface_name"><code>network_bootstrap_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update certain properties of the Network Bootstrap Interface resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-network_bootstrap_interface_name"><code>network_bootstrap_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the Network Bootstrap Interface resource.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-network_bootstrap_interface_name"><code>network_bootstrap_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the admin state of the Network Interface.</td>
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
<tr id="parameter-network_bootstrap_device_name">
    <td><CopyableCode code="network_bootstrap_device_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Bootstrap Device. Required.</td>
</tr>
<tr id="parameter-network_bootstrap_interface_name">
    <td><CopyableCode code="network_bootstrap_interface_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Bootstrap Interface. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_network_bootstrap_device', value: 'list_by_network_bootstrap_device' }
    ]}
>
<TabItem value="get">

Get the Network Bootstrap Interface resource details.

```sql
SELECT
id,
name,
additionalDescription,
administrativeState,
annotation,
configurationState,
connectedTo,
description,
interfaceType,
ipv4Address,
ipv6Address,
physicalIdentifier,
provisioningState,
serialNumber,
systemData,
type
FROM azure.managednetworkfabric.network_bootstrap_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_bootstrap_device_name = '{{ network_bootstrap_device_name }}' -- required
AND network_bootstrap_interface_name = '{{ network_bootstrap_interface_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_network_bootstrap_device">

List all the Network Bootstrap Interface resources in a given resource group.

```sql
SELECT
id,
name,
additionalDescription,
administrativeState,
annotation,
configurationState,
connectedTo,
description,
interfaceType,
ipv4Address,
ipv6Address,
physicalIdentifier,
provisioningState,
serialNumber,
systemData,
type
FROM azure.managednetworkfabric.network_bootstrap_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_bootstrap_device_name = '{{ network_bootstrap_device_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a Network Bootstrap Interface resource.

```sql
INSERT INTO azure.managednetworkfabric.network_bootstrap_interfaces (
properties,
resource_group_name,
network_bootstrap_device_name,
network_bootstrap_interface_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ network_bootstrap_device_name }}',
'{{ network_bootstrap_interface_name }}',
'{{ subscription_id }}'
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
- name: network_bootstrap_interfaces
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_bootstrap_interfaces resource.
    - name: network_bootstrap_device_name
      value: "{{ network_bootstrap_device_name }}"
      description: Required parameter for the network_bootstrap_interfaces resource.
    - name: network_bootstrap_interface_name
      value: "{{ network_bootstrap_interface_name }}"
      description: Required parameter for the network_bootstrap_interfaces resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_bootstrap_interfaces resource.
    - name: properties
      description: |
        The NetworkBootstrapInterface properties. Required.
      value:
        annotation: "{{ annotation }}"
        provisioningState: "{{ provisioningState }}"
        administrativeState: "{{ administrativeState }}"
        configurationState: "{{ configurationState }}"
        physicalIdentifier: "{{ physicalIdentifier }}"
        connectedTo: "{{ connectedTo }}"
        interfaceType: "{{ interfaceType }}"
        description: "{{ description }}"
        additionalDescription: "{{ additionalDescription }}"
        ipv4Address: "{{ ipv4Address }}"
        ipv6Address: "{{ ipv6Address }}"
        serialNumber: "{{ serialNumber }}"
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

Update certain properties of the Network Bootstrap Interface resource.

```sql
UPDATE azure.managednetworkfabric.network_bootstrap_interfaces
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_bootstrap_device_name = '{{ network_bootstrap_device_name }}' --required
AND network_bootstrap_interface_name = '{{ network_bootstrap_interface_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Delete the Network Bootstrap Interface resource.

```sql
DELETE FROM azure.managednetworkfabric.network_bootstrap_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_bootstrap_device_name = '{{ network_bootstrap_device_name }}' --required
AND network_bootstrap_interface_name = '{{ network_bootstrap_interface_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_administrative_state"
    values={[
        { label: 'update_administrative_state', value: 'update_administrative_state' }
    ]}
>
<TabItem value="update_administrative_state">

Update the admin state of the Network Interface.

```sql
EXEC azure.managednetworkfabric.network_bootstrap_interfaces.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_bootstrap_device_name='{{ network_bootstrap_device_name }}' --required, 
@network_bootstrap_interface_name='{{ network_bootstrap_interface_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
</Tabs>
