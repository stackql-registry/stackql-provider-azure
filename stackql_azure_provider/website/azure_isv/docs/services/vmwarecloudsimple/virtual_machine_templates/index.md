--- 
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - vmwarecloudsimple
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmwarecloudsimple.virtual_machine_templates" /></td></tr>
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
    <td>virtual machine template id (privateCloudId:vsphereId).</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;virtualMachineTemplateName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="amountOfRam" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory.</td>
</tr>
<tr>
    <td><CopyableCode code="controllers" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disk Controllers.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of Virtual Machine Template.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks.</td>
</tr>
<tr>
    <td><CopyableCode code="exposeToGuestVM" /></td>
    <td><code>boolean</code></td>
    <td>Expose Guest OS or not.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOS" /></td>
    <td><code>string</code></td>
    <td>The Guest OS.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOSType" /></td>
    <td><code>string</code></td>
    <td>The Guest OS types.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region.</td>
</tr>
<tr>
    <td><CopyableCode code="nics" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual NICs.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>path to folder.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>The Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereNetworks" /></td>
    <td><code>array</code></td>
    <td>The list of VSphere networks.</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereTags" /></td>
    <td><code>array</code></td>
    <td>The tags from VSphere.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwaretools" /></td>
    <td><code>string</code></td>
    <td>The VMware tools version.</td>
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
    <td>virtual machine template id (privateCloudId:vsphereId).</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;virtualMachineTemplateName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="amountOfRam" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory.</td>
</tr>
<tr>
    <td><CopyableCode code="controllers" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disk Controllers.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of Virtual Machine Template.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks.</td>
</tr>
<tr>
    <td><CopyableCode code="exposeToGuestVM" /></td>
    <td><code>boolean</code></td>
    <td>Expose Guest OS or not.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOS" /></td>
    <td><code>string</code></td>
    <td>The Guest OS.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOSType" /></td>
    <td><code>string</code></td>
    <td>The Guest OS types.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region.</td>
</tr>
<tr>
    <td><CopyableCode code="nics" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual NICs.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>path to folder.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>The Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereNetworks" /></td>
    <td><code>array</code></td>
    <td>The list of VSphere networks.</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereTags" /></td>
    <td><code>array</code></td>
    <td>The tags from VSphere.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwaretools" /></td>
    <td><code>string</code></td>
    <td>The VMware tools version.</td>
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
    <td><a href="#parameter-region_id"><code>region_id</code></a>, <a href="#parameter-pc_name"><code>pc_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements virtual machine template GET method. Returns virtual machine templates by its name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pc_name"><code>pc_name</code></a>, <a href="#parameter-region_id"><code>region_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourcePoolName"><code>resourcePoolName</code></a></td>
    <td></td>
    <td>Implements list of available VM templates. Returns list of virtual machine templates in region for private cloud.</td>
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
<tr id="parameter-resourcePoolName">
    <td><CopyableCode code="resourcePoolName" /></td>
    <td><code>string</code></td>
    <td>Resource pool used to derive vSphere cluster which contains VM templates. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_machine_template_name">
    <td><CopyableCode code="virtual_machine_template_name" /></td>
    <td><code>string</code></td>
    <td>virtual machine template id (vsphereId). Required.</td>
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

Implements virtual machine template GET method. Returns virtual machine templates by its name.

```sql
SELECT
id,
name,
amountOfRam,
controllers,
description,
disks,
exposeToGuestVM,
guestOS,
guestOSType,
location,
nics,
numberOfCores,
path,
privateCloudId,
type,
vSphereNetworks,
vSphereTags,
vmwaretools
FROM azure_isv.vmwarecloudsimple.virtual_machine_templates
WHERE region_id = '{{ region_id }}' -- required
AND pc_name = '{{ pc_name }}' -- required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Implements list of available VM templates. Returns list of virtual machine templates in region for private cloud.

```sql
SELECT
id,
name,
amountOfRam,
controllers,
description,
disks,
exposeToGuestVM,
guestOS,
guestOSType,
location,
nics,
numberOfCores,
path,
privateCloudId,
type,
vSphereNetworks,
vSphereTags,
vmwaretools
FROM azure_isv.vmwarecloudsimple.virtual_machine_templates
WHERE pc_name = '{{ pc_name }}' -- required
AND region_id = '{{ region_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND resourcePoolName = '{{ resourcePoolName }}' -- required
;
```
</TabItem>
</Tabs>
