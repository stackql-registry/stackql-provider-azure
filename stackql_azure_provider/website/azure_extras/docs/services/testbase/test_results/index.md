--- 
title: test_results
hide_title: false
hide_table_of_contents: false
keywords:
  - test_results
  - testbase
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

Creates, updates, deletes, gets or lists a <code>test_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.test_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_console_log_download_url"
    values={[
        { label: 'get_console_log_download_url', value: 'get_console_log_download_url' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_console_log_download_url">

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
    <td><CopyableCode code="downloadUrl" /></td>
    <td><code>string</code></td>
    <td>The download URL.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date of the download URL.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="analysisSummaries" /></td>
    <td><code>array</code></td>
    <td>List of analysis summaries.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationName" /></td>
    <td><code>string</code></td>
    <td>Application name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationVersion" /></td>
    <td><code>string</code></td>
    <td>Application version.</td>
</tr>
<tr>
    <td><CopyableCode code="baselineTestResultId" /></td>
    <td><code>string</code></td>
    <td>Azure Id of the baseline test result.</td>
</tr>
<tr>
    <td><CopyableCode code="buildRevision" /></td>
    <td><code>string</code></td>
    <td>The build revision of the tested release (OS update).</td>
</tr>
<tr>
    <td><CopyableCode code="buildVersion" /></td>
    <td><code>string</code></td>
    <td>The build version of the tested release (OS update).</td>
</tr>
<tr>
    <td><CopyableCode code="executionStatus" /></td>
    <td><code>string</code></td>
    <td>The execution status of the test. Known values are: "None", "InProgress", "Processing", "Completed", "NotExecuted", "Incomplete", "Failed", and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="flightingRing" /></td>
    <td><code>string</code></td>
    <td>The flighting ring, only for release of feature updates.</td>
</tr>
<tr>
    <td><CopyableCode code="grade" /></td>
    <td><code>string</code></td>
    <td>The grade of the test. Known values are: "None", "NotAvailable", "Pass", and "Fail".</td>
</tr>
<tr>
    <td><CopyableCode code="interopMediaType" /></td>
    <td><code>string</code></td>
    <td>Interop media type.</td>
</tr>
<tr>
    <td><CopyableCode code="interopMediaVersion" /></td>
    <td><code>string</code></td>
    <td>Interop media version.</td>
</tr>
<tr>
    <td><CopyableCode code="isDownloadDataAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Whether download data is available.</td>
</tr>
<tr>
    <td><CopyableCode code="isVideoAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Whether video data is available.</td>
</tr>
<tr>
    <td><CopyableCode code="kbNumber" /></td>
    <td><code>string</code></td>
    <td>KB number.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>The operating system name, e.g. Windows 10 1809.</td>
</tr>
<tr>
    <td><CopyableCode code="packageId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="packageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Windows update package.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the tested release (OS update).</td>
</tr>
<tr>
    <td><CopyableCode code="releaseVersionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The release version date of the tested release.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunTime" /></td>
    <td><code>string</code></td>
    <td>The run time of the test.</td>
</tr>
<tr>
    <td><CopyableCode code="testStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the test. Known values are: "None", "TestExecutionInProgress", "DataProcessing", "TestFailure", "UpdateFailure", "TestAndUpdateFailure", "InfrastructureFailure", and "Completed".</td>
</tr>
<tr>
    <td><CopyableCode code="testType" /></td>
    <td><code>string</code></td>
    <td>Test type. E.g. 'Out of box test' or 'Functional test'.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><CopyableCode code="analysisSummaries" /></td>
    <td><code>array</code></td>
    <td>List of analysis summaries.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationName" /></td>
    <td><code>string</code></td>
    <td>Application name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationVersion" /></td>
    <td><code>string</code></td>
    <td>Application version.</td>
</tr>
<tr>
    <td><CopyableCode code="baselineTestResultId" /></td>
    <td><code>string</code></td>
    <td>Azure Id of the baseline test result.</td>
</tr>
<tr>
    <td><CopyableCode code="buildRevision" /></td>
    <td><code>string</code></td>
    <td>The build revision of the tested release (OS update).</td>
</tr>
<tr>
    <td><CopyableCode code="buildVersion" /></td>
    <td><code>string</code></td>
    <td>The build version of the tested release (OS update).</td>
</tr>
<tr>
    <td><CopyableCode code="executionStatus" /></td>
    <td><code>string</code></td>
    <td>The execution status of the test. Known values are: "None", "InProgress", "Processing", "Completed", "NotExecuted", "Incomplete", "Failed", and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="flightingRing" /></td>
    <td><code>string</code></td>
    <td>The flighting ring, only for release of feature updates.</td>
</tr>
<tr>
    <td><CopyableCode code="grade" /></td>
    <td><code>string</code></td>
    <td>The grade of the test. Known values are: "None", "NotAvailable", "Pass", and "Fail".</td>
</tr>
<tr>
    <td><CopyableCode code="interopMediaType" /></td>
    <td><code>string</code></td>
    <td>Interop media type.</td>
</tr>
<tr>
    <td><CopyableCode code="interopMediaVersion" /></td>
    <td><code>string</code></td>
    <td>Interop media version.</td>
</tr>
<tr>
    <td><CopyableCode code="isDownloadDataAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Whether download data is available.</td>
</tr>
<tr>
    <td><CopyableCode code="isVideoAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Whether video data is available.</td>
</tr>
<tr>
    <td><CopyableCode code="kbNumber" /></td>
    <td><code>string</code></td>
    <td>KB number.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>The operating system name, e.g. Windows 10 1809.</td>
</tr>
<tr>
    <td><CopyableCode code="packageId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="packageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Windows update package.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the tested release (OS update).</td>
</tr>
<tr>
    <td><CopyableCode code="releaseVersionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The release version date of the tested release.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunTime" /></td>
    <td><code>string</code></td>
    <td>The run time of the test.</td>
</tr>
<tr>
    <td><CopyableCode code="testStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the test. Known values are: "None", "TestExecutionInProgress", "DataProcessing", "TestFailure", "UpdateFailure", "TestAndUpdateFailure", "InfrastructureFailure", and "Completed".</td>
</tr>
<tr>
    <td><CopyableCode code="testType" /></td>
    <td><code>string</code></td>
    <td>Test type. E.g. 'Out of box test' or 'Functional test'.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#get_console_log_download_url"><CopyableCode code="get_console_log_download_url" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-test_result_name"><code>test_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the download URL of the test execution console log file.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-test_result_name"><code>test_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Test Result by Id with specified OS Update type for a Test Base Package.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-osUpdateType"><code>osUpdateType</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all the Test Results with specified OS Update type for a Test Base Package. Can be filtered by osName, releaseName, flightingRing, buildVersion, buildRevision.</td>
</tr>
<tr>
    <td><a href="#get_download_url"><CopyableCode code="get_download_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-test_result_name"><code>test_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the download URL of the test result.</td>
</tr>
<tr>
    <td><a href="#get_video_download_url"><CopyableCode code="get_video_download_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-test_result_name"><code>test_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the download URL of the test execution screen recording.</td>
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
<tr id="parameter-osUpdateType">
    <td><CopyableCode code="osUpdateType" /></td>
    <td><code>string</code></td>
    <td>The type of the OS Update. Known values are: "SecurityUpdate" and "FeatureUpdate". Required.</td>
</tr>
<tr id="parameter-package_name">
    <td><CopyableCode code="package_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the Test Base Package. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-test_base_account_name">
    <td><CopyableCode code="test_base_account_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the Test Base Account. Required.</td>
</tr>
<tr id="parameter-test_result_name">
    <td><CopyableCode code="test_result_name" /></td>
    <td><code>string</code></td>
    <td>The Test Result Name. It equals to TestResult-&#123;TestResultId&#125; string. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Odata filter. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_console_log_download_url"
    values={[
        { label: 'get_console_log_download_url', value: 'get_console_log_download_url' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_console_log_download_url">

Gets the download URL of the test execution console log file.

```sql
SELECT
downloadUrl,
expirationTime
FROM azure_extras.testbase.test_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND package_name = '{{ package_name }}' -- required
AND test_result_name = '{{ test_result_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the Test Result by Id with specified OS Update type for a Test Base Package.

```sql
SELECT
id,
name,
analysisSummaries,
applicationName,
applicationVersion,
baselineTestResultId,
buildRevision,
buildVersion,
executionStatus,
flightingRing,
grade,
interopMediaType,
interopMediaVersion,
isDownloadDataAvailable,
isVideoAvailable,
kbNumber,
osName,
packageId,
packageVersion,
releaseName,
releaseVersionDate,
systemData,
testRunTime,
testStatus,
testType,
type
FROM azure_extras.testbase.test_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND package_name = '{{ package_name }}' -- required
AND test_result_name = '{{ test_result_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the Test Results with specified OS Update type for a Test Base Package. Can be filtered by osName, releaseName, flightingRing, buildVersion, buildRevision.

```sql
SELECT
id,
name,
analysisSummaries,
applicationName,
applicationVersion,
baselineTestResultId,
buildRevision,
buildVersion,
executionStatus,
flightingRing,
grade,
interopMediaType,
interopMediaVersion,
isDownloadDataAvailable,
isVideoAvailable,
kbNumber,
osName,
packageId,
packageVersion,
releaseName,
releaseVersionDate,
systemData,
testRunTime,
testStatus,
testType,
type
FROM azure_extras.testbase.test_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND package_name = '{{ package_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND osUpdateType = '{{ osUpdateType }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_download_url"
    values={[
        { label: 'get_download_url', value: 'get_download_url' },
        { label: 'get_video_download_url', value: 'get_video_download_url' }
    ]}
>
<TabItem value="get_download_url">

Gets the download URL of the test result.

```sql
EXEC azure_extras.testbase.test_results.get_download_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@package_name='{{ package_name }}' --required, 
@test_result_name='{{ test_result_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_video_download_url">

Gets the download URL of the test execution screen recording.

```sql
EXEC azure_extras.testbase.test_results.get_video_download_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@package_name='{{ package_name }}' --required, 
@test_result_name='{{ test_result_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
