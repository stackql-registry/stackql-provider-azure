--- 
title: capabilities_by_location
hide_title: false
hide_table_of_contents: false
keywords:
  - capabilities_by_location
  - postgresql_flexible_servers
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

Creates, updates, deletes, gets or lists a <code>capabilities_by_location</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="capabilities_by_location" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_flexible_servers.capabilities_by_location" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of flexible servers capabilities.</td>
</tr>
<tr>
    <td><CopyableCode code="fastProvisioningSupported" /></td>
    <td><code>string</code></td>
    <td>Indicates if fast provisioning is supported. 'Enabled' means fast provisioning is supported. 'Disabled' stands for fast provisioning is not supported. Will be deprecated in the future. Look to Supported Features for 'FastProvisioning'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="geoBackupSupported" /></td>
    <td><code>string</code></td>
    <td>Indicates if geographically redundant backups are supported in this location. 'Enabled' means geographically redundant backups are supported. 'Disabled' stands for geographically redundant backup is not supported. Will be deprecated in the future. Look to Supported Features for 'GeoBackup'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="onlineResizeSupported" /></td>
    <td><code>string</code></td>
    <td>Indicates if resizing the storage, without interrupting the operation of the database engine, is supported in this location for the given subscription. 'Enabled' means resizing the storage without interrupting the operation of the database engine is supported. 'Disabled' means resizing the storage without interrupting the operation of the database engine is not supported. Will be deprecated in the future. Look to Supported Features for 'OnlineResize'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Reason for the capability not being available.</td>
</tr>
<tr>
    <td><CopyableCode code="restricted" /></td>
    <td><code>string</code></td>
    <td>Indicates if this location is restricted. 'Enabled' means location is restricted. 'Disabled' stands for location is not restricted. Will be deprecated in the future. Look to Supported Features for 'Restricted'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the capability. Known values are: "Visible", "Available", "Default", and "Disabled". (Visible, Available, Default, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAutoGrowthSupported" /></td>
    <td><code>string</code></td>
    <td>Indicates if storage autogrow is supported in this location. 'Enabled' means storage autogrow is supported. 'Disabled' stands for storage autogrow is not supported. Will be deprecated in the future. Look to Supported Features for 'StorageAutoGrowth'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedFastProvisioningEditions" /></td>
    <td><code>array</code></td>
    <td>List of compute tiers supporting fast provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedFeatures" /></td>
    <td><code>array</code></td>
    <td>Features supported.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedServerEditions" /></td>
    <td><code>array</code></td>
    <td>List of supported compute tiers.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedServerVersions" /></td>
    <td><code>array</code></td>
    <td>List of supported major versions of PostgreSQL database engine.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundantHaAndGeoBackupSupported" /></td>
    <td><code>string</code></td>
    <td>Indicates if high availability with zone redundancy is supported in conjunction with geographically redundant backups in this location. 'Enabled' means high availability with zone redundancy is supported in conjunction with geographically redundant backups is supported. 'Disabled' stands for high availability with zone redundancy is supported in conjunction with geographically redundant backups is not supported. Will be deprecated in the future. Look to Supported Features for 'ZoneRedundantHaAndGeoBackup'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundantHaSupported" /></td>
    <td><code>string</code></td>
    <td>Indicates if high availability with zone redundancy is supported in this location. 'Enabled' means high availability with zone redundancy is supported. 'Disabled' stands for high availability with zone redundancy is not supported. Will be deprecated in the future. Look to Supported Features for 'ZoneRedundantHa'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the capabilities available in a given location for a specific subscription.</td>
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
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The name of the location. Required.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists the capabilities available in a given location for a specific subscription.

```sql
SELECT
name,
fastProvisioningSupported,
geoBackupSupported,
onlineResizeSupported,
reason,
restricted,
status,
storageAutoGrowthSupported,
supportedFastProvisioningEditions,
supportedFeatures,
supportedServerEditions,
supportedServerVersions,
zoneRedundantHaAndGeoBackupSupported,
zoneRedundantHaSupported
FROM azure.postgresql_flexible_servers.capabilities_by_location
WHERE location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
