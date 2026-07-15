--- 
title: kubernetes_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_versions
  - hybrid_container_service
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

Creates, updates, deletes, gets or lists a <code>kubernetes_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kubernetes_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_container_service.kubernetes_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location pointing to the underlying infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Deleting", "Updating", "Upgrading", and "Accepted".</td>
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
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>List of supported Kubernetes versions.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-custom_location_resource_uri"><code>custom_location_resource_uri</code></a></td>
    <td></td>
    <td>Lists the supported kubernetes versions. Lists the supported kubernetes versions for the specified custom location.</td>
</tr>
<tr>
    <td><a href="#delete_kubernetes_versions"><CopyableCode code="delete_kubernetes_versions" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_location_resource_uri"><code>custom_location_resource_uri</code></a></td>
    <td></td>
    <td>Deletes the default kubernetes version resource type. Delete the default kubernetes versions resource type.</td>
</tr>
<tr>
    <td><a href="#get_kubernetes_versions"><CopyableCode code="get_kubernetes_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-custom_location_resource_uri"><code>custom_location_resource_uri</code></a></td>
    <td></td>
    <td>Lists the supported kubernetes versions. Lists the supported kubernetes versions for the specified custom location.</td>
</tr>
<tr>
    <td><a href="#put_kubernetes_versions"><CopyableCode code="put_kubernetes_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-custom_location_resource_uri"><code>custom_location_resource_uri</code></a></td>
    <td></td>
    <td>Puts the default kubernetes version resource type (one time operation, before listing the kubernetes versions). Puts the default kubernetes version resource type (one time operation, before listing the kubernetes versions).</td>
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
<tr id="parameter-custom_location_resource_uri">
    <td><CopyableCode code="custom_location_resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource Manager identifier of the custom location resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists the supported kubernetes versions. Lists the supported kubernetes versions for the specified custom location.

```sql
SELECT
id,
name,
extendedLocation,
provisioningState,
systemData,
type,
values
FROM azure.hybrid_container_service.kubernetes_versions
WHERE custom_location_resource_uri = '{{ custom_location_resource_uri }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_kubernetes_versions"
    values={[
        { label: 'delete_kubernetes_versions', value: 'delete_kubernetes_versions' }
    ]}
>
<TabItem value="delete_kubernetes_versions">

Deletes the default kubernetes version resource type. Delete the default kubernetes versions resource type.

```sql
DELETE FROM azure.hybrid_container_service.kubernetes_versions
WHERE custom_location_resource_uri = '{{ custom_location_resource_uri }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_kubernetes_versions"
    values={[
        { label: 'get_kubernetes_versions', value: 'get_kubernetes_versions' },
        { label: 'put_kubernetes_versions', value: 'put_kubernetes_versions' }
    ]}
>
<TabItem value="get_kubernetes_versions">

Lists the supported kubernetes versions. Lists the supported kubernetes versions for the specified custom location.

```sql
EXEC azure.hybrid_container_service.kubernetes_versions.get_kubernetes_versions 
@custom_location_resource_uri='{{ custom_location_resource_uri }}' --required
;
```
</TabItem>
<TabItem value="put_kubernetes_versions">

Puts the default kubernetes version resource type (one time operation, before listing the kubernetes versions). Puts the default kubernetes version resource type (one time operation, before listing the kubernetes versions).

```sql
EXEC azure.hybrid_container_service.kubernetes_versions.put_kubernetes_versions 
@custom_location_resource_uri='{{ custom_location_resource_uri }}' --required 
@@json=
'{
"extendedLocation": "{{ extendedLocation }}"
}'
;
```
</TabItem>
</Tabs>
