--- 
title: sites_by_service_group
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_by_service_group
  - site_manager
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

Creates, updates, deletes, gets or lists a <code>sites_by_service_group</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sites_by_service_group" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.site_manager.sites_by_service_group" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service_group', value: 'list_by_service_group' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of Site resource.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>displayName of Site resource.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs for labeling the site resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of last operation. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="siteAddress" /></td>
    <td><code>object</code></td>
    <td>Physical address of the site.</td>
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
<TabItem value="list_by_service_group">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of Site resource.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>displayName of Site resource.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs for labeling the site resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of last operation. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="siteAddress" /></td>
    <td><code>object</code></td>
    <td>Physical address of the site.</td>
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
    <td><a href="#parameter-servicegroup_name"><code>servicegroup_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a></td>
    <td></td>
    <td>Get Site at SG scope.</td>
</tr>
<tr>
    <td><a href="#list_by_service_group"><CopyableCode code="list_by_service_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-servicegroup_name"><code>servicegroup_name</code></a></td>
    <td></td>
    <td>list Site at SG scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-servicegroup_name"><code>servicegroup_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a></td>
    <td></td>
    <td>create or update Site at SG scope.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-servicegroup_name"><code>servicegroup_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a></td>
    <td></td>
    <td>update Site at SG scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-servicegroup_name"><code>servicegroup_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a></td>
    <td></td>
    <td>create or update Site at SG scope.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-servicegroup_name"><code>servicegroup_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a></td>
    <td></td>
    <td>delete Site at SG scope.</td>
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
<tr id="parameter-servicegroup_name">
    <td><CopyableCode code="servicegroup_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
</tr>
<tr id="parameter-site_name">
    <td><CopyableCode code="site_name" /></td>
    <td><code>string</code></td>
    <td>The name of the site. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service_group', value: 'list_by_service_group' }
    ]}
>
<TabItem value="get">

Get Site at SG scope.

```sql
SELECT
id,
name,
description,
displayName,
labels,
provisioningState,
siteAddress,
systemData,
type
FROM azure.site_manager.sites_by_service_group
WHERE servicegroup_name = '{{ servicegroup_name }}' -- required
AND site_name = '{{ site_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_service_group">

list Site at SG scope.

```sql
SELECT
id,
name,
description,
displayName,
labels,
provisioningState,
siteAddress,
systemData,
type
FROM azure.site_manager.sites_by_service_group
WHERE servicegroup_name = '{{ servicegroup_name }}' -- required
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

create or update Site at SG scope.

```sql
INSERT INTO azure.site_manager.sites_by_service_group (
properties,
servicegroup_name,
site_name
)
SELECT 
'{{ properties }}',
'{{ servicegroup_name }}',
'{{ site_name }}'
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
- name: sites_by_service_group
  props:
    - name: servicegroup_name
      value: "{{ servicegroup_name }}"
      description: Required parameter for the sites_by_service_group resource.
    - name: site_name
      value: "{{ site_name }}"
      description: Required parameter for the sites_by_service_group resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        siteAddress:
          streetAddress1: "{{ streetAddress1 }}"
          streetAddress2: "{{ streetAddress2 }}"
          city: "{{ city }}"
          stateOrProvince: "{{ stateOrProvince }}"
          country: "{{ country }}"
          postalCode: "{{ postalCode }}"
        labels: "{{ labels }}"
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

update Site at SG scope.

```sql
UPDATE azure.site_manager.sites_by_service_group
SET 
properties = '{{ properties }}'
WHERE 
servicegroup_name = '{{ servicegroup_name }}' --required
AND site_name = '{{ site_name }}' --required
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

create or update Site at SG scope.

```sql
REPLACE azure.site_manager.sites_by_service_group
SET 
properties = '{{ properties }}'
WHERE 
servicegroup_name = '{{ servicegroup_name }}' --required
AND site_name = '{{ site_name }}' --required
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

delete Site at SG scope.

```sql
DELETE FROM azure.site_manager.sites_by_service_group
WHERE servicegroup_name = '{{ servicegroup_name }}' --required
AND site_name = '{{ site_name }}' --required
;
```
</TabItem>
</Tabs>
