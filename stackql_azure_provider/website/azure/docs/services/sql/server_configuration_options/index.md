--- 
title: server_configuration_options
hide_title: false
hide_table_of_contents: false
keywords:
  - server_configuration_options
  - sql
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

Creates, updates, deletes, gets or lists a <code>server_configuration_options</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="server_configuration_options" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_configuration_options" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_managed_instance', value: 'list_by_managed_instance' }
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of server configuration option. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="serverConfigurationOptionValue" /></td>
    <td><code>integer</code></td>
    <td>Value of the server configuration option. Required.</td>
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
<TabItem value="list_by_managed_instance">

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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of server configuration option. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="serverConfigurationOptionValue" /></td>
    <td><code>integer</code></td>
    <td>Value of the server configuration option. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-server_configuration_option_name"><code>server_configuration_option_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets managed instance server configuration option.</td>
</tr>
<tr>
    <td><a href="#list_by_managed_instance"><CopyableCode code="list_by_managed_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of managed instance server configuration options.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-server_configuration_option_name"><code>server_configuration_option_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates managed instance server configuration option.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-server_configuration_option_name"><code>server_configuration_option_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates managed instance server configuration option.</td>
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
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_configuration_option_name">
    <td><CopyableCode code="server_configuration_option_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server configuration option. "allowPolybaseExport" Required.</td>
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
        { label: 'list_by_managed_instance', value: 'list_by_managed_instance' }
    ]}
>
<TabItem value="get">

Gets managed instance server configuration option.

```sql
SELECT
id,
name,
provisioningState,
serverConfigurationOptionValue,
systemData,
type
FROM azure.sql.server_configuration_options
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND server_configuration_option_name = '{{ server_configuration_option_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_managed_instance">

Gets a list of managed instance server configuration options.

```sql
SELECT
id,
name,
provisioningState,
serverConfigurationOptionValue,
systemData,
type
FROM azure.sql.server_configuration_options
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
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

Updates managed instance server configuration option.

```sql
INSERT INTO azure.sql.server_configuration_options (
properties,
resource_group_name,
managed_instance_name,
server_configuration_option_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ managed_instance_name }}',
'{{ server_configuration_option_name }}',
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
- name: server_configuration_options
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the server_configuration_options resource.
    - name: managed_instance_name
      value: "{{ managed_instance_name }}"
      description: Required parameter for the server_configuration_options resource.
    - name: server_configuration_option_name
      value: "{{ server_configuration_option_name }}"
      description: Required parameter for the server_configuration_options resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the server_configuration_options resource.
    - name: properties
      description: |
        Resource properties.
      value:
        serverConfigurationOptionValue: {{ serverConfigurationOptionValue }}
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

Updates managed instance server configuration option.

```sql
REPLACE azure.sql.server_configuration_options
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND server_configuration_option_name = '{{ server_configuration_option_name }}' --required
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
