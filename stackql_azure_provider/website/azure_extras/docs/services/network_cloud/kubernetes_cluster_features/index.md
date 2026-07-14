--- 
title: kubernetes_cluster_features
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_cluster_features
  - network_cloud
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

Creates, updates, deletes, gets or lists a <code>kubernetes_cluster_features</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kubernetes_cluster_features" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.network_cloud.kubernetes_cluster_features" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_kubernetes_cluster', value: 'list_by_kubernetes_cluster' }
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
    <td><CopyableCode code="availabilityLifecycle" /></td>
    <td><code>string</code></td>
    <td>The lifecycle indicator of the feature. Known values are: "Preview" and "GenerallyAvailable". (Preview, GenerallyAvailable)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status of the feature. Known values are: "Error", "Provisioning", and "Installed". (Error, Provisioning, Installed)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message for the detailed status of the feature.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>array</code></td>
    <td>The configured options for the feature.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Kubernetes cluster feature. Known values are: "Accepted", "Canceled", "Deleting", "Failed", "Succeeded", and "Updating". (Accepted, Canceled, Deleting, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="required" /></td>
    <td><code>string</code></td>
    <td>The indicator of if the feature is required or optional. Optional features may be deleted by the user, while required features are managed with the kubernetes cluster lifecycle. Known values are: "True" and "False". (True, False)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the feature.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_kubernetes_cluster">

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
    <td><CopyableCode code="availabilityLifecycle" /></td>
    <td><code>string</code></td>
    <td>The lifecycle indicator of the feature. Known values are: "Preview" and "GenerallyAvailable". (Preview, GenerallyAvailable)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status of the feature. Known values are: "Error", "Provisioning", and "Installed". (Error, Provisioning, Installed)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message for the detailed status of the feature.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>array</code></td>
    <td>The configured options for the feature.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Kubernetes cluster feature. Known values are: "Accepted", "Canceled", "Deleting", "Failed", "Succeeded", and "Updating". (Accepted, Canceled, Deleting, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="required" /></td>
    <td><code>string</code></td>
    <td>The indicator of if the feature is required or optional. Optional features may be deleted by the user, while required features are managed with the kubernetes cluster lifecycle. Known values are: "True" and "False". (True, False)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the feature.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided the Kubernetes cluster feature.</td>
</tr>
<tr>
    <td><a href="#list_by_kubernetes_cluster"><CopyableCode code="list_by_kubernetes_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of features for the provided Kubernetes cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a new Kubernetes cluster feature or update properties of the Kubernetes cluster feature if it exists.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch properties of the provided Kubernetes cluster feature.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a new Kubernetes cluster feature or update properties of the Kubernetes cluster feature if it exists.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided Kubernetes cluster feature.</td>
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
<tr id="parameter-feature_name">
    <td><CopyableCode code="feature_name" /></td>
    <td><code>string</code></td>
    <td>The name of the feature. Required.</td>
</tr>
<tr id="parameter-kubernetes_cluster_name">
    <td><CopyableCode code="kubernetes_cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Kubernetes cluster. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The opaque token that the server returns to indicate where to continue listing resources from. This is used for paging through large result sets. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_kubernetes_cluster', value: 'list_by_kubernetes_cluster' }
    ]}
>
<TabItem value="get">

Get properties of the provided the Kubernetes cluster feature.

```sql
SELECT
id,
name,
availabilityLifecycle,
detailedStatus,
detailedStatusMessage,
etag,
location,
options,
provisioningState,
required,
systemData,
tags,
type,
version
FROM azure_extras.network_cloud.kubernetes_cluster_features
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' -- required
AND feature_name = '{{ feature_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_kubernetes_cluster">

Get a list of features for the provided Kubernetes cluster.

```sql
SELECT
id,
name,
availabilityLifecycle,
detailedStatus,
detailedStatusMessage,
etag,
location,
options,
provisioningState,
required,
systemData,
tags,
type,
version
FROM azure_extras.network_cloud.kubernetes_cluster_features
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a new Kubernetes cluster feature or update properties of the Kubernetes cluster feature if it exists.

```sql
INSERT INTO azure_extras.network_cloud.kubernetes_cluster_features (
tags,
location,
properties,
resource_group_name,
kubernetes_cluster_name,
feature_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ kubernetes_cluster_name }}',
'{{ feature_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: kubernetes_cluster_features
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the kubernetes_cluster_features resource.
    - name: kubernetes_cluster_name
      value: "{{ kubernetes_cluster_name }}"
      description: Required parameter for the kubernetes_cluster_features resource.
    - name: feature_name
      value: "{{ feature_name }}"
      description: Required parameter for the kubernetes_cluster_features resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the kubernetes_cluster_features resource.
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
        The list of the resource properties.
      value:
        options:
          - key: "{{ key }}"
            value: "{{ value }}"
        availabilityLifecycle: "{{ availabilityLifecycle }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        required: "{{ required }}"
        version: "{{ version }}"
        provisioningState: "{{ provisioningState }}"
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

Patch properties of the provided Kubernetes cluster feature.

```sql
UPDATE azure_extras.network_cloud.kubernetes_cluster_features
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND feature_name = '{{ feature_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
systemData,
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

Create a new Kubernetes cluster feature or update properties of the Kubernetes cluster feature if it exists.

```sql
REPLACE azure_extras.network_cloud.kubernetes_cluster_features
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND feature_name = '{{ feature_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
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

Delete the provided Kubernetes cluster feature.

```sql
DELETE FROM azure_extras.network_cloud.kubernetes_cluster_features
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND feature_name = '{{ feature_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
