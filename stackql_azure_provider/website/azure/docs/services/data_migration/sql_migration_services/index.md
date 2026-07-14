--- 
title: sql_migration_services
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_migration_services
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>sql_migration_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_migration_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.sql_migration_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="integrationRuntimeState" /></td>
    <td><code>string</code></td>
    <td>Current state of the Integration runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="integrationRuntimeState" /></td>
    <td><code>string</code></td>
    <td>Current state of the Integration runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="integrationRuntimeState" /></td>
    <td><code>string</code></td>
    <td>Current state of the Integration runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>:vartype location: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>:vartype tags: dict[str, str]</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the Database Migration Service.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve all SQL migration services in the resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve all SQL migration services in the subscriptions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update Database Migration Service.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update Database Migration Service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update Database Migration Service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Database Migration Service.</td>
</tr>
<tr>
    <td><a href="#list_auth_keys"><CopyableCode code="list_auth_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the List of Authentication Keys for Self Hosted Integration Runtime.</td>
</tr>
<tr>
    <td><a href="#list_migrations"><CopyableCode code="list_migrations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the List of database migrations attached to the service.</td>
</tr>
<tr>
    <td><a href="#list_monitoring_data"><CopyableCode code="list_monitoring_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the registered Integration Runtime nodes and their monitoring data for a given Database Migration Service.</td>
</tr>
<tr>
    <td><a href="#regenerate_auth_keys"><CopyableCode code="regenerate_auth_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerate a new set of Authentication Keys for Self Hosted Integration Runtime.</td>
</tr>
<tr>
    <td><a href="#delete_node"><CopyableCode code="delete_node" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_migration_service_name"><code>sql_migration_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the integration runtime node.</td>
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
<tr id="parameter-sql_migration_service_name">
    <td><CopyableCode code="sql_migration_service_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SQL Migration Service. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Retrieve the Database Migration Service.

```sql
SELECT
id,
name,
integrationRuntimeState,
location,
provisioningState,
systemData,
tags,
type
FROM azure.data_migration.sql_migration_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_migration_service_name = '{{ sql_migration_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieve all SQL migration services in the resource group.

```sql
SELECT
id,
name,
integrationRuntimeState,
location,
provisioningState,
systemData,
tags,
type
FROM azure.data_migration.sql_migration_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Retrieve all SQL migration services in the subscriptions.

```sql
SELECT
id,
name,
integrationRuntimeState,
location,
provisioningState,
systemData,
tags,
type
FROM azure.data_migration.sql_migration_services
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or Update Database Migration Service.

```sql
INSERT INTO azure.data_migration.sql_migration_services (
properties,
location,
tags,
resource_group_name,
sql_migration_service_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ sql_migration_service_name }}',
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
- name: sql_migration_services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_migration_services resource.
    - name: sql_migration_service_name
      value: "{{ sql_migration_service_name }}"
      description: Required parameter for the sql_migration_services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_migration_services resource.
    - name: properties
      description: |
        The SQL Migration Service properties.
      value:
        provisioningState: "{{ provisioningState }}"
        integrationRuntimeState: "{{ integrationRuntimeState }}"
    - name: location
      value: "{{ location }}"
      description: |
        :vartype location: str
    - name: tags
      value: "{{ tags }}"
      description: |
        :vartype tags: dict[str, str]
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

Update Database Migration Service.

```sql
UPDATE azure.data_migration.sql_migration_services
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_migration_service_name = '{{ sql_migration_service_name }}' --required
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

Create or Update Database Migration Service.

```sql
REPLACE azure.data_migration.sql_migration_services
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_migration_service_name = '{{ sql_migration_service_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete Database Migration Service.

```sql
DELETE FROM azure.data_migration.sql_migration_services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sql_migration_service_name = '{{ sql_migration_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_auth_keys"
    values={[
        { label: 'list_auth_keys', value: 'list_auth_keys' },
        { label: 'list_migrations', value: 'list_migrations' },
        { label: 'list_monitoring_data', value: 'list_monitoring_data' },
        { label: 'regenerate_auth_keys', value: 'regenerate_auth_keys' },
        { label: 'delete_node', value: 'delete_node' }
    ]}
>
<TabItem value="list_auth_keys">

Retrieve the List of Authentication Keys for Self Hosted Integration Runtime.

```sql
EXEC azure.data_migration.sql_migration_services.list_auth_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_migration_service_name='{{ sql_migration_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_migrations">

Retrieve the List of database migrations attached to the service.

```sql
EXEC azure.data_migration.sql_migration_services.list_migrations 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_migration_service_name='{{ sql_migration_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_monitoring_data">

Retrieve the registered Integration Runtime nodes and their monitoring data for a given Database Migration Service.

```sql
EXEC azure.data_migration.sql_migration_services.list_monitoring_data 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_migration_service_name='{{ sql_migration_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_auth_keys">

Regenerate a new set of Authentication Keys for Self Hosted Integration Runtime.

```sql
EXEC azure.data_migration.sql_migration_services.regenerate_auth_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_migration_service_name='{{ sql_migration_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}", 
"authKey1": "{{ authKey1 }}", 
"authKey2": "{{ authKey2 }}"
}'
;
```
</TabItem>
<TabItem value="delete_node">

Delete the integration runtime node.

```sql
EXEC azure.data_migration.sql_migration_services.delete_node 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_migration_service_name='{{ sql_migration_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodeName": "{{ nodeName }}", 
"integrationRuntimeName": "{{ integrationRuntimeName }}"
}'
;
```
</TabItem>
</Tabs>
