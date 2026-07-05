--- 
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
  - confluent
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>connector</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connector" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.connector" /></td></tr>
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
    <td><CopyableCode code="connectorBasicInfo" /></td>
    <td><code>object</code></td>
    <td>Connector Info Base.</td>
</tr>
<tr>
    <td><CopyableCode code="connectorServiceTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Connector Service type info base properties.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerConnectorInfo" /></td>
    <td><code>object</code></td>
    <td>The connection information consumed by applications.</td>
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
    <td><CopyableCode code="connectorBasicInfo" /></td>
    <td><code>object</code></td>
    <td>Connector Info Base.</td>
</tr>
<tr>
    <td><CopyableCode code="connectorServiceTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Connector Service type info base properties.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerConnectorInfo" /></td>
    <td><code>object</code></td>
    <td>The connection information consumed by applications.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get confluent connector by Name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-pageToken"><code>pageToken</code></a></td>
    <td>Lists all the connectors in a cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create confluent connector by Name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create confluent connector by Name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete confluent connector by name.</td>
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
<tr id="parameter-cluster_id">
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td>Confluent kafka or schema registry cluster id. Required.</td>
</tr>
<tr id="parameter-connector_name">
    <td><CopyableCode code="connector_name" /></td>
    <td><code>string</code></td>
    <td>Confluent connector name. Required.</td>
</tr>
<tr id="parameter-environment_id">
    <td><CopyableCode code="environment_id" /></td>
    <td><code>string</code></td>
    <td>Confluent environment id. Required.</td>
</tr>
<tr id="parameter-organization_name">
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Organization resource name. Required.</td>
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
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Pagination size. Default value is None.</td>
</tr>
<tr id="parameter-pageToken">
    <td><CopyableCode code="pageToken" /></td>
    <td><code>string</code></td>
    <td>An opaque pagination token to fetch the next set of records. Default value is None.</td>
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

Get confluent connector by Name.

```sql
SELECT
id,
name,
connectorBasicInfo,
connectorServiceTypeInfo,
partnerConnectorInfo,
systemData,
type
FROM azure_isv.confluent.connector
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
AND environment_id = '{{ environment_id }}' -- required
AND cluster_id = '{{ cluster_id }}' -- required
AND connector_name = '{{ connector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the connectors in a cluster.

```sql
SELECT
id,
name,
connectorBasicInfo,
connectorServiceTypeInfo,
partnerConnectorInfo,
systemData,
type
FROM azure_isv.confluent.connector
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
AND environment_id = '{{ environment_id }}' -- required
AND cluster_id = '{{ cluster_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND pageToken = '{{ pageToken }}'
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

Create confluent connector by Name.

```sql
INSERT INTO azure_isv.confluent.connector (
properties,
resource_group_name,
organization_name,
environment_id,
cluster_id,
connector_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ organization_name }}',
'{{ environment_id }}',
'{{ cluster_id }}',
'{{ connector_name }}',
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
- name: connector
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connector resource.
    - name: organization_name
      value: "{{ organization_name }}"
      description: Required parameter for the connector resource.
    - name: environment_id
      value: "{{ environment_id }}"
      description: Required parameter for the connector resource.
    - name: cluster_id
      value: "{{ cluster_id }}"
      description: Required parameter for the connector resource.
    - name: connector_name
      value: "{{ connector_name }}"
      description: Required parameter for the connector resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connector resource.
    - name: properties
      description: |
        The properties of the Connector. Required.
      value:
        connectorBasicInfo:
          connectorType: "{{ connectorType }}"
          connectorClass: "{{ connectorClass }}"
          connectorName: "{{ connectorName }}"
          connectorId: "{{ connectorId }}"
          connectorState: "{{ connectorState }}"
        connectorServiceTypeInfo:
          connectorServiceType: "{{ connectorServiceType }}"
        partnerConnectorInfo:
          partnerConnectorType: "{{ partnerConnectorType }}"
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

Create confluent connector by Name.

```sql
REPLACE azure_isv.confluent.connector
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND environment_id = '{{ environment_id }}' --required
AND cluster_id = '{{ cluster_id }}' --required
AND connector_name = '{{ connector_name }}' --required
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

Delete confluent connector by name.

```sql
DELETE FROM azure_isv.confluent.connector
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND environment_id = '{{ environment_id }}' --required
AND cluster_id = '{{ cluster_id }}' --required
AND connector_name = '{{ connector_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
