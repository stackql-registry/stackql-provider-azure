--- 
title: report
hide_title: false
hide_table_of_contents: false
keywords:
  - report
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

Creates, updates, deletes, gets or lists a <code>report</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="report" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.report" /></td></tr>
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
    <td><CopyableCode code="certRecords" /></td>
    <td><code>array</code></td>
    <td>List of synchronized certification records.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>object</code></td>
    <td>Report compliance status.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>List of report error codes.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTriggerTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Report last collection trigger time.</td>
</tr>
<tr>
    <td><CopyableCode code="nextTriggerTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Report next collection trigger time.</td>
</tr>
<tr>
    <td><CopyableCode code="offerGuid" /></td>
    <td><code>string</code></td>
    <td>A list of comma-separated offerGuids indicates a series of offerGuids that map to the report. For example, "00000000-0000-0000-0000-000000000001,00000000-0000-0000-0000-000000000002" and "00000000-0000-0000-0000-000000000003".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>List of resource data. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Report status. Known values are: "Active", "Failed", "Reviewing", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageInfo" /></td>
    <td><code>object</code></td>
    <td>The information of 'bring your own storage' account binding to the report.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription Ids.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Report's tenant id.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>Report collection trigger time's time zone, the available list can be obtained by executing "Get-TimeZone -ListAvailable" in PowerShell. An example of valid timezone id is "Pacific Standard Time". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Report collection trigger time. Required.</td>
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
    <td><CopyableCode code="certRecords" /></td>
    <td><code>array</code></td>
    <td>List of synchronized certification records.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>object</code></td>
    <td>Report compliance status.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>List of report error codes.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTriggerTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Report last collection trigger time.</td>
</tr>
<tr>
    <td><CopyableCode code="nextTriggerTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Report next collection trigger time.</td>
</tr>
<tr>
    <td><CopyableCode code="offerGuid" /></td>
    <td><code>string</code></td>
    <td>A list of comma-separated offerGuids indicates a series of offerGuids that map to the report. For example, "00000000-0000-0000-0000-000000000001,00000000-0000-0000-0000-000000000002" and "00000000-0000-0000-0000-000000000003".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>List of resource data. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Report status. Known values are: "Active", "Failed", "Reviewing", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageInfo" /></td>
    <td><code>object</code></td>
    <td>The information of 'bring your own storage' account binding to the report.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription Ids.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Report's tenant id.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>Report collection trigger time's time zone, the available list can be obtained by executing "Get-TimeZone -ListAvailable" in PowerShell. An example of valid timezone id is "Pacific Standard Time". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Report collection trigger time. Required.</td>
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
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td></td>
    <td>Get the AppComplianceAutomation report and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-offerGuid"><code>offerGuid</code></a>, <a href="#parameter-reportCreatorTenantId"><code>reportCreatorTenantId</code></a></td>
    <td>Get the AppComplianceAutomation report list for the tenant.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td></td>
    <td>Update an exiting AppComplianceAutomation report.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td></td>
    <td>Delete an AppComplianceAutomation report.</td>
</tr>
<tr>
    <td><a href="#get_scoping_questions"><CopyableCode code="get_scoping_questions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td></td>
    <td>Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed.</td>
</tr>
<tr>
    <td><a href="#nested_resource_check_name_availability"><CopyableCode code="nested_resource_check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td></td>
    <td>Checks the report's nested resource name availability, e.g: Webhooks, Evidences, Snapshots.</td>
</tr>
<tr>
    <td><a href="#fix"><CopyableCode code="fix" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td></td>
    <td>Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed.</td>
</tr>
<tr>
    <td><a href="#sync_cert_record"><CopyableCode code="sync_cert_record" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-certRecord"><code>certRecord</code></a></td>
    <td></td>
    <td>Synchronize attestation record from app compliance.</td>
</tr>
<tr>
    <td><a href="#verify"><CopyableCode code="verify" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td></td>
    <td>Verify the AppComplianceAutomation report health status.</td>
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

Get the AppComplianceAutomation report and its properties.

```sql
SELECT
id,
name,
certRecords,
complianceStatus,
errors,
lastTriggerTime,
nextTriggerTime,
offerGuid,
provisioningState,
resources,
status,
storageInfo,
subscriptions,
systemData,
tenantId,
timeZone,
triggerTime,
type
FROM azure_extras.app_compliance_automation.report
WHERE report_name = '{{ report_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the AppComplianceAutomation report list for the tenant.

```sql
SELECT
id,
name,
certRecords,
complianceStatus,
errors,
lastTriggerTime,
nextTriggerTime,
offerGuid,
provisioningState,
resources,
status,
storageInfo,
subscriptions,
systemData,
tenantId,
timeZone,
triggerTime,
type
FROM azure_extras.app_compliance_automation.report
WHERE $skipToken = '{{ $skipToken }}'
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


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report.

```sql
INSERT INTO azure_extras.app_compliance_automation.report (
properties,
report_name
)
SELECT 
'{{ properties }}' /* required */,
'{{ report_name }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: report
  props:
    - name: report_name
      value: "{{ report_name }}"
      description: Required parameter for the report resource.
    - name: properties
      description: |
        Report property. Required.
      value:
        triggerTime: "{{ triggerTime }}"
        timeZone: "{{ timeZone }}"
        resources:
          - resourceId: "{{ resourceId }}"
            resourceType: "{{ resourceType }}"
            resourceKind: "{{ resourceKind }}"
            resourceOrigin: "{{ resourceOrigin }}"
            accountId: "{{ accountId }}"
        status: "{{ status }}"
        errors:
          - "{{ errors }}"
        tenantId: "{{ tenantId }}"
        offerGuid: "{{ offerGuid }}"
        nextTriggerTime: "{{ nextTriggerTime }}"
        lastTriggerTime: "{{ lastTriggerTime }}"
        subscriptions:
          - "{{ subscriptions }}"
        complianceStatus:
          m365:
            passedCount: {{ passedCount }}
            failedCount: {{ failedCount }}
            manualCount: {{ manualCount }}
            notApplicableCount: {{ notApplicableCount }}
            pendingCount: {{ pendingCount }}
        storageInfo:
          subscriptionId: "{{ subscriptionId }}"
          resourceGroup: "{{ resourceGroup }}"
          accountName: "{{ accountName }}"
          location: "{{ location }}"
        certRecords:
          - offerGuid: "{{ offerGuid }}"
            certificationStatus: "{{ certificationStatus }}"
            ingestionStatus: "{{ ingestionStatus }}"
            controls: "{{ controls }}"
        provisioningState: "{{ provisioningState }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an exiting AppComplianceAutomation report.

```sql
UPDATE azure_extras.app_compliance_automation.report
SET 
properties = '{{ properties }}'
WHERE 
report_name = '{{ report_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
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

Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report.

```sql
REPLACE azure_extras.app_compliance_automation.report
SET 
properties = '{{ properties }}'
WHERE 
report_name = '{{ report_name }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
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

Delete an AppComplianceAutomation report.

```sql
DELETE FROM azure_extras.app_compliance_automation.report
WHERE report_name = '{{ report_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_scoping_questions"
    values={[
        { label: 'get_scoping_questions', value: 'get_scoping_questions' },
        { label: 'nested_resource_check_name_availability', value: 'nested_resource_check_name_availability' },
        { label: 'fix', value: 'fix' },
        { label: 'sync_cert_record', value: 'sync_cert_record' },
        { label: 'verify', value: 'verify' }
    ]}
>
<TabItem value="get_scoping_questions">

Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed.

```sql
EXEC azure_extras.app_compliance_automation.report.get_scoping_questions 
@report_name='{{ report_name }}' --required
;
```
</TabItem>
<TabItem value="nested_resource_check_name_availability">

Checks the report's nested resource name availability, e.g: Webhooks, Evidences, Snapshots.

```sql
EXEC azure_extras.app_compliance_automation.report.nested_resource_check_name_availability 
@report_name='{{ report_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
<TabItem value="fix">

Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed.

```sql
EXEC azure_extras.app_compliance_automation.report.fix 
@report_name='{{ report_name }}' --required
;
```
</TabItem>
<TabItem value="sync_cert_record">

Synchronize attestation record from app compliance.

```sql
EXEC azure_extras.app_compliance_automation.report.sync_cert_record 
@report_name='{{ report_name }}' --required 
@@json=
'{
"certRecord": "{{ certRecord }}"
}'
;
```
</TabItem>
<TabItem value="verify">

Verify the AppComplianceAutomation report health status.

```sql
EXEC azure_extras.app_compliance_automation.report.verify 
@report_name='{{ report_name }}' --required
;
```
</TabItem>
</Tabs>
