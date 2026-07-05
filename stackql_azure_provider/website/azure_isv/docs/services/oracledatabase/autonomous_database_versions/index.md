--- 
title: autonomous_database_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_versions
  - oracledatabase
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

Creates, updates, deletes, gets or lists an <code>autonomous_database_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="autonomous_database_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracledatabase.autonomous_database_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_location', value: 'list_by_location' }
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
    <td><CopyableCode code="dbWorkload" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database workload type. Known values are: "OLTP", "DW", "AJD", and "APEX". (OLTP, DW, AJD, APEX)</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultForFree" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software's default is free.</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultForPaid" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software's default is paid.</td>
</tr>
<tr>
    <td><CopyableCode code="isFreeTierEnabled" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software can be used for Always-Free Autonomous Databases.</td>
</tr>
<tr>
    <td><CopyableCode code="isPaidEnabled" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software has payments enabled.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Supported Autonomous Db versions. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_location">

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
    <td><CopyableCode code="dbWorkload" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database workload type. Known values are: "OLTP", "DW", "AJD", and "APEX". (OLTP, DW, AJD, APEX)</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultForFree" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software's default is free.</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultForPaid" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software's default is paid.</td>
</tr>
<tr>
    <td><CopyableCode code="isFreeTierEnabled" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software can be used for Always-Free Autonomous Databases.</td>
</tr>
<tr>
    <td><CopyableCode code="isPaidEnabled" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software has payments enabled.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Supported Autonomous Db versions. Required.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-autonomousdbversionsname"><code>autonomousdbversionsname</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AutonomousDbVersion.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AutonomousDbVersion resources by SubscriptionLocationResource.</td>
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
<tr id="parameter-autonomousdbversionsname">
    <td><CopyableCode code="autonomousdbversionsname" /></td>
    <td><code>string</code></td>
    <td>AutonomousDbVersion name. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
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
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="get">

Get a AutonomousDbVersion.

```sql
SELECT
id,
name,
dbWorkload,
isDefaultForFree,
isDefaultForPaid,
isFreeTierEnabled,
isPaidEnabled,
systemData,
type,
version
FROM azure_isv.oracledatabase.autonomous_database_versions
WHERE location = '{{ location }}' -- required
AND autonomousdbversionsname = '{{ autonomousdbversionsname }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_location">

List AutonomousDbVersion resources by SubscriptionLocationResource.

```sql
SELECT
id,
name,
dbWorkload,
isDefaultForFree,
isDefaultForPaid,
isFreeTierEnabled,
isPaidEnabled,
systemData,
type,
version
FROM azure_isv.oracledatabase.autonomous_database_versions
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
