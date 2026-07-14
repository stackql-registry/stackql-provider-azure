--- 
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - app_configuration
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.snapshots" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="compositionType" /></td>
    <td><code>string</code></td>
    <td>The composition type describes how the key-values within the snapshot are composed. The 'key' composition type ensures there are no two key-values containing the same key. The 'key_label' composition type ensures there are no two key-values containing the same key and label. Known values are: "Key" and "Key_Label". (Key, Key_Label)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the snapshot was created.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A value representing the current state of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="expires" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the snapshot will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>A list of filters used to filter the key-values included in the snapshot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsCount" /></td>
    <td><code>integer</code></td>
    <td>The amount of key-values in the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the snapshot. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionPeriod" /></td>
    <td><code>integer</code></td>
    <td>The amount of time, in seconds, that a snapshot will remain in the archived state before expiring. This property is only writable during the creation of a snapshot. If not specified, the default lifetime of key-value revisions will be used.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>The size in bytes of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the snapshot. Known values are: "Provisioning", "Ready", "Archived", and "Failed". (Provisioning, Ready, Archived, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the snapshot. NOTE: These are data plane tags, not ARM tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the specified snapshot. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration snapshots the data plane API should be used instead.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a snapshot. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration snapshots the data plane API should be used instead.</td>
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
<tr id="parameter-config_store_name">
    <td><CopyableCode code="config_store_name" /></td>
    <td><code>string</code></td>
    <td>The name of the configuration store. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-snapshot_name">
    <td><CopyableCode code="snapshot_name" /></td>
    <td><code>string</code></td>
    <td>The name of the snapshot. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the properties of the specified snapshot. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration snapshots the data plane API should be used instead.

```sql
SELECT
id,
name,
compositionType,
created,
etag,
expires,
filters,
itemsCount,
provisioningState,
retentionPeriod,
size,
status,
systemData,
tags,
type
FROM azure.app_configuration.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND config_store_name = '{{ config_store_name }}' -- required
AND snapshot_name = '{{ snapshot_name }}' -- required
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

Creates a snapshot. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration snapshots the data plane API should be used instead.

```sql
INSERT INTO azure.app_configuration.snapshots (
properties,
resource_group_name,
config_store_name,
snapshot_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ config_store_name }}',
'{{ snapshot_name }}',
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
- name: snapshots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the snapshots resource.
    - name: config_store_name
      value: "{{ config_store_name }}"
      description: Required parameter for the snapshots resource.
    - name: snapshot_name
      value: "{{ snapshot_name }}"
      description: Required parameter for the snapshots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the snapshots resource.
    - name: properties
      description: |
        All snapshot properties. Required.
      value:
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        filters:
          - key: "{{ key }}"
            label: "{{ label }}"
        compositionType: "{{ compositionType }}"
        created: "{{ created }}"
        expires: "{{ expires }}"
        retentionPeriod: {{ retentionPeriod }}
        size: {{ size }}
        itemsCount: {{ itemsCount }}
        tags: "{{ tags }}"
        etag: "{{ etag }}"
`}</CodeBlock>

</TabItem>
</Tabs>
