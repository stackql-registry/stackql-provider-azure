--- 
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - sphere
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.sphere.deployments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_device_group', value: 'list_by_device_group' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deployedImages" /></td>
    <td><code>array</code></td>
    <td>Images deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentDateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Deployment date UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>Deployment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
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
<TabItem value="list_by_device_group">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deployedImages" /></td>
    <td><code>array</code></td>
    <td>Images deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentDateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Deployment date UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>Deployment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#list_by_device_group"><CopyableCode code="list_by_device_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$maxpagesize"><code>$maxpagesize</code></a></td>
    <td>List Deployment resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-device_group_name"><code>device_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>Name of catalog. Required.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>Deployment name. Use .default for deployment creation and to get the current deployment for the associated device group. Required.</td>
</tr>
<tr id="parameter-device_group_name">
    <td><CopyableCode code="device_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of device group. Required.</td>
</tr>
<tr id="parameter-product_name">
    <td><CopyableCode code="product_name" /></td>
    <td><code>string</code></td>
    <td>Name of product. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter the result list using the given expression. Default value is None.</td>
</tr>
<tr id="parameter-$maxpagesize">
    <td><CopyableCode code="$maxpagesize" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of result items per page. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_device_group', value: 'list_by_device_group' }
    ]}
>
<TabItem value="get">

Get a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
SELECT
id,
name,
deployedImages,
deploymentDateUtc,
deploymentId,
provisioningState,
systemData,
type
FROM azure_extras.sphere.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND product_name = '{{ product_name }}' -- required
AND device_group_name = '{{ device_group_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_device_group">

List Deployment resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
SELECT
id,
name,
deployedImages,
deploymentDateUtc,
deploymentId,
provisioningState,
systemData,
type
FROM azure_extras.sphere.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND product_name = '{{ product_name }}' -- required
AND device_group_name = '{{ device_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $maxpagesize = '{{ $maxpagesize }}'
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

Create a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
INSERT INTO azure_extras.sphere.deployments (
properties,
resource_group_name,
catalog_name,
product_name,
device_group_name,
deployment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ catalog_name }}',
'{{ product_name }}',
'{{ device_group_name }}',
'{{ deployment_name }}',
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
- name: deployments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the deployments resource.
    - name: catalog_name
      value: "{{ catalog_name }}"
      description: Required parameter for the deployments resource.
    - name: product_name
      value: "{{ product_name }}"
      description: Required parameter for the deployments resource.
    - name: device_group_name
      value: "{{ device_group_name }}"
      description: Required parameter for the deployments resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the deployments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the deployments resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        deploymentId: "{{ deploymentId }}"
        deployedImages:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              image: "{{ image }}"
              imageId: "{{ imageId }}"
              imageName: "{{ imageName }}"
              regionalDataBoundary: "{{ regionalDataBoundary }}"
              uri: "{{ uri }}"
              description: "{{ description }}"
              componentId: "{{ componentId }}"
              imageType: "{{ imageType }}"
              provisioningState: "{{ provisioningState }}"
        deploymentDateUtc: "{{ deploymentDateUtc }}"
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

Create a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
REPLACE azure_extras.sphere.deployments
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
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

Delete a Deployment. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

```sql
DELETE FROM azure_extras.sphere.deployments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND product_name = '{{ product_name }}' --required
AND device_group_name = '{{ device_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
