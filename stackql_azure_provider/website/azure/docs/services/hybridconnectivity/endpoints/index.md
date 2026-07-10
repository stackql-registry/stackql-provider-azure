--- 
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - hybridconnectivity
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

Creates, updates, deletes, gets or lists an <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridconnectivity.endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_managed_proxy_details"
    values={[
        { label: 'list_managed_proxy_details', value: 'list_managed_proxy_details' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_managed_proxy_details">

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
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>integer</code></td>
    <td>The expiration time of short lived proxy name in unix epoch. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="proxy" /></td>
    <td><code>string</code></td>
    <td>The short lived proxy name. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>The resource provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the connectivity endpoint (optional).</td>
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the connectivity endpoint (optional).</td>
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
    <td><a href="#list_managed_proxy_details"><CopyableCode code="list_managed_proxy_details" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td></td>
    <td>Fetches the managed proxy details.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td></td>
    <td>Gets the endpoint to the resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>List of endpoints to the target resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td></td>
    <td>Create or update the endpoint to the target resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td></td>
    <td>Update the endpoint to the target resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td></td>
    <td>Create or update the endpoint to the target resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td></td>
    <td>Deletes the endpoint access to the target resource.</td>
</tr>
<tr>
    <td><a href="#list_credentials"><CopyableCode code="list_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td><a href="#parameter-expiresin"><code>expiresin</code></a></td>
    <td>Gets the endpoint access credentials to the resource.</td>
</tr>
<tr>
    <td><a href="#list_ingress_gateway_credentials"><CopyableCode code="list_ingress_gateway_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td><a href="#parameter-expiresin"><code>expiresin</code></a></td>
    <td>Gets the ingress gateway endpoint credentials.</td>
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
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The endpoint name. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-expiresin">
    <td><CopyableCode code="expiresin" /></td>
    <td><code>integer</code></td>
    <td>The is how long the endpoint access token is valid (in seconds). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_managed_proxy_details"
    values={[
        { label: 'list_managed_proxy_details', value: 'list_managed_proxy_details' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_managed_proxy_details">

Fetches the managed proxy details.

```sql
SELECT
expiresOn,
proxy
FROM azure.hybridconnectivity.endpoints
WHERE resource_uri = '{{ resource_uri }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the endpoint to the resource.

```sql
SELECT
id,
name,
provisioningState,
resourceId,
systemData,
type
FROM azure.hybridconnectivity.endpoints
WHERE resource_uri = '{{ resource_uri }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List of endpoints to the target resource.

```sql
SELECT
id,
name,
provisioningState,
resourceId,
systemData,
type
FROM azure.hybridconnectivity.endpoints
WHERE resource_uri = '{{ resource_uri }}' -- required
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

Create or update the endpoint to the target resource.

```sql
INSERT INTO azure.hybridconnectivity.endpoints (
properties,
resource_uri,
endpoint_name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ endpoint_name }}'
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
- name: endpoints
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the endpoints resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the endpoints resource.
    - name: properties
      description: |
        The endpoint properties.
      value:
        type: "{{ type }}"
        resourceId: "{{ resourceId }}"
        provisioningState: "{{ provisioningState }}"
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

Update the endpoint to the target resource.

```sql
UPDATE azure.hybridconnectivity.endpoints
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
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

Create or update the endpoint to the target resource.

```sql
REPLACE azure.hybridconnectivity.endpoints
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
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

Deletes the endpoint access to the target resource.

```sql
DELETE FROM azure.hybridconnectivity.endpoints
WHERE resource_uri = '{{ resource_uri }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_credentials"
    values={[
        { label: 'list_credentials', value: 'list_credentials' },
        { label: 'list_ingress_gateway_credentials', value: 'list_ingress_gateway_credentials' }
    ]}
>
<TabItem value="list_credentials">

Gets the endpoint access credentials to the resource.

```sql
EXEC azure.hybridconnectivity.endpoints.list_credentials 
@resource_uri='{{ resource_uri }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@expiresin='{{ expiresin }}' 
@@json=
'{
"serviceName": "{{ serviceName }}"
}'
;
```
</TabItem>
<TabItem value="list_ingress_gateway_credentials">

Gets the ingress gateway endpoint credentials.

```sql
EXEC azure.hybridconnectivity.endpoints.list_ingress_gateway_credentials 
@resource_uri='{{ resource_uri }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@expiresin='{{ expiresin }}' 
@@json=
'{
"serviceName": "{{ serviceName }}"
}'
;
```
</TabItem>
</Tabs>
