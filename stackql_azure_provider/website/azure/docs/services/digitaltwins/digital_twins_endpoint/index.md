--- 
title: digital_twins_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - digital_twins_endpoint
  - digitaltwins
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

Creates, updates, deletes, gets or lists a <code>digital_twins_endpoint</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="digital_twins_endpoint" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digitaltwins.digital_twins_endpoint" /></td></tr>
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
    <td>The resource identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Extension resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationType" /></td>
    <td><code>string</code></td>
    <td>Specifies the authentication type being used for connecting to the endpoint. Defaults to 'KeyBased'. If 'KeyBased' is selected, a connection string must be specified (at least the primary connection string). If 'IdentityBased' is select, the endpointUri and entityPath properties must be specified. Known values are: "KeyBased" and "IdentityBased".</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the Endpoint was added to DigitalTwinsInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetterSecret" /></td>
    <td><code>string</code></td>
    <td>Dead letter storage secret for key-based authentication. Will be obfuscated during read.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetterUri" /></td>
    <td><code>string</code></td>
    <td>Dead letter storage URL for identity-based authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointType" /></td>
    <td><code>string</code></td>
    <td>The type of Digital Twins endpoint. Required. Known values are: "EventHub", "EventGrid", and "ServiceBus".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed identity properties for the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Provisioning", "Deleting", "Updating", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring", "Moving", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td>The resource identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Extension resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationType" /></td>
    <td><code>string</code></td>
    <td>Specifies the authentication type being used for connecting to the endpoint. Defaults to 'KeyBased'. If 'KeyBased' is selected, a connection string must be specified (at least the primary connection string). If 'IdentityBased' is select, the endpointUri and entityPath properties must be specified. Known values are: "KeyBased" and "IdentityBased".</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the Endpoint was added to DigitalTwinsInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetterSecret" /></td>
    <td><code>string</code></td>
    <td>Dead letter storage secret for key-based authentication. Will be obfuscated during read.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetterUri" /></td>
    <td><code>string</code></td>
    <td>Dead letter storage URL for identity-based authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointType" /></td>
    <td><code>string</code></td>
    <td>The type of Digital Twins endpoint. Required. Known values are: "EventHub", "EventGrid", and "ServiceBus".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed identity properties for the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Provisioning", "Deleting", "Updating", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring", "Moving", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get DigitalTwinsInstances Endpoint.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get DigitalTwinsInstance Endpoints.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update DigitalTwinsInstance endpoint.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update DigitalTwinsInstance endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a DigitalTwinsInstance endpoint.</td>
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
    <td>Name of Endpoint Resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the DigitalTwinsInstance. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DigitalTwinsInstance. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get DigitalTwinsInstances Endpoint.

```sql
SELECT
id,
name,
authenticationType,
createdTime,
deadLetterSecret,
deadLetterUri,
endpointType,
identity,
provisioningState,
systemData,
type
FROM azure.digitaltwins.digital_twins_endpoint
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get DigitalTwinsInstance Endpoints.

```sql
SELECT
id,
name,
authenticationType,
createdTime,
deadLetterSecret,
deadLetterUri,
endpointType,
identity,
provisioningState,
systemData,
type
FROM azure.digitaltwins.digital_twins_endpoint
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Create or update DigitalTwinsInstance endpoint.

```sql
INSERT INTO azure.digitaltwins.digital_twins_endpoint (
properties,
resource_group_name,
resource_name,
endpoint_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ endpoint_name }}',
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
- name: digital_twins_endpoint
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the digital_twins_endpoint resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the digital_twins_endpoint resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the digital_twins_endpoint resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the digital_twins_endpoint resource.
    - name: properties
      description: |
        DigitalTwinsInstance endpoint resource properties. Required.
      value:
        endpointType: "{{ endpointType }}"
        provisioningState: "{{ provisioningState }}"
        createdTime: "{{ createdTime }}"
        authenticationType: "{{ authenticationType }}"
        deadLetterSecret: "{{ deadLetterSecret }}"
        deadLetterUri: "{{ deadLetterUri }}"
        identity:
          type: "{{ type }}"
          userAssignedIdentity: "{{ userAssignedIdentity }}"
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

Create or update DigitalTwinsInstance endpoint.

```sql
REPLACE azure.digitaltwins.digital_twins_endpoint
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Delete a DigitalTwinsInstance endpoint.

```sql
DELETE FROM azure.digitaltwins.digital_twins_endpoint
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
