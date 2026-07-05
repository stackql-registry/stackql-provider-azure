--- 
title: dpp_resource_guard_proxy
hide_title: false
hide_table_of_contents: false
keywords:
  - dpp_resource_guard_proxy
  - dataprotection
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

Creates, updates, deletes, gets or lists a <code>dpp_resource_guard_proxy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dpp_resource_guard_proxy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dataprotection.dpp_resource_guard_proxy" /></td></tr>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string</code></td>
    <td>:vartype last_updated_time: str</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationDetails" /></td>
    <td><code>array</code></td>
    <td>:vartype resource_guard_operation_details: list[~azure.mgmt.dataprotection.models.ResourceGuardOperationDetail]</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardResourceId" /></td>
    <td><code>string</code></td>
    <td>:vartype resource_guard_resource_id: str</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string</code></td>
    <td>:vartype last_updated_time: str</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationDetails" /></td>
    <td><code>array</code></td>
    <td>:vartype resource_guard_operation_details: list[~azure.mgmt.dataprotection.models.ResourceGuardOperationDetail]</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardResourceId" /></td>
    <td><code>string</code></td>
    <td>:vartype resource_guard_resource_id: str</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_guard_proxy_name"><code>resource_guard_proxy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the ResourceGuardProxy object associated with the vault, and that matches the name in the request.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the list of ResourceGuardProxies associated with the vault.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_guard_proxy_name"><code>resource_guard_proxy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a ResourceGuardProxy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_guard_proxy_name"><code>resource_guard_proxy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a ResourceGuardProxy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_guard_proxy_name"><code>resource_guard_proxy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the ResourceGuardProxy.</td>
</tr>
<tr>
    <td><a href="#unlock_delete"><CopyableCode code="unlock_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_guard_proxy_name"><code>resource_guard_proxy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>UnlockDelete call for ResourceGuardProxy, executed before one can delete it.</td>
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
<tr id="parameter-resource_guard_proxy_name">
    <td><CopyableCode code="resource_guard_proxy_name" /></td>
    <td><code>string</code></td>
    <td>name of the resource guard proxy. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the backup vault. Required.</td>
</tr>
<tr id="parameter-x-ms-authorization-auxiliary">
    <td><CopyableCode code="x-ms-authorization-auxiliary" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
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

Returns the ResourceGuardProxy object associated with the vault, and that matches the name in the request.

```sql
SELECT
id,
name,
description,
lastUpdatedTime,
resourceGuardOperationDetails,
resourceGuardResourceId,
systemData,
type
FROM azure.dataprotection.dpp_resource_guard_proxy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND resource_guard_proxy_name = '{{ resource_guard_proxy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns the list of ResourceGuardProxies associated with the vault.

```sql
SELECT
id,
name,
description,
lastUpdatedTime,
resourceGuardOperationDetails,
resourceGuardResourceId,
systemData,
type
FROM azure.dataprotection.dpp_resource_guard_proxy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
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

Creates or Updates a ResourceGuardProxy.

```sql
INSERT INTO azure.dataprotection.dpp_resource_guard_proxy (
properties,
resource_group_name,
vault_name,
resource_guard_proxy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ vault_name }}',
'{{ resource_guard_proxy_name }}',
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
- name: dpp_resource_guard_proxy
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dpp_resource_guard_proxy resource.
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the dpp_resource_guard_proxy resource.
    - name: resource_guard_proxy_name
      value: "{{ resource_guard_proxy_name }}"
      description: Required parameter for the dpp_resource_guard_proxy resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dpp_resource_guard_proxy resource.
    - name: properties
      description: |
        ResourceGuardProxyBaseResource properties.
      value:
        resourceGuardResourceId: "{{ resourceGuardResourceId }}"
        resourceGuardOperationDetails:
          - vaultCriticalOperation: "{{ vaultCriticalOperation }}"
            defaultResourceRequest: "{{ defaultResourceRequest }}"
        lastUpdatedTime: "{{ lastUpdatedTime }}"
        description: "{{ description }}"
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

Creates or Updates a ResourceGuardProxy.

```sql
REPLACE azure.dataprotection.dpp_resource_guard_proxy
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND resource_guard_proxy_name = '{{ resource_guard_proxy_name }}' --required
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

Deletes the ResourceGuardProxy.

```sql
DELETE FROM azure.dataprotection.dpp_resource_guard_proxy
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND resource_guard_proxy_name = '{{ resource_guard_proxy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="unlock_delete"
    values={[
        { label: 'unlock_delete', value: 'unlock_delete' }
    ]}
>
<TabItem value="unlock_delete">

UnlockDelete call for ResourceGuardProxy, executed before one can delete it.

```sql
EXEC azure.dataprotection.dpp_resource_guard_proxy.unlock_delete 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@resource_guard_proxy_name='{{ resource_guard_proxy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@x-ms-authorization-auxiliary='{{ x-ms-authorization-auxiliary }}' 
@@json=
'{
"resourceGuardOperationRequests": "{{ resourceGuardOperationRequests }}", 
"resourceToBeDeleted": "{{ resourceToBeDeleted }}"
}'
;
```
</TabItem>
</Tabs>
