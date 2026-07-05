--- 
title: sql_virtual_machine_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machine_groups
  - sqlvirtualmachine
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

Creates, updates, deletes, gets or lists a <code>sql_virtual_machine_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_virtual_machine_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sqlvirtualmachine.sql_virtual_machine_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterConfiguration" /></td>
    <td><code>string</code></td>
    <td>Cluster type. "Domainful"</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerType" /></td>
    <td><code>string</code></td>
    <td>Type of cluster manager: Windows Server Failover Cluster (WSFC), implied by the scale type of the group and the OS type. "WSFC"</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleType" /></td>
    <td><code>string</code></td>
    <td>Scale type. "HA"</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageOffer" /></td>
    <td><code>string</code></td>
    <td>SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageSku" /></td>
    <td><code>string</code></td>
    <td>SQL image sku. Known values are: "Developer" and "Enterprise".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcDomainProfile" /></td>
    <td><code>object</code></td>
    <td>Cluster Active Directory domain profile.</td>
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
    <td><CopyableCode code="clusterConfiguration" /></td>
    <td><code>string</code></td>
    <td>Cluster type. "Domainful"</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerType" /></td>
    <td><code>string</code></td>
    <td>Type of cluster manager: Windows Server Failover Cluster (WSFC), implied by the scale type of the group and the OS type. "WSFC"</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleType" /></td>
    <td><code>string</code></td>
    <td>Scale type. "HA"</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageOffer" /></td>
    <td><code>string</code></td>
    <td>SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageSku" /></td>
    <td><code>string</code></td>
    <td>SQL image sku. Known values are: "Developer" and "Enterprise".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcDomainProfile" /></td>
    <td><code>object</code></td>
    <td>Cluster Active Directory domain profile.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterConfiguration" /></td>
    <td><code>string</code></td>
    <td>Cluster type. "Domainful"</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerType" /></td>
    <td><code>string</code></td>
    <td>Type of cluster manager: Windows Server Failover Cluster (WSFC), implied by the scale type of the group and the OS type. "WSFC"</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleType" /></td>
    <td><code>string</code></td>
    <td>Scale type. "HA"</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageOffer" /></td>
    <td><code>string</code></td>
    <td>SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageSku" /></td>
    <td><code>string</code></td>
    <td>SQL image sku. Known values are: "Developer" and "Enterprise".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcDomainProfile" /></td>
    <td><code>object</code></td>
    <td>Cluster Active Directory domain profile.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a SQL virtual machine group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all SQL virtual machine groups in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all SQL virtual machine groups in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a SQL virtual machine group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates SQL virtual machine group tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a SQL virtual machine group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a SQL virtual machine group.</td>
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
    <td>Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-sql_virtual_machine_group_name">
    <td><CopyableCode code="sql_virtual_machine_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SQL virtual machine group. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a SQL virtual machine group.

```sql
SELECT
id,
name,
clusterConfiguration,
clusterManagerType,
location,
provisioningState,
scaleType,
sqlImageOffer,
sqlImageSku,
systemData,
tags,
type,
wsfcDomainProfile
FROM azure.sqlvirtualmachine.sql_virtual_machine_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all SQL virtual machine groups in a resource group.

```sql
SELECT
id,
name,
clusterConfiguration,
clusterManagerType,
location,
provisioningState,
scaleType,
sqlImageOffer,
sqlImageSku,
systemData,
tags,
type,
wsfcDomainProfile
FROM azure.sqlvirtualmachine.sql_virtual_machine_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all SQL virtual machine groups in a subscription.

```sql
SELECT
id,
name,
clusterConfiguration,
clusterManagerType,
location,
provisioningState,
scaleType,
sqlImageOffer,
sqlImageSku,
systemData,
tags,
type,
wsfcDomainProfile
FROM azure.sqlvirtualmachine.sql_virtual_machine_groups
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a SQL virtual machine group.

```sql
INSERT INTO azure.sqlvirtualmachine.sql_virtual_machine_groups (
location,
tags,
properties,
resource_group_name,
sql_virtual_machine_group_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sql_virtual_machine_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: sql_virtual_machine_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_virtual_machine_groups resource.
    - name: sql_virtual_machine_group_name
      value: "{{ sql_virtual_machine_group_name }}"
      description: Required parameter for the sql_virtual_machine_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_virtual_machine_groups resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      value:
        sqlImageOffer: "{{ sqlImageOffer }}"
        sqlImageSku: "{{ sqlImageSku }}"
        wsfcDomainProfile:
          domainFqdn: "{{ domainFqdn }}"
          ouPath: "{{ ouPath }}"
          clusterBootstrapAccount: "{{ clusterBootstrapAccount }}"
          clusterOperatorAccount: "{{ clusterOperatorAccount }}"
          sqlServiceAccount: "{{ sqlServiceAccount }}"
          fileShareWitnessPath: "{{ fileShareWitnessPath }}"
          storageAccountUrl: "{{ storageAccountUrl }}"
          storageAccountPrimaryKey: "{{ storageAccountPrimaryKey }}"
          clusterSubnetType: "{{ clusterSubnetType }}"
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

Updates SQL virtual machine group tags.

```sql
UPDATE azure.sqlvirtualmachine.sql_virtual_machine_groups
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Creates or updates a SQL virtual machine group.

```sql
REPLACE azure.sqlvirtualmachine.sql_virtual_machine_groups
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Deletes a SQL virtual machine group.

```sql
DELETE FROM azure.sqlvirtualmachine.sql_virtual_machine_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
