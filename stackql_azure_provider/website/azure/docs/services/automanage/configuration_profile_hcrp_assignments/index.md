--- 
title: configuration_profile_hcrp_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_hcrp_assignments
  - automanage
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

Creates, updates, deletes, gets or lists a <code>configuration_profile_hcrp_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configuration_profile_hcrp_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.configuration_profile_hcrp_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="configurationProfile" /></td>
    <td><code>string</code></td>
    <td>The Automanage configurationProfile ARM Resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Azure resource id. Indicates if this resource is managed by another Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of onboarding, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetId" /></td>
    <td><code>string</code></td>
    <td>The target VM resource URI.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-configuration_profile_assignment_name"><code>configuration_profile_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get information about a configuration profile assignment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-configuration_profile_assignment_name"><code>configuration_profile_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an association between a ARC machine and Automanage configuration profile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-configuration_profile_assignment_name"><code>configuration_profile_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an association between a ARC machine and Automanage configuration profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-configuration_profile_assignment_name"><code>configuration_profile_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a configuration profile assignment.</td>
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
<tr id="parameter-configuration_profile_assignment_name">
    <td><CopyableCode code="configuration_profile_assignment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the configuration profile assignment. Required.</td>
</tr>
<tr id="parameter-machine_name">
    <td><CopyableCode code="machine_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Arc machine. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get information about a configuration profile assignment.

```sql
SELECT
id,
name,
configurationProfile,
managedBy,
status,
systemData,
targetId,
type
FROM azure.automanage.configuration_profile_hcrp_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND machine_name = '{{ machine_name }}' -- required
AND configuration_profile_assignment_name = '{{ configuration_profile_assignment_name }}' -- required
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

Creates an association between a ARC machine and Automanage configuration profile.

```sql
INSERT INTO azure.automanage.configuration_profile_hcrp_assignments (
properties,
resource_group_name,
machine_name,
configuration_profile_assignment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ machine_name }}',
'{{ configuration_profile_assignment_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
managedBy,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: configuration_profile_hcrp_assignments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the configuration_profile_hcrp_assignments resource.
    - name: machine_name
      value: "{{ machine_name }}"
      description: Required parameter for the configuration_profile_hcrp_assignments resource.
    - name: configuration_profile_assignment_name
      value: "{{ configuration_profile_assignment_name }}"
      description: Required parameter for the configuration_profile_hcrp_assignments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the configuration_profile_hcrp_assignments resource.
    - name: properties
      description: |
        Properties of the configuration profile assignment.
      value:
        configurationProfile: "{{ configurationProfile }}"
        targetId: "{{ targetId }}"
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

Creates an association between a ARC machine and Automanage configuration profile.

```sql
REPLACE azure.automanage.configuration_profile_hcrp_assignments
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND configuration_profile_assignment_name = '{{ configuration_profile_assignment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
managedBy,
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

Delete a configuration profile assignment.

```sql
DELETE FROM azure.automanage.configuration_profile_hcrp_assignments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND configuration_profile_assignment_name = '{{ configuration_profile_assignment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
