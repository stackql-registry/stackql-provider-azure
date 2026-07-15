--- 
title: shared_limit_caps
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_limit_caps
  - compute_limit
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

Creates, updates, deletes, gets or lists a <code>shared_limit_caps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="shared_limit_caps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute_limit.shared_limit_caps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription_location_resource', value: 'list_by_subscription_location_resource' }
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
    <td><CopyableCode code="defaultMemberCap" /></td>
    <td><code>integer</code></td>
    <td>The default member cap value (in count units). Set to a non-negative integer to apply a cap to all member subscriptions that do not have a per-member override. Omit the property to leave no default cap in effect.</td>
</tr>
<tr>
    <td><CopyableCode code="isBoundedCap" /></td>
    <td><code>boolean</code></td>
    <td>Controls whether the service validates the aggregate cap against the group limit for the VM family. SUM(caps) is the sum of all per-member overrides' cap values plus `defaultMemberCap` multiplied by the number of member subscriptions without an override. When true, the service rejects any configuration where SUM(caps) exceeds the group limit. When false, SUM(caps) is permitted to exceed the group limit. Enabling this flag is rejected if the current configuration already breaches the group limit; reduce caps first, then enable. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
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
<TabItem value="list_by_subscription_location_resource">

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
    <td><CopyableCode code="defaultMemberCap" /></td>
    <td><code>integer</code></td>
    <td>The default member cap value (in count units). Set to a non-negative integer to apply a cap to all member subscriptions that do not have a per-member override. Omit the property to leave no default cap in effect.</td>
</tr>
<tr>
    <td><CopyableCode code="isBoundedCap" /></td>
    <td><code>boolean</code></td>
    <td>Controls whether the service validates the aggregate cap against the group limit for the VM family. SUM(caps) is the sum of all per-member overrides' cap values plus `defaultMemberCap` multiplied by the number of member subscriptions without an override. When true, the service rejects any configuration where SUM(caps) exceeds the group limit. When false, SUM(caps) is permitted to exceed the group limit. Enabling this flag is rejected if the current configuration already breaches the group limit; reduce caps first, then enable. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-vm_family_name"><code>vm_family_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the shared limit cap configuration for a VM family, as visible to the caller's subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription_location_resource"><CopyableCode code="list_by_subscription_location_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all shared limit cap configurations visible to the caller's subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-vm_family_name"><code>vm_family_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or replaces the shared limit cap configuration for a VM family.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-vm_family_name"><code>vm_family_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or replaces the shared limit cap configuration for a VM family.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-vm_family_name"><code>vm_family_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the shared limit cap configuration for a VM family. The caller's subscription is treated as the host subscription.</td>
</tr>
<tr>
    <td><a href="#set_member_cap_overrides"><CopyableCode code="set_member_cap_overrides" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-vm_family_name"><code>vm_family_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-memberCapOverrides"><code>memberCapOverrides</code></a></td>
    <td></td>
    <td>Replaces the full set of per-member cap overrides for this shared limit cap. The supplied array becomes the new complete set of overrides; supplying an empty array clears all existing overrides.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vm_family_name">
    <td><CopyableCode code="vm_family_name" /></td>
    <td><code>string</code></td>
    <td>The name of the SharedLimitCap. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription_location_resource', value: 'list_by_subscription_location_resource' }
    ]}
>
<TabItem value="get">

Gets the shared limit cap configuration for a VM family, as visible to the caller's subscription.

```sql
SELECT
id,
name,
defaultMemberCap,
isBoundedCap,
provisioningState,
systemData,
type
FROM azure.compute_limit.shared_limit_caps
WHERE location = '{{ location }}' -- required
AND vm_family_name = '{{ vm_family_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription_location_resource">

Lists all shared limit cap configurations visible to the caller's subscription.

```sql
SELECT
id,
name,
defaultMemberCap,
isBoundedCap,
provisioningState,
systemData,
type
FROM azure.compute_limit.shared_limit_caps
WHERE location = '{{ location }}' -- required
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

Creates or replaces the shared limit cap configuration for a VM family.

```sql
INSERT INTO azure.compute_limit.shared_limit_caps (
properties,
location,
vm_family_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ vm_family_name }}',
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
- name: shared_limit_caps
  props:
    - name: location
      value: "{{ location }}"
      description: Required parameter for the shared_limit_caps resource.
    - name: vm_family_name
      value: "{{ vm_family_name }}"
      description: Required parameter for the shared_limit_caps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the shared_limit_caps resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        defaultMemberCap: {{ defaultMemberCap }}
        isBoundedCap: {{ isBoundedCap }}
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

Creates or replaces the shared limit cap configuration for a VM family.

```sql
REPLACE azure.compute_limit.shared_limit_caps
SET 
properties = '{{ properties }}'
WHERE 
location = '{{ location }}' --required
AND vm_family_name = '{{ vm_family_name }}' --required
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

Deletes the shared limit cap configuration for a VM family. The caller's subscription is treated as the host subscription.

```sql
DELETE FROM azure.compute_limit.shared_limit_caps
WHERE location = '{{ location }}' --required
AND vm_family_name = '{{ vm_family_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="set_member_cap_overrides"
    values={[
        { label: 'set_member_cap_overrides', value: 'set_member_cap_overrides' }
    ]}
>
<TabItem value="set_member_cap_overrides">

Replaces the full set of per-member cap overrides for this shared limit cap. The supplied array becomes the new complete set of overrides; supplying an empty array clears all existing overrides.

```sql
EXEC azure.compute_limit.shared_limit_caps.set_member_cap_overrides 
@location='{{ location }}' --required, 
@vm_family_name='{{ vm_family_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"memberCapOverrides": "{{ memberCapOverrides }}"
}'
;
```
</TabItem>
</Tabs>
