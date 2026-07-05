--- 
title: bastion_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_hosts
  - network
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

Creates, updates, deletes, gets or lists a <code>bastion_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bastion_hosts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.bastion_hosts" /></td></tr>
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
    <td><CopyableCode code="disableCopyPaste" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Copy/Paste feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsName" /></td>
    <td><code>string</code></td>
    <td>FQDN for the endpoint on which bastion host is accessible.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFileCopy" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable File Copy feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIpConnect" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable IP Connect feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableKerberos" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Kerberos feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateOnlyBastion" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Private Only feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSessionRecording" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Session Recording feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableShareableLink" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Shareable Link of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableTunneling" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Tunneling feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configuration of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>:vartype network_acls: ~azure.mgmt.network.models.BastionHostPropertiesFormatNetworkAcls</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the bastion host resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnits" /></td>
    <td><code>integer</code></td>
    <td>The scale units for the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of this Bastion Host.</td>
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
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><CopyableCode code="disableCopyPaste" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Copy/Paste feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsName" /></td>
    <td><code>string</code></td>
    <td>FQDN for the endpoint on which bastion host is accessible.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFileCopy" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable File Copy feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIpConnect" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable IP Connect feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableKerberos" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Kerberos feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateOnlyBastion" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Private Only feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSessionRecording" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Session Recording feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableShareableLink" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Shareable Link of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableTunneling" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Tunneling feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configuration of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>:vartype network_acls: ~azure.mgmt.network.models.BastionHostPropertiesFormatNetworkAcls</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the bastion host resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnits" /></td>
    <td><code>integer</code></td>
    <td>The scale units for the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of this Bastion Host.</td>
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
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><CopyableCode code="disableCopyPaste" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Copy/Paste feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsName" /></td>
    <td><code>string</code></td>
    <td>FQDN for the endpoint on which bastion host is accessible.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFileCopy" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable File Copy feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIpConnect" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable IP Connect feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableKerberos" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Kerberos feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateOnlyBastion" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Private Only feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSessionRecording" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Session Recording feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableShareableLink" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Shareable Link of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableTunneling" /></td>
    <td><code>boolean</code></td>
    <td>Enable/Disable Tunneling feature of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configuration of the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>:vartype network_acls: ~azure.mgmt.network.models.BastionHostPropertiesFormatNetworkAcls</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the bastion host resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnits" /></td>
    <td><code>integer</code></td>
    <td>The scale units for the Bastion Host resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of this Bastion Host.</td>
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
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified Bastion Host.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Bastion Hosts in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Bastion Hosts in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Bastion Host.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates Tags for BastionHost resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Bastion Host.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Bastion Host.</td>
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
<tr id="parameter-bastion_host_name">
    <td><CopyableCode code="bastion_host_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bastion Host. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified Bastion Host.

```sql
SELECT
id,
name,
disableCopyPaste,
dnsName,
enableFileCopy,
enableIpConnect,
enableKerberos,
enablePrivateOnlyBastion,
enableSessionRecording,
enableShareableLink,
enableTunneling,
etag,
ipConfigurations,
location,
networkAcls,
provisioningState,
scaleUnits,
sku,
tags,
type,
virtualNetwork,
zones
FROM azure.network.bastion_hosts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND bastion_host_name = '{{ bastion_host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all Bastion Hosts in a resource group.

```sql
SELECT
id,
name,
disableCopyPaste,
dnsName,
enableFileCopy,
enableIpConnect,
enableKerberos,
enablePrivateOnlyBastion,
enableSessionRecording,
enableShareableLink,
enableTunneling,
etag,
ipConfigurations,
location,
networkAcls,
provisioningState,
scaleUnits,
sku,
tags,
type,
virtualNetwork,
zones
FROM azure.network.bastion_hosts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Bastion Hosts in a subscription.

```sql
SELECT
id,
name,
disableCopyPaste,
dnsName,
enableFileCopy,
enableIpConnect,
enableKerberos,
enablePrivateOnlyBastion,
enableSessionRecording,
enableShareableLink,
enableTunneling,
etag,
ipConfigurations,
location,
networkAcls,
provisioningState,
scaleUnits,
sku,
tags,
type,
virtualNetwork,
zones
FROM azure.network.bastion_hosts
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

Creates or updates the specified Bastion Host.

```sql
INSERT INTO azure.network.bastion_hosts (
id,
location,
tags,
properties,
zones,
sku,
resource_group_name,
bastion_host_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ zones }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ bastion_host_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
sku,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: bastion_hosts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bastion_hosts resource.
    - name: bastion_host_name
      value: "{{ bastion_host_name }}"
      description: Required parameter for the bastion_hosts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bastion_hosts resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Represents the bastion host resource.
      value:
        ipConfigurations:
          - id: "{{ id }}"
            properties:
              subnet:
                id: "{{ id }}"
              publicIPAddress:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
              privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        dnsName: "{{ dnsName }}"
        virtualNetwork:
          id: "{{ id }}"
        networkAcls:
          ipRules:
            - addressPrefix: "{{ addressPrefix }}"
        provisioningState: "{{ provisioningState }}"
        scaleUnits: {{ scaleUnits }}
        disableCopyPaste: {{ disableCopyPaste }}
        enableFileCopy: {{ enableFileCopy }}
        enableIpConnect: {{ enableIpConnect }}
        enableShareableLink: {{ enableShareableLink }}
        enableTunneling: {{ enableTunneling }}
        enableKerberos: {{ enableKerberos }}
        enableSessionRecording: {{ enableSessionRecording }}
        enablePrivateOnlyBastion: {{ enablePrivateOnlyBastion }}
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting where the resource needs to come from.
    - name: sku
      description: |
        The sku of this Bastion Host.
      value:
        name: "{{ name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates Tags for BastionHost resource.

```sql
UPDATE azure.network.bastion_hosts
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND bastion_host_name = '{{ bastion_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
tags,
type,
zones;
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

Creates or updates the specified Bastion Host.

```sql
REPLACE azure.network.bastion_hosts
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
zones = '{{ zones }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND bastion_host_name = '{{ bastion_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
tags,
type,
zones;
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

Deletes the specified Bastion Host.

```sql
DELETE FROM azure.network.bastion_hosts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND bastion_host_name = '{{ bastion_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
