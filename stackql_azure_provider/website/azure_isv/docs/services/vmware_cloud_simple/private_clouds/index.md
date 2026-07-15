--- 
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>private_clouds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_clouds" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.private_clouds" /></td></tr>
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
    <td>Azure Id, e.g. "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Private cloud name.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneId" /></td>
    <td><code>string</code></td>
    <td>Availability Zone id, e.g. "az1".</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneName" /></td>
    <td><code>string</code></td>
    <td>Availability Zone name, e.g. "Availability Zone 1".</td>
</tr>
<tr>
    <td><CopyableCode code="clustersNumber" /></td>
    <td><code>integer</code></td>
    <td>Number of clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>User's emails who created cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>When private cloud was created.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServers" /></td>
    <td><code>array</code></td>
    <td>Array of DNS servers.</td>
</tr>
<tr>
    <td><CopyableCode code="expires" /></td>
    <td><code>string</code></td>
    <td>Expiration date of PC.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where private cloud created, e.g "westus".</td>
</tr>
<tr>
    <td><CopyableCode code="nsxType" /></td>
    <td><code>string</code></td>
    <td>Nsx Type, e.g. "Advanced".</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupId" /></td>
    <td><code>string</code></td>
    <td>Placement Group id, e.g. "n1".</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupName" /></td>
    <td><code>string</code></td>
    <td>Placement Group name.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Id of a private cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcePools" /></td>
    <td><code>array</code></td>
    <td>The list of Resource Pools.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Private Cloud state, e.g. "operational".</td>
</tr>
<tr>
    <td><CopyableCode code="totalCpuCores" /></td>
    <td><code>integer</code></td>
    <td>Number of cores.</td>
</tr>
<tr>
    <td><CopyableCode code="totalNodes" /></td>
    <td><code>integer</code></td>
    <td>Number of nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRam" /></td>
    <td><code>integer</code></td>
    <td>Memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorage" /></td>
    <td><code>number</code></td>
    <td>Disk space in TB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure Resource type. Default value is "Microsoft.VMwareCloudSimple/privateClouds".</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereVersion" /></td>
    <td><code>string</code></td>
    <td>e.g. "6.5u2".</td>
</tr>
<tr>
    <td><CopyableCode code="vcenterFqdn" /></td>
    <td><code>string</code></td>
    <td>FQDN for vcenter access.</td>
</tr>
<tr>
    <td><CopyableCode code="vcenterRefid" /></td>
    <td><code>string</code></td>
    <td>Vcenter ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineTemplates" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Machine Templates.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Networks.</td>
</tr>
<tr>
    <td><CopyableCode code="vrOpsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is Vrops enabled/disabled.</td>
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
    <td>Azure Id, e.g. "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Private cloud name.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneId" /></td>
    <td><code>string</code></td>
    <td>Availability Zone id, e.g. "az1".</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneName" /></td>
    <td><code>string</code></td>
    <td>Availability Zone name, e.g. "Availability Zone 1".</td>
</tr>
<tr>
    <td><CopyableCode code="clustersNumber" /></td>
    <td><code>integer</code></td>
    <td>Number of clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>User's emails who created cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>When private cloud was created.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServers" /></td>
    <td><code>array</code></td>
    <td>Array of DNS servers.</td>
</tr>
<tr>
    <td><CopyableCode code="expires" /></td>
    <td><code>string</code></td>
    <td>Expiration date of PC.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where private cloud created, e.g "westus".</td>
</tr>
<tr>
    <td><CopyableCode code="nsxType" /></td>
    <td><code>string</code></td>
    <td>Nsx Type, e.g. "Advanced".</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupId" /></td>
    <td><code>string</code></td>
    <td>Placement Group id, e.g. "n1".</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupName" /></td>
    <td><code>string</code></td>
    <td>Placement Group name.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Id of a private cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcePools" /></td>
    <td><code>array</code></td>
    <td>The list of Resource Pools.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Private Cloud state, e.g. "operational".</td>
</tr>
<tr>
    <td><CopyableCode code="totalCpuCores" /></td>
    <td><code>integer</code></td>
    <td>Number of cores.</td>
</tr>
<tr>
    <td><CopyableCode code="totalNodes" /></td>
    <td><code>integer</code></td>
    <td>Number of nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRam" /></td>
    <td><code>integer</code></td>
    <td>Memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorage" /></td>
    <td><code>number</code></td>
    <td>Disk space in TB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure Resource type. Default value is "Microsoft.VMwareCloudSimple/privateClouds".</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereVersion" /></td>
    <td><code>string</code></td>
    <td>e.g. "6.5u2".</td>
</tr>
<tr>
    <td><CopyableCode code="vcenterFqdn" /></td>
    <td><code>string</code></td>
    <td>FQDN for vcenter access.</td>
</tr>
<tr>
    <td><CopyableCode code="vcenterRefid" /></td>
    <td><code>string</code></td>
    <td>Vcenter ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineTemplates" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Machine Templates.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Networks.</td>
</tr>
<tr>
    <td><CopyableCode code="vrOpsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is Vrops enabled/disabled.</td>
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
    <td><a href="#parameter-pc_name"><code>pc_name</code></a>, <a href="#parameter-region_id"><code>region_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements private cloud GET method. Returns private cloud by its name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-region_id"><code>region_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements private cloud list GET method. Returns list of private clouds in particular region.</td>
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
<tr id="parameter-pc_name">
    <td><CopyableCode code="pc_name" /></td>
    <td><code>string</code></td>
    <td>The private cloud name. Required.</td>
</tr>
<tr id="parameter-region_id">
    <td><CopyableCode code="region_id" /></td>
    <td><code>string</code></td>
    <td>The region Id (westus, eastus). Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Implements private cloud GET method. Returns private cloud by its name.

```sql
SELECT
id,
name,
availabilityZoneId,
availabilityZoneName,
clustersNumber,
createdBy,
createdOn,
dnsServers,
expires,
location,
nsxType,
placementGroupId,
placementGroupName,
privateCloudId,
resourcePools,
state,
totalCpuCores,
totalNodes,
totalRam,
totalStorage,
type,
vSphereVersion,
vcenterFqdn,
vcenterRefid,
virtualMachineTemplates,
virtualNetworks,
vrOpsEnabled
FROM azure_isv.vmware_cloud_simple.private_clouds
WHERE pc_name = '{{ pc_name }}' -- required
AND region_id = '{{ region_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Implements private cloud list GET method. Returns list of private clouds in particular region.

```sql
SELECT
id,
name,
availabilityZoneId,
availabilityZoneName,
clustersNumber,
createdBy,
createdOn,
dnsServers,
expires,
location,
nsxType,
placementGroupId,
placementGroupName,
privateCloudId,
resourcePools,
state,
totalCpuCores,
totalNodes,
totalRam,
totalStorage,
type,
vSphereVersion,
vcenterFqdn,
vcenterRefid,
virtualMachineTemplates,
virtualNetworks,
vrOpsEnabled
FROM azure_isv.vmware_cloud_simple.private_clouds
WHERE region_id = '{{ region_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
