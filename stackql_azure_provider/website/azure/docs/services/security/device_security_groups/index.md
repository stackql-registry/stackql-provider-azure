--- 
title: device_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_security_groups
  - security
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

Creates, updates, deletes, gets or lists a <code>device_security_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="device_security_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.device_security_groups" /></td></tr>
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
    <td><CopyableCode code="allowlistRules" /></td>
    <td><code>array</code></td>
    <td>The allow-list custom alert rules.</td>
</tr>
<tr>
    <td><CopyableCode code="denylistRules" /></td>
    <td><code>array</code></td>
    <td>The deny-list custom alert rules.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thresholdRules" /></td>
    <td><code>array</code></td>
    <td>The list of custom alert threshold rules.</td>
</tr>
<tr>
    <td><CopyableCode code="timeWindowRules" /></td>
    <td><code>array</code></td>
    <td>The list of custom alert time-window rules.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="allowlistRules" /></td>
    <td><code>array</code></td>
    <td>The allow-list custom alert rules.</td>
</tr>
<tr>
    <td><CopyableCode code="denylistRules" /></td>
    <td><code>array</code></td>
    <td>The deny-list custom alert rules.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thresholdRules" /></td>
    <td><code>array</code></td>
    <td>The list of custom alert threshold rules.</td>
</tr>
<tr>
    <td><CopyableCode code="timeWindowRules" /></td>
    <td><code>array</code></td>
    <td>The list of custom alert time-window rules.</td>
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
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-device_security_group_name"><code>device_security_group_name</code></a></td>
    <td></td>
    <td>Use this method to get the device security group for the specified IoT Hub resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Use this method get the list of device security groups for the specified IoT Hub resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-device_security_group_name"><code>device_security_group_name</code></a></td>
    <td></td>
    <td>Use this method to creates or updates the device security group on a specified IoT Hub resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-device_security_group_name"><code>device_security_group_name</code></a></td>
    <td></td>
    <td>Use this method to creates or updates the device security group on a specified IoT Hub resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-device_security_group_name"><code>device_security_group_name</code></a></td>
    <td></td>
    <td>User this method to deletes the device security group.</td>
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
<tr id="parameter-device_security_group_name">
    <td><CopyableCode code="device_security_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the device security group. Note that the name of the device security group is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
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

Use this method to get the device security group for the specified IoT Hub resource.

```sql
SELECT
id,
name,
allowlistRules,
denylistRules,
systemData,
thresholdRules,
timeWindowRules,
type
FROM azure.security.device_security_groups
WHERE resource_id = '{{ resource_id }}' -- required
AND device_security_group_name = '{{ device_security_group_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Use this method get the list of device security groups for the specified IoT Hub resource.

```sql
SELECT
id,
name,
allowlistRules,
denylistRules,
systemData,
thresholdRules,
timeWindowRules,
type
FROM azure.security.device_security_groups
WHERE resource_id = '{{ resource_id }}' -- required
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

Use this method to creates or updates the device security group on a specified IoT Hub resource.

```sql
INSERT INTO azure.security.device_security_groups (
properties,
resource_id,
device_security_group_name
)
SELECT 
'{{ properties }}',
'{{ resource_id }}',
'{{ device_security_group_name }}'
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
- name: device_security_groups
  props:
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the device_security_groups resource.
    - name: device_security_group_name
      value: "{{ device_security_group_name }}"
      description: Required parameter for the device_security_groups resource.
    - name: properties
      description: |
        Device Security group data.
      value:
        thresholdRules:
          - displayName: "{{ displayName }}"
            description: "{{ description }}"
            isEnabled: {{ isEnabled }}
            ruleType: "{{ ruleType }}"
            minThreshold: {{ minThreshold }}
            maxThreshold: {{ maxThreshold }}
        timeWindowRules:
          - displayName: "{{ displayName }}"
            description: "{{ description }}"
            isEnabled: {{ isEnabled }}
            ruleType: "{{ ruleType }}"
            minThreshold: {{ minThreshold }}
            maxThreshold: {{ maxThreshold }}
            timeWindowSize: "{{ timeWindowSize }}"
        allowlistRules:
          - displayName: "{{ displayName }}"
            description: "{{ description }}"
            isEnabled: {{ isEnabled }}
            ruleType: "{{ ruleType }}"
            valueType: "{{ valueType }}"
            allowlistValues: "{{ allowlistValues }}"
        denylistRules:
          - displayName: "{{ displayName }}"
            description: "{{ description }}"
            isEnabled: {{ isEnabled }}
            ruleType: "{{ ruleType }}"
            valueType: "{{ valueType }}"
            denylistValues: "{{ denylistValues }}"
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

Use this method to creates or updates the device security group on a specified IoT Hub resource.

```sql
REPLACE azure.security.device_security_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_id = '{{ resource_id }}' --required
AND device_security_group_name = '{{ device_security_group_name }}' --required
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

User this method to deletes the device security group.

```sql
DELETE FROM azure.security.device_security_groups
WHERE resource_id = '{{ resource_id }}' --required
AND device_security_group_name = '{{ device_security_group_name }}' --required
;
```
</TabItem>
</Tabs>
