--- 
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
  - iot_operations
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

Creates, updates, deletes, gets or lists an <code>instance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="instance" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_operations.instance" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="adrNamespaceRef" /></td>
    <td><code>object</code></td>
    <td>The Azure Device Registry Namespace used by Assets, Discovered Assets and devices.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecretProviderClassRef" /></td>
    <td><code>object</code></td>
    <td>The reference to the AIO Secret provider class.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>object</code></td>
    <td>The features of the AIO Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="schemaRegistryRef" /></td>
    <td><code>object</code></td>
    <td>The reference to the Schema Registry for this AIO Instance. Required.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The Azure IoT Operations version.</td>
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
    <td><CopyableCode code="adrNamespaceRef" /></td>
    <td><code>object</code></td>
    <td>The Azure Device Registry Namespace used by Assets, Discovered Assets and devices.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecretProviderClassRef" /></td>
    <td><code>object</code></td>
    <td>The reference to the AIO Secret provider class.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>object</code></td>
    <td>The features of the AIO Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="schemaRegistryRef" /></td>
    <td><code>object</code></td>
    <td>The reference to the Schema Registry for this AIO Instance. Required.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The Azure IoT Operations version.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="adrNamespaceRef" /></td>
    <td><code>object</code></td>
    <td>The Azure Device Registry Namespace used by Assets, Discovered Assets and devices.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecretProviderClassRef" /></td>
    <td><code>object</code></td>
    <td>The reference to the AIO Secret provider class.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>object</code></td>
    <td>The features of the AIO Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="schemaRegistryRef" /></td>
    <td><code>object</code></td>
    <td>The reference to the Schema Registry for this AIO Instance. Required.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The Azure IoT Operations version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a InstanceResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List InstanceResource resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List InstanceResource resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a InstanceResource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a InstanceResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a InstanceResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a InstanceResource.</td>
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
<tr id="parameter-instance_name">
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of instance. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a InstanceResource.

```sql
SELECT
id,
name,
adrNamespaceRef,
defaultSecretProviderClassRef,
description,
extendedLocation,
features,
healthState,
identity,
location,
provisioningState,
schemaRegistryRef,
systemData,
tags,
type,
version
FROM azure.iot_operations.instance
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List InstanceResource resources by resource group.

```sql
SELECT
id,
name,
adrNamespaceRef,
defaultSecretProviderClassRef,
description,
extendedLocation,
features,
healthState,
identity,
location,
provisioningState,
schemaRegistryRef,
systemData,
tags,
type,
version
FROM azure.iot_operations.instance
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List InstanceResource resources by subscription ID.

```sql
SELECT
id,
name,
adrNamespaceRef,
defaultSecretProviderClassRef,
description,
extendedLocation,
features,
healthState,
identity,
location,
provisioningState,
schemaRegistryRef,
systemData,
tags,
type,
version
FROM azure.iot_operations.instance
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

Create a InstanceResource.

```sql
INSERT INTO azure.iot_operations.instance (
tags,
location,
properties,
extendedLocation,
identity,
resource_group_name,
instance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ instance_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
identity,
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
- name: instance
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the instance resource.
    - name: instance_name
      value: "{{ instance_name }}"
      description: Required parameter for the instance resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the instance resource.
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
        The resource-specific properties for this resource.
      value:
        description: "{{ description }}"
        provisioningState: "{{ provisioningState }}"
        version: "{{ version }}"
        schemaRegistryRef:
          resourceId: "{{ resourceId }}"
        defaultSecretProviderClassRef:
          resourceId: "{{ resourceId }}"
        features: "{{ features }}"
        adrNamespaceRef:
          resourceId: "{{ resourceId }}"
        healthState: "{{ healthState }}"
    - name: extendedLocation
      description: |
        Edge location of the resource. Required.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update a InstanceResource.

```sql
UPDATE azure.iot_operations.instance
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
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

Create a InstanceResource.

```sql
REPLACE azure.iot_operations.instance
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
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

Delete a InstanceResource.

```sql
DELETE FROM azure.iot_operations.instance
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
