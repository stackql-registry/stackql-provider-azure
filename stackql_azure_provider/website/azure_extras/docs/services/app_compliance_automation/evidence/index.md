--- 
title: evidence
hide_title: false
hide_table_of_contents: false
keywords:
  - evidence
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

Creates, updates, deletes, gets or lists an <code>evidence</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="evidence" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.evidence" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_report', value: 'list_by_report' }
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
    <td><CopyableCode code="controlId" /></td>
    <td><code>string</code></td>
    <td>Control id.</td>
</tr>
<tr>
    <td><CopyableCode code="evidenceType" /></td>
    <td><code>string</code></td>
    <td>Evidence type. Known values are: "File", "AutoCollectedEvidence", and "Data".</td>
</tr>
<tr>
    <td><CopyableCode code="extraData" /></td>
    <td><code>string</code></td>
    <td>Extra data considered as evidence.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>The path of the file in storage. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="responsibilityId" /></td>
    <td><code>string</code></td>
    <td>Responsibility id.</td>
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
<TabItem value="list_by_report">

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
    <td><CopyableCode code="controlId" /></td>
    <td><code>string</code></td>
    <td>Control id.</td>
</tr>
<tr>
    <td><CopyableCode code="evidenceType" /></td>
    <td><code>string</code></td>
    <td>Evidence type. Known values are: "File", "AutoCollectedEvidence", and "Data".</td>
</tr>
<tr>
    <td><CopyableCode code="extraData" /></td>
    <td><code>string</code></td>
    <td>Extra data considered as evidence.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>The path of the file in storage. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="responsibilityId" /></td>
    <td><code>string</code></td>
    <td>Responsibility id.</td>
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
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-evidence_name"><code>evidence_name</code></a></td>
    <td></td>
    <td>Get the evidence metadata.</td>
</tr>
<tr>
    <td><a href="#list_by_report"><CopyableCode code="list_by_report" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-offerGuid"><code>offerGuid</code></a>, <a href="#parameter-reportCreatorTenantId"><code>reportCreatorTenantId</code></a></td>
    <td>Returns a paginated list of evidences for a specified report.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-evidence_name"><code>evidence_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-offerGuid"><code>offerGuid</code></a>, <a href="#parameter-reportCreatorTenantId"><code>reportCreatorTenantId</code></a></td>
    <td>Create or Update an evidence a specified report.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-evidence_name"><code>evidence_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-offerGuid"><code>offerGuid</code></a>, <a href="#parameter-reportCreatorTenantId"><code>reportCreatorTenantId</code></a></td>
    <td>Create or Update an evidence a specified report.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-evidence_name"><code>evidence_name</code></a></td>
    <td></td>
    <td>Delete an existent evidence from a specified report.</td>
</tr>
<tr>
    <td><a href="#download"><CopyableCode code="download" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-evidence_name"><code>evidence_name</code></a></td>
    <td></td>
    <td>Download evidence file.</td>
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
<tr id="parameter-evidence_name">
    <td><CopyableCode code="evidence_name" /></td>
    <td><code>string</code></td>
    <td>The evidence name. Required.</td>
</tr>
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
        { label: 'list_by_report', value: 'list_by_report' }
    ]}
>
<TabItem value="get">

Get the evidence metadata.

```sql
SELECT
id,
name,
controlId,
evidenceType,
extraData,
filePath,
provisioningState,
responsibilityId,
systemData,
type
FROM azure_extras.app_compliance_automation.evidence
WHERE report_name = '{{ report_name }}' -- required
AND evidence_name = '{{ evidence_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_report">

Returns a paginated list of evidences for a specified report.

```sql
SELECT
id,
name,
controlId,
evidenceType,
extraData,
filePath,
provisioningState,
responsibilityId,
systemData,
type
FROM azure_extras.app_compliance_automation.evidence
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


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or Update an evidence a specified report.

```sql
INSERT INTO azure_extras.app_compliance_automation.evidence (
properties,
report_name,
evidence_name,
offerGuid,
reportCreatorTenantId
)
SELECT 
'{{ properties }}' /* required */,
'{{ report_name }}',
'{{ evidence_name }}',
'{{ offerGuid }}',
'{{ reportCreatorTenantId }}'
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
- name: evidence
  props:
    - name: report_name
      value: "{{ report_name }}"
      description: Required parameter for the evidence resource.
    - name: evidence_name
      value: "{{ evidence_name }}"
      description: Required parameter for the evidence resource.
    - name: properties
      description: |
        Evidence property. Required.
      value:
        evidenceType: "{{ evidenceType }}"
        filePath: "{{ filePath }}"
        extraData: "{{ extraData }}"
        controlId: "{{ controlId }}"
        responsibilityId: "{{ responsibilityId }}"
        provisioningState: "{{ provisioningState }}"
    - name: offerGuid
      value: "{{ offerGuid }}"
      description: The offerGuid which mapping to the reports. Default value is None.
      description: The offerGuid which mapping to the reports. Default value is None.
    - name: reportCreatorTenantId
      value: "{{ reportCreatorTenantId }}"
      description: The tenant id of the report creator. Default value is None.
      description: The tenant id of the report creator. Default value is None.
`}</CodeBlock>

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

Create or Update an evidence a specified report.

```sql
REPLACE azure_extras.app_compliance_automation.evidence
SET 
properties = '{{ properties }}'
WHERE 
report_name = '{{ report_name }}' --required
AND evidence_name = '{{ evidence_name }}' --required
AND properties = '{{ properties }}' --required
AND offerGuid = '{{ offerGuid}}'
AND reportCreatorTenantId = '{{ reportCreatorTenantId}}'
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

Delete an existent evidence from a specified report.

```sql
DELETE FROM azure_extras.app_compliance_automation.evidence
WHERE report_name = '{{ report_name }}' --required
AND evidence_name = '{{ evidence_name }}' --required
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

Download evidence file.

```sql
EXEC azure_extras.app_compliance_automation.evidence.download 
@report_name='{{ report_name }}' --required, 
@evidence_name='{{ evidence_name }}' --required 
@@json=
'{
"reportCreatorTenantId": "{{ reportCreatorTenantId }}", 
"offerGuid": "{{ offerGuid }}"
}'
;
```
</TabItem>
</Tabs>
