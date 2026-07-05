--- 
title: serial_ports
hide_title: false
hide_table_of_contents: false
keywords:
  - serial_ports
  - serialconsole
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

Creates, updates, deletes, gets or lists a <code>serial_ports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="serial_ports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.serialconsole.serial_ports" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscriptions', value: 'list_by_subscriptions' }
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
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the port is currently active. Known values are: "active" and "inactive". (active, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the port is enabled for a serial console connection. Known values are: "enabled" and "disabled". (enabled, disabled)</td>
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
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the port is currently active. Known values are: "active" and "inactive". (active, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the port is enabled for a serial console connection. Known values are: "enabled" and "disabled". (enabled, disabled)</td>
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
<TabItem value="list_by_subscriptions">

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
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the port is currently active. Known values are: "active" and "inactive". (active, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the port is enabled for a serial console connection. Known values are: "enabled" and "disabled". (enabled, disabled)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource"><code>parent_resource</code></a>, <a href="#parameter-serial_port"><code>serial_port</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the configured settings for a serial port.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource"><code>parent_resource</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the configured serial ports for a parent resource.</td>
</tr>
<tr>
    <td><a href="#list_by_subscriptions"><CopyableCode code="list_by_subscriptions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all SerialPort resources in a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource"><code>parent_resource</code></a>, <a href="#parameter-serial_port"><code>serial_port</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a serial port.</td>
</tr>
<tr>
    <td><a href="#connect"><CopyableCode code="connect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_type"><code>parent_resource_type</code></a>, <a href="#parameter-parent_resource"><code>parent_resource</code></a>, <a href="#parameter-serial_port"><code>serial_port</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Connect to serial port of the target resource.</td>
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
<tr id="parameter-parent_resource">
    <td><CopyableCode code="parent_resource" /></td>
    <td><code>string</code></td>
    <td>The name of the parent resource. Required.</td>
</tr>
<tr id="parameter-parent_resource_type">
    <td><CopyableCode code="parent_resource_type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the parent resource. For example: 'virtualMachines' or 'virtualMachineScaleSets'. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. Required.</td>
</tr>
<tr id="parameter-resource_provider_namespace">
    <td><CopyableCode code="resource_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The resource provider namespace of the parent resource. Required.</td>
</tr>
<tr id="parameter-serial_port">
    <td><CopyableCode code="serial_port" /></td>
    <td><code>string</code></td>
    <td>The name of the serial port to connect to. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_by_subscriptions', value: 'list_by_subscriptions' }
    ]}
>
<TabItem value="get">

Gets the configured settings for a serial port.

```sql
SELECT
id,
name,
connectionState,
state,
systemData,
type
FROM azure.serialconsole.serial_ports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_type = '{{ parent_resource_type }}' -- required
AND parent_resource = '{{ parent_resource }}' -- required
AND serial_port = '{{ serial_port }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all of the configured serial ports for a parent resource.

```sql
SELECT
id,
name,
connectionState,
state,
systemData,
type
FROM azure.serialconsole.serial_ports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_type = '{{ parent_resource_type }}' -- required
AND parent_resource = '{{ parent_resource }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscriptions">

Handles requests to list all SerialPort resources in a subscription.

```sql
SELECT
id,
name,
connectionState,
state,
systemData,
type
FROM azure.serialconsole.serial_ports
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a serial port.

```sql
INSERT INTO azure.serialconsole.serial_ports (
properties,
resource_group_name,
resource_provider_namespace,
parent_resource_type,
parent_resource,
serial_port,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_provider_namespace }}',
'{{ parent_resource_type }}',
'{{ parent_resource }}',
'{{ serial_port }}',
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
- name: serial_ports
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the serial_ports resource.
    - name: resource_provider_namespace
      value: "{{ resource_provider_namespace }}"
      description: Required parameter for the serial_ports resource.
    - name: parent_resource_type
      value: "{{ parent_resource_type }}"
      description: Required parameter for the serial_ports resource.
    - name: parent_resource
      value: "{{ parent_resource }}"
      description: Required parameter for the serial_ports resource.
    - name: serial_port
      value: "{{ serial_port }}"
      description: Required parameter for the serial_ports resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the serial_ports resource.
    - name: properties
      description: |
        The properties of the serial port.
      value:
        state: "{{ state }}"
        connectionState: "{{ connectionState }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="connect"
    values={[
        { label: 'connect', value: 'connect' }
    ]}
>
<TabItem value="connect">

Connect to serial port of the target resource.

```sql
EXEC azure.serialconsole.serial_ports.connect 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_provider_namespace='{{ resource_provider_namespace }}' --required, 
@parent_resource_type='{{ parent_resource_type }}' --required, 
@parent_resource='{{ parent_resource }}' --required, 
@serial_port='{{ serial_port }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
