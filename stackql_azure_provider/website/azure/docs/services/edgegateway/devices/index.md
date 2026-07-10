--- 
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - edgegateway
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.edgegateway.devices" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Modifies a Data Box Edge/Gateway resource.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Gets the properties of the data box edge/gateway device.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets all the data box edge/gateway devices in a subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets all the data box edge/gateway devices in a resource group.</td>
</tr>
<tr>
    <td><a href="#get_extended_information"><CopyableCode code="get_extended_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Gets additional information for the specified data box edge/gateway device.</td>
</tr>
<tr>
    <td><a href="#get_network_settings"><CopyableCode code="get_network_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Gets the network settings of the specified data box edge/gateway device.</td>
</tr>
<tr>
    <td><a href="#get_update_summary"><CopyableCode code="get_update_summary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.</td>
</tr>
<tr>
    <td><a href="#download_updates"><CopyableCode code="download_updates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Downloads the updates on a data box edge/gateway device.</td>
</tr>
<tr>
    <td><a href="#install_updates"><CopyableCode code="install_updates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Installs the updates on the data box edge/gateway device.</td>
</tr>
<tr>
    <td><a href="#scan_for_updates"><CopyableCode code="scan_for_updates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Scans for updates on a data box edge/gateway device.</td>
</tr>
<tr>
    <td><a href="#create_or_update_security_settings"><CopyableCode code="create_or_update_security_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Updates the security settings on a data box edge/gateway device.</td>
</tr>
<tr>
    <td><a href="#upload_certificate"><CopyableCode code="upload_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Uploads registration certificate for the device.</td>
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
    <td>The device name.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Specify $expand=details to populate additional fields related to the resource or Specify $skipToken= to populate the next page in the list.</td>
</tr>
<tr id="parameter-accept-language">
    <td><CopyableCode code="accept-language" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Modifies a Data Box Edge/Gateway resource.

```sql
UPDATE azure.edgegateway.devices
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND device_name = '{{ device_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND accept-language = '{{ accept-language}}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_raw"
    values={[
        { label: 'get_raw', value: 'get_raw' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'get_extended_information', value: 'get_extended_information' },
        { label: 'get_network_settings', value: 'get_network_settings' },
        { label: 'get_update_summary', value: 'get_update_summary' },
        { label: 'download_updates', value: 'download_updates' },
        { label: 'install_updates', value: 'install_updates' },
        { label: 'scan_for_updates', value: 'scan_for_updates' },
        { label: 'create_or_update_security_settings', value: 'create_or_update_security_settings' },
        { label: 'upload_certificate', value: 'upload_certificate' }
    ]}
>
<TabItem value="get_raw">

Gets the properties of the data box edge/gateway device.

```sql
EXEC azure.edgegateway.devices.get_raw 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all the data box edge/gateway devices in a subscription.

```sql
EXEC azure.edgegateway.devices.list_by_subscription 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}', 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all the data box edge/gateway devices in a resource group.

```sql
EXEC azure.edgegateway.devices.list_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}', 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_extended_information">

Gets additional information for the specified data box edge/gateway device.

```sql
EXEC azure.edgegateway.devices.get_extended_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
<TabItem value="get_network_settings">

Gets the network settings of the specified data box edge/gateway device.

```sql
EXEC azure.edgegateway.devices.get_network_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
<TabItem value="get_update_summary">

Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.

```sql
EXEC azure.edgegateway.devices.get_update_summary 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
<TabItem value="download_updates">

Downloads the updates on a data box edge/gateway device.

```sql
EXEC azure.edgegateway.devices.download_updates 

;
```
</TabItem>
<TabItem value="install_updates">

Installs the updates on the data box edge/gateway device.

```sql
EXEC azure.edgegateway.devices.install_updates 

;
```
</TabItem>
<TabItem value="scan_for_updates">

Scans for updates on a data box edge/gateway device.

```sql
EXEC azure.edgegateway.devices.scan_for_updates 

;
```
</TabItem>
<TabItem value="create_or_update_security_settings">

Updates the security settings on a data box edge/gateway device.

```sql
EXEC azure.edgegateway.devices.create_or_update_security_settings 

;
```
</TabItem>
<TabItem value="upload_certificate">

Uploads registration certificate for the device.

```sql
EXEC azure.edgegateway.devices.upload_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
</Tabs>
