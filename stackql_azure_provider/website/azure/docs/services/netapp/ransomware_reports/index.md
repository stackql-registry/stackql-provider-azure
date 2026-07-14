--- 
title: ransomware_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - ransomware_reports
  - netapp
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

Creates, updates, deletes, gets or lists a <code>ransomware_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ransomware_reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.ransomware_reports" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clearedCount" /></td>
    <td><code>integer</code></td>
    <td>The number of cleared suspects identified by the ARP report.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date and time of the report.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedCount" /></td>
    <td><code>integer</code></td>
    <td>The number of suspects identified by the ARP report.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>Severity of the Advanced Ransomware Protection (ARP) report. Known values are: "None", "Low", "Moderate", and "High". (None, Low, Moderate, High)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of the Advanced Ransomware Protection (ARP) report. Known values are: "Active" and "Resolved". (Active, Resolved)</td>
</tr>
<tr>
    <td><CopyableCode code="suspects" /></td>
    <td><code>array</code></td>
    <td>Suspects identified in an ARP report.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clearedCount" /></td>
    <td><code>integer</code></td>
    <td>The number of cleared suspects identified by the ARP report.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date and time of the report.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedCount" /></td>
    <td><code>integer</code></td>
    <td>The number of suspects identified by the ARP report.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>Severity of the Advanced Ransomware Protection (ARP) report. Known values are: "None", "Low", "Moderate", and "High". (None, Low, Moderate, High)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of the Advanced Ransomware Protection (ARP) report. Known values are: "Active" and "Resolved". (Active, Resolved)</td>
</tr>
<tr>
    <td><CopyableCode code="suspects" /></td>
    <td><code>array</code></td>
    <td>Suspects identified in an ARP report.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-ransomware_report_name"><code>ransomware_report_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get details of the specified ransomware report (ARP) ARP reports are created with a list of suspected files when it detects any combination of high data entropy, abnormal volume activity with data encryption, and unusual file extensions. ARP creates snapshots named Anti_ransomware_backup when it detects a potential ransomware threat. You can use one of these ARP snapshots or another snapshot of your volume to restore data.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all ransomware reports for the volume Returns a list of the Advanced Ransomware Protection (ARP) reports for the volume. ARP reports are created with a list of suspected files when it detects any combination of high data entropy, abnormal volume activity with data encryption, and unusual file extensions. ARP creates snapshots named Anti_ransomware_backup when it detects a potential ransomware threat. You can use one of these ARP snapshots or another snapshot of your volume to restore data".</td>
</tr>
<tr>
    <td><a href="#clear_suspects"><CopyableCode code="clear_suspects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-ransomware_report_name"><code>ransomware_report_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resolution"><code>resolution</code></a>, <a href="#parameter-extensions"><code>extensions</code></a></td>
    <td></td>
    <td>Clear ransomware suspects for the given Advanced Ransomware Protection report. You should evaluate the report to determine whether the activity is acceptable (false positive) or whether an attack seems malicious. ARP creates snapshots named Anti_ransomware_backup when it detects a potential ransomware threat. You can use one of these ARP snapshots or another snapshot of your volume to restore data",.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NetApp account. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capacity pool. Required.</td>
</tr>
<tr id="parameter-ransomware_report_name">
    <td><CopyableCode code="ransomware_report_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ransomware report. Required.</td>
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
<tr id="parameter-volume_name">
    <td><CopyableCode code="volume_name" /></td>
    <td><code>string</code></td>
    <td>The name of the volume. Required.</td>
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

Get details of the specified ransomware report (ARP) ARP reports are created with a list of suspected files when it detects any combination of high data entropy, abnormal volume activity with data encryption, and unusual file extensions. ARP creates snapshots named Anti_ransomware_backup when it detects a potential ransomware threat. You can use one of these ARP snapshots or another snapshot of your volume to restore data.

```sql
SELECT
id,
name,
clearedCount,
eventTime,
provisioningState,
reportedCount,
severity,
state,
suspects,
systemData,
type
FROM azure.netapp.ransomware_reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND ransomware_report_name = '{{ ransomware_report_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all ransomware reports for the volume Returns a list of the Advanced Ransomware Protection (ARP) reports for the volume. ARP reports are created with a list of suspected files when it detects any combination of high data entropy, abnormal volume activity with data encryption, and unusual file extensions. ARP creates snapshots named Anti_ransomware_backup when it detects a potential ransomware threat. You can use one of these ARP snapshots or another snapshot of your volume to restore data".

```sql
SELECT
id,
name,
clearedCount,
eventTime,
provisioningState,
reportedCount,
severity,
state,
suspects,
systemData,
type
FROM azure.netapp.ransomware_reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="clear_suspects"
    values={[
        { label: 'clear_suspects', value: 'clear_suspects' }
    ]}
>
<TabItem value="clear_suspects">

Clear ransomware suspects for the given Advanced Ransomware Protection report. You should evaluate the report to determine whether the activity is acceptable (false positive) or whether an attack seems malicious. ARP creates snapshots named Anti_ransomware_backup when it detects a potential ransomware threat. You can use one of these ARP snapshots or another snapshot of your volume to restore data",.

```sql
EXEC azure.netapp.ransomware_reports.clear_suspects 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@ransomware_report_name='{{ ransomware_report_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resolution": "{{ resolution }}", 
"extensions": "{{ extensions }}"
}'
;
```
</TabItem>
</Tabs>
