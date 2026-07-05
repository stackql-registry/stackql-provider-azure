--- 
title: network_security_perimeter_links
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_links
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_security_perimeter_links" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_security_perimeter_links" /></td></tr>
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
    <td><CopyableCode code="autoApprovedRemotePerimeterResourceId" /></td>
    <td><code>string</code></td>
    <td>Perimeter ARM Id for the remote NSP with which the link gets created in Auto-approval mode. It should be used when the NSP admin have Microsoft.Network/networkSecurityPerimeters/linkPerimeter/action permission on the remote NSP resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A message passed to the owner of the remote NSP link resource with this connection request. In case of Auto-approved flow, it is default to 'Auto Approved'. Restricted to 140 chars.</td>
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
    <td>The provisioning state of the NSP Link resource. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "WaitForRemoteCompletion". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, WaitForRemoteCompletion)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteInboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Inbound profile names to which Inbound is allowed. Use ['*'] to allow inbound to all profiles. This property can only be updated in auto-approval mode.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteOutboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Outbound profile names from which Outbound is allowed. In current version, it is readonly property and it's value is set to ['*'] to allow outbound from all profiles. In later version, user will be able to modify it.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterGuid" /></td>
    <td><code>string</code></td>
    <td>Remote NSP Guid with which the link gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterLocation" /></td>
    <td><code>string</code></td>
    <td>Remote NSP location with which the link gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The NSP link state. Known values are: "Approved", "Pending", "Rejected", and "Disconnected". (Approved, Pending, Rejected, Disconnected)</td>
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
    <td><CopyableCode code="autoApprovedRemotePerimeterResourceId" /></td>
    <td><code>string</code></td>
    <td>Perimeter ARM Id for the remote NSP with which the link gets created in Auto-approval mode. It should be used when the NSP admin have Microsoft.Network/networkSecurityPerimeters/linkPerimeter/action permission on the remote NSP resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A message passed to the owner of the remote NSP link resource with this connection request. In case of Auto-approved flow, it is default to 'Auto Approved'. Restricted to 140 chars.</td>
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
    <td>The provisioning state of the NSP Link resource. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "WaitForRemoteCompletion". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, WaitForRemoteCompletion)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteInboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Inbound profile names to which Inbound is allowed. Use ['*'] to allow inbound to all profiles. This property can only be updated in auto-approval mode.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteOutboundProfiles" /></td>
    <td><code>array</code></td>
    <td>Remote Outbound profile names from which Outbound is allowed. In current version, it is readonly property and it's value is set to ['*'] to allow outbound from all profiles. In later version, user will be able to modify it.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterGuid" /></td>
    <td><code>string</code></td>
    <td>Remote NSP Guid with which the link gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="remotePerimeterLocation" /></td>
    <td><code>string</code></td>
    <td>Remote NSP location with which the link gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The NSP link state. Known values are: "Approved", "Pending", "Rejected", and "Disconnected". (Approved, Pending, Rejected, Disconnected)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-link_name"><code>link_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified NSP link resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists the NSP Link resources in the specified network security perimeter.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-link_name"><code>link_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates NSP link resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-link_name"><code>link_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates NSP link resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-link_name"><code>link_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an NSP Link resource.</td>
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
<tr id="parameter-link_name">
    <td><CopyableCode code="link_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NSP link. Required.</td>
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

Gets the specified NSP link resource.

```sql
SELECT
id,
name,
autoApprovedRemotePerimeterResourceId,
description,
localInboundProfiles,
localOutboundProfiles,
provisioningState,
remoteInboundProfiles,
remoteOutboundProfiles,
remotePerimeterGuid,
remotePerimeterLocation,
status,
systemData,
type
FROM azure.network.network_security_perimeter_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' -- required
AND link_name = '{{ link_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the NSP Link resources in the specified network security perimeter.

```sql
SELECT
id,
name,
autoApprovedRemotePerimeterResourceId,
description,
localInboundProfiles,
localOutboundProfiles,
provisioningState,
remoteInboundProfiles,
remoteOutboundProfiles,
remotePerimeterGuid,
remotePerimeterLocation,
status,
systemData,
type
FROM azure.network.network_security_perimeter_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Creates or updates NSP link resource.

```sql
INSERT INTO azure.network.network_security_perimeter_links (
properties,
resource_group_name,
network_security_perimeter_name,
link_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_security_perimeter_name }}',
'{{ link_name }}',
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
- name: network_security_perimeter_links
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_security_perimeter_links resource.
    - name: network_security_perimeter_name
      value: "{{ network_security_perimeter_name }}"
      description: Required parameter for the network_security_perimeter_links resource.
    - name: link_name
      value: "{{ link_name }}"
      description: Required parameter for the network_security_perimeter_links resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_security_perimeter_links resource.
    - name: properties
      description: |
        Properties of the network security perimeter link resource.
      value:
        provisioningState: "{{ provisioningState }}"
        autoApprovedRemotePerimeterResourceId: "{{ autoApprovedRemotePerimeterResourceId }}"
        remotePerimeterGuid: "{{ remotePerimeterGuid }}"
        remotePerimeterLocation: "{{ remotePerimeterLocation }}"
        localInboundProfiles:
          - "{{ localInboundProfiles }}"
        localOutboundProfiles:
          - "{{ localOutboundProfiles }}"
        remoteInboundProfiles:
          - "{{ remoteInboundProfiles }}"
        remoteOutboundProfiles:
          - "{{ remoteOutboundProfiles }}"
        description: "{{ description }}"
        status: "{{ status }}"
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

Creates or updates NSP link resource.

```sql
REPLACE azure.network.network_security_perimeter_links
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' --required
AND link_name = '{{ link_name }}' --required
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

Deletes an NSP Link resource.

```sql
DELETE FROM azure.network.network_security_perimeter_links
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' --required
AND link_name = '{{ link_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
