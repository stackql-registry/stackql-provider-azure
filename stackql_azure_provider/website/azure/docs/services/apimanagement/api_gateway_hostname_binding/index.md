--- 
title: api_gateway_hostname_binding
hide_title: false
hide_table_of_contents: false
keywords:
  - api_gateway_hostname_binding
  - apimanagement
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

Creates, updates, deletes, gets or lists an <code>api_gateway_hostname_binding</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="api_gateway_hostname_binding" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.apimanagement.api_gateway_hostname_binding" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_gateway', value: 'list_by_gateway' }
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
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>The hostnames of the data-plane gateway to which requests can be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The default hostname of the data-plane gateway. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVault" /></td>
    <td><code>object</code></td>
    <td>The link to the API Management service workspace. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the API Management gateway hostname binding.</td>
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
<TabItem value="list_by_gateway">

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
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>The hostnames of the data-plane gateway to which requests can be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The default hostname of the data-plane gateway. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVault" /></td>
    <td><code>object</code></td>
    <td>The link to the API Management service workspace. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the API Management gateway hostname binding.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-hostname_binding_name"><code>hostname_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an API Management gateway hostname binding resource description.</td>
</tr>
<tr>
    <td><a href="#list_by_gateway"><CopyableCode code="list_by_gateway" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all API Management gateway hostname bindings within a gateway.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-hostname_binding_name"><code>hostname_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an API Management gateway hostname binding. This is long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-hostname_binding_name"><code>hostname_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an API Management gateway hostname binding. This is long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-hostname_binding_name"><code>hostname_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing API Management gateway hostname binding.</td>
</tr>
<tr>
    <td><a href="#refresh_secret"><CopyableCode code="refresh_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-hostname_binding_name"><code>hostname_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refresh the secret for an API Management gateway hostname binding.</td>
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
<tr id="parameter-gateway_name">
    <td><CopyableCode code="gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management gateway. Required.</td>
</tr>
<tr id="parameter-hostname_binding_name">
    <td><CopyableCode code="hostname_binding_name" /></td>
    <td><code>string</code></td>
    <td>Gateway hostname binding identifier. Must be unique in the scope of parent Gateway entity. Required.</td>
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
        { label: 'list_by_gateway', value: 'list_by_gateway' }
    ]}
>
<TabItem value="get">

Gets an API Management gateway hostname binding resource description.

```sql
SELECT
id,
name,
certificate,
etag,
hostname,
keyVault,
provisioningState,
systemData,
type
FROM azure.apimanagement.api_gateway_hostname_binding
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND hostname_binding_name = '{{ hostname_binding_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_gateway">

List all API Management gateway hostname bindings within a gateway.

```sql
SELECT
id,
name,
certificate,
etag,
hostname,
keyVault,
provisioningState,
systemData,
type
FROM azure.apimanagement.api_gateway_hostname_binding
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
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

Creates or updates an API Management gateway hostname binding. This is long running operation and could take several minutes to complete.

```sql
INSERT INTO azure.apimanagement.api_gateway_hostname_binding (
properties,
resource_group_name,
gateway_name,
hostname_binding_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ gateway_name }}',
'{{ hostname_binding_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: api_gateway_hostname_binding
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the api_gateway_hostname_binding resource.
    - name: gateway_name
      value: "{{ gateway_name }}"
      description: Required parameter for the api_gateway_hostname_binding resource.
    - name: hostname_binding_name
      value: "{{ hostname_binding_name }}"
      description: Required parameter for the api_gateway_hostname_binding resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the api_gateway_hostname_binding resource.
    - name: properties
      description: |
        Properties of the API Management gateway hostname binding. Required.
      value:
        provisioningState: "{{ provisioningState }}"
        hostname: "{{ hostname }}"
        keyVault:
          secretId: "{{ secretId }}"
          identityClientId: "{{ identityClientId }}"
          lastStatus:
            code: "{{ code }}"
            timeStampUtc: "{{ timeStampUtc }}"
            lastSuccessTimeStampUtc: "{{ lastSuccessTimeStampUtc }}"
        certificate:
          thumbprint: "{{ thumbprint }}"
          subject: "{{ subject }}"
          expiry: "{{ expiry }}"
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

Creates or updates an API Management gateway hostname binding. This is long running operation and could take several minutes to complete.

```sql
REPLACE azure.apimanagement.api_gateway_hostname_binding
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND hostname_binding_name = '{{ hostname_binding_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
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

Deletes an existing API Management gateway hostname binding.

```sql
DELETE FROM azure.apimanagement.api_gateway_hostname_binding
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND hostname_binding_name = '{{ hostname_binding_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh_secret"
    values={[
        { label: 'refresh_secret', value: 'refresh_secret' }
    ]}
>
<TabItem value="refresh_secret">

Refresh the secret for an API Management gateway hostname binding.

```sql
EXEC azure.apimanagement.api_gateway_hostname_binding.refresh_secret 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@hostname_binding_name='{{ hostname_binding_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
