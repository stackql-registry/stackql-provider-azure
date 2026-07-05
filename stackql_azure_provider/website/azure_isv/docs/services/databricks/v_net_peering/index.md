--- 
title: v_net_peering
hide_title: false
hide_table_of_contents: false
keywords:
  - v_net_peering
  - databricks
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>v_net_peering</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="v_net_peering" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.v_net_peering" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="allowForwardedTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowGatewayTransit" /></td>
    <td><code>boolean</code></td>
    <td>If gateway links can be used in remote virtual networking to link to this virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowVirtualNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.</td>
</tr>
<tr>
    <td><CopyableCode code="databricksAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the databricks virtual network address space.</td>
</tr>
<tr>
    <td><CopyableCode code="databricksVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>The remote virtual network should be in the same region. See here to learn more (`https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering `_).</td>
</tr>
<tr>
    <td><CopyableCode code="peeringState" /></td>
    <td><code>string</code></td>
    <td>The status of the virtual network peering. Known values are: "Initiated", "Connected", and "Disconnected". (Initiated, Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network peering resource. Known values are: "Succeeded", "Updating", "Deleting", and "Failed". (Succeeded, Updating, Deleting, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the remote virtual network address space.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>The remote virtual network should be in the same region. See here to learn more (`https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering `_). Required.</td>
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
    <td><CopyableCode code="useRemoteGateways" /></td>
    <td><code>boolean</code></td>
    <td>If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="allowForwardedTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowGatewayTransit" /></td>
    <td><code>boolean</code></td>
    <td>If gateway links can be used in remote virtual networking to link to this virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowVirtualNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.</td>
</tr>
<tr>
    <td><CopyableCode code="databricksAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the databricks virtual network address space.</td>
</tr>
<tr>
    <td><CopyableCode code="databricksVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>The remote virtual network should be in the same region. See here to learn more (`https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering `_).</td>
</tr>
<tr>
    <td><CopyableCode code="peeringState" /></td>
    <td><code>string</code></td>
    <td>The status of the virtual network peering. Known values are: "Initiated", "Connected", and "Disconnected". (Initiated, Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network peering resource. Known values are: "Succeeded", "Updating", "Deleting", and "Failed". (Succeeded, Updating, Deleting, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the remote virtual network address space.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>The remote virtual network should be in the same region. See here to learn more (`https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering `_). Required.</td>
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
    <td><CopyableCode code="useRemoteGateways" /></td>
    <td><code>boolean</code></td>
    <td>If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the workspace vNet Peering.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the workspace vNet Peerings.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates vNet Peering for workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates vNet Peering for workspace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the workspace vNetPeering.</td>
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
<tr id="parameter-peering_name">
    <td><CopyableCode code="peering_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace vNet peering. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Gets the workspace vNet Peering.

```sql
SELECT
id,
name,
allowForwardedTraffic,
allowGatewayTransit,
allowVirtualNetworkAccess,
databricksAddressSpace,
databricksVirtualNetwork,
peeringState,
provisioningState,
remoteAddressSpace,
remoteVirtualNetwork,
systemData,
type,
useRemoteGateways
FROM azure_isv.databricks.v_net_peering
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

Lists the workspace vNet Peerings.

```sql
SELECT
id,
name,
allowForwardedTraffic,
allowGatewayTransit,
allowVirtualNetworkAccess,
databricksAddressSpace,
databricksVirtualNetwork,
peeringState,
provisioningState,
remoteAddressSpace,
remoteVirtualNetwork,
systemData,
type,
useRemoteGateways
FROM azure_isv.databricks.v_net_peering
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Creates vNet Peering for workspace.

```sql
INSERT INTO azure_isv.databricks.v_net_peering (
properties,
resource_group_name,
workspace_name,
peering_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ peering_name }}',
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
- name: v_net_peering
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the v_net_peering resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the v_net_peering resource.
    - name: peering_name
      value: "{{ peering_name }}"
      description: Required parameter for the v_net_peering resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the v_net_peering resource.
    - name: properties
      description: |
        List of properties for vNet Peering. Required.
      value:
        allowVirtualNetworkAccess: {{ allowVirtualNetworkAccess }}
        allowForwardedTraffic: {{ allowForwardedTraffic }}
        allowGatewayTransit: {{ allowGatewayTransit }}
        useRemoteGateways: {{ useRemoteGateways }}
        databricksVirtualNetwork:
          id: "{{ id }}"
        databricksAddressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
        remoteVirtualNetwork:
          id: "{{ id }}"
        remoteAddressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
        peeringState: "{{ peeringState }}"
        provisioningState: "{{ provisioningState }}"
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

Creates vNet Peering for workspace.

```sql
REPLACE azure_isv.databricks.v_net_peering
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Deletes the workspace vNetPeering.

```sql
DELETE FROM azure_isv.databricks.v_net_peering
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
