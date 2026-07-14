--- 
title: dataflow_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_profile
  - iot_operations
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

Creates, updates, deletes, gets or lists a <code>dataflow_profile</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dataflow_profile" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_operations.dataflow_profile" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
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
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Spec defines the desired identities of NBC diagnostics settings.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="instanceCount" /></td>
    <td><code>integer</code></td>
    <td>To manually scale the dataflow profile, specify the maximum number of instances you want to run.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status for the dataflow profile.</td>
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
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Spec defines the desired identities of NBC diagnostics settings.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="instanceCount" /></td>
    <td><code>integer</code></td>
    <td>To manually scale the dataflow profile, specify the maximum number of instances you want to run.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status for the dataflow profile.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_profile_name"><code>dataflow_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DataflowProfileResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DataflowProfileResource resources by InstanceResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_profile_name"><code>dataflow_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a DataflowProfileResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_profile_name"><code>dataflow_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a DataflowProfileResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_profile_name"><code>dataflow_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a DataflowProfileResource.</td>
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
<tr id="parameter-dataflow_profile_name">
    <td><CopyableCode code="dataflow_profile_name" /></td>
    <td><code>string</code></td>
    <td>Name of Instance dataflowProfile resource. Required.</td>
</tr>
<tr id="parameter-instance_name">
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of instance. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
    ]}
>
<TabItem value="get">

Get a DataflowProfileResource.

```sql
SELECT
id,
name,
diagnostics,
extendedLocation,
healthState,
instanceCount,
provisioningState,
status,
systemData,
type
FROM azure.iot_operations.dataflow_profile
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
AND dataflow_profile_name = '{{ dataflow_profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List DataflowProfileResource resources by InstanceResource.

```sql
SELECT
id,
name,
diagnostics,
extendedLocation,
healthState,
instanceCount,
provisioningState,
status,
systemData,
type
FROM azure.iot_operations.dataflow_profile
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
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

Create a DataflowProfileResource.

```sql
INSERT INTO azure.iot_operations.dataflow_profile (
properties,
extendedLocation,
resource_group_name,
instance_name,
dataflow_profile_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ instance_name }}',
'{{ dataflow_profile_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: dataflow_profile
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dataflow_profile resource.
    - name: instance_name
      value: "{{ instance_name }}"
      description: Required parameter for the dataflow_profile resource.
    - name: dataflow_profile_name
      value: "{{ dataflow_profile_name }}"
      description: Required parameter for the dataflow_profile resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dataflow_profile resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        diagnostics:
          logs:
            level: "{{ level }}"
          metrics:
            prometheusPort: {{ prometheusPort }}
        instanceCount: {{ instanceCount }}
        provisioningState: "{{ provisioningState }}"
        status:
          healthState:
            status: "{{ status }}"
            lastTransitionTime: "{{ lastTransitionTime }}"
            lastUpdateTime: "{{ lastUpdateTime }}"
            message: "{{ message }}"
            reasonCode: "{{ reasonCode }}"
        healthState: "{{ healthState }}"
    - name: extendedLocation
      description: |
        Edge location of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Create a DataflowProfileResource.

```sql
REPLACE azure.iot_operations.dataflow_profile
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND dataflow_profile_name = '{{ dataflow_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
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

Delete a DataflowProfileResource.

```sql
DELETE FROM azure.iot_operations.dataflow_profile
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND dataflow_profile_name = '{{ dataflow_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
