--- 
title: shares
hide_title: false
hide_table_of_contents: false
keywords:
  - shares
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="shares" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.shares" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' }
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
    <td><CopyableCode code="accessProtocol" /></td>
    <td><code>string</code></td>
    <td>Access protocol to be used by the share. Required. Known values are: "SMB" and "NFS". (SMB, NFS)</td>
</tr>
<tr>
    <td><CopyableCode code="azureContainerInfo" /></td>
    <td><code>object</code></td>
    <td>Azure container mapping for the share.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAccessRights" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses and corresponding access rights on the share(required for NFS protocol).</td>
</tr>
<tr>
    <td><CopyableCode code="dataPolicy" /></td>
    <td><code>string</code></td>
    <td>Data policy of the share. Known values are: "Cloud" and "Local". (Cloud, Local)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the share.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Current monitoring status of the share. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the refresh job on this share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareMappings" /></td>
    <td><code>array</code></td>
    <td>Share mount point to the role.</td>
</tr>
<tr>
    <td><CopyableCode code="shareStatus" /></td>
    <td><code>string</code></td>
    <td>Current status of the share. Required. Known values are: "Offline", "Unknown", "OK", "Updating", and "NeedsAttention". (Offline, Unknown, OK, Updating, NeedsAttention)</td>
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
    <td><CopyableCode code="userAccessRights" /></td>
    <td><code>array</code></td>
    <td>Mapping of users and corresponding access rights on the share (required for SMB protocol).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_data_box_edge_device">

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
    <td><CopyableCode code="accessProtocol" /></td>
    <td><code>string</code></td>
    <td>Access protocol to be used by the share. Required. Known values are: "SMB" and "NFS". (SMB, NFS)</td>
</tr>
<tr>
    <td><CopyableCode code="azureContainerInfo" /></td>
    <td><code>object</code></td>
    <td>Azure container mapping for the share.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAccessRights" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses and corresponding access rights on the share(required for NFS protocol).</td>
</tr>
<tr>
    <td><CopyableCode code="dataPolicy" /></td>
    <td><code>string</code></td>
    <td>Data policy of the share. Known values are: "Cloud" and "Local". (Cloud, Local)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the share.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Current monitoring status of the share. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the refresh job on this share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareMappings" /></td>
    <td><code>array</code></td>
    <td>Share mount point to the role.</td>
</tr>
<tr>
    <td><CopyableCode code="shareStatus" /></td>
    <td><code>string</code></td>
    <td>Current status of the share. Required. Known values are: "Offline", "Unknown", "OK", "Updating", and "NeedsAttention". (Offline, Unknown, OK, Updating, NeedsAttention)</td>
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
    <td><CopyableCode code="userAccessRights" /></td>
    <td><code>array</code></td>
    <td>Mapping of users and corresponding access rights on the share (required for SMB protocol).</td>
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
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a share by name. Gets a share by name.</td>
</tr>
<tr>
    <td><a href="#list_by_data_box_edge_device"><CopyableCode code="list_by_data_box_edge_device" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the shares in a Data Box Edge/Data Box Gateway device. Lists all the shares in a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new share or updates an existing share on the device. Creates a new share or updates an existing share on the device.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new share or updates an existing share on the device. Creates a new share or updates an existing share on the device.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the share on the Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#refresh"><CopyableCode code="refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes the share metadata with the data from the cloud. Refreshes the share metadata with the data from the cloud.</td>
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
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The share name. Required.</td>
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
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' }
    ]}
>
<TabItem value="get">

Gets a share by name. Gets a share by name.

```sql
SELECT
id,
name,
accessProtocol,
azureContainerInfo,
clientAccessRights,
dataPolicy,
description,
monitoringStatus,
refreshDetails,
shareMappings,
shareStatus,
systemData,
type,
userAccessRights
FROM azure.data_box_edge.shares
WHERE device_name = '{{ device_name }}' -- required
AND name = '{{ name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_data_box_edge_device">

Lists all the shares in a Data Box Edge/Data Box Gateway device. Lists all the shares in a Data Box Edge/Data Box Gateway device.

```sql
SELECT
id,
name,
accessProtocol,
azureContainerInfo,
clientAccessRights,
dataPolicy,
description,
monitoringStatus,
refreshDetails,
shareMappings,
shareStatus,
systemData,
type,
userAccessRights
FROM azure.data_box_edge.shares
WHERE device_name = '{{ device_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
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

Creates a new share or updates an existing share on the device. Creates a new share or updates an existing share on the device.

```sql
INSERT INTO azure.data_box_edge.shares (
properties,
device_name,
name,
resource_group_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ device_name }}',
'{{ name }}',
'{{ resource_group_name }}',
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
- name: shares
  props:
    - name: device_name
      value: "{{ device_name }}"
      description: Required parameter for the shares resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the shares resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the shares resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the shares resource.
    - name: properties
      description: |
        The share properties. Required.
      value:
        description: "{{ description }}"
        shareStatus: "{{ shareStatus }}"
        monitoringStatus: "{{ monitoringStatus }}"
        azureContainerInfo:
          storageAccountCredentialId: "{{ storageAccountCredentialId }}"
          containerName: "{{ containerName }}"
          dataFormat: "{{ dataFormat }}"
        accessProtocol: "{{ accessProtocol }}"
        userAccessRights:
          - userId: "{{ userId }}"
            accessType: "{{ accessType }}"
        clientAccessRights:
          - client: "{{ client }}"
            accessPermission: "{{ accessPermission }}"
        refreshDetails:
          inProgressRefreshJobId: "{{ inProgressRefreshJobId }}"
          lastCompletedRefreshJobTimeInUTC: "{{ lastCompletedRefreshJobTimeInUTC }}"
          errorManifestFile: "{{ errorManifestFile }}"
          lastJob: "{{ lastJob }}"
        shareMappings:
          - shareId: "{{ shareId }}"
            roleId: "{{ roleId }}"
            mountPoint: "{{ mountPoint }}"
            mountType: "{{ mountType }}"
            roleType: "{{ roleType }}"
        dataPolicy: "{{ dataPolicy }}"
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

Creates a new share or updates an existing share on the device. Creates a new share or updates an existing share on the device.

```sql
REPLACE azure.data_box_edge.shares
SET 
properties = '{{ properties }}'
WHERE 
device_name = '{{ device_name }}' --required
AND name = '{{ name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
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

Deletes the share on the Data Box Edge/Data Box Gateway device.

```sql
DELETE FROM azure.data_box_edge.shares
WHERE device_name = '{{ device_name }}' --required
AND name = '{{ name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh"
    values={[
        { label: 'refresh', value: 'refresh' }
    ]}
>
<TabItem value="refresh">

Refreshes the share metadata with the data from the cloud. Refreshes the share metadata with the data from the cloud.

```sql
EXEC azure.data_box_edge.shares.refresh 
@device_name='{{ device_name }}' --required, 
@name='{{ name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
