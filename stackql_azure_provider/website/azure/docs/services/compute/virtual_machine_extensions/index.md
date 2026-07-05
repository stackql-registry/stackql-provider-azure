--- 
title: virtual_machine_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_extensions
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_extensions" /></td></tr>
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
    <td><CopyableCode code="autoUpgradeMinorVersion" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticUpgrade" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the extension should be automatically upgraded by the platform if there is a newer version of the extension available.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>How the extension handler should be forced to update even if the extension configuration has not changed.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine extension instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedSettings" /></td>
    <td><code>object</code></td>
    <td>The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedSettingsFromKeyVault" /></td>
    <td><code>object</code></td>
    <td>The extensions protected settings that are passed by reference, and consumed from key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionAfterExtensions" /></td>
    <td><code>array</code></td>
    <td>Collection of extension names after which this extension needs to be provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The name of the extension handler publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Json formatted public settings for the extension.</td>
</tr>
<tr>
    <td><CopyableCode code="suppressFailures" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether failures stemming from the extension will be suppressed (Operational failures such as not connecting to the VM will not be suppressed regardless of this value). The default is false.</td>
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
    <td><CopyableCode code="typeHandlerVersion" /></td>
    <td><code>string</code></td>
    <td>Specifies the version of the script handler.</td>
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
    <td><CopyableCode code="autoUpgradeMinorVersion" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticUpgrade" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the extension should be automatically upgraded by the platform if there is a newer version of the extension available.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>How the extension handler should be forced to update even if the extension configuration has not changed.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine extension instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedSettings" /></td>
    <td><code>object</code></td>
    <td>The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedSettingsFromKeyVault" /></td>
    <td><code>object</code></td>
    <td>The extensions protected settings that are passed by reference, and consumed from key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionAfterExtensions" /></td>
    <td><code>array</code></td>
    <td>Collection of extension names after which this extension needs to be provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The name of the extension handler publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Json formatted public settings for the extension.</td>
</tr>
<tr>
    <td><CopyableCode code="suppressFailures" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether failures stemming from the extension will be suppressed (Operational failures such as not connecting to the VM will not be suppressed regardless of this value). The default is false.</td>
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
    <td><CopyableCode code="typeHandlerVersion" /></td>
    <td><code>string</code></td>
    <td>Specifies the version of the script handler.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-vm_extension_name"><code>vm_extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to get the extension.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to get all extensions of a Virtual Machine.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-vm_extension_name"><code>vm_extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update the extension.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-vm_extension_name"><code>vm_extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update the extension.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-vm_extension_name"><code>vm_extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update the extension.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-vm_extension_name"><code>vm_extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete the extension.</td>
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
<tr id="parameter-vm_extension_name">
    <td><CopyableCode code="vm_extension_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine extension. Required.</td>
</tr>
<tr id="parameter-vm_name">
    <td><CopyableCode code="vm_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. Default value is None.</td>
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

The operation to get the extension.

```sql
SELECT
id,
name,
autoUpgradeMinorVersion,
enableAutomaticUpgrade,
forceUpdateTag,
instanceView,
location,
protectedSettings,
protectedSettingsFromKeyVault,
provisionAfterExtensions,
provisioningState,
publisher,
settings,
suppressFailures,
systemData,
tags,
type,
typeHandlerVersion
FROM azure.compute.virtual_machine_extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND vm_extension_name = '{{ vm_extension_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

The operation to get all extensions of a Virtual Machine.

```sql
SELECT
id,
name,
autoUpgradeMinorVersion,
enableAutomaticUpgrade,
forceUpdateTag,
instanceView,
location,
protectedSettings,
protectedSettingsFromKeyVault,
provisionAfterExtensions,
provisioningState,
publisher,
settings,
suppressFailures,
systemData,
tags,
type,
typeHandlerVersion
FROM azure.compute.virtual_machine_extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
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

The operation to create or update the extension.

```sql
INSERT INTO azure.compute.virtual_machine_extensions (
tags,
location,
properties,
resource_group_name,
vm_name,
vm_extension_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ vm_name }}',
'{{ vm_extension_name }}',
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
- name: virtual_machine_extensions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machine_extensions resource.
    - name: vm_name
      value: "{{ vm_name }}"
      description: Required parameter for the virtual_machine_extensions resource.
    - name: vm_extension_name
      value: "{{ vm_extension_name }}"
      description: Required parameter for the virtual_machine_extensions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machine_extensions resource.
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
        Describes the properties of a Virtual Machine Extension.
      value:
        forceUpdateTag: "{{ forceUpdateTag }}"
        publisher: "{{ publisher }}"
        type: "{{ type }}"
        typeHandlerVersion: "{{ typeHandlerVersion }}"
        autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
        enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
        settings: "{{ settings }}"
        protectedSettings: "{{ protectedSettings }}"
        provisioningState: "{{ provisioningState }}"
        instanceView:
          name: "{{ name }}"
          type: "{{ type }}"
          typeHandlerVersion: "{{ typeHandlerVersion }}"
          substatuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
          statuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        suppressFailures: {{ suppressFailures }}
        protectedSettingsFromKeyVault:
          secretUrl: "{{ secretUrl }}"
          sourceVault:
            id: "{{ id }}"
        provisionAfterExtensions:
          - "{{ provisionAfterExtensions }}"
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

The operation to update the extension.

```sql
UPDATE azure.compute.virtual_machine_extensions
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND vm_extension_name = '{{ vm_extension_name }}' --required
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

The operation to create or update the extension.

```sql
REPLACE azure.compute.virtual_machine_extensions
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND vm_extension_name = '{{ vm_extension_name }}' --required
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

The operation to delete the extension.

```sql
DELETE FROM azure.compute.virtual_machine_extensions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND vm_extension_name = '{{ vm_extension_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
