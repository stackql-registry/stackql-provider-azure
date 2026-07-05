--- 
title: quota
hide_title: false
hide_table_of_contents: false
keywords:
  - quota
  - quota
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.quota" /></td></tr>
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
    <td><CopyableCode code="isQuotaApplicable" /></td>
    <td><code>boolean</code></td>
    <td>States if quota can be requested for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="limit" /></td>
    <td><code>object</code></td>
    <td>Resource quota limit properties.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the specific resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaPeriod" /></td>
    <td><code>string</code></td>
    <td>The time period over which the quota usage values are summarized. For example: *P1D (per one day) *PT1M (per one minute) *PT1S (per one second). This parameter is optional because, for some resources like compute, the period is irrelevant.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The name of the resource type. Optional field.</td>
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
    <td>The quota units, such as Count and Bytes. When requesting quota, use the **unit** value returned in the GET response in the request body of your PUT operation.</td>
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
    <td><CopyableCode code="isQuotaApplicable" /></td>
    <td><code>boolean</code></td>
    <td>States if quota can be requested for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="limit" /></td>
    <td><code>object</code></td>
    <td>Resource quota limit properties.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the specific resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaPeriod" /></td>
    <td><code>string</code></td>
    <td>The time period over which the quota usage values are summarized. For example: *P1D (per one day) *PT1M (per one minute) *PT1S (per one second). This parameter is optional because, for some resources like compute, the period is irrelevant.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The name of the resource type. Optional field.</td>
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
    <td>The quota units, such as Count and Bytes. When requesting quota, use the **unit** value returned in the GET response in the request body of your PUT operation.</td>
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
    <td><a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get the quota limit of a resource. The response can be used to determine the remaining quota to calculate a new quota limit that can be submitted with a PUT request.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get a list of current quota limits of all resources for the specified scope. The response from this GET operation can be leveraged to submit requests to update a quota.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Create or update the quota limit for the specified resource with the requested value. To update the quota, follow these steps: 1. Use the GET operation for quotas and usages to determine how much quota remains for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670). 2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Update the quota limit for a specific resource to the specified value: 1. Use the Usages-GET and Quota-GET operations to determine the remaining quota for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670). 2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Create or update the quota limit for the specified resource with the requested value. To update the quota, follow these steps: 1. Use the GET operation for quotas and usages to determine how much quota remains for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670). 2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request.</td>
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
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Resource name for a given resource provider. For example: * SKU name for Microsoft.Compute * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices For Microsoft.Network PublicIPAddresses. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
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

Get the quota limit of a resource. The response can be used to determine the remaining quota to calculate a new quota limit that can be submitted with a PUT request.

```sql
SELECT
id,
name,
isQuotaApplicable,
limit,
properties,
quotaPeriod,
resourceType,
systemData,
type,
unit
FROM azure.quota.quota
WHERE resource_name = '{{ resource_name }}' -- required
AND scope = '{{ scope }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of current quota limits of all resources for the specified scope. The response from this GET operation can be leveraged to submit requests to update a quota.

```sql
SELECT
id,
name,
isQuotaApplicable,
limit,
properties,
quotaPeriod,
resourceType,
systemData,
type,
unit
FROM azure.quota.quota
WHERE scope = '{{ scope }}' -- required
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

Create or update the quota limit for the specified resource with the requested value. To update the quota, follow these steps: 1. Use the GET operation for quotas and usages to determine how much quota remains for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670). 2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request.

```sql
INSERT INTO azure.quota.quota (
properties,
resource_name,
scope
)
SELECT 
'{{ properties }}',
'{{ resource_name }}',
'{{ scope }}'
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
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the quota resource.
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the quota resource.
    - name: properties
      description: |
        Quota properties for the specified resource, based on the API called, Quotas or Usages.
      value:
        limit:
          limitObjectType: "{{ limitObjectType }}"
        unit: "{{ unit }}"
        name:
          value: "{{ value }}"
          localizedValue: "{{ localizedValue }}"
        resourceType: "{{ resourceType }}"
        quotaPeriod: "{{ quotaPeriod }}"
        isQuotaApplicable: {{ isQuotaApplicable }}
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

Update the quota limit for a specific resource to the specified value: 1. Use the Usages-GET and Quota-GET operations to determine the remaining quota for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670). 2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request.

```sql
UPDATE azure.quota.quota
SET 
properties = '{{ properties }}'
WHERE 
resource_name = '{{ resource_name }}' --required
AND scope = '{{ scope }}' --required
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

Create or update the quota limit for the specified resource with the requested value. To update the quota, follow these steps: 1. Use the GET operation for quotas and usages to determine how much quota remains for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670). 2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request.

```sql
REPLACE azure.quota.quota
SET 
properties = '{{ properties }}'
WHERE 
resource_name = '{{ resource_name }}' --required
AND scope = '{{ scope }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
