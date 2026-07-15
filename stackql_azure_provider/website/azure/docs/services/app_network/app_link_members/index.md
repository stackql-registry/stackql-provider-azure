--- 
title: app_link_members
hide_title: false
hide_table_of_contents: false
keywords:
  - app_link_members
  - app_network
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

Creates, updates, deletes, gets or lists an <code>app_link_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_link_members" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_network.app_link_members" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_app_link', value: 'list_by_app_link' }
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
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>Cluster type. "AKS" (AKS)</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityProfile" /></td>
    <td><code>object</code></td>
    <td>Connectivity profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>AppLink Member Metadata. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="observabilityProfile" /></td>
    <td><code>object</code></td>
    <td>Observability profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
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
    <td><CopyableCode code="upgradeProfile" /></td>
    <td><code>object</code></td>
    <td>Upgrade profile.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_app_link">

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
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>Cluster type. "AKS" (AKS)</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityProfile" /></td>
    <td><code>object</code></td>
    <td>Connectivity profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>AppLink Member Metadata. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="observabilityProfile" /></td>
    <td><code>object</code></td>
    <td>Observability profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
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
    <td><CopyableCode code="upgradeProfile" /></td>
    <td><code>object</code></td>
    <td>Upgrade profile.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-app_link_name"><code>app_link_name</code></a>, <a href="#parameter-app_link_member_name"><code>app_link_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an AppLinkMember.</td>
</tr>
<tr>
    <td><a href="#list_by_app_link"><CopyableCode code="list_by_app_link" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-app_link_name"><code>app_link_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AppLinkMember resources by AppLink.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-app_link_name"><code>app_link_name</code></a>, <a href="#parameter-app_link_member_name"><code>app_link_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create an AppLinkMember.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-app_link_name"><code>app_link_name</code></a>, <a href="#parameter-app_link_member_name"><code>app_link_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an AppLinkMember.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-app_link_name"><code>app_link_name</code></a>, <a href="#parameter-app_link_member_name"><code>app_link_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create an AppLinkMember.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-app_link_name"><code>app_link_name</code></a>, <a href="#parameter-app_link_member_name"><code>app_link_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an AppLinkMember.</td>
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
<tr id="parameter-app_link_member_name">
    <td><CopyableCode code="app_link_member_name" /></td>
    <td><code>string</code></td>
    <td>The name of the AppLinkMember. Required.</td>
</tr>
<tr id="parameter-app_link_name">
    <td><CopyableCode code="app_link_name" /></td>
    <td><code>string</code></td>
    <td>The name of the AppLink. Required.</td>
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
        { label: 'list_by_app_link', value: 'list_by_app_link' }
    ]}
>
<TabItem value="get">

Get an AppLinkMember.

```sql
SELECT
id,
name,
clusterType,
connectivityProfile,
location,
metadata,
observabilityProfile,
provisioningState,
systemData,
tags,
type,
upgradeProfile
FROM azure.app_network.app_link_members
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND app_link_name = '{{ app_link_name }}' -- required
AND app_link_member_name = '{{ app_link_member_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_app_link">

List AppLinkMember resources by AppLink.

```sql
SELECT
id,
name,
clusterType,
connectivityProfile,
location,
metadata,
observabilityProfile,
provisioningState,
systemData,
tags,
type,
upgradeProfile
FROM azure.app_network.app_link_members
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND app_link_name = '{{ app_link_name }}' -- required
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

Create an AppLinkMember.

```sql
INSERT INTO azure.app_network.app_link_members (
tags,
location,
properties,
resource_group_name,
app_link_name,
app_link_member_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ app_link_name }}',
'{{ app_link_member_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: app_link_members
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the app_link_members resource.
    - name: app_link_name
      value: "{{ app_link_name }}"
      description: Required parameter for the app_link_members resource.
    - name: app_link_member_name
      value: "{{ app_link_member_name }}"
      description: Required parameter for the app_link_members resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the app_link_members resource.
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
        The resource-specific properties for this resource.
      value:
        clusterType: "{{ clusterType }}"
        metadata:
          resourceId: "{{ resourceId }}"
        upgradeProfile:
          mode: "{{ mode }}"
          fullyManagedUpgradeProfile:
            releaseChannel: "{{ releaseChannel }}"
          selfManagedUpgradeProfile:
            version: "{{ version }}"
        observabilityProfile:
          metrics:
            metricsEndpoint: "{{ metricsEndpoint }}"
        connectivityProfile:
          eastWestGateway:
            visibility: "{{ visibility }}"
          privateConnect:
            subnetResourceId: "{{ subnetResourceId }}"
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

Update an AppLinkMember.

```sql
UPDATE azure.app_network.app_link_members
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND app_link_name = '{{ app_link_name }}' --required
AND app_link_member_name = '{{ app_link_member_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create an AppLinkMember.

```sql
REPLACE azure.app_network.app_link_members
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND app_link_name = '{{ app_link_name }}' --required
AND app_link_member_name = '{{ app_link_member_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete an AppLinkMember.

```sql
DELETE FROM azure.app_network.app_link_members
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND app_link_name = '{{ app_link_name }}' --required
AND app_link_member_name = '{{ app_link_member_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
