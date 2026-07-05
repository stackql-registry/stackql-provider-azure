--- 
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - azurestackhci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azurestackhci.extensions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_arc_setting', value: 'list_by_arc_setting' }
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
    <td><CopyableCode code="aggregateState" /></td>
    <td><code>string</code></td>
    <td>Aggregate state of Arc Extensions across the nodes in this HCI cluster. This reflects the overall status of the extension deployment and operation across all nodes. Known values are: "NotSpecified", "Error", "Succeeded", "Canceled", "Failed", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "UpgradeFailedRollbackSucceeded". (NotSpecified, Error, Succeeded, Canceled, Failed, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, UpgradeFailedRollbackSucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="extensionParameters" /></td>
    <td><code>object</code></td>
    <td>Parameters specific to this extension type.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Indicates if the extension is managed by Azure or the user. This determines who controls the deployment and lifecycle of the extension. Known values are: "User" and "Azure". (User, Azure)</td>
</tr>
<tr>
    <td><CopyableCode code="perNodeExtensionDetails" /></td>
    <td><code>array</code></td>
    <td>State of Arc Extension in each of the nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Extension proxy resource. Indicates the current lifecycle status of the resource, such as whether it's being created, updated, deleted, or has encountered an error. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
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
<TabItem value="list_by_arc_setting">

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
    <td><CopyableCode code="aggregateState" /></td>
    <td><code>string</code></td>
    <td>Aggregate state of Arc Extensions across the nodes in this HCI cluster. This reflects the overall status of the extension deployment and operation across all nodes. Known values are: "NotSpecified", "Error", "Succeeded", "Canceled", "Failed", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "UpgradeFailedRollbackSucceeded". (NotSpecified, Error, Succeeded, Canceled, Failed, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, UpgradeFailedRollbackSucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="extensionParameters" /></td>
    <td><code>object</code></td>
    <td>Parameters specific to this extension type.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Indicates if the extension is managed by Azure or the user. This determines who controls the deployment and lifecycle of the extension. Known values are: "User" and "Azure". (User, Azure)</td>
</tr>
<tr>
    <td><CopyableCode code="perNodeExtensionDetails" /></td>
    <td><code>array</code></td>
    <td>State of Arc Extension in each of the nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Extension proxy resource. Indicates the current lifecycle status of the resource, such as whether it's being created, updated, deleted, or has encountered an error. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get particular Arc Extension of HCI Cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_arc_setting"><CopyableCode code="list_by_arc_setting" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Extensions under ArcSetting resource.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Extension for HCI cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update Extension for HCI cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete particular Arc Extension of HCI Cluster.</td>
</tr>
<tr>
    <td><a href="#upgrade"><CopyableCode code="upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrade a particular Arc Extension of HCI Cluster.</td>
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
<tr id="parameter-arc_setting_name">
    <td><CopyableCode code="arc_setting_name" /></td>
    <td><code>string</code></td>
    <td>The name of the proxy resource holding details of HCI ArcSetting information. Required.</td>
</tr>
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
</tr>
<tr id="parameter-extension_name">
    <td><CopyableCode code="extension_name" /></td>
    <td><code>string</code></td>
    <td>The name of the machine extension. Required.</td>
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
        { label: 'list_by_arc_setting', value: 'list_by_arc_setting' }
    ]}
>
<TabItem value="get">

Get particular Arc Extension of HCI Cluster.

```sql
SELECT
id,
name,
aggregateState,
extensionParameters,
managedBy,
perNodeExtensionDetails,
provisioningState,
systemData,
type
FROM azure_stack.azurestackhci.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND arc_setting_name = '{{ arc_setting_name }}' -- required
AND extension_name = '{{ extension_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_arc_setting">

List all Extensions under ArcSetting resource.

```sql
SELECT
id,
name,
aggregateState,
extensionParameters,
managedBy,
perNodeExtensionDetails,
provisioningState,
systemData,
type
FROM azure_stack.azurestackhci.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND arc_setting_name = '{{ arc_setting_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create Extension for HCI cluster.

```sql
INSERT INTO azure_stack.azurestackhci.extensions (
properties,
resource_group_name,
cluster_name,
arc_setting_name,
extension_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ arc_setting_name }}',
'{{ extension_name }}',
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
- name: extensions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the extensions resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the extensions resource.
    - name: arc_setting_name
      value: "{{ arc_setting_name }}"
      description: Required parameter for the extensions resource.
    - name: extension_name
      value: "{{ extension_name }}"
      description: Required parameter for the extensions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the extensions resource.
    - name: properties
      description: |
        Describes Machine Extension Properties.
      value:
        provisioningState: "{{ provisioningState }}"
        extensionParameters:
          forceUpdateTag: "{{ forceUpdateTag }}"
          publisher: "{{ publisher }}"
          type: "{{ type }}"
          typeHandlerVersion: "{{ typeHandlerVersion }}"
          autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
          settings: "{{ settings }}"
          protectedSettings: "{{ protectedSettings }}"
          enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
        aggregateState: "{{ aggregateState }}"
        perNodeExtensionDetails:
          - name: "{{ name }}"
            extension: "{{ extension }}"
            typeHandlerVersion: "{{ typeHandlerVersion }}"
            state: "{{ state }}"
            instanceView:
              name: "{{ name }}"
              type: "{{ type }}"
              typeHandlerVersion: "{{ typeHandlerVersion }}"
              status:
                code: "{{ code }}"
                level: "{{ level }}"
                displayStatus: "{{ displayStatus }}"
                message: "{{ message }}"
                time: "{{ time }}"
        managedBy: "{{ managedBy }}"
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

Update Extension for HCI cluster.

```sql
UPDATE azure_stack.azurestackhci.extensions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND arc_setting_name = '{{ arc_setting_name }}' --required
AND extension_name = '{{ extension_name }}' --required
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

Delete particular Arc Extension of HCI Cluster.

```sql
DELETE FROM azure_stack.azurestackhci.extensions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND arc_setting_name = '{{ arc_setting_name }}' --required
AND extension_name = '{{ extension_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upgrade"
    values={[
        { label: 'upgrade', value: 'upgrade' }
    ]}
>
<TabItem value="upgrade">

Upgrade a particular Arc Extension of HCI Cluster.

```sql
EXEC azure_stack.azurestackhci.extensions.upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@arc_setting_name='{{ arc_setting_name }}' --required, 
@extension_name='{{ extension_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetVersion": "{{ targetVersion }}"
}'
;
```
</TabItem>
</Tabs>
