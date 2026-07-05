--- 
title: jit_network_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_network_access_policies
  - security
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

Creates, updates, deletes, gets or lists a <code>jit_network_access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jit_network_access_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.jit_network_access_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group_and_region', value: 'list_by_resource_group_and_region' },
        { label: 'list_by_region', value: 'list_by_region' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where the resource is stored. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the Just-in-Time policy.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>array</code></td>
    <td>:vartype requests: list[~azure.mgmt.security.models.JitNetworkAccessRequest]</td>
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
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>Configurations for Microsoft.Compute/virtualMachines resource type. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group_and_region">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where the resource is stored. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the Just-in-Time policy.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>array</code></td>
    <td>:vartype requests: list[~azure.mgmt.security.models.JitNetworkAccessRequest]</td>
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
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>Configurations for Microsoft.Compute/virtualMachines resource type. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_region">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where the resource is stored. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the Just-in-Time policy.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>array</code></td>
    <td>:vartype requests: list[~azure.mgmt.security.models.JitNetworkAccessRequest]</td>
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
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>Configurations for Microsoft.Compute/virtualMachines resource type. Required.</td>
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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where the resource is stored. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the Just-in-Time policy.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>array</code></td>
    <td>:vartype requests: list[~azure.mgmt.security.models.JitNetworkAccessRequest]</td>
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
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>Configurations for Microsoft.Compute/virtualMachines resource type. Required.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where the resource is stored. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the Just-in-Time policy.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>array</code></td>
    <td>:vartype requests: list[~azure.mgmt.security.models.JitNetworkAccessRequest]</td>
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
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>Configurations for Microsoft.Compute/virtualMachines resource type. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-jit_network_access_policy_name"><code>jit_network_access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Policies for protecting resources using Just-in-Time access control for the subscription, location.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group_and_region"><CopyableCode code="list_by_resource_group_and_region" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Policies for protecting resources using Just-in-Time access control for the subscription, location.</td>
</tr>
<tr>
    <td><a href="#list_by_region"><CopyableCode code="list_by_region" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Policies for protecting resources using Just-in-Time access control for the subscription, location.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Policies for protecting resources using Just-in-Time access control for the subscription, location.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Policies for protecting resources using Just-in-Time access control.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-jit_network_access_policy_name"><code>jit_network_access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a policy for protecting resources using Just-in-Time access control.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-jit_network_access_policy_name"><code>jit_network_access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a policy for protecting resources using Just-in-Time access control.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-jit_network_access_policy_name"><code>jit_network_access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Just-in-Time access control policy.</td>
</tr>
<tr>
    <td><a href="#initiate"><CopyableCode code="initiate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-jit_network_access_policy_name"><code>jit_network_access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-virtualMachines"><code>virtualMachines</code></a></td>
    <td></td>
    <td>Initiate a JIT access from a specific Just-in-Time policy configuration.</td>
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
<tr id="parameter-asc_location">
    <td><CopyableCode code="asc_location" /></td>
    <td><code>string</code></td>
    <td>The location where ASC stores the data of the subscription. can be retrieved from Get locations. Required.</td>
</tr>
<tr id="parameter-jit_network_access_policy_name">
    <td><CopyableCode code="jit_network_access_policy_name" /></td>
    <td><code>string</code></td>
    <td>Name of a Just-in-Time access configuration policy. Required.</td>
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
        { label: 'list_by_resource_group_and_region', value: 'list_by_resource_group_and_region' },
        { label: 'list_by_region', value: 'list_by_region' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Policies for protecting resources using Just-in-Time access control for the subscription, location.

```sql
SELECT
id,
name,
kind,
location,
provisioningState,
requests,
systemData,
type,
virtualMachines
FROM azure.security.jit_network_access_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND asc_location = '{{ asc_location }}' -- required
AND jit_network_access_policy_name = '{{ jit_network_access_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group_and_region">

Policies for protecting resources using Just-in-Time access control for the subscription, location.

```sql
SELECT
id,
name,
kind,
location,
provisioningState,
requests,
systemData,
type,
virtualMachines
FROM azure.security.jit_network_access_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND asc_location = '{{ asc_location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_region">

Policies for protecting resources using Just-in-Time access control for the subscription, location.

```sql
SELECT
id,
name,
kind,
location,
provisioningState,
requests,
systemData,
type,
virtualMachines
FROM azure.security.jit_network_access_policies
WHERE asc_location = '{{ asc_location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Policies for protecting resources using Just-in-Time access control for the subscription, location.

```sql
SELECT
id,
name,
kind,
location,
provisioningState,
requests,
systemData,
type,
virtualMachines
FROM azure.security.jit_network_access_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Policies for protecting resources using Just-in-Time access control.

```sql
SELECT
id,
name,
kind,
location,
provisioningState,
requests,
systemData,
type,
virtualMachines
FROM azure.security.jit_network_access_policies
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a policy for protecting resources using Just-in-Time access control.

```sql
INSERT INTO azure.security.jit_network_access_policies (
properties,
kind,
resource_group_name,
asc_location,
jit_network_access_policy_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ kind }}',
'{{ resource_group_name }}',
'{{ asc_location }}',
'{{ jit_network_access_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: jit_network_access_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the jit_network_access_policies resource.
    - name: asc_location
      value: "{{ asc_location }}"
      description: Required parameter for the jit_network_access_policies resource.
    - name: jit_network_access_policy_name
      value: "{{ jit_network_access_policy_name }}"
      description: Required parameter for the jit_network_access_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the jit_network_access_policies resource.
    - name: properties
      description: |
        Required.
      value:
        virtualMachines:
          - id: "{{ id }}"
            ports: "{{ ports }}"
            publicIpAddress: "{{ publicIpAddress }}"
        requests:
          - virtualMachines: "{{ virtualMachines }}"
            startTimeUtc: "{{ startTimeUtc }}"
            requestor: "{{ requestor }}"
            justification: "{{ justification }}"
        provisioningState: "{{ provisioningState }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of the resource.
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

Create a policy for protecting resources using Just-in-Time access control.

```sql
REPLACE azure.security.jit_network_access_policies
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND asc_location = '{{ asc_location }}' --required
AND jit_network_access_policy_name = '{{ jit_network_access_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
kind,
location,
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

Delete a Just-in-Time access control policy.

```sql
DELETE FROM azure.security.jit_network_access_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND asc_location = '{{ asc_location }}' --required
AND jit_network_access_policy_name = '{{ jit_network_access_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="initiate"
    values={[
        { label: 'initiate', value: 'initiate' }
    ]}
>
<TabItem value="initiate">

Initiate a JIT access from a specific Just-in-Time policy configuration.

```sql
EXEC azure.security.jit_network_access_policies.initiate 
@resource_group_name='{{ resource_group_name }}' --required, 
@asc_location='{{ asc_location }}' --required, 
@jit_network_access_policy_name='{{ jit_network_access_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"virtualMachines": "{{ virtualMachines }}", 
"justification": "{{ justification }}"
}'
;
```
</TabItem>
</Tabs>
