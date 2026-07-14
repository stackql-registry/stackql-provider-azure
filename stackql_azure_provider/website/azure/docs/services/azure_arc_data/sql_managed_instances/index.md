--- 
title: sql_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_managed_instances
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

Creates, updates, deletes, gets or lists a <code>sql_managed_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_managed_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_managed_instances" /></td></tr>
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
    <td><CopyableCode code="activeDirectoryInformation" /></td>
    <td><code>object</code></td>
    <td>Active Directory information related to this SQL Managed Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="admin" /></td>
    <td><code>string</code></td>
    <td>The instance admin user.</td>
</tr>
<tr>
    <td><CopyableCode code="basicLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Username and password for basic authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the connected cluster the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="dataControllerId" /></td>
    <td><code>string</code></td>
    <td>null.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>The instance end time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the extension the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="k8sRaw" /></td>
    <td><code>object</code></td>
    <td>The raw kubernetes information.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last uploaded date from Kubernetes cluster. Defaults to current date time.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this managed instance. Known values are: "BasePrice", "LicenseIncluded", and "DisasterRecovery".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc-enabled SQL Managed Instance resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Resource sku.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The instance start time.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="activeDirectoryInformation" /></td>
    <td><code>object</code></td>
    <td>Active Directory information related to this SQL Managed Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="admin" /></td>
    <td><code>string</code></td>
    <td>The instance admin user.</td>
</tr>
<tr>
    <td><CopyableCode code="basicLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Username and password for basic authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the connected cluster the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="dataControllerId" /></td>
    <td><code>string</code></td>
    <td>null.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>The instance end time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the extension the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="k8sRaw" /></td>
    <td><code>object</code></td>
    <td>The raw kubernetes information.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last uploaded date from Kubernetes cluster. Defaults to current date time.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this managed instance. Known values are: "BasePrice", "LicenseIncluded", and "DisasterRecovery".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc-enabled SQL Managed Instance resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Resource sku.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The instance start time.</td>
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
    <td><CopyableCode code="activeDirectoryInformation" /></td>
    <td><code>object</code></td>
    <td>Active Directory information related to this SQL Managed Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="admin" /></td>
    <td><code>string</code></td>
    <td>The instance admin user.</td>
</tr>
<tr>
    <td><CopyableCode code="basicLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Username and password for basic authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the connected cluster the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="dataControllerId" /></td>
    <td><code>string</code></td>
    <td>null.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>The instance end time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the extension the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="k8sRaw" /></td>
    <td><code>object</code></td>
    <td>The raw kubernetes information.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last uploaded date from Kubernetes cluster. Defaults to current date time.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this managed instance. Known values are: "BasePrice", "LicenseIncluded", and "DisasterRecovery".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc-enabled SQL Managed Instance resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Resource sku.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The instance start time.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_managed_instance_name"><code>sql_managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a SQL Managed Instance resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List sqlManagedInstance resources in the resource group. Gets all sqlManagedInstances in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List sqlManagedInstance resources in the subscription. List sqlManagedInstance resources in the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_managed_instance_name"><code>sql_managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or replaces a SQL Managed Instance resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_managed_instance_name"><code>sql_managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a SQL Managed Instance resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_managed_instance_name"><code>sql_managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a SQL Managed Instance resource.</td>
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
<tr id="parameter-sql_managed_instance_name">
    <td><CopyableCode code="sql_managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of SQL Managed Instance. Required.</td>
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

Retrieves a SQL Managed Instance resource.

```sql
SELECT
id,
name,
activeDirectoryInformation,
admin,
basicLoginInformation,
clusterId,
dataControllerId,
endTime,
extendedLocation,
extensionId,
k8sRaw,
lastUploadedDate,
licenseType,
location,
provisioningState,
sku,
startTime,
systemData,
tags,
type
FROM azure.azure_arc_data.sql_managed_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_managed_instance_name = '{{ sql_managed_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List sqlManagedInstance resources in the resource group. Gets all sqlManagedInstances in a resource group.

```sql
SELECT
id,
name,
activeDirectoryInformation,
admin,
basicLoginInformation,
clusterId,
dataControllerId,
endTime,
extendedLocation,
extensionId,
k8sRaw,
lastUploadedDate,
licenseType,
location,
provisioningState,
sku,
startTime,
systemData,
tags,
type
FROM azure.azure_arc_data.sql_managed_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List sqlManagedInstance resources in the subscription. List sqlManagedInstance resources in the subscription.

```sql
SELECT
id,
name,
activeDirectoryInformation,
admin,
basicLoginInformation,
clusterId,
dataControllerId,
endTime,
extendedLocation,
extensionId,
k8sRaw,
lastUploadedDate,
licenseType,
location,
provisioningState,
sku,
startTime,
systemData,
tags,
type
FROM azure.azure_arc_data.sql_managed_instances
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

Creates or replaces a SQL Managed Instance resource.

```sql
INSERT INTO azure.azure_arc_data.sql_managed_instances (
tags,
location,
properties,
extendedLocation,
sku,
resource_group_name,
sql_managed_instance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ sql_managed_instance_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sql_managed_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_managed_instances resource.
    - name: sql_managed_instance_name
      value: "{{ sql_managed_instance_name }}"
      description: Required parameter for the sql_managed_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_managed_instances resource.
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
        null. Required.
      value:
        dataControllerId: "{{ dataControllerId }}"
        admin: "{{ admin }}"
        startTime: "{{ startTime }}"
        endTime: "{{ endTime }}"
        k8sRaw:
          : "{{  }}"
          spec:
            : "{{  }}"
            scheduling:
              : "{{  }}"
              default:
                : "{{  }}"
                resources: "{{ resources }}"
            replicas: {{ replicas }}
        basicLoginInformation:
          username: "{{ username }}"
          password: "{{ password }}"
        lastUploadedDate: "{{ lastUploadedDate }}"
        provisioningState: "{{ provisioningState }}"
        activeDirectoryInformation:
          keytabInformation:
            keytab: "{{ keytab }}"
        licenseType: "{{ licenseType }}"
        clusterId: "{{ clusterId }}"
        extensionId: "{{ extensionId }}"
    - name: extendedLocation
      description: |
        The extendedLocation of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: sku
      description: |
        Resource sku.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        dev: {{ dev }}
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
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

Updates a SQL Managed Instance resource.

```sql
UPDATE azure.azure_arc_data.sql_managed_instances
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_managed_instance_name = '{{ sql_managed_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
location,
properties,
sku,
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

Deletes a SQL Managed Instance resource.

```sql
DELETE FROM azure.azure_arc_data.sql_managed_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sql_managed_instance_name = '{{ sql_managed_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
