--- 
title: application_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - application_groups
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists an <code>application_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.application_groups" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGroupType" /></td>
    <td><code>string</code></td>
    <td>Resource Type of ApplicationGroup. Required. Known values are: "RemoteApp" and "Desktop".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudPcResource" /></td>
    <td><code>boolean</code></td>
    <td>Is cloud pc resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of ApplicationGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of ApplicationGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPoolArmPath" /></td>
    <td><code>string</code></td>
    <td>HostPool arm path of ApplicationGroup. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of ApplicationGroup. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>:vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan</td>
</tr>
<tr>
    <td><CopyableCode code="showInFeed" /></td>
    <td><code>boolean</code></td>
    <td>Boolean representing whether the applicationGroup is show in the feed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku</td>
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
    <td><CopyableCode code="workspaceArmPath" /></td>
    <td><code>string</code></td>
    <td>Workspace arm path of ApplicationGroup.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGroupType" /></td>
    <td><code>string</code></td>
    <td>Resource Type of ApplicationGroup. Required. Known values are: "RemoteApp" and "Desktop".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudPcResource" /></td>
    <td><code>boolean</code></td>
    <td>Is cloud pc resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of ApplicationGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of ApplicationGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPoolArmPath" /></td>
    <td><code>string</code></td>
    <td>HostPool arm path of ApplicationGroup. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of ApplicationGroup. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>:vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan</td>
</tr>
<tr>
    <td><CopyableCode code="showInFeed" /></td>
    <td><code>boolean</code></td>
    <td>Boolean representing whether the applicationGroup is show in the feed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku</td>
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
    <td><CopyableCode code="workspaceArmPath" /></td>
    <td><code>string</code></td>
    <td>Workspace arm path of ApplicationGroup.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGroupType" /></td>
    <td><code>string</code></td>
    <td>Resource Type of ApplicationGroup. Required. Known values are: "RemoteApp" and "Desktop".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudPcResource" /></td>
    <td><code>boolean</code></td>
    <td>Is cloud pc resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of ApplicationGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of ApplicationGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPoolArmPath" /></td>
    <td><code>string</code></td>
    <td>HostPool arm path of ApplicationGroup. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of ApplicationGroup. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>:vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan</td>
</tr>
<tr>
    <td><CopyableCode code="showInFeed" /></td>
    <td><code>boolean</code></td>
    <td>Boolean representing whether the applicationGroup is show in the feed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku</td>
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
    <td><CopyableCode code="workspaceArmPath" /></td>
    <td><code>string</code></td>
    <td>Workspace arm path of ApplicationGroup.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an application group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List applicationGroups.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>List applicationGroups in subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an applicationGroup.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an applicationGroup.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an applicationGroup.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_group_name"><code>application_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove an applicationGroup.</td>
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
<tr id="parameter-application_group_name">
    <td><CopyableCode code="application_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application group. Required.</td>
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
    <td>OData filter expression. Valid properties for filtering are applicationGroupType. Default value is None.</td>
</tr>
<tr id="parameter-initialSkip">
    <td><CopyableCode code="initialSkip" /></td>
    <td><code>integer</code></td>
    <td>Initial number of items to skip. Default value is None.</td>
</tr>
<tr id="parameter-isDescending">
    <td><CopyableCode code="isDescending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the collection is descending. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Number of items per page. Default value is None.</td>
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

Get an application group.

```sql
SELECT
id,
name,
applicationGroupType,
cloudPcResource,
description,
etag,
friendlyName,
hostPoolArmPath,
identity,
kind,
location,
managedBy,
objectId,
plan,
showInFeed,
sku,
systemData,
tags,
type,
workspaceArmPath
FROM azure.desktop_virtualization.application_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND application_group_name = '{{ application_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List applicationGroups.

```sql
SELECT
id,
name,
applicationGroupType,
cloudPcResource,
description,
etag,
friendlyName,
hostPoolArmPath,
identity,
kind,
location,
managedBy,
objectId,
plan,
showInFeed,
sku,
systemData,
tags,
type,
workspaceArmPath
FROM azure.desktop_virtualization.application_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

List applicationGroups in subscription.

```sql
SELECT
id,
name,
applicationGroupType,
cloudPcResource,
description,
etag,
friendlyName,
hostPoolArmPath,
identity,
kind,
location,
managedBy,
objectId,
plan,
showInFeed,
sku,
systemData,
tags,
type,
workspaceArmPath
FROM azure.desktop_virtualization.application_groups
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Create or update an applicationGroup.

```sql
INSERT INTO azure.desktop_virtualization.application_groups (
tags,
location,
managedBy,
kind,
identity,
sku,
plan,
properties,
resource_group_name,
application_group_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ managedBy }}',
'{{ kind }}',
'{{ identity }}',
'{{ sku }}',
'{{ plan }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ application_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
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
- name: application_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the application_groups resource.
    - name: application_group_name
      value: "{{ application_group_name }}"
      description: Required parameter for the application_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the application_groups resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
    - name: identity
      description: |
        :vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: sku
      description: |
        :vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: plan
      description: |
        :vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
    - name: properties
      value:
        description: "{{ description }}"
        friendlyName: "{{ friendlyName }}"
        hostPoolArmPath: "{{ hostPoolArmPath }}"
        applicationGroupType: "{{ applicationGroupType }}"
        showInFeed: {{ showInFeed }}
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

Update an applicationGroup.

```sql
UPDATE azure.desktop_virtualization.application_groups
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_group_name = '{{ application_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
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

Create or update an applicationGroup.

```sql
REPLACE azure.desktop_virtualization.application_groups
SET 
tags = '{{ tags }}',
location = '{{ location }}',
managedBy = '{{ managedBy }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_group_name = '{{ application_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
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

Remove an applicationGroup.

```sql
DELETE FROM azure.desktop_virtualization.application_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND application_group_name = '{{ application_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
