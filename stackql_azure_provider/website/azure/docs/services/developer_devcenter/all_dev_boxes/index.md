--- 
title: all_dev_boxes
hide_title: false
hide_table_of_contents: false
keywords:
  - all_dev_boxes
  - developer_devcenter
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

Creates, updates, deletes, gets or lists an <code>all_dev_boxes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="all_dev_boxes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.all_dev_boxes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_all_dev_boxes_by_user"
    values={[
        { label: 'list_all_dev_boxes_by_user', value: 'list_all_dev_boxes_by_user' },
        { label: 'list_all_dev_boxes', value: 'list_all_dev_boxes' }
    ]}
>
<TabItem value="list_all_dev_boxes_by_user">

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
    <td>Display name for the Dev Box. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="actionState" /></td>
    <td><code>string</code></td>
    <td>The current action state of the Dev Box. This is state is based on previous action performed by user.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of this Dev Box.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Provisioning or action error details. Populated only for error states.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the Dev Box's hardware resources.</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether hibernate is enabled/disabled or unknown. Known values are: "Enabled", "Disabled", and "OsUnsupported". (Enabled, Disabled, OsUnsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Information about the image used for this Dev Box.</td>
</tr>
<tr>
    <td><CopyableCode code="localAdministrator" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the owner of the Dev Box is a local administrator. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region where this Dev Box is located. This will be the same region as the Virtual Network it is attached to.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type of this Dev Box. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="poolName" /></td>
    <td><code>string</code></td>
    <td>The name of the Dev Box pool this machine belongs to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The current power state of the Dev Box. Known values are: "Unknown", "Running", "Deallocated", "PoweredOff", and "Hibernated". (Unknown, Running, Deallocated, PoweredOff, Hibernated)</td>
</tr>
<tr>
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>Name of the project this Dev Box belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the Dev Box. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Updating", "Starting", "Stopping", "Provisioning", "ProvisionedWithWarning", "InGracePeriod", and "NotProvisioned". (Succeeded, Failed, Canceled, Creating, Deleting, Updating, Starting, Stopping, Provisioning, ProvisionedWithWarning, InGracePeriod, NotProvisioned)</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage settings for this Dev Box.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for the Dev Box. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>string</code></td>
    <td>The AAD object id of the user this Dev Box is assigned to.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all_dev_boxes">

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
    <td>Display name for the Dev Box. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="actionState" /></td>
    <td><code>string</code></td>
    <td>The current action state of the Dev Box. This is state is based on previous action performed by user.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of this Dev Box.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Provisioning or action error details. Populated only for error states.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the Dev Box's hardware resources.</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether hibernate is enabled/disabled or unknown. Known values are: "Enabled", "Disabled", and "OsUnsupported". (Enabled, Disabled, OsUnsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Information about the image used for this Dev Box.</td>
</tr>
<tr>
    <td><CopyableCode code="localAdministrator" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the owner of the Dev Box is a local administrator. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region where this Dev Box is located. This will be the same region as the Virtual Network it is attached to.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type of this Dev Box. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="poolName" /></td>
    <td><code>string</code></td>
    <td>The name of the Dev Box pool this machine belongs to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The current power state of the Dev Box. Known values are: "Unknown", "Running", "Deallocated", "PoweredOff", and "Hibernated". (Unknown, Running, Deallocated, PoweredOff, Hibernated)</td>
</tr>
<tr>
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>Name of the project this Dev Box belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the Dev Box. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Updating", "Starting", "Stopping", "Provisioning", "ProvisionedWithWarning", "InGracePeriod", and "NotProvisioned". (Succeeded, Failed, Canceled, Creating, Deleting, Updating, Starting, Stopping, Provisioning, ProvisionedWithWarning, InGracePeriod, NotProvisioned)</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage settings for this Dev Box.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for the Dev Box. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>string</code></td>
    <td>The AAD object id of the user this Dev Box is assigned to.</td>
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
    <td><a href="#list_all_dev_boxes_by_user"><CopyableCode code="list_all_dev_boxes_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists Dev Boxes in the Dev Center for a particular user.</td>
</tr>
<tr>
    <td><a href="#list_all_dev_boxes"><CopyableCode code="list_all_dev_boxes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists Dev Boxes that the caller has access to in the DevCenter.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The AAD object id of the user. If value is 'me', the identity is taken from the authentication context. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_all_dev_boxes_by_user"
    values={[
        { label: 'list_all_dev_boxes_by_user', value: 'list_all_dev_boxes_by_user' },
        { label: 'list_all_dev_boxes', value: 'list_all_dev_boxes' }
    ]}
>
<TabItem value="list_all_dev_boxes_by_user">

Lists Dev Boxes in the Dev Center for a particular user.

```sql
SELECT
name,
actionState,
createdTime,
error,
hardwareProfile,
hibernateSupport,
imageReference,
localAdministrator,
location,
osType,
poolName,
powerState,
projectName,
provisioningState,
storageProfile,
uniqueId,
user
FROM azure.developer_devcenter.all_dev_boxes
WHERE user_id = '{{ user_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_all_dev_boxes">

Lists Dev Boxes that the caller has access to in the DevCenter.

```sql
SELECT
name,
actionState,
createdTime,
error,
hardwareProfile,
hibernateSupport,
imageReference,
localAdministrator,
location,
osType,
poolName,
powerState,
projectName,
provisioningState,
storageProfile,
uniqueId,
user
FROM azure.developer_devcenter.all_dev_boxes
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
