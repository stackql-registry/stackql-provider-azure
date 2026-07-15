--- 
title: sql_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_instances
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>sql_server_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_server_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_server_instances" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureDefenderStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Defender. Known values are: "Protected", "Unprotected", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="azureDefenderStatusLastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of last Azure Defender status update.</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>SQL Server collation.</td>
</tr>
<tr>
    <td><CopyableCode code="containerResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource id of the container resource (Azure Arc for Servers). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string</code></td>
    <td>The time when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currentVersion" /></td>
    <td><code>string</code></td>
    <td>SQL Server current version.</td>
</tr>
<tr>
    <td><CopyableCode code="edition" /></td>
    <td><code>string</code></td>
    <td>SQL Server edition. Known values are: "Evaluation", "Enterprise", "Standard", "Web", "Developer", and "Express".</td>
</tr>
<tr>
    <td><CopyableCode code="hostType" /></td>
    <td><code>string</code></td>
    <td>Type of host for Azure Arc SQL Server. Known values are: "Azure Virtual Machine", "Azure VMWare Virtual Machine", "Azure Kubernetes Service", "AWS VMWare Virtual Machine", "AWS Kubernetes Service", "GCP VMWare Virtual Machine", "GCP Kubernetes Service", "Container", "Virtual Machine", "Physical Server", "AWS Virtual Machine", "GCP Virtual Machine", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="instanceName" /></td>
    <td><code>string</code></td>
    <td>SQL Server instance name.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>SQL Server license type. Known values are: "Undefined", "Free", "HADR", "ServerCAL", "LicenseOnly", "PAYG", and "Paid".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="patchLevel" /></td>
    <td><code>string</code></td>
    <td>SQL Server update level.</td>
</tr>
<tr>
    <td><CopyableCode code="productId" /></td>
    <td><code>string</code></td>
    <td>SQL Server product ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc-enabled SQL Server resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The cloud connectivity status. Required. Known values are: "Connected", "Disconnected", "Registered", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tcpDynamicPorts" /></td>
    <td><code>string</code></td>
    <td>Dynamic TCP ports used by SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="tcpStaticPorts" /></td>
    <td><code>string</code></td>
    <td>Static TCP ports used by SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCore" /></td>
    <td><code>string</code></td>
    <td>The number of logical processors used by the SQL Server instance.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>SQL Server version. Known values are: "SQL Server 2012", "SQL Server 2014", "SQL Server 2016", "SQL Server 2017", "SQL Server 2019", "SQL Server 2022", and "Unknown".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureDefenderStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Defender. Known values are: "Protected", "Unprotected", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="azureDefenderStatusLastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of last Azure Defender status update.</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>SQL Server collation.</td>
</tr>
<tr>
    <td><CopyableCode code="containerResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource id of the container resource (Azure Arc for Servers). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string</code></td>
    <td>The time when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currentVersion" /></td>
    <td><code>string</code></td>
    <td>SQL Server current version.</td>
</tr>
<tr>
    <td><CopyableCode code="edition" /></td>
    <td><code>string</code></td>
    <td>SQL Server edition. Known values are: "Evaluation", "Enterprise", "Standard", "Web", "Developer", and "Express".</td>
</tr>
<tr>
    <td><CopyableCode code="hostType" /></td>
    <td><code>string</code></td>
    <td>Type of host for Azure Arc SQL Server. Known values are: "Azure Virtual Machine", "Azure VMWare Virtual Machine", "Azure Kubernetes Service", "AWS VMWare Virtual Machine", "AWS Kubernetes Service", "GCP VMWare Virtual Machine", "GCP Kubernetes Service", "Container", "Virtual Machine", "Physical Server", "AWS Virtual Machine", "GCP Virtual Machine", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="instanceName" /></td>
    <td><code>string</code></td>
    <td>SQL Server instance name.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>SQL Server license type. Known values are: "Undefined", "Free", "HADR", "ServerCAL", "LicenseOnly", "PAYG", and "Paid".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="patchLevel" /></td>
    <td><code>string</code></td>
    <td>SQL Server update level.</td>
</tr>
<tr>
    <td><CopyableCode code="productId" /></td>
    <td><code>string</code></td>
    <td>SQL Server product ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc-enabled SQL Server resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The cloud connectivity status. Required. Known values are: "Connected", "Disconnected", "Registered", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tcpDynamicPorts" /></td>
    <td><code>string</code></td>
    <td>Dynamic TCP ports used by SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="tcpStaticPorts" /></td>
    <td><code>string</code></td>
    <td>Static TCP ports used by SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCore" /></td>
    <td><code>string</code></td>
    <td>The number of logical processors used by the SQL Server instance.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>SQL Server version. Known values are: "SQL Server 2012", "SQL Server 2014", "SQL Server 2016", "SQL Server 2017", "SQL Server 2019", "SQL Server 2022", and "Unknown".</td>
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
    <td><CopyableCode code="azureDefenderStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Defender. Known values are: "Protected", "Unprotected", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="azureDefenderStatusLastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of last Azure Defender status update.</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>SQL Server collation.</td>
</tr>
<tr>
    <td><CopyableCode code="containerResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource id of the container resource (Azure Arc for Servers). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string</code></td>
    <td>The time when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currentVersion" /></td>
    <td><code>string</code></td>
    <td>SQL Server current version.</td>
</tr>
<tr>
    <td><CopyableCode code="edition" /></td>
    <td><code>string</code></td>
    <td>SQL Server edition. Known values are: "Evaluation", "Enterprise", "Standard", "Web", "Developer", and "Express".</td>
</tr>
<tr>
    <td><CopyableCode code="hostType" /></td>
    <td><code>string</code></td>
    <td>Type of host for Azure Arc SQL Server. Known values are: "Azure Virtual Machine", "Azure VMWare Virtual Machine", "Azure Kubernetes Service", "AWS VMWare Virtual Machine", "AWS Kubernetes Service", "GCP VMWare Virtual Machine", "GCP Kubernetes Service", "Container", "Virtual Machine", "Physical Server", "AWS Virtual Machine", "GCP Virtual Machine", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="instanceName" /></td>
    <td><code>string</code></td>
    <td>SQL Server instance name.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>SQL Server license type. Known values are: "Undefined", "Free", "HADR", "ServerCAL", "LicenseOnly", "PAYG", and "Paid".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="patchLevel" /></td>
    <td><code>string</code></td>
    <td>SQL Server update level.</td>
</tr>
<tr>
    <td><CopyableCode code="productId" /></td>
    <td><code>string</code></td>
    <td>SQL Server product ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc-enabled SQL Server resource.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The cloud connectivity status. Required. Known values are: "Connected", "Disconnected", "Registered", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tcpDynamicPorts" /></td>
    <td><code>string</code></td>
    <td>Dynamic TCP ports used by SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="tcpStaticPorts" /></td>
    <td><code>string</code></td>
    <td>Static TCP ports used by SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCore" /></td>
    <td><code>string</code></td>
    <td>The number of logical processors used by the SQL Server instance.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>SQL Server version. Known values are: "SQL Server 2012", "SQL Server 2014", "SQL Server 2016", "SQL Server 2017", "SQL Server 2019", "SQL Server 2022", and "Unknown".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_server_instance_name"><code>sql_server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a SQL Server Instance resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List sqlServerInstance resources in the resource group. Gets all sqlServerInstances in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List sqlServerInstance resources in the subscription. List sqlServerInstance resources in the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_server_instance_name"><code>sql_server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or replaces a SQL Server Instance resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_server_instance_name"><code>sql_server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a SQL Server Instance resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_server_instance_name"><code>sql_server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a SQL Server Instance resource.</td>
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
    <td>The name of the Azure resource group. Required.</td>
</tr>
<tr id="parameter-sql_server_instance_name">
    <td><CopyableCode code="sql_server_instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of SQL Server Instance. Required.</td>
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

Retrieves a SQL Server Instance resource.

```sql
SELECT
id,
name,
azureDefenderStatus,
azureDefenderStatusLastUpdated,
collation,
containerResourceId,
createTime,
currentVersion,
edition,
hostType,
instanceName,
licenseType,
location,
patchLevel,
productId,
provisioningState,
status,
systemData,
tags,
tcpDynamicPorts,
tcpStaticPorts,
type,
vCore,
version
FROM azure.azure_arc_data.sql_server_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_server_instance_name = '{{ sql_server_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List sqlServerInstance resources in the resource group. Gets all sqlServerInstances in a resource group.

```sql
SELECT
id,
name,
azureDefenderStatus,
azureDefenderStatusLastUpdated,
collation,
containerResourceId,
createTime,
currentVersion,
edition,
hostType,
instanceName,
licenseType,
location,
patchLevel,
productId,
provisioningState,
status,
systemData,
tags,
tcpDynamicPorts,
tcpStaticPorts,
type,
vCore,
version
FROM azure.azure_arc_data.sql_server_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List sqlServerInstance resources in the subscription. List sqlServerInstance resources in the subscription.

```sql
SELECT
id,
name,
azureDefenderStatus,
azureDefenderStatusLastUpdated,
collation,
containerResourceId,
createTime,
currentVersion,
edition,
hostType,
instanceName,
licenseType,
location,
patchLevel,
productId,
provisioningState,
status,
systemData,
tags,
tcpDynamicPorts,
tcpStaticPorts,
type,
vCore,
version
FROM azure.azure_arc_data.sql_server_instances
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or replaces a SQL Server Instance resource.

```sql
INSERT INTO azure.azure_arc_data.sql_server_instances (
tags,
location,
properties,
resource_group_name,
sql_server_instance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sql_server_instance_name }}',
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
- name: sql_server_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_server_instances resource.
    - name: sql_server_instance_name
      value: "{{ sql_server_instance_name }}"
      description: Required parameter for the sql_server_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_server_instances resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        null.
      value:
        version: "{{ version }}"
        edition: "{{ edition }}"
        containerResourceId: "{{ containerResourceId }}"
        createTime: "{{ createTime }}"
        vCore: "{{ vCore }}"
        status: "{{ status }}"
        patchLevel: "{{ patchLevel }}"
        collation: "{{ collation }}"
        currentVersion: "{{ currentVersion }}"
        instanceName: "{{ instanceName }}"
        tcpDynamicPorts: "{{ tcpDynamicPorts }}"
        tcpStaticPorts: "{{ tcpStaticPorts }}"
        productId: "{{ productId }}"
        licenseType: "{{ licenseType }}"
        azureDefenderStatusLastUpdated: "{{ azureDefenderStatusLastUpdated }}"
        azureDefenderStatus: "{{ azureDefenderStatus }}"
        provisioningState: "{{ provisioningState }}"
        hostType: "{{ hostType }}"
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

Updates a SQL Server Instance resource.

```sql
UPDATE azure.azure_arc_data.sql_server_instances
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_server_instance_name = '{{ sql_server_instance_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a SQL Server Instance resource.

```sql
DELETE FROM azure.azure_arc_data.sql_server_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sql_server_instance_name = '{{ sql_server_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
