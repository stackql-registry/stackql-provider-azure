--- 
title: workspace_api_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_schema
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_api_schema</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_api_schema" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_schema" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_api', value: 'list_by_api' }
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
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml` - `OData Schema` use `application/vnd.ms-azure-apim.odata.schema` - `gRPC Schema` use `text/protobuf`. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="document" /></td>
    <td><code>object</code></td>
    <td>Create or update Properties of the API Schema Document. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
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
<TabItem value="list_by_api">

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
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml` - `OData Schema` use `application/vnd.ms-azure-apim.odata.schema` - `gRPC Schema` use `text/protobuf`. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="document" /></td>
    <td><code>object</code></td>
    <td>Create or update Properties of the API Schema Document. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the schema configuration at the API level.</td>
</tr>
<tr>
    <td><a href="#list_by_api"><CopyableCode code="list_by_api" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Get the schema configuration at the API level.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates schema configuration for the API.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates schema configuration for the API.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes the schema configuration at the Api.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the entity state (Etag) version of the schema specified by its identifier.</td>
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
<tr id="parameter-api_id">
    <td><CopyableCode code="api_id" /></td>
    <td><code>string</code></td>
    <td>API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-schema_id">
    <td><CopyableCode code="schema_id" /></td>
    <td><code>string</code></td>
    <td>Schema id identifier. Must be unique in the current API Management service instance. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>string</code></td>
    <td>Workspace identifier. Must be unique in the current API Management service instance. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>| Field | Usage | Supported operators | Supported functions ||-------------|-------------|-------------|-------------|| contentType | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of records to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of records to return. Default value is None.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>If true removes all references to the schema before deleting it. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_api', value: 'list_by_api' }
    ]}
>
<TabItem value="get">

Get the schema configuration at the API level.

```sql
SELECT
id,
name,
contentType,
document,
provisioningState,
systemData,
type
FROM azure.api_management.workspace_api_schema
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
AND api_id = '{{ api_id }}' -- required
AND schema_id = '{{ schema_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_api">

Get the schema configuration at the API level.

```sql
SELECT
id,
name,
contentType,
document,
provisioningState,
systemData,
type
FROM azure.api_management.workspace_api_schema
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
AND api_id = '{{ api_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
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

Creates or updates schema configuration for the API.

```sql
INSERT INTO azure.api_management.workspace_api_schema (
properties,
resource_group_name,
service_name,
workspace_id,
api_id,
schema_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ workspace_id }}',
'{{ api_id }}',
'{{ schema_id }}',
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
- name: workspace_api_schema
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspace_api_schema resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the workspace_api_schema resource.
    - name: workspace_id
      value: "{{ workspace_id }}"
      description: Required parameter for the workspace_api_schema resource.
    - name: api_id
      value: "{{ api_id }}"
      description: Required parameter for the workspace_api_schema resource.
    - name: schema_id
      value: "{{ schema_id }}"
      description: Required parameter for the workspace_api_schema resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspace_api_schema resource.
    - name: properties
      description: |
        Properties of the API Schema.
      value:
        contentType: "{{ contentType }}"
        document:
          value: "{{ value }}"
          definitions: "{{ definitions }}"
          components: "{{ components }}"
        provisioningState: "{{ provisioningState }}"
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

Creates or updates schema configuration for the API.

```sql
REPLACE azure.api_management.workspace_api_schema
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND api_id = '{{ api_id }}' --required
AND schema_id = '{{ schema_id }}' --required
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

Deletes the schema configuration at the Api.

```sql
DELETE FROM azure.api_management.workspace_api_schema
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND api_id = '{{ api_id }}' --required
AND schema_id = '{{ schema_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_entity_tag"
    values={[
        { label: 'get_entity_tag', value: 'get_entity_tag' }
    ]}
>
<TabItem value="get_entity_tag">

Gets the entity state (Etag) version of the schema specified by its identifier.

```sql
EXEC azure.api_management.workspace_api_schema.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@workspace_id='{{ workspace_id }}' --required, 
@api_id='{{ api_id }}' --required, 
@schema_id='{{ schema_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
