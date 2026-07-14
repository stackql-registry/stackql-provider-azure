--- 
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - mysql_flexible_servers
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql_flexible_servers.configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedValues" /></td>
    <td><code>string</code></td>
    <td>Allowed values of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="currentValue" /></td>
    <td><code>string</code></td>
    <td>Current value of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>Data type of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultValue" /></td>
    <td><code>string</code></td>
    <td>Default value of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="documentationLink" /></td>
    <td><code>string</code></td>
    <td>The link used to get the document from community or Azure site.</td>
</tr>
<tr>
    <td><CopyableCode code="isConfigPendingRestart" /></td>
    <td><code>string</code></td>
    <td>If is the configuration pending restart or not. Known values are: "True" and "False".</td>
</tr>
<tr>
    <td><CopyableCode code="isDynamicConfig" /></td>
    <td><code>string</code></td>
    <td>If is the configuration dynamic. Known values are: "True" and "False".</td>
</tr>
<tr>
    <td><CopyableCode code="isReadOnly" /></td>
    <td><code>string</code></td>
    <td>If is the configuration read only. Known values are: "True" and "False".</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the configuration. Known values are: "system-default" and "user-override".</td>
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
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Value of the configuration.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_server">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedValues" /></td>
    <td><code>string</code></td>
    <td>Allowed values of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="currentValue" /></td>
    <td><code>string</code></td>
    <td>Current value of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>Data type of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultValue" /></td>
    <td><code>string</code></td>
    <td>Default value of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="documentationLink" /></td>
    <td><code>string</code></td>
    <td>The link used to get the document from community or Azure site.</td>
</tr>
<tr>
    <td><CopyableCode code="isConfigPendingRestart" /></td>
    <td><code>string</code></td>
    <td>If is the configuration pending restart or not. Known values are: "True" and "False".</td>
</tr>
<tr>
    <td><CopyableCode code="isDynamicConfig" /></td>
    <td><code>string</code></td>
    <td>If is the configuration dynamic. Known values are: "True" and "False".</td>
</tr>
<tr>
    <td><CopyableCode code="isReadOnly" /></td>
    <td><code>string</code></td>
    <td>If is the configuration read only. Known values are: "True" and "False".</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the configuration. Known values are: "system-default" and "user-override".</td>
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
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Value of the configuration.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a configuration of server.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-keyword"><code>keyword</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a></td>
    <td>List all the configurations in a given server.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a configuration of a server.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a configuration of a server.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a configuration of a server.</td>
</tr>
<tr>
    <td><a href="#batch_update"><CopyableCode code="batch_update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a list of configurations in a given server.</td>
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
<tr id="parameter-configuration_name">
    <td><CopyableCode code="configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server configuration. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-keyword">
    <td><CopyableCode code="keyword" /></td>
    <td><code>string</code></td>
    <td>The keyword of the server configuration. Default value is None.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>The page of the server configuration. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>The pageSize of the server configuration. Default value is None.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td>The tags of the server configuration. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="get">

Gets information about a configuration of server.

```sql
SELECT
id,
name,
allowedValues,
currentValue,
dataType,
defaultValue,
description,
documentationLink,
isConfigPendingRestart,
isDynamicConfig,
isReadOnly,
source,
systemData,
type,
value
FROM azure.mysql_flexible_servers.configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND configuration_name = '{{ configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

List all the configurations in a given server.

```sql
SELECT
id,
name,
allowedValues,
currentValue,
dataType,
defaultValue,
description,
documentationLink,
isConfigPendingRestart,
isDynamicConfig,
isReadOnly,
source,
systemData,
type,
value
FROM azure.mysql_flexible_servers.configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND tags = '{{ tags }}'
AND keyword = '{{ keyword }}'
AND page = '{{ page }}'
AND pageSize = '{{ pageSize }}'
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

Updates a configuration of a server.

```sql
INSERT INTO azure.mysql_flexible_servers.configurations (
properties,
resource_group_name,
server_name,
configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ configuration_name }}',
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
- name: configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the configurations resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the configurations resource.
    - name: configuration_name
      value: "{{ configuration_name }}"
      description: Required parameter for the configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the configurations resource.
    - name: properties
      value:
        value: "{{ value }}"
        currentValue: "{{ currentValue }}"
        source: "{{ source }}"
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

Updates a configuration of a server.

```sql
UPDATE azure.mysql_flexible_servers.configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND configuration_name = '{{ configuration_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Updates a configuration of a server.

```sql
REPLACE azure.mysql_flexible_servers.configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND configuration_name = '{{ configuration_name }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="batch_update"
    values={[
        { label: 'batch_update', value: 'batch_update' }
    ]}
>
<TabItem value="batch_update">

Update a list of configurations in a given server.

```sql
EXEC azure.mysql_flexible_servers.configurations.batch_update 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}", 
"resetAllToDefault": "{{ resetAllToDefault }}"
}'
;
```
</TabItem>
</Tabs>
