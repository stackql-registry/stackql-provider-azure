--- 
title: workspace_managed_sql_server_encryption_protector
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_encryption_protector
  - synapse
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

Creates, updates, deletes, gets or lists a <code>workspace_managed_sql_server_encryption_protector</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_managed_sql_server_encryption_protector" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_managed_sql_server_encryption_protector" /></td></tr>
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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of encryption protector. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="serverKeyName" /></td>
    <td><code>string</code></td>
    <td>The name of the server key.</td>
</tr>
<tr>
    <td><CopyableCode code="serverKeyType" /></td>
    <td><code>string</code></td>
    <td>The encryption protector type like 'ServiceManaged', 'AzureKeyVault'. Known values are: "ServiceManaged" and "AzureKeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="subregion" /></td>
    <td><code>string</code></td>
    <td>Subregion of the encryption protector.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the server key.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>The URI of the server key.</td>
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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of encryption protector. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="serverKeyName" /></td>
    <td><code>string</code></td>
    <td>The name of the server key.</td>
</tr>
<tr>
    <td><CopyableCode code="serverKeyType" /></td>
    <td><code>string</code></td>
    <td>The encryption protector type like 'ServiceManaged', 'AzureKeyVault'. Known values are: "ServiceManaged" and "AzureKeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="subregion" /></td>
    <td><code>string</code></td>
    <td>Subregion of the encryption protector.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the server key.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>The URI of the server key.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-encryption_protector_name"><code>encryption_protector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get workspace server's encryption protector. Get workspace managed sql server's encryption protector.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get list of encryption protectors for the server. Get list of encryption protectors for workspace managed sql server.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-encryption_protector_name"><code>encryption_protector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates workspace server's encryption protector. Updates workspace managed sql server's encryption protector.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-encryption_protector_name"><code>encryption_protector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates workspace server's encryption protector. Updates workspace managed sql server's encryption protector.</td>
</tr>
<tr>
    <td><a href="#revalidate"><CopyableCode code="revalidate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-encryption_protector_name"><code>encryption_protector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revalidates server's existing encryption protector. Revalidates workspace managed sql server's existing encryption protector.</td>
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
<tr id="parameter-encryption_protector_name">
    <td><CopyableCode code="encryption_protector_name" /></td>
    <td><code>string</code></td>
    <td>The name of the encryption protector. "current" Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
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

Get workspace server's encryption protector. Get workspace managed sql server's encryption protector.

```sql
SELECT
id,
name,
kind,
location,
serverKeyName,
serverKeyType,
subregion,
thumbprint,
type,
uri
FROM azure.synapse.workspace_managed_sql_server_encryption_protector
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND encryption_protector_name = '{{ encryption_protector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get list of encryption protectors for the server. Get list of encryption protectors for workspace managed sql server.

```sql
SELECT
id,
name,
kind,
location,
serverKeyName,
serverKeyType,
subregion,
thumbprint,
type,
uri
FROM azure.synapse.workspace_managed_sql_server_encryption_protector
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Updates workspace server's encryption protector. Updates workspace managed sql server's encryption protector.

```sql
INSERT INTO azure.synapse.workspace_managed_sql_server_encryption_protector (
properties,
resource_group_name,
workspace_name,
encryption_protector_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ encryption_protector_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
location,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspace_managed_sql_server_encryption_protector
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspace_managed_sql_server_encryption_protector resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the workspace_managed_sql_server_encryption_protector resource.
    - name: encryption_protector_name
      value: "{{ encryption_protector_name }}"
      description: Required parameter for the workspace_managed_sql_server_encryption_protector resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspace_managed_sql_server_encryption_protector resource.
    - name: properties
      value:
        serverKeyName: "{{ serverKeyName }}"
        serverKeyType: "{{ serverKeyType }}"
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

Updates workspace server's encryption protector. Updates workspace managed sql server's encryption protector.

```sql
REPLACE azure.synapse.workspace_managed_sql_server_encryption_protector
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND encryption_protector_name = '{{ encryption_protector_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
location,
properties,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revalidate"
    values={[
        { label: 'revalidate', value: 'revalidate' }
    ]}
>
<TabItem value="revalidate">

Revalidates server's existing encryption protector. Revalidates workspace managed sql server's existing encryption protector.

```sql
EXEC azure.synapse.workspace_managed_sql_server_encryption_protector.revalidate 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@encryption_protector_name='{{ encryption_protector_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
