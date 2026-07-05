--- 
title: test_profile_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - test_profile_runs
  - developer_loadtesting
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

Creates, updates, deletes, gets or lists a <code>test_profile_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_profile_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.test_profile_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_test_profile_run"
    values={[
        { label: 'get_test_profile_run', value: 'get_test_profile_run' },
        { label: 'list_test_profile_runs', value: 'list_test_profile_runs' }
    ]}
>
<TabItem value="get_test_profile_run">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The test profile run description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the test profile run.</td>
</tr>
<tr>
    <td><CopyableCode code="durationInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Test profile run duration in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test profile run end DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>Error details if there is any failure in test profile run. These errors are specific to the Test Profile Run.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="recommendations" /></td>
    <td><code>array</code></td>
    <td>Recommendations provided based on a successful test profile run.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test profile run start DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The test profile run status. Known values are: "ACCEPTED", "NOTSTARTED", "EXECUTING", "DONE", "CANCELLING", "CANCELLED", and "FAILED". (ACCEPTED, NOTSTARTED, EXECUTING, DONE, CANCELLING, CANCELLED, FAILED)</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceConfigurations" /></td>
    <td><code>object</code></td>
    <td>Configurations of the target resource on which the test profile ran.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Target resource ID on which the test profile run is created.</td>
</tr>
<tr>
    <td><CopyableCode code="testProfileId" /></td>
    <td><code>string</code></td>
    <td>Associated test profile ID for the test profile run. This is required to create a test profile run and can't be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="testProfileRunId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the test profile run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the test runs ran as part of the test profile run. Key is the testRunId of the corresponding testRun.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_test_profile_runs">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The test profile run description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the test profile run.</td>
</tr>
<tr>
    <td><CopyableCode code="durationInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Test profile run duration in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test profile run end DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>Error details if there is any failure in test profile run. These errors are specific to the Test Profile Run.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="recommendations" /></td>
    <td><code>array</code></td>
    <td>Recommendations provided based on a successful test profile run.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test profile run start DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The test profile run status. Known values are: "ACCEPTED", "NOTSTARTED", "EXECUTING", "DONE", "CANCELLING", "CANCELLED", and "FAILED". (ACCEPTED, NOTSTARTED, EXECUTING, DONE, CANCELLING, CANCELLED, FAILED)</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceConfigurations" /></td>
    <td><code>object</code></td>
    <td>Configurations of the target resource on which the test profile ran.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Target resource ID on which the test profile run is created.</td>
</tr>
<tr>
    <td><CopyableCode code="testProfileId" /></td>
    <td><code>string</code></td>
    <td>Associated test profile ID for the test profile run. This is required to create a test profile run and can't be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="testProfileRunId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the test profile run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the test runs ran as part of the test profile run. Key is the testRunId of the corresponding testRun.</td>
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
    <td><a href="#get_test_profile_run"><CopyableCode code="get_test_profile_run" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_profile_run_id"><code>test_profile_run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get test profile run details. Get test profile run details by test profile run Id.</td>
</tr>
<tr>
    <td><a href="#list_test_profile_runs"><CopyableCode code="list_test_profile_runs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-minStartDateTime"><code>minStartDateTime</code></a>, <a href="#parameter-maxStartDateTime"><code>maxStartDateTime</code></a>, <a href="#parameter-minEndDateTime"><code>minEndDateTime</code></a>, <a href="#parameter-maxEndDateTime"><code>maxEndDateTime</code></a>, <a href="#parameter-createdDateStartTime"><code>createdDateStartTime</code></a>, <a href="#parameter-createdDateEndTime"><code>createdDateEndTime</code></a>, <a href="#parameter-testProfileRunIds"><code>testProfileRunIds</code></a>, <a href="#parameter-testProfileIds"><code>testProfileIds</code></a>, <a href="#parameter-statuses"><code>statuses</code></a></td>
    <td>List test profile runs. Get all test profile runs for the given filters.</td>
</tr>
<tr>
    <td><a href="#delete_test_profile_run"><CopyableCode code="delete_test_profile_run" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-test_profile_run_id"><code>test_profile_run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an existing load test profile run. Delete an existing load test profile run by providing the test profile run Id.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-test_profile_run_id">
    <td><CopyableCode code="test_profile_run_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the test profile run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr id="parameter-createdDateEndTime">
    <td><CopyableCode code="createdDateEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime(RFC 3339 literal format) of the created time range to filter test profile runs. Default value is None.</td>
</tr>
<tr id="parameter-createdDateStartTime">
    <td><CopyableCode code="createdDateStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime(RFC 3339 literal format) of the created time range to filter test profile runs. Default value is None.</td>
</tr>
<tr id="parameter-maxEndDateTime">
    <td><CopyableCode code="maxEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum End DateTime(RFC 3339 literal format) of the test profile runs to filter on. Default value is None.</td>
</tr>
<tr id="parameter-maxStartDateTime">
    <td><CopyableCode code="maxStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum Start DateTime(RFC 3339 literal format) of the test profile runs to filter on. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-minEndDateTime">
    <td><CopyableCode code="minEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum End DateTime(RFC 3339 literal format) of the test profile runs to filter on. Default value is None.</td>
</tr>
<tr id="parameter-minStartDateTime">
    <td><CopyableCode code="minStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum Start DateTime(RFC 3339 literal format) of the test profile runs to filter on. Default value is None.</td>
</tr>
<tr id="parameter-statuses">
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>Comma separated list of Statuses of the test profile runs to filter. Default value is None.</td>
</tr>
<tr id="parameter-testProfileIds">
    <td><CopyableCode code="testProfileIds" /></td>
    <td><code>array</code></td>
    <td>Comma separated IDs of the test profiles which should be associated with the test profile runs to fetch. Default value is None.</td>
</tr>
<tr id="parameter-testProfileRunIds">
    <td><CopyableCode code="testProfileRunIds" /></td>
    <td><code>array</code></td>
    <td>Comma separated list of IDs of the test profile runs to filter. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_test_profile_run"
    values={[
        { label: 'get_test_profile_run', value: 'get_test_profile_run' },
        { label: 'list_test_profile_runs', value: 'list_test_profile_runs' }
    ]}
>
<TabItem value="get_test_profile_run">

Get test profile run details. Get test profile run details by test profile run Id.

```sql
SELECT
createdBy,
createdDateTime,
description,
displayName,
durationInSeconds,
endDateTime,
errorDetails,
lastModifiedBy,
lastModifiedDateTime,
recommendations,
startDateTime,
status,
targetResourceConfigurations,
targetResourceId,
testProfileId,
testProfileRunId,
testRunDetails
FROM azure.developer_loadtesting.test_profile_runs
WHERE test_profile_run_id = '{{ test_profile_run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_test_profile_runs">

List test profile runs. Get all test profile runs for the given filters.

```sql
SELECT
createdBy,
createdDateTime,
description,
displayName,
durationInSeconds,
endDateTime,
errorDetails,
lastModifiedBy,
lastModifiedDateTime,
recommendations,
startDateTime,
status,
targetResourceConfigurations,
targetResourceId,
testProfileId,
testProfileRunId,
testRunDetails
FROM azure.developer_loadtesting.test_profile_runs
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
AND minStartDateTime = '{{ minStartDateTime }}'
AND maxStartDateTime = '{{ maxStartDateTime }}'
AND minEndDateTime = '{{ minEndDateTime }}'
AND maxEndDateTime = '{{ maxEndDateTime }}'
AND createdDateStartTime = '{{ createdDateStartTime }}'
AND createdDateEndTime = '{{ createdDateEndTime }}'
AND testProfileRunIds = '{{ testProfileRunIds }}'
AND testProfileIds = '{{ testProfileIds }}'
AND statuses = '{{ statuses }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_test_profile_run"
    values={[
        { label: 'delete_test_profile_run', value: 'delete_test_profile_run' }
    ]}
>
<TabItem value="delete_test_profile_run">

Delete an existing load test profile run. Delete an existing load test profile run by providing the test profile run Id.

```sql
DELETE FROM azure.developer_loadtesting.test_profile_runs
WHERE test_profile_run_id = '{{ test_profile_run_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
