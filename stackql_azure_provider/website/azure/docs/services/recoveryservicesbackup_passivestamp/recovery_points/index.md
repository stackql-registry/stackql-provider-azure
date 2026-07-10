--- 
title: recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points
  - recoveryservicesbackup_passivestamp
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

Creates, updates, deletes, gets or lists a <code>recovery_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recovery_points" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup_passivestamp.recovery_points" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_access_token"
    values={[
        { label: 'get_access_token', value: 'get_access_token' }
    ]}
>
<TabItem value="get_access_token">

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
    <td>Resource Id represents the complete path to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="accessTokenString" /></td>
    <td><code>string</code></td>
    <td>Access token used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="bMSActiveRegion" /></td>
    <td><code>string</code></td>
    <td>Active region name of BMS Stamp.</td>
</tr>
<tr>
    <td><CopyableCode code="backupManagementType" /></td>
    <td><code>string</code></td>
    <td>Backup Management Type.</td>
</tr>
<tr>
    <td><CopyableCode code="containerName" /></td>
    <td><code>string</code></td>
    <td>Container Unique name.</td>
</tr>
<tr>
    <td><CopyableCode code="containerType" /></td>
    <td><code>string</code></td>
    <td>Container Type.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorServiceStampId" /></td>
    <td><code>string</code></td>
    <td>CoordinatorServiceStampId to be used by BCM in restore call.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorServiceStampUri" /></td>
    <td><code>string</code></td>
    <td>CoordinatorServiceStampUri to be used by BCM in restore call.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceContainerName" /></td>
    <td><code>string</code></td>
    <td>Datasource Container Unique Name.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceId" /></td>
    <td><code>string</code></td>
    <td>Datasource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceName" /></td>
    <td><code>string</code></td>
    <td>Datasource Friendly Name.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceType" /></td>
    <td><code>string</code></td>
    <td>Datasource Type.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="objectType" /></td>
    <td><code>string</code></td>
    <td>Type of the specific object - used for deserializing. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionContainerId" /></td>
    <td><code>integer</code></td>
    <td>Protected item container id.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionServiceStampId" /></td>
    <td><code>string</code></td>
    <td>ProtectionServiceStampId to be used by BCM in restore call.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionServiceStampUri" /></td>
    <td><code>string</code></td>
    <td>ProtectionServiceStampUri to be used by BCM in restore call.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPointId" /></td>
    <td><code>string</code></td>
    <td>Recovery Point Id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPointTime" /></td>
    <td><code>string</code></td>
    <td>Recovery Point Time.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroupName" /></td>
    <td><code>string</code></td>
    <td>Resource Group name of the source vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the source vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>Resource Name of the source vault.</td>
</tr>
<tr>
    <td><CopyableCode code="rpIsManagedVirtualMachine" /></td>
    <td><code>boolean</code></td>
    <td>Recovery point information: Managed virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="rpOriginalSAOption" /></td>
    <td><code>boolean</code></td>
    <td>Recovery point information: Original SA option.</td>
</tr>
<tr>
    <td><CopyableCode code="rpTierInformation" /></td>
    <td><code>object</code></td>
    <td>Recovery point Tier Information.</td>
</tr>
<tr>
    <td><CopyableCode code="rpVMSizeDescription" /></td>
    <td><code>string</code></td>
    <td>Recovery point information: VM size description.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription Id of the source vault.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenExtendedInformation" /></td>
    <td><code>string</code></td>
    <td>Extended Information about the token like FileSpec etc.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/...</td>
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
    <td><a href="#get_access_token"><CopyableCode code="get_access_token" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-recovery_point_id"><code>recovery_point_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the Access token for communication between BMS and Protection service. Returns the Access token for communication between BMS and Protection service.</td>
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
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>Name of the container. Required.</td>
</tr>
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name associated with the container. Required.</td>
</tr>
<tr id="parameter-protected_item_name">
    <td><CopyableCode code="protected_item_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Protected Item. Required.</td>
</tr>
<tr id="parameter-recovery_point_id">
    <td><CopyableCode code="recovery_point_id" /></td>
    <td><code>string</code></td>
    <td>Recovery Point Id. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group where the recovery services vault is present. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery services vault. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_access_token"
    values={[
        { label: 'get_access_token', value: 'get_access_token' }
    ]}
>
<TabItem value="get_access_token">

Returns the Access token for communication between BMS and Protection service. Returns the Access token for communication between BMS and Protection service.

```sql
SELECT
id,
name,
accessTokenString,
bMSActiveRegion,
backupManagementType,
containerName,
containerType,
coordinatorServiceStampId,
coordinatorServiceStampUri,
datasourceContainerName,
datasourceId,
datasourceName,
datasourceType,
eTag,
location,
objectType,
protectionContainerId,
protectionServiceStampId,
protectionServiceStampUri,
recoveryPointId,
recoveryPointTime,
resourceGroupName,
resourceId,
resourceName,
rpIsManagedVirtualMachine,
rpOriginalSAOption,
rpTierInformation,
rpVMSizeDescription,
subscriptionId,
tags,
tokenExtendedInformation,
type
FROM azure.recoveryservicesbackup_passivestamp.recovery_points
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND protected_item_name = '{{ protected_item_name }}' -- required
AND recovery_point_id = '{{ recovery_point_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
