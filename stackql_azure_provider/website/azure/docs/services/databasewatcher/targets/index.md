--- 
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - databasewatcher
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

Creates, updates, deletes, gets or lists a <code>targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="targets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databasewatcher.targets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_watcher', value: 'list_by_watcher' }
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
    <td><CopyableCode code="connectionServerName" /></td>
    <td><code>string</code></td>
    <td>The server name to use in the connection string when connecting to a target. Port number and instance name must be specified separately. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The type of authentication to use when connecting to a target. Required. Known values are: "Aad" and "Sql". (Aad, Sql)</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>Discriminator property for TargetProperties. Required. Default value is None.</td>
</tr>
<tr>
    <td><CopyableCode code="targetVault" /></td>
    <td><code>object</code></td>
    <td>To use SQL authentication when connecting to targets, specify the vault where the login name and password secrets are stored.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_watcher">

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
    <td><CopyableCode code="connectionServerName" /></td>
    <td><code>string</code></td>
    <td>The server name to use in the connection string when connecting to a target. Port number and instance name must be specified separately. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The type of authentication to use when connecting to a target. Required. Known values are: "Aad" and "Sql". (Aad, Sql)</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>Discriminator property for TargetProperties. Required. Default value is None.</td>
</tr>
<tr>
    <td><CopyableCode code="targetVault" /></td>
    <td><code>object</code></td>
    <td>To use SQL authentication when connecting to targets, specify the vault where the login name and password secrets are stored.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Target.</td>
</tr>
<tr>
    <td><a href="#list_by_watcher"><CopyableCode code="list_by_watcher" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Target resources by Watcher.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Target.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Target.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-watcher_name"><code>watcher_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Target.</td>
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
<tr id="parameter-target_name">
    <td><CopyableCode code="target_name" /></td>
    <td><code>string</code></td>
    <td>The target resource name. Required.</td>
</tr>
<tr id="parameter-watcher_name">
    <td><CopyableCode code="watcher_name" /></td>
    <td><code>string</code></td>
    <td>The database watcher name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_watcher', value: 'list_by_watcher' }
    ]}
>
<TabItem value="get">

Get a Target.

```sql
SELECT
id,
name,
connectionServerName,
provisioningState,
systemData,
targetAuthenticationType,
targetType,
targetVault,
type
FROM azure.databasewatcher.targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND watcher_name = '{{ watcher_name }}' -- required
AND target_name = '{{ target_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_watcher">

List Target resources by Watcher.

```sql
SELECT
id,
name,
connectionServerName,
provisioningState,
systemData,
targetAuthenticationType,
targetType,
targetVault,
type
FROM azure.databasewatcher.targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND watcher_name = '{{ watcher_name }}' -- required
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

Create a Target.

```sql
INSERT INTO azure.databasewatcher.targets (
properties,
resource_group_name,
watcher_name,
target_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ watcher_name }}',
'{{ target_name }}',
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
- name: targets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the targets resource.
    - name: watcher_name
      value: "{{ watcher_name }}"
      description: Required parameter for the targets resource.
    - name: target_name
      value: "{{ target_name }}"
      description: Required parameter for the targets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the targets resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        targetType: "{{ targetType }}"
        targetAuthenticationType: "{{ targetAuthenticationType }}"
        targetVault:
          akvResourceId: "{{ akvResourceId }}"
          akvTargetUser: "{{ akvTargetUser }}"
          akvTargetPassword: "{{ akvTargetPassword }}"
        connectionServerName: "{{ connectionServerName }}"
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

Create a Target.

```sql
REPLACE azure.databasewatcher.targets
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND watcher_name = '{{ watcher_name }}' --required
AND target_name = '{{ target_name }}' --required
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

Delete a Target.

```sql
DELETE FROM azure.databasewatcher.targets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND watcher_name = '{{ watcher_name }}' --required
AND target_name = '{{ target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
