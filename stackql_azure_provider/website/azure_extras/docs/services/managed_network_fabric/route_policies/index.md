--- 
title: route_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - route_policies
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>route_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="route_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.managed_network_fabric.route_policies" /></td></tr>
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
    <td><CopyableCode code="addressFamilyType" /></td>
    <td><code>string</code></td>
    <td>AddressFamilyType. This parameter decides whether the given ipv4 or ipv6 route policy. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
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
    <td><CopyableCode code="defaultAction" /></td>
    <td><code>string</code></td>
    <td>Default action that needs to be applied when no condition is matched. Example: Permit | Deny. Known values are: "Permit" and "Deny". (Permit, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Arm Resource ID of Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="statements" /></td>
    <td><code>array</code></td>
    <td>Route Policy statements. Required.</td>
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
    <td><CopyableCode code="addressFamilyType" /></td>
    <td><code>string</code></td>
    <td>AddressFamilyType. This parameter decides whether the given ipv4 or ipv6 route policy. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
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
    <td><CopyableCode code="defaultAction" /></td>
    <td><code>string</code></td>
    <td>Default action that needs to be applied when no condition is matched. Example: Permit | Deny. Known values are: "Permit" and "Deny". (Permit, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Arm Resource ID of Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="statements" /></td>
    <td><code>array</code></td>
    <td>Route Policy statements. Required.</td>
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
    <td><CopyableCode code="addressFamilyType" /></td>
    <td><code>string</code></td>
    <td>AddressFamilyType. This parameter decides whether the given ipv4 or ipv6 route policy. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
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
    <td><CopyableCode code="defaultAction" /></td>
    <td><code>string</code></td>
    <td>Default action that needs to be applied when no condition is matched. Example: Permit | Deny. Known values are: "Permit" and "Deny". (Permit, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Arm Resource ID of Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="statements" /></td>
    <td><code>array</code></td>
    <td>Route Policy statements. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_policy_name"><code>route_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements Route Policy GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements RoutePolicies list by resource group GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements RoutePolicies list by subscription GET method.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_policy_name"><code>route_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Implements Route Policy PUT method.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_policy_name"><code>route_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>API to update certain properties of the Route Policy resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_policy_name"><code>route_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements Route Policy DELETE method.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_policy_name"><code>route_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updated the admin state for this Route Policy.</td>
</tr>
<tr>
    <td><a href="#validate_configuration"><CopyableCode code="validate_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_policy_name"><code>route_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates the configuration of the resources.</td>
</tr>
<tr>
    <td><a href="#commit_configuration"><CopyableCode code="commit_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_policy_name"><code>route_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Commits the configuration of the given resources.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-route_policy_name">
    <td><CopyableCode code="route_policy_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Route Policy. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Implements Route Policy GET method.

```sql
SELECT
id,
name,
addressFamilyType,
administrativeState,
annotation,
configurationState,
defaultAction,
lastOperation,
location,
networkFabricId,
provisioningState,
statements,
systemData,
tags,
type
FROM azure_extras.managed_network_fabric.route_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND route_policy_name = '{{ route_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Implements RoutePolicies list by resource group GET method.

```sql
SELECT
id,
name,
addressFamilyType,
administrativeState,
annotation,
configurationState,
defaultAction,
lastOperation,
location,
networkFabricId,
provisioningState,
statements,
systemData,
tags,
type
FROM azure_extras.managed_network_fabric.route_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Implements RoutePolicies list by subscription GET method.

```sql
SELECT
id,
name,
addressFamilyType,
administrativeState,
annotation,
configurationState,
defaultAction,
lastOperation,
location,
networkFabricId,
provisioningState,
statements,
systemData,
tags,
type
FROM azure_extras.managed_network_fabric.route_policies
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Implements Route Policy PUT method.

```sql
INSERT INTO azure_extras.managed_network_fabric.route_policies (
tags,
location,
properties,
resource_group_name,
route_policy_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ route_policy_name }}',
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
- name: route_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the route_policies resource.
    - name: route_policy_name
      value: "{{ route_policy_name }}"
      description: Required parameter for the route_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the route_policies resource.
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
        The RoutePolicy properties. Required.
      value:
        annotation: "{{ annotation }}"
        defaultAction: "{{ defaultAction }}"
        statements:
          - annotation: "{{ annotation }}"
            sequenceNumber: {{ sequenceNumber }}
            condition:
              ipCommunityIds:
                - "{{ ipCommunityIds }}"
              ipExtendedCommunityIds:
                - "{{ ipExtendedCommunityIds }}"
              type: "{{ type }}"
              ipPrefixId: "{{ ipPrefixId }}"
            action:
              localPreference: {{ localPreference }}
              actionType: "{{ actionType }}"
              ipCommunityProperties:
                add:
                  ipCommunityIds: "{{ ipCommunityIds }}"
                delete:
                  ipCommunityIds: "{{ ipCommunityIds }}"
                set:
                  ipCommunityIds: "{{ ipCommunityIds }}"
              ipExtendedCommunityProperties:
                add:
                  ipExtendedCommunityIds: "{{ ipExtendedCommunityIds }}"
                delete:
                  ipExtendedCommunityIds: "{{ ipExtendedCommunityIds }}"
                set:
                  ipExtendedCommunityIds: "{{ ipExtendedCommunityIds }}"
        networkFabricId: "{{ networkFabricId }}"
        addressFamilyType: "{{ addressFamilyType }}"
        lastOperation:
          details: "{{ details }}"
        configurationState: "{{ configurationState }}"
        provisioningState: "{{ provisioningState }}"
        administrativeState: "{{ administrativeState }}"
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

API to update certain properties of the Route Policy resource.

```sql
UPDATE azure_extras.managed_network_fabric.route_policies
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND route_policy_name = '{{ route_policy_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Implements Route Policy DELETE method.

```sql
DELETE FROM azure_extras.managed_network_fabric.route_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND route_policy_name = '{{ route_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_administrative_state"
    values={[
        { label: 'update_administrative_state', value: 'update_administrative_state' },
        { label: 'validate_configuration', value: 'validate_configuration' },
        { label: 'commit_configuration', value: 'commit_configuration' }
    ]}
>
<TabItem value="update_administrative_state">

Updated the admin state for this Route Policy.

```sql
EXEC azure_extras.managed_network_fabric.route_policies.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@route_policy_name='{{ route_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="validate_configuration">

Validates the configuration of the resources.

```sql
EXEC azure_extras.managed_network_fabric.route_policies.validate_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@route_policy_name='{{ route_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="commit_configuration">

Commits the configuration of the given resources.

```sql
EXEC azure_extras.managed_network_fabric.route_policies.commit_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@route_policy_name='{{ route_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
