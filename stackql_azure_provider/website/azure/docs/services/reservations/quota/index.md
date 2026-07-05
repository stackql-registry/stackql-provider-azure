--- 
title: quota
hide_title: false
hide_table_of_contents: false
keywords:
  - quota
  - reservations
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

Creates, updates, deletes, gets or lists a <code>quota</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="quota" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.quota" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="currentValue" /></td>
    <td><code>integer</code></td>
    <td>Current usage value for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Quota properties.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the specified resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaPeriod" /></td>
    <td><code>string</code></td>
    <td>The time period over which the quota usage values are summarized. For example, P1D (per one day), PT1M (per one minute), and PT1S (per one second). This parameter is optional because, for some resources such as compute, the time period is irrelevant.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The name of the resource type. Known values are: "standard", "dedicated", "lowPriority", "shared", and "serviceSpecific". (standard, dedicated, lowPriority, shared, serviceSpecific)</td>
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
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>The limit units, such as **count** and **bytes**. Use the unit field provided in the response of the GET quota operation.</td>
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
    <td><CopyableCode code="currentValue" /></td>
    <td><code>integer</code></td>
    <td>Current usage value for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Quota properties.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the specified resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaPeriod" /></td>
    <td><code>string</code></td>
    <td>The time period over which the quota usage values are summarized. For example, P1D (per one day), PT1M (per one minute), and PT1S (per one second). This parameter is optional because, for some resources such as compute, the time period is irrelevant.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The name of the resource type. Known values are: "standard", "dedicated", "lowPriority", "shared", and "serviceSpecific". (standard, dedicated, lowPriority, shared, serviceSpecific)</td>
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
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>The limit units, such as **count** and **bytes**. Use the unit field provided in the response of the GET quota operation.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a></td>
    <td></td>
    <td>Get the current quota (service limit) and usage of a resource. You can use the response from the GET operation to submit quota update request.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Gets a list of current quotas (service limits) and usage for all resources. The response from the list quota operation can be leveraged to request quota updates.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a></td>
    <td></td>
    <td>Create or update the quota (service limits) of a resource to the requested value. Steps: 1. Make the Get request to get the quota information for specific resource. 2. To increase the quota, update the limit field in the response from Get request to new value. 3. Submit the JSON to the quota request API to update the quota. The Create quota request may be constructed as follows. The PUT operation can be used to update the quota.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a></td>
    <td></td>
    <td>Update the quota (service limits) of this resource to the requested value. • To get the quota information for specific resource, send a GET request. • To increase the quota, update the limit field from the GET response to a new value. • To update the quota value, submit the JSON response to the quota request API to update the quota. • To update the quota. use the PATCH operation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a></td>
    <td></td>
    <td>Create or update the quota (service limits) of a resource to the requested value. Steps: 1. Make the Get request to get the quota information for specific resource. 2. To increase the quota, update the limit field in the response from Get request to new value. 3. Submit the JSON to the quota request API to update the quota. The Create quota request may be constructed as follows. The PUT operation can be used to update the quota.</td>
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
    <td>Azure region. Required.</td>
</tr>
<tr id="parameter-provider_id">
    <td><CopyableCode code="provider_id" /></td>
    <td><code>string</code></td>
    <td>Azure resource provider ID. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The resource name for a resource provider, such as SKU name for Microsoft.Compute, Sku or TotalLowPriorityCores for Microsoft.MachineLearningServices. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the target subscription. The value must be an UUID. Required.</td>
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

Get the current quota (service limit) and usage of a resource. You can use the response from the GET operation to submit quota update request.

```sql
SELECT
id,
name,
currentValue,
limit,
properties,
quotaPeriod,
resourceType,
systemData,
type,
unit
FROM azure.reservations.quota
WHERE subscription_id = '{{ subscription_id }}' -- required
AND provider_id = '{{ provider_id }}' -- required
AND location = '{{ location }}' -- required
AND resource_name = '{{ resource_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of current quotas (service limits) and usage for all resources. The response from the list quota operation can be leveraged to request quota updates.

```sql
SELECT
id,
name,
currentValue,
limit,
properties,
quotaPeriod,
resourceType,
systemData,
type,
unit
FROM azure.reservations.quota
WHERE subscription_id = '{{ subscription_id }}' -- required
AND provider_id = '{{ provider_id }}' -- required
AND location = '{{ location }}' -- required
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

Create or update the quota (service limits) of a resource to the requested value. Steps: 1. Make the Get request to get the quota information for specific resource. 2. To increase the quota, update the limit field in the response from Get request to new value. 3. Submit the JSON to the quota request API to update the quota. The Create quota request may be constructed as follows. The PUT operation can be used to update the quota.

```sql
INSERT INTO azure.reservations.quota (
properties,
subscription_id,
provider_id,
location,
resource_name
)
SELECT 
'{{ properties }}',
'{{ subscription_id }}',
'{{ provider_id }}',
'{{ location }}',
'{{ resource_name }}'
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
- name: quota
  props:
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the quota resource.
    - name: provider_id
      value: "{{ provider_id }}"
      description: Required parameter for the quota resource.
    - name: location
      value: "{{ location }}"
      description: Required parameter for the quota resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the quota resource.
    - name: properties
      description: |
        Quota properties for the resource.
      value:
        limit: {{ limit }}
        currentValue: {{ currentValue }}
        unit: "{{ unit }}"
        name:
          value: "{{ value }}"
          localizedValue: "{{ localizedValue }}"
        resourceType: "{{ resourceType }}"
        quotaPeriod: "{{ quotaPeriod }}"
        properties: "{{ properties }}"
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

Update the quota (service limits) of this resource to the requested value. • To get the quota information for specific resource, send a GET request. • To increase the quota, update the limit field from the GET response to a new value. • To update the quota value, submit the JSON response to the quota request API to update the quota. • To update the quota. use the PATCH operation.

```sql
UPDATE azure.reservations.quota
SET 
properties = '{{ properties }}'
WHERE 
subscription_id = '{{ subscription_id }}' --required
AND provider_id = '{{ provider_id }}' --required
AND location = '{{ location }}' --required
AND resource_name = '{{ resource_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
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

Create or update the quota (service limits) of a resource to the requested value. Steps: 1. Make the Get request to get the quota information for specific resource. 2. To increase the quota, update the limit field in the response from Get request to new value. 3. Submit the JSON to the quota request API to update the quota. The Create quota request may be constructed as follows. The PUT operation can be used to update the quota.

```sql
REPLACE azure.reservations.quota
SET 
properties = '{{ properties }}'
WHERE 
subscription_id = '{{ subscription_id }}' --required
AND provider_id = '{{ provider_id }}' --required
AND location = '{{ location }}' --required
AND resource_name = '{{ resource_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
