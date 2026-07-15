--- 
title: db_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - db_versions
  - oracle_database
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

Creates, updates, deletes, gets or lists a <code>db_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="db_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.db_versions" /></td></tr>
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
    <td><CopyableCode code="isLatestForMajorVersion" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software is the latest version for a release.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreviewDbVersion" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software is the preview version.</td>
</tr>
<tr>
    <td><CopyableCode code="isUpgradeSupported" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software is supported for Upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsPdb" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software supports pluggable databases.</td>
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
    <td>A valid Oracle Database version. Required.</td>
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
    <td><CopyableCode code="isLatestForMajorVersion" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software is the latest version for a release.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreviewDbVersion" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software is the preview version.</td>
</tr>
<tr>
    <td><CopyableCode code="isUpgradeSupported" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software is supported for Upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsPdb" /></td>
    <td><code>boolean</code></td>
    <td>True if this version of the Oracle Database software supports pluggable databases.</td>
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
    <td>A valid Oracle Database version. Required.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-dbversionsname"><code>dbversionsname</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DbVersion.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-dbSystemShape"><code>dbSystemShape</code></a>, <a href="#parameter-dbSystemId"><code>dbSystemId</code></a>, <a href="#parameter-storageManagement"><code>storageManagement</code></a>, <a href="#parameter-isUpgradeSupported"><code>isUpgradeSupported</code></a>, <a href="#parameter-isDatabaseSoftwareImageSupported"><code>isDatabaseSoftwareImageSupported</code></a>, <a href="#parameter-shapeFamily"><code>shapeFamily</code></a></td>
    <td>List DbVersion resources by SubscriptionLocationResource.</td>
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
<tr id="parameter-dbversionsname">
    <td><CopyableCode code="dbversionsname" /></td>
    <td><code>string</code></td>
    <td>DbVersion name. Required.</td>
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
<tr id="parameter-dbSystemId">
    <td><CopyableCode code="dbSystemId" /></td>
    <td><code>string</code></td>
    <td>The DB system AzureId. If provided, filters the results to the set of database versions which are supported for the DB system. Default value is None.</td>
</tr>
<tr id="parameter-dbSystemShape">
    <td><CopyableCode code="dbSystemShape" /></td>
    <td><code>string</code></td>
    <td>If provided, filters the results to the set of database versions which are supported for the given shape. e.g., VM.Standard.E5.Flex. "VM.Standard.x86" Default value is None.</td>
</tr>
<tr id="parameter-isDatabaseSoftwareImageSupported">
    <td><CopyableCode code="isDatabaseSoftwareImageSupported" /></td>
    <td><code>boolean</code></td>
    <td>If true, filters the results to the set of Oracle Database versions that are supported for the database software images. Default value is None.</td>
</tr>
<tr id="parameter-isUpgradeSupported">
    <td><CopyableCode code="isUpgradeSupported" /></td>
    <td><code>boolean</code></td>
    <td>If true, filters the results to the set of database versions which are supported for Upgrade. Default value is None.</td>
</tr>
<tr id="parameter-shapeFamily">
    <td><CopyableCode code="shapeFamily" /></td>
    <td><code>string</code></td>
    <td>If provided, filters the results to the set of database versions which are supported for the given shape family. Known values are: "EXADATA", "EXADB_XS", "SINGLENODE", and "VIRTUALMACHINE". Default value is None.</td>
</tr>
<tr id="parameter-storageManagement">
    <td><CopyableCode code="storageManagement" /></td>
    <td><code>string</code></td>
    <td>The DB system storage management option. Used to list database versions available for that storage manager. Valid values are ASM and LVM. "LVM" Default value is None.</td>
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

Get a DbVersion.

```sql
SELECT
id,
name,
isLatestForMajorVersion,
isPreviewDbVersion,
isUpgradeSupported,
supportsPdb,
systemData,
type,
version
FROM azure_isv.oracle_database.db_versions
WHERE location = '{{ location }}' -- required
AND dbversionsname = '{{ dbversionsname }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_location">

List DbVersion resources by SubscriptionLocationResource.

```sql
SELECT
id,
name,
isLatestForMajorVersion,
isPreviewDbVersion,
isUpgradeSupported,
supportsPdb,
systemData,
type,
version
FROM azure_isv.oracle_database.db_versions
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND dbSystemShape = '{{ dbSystemShape }}'
AND dbSystemId = '{{ dbSystemId }}'
AND storageManagement = '{{ storageManagement }}'
AND isUpgradeSupported = '{{ isUpgradeSupported }}'
AND isDatabaseSoftwareImageSupported = '{{ isDatabaseSoftwareImageSupported }}'
AND shapeFamily = '{{ shapeFamily }}'
;
```
</TabItem>
</Tabs>
