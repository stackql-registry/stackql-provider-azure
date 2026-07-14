--- 
title: api_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - api_policy
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

Creates, updates, deletes, gets or lists an <code>api_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="api_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_policy" /></td></tr>
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
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format of the policyContent. Known values are: "xml", "xml-link", "rawxml", and "rawxml-link". (xml, xml-link, rawxml, rawxml-link)</td>
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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Contents of the Policy as defined by the format. Required.</td>
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
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format of the policyContent. Known values are: "xml", "xml-link", "rawxml", and "rawxml-link". (xml, xml-link, rawxml, rawxml-link)</td>
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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Contents of the Policy as defined by the format. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a></td>
    <td>Get the policy configuration at the API level.</td>
</tr>
<tr>
    <td><a href="#list_by_api"><CopyableCode code="list_by_api" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the policy configuration at the API level.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates policy configuration for the API.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates policy configuration for the API.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the policy configuration at the Api.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the entity state (Etag) version of the API policy specified by its identifier.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the Policy. "policy" Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Policy Export Format. Known values are: "xml" and "rawxml". Default value is None.</td>
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

Get the policy configuration at the API level.

```sql
SELECT
id,
name,
format,
systemData,
type,
value
FROM azure.api_management.api_policy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND api_id = '{{ api_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND format = '{{ format }}'
;
```
</TabItem>
<TabItem value="list_by_api">

Get the policy configuration at the API level.

```sql
SELECT
id,
name,
format,
systemData,
type,
value
FROM azure.api_management.api_policy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND api_id = '{{ api_id }}' -- required
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

Creates or updates policy configuration for the API.

```sql
INSERT INTO azure.api_management.api_policy (
properties,
resource_group_name,
service_name,
api_id,
policy_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ api_id }}',
'{{ policy_id }}',
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
- name: api_policy
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the api_policy resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the api_policy resource.
    - name: api_id
      value: "{{ api_id }}"
      description: Required parameter for the api_policy resource.
    - name: policy_id
      value: "{{ policy_id }}"
      description: Required parameter for the api_policy resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the api_policy resource.
    - name: properties
      description: |
        Properties of the Policy.
      value:
        value: "{{ value }}"
        format: "{{ format }}"
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

Creates or updates policy configuration for the API.

```sql
REPLACE azure.api_management.api_policy
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND api_id = '{{ api_id }}' --required
AND policy_id = '{{ policy_id }}' --required
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

Deletes the policy configuration at the Api.

```sql
DELETE FROM azure.api_management.api_policy
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND api_id = '{{ api_id }}' --required
AND policy_id = '{{ policy_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Gets the entity state (Etag) version of the API policy specified by its identifier.

```sql
EXEC azure.api_management.api_policy.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@api_id='{{ api_id }}' --required, 
@policy_id='{{ policy_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
