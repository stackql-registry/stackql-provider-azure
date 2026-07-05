--- 
title: test_base_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - test_base_accounts
  - testbase
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>test_base_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_base_accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.test_base_accounts" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="accessLevel" /></td>
    <td><code>string</code></td>
    <td>The access level of the Test Base Account.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Cancelled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Describes a Test Base Account SKU. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="accessLevel" /></td>
    <td><code>string</code></td>
    <td>The access level of the Test Base Account.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Cancelled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Describes a Test Base Account SKU. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="accessLevel" /></td>
    <td><code>string</code></td>
    <td>The access level of the Test Base Account.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Cancelled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Describes a Test Base Account SKU. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Test Base Account.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-getDeleted"><code>getDeleted</code></a></td>
    <td>Lists all the Test Base Accounts in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-getDeleted"><code>getDeleted</code></a></td>
    <td>Lists all the Test Base Accounts in a subscription. This API is required by ARM guidelines.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-restore"><code>restore</code></a></td>
    <td>Create or replace (overwrite/recreate, with potential downtime) a Test Base Account in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing Test Base Account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Test Base Account.</td>
</tr>
<tr>
    <td><a href="#get_file_upload_url"><CopyableCode code="get_file_upload_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the file upload URL of a Test Base Account.</td>
</tr>
<tr>
    <td><a href="#offboard"><CopyableCode code="offboard" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Offboard a Test Base Account.</td>
</tr>
<tr>
    <td><a href="#check_package_name_availability"><CopyableCode code="check_package_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-applicationName"><code>applicationName</code></a>, <a href="#parameter-version"><code>version</code></a></td>
    <td></td>
    <td>Checks that the Test Base Package name and version is valid and is not already in use.</td>
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
    <td>The name of the resource group that contains the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-test_base_account_name">
    <td><CopyableCode code="test_base_account_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the Test Base Account. Required.</td>
</tr>
<tr id="parameter-getDeleted">
    <td><CopyableCode code="getDeleted" /></td>
    <td><code>boolean</code></td>
    <td>The flag indicating if we need to include the Test Base Accounts which were soft deleted before. Default value is None.</td>
</tr>
<tr id="parameter-restore">
    <td><CopyableCode code="restore" /></td>
    <td><code>boolean</code></td>
    <td>The flag indicating if we would like to restore the Test Base Accounts which were soft deleted before. Default value is None.</td>
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

Gets a Test Base Account.

```sql
SELECT
id,
name,
accessLevel,
etag,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure_extras.testbase.test_base_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the Test Base Accounts in a resource group.

```sql
SELECT
id,
name,
accessLevel,
etag,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure_extras.testbase.test_base_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND getDeleted = '{{ getDeleted }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all the Test Base Accounts in a subscription. This API is required by ARM guidelines.

```sql
SELECT
id,
name,
accessLevel,
etag,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure_extras.testbase.test_base_accounts
WHERE subscription_id = '{{ subscription_id }}' -- required
AND getDeleted = '{{ getDeleted }}'
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

Create or replace (overwrite/recreate, with potential downtime) a Test Base Account in the specified subscription.

```sql
INSERT INTO azure_extras.testbase.test_base_accounts (
tags,
location,
properties,
resource_group_name,
test_base_account_name,
subscription_id,
restore
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ test_base_account_name }}',
'{{ subscription_id }}',
'{{ restore }}'
RETURNING
id,
name,
etag,
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
- name: test_base_accounts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the test_base_accounts resource.
    - name: test_base_account_name
      value: "{{ test_base_account_name }}"
      description: Required parameter for the test_base_accounts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the test_base_accounts resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags of the resource.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        sku:
          resourceType: "{{ resourceType }}"
          name: "{{ name }}"
          tier: "{{ tier }}"
          capabilities:
            - name: "{{ name }}"
              value: "{{ value }}"
          locations:
            - "{{ locations }}"
    - name: restore
      value: {{ restore }}
      description: The flag indicating if we would like to restore the Test Base Accounts which were soft deleted before. Default value is None.
      description: The flag indicating if we would like to restore the Test Base Accounts which were soft deleted before. Default value is None.
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

Update an existing Test Base Account.

```sql
UPDATE azure_extras.testbase.test_base_accounts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND test_base_account_name = '{{ test_base_account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Deletes a Test Base Account.

```sql
DELETE FROM azure_extras.testbase.test_base_accounts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND test_base_account_name = '{{ test_base_account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_file_upload_url"
    values={[
        { label: 'get_file_upload_url', value: 'get_file_upload_url' },
        { label: 'offboard', value: 'offboard' },
        { label: 'check_package_name_availability', value: 'check_package_name_availability' }
    ]}
>
<TabItem value="get_file_upload_url">

Gets the file upload URL of a Test Base Account.

```sql
EXEC azure_extras.testbase.test_base_accounts.get_file_upload_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"blobName": "{{ blobName }}"
}'
;
```
</TabItem>
<TabItem value="offboard">

Offboard a Test Base Account.

```sql
EXEC azure_extras.testbase.test_base_accounts.offboard 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_package_name_availability">

Checks that the Test Base Package name and version is valid and is not already in use.

```sql
EXEC azure_extras.testbase.test_base_accounts.check_package_name_availability 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"applicationName": "{{ applicationName }}", 
"version": "{{ version }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
