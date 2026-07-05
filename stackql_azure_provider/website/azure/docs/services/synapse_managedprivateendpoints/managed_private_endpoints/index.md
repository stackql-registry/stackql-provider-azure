--- 
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - synapse_managedprivateendpoints
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

Creates, updates, deletes, gets or lists a <code>managed_private_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_private_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_managedprivateendpoints.managed_private_endpoints" /></td></tr>
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionState" /></td>
    <td><code>object</code></td>
    <td>The connection state of a managed private endpoint. Variables are only populated by the server, and will be ignored when sending a request.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isReserved" /></td>
    <td><code>boolean</code></td>
    <td>Denotes whether the managed private endpoint is reserved.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The managed private endpoint provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
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
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>The link to the next page of results, if any remaining results exist.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#parameter-managed_private_endpoint_name"><code>managed_private_endpoint_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-managed_virtual_network_name"><code>managed_virtual_network_name</code></a></td>
    <td></td>
    <td>Get Managed Private Endpoints.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-managed_virtual_network_name"><code>managed_virtual_network_name</code></a></td>
    <td></td>
    <td>List Managed Private Endpoints.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-managed_private_endpoint_name"><code>managed_private_endpoint_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-managed_virtual_network_name"><code>managed_virtual_network_name</code></a></td>
    <td></td>
    <td>Create Managed Private Endpoints.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-managed_private_endpoint_name"><code>managed_private_endpoint_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-managed_virtual_network_name"><code>managed_virtual_network_name</code></a></td>
    <td></td>
    <td>Delete Managed Private Endpoints.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-managed_private_endpoint_name">
    <td><CopyableCode code="managed_private_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Managed private endpoint name.</td>
</tr>
<tr id="parameter-managed_virtual_network_name">
    <td><CopyableCode code="managed_virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>Managed virtual network name.</td>
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

Get Managed Private Endpoints.

```sql
SELECT
id,
name,
connectionState,
fqdns,
groupId,
isCompliant,
isReserved,
privateLinkResourceId,
provisioningState,
type
FROM azure.synapse_managedprivateendpoints.managed_private_endpoints
WHERE managed_private_endpoint_name = '{{ managed_private_endpoint_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND managed_virtual_network_name = '{{ managed_virtual_network_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Managed Private Endpoints.

```sql
SELECT
nextLink,
value
FROM azure.synapse_managedprivateendpoints.managed_private_endpoints
WHERE endpoint = '{{ endpoint }}' -- required
AND managed_virtual_network_name = '{{ managed_virtual_network_name }}' -- required
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

Create Managed Private Endpoints.

```sql
INSERT INTO azure.synapse_managedprivateendpoints.managed_private_endpoints (
properties,
managed_private_endpoint_name,
endpoint,
managed_virtual_network_name
)
SELECT 
'{{ properties }}',
'{{ managed_private_endpoint_name }}',
'{{ endpoint }}',
'{{ managed_virtual_network_name }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: managed_private_endpoints
  props:
    - name: managed_private_endpoint_name
      value: "{{ managed_private_endpoint_name }}"
      description: Required parameter for the managed_private_endpoints resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the managed_private_endpoints resource.
    - name: managed_virtual_network_name
      value: "{{ managed_virtual_network_name }}"
      description: Required parameter for the managed_private_endpoints resource.
    - name: properties
      description: |
        Properties of a managed private endpoint. Variables are only populated by the server, and will be ignored when sending a request.
      value:
        name: "{{ name }}"
        privateLinkResourceId: "{{ privateLinkResourceId }}"
        groupId: "{{ groupId }}"
        provisioningState: "{{ provisioningState }}"
        connectionState:
          status: "{{ status }}"
          description: "{{ description }}"
          actionsRequired: "{{ actionsRequired }}"
        isReserved: {{ isReserved }}
        fqdns:
          - "{{ fqdns }}"
        isCompliant: {{ isCompliant }}
`}</CodeBlock>

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

Delete Managed Private Endpoints.

```sql
DELETE FROM azure.synapse_managedprivateendpoints.managed_private_endpoints
WHERE managed_private_endpoint_name = '{{ managed_private_endpoint_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND managed_virtual_network_name = '{{ managed_virtual_network_name }}' --required
;
```
</TabItem>
</Tabs>
