--- 
title: dedicated_cloud_services
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_services
  - vmware_cloud_simple
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>dedicated_cloud_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dedicated_cloud_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.dedicated_cloud_services" /></td></tr>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudServices/&#123;dedicatedCloudServiceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;dedicatedCloudServiceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewaySubnet" /></td>
    <td><code>string</code></td>
    <td>gateway Subnet for the account. It will collect the subnet address and always treat it as /28.</td>
</tr>
<tr>
    <td><CopyableCode code="isAccountOnboarded" /></td>
    <td><code>string</code></td>
    <td>indicates whether account onboarded or not in a given region. Known values are: "notOnBoarded", "onBoarded", "onBoardingFailed", and "onBoarding".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodes" /></td>
    <td><code>integer</code></td>
    <td>total nodes purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceURL" /></td>
    <td><code>string</code></td>
    <td>link to a service management web portal.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudServices/&#123;dedicatedCloudServiceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;dedicatedCloudServiceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewaySubnet" /></td>
    <td><code>string</code></td>
    <td>gateway Subnet for the account. It will collect the subnet address and always treat it as /28.</td>
</tr>
<tr>
    <td><CopyableCode code="isAccountOnboarded" /></td>
    <td><code>string</code></td>
    <td>indicates whether account onboarded or not in a given region. Known values are: "notOnBoarded", "onBoarded", "onBoardingFailed", and "onBoarding".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodes" /></td>
    <td><code>integer</code></td>
    <td>total nodes purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceURL" /></td>
    <td><code>string</code></td>
    <td>link to a service management web portal.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudServices/&#123;dedicatedCloudServiceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;dedicatedCloudServiceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewaySubnet" /></td>
    <td><code>string</code></td>
    <td>gateway Subnet for the account. It will collect the subnet address and always treat it as /28.</td>
</tr>
<tr>
    <td><CopyableCode code="isAccountOnboarded" /></td>
    <td><code>string</code></td>
    <td>indicates whether account onboarded or not in a given region. Known values are: "notOnBoarded", "onBoarded", "onBoardingFailed", and "onBoarding".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodes" /></td>
    <td><code>integer</code></td>
    <td>total nodes purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceURL" /></td>
    <td><code>string</code></td>
    <td>link to a service management web portal.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_service_name"><code>dedicated_cloud_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements dedicatedCloudService GET method. Returns Dedicate Cloud Service.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Implements list of dedicatedCloudService objects within RG method. Returns list of dedicated cloud services within a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Implements list of dedicatedCloudService objects within subscription method. Returns list of dedicated cloud services within a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_service_name"><code>dedicated_cloud_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements dedicated cloud service PUT method. Create dedicate cloud service.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_service_name"><code>dedicated_cloud_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements dedicatedCloudService PATCH method. Patch dedicated cloud service's properties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_service_name"><code>dedicated_cloud_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements dedicated cloud service PUT method. Create dedicate cloud service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_service_name"><code>dedicated_cloud_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements dedicatedCloudService DELETE method. Delete dedicate cloud service.</td>
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
<tr id="parameter-dedicated_cloud_service_name">
    <td><CopyableCode code="dedicated_cloud_service_name" /></td>
    <td><code>string</code></td>
    <td>dedicated cloud service name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the list operation. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>to be used by nextLink implementation. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of record sets to return. Default value is None.</td>
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

Implements dedicatedCloudService GET method. Returns Dedicate Cloud Service.

```sql
SELECT
id,
name,
gatewaySubnet,
isAccountOnboarded,
location,
nodes,
serviceURL,
tags,
type
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dedicated_cloud_service_name = '{{ dedicated_cloud_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Implements list of dedicatedCloudService objects within RG method. Returns list of dedicated cloud services within a resource group.

```sql
SELECT
id,
name,
gatewaySubnet,
isAccountOnboarded,
location,
nodes,
serviceURL,
tags,
type
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Implements list of dedicatedCloudService objects within subscription method. Returns list of dedicated cloud services within a subscription.

```sql
SELECT
id,
name,
gatewaySubnet,
isAccountOnboarded,
location,
nodes,
serviceURL,
tags,
type
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_services
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Implements dedicated cloud service PUT method. Create dedicate cloud service.

```sql
INSERT INTO azure_isv.vmware_cloud_simple.dedicated_cloud_services (
location,
tags,
properties,
resource_group_name,
dedicated_cloud_service_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ dedicated_cloud_service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: dedicated_cloud_services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dedicated_cloud_services resource.
    - name: dedicated_cloud_service_name
      value: "{{ dedicated_cloud_service_name }}"
      description: Required parameter for the dedicated_cloud_services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dedicated_cloud_services resource.
    - name: location
      value: "{{ location }}"
      description: |
        Azure region. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        The list of tags.
    - name: properties
      value:
        gatewaySubnet: "{{ gatewaySubnet }}"
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

Implements dedicatedCloudService PATCH method. Patch dedicated cloud service's properties.

```sql
UPDATE azure_isv.vmware_cloud_simple.dedicated_cloud_services
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_cloud_service_name = '{{ dedicated_cloud_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
tags,
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

Implements dedicated cloud service PUT method. Create dedicate cloud service.

```sql
REPLACE azure_isv.vmware_cloud_simple.dedicated_cloud_services
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_cloud_service_name = '{{ dedicated_cloud_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
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

Implements dedicatedCloudService DELETE method. Delete dedicate cloud service.

```sql
DELETE FROM azure_isv.vmware_cloud_simple.dedicated_cloud_services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_cloud_service_name = '{{ dedicated_cloud_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
