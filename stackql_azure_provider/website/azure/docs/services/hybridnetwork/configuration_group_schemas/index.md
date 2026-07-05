--- 
title: configuration_group_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_group_schemas
  - hybridnetwork
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

Creates, updates, deletes, gets or lists a <code>configuration_group_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configuration_group_schemas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridnetwork.configuration_group_schemas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_publisher', value: 'list_by_publisher' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of what schema can contain.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Configuration group schema resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaDefinition" /></td>
    <td><code>string</code></td>
    <td>Name and value pairs that define the configuration value. It can be a well formed escaped JSON string.</td>
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
    <td><CopyableCode code="versionState" /></td>
    <td><code>string</code></td>
    <td>The configuration group schema version state. Known values are: "Unknown", "Preview", "Active", "Deprecated", "Validating", and "ValidationFailed".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_publisher">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of what schema can contain.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Configuration group schema resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaDefinition" /></td>
    <td><code>string</code></td>
    <td>Name and value pairs that define the configuration value. It can be a well formed escaped JSON string.</td>
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
    <td><CopyableCode code="versionState" /></td>
    <td><code>string</code></td>
    <td>The configuration group schema version state. Known values are: "Unknown", "Preview", "Active", "Deprecated", "Validating", and "ValidationFailed".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-configuration_group_schema_name"><code>configuration_group_schema_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified configuration group schema.</td>
</tr>
<tr>
    <td><a href="#list_by_publisher"><CopyableCode code="list_by_publisher" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information of the configuration group schemas under a publisher.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-configuration_group_schema_name"><code>configuration_group_schema_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a configuration group schema.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-configuration_group_schema_name"><code>configuration_group_schema_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a configuration group schema resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-configuration_group_schema_name"><code>configuration_group_schema_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a configuration group schema.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-configuration_group_schema_name"><code>configuration_group_schema_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specified configuration group schema.</td>
</tr>
<tr>
    <td><a href="#update_state"><CopyableCode code="update_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-configuration_group_schema_name"><code>configuration_group_schema_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update configuration group schema state.</td>
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
<tr id="parameter-configuration_group_schema_name">
    <td><CopyableCode code="configuration_group_schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the configuration group schema. Required.</td>
</tr>
<tr id="parameter-publisher_name">
    <td><CopyableCode code="publisher_name" /></td>
    <td><code>string</code></td>
    <td>The name of the publisher. Required.</td>
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
        { label: 'list_by_publisher', value: 'list_by_publisher' }
    ]}
>
<TabItem value="get">

Gets information about the specified configuration group schema.

```sql
SELECT
id,
name,
description,
location,
provisioningState,
schemaDefinition,
systemData,
tags,
type,
versionState
FROM azure.hybridnetwork.configuration_group_schemas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND configuration_group_schema_name = '{{ configuration_group_schema_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_publisher">

Gets information of the configuration group schemas under a publisher.

```sql
SELECT
id,
name,
description,
location,
provisioningState,
schemaDefinition,
systemData,
tags,
type,
versionState
FROM azure.hybridnetwork.configuration_group_schemas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
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

Creates or updates a configuration group schema.

```sql
INSERT INTO azure.hybridnetwork.configuration_group_schemas (
tags,
location,
properties,
resource_group_name,
publisher_name,
configuration_group_schema_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ publisher_name }}',
'{{ configuration_group_schema_name }}',
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
- name: configuration_group_schemas
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the configuration_group_schemas resource.
    - name: publisher_name
      value: "{{ publisher_name }}"
      description: Required parameter for the configuration_group_schemas resource.
    - name: configuration_group_schema_name
      value: "{{ configuration_group_schema_name }}"
      description: Required parameter for the configuration_group_schemas resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the configuration_group_schemas resource.
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
        Configuration group schema properties.
      value:
        provisioningState: "{{ provisioningState }}"
        versionState: "{{ versionState }}"
        description: "{{ description }}"
        schemaDefinition: "{{ schemaDefinition }}"
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

Updates a configuration group schema resource.

```sql
UPDATE azure.hybridnetwork.configuration_group_schemas
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND configuration_group_schema_name = '{{ configuration_group_schema_name }}' --required
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

Creates or updates a configuration group schema.

```sql
REPLACE azure.hybridnetwork.configuration_group_schemas
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND configuration_group_schema_name = '{{ configuration_group_schema_name }}' --required
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

Deletes a specified configuration group schema.

```sql
DELETE FROM azure.hybridnetwork.configuration_group_schemas
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND configuration_group_schema_name = '{{ configuration_group_schema_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_state"
    values={[
        { label: 'update_state', value: 'update_state' }
    ]}
>
<TabItem value="update_state">

Update configuration group schema state.

```sql
EXEC azure.hybridnetwork.configuration_group_schemas.update_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@publisher_name='{{ publisher_name }}' --required, 
@configuration_group_schema_name='{{ configuration_group_schema_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"versionState": "{{ versionState }}"
}'
;
```
</TabItem>
</Tabs>
