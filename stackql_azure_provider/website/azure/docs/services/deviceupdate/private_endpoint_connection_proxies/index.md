--- 
title: private_endpoint_connection_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_proxies
  - deviceupdate
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connection_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_endpoint_connection_proxies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.deviceupdate.private_endpoint_connection_proxies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_account', value: 'list_by_account' }
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
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>ETag from NRP.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private endpoint connection proxy resource. Known values are: "Succeeded", "Creating", "Deleting", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="remotePrivateEndpoint" /></td>
    <td><code>object</code></td>
    <td>Remote private endpoint details.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status.</td>
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
<TabItem value="list_by_account">

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
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>ETag from NRP.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private endpoint connection proxy resource. Known values are: "Succeeded", "Creating", "Deleting", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="remotePrivateEndpoint" /></td>
    <td><code>object</code></td>
    <td>Remote private endpoint details.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-private_endpoint_connection_proxy_id"><code>private_endpoint_connection_proxy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>(INTERNAL - DO NOT USE) Get the specified private endpoint connection proxy associated with the device update account.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>(INTERNAL - DO NOT USE) List all private endpoint connection proxies in a device update account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-private_endpoint_connection_proxy_id"><code>private_endpoint_connection_proxy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>(INTERNAL - DO NOT USE) Creates or updates the specified private endpoint connection proxy resource associated with the device update account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-private_endpoint_connection_proxy_id"><code>private_endpoint_connection_proxy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>(INTERNAL - DO NOT USE) Creates or updates the specified private endpoint connection proxy resource associated with the device update account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-private_endpoint_connection_proxy_id"><code>private_endpoint_connection_proxy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>(INTERNAL - DO NOT USE) Deletes the specified private endpoint connection proxy associated with the device update account.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-private_endpoint_connection_proxy_id"><code>private_endpoint_connection_proxy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>(INTERNAL - DO NOT USE) Validates a private endpoint connection proxy object.</td>
</tr>
<tr>
    <td><a href="#update_private_endpoint_properties"><CopyableCode code="update_private_endpoint_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-private_endpoint_connection_proxy_id"><code>private_endpoint_connection_proxy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>(INTERNAL - DO NOT USE) Updates a private endpoint inside the private endpoint connection proxy object.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>Account name. Required.</td>
</tr>
<tr id="parameter-private_endpoint_connection_proxy_id">
    <td><CopyableCode code="private_endpoint_connection_proxy_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the private endpoint connection proxy object. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
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
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get">

(INTERNAL - DO NOT USE) Get the specified private endpoint connection proxy associated with the device update account.

```sql
SELECT
id,
name,
eTag,
provisioningState,
remotePrivateEndpoint,
status,
systemData,
type
FROM azure.deviceupdate.private_endpoint_connection_proxies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND private_endpoint_connection_proxy_id = '{{ private_endpoint_connection_proxy_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

(INTERNAL - DO NOT USE) List all private endpoint connection proxies in a device update account.

```sql
SELECT
id,
name,
eTag,
provisioningState,
remotePrivateEndpoint,
status,
systemData,
type
FROM azure.deviceupdate.private_endpoint_connection_proxies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
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

(INTERNAL - DO NOT USE) Creates or updates the specified private endpoint connection proxy resource associated with the device update account.

```sql
INSERT INTO azure.deviceupdate.private_endpoint_connection_proxies (
remotePrivateEndpoint,
status,
resource_group_name,
account_name,
private_endpoint_connection_proxy_id,
subscription_id
)
SELECT 
'{{ remotePrivateEndpoint }}',
'{{ status }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ private_endpoint_connection_proxy_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
properties,
remotePrivateEndpoint,
status,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: private_endpoint_connection_proxies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the private_endpoint_connection_proxies resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the private_endpoint_connection_proxies resource.
    - name: private_endpoint_connection_proxy_id
      value: "{{ private_endpoint_connection_proxy_id }}"
      description: Required parameter for the private_endpoint_connection_proxies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the private_endpoint_connection_proxies resource.
    - name: remotePrivateEndpoint
      description: |
        Remote private endpoint details.
      value:
        id: "{{ id }}"
        location: "{{ location }}"
        immutableSubscriptionId: "{{ immutableSubscriptionId }}"
        immutableResourceId: "{{ immutableResourceId }}"
        vnetTrafficTag: "{{ vnetTrafficTag }}"
        manualPrivateLinkServiceConnections:
          - name: "{{ name }}"
            groupIds: "{{ groupIds }}"
            requestMessage: "{{ requestMessage }}"
        privateLinkServiceConnections:
          - name: "{{ name }}"
            groupIds: "{{ groupIds }}"
            requestMessage: "{{ requestMessage }}"
        privateLinkServiceProxies:
          - id: "{{ id }}"
            remotePrivateLinkServiceConnectionState:
              status: "{{ status }}"
              description: "{{ description }}"
              actionsRequired: "{{ actionsRequired }}"
            remotePrivateEndpointConnection:
              id: "{{ id }}"
            groupConnectivityInformation: "{{ groupConnectivityInformation }}"
        connectionDetails:
          - id: "{{ id }}"
            privateIpAddress: "{{ privateIpAddress }}"
            linkIdentifier: "{{ linkIdentifier }}"
            groupId: "{{ groupId }}"
            memberName: "{{ memberName }}"
    - name: status
      value: "{{ status }}"
      description: |
        Operation status.
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

(INTERNAL - DO NOT USE) Creates or updates the specified private endpoint connection proxy resource associated with the device update account.

```sql
REPLACE azure.deviceupdate.private_endpoint_connection_proxies
SET 
remotePrivateEndpoint = '{{ remotePrivateEndpoint }}',
status = '{{ status }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND private_endpoint_connection_proxy_id = '{{ private_endpoint_connection_proxy_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
properties,
remotePrivateEndpoint,
status,
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

(INTERNAL - DO NOT USE) Deletes the specified private endpoint connection proxy associated with the device update account.

```sql
DELETE FROM azure.deviceupdate.private_endpoint_connection_proxies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND private_endpoint_connection_proxy_id = '{{ private_endpoint_connection_proxy_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate"
    values={[
        { label: 'validate', value: 'validate' },
        { label: 'update_private_endpoint_properties', value: 'update_private_endpoint_properties' }
    ]}
>
<TabItem value="validate">

(INTERNAL - DO NOT USE) Validates a private endpoint connection proxy object.

```sql
EXEC azure.deviceupdate.private_endpoint_connection_proxies.validate 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@private_endpoint_connection_proxy_id='{{ private_endpoint_connection_proxy_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"remotePrivateEndpoint": "{{ remotePrivateEndpoint }}", 
"status": "{{ status }}"
}'
;
```
</TabItem>
<TabItem value="update_private_endpoint_properties">

(INTERNAL - DO NOT USE) Updates a private endpoint inside the private endpoint connection proxy object.

```sql
EXEC azure.deviceupdate.private_endpoint_connection_proxies.update_private_endpoint_properties 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@private_endpoint_connection_proxy_id='{{ private_endpoint_connection_proxy_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"location": "{{ location }}", 
"immutableSubscriptionId": "{{ immutableSubscriptionId }}", 
"immutableResourceId": "{{ immutableResourceId }}", 
"vnetTrafficTag": "{{ vnetTrafficTag }}"
}'
;
```
</TabItem>
</Tabs>
