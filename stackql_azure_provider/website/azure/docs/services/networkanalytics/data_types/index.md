--- 
title: data_types
hide_title: false
hide_table_of_contents: false
keywords:
  - data_types
  - networkanalytics
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

Creates, updates, deletes, gets or lists a <code>data_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_types" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.networkanalytics.data_types" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_data_product', value: 'list_by_data_product' }
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
    <td><CopyableCode code="databaseCacheRetention" /></td>
    <td><code>integer</code></td>
    <td>Field for database cache retention in days.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseRetention" /></td>
    <td><code>integer</code></td>
    <td>Field for database data retention in days.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Latest provisioning state of data product. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of data type. Known values are: "Stopped" and "Running".</td>
</tr>
<tr>
    <td><CopyableCode code="stateReason" /></td>
    <td><code>string</code></td>
    <td>Reason for the state of data type.</td>
</tr>
<tr>
    <td><CopyableCode code="storageOutputRetention" /></td>
    <td><code>integer</code></td>
    <td>Field for storage output retention in days.</td>
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
    <td><CopyableCode code="visualizationUrl" /></td>
    <td><code>string</code></td>
    <td>Url for data visualization.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_data_product">

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
    <td><CopyableCode code="databaseCacheRetention" /></td>
    <td><code>integer</code></td>
    <td>Field for database cache retention in days.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseRetention" /></td>
    <td><code>integer</code></td>
    <td>Field for database data retention in days.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Latest provisioning state of data product. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of data type. Known values are: "Stopped" and "Running".</td>
</tr>
<tr>
    <td><CopyableCode code="stateReason" /></td>
    <td><code>string</code></td>
    <td>Reason for the state of data type.</td>
</tr>
<tr>
    <td><CopyableCode code="storageOutputRetention" /></td>
    <td><code>integer</code></td>
    <td>Field for storage output retention in days.</td>
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
    <td><CopyableCode code="visualizationUrl" /></td>
    <td><code>string</code></td>
    <td>Url for data visualization.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-data_type_name"><code>data_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve data type resource.</td>
</tr>
<tr>
    <td><a href="#list_by_data_product"><CopyableCode code="list_by_data_product" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List data type by parent resource.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-data_type_name"><code>data_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create data type resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-data_type_name"><code>data_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update data type resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-data_type_name"><code>data_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete data type resource.</td>
</tr>
<tr>
    <td><a href="#delete_data"><CopyableCode code="delete_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-data_type_name"><code>data_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete data for data type.</td>
</tr>
<tr>
    <td><a href="#generate_storage_container_sas_token"><CopyableCode code="generate_storage_container_sas_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-data_type_name"><code>data_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-startTimeStamp"><code>startTimeStamp</code></a>, <a href="#parameter-expiryTimeStamp"><code>expiryTimeStamp</code></a>, <a href="#parameter-ipAddress"><code>ipAddress</code></a></td>
    <td></td>
    <td>Generate sas token for storage container.</td>
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
<tr id="parameter-data_product_name">
    <td><CopyableCode code="data_product_name" /></td>
    <td><code>string</code></td>
    <td>The data product resource name. Required.</td>
</tr>
<tr id="parameter-data_type_name">
    <td><CopyableCode code="data_type_name" /></td>
    <td><code>string</code></td>
    <td>The data type name. Required.</td>
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
        { label: 'list_by_data_product', value: 'list_by_data_product' }
    ]}
>
<TabItem value="get">

Retrieve data type resource.

```sql
SELECT
id,
name,
databaseCacheRetention,
databaseRetention,
provisioningState,
state,
stateReason,
storageOutputRetention,
systemData,
type,
visualizationUrl
FROM azure.networkanalytics.data_types
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_product_name = '{{ data_product_name }}' -- required
AND data_type_name = '{{ data_type_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_data_product">

List data type by parent resource.

```sql
SELECT
id,
name,
databaseCacheRetention,
databaseRetention,
provisioningState,
state,
stateReason,
storageOutputRetention,
systemData,
type,
visualizationUrl
FROM azure.networkanalytics.data_types
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_product_name = '{{ data_product_name }}' -- required
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

Create data type resource.

```sql
INSERT INTO azure.networkanalytics.data_types (
properties,
resource_group_name,
data_product_name,
data_type_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ data_product_name }}',
'{{ data_type_name }}',
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
- name: data_types
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_types resource.
    - name: data_product_name
      value: "{{ data_product_name }}"
      description: Required parameter for the data_types resource.
    - name: data_type_name
      value: "{{ data_type_name }}"
      description: Required parameter for the data_types resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_types resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        state: "{{ state }}"
        stateReason: "{{ stateReason }}"
        storageOutputRetention: {{ storageOutputRetention }}
        databaseCacheRetention: {{ databaseCacheRetention }}
        databaseRetention: {{ databaseRetention }}
        visualizationUrl: "{{ visualizationUrl }}"
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

Update data type resource.

```sql
UPDATE azure.networkanalytics.data_types
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND data_product_name = '{{ data_product_name }}' --required
AND data_type_name = '{{ data_type_name }}' --required
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

Delete data type resource.

```sql
DELETE FROM azure.networkanalytics.data_types
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND data_product_name = '{{ data_product_name }}' --required
AND data_type_name = '{{ data_type_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete_data"
    values={[
        { label: 'delete_data', value: 'delete_data' },
        { label: 'generate_storage_container_sas_token', value: 'generate_storage_container_sas_token' }
    ]}
>
<TabItem value="delete_data">

Delete data for data type.

```sql
EXEC azure.networkanalytics.data_types.delete_data 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_product_name='{{ data_product_name }}' --required, 
@data_type_name='{{ data_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_storage_container_sas_token">

Generate sas token for storage container.

```sql
EXEC azure.networkanalytics.data_types.generate_storage_container_sas_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_product_name='{{ data_product_name }}' --required, 
@data_type_name='{{ data_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startTimeStamp": "{{ startTimeStamp }}", 
"expiryTimeStamp": "{{ expiryTimeStamp }}", 
"ipAddress": "{{ ipAddress }}"
}'
;
```
</TabItem>
</Tabs>
