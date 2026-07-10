--- 
title: capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities
  - powerbidedicated
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

Creates, updates, deletes, gets or lists a <code>capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="capacities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbidedicated.capacities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_skus_for_capacity"
    values={[
        { label: 'list_skus_for_capacity', value: 'list_skus_for_capacity' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_skus_for_capacity">

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
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>The collection of available SKUs for existing resources.</td>
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
    <td>An identifier that represents the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administration" /></td>
    <td><code>object</code></td>
    <td>A collection of Dedicated capacity administrators.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Capacity name.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the PowerBI Dedicated resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Specifies the generation of the Power BI Embedded capacity. If no value is specified, the default value 'Gen2' is used. `Learn More `_. Known values are: "Gen1" and "Gen2".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of PowerBI Dedicated resource. The provisioningState is to indicate states for resource provisioning. Known values are: "Deleting", "Succeeded", "Failed", "Paused", "Suspended", "Provisioning", "Updating", "Suspending", "Pausing", "Resuming", "Preparing", and "Scaling".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the PowerBI Dedicated capacity resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of PowerBI Dedicated resource. The state is to indicate more states outside of resource provisioning. Known values are: "Deleting", "Succeeded", "Failed", "Paused", "Suspended", "Provisioning", "Updating", "Suspending", "Pausing", "Resuming", "Preparing", and "Scaling".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs of additional resource provisioning properties.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the capacity. Used for creating Pro Plus capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the PowerBI Dedicated resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>The detailed message of the request unavailability.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Indicator of availability of the capacity name.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason of unavailability.</td>
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
    <td>An identifier that represents the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administration" /></td>
    <td><code>object</code></td>
    <td>A collection of Dedicated capacity administrators.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Capacity name.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the PowerBI Dedicated resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Specifies the generation of the Power BI Embedded capacity. If no value is specified, the default value 'Gen2' is used. `Learn More `_. Known values are: "Gen1" and "Gen2".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of PowerBI Dedicated resource. The provisioningState is to indicate states for resource provisioning. Known values are: "Deleting", "Succeeded", "Failed", "Paused", "Suspended", "Provisioning", "Updating", "Suspending", "Pausing", "Resuming", "Preparing", and "Scaling".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the PowerBI Dedicated capacity resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of PowerBI Dedicated resource. The state is to indicate more states outside of resource provisioning. Known values are: "Deleting", "Succeeded", "Failed", "Paused", "Suspended", "Provisioning", "Updating", "Suspending", "Pausing", "Resuming", "Preparing", and "Scaling".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs of additional resource provisioning properties.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the capacity. Used for creating Pro Plus capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the PowerBI Dedicated resource.</td>
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
    <td><a href="#list_skus_for_capacity"><CopyableCode code="list_skus_for_capacity" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_capacity_name"><code>dedicated_capacity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists eligible SKUs for a PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the Dedicated capacities for the given resource group.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check the name availability in the target location.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the Dedicated capacities for the given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_capacity_name"><code>dedicated_capacity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Provisions the specified Dedicated capacity based on the configuration specified in the request.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_capacity_name"><code>dedicated_capacity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the current state of the specified Dedicated capacity.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_capacity_name"><code>dedicated_capacity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Dedicated capacity.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists eligible SKUs for PowerBI Dedicated resource provider.</td>
</tr>
<tr>
    <td><a href="#get_details"><CopyableCode code="get_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_capacity_name"><code>dedicated_capacity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details about the specified dedicated capacity.</td>
</tr>
<tr>
    <td><a href="#suspend"><CopyableCode code="suspend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_capacity_name"><code>dedicated_capacity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Suspends operation of the specified dedicated capacity instance.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_capacity_name"><code>dedicated_capacity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resumes operation of the specified Dedicated capacity instance.</td>
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
<tr id="parameter-dedicated_capacity_name">
    <td><CopyableCode code="dedicated_capacity_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The region name which the operation will lookup into. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. Required.</td>
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
    defaultValue="list_skus_for_capacity"
    values={[
        { label: 'list_skus_for_capacity', value: 'list_skus_for_capacity' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_skus_for_capacity">

Lists eligible SKUs for a PowerBI Dedicated resource.

```sql
SELECT
value
FROM azure.powerbidedicated.capacities
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dedicated_capacity_name = '{{ dedicated_capacity_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all the Dedicated capacities for the given resource group.

```sql
SELECT
id,
name,
administration,
friendlyName,
location,
mode,
provisioningState,
sku,
state,
systemData,
tags,
tenantId,
type
FROM azure.powerbidedicated.capacities
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Check the name availability in the target location.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.powerbidedicated.capacities
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the Dedicated capacities for the given subscription.

```sql
SELECT
id,
name,
administration,
friendlyName,
location,
mode,
provisioningState,
sku,
state,
systemData,
tags,
tenantId,
type
FROM azure.powerbidedicated.capacities
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

Provisions the specified Dedicated capacity based on the configuration specified in the request.

```sql
INSERT INTO azure.powerbidedicated.capacities (
location,
tags,
systemData,
sku,
properties,
resource_group_name,
dedicated_capacity_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ systemData }}',
'{{ sku }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ dedicated_capacity_name }}',
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
- name: capacities
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the capacities resource.
    - name: dedicated_capacity_name
      value: "{{ dedicated_capacity_name }}"
      description: Required parameter for the capacities resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the capacities resource.
    - name: location
      value: "{{ location }}"
      description: |
        Location of the PowerBI Dedicated resource. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Key-value pairs of additional resource provisioning properties.
    - name: systemData
      description: |
        Metadata pertaining to creation and last modification of the resource.
      value:
        createdBy: "{{ createdBy }}"
        createdByType: "{{ createdByType }}"
        createdAt: "{{ createdAt }}"
        lastModifiedBy: "{{ lastModifiedBy }}"
        lastModifiedByType: "{{ lastModifiedByType }}"
        lastModifiedAt: "{{ lastModifiedAt }}"
    - name: sku
      description: |
        Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. All required parameters must be populated in order to send to server.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: properties
      value:
        administration:
          members:
            - "{{ members }}"
        mode: "{{ mode }}"
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

Updates the current state of the specified Dedicated capacity.

```sql
UPDATE azure.powerbidedicated.capacities
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_capacity_name = '{{ dedicated_capacity_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the specified Dedicated capacity.

```sql
DELETE FROM azure.powerbidedicated.capacities
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_capacity_name = '{{ dedicated_capacity_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_skus"
    values={[
        { label: 'list_skus', value: 'list_skus' },
        { label: 'get_details', value: 'get_details' },
        { label: 'suspend', value: 'suspend' },
        { label: 'resume', value: 'resume' }
    ]}
>
<TabItem value="list_skus">

Lists eligible SKUs for PowerBI Dedicated resource provider.

```sql
EXEC azure.powerbidedicated.capacities.list_skus 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_details">

Gets details about the specified dedicated capacity.

```sql
EXEC azure.powerbidedicated.capacities.get_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@dedicated_capacity_name='{{ dedicated_capacity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="suspend">

Suspends operation of the specified dedicated capacity instance.

```sql
EXEC azure.powerbidedicated.capacities.suspend 
@resource_group_name='{{ resource_group_name }}' --required, 
@dedicated_capacity_name='{{ dedicated_capacity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resumes operation of the specified Dedicated capacity instance.

```sql
EXEC azure.powerbidedicated.capacities.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@dedicated_capacity_name='{{ dedicated_capacity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
