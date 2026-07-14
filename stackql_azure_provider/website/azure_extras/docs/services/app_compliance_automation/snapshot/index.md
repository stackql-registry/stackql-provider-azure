--- 
title: snapshot
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot
  - app_compliance_automation
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>snapshot</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="snapshot" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.snapshot" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceResults" /></td>
    <td><code>array</code></td>
    <td>List of compliance results.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of resource creation (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="reportProperties" /></td>
    <td><code>object</code></td>
    <td>The report essential info.</td>
</tr>
<tr>
    <td><CopyableCode code="reportSystemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotName" /></td>
    <td><code>string</code></td>
    <td>Snapshot name.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceResults" /></td>
    <td><code>array</code></td>
    <td>List of compliance results.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of resource creation (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="reportProperties" /></td>
    <td><code>object</code></td>
    <td>The report essential info.</td>
</tr>
<tr>
    <td><CopyableCode code="reportSystemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotName" /></td>
    <td><code>string</code></td>
    <td>Snapshot name.</td>
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
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a></td>
    <td></td>
    <td>Get the AppComplianceAutomation snapshot and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-offerGuid"><code>offerGuid</code></a>, <a href="#parameter-reportCreatorTenantId"><code>reportCreatorTenantId</code></a></td>
    <td>Get the AppComplianceAutomation snapshot list.</td>
</tr>
<tr>
    <td><a href="#download"><CopyableCode code="download" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-downloadType"><code>downloadType</code></a></td>
    <td></td>
    <td>Download compliance needs from snapshot, like: Compliance Report, Resource List.</td>
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
<tr id="parameter-report_name">
    <td><CopyableCode code="report_name" /></td>
    <td><code>string</code></td>
    <td>Report Name. Required.</td>
</tr>
<tr id="parameter-snapshot_name">
    <td><CopyableCode code="snapshot_name" /></td>
    <td><code>string</code></td>
    <td>Snapshot Name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>OData order by query option. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>OData Select statement. Limits the properties on each entry to just those requested, e.g. ?$select=reportName,id. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip over when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-offerGuid">
    <td><CopyableCode code="offerGuid" /></td>
    <td><code>string</code></td>
    <td>The offerGuid which mapping to the reports. Default value is None.</td>
</tr>
<tr id="parameter-reportCreatorTenantId">
    <td><CopyableCode code="reportCreatorTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant id of the report creator. Default value is None.</td>
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

Get the AppComplianceAutomation snapshot and its properties.

```sql
SELECT
id,
name,
complianceResults,
createdAt,
provisioningState,
reportProperties,
reportSystemData,
snapshotName,
systemData,
type
FROM azure_extras.app_compliance_automation.snapshot
WHERE report_name = '{{ report_name }}' -- required
AND snapshot_name = '{{ snapshot_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the AppComplianceAutomation snapshot list.

```sql
SELECT
id,
name,
complianceResults,
createdAt,
provisioningState,
reportProperties,
reportSystemData,
snapshotName,
systemData,
type
FROM azure_extras.app_compliance_automation.snapshot
WHERE report_name = '{{ report_name }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
AND $select = '{{ $select }}'
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND offerGuid = '{{ offerGuid }}'
AND reportCreatorTenantId = '{{ reportCreatorTenantId }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="download"
    values={[
        { label: 'download', value: 'download' }
    ]}
>
<TabItem value="download">

Download compliance needs from snapshot, like: Compliance Report, Resource List.

```sql
EXEC azure_extras.app_compliance_automation.snapshot.download 
@report_name='{{ report_name }}' --required, 
@snapshot_name='{{ snapshot_name }}' --required 
@@json=
'{
"reportCreatorTenantId": "{{ reportCreatorTenantId }}", 
"downloadType": "{{ downloadType }}", 
"offerGuid": "{{ offerGuid }}"
}'
;
```
</TabItem>
</Tabs>
