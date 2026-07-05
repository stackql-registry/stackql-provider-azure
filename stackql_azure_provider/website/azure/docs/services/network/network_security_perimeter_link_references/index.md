--- 
title: network_security_perimeter_link_references
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_link_references
  - network
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter_link_references</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_security_perimeter_link_references" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_security_perimeter_link_references" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A message sent by the remote NSP link admin for connection request. In case of Auto-approved flow, it is default to 'Auto Approved'.</td>
</tr>
<tr>
    <td><CopyableCode code="localInboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Local Inbound profile names to which Inbound is allowed. Use ['*'] to allow inbound to all profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="localOutboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Local Outbound profile names from which Outbound is allowed. In current version, it is readonly property and it's value is set to ['*'] to allow outbound from all profiles. In later version, user will be able to modify it.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NSP LinkReference resource. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "WaitForRemoteCompletion". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, WaitForRemoteCompletion)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteInboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Inbound profile names to which Inbound is allowed. ['*'] value implies inbound is allowed to all profiles at remote perimeter. This property can only be updated from corresponding link resource present in remote perimeter.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteOutboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Outbound profile names from which Outbound is allowed. ['*'] value implies outbound is allowed from all profiles at remote perimeter. This property can only be updated from corresponding link resource present in remote perimeter.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterGuid" /></td>
    <td><code>string</code></td>
    <td>Remote NSP Guid with which the link is created.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterLocation" /></td>
    <td><code>string</code></td>
    <td>Remote NSP location with which the link gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterResourceId" /></td>
    <td><code>string</code></td>
    <td>Perimeter ARM Id for the remote NSP with which the link is created.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The NSP linkReference state. It cannot be changed if link is created in auto-approval mode. Known values are: "Approved", "Pending", "Rejected", and "Disconnected". (Approved, Pending, Rejected, Disconnected)</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A message sent by the remote NSP link admin for connection request. In case of Auto-approved flow, it is default to 'Auto Approved'.</td>
</tr>
<tr>
    <td><CopyableCode code="localInboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Local Inbound profile names to which Inbound is allowed. Use ['*'] to allow inbound to all profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="localOutboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Local Outbound profile names from which Outbound is allowed. In current version, it is readonly property and it's value is set to ['*'] to allow outbound from all profiles. In later version, user will be able to modify it.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NSP LinkReference resource. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "WaitForRemoteCompletion". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, WaitForRemoteCompletion)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteInboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Inbound profile names to which Inbound is allowed. ['*'] value implies inbound is allowed to all profiles at remote perimeter. This property can only be updated from corresponding link resource present in remote perimeter.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteOutboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Outbound profile names from which Outbound is allowed. ['*'] value implies outbound is allowed from all profiles at remote perimeter. This property can only be updated from corresponding link resource present in remote perimeter.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterGuid" /></td>
    <td><code>string</code></td>
    <td>Remote NSP Guid with which the link is created.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterLocation" /></td>
    <td><code>string</code></td>
    <td>Remote NSP location with which the link gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterResourceId" /></td>
    <td><code>string</code></td>
    <td>Perimeter ARM Id for the remote NSP with which the link is created.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The NSP linkReference state. It cannot be changed if link is created in auto-approval mode. Known values are: "Approved", "Pending", "Rejected", and "Disconnected". (Approved, Pending, Rejected, Disconnected)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-link_reference_name"><code>link_reference_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified NSP linkReference resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists the NSP LinkReference resources in the specified network security perimeter.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-link_reference_name"><code>link_reference_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an NSP LinkReference resource.</td>
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
<tr id="parameter-link_reference_name">
    <td><CopyableCode code="link_reference_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NSP linkReference. Required.</td>
</tr>
<tr id="parameter-network_security_perimeter_name">
    <td><CopyableCode code="network_security_perimeter_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network security perimeter. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>SkipToken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>An optional query parameter which specifies the maximum number of records to be returned by the server. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified NSP linkReference resource.

```sql
SELECT
id,
name,
description,
localInboundProfiles,
localOutboundProfiles,
provisioningState,
remoteInboundProfiles,
remoteOutboundProfiles,
remotePerimeterGuid,
remotePerimeterLocation,
remotePerimeterResourceId,
status,
systemData,
type
FROM azure.network.network_security_perimeter_link_references
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' -- required
AND link_reference_name = '{{ link_reference_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the NSP LinkReference resources in the specified network security perimeter.

```sql
SELECT
id,
name,
description,
localInboundProfiles,
localOutboundProfiles,
provisioningState,
remoteInboundProfiles,
remoteOutboundProfiles,
remotePerimeterGuid,
remotePerimeterLocation,
remotePerimeterResourceId,
status,
systemData,
type
FROM azure.network.network_security_perimeter_link_references
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
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

Deletes an NSP LinkReference resource.

```sql
DELETE FROM azure.network.network_security_perimeter_link_references
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' --required
AND link_reference_name = '{{ link_reference_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
