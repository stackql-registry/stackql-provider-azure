--- 
title: test_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - test_runs
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

Creates, updates, deletes, gets or lists a <code>test_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.test_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_test_run"
    values={[
        { label: 'get_test_run', value: 'get_test_run' },
        { label: 'list_test_runs', value: 'list_test_runs' }
    ]}
>
<TabItem value="get_test_run">

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
    <td><CopyableCode code="autoStopCriteria" /></td>
    <td><code>object</code></td>
    <td>Auto stop criteria for a test. This will automatically stop a load test if the error percentage is high for a certain time window.</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>Certificates metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>The type of the entity that created the test run. (E.x. User, ScheduleTrigger, etc). Known values are: "User", "ScheduledTrigger", "AzurePipelines", and "GitHubWorkflows". (User, ScheduledTrigger, AzurePipelines, GitHubWorkflows)</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUri" /></td>
    <td><code>string</code></td>
    <td>The URI pointing to the entity that created the test run.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="debugLogsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enable or disable debug level logging. True if debug logs are enabled for the test run. False otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The test run description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of a testRun.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td>Test run duration in milliseconds.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run end DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>object</code></td>
    <td>Environment variables which are defined as a set of pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>Error details if there is any failure in load test run.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedVirtualUserHours" /></td>
    <td><code>number</code></td>
    <td>Estimated virtual user hours for the test run.</td>
</tr>
<tr>
    <td><CopyableCode code="executedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Test run initiated time. This is legacy, new developments should use createdDateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="executionEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run execution end DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="executionStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run execution start DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of test. Known values are: "URL", "JMX", and "Locust". (URL, JMX, Locust)</td>
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
    <td><CopyableCode code="loadTestConfiguration" /></td>
    <td><code>object</code></td>
    <td>The load test configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="passFailCriteria" /></td>
    <td><code>object</code></td>
    <td>Pass fail criteria for a test.</td>
</tr>
<tr>
    <td><CopyableCode code="portalUrl" /></td>
    <td><code>string</code></td>
    <td>Portal url.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Inject load test engines without deploying public IP for outbound access.</td>
</tr>
<tr>
    <td><CopyableCode code="regionalStatistics" /></td>
    <td><code>object</code></td>
    <td>Regional statistics. Key is the Azure region name and value is the test run statistics. The region name should of format accepted by ARM, and should be a region supported by Azure Load Testing. For example, East US should be passed as "eastus". The region name must match one of the strings in the "Name" column returned from running the "az account list-locations -o table" Azure CLI command.</td>
</tr>
<tr>
    <td><CopyableCode code="requestDataLevel" /></td>
    <td><code>string</code></td>
    <td>Request data collection level for test run. Known values are: "NONE" and "ERRORS". (NONE, ERRORS)</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>object</code></td>
    <td>Secrets can be stored in an Azure Key Vault or any other secret store. If the secret is stored in an Azure Key Vault, the value should be the secret identifier and the type should be AKV_SECRET_URI. If the secret is stored elsewhere, the secret value should be provided directly and the type should be SECRET_VALUE.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run start DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The test run status. Known values are: "ACCEPTED", "NOTSTARTED", "PROVISIONING", "PROVISIONED", "CONFIGURING", "CONFIGURED", "EXECUTING", "EXECUTED", "DEPROVISIONING", "DEPROVISIONED", "DONE", "CANCELLING", "CANCELLED", "FAILED", "VALIDATION_SUCCESS", and "VALIDATION_FAILURE". (ACCEPTED, NOTSTARTED, PROVISIONING, PROVISIONED, CONFIGURING, CONFIGURED, EXECUTING, EXECUTED, DEPROVISIONING, DEPROVISIONED, DONE, CANCELLING, CANCELLED, FAILED, VALIDATION_SUCCESS, VALIDATION_FAILURE)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet ID on which the load test instances should run.</td>
</tr>
<tr>
    <td><CopyableCode code="testArtifacts" /></td>
    <td><code>object</code></td>
    <td>Collection of test run artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Associated test Id.</td>
</tr>
<tr>
    <td><CopyableCode code="testResult" /></td>
    <td><code>string</code></td>
    <td>Test result for pass/Fail criteria used during the test run. Known values are: "PASSED", "NOT_APPLICABLE", and "FAILED". (PASSED, NOT_APPLICABLE, FAILED)</td>
</tr>
<tr>
    <td><CopyableCode code="testRunId" /></td>
    <td><code>string</code></td>
    <td>Unique test run identifier for the load test run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunStatistics" /></td>
    <td><code>object</code></td>
    <td>Test run statistics. Key is the sampler name and value is the set of statistics for performance metrics like response time, throughput, etc. from the load test run. The sampler name is the same as the name mentioned in the test script. Sampler name "Total" represents the aggregated statistics of all the samplers.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualUserHours" /></td>
    <td><code>number</code></td>
    <td>Virtual user hours consumed by the test run.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualUsers" /></td>
    <td><code>integer</code></td>
    <td>Number of virtual users, for which test has been run.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_test_runs">

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
    <td><CopyableCode code="autoStopCriteria" /></td>
    <td><code>object</code></td>
    <td>Auto stop criteria for a test. This will automatically stop a load test if the error percentage is high for a certain time window.</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>Certificates metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>The type of the entity that created the test run. (E.x. User, ScheduleTrigger, etc). Known values are: "User", "ScheduledTrigger", "AzurePipelines", and "GitHubWorkflows". (User, ScheduledTrigger, AzurePipelines, GitHubWorkflows)</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUri" /></td>
    <td><code>string</code></td>
    <td>The URI pointing to the entity that created the test run.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="debugLogsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enable or disable debug level logging. True if debug logs are enabled for the test run. False otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The test run description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of a testRun.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td>Test run duration in milliseconds.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run end DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>object</code></td>
    <td>Environment variables which are defined as a set of pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>Error details if there is any failure in load test run.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedVirtualUserHours" /></td>
    <td><code>number</code></td>
    <td>Estimated virtual user hours for the test run.</td>
</tr>
<tr>
    <td><CopyableCode code="executedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Test run initiated time. This is legacy, new developments should use createdDateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="executionEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run execution end DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="executionStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run execution start DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of test. Known values are: "URL", "JMX", and "Locust". (URL, JMX, Locust)</td>
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
    <td><CopyableCode code="loadTestConfiguration" /></td>
    <td><code>object</code></td>
    <td>The load test configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="passFailCriteria" /></td>
    <td><code>object</code></td>
    <td>Pass fail criteria for a test.</td>
</tr>
<tr>
    <td><CopyableCode code="portalUrl" /></td>
    <td><code>string</code></td>
    <td>Portal url.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Inject load test engines without deploying public IP for outbound access.</td>
</tr>
<tr>
    <td><CopyableCode code="regionalStatistics" /></td>
    <td><code>object</code></td>
    <td>Regional statistics. Key is the Azure region name and value is the test run statistics. The region name should of format accepted by ARM, and should be a region supported by Azure Load Testing. For example, East US should be passed as "eastus". The region name must match one of the strings in the "Name" column returned from running the "az account list-locations -o table" Azure CLI command.</td>
</tr>
<tr>
    <td><CopyableCode code="requestDataLevel" /></td>
    <td><code>string</code></td>
    <td>Request data collection level for test run. Known values are: "NONE" and "ERRORS". (NONE, ERRORS)</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>object</code></td>
    <td>Secrets can be stored in an Azure Key Vault or any other secret store. If the secret is stored in an Azure Key Vault, the value should be the secret identifier and the type should be AKV_SECRET_URI. If the secret is stored elsewhere, the secret value should be provided directly and the type should be SECRET_VALUE.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The test run start DateTime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The test run status. Known values are: "ACCEPTED", "NOTSTARTED", "PROVISIONING", "PROVISIONED", "CONFIGURING", "CONFIGURED", "EXECUTING", "EXECUTED", "DEPROVISIONING", "DEPROVISIONED", "DONE", "CANCELLING", "CANCELLED", "FAILED", "VALIDATION_SUCCESS", and "VALIDATION_FAILURE". (ACCEPTED, NOTSTARTED, PROVISIONING, PROVISIONED, CONFIGURING, CONFIGURED, EXECUTING, EXECUTED, DEPROVISIONING, DEPROVISIONED, DONE, CANCELLING, CANCELLED, FAILED, VALIDATION_SUCCESS, VALIDATION_FAILURE)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet ID on which the load test instances should run.</td>
</tr>
<tr>
    <td><CopyableCode code="testArtifacts" /></td>
    <td><code>object</code></td>
    <td>Collection of test run artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Associated test Id.</td>
</tr>
<tr>
    <td><CopyableCode code="testResult" /></td>
    <td><code>string</code></td>
    <td>Test result for pass/Fail criteria used during the test run. Known values are: "PASSED", "NOT_APPLICABLE", and "FAILED". (PASSED, NOT_APPLICABLE, FAILED)</td>
</tr>
<tr>
    <td><CopyableCode code="testRunId" /></td>
    <td><code>string</code></td>
    <td>Unique test run identifier for the load test run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunStatistics" /></td>
    <td><code>object</code></td>
    <td>Test run statistics. Key is the sampler name and value is the set of statistics for performance metrics like response time, throughput, etc. from the load test run. The sampler name is the same as the name mentioned in the test script. Sampler name "Total" represents the aggregated statistics of all the samplers.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualUserHours" /></td>
    <td><code>number</code></td>
    <td>Virtual user hours consumed by the test run.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualUsers" /></td>
    <td><code>integer</code></td>
    <td>Number of virtual users, for which test has been run.</td>
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
    <td><a href="#get_test_run"><CopyableCode code="get_test_run" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get test run details by test run Id. Get test run details by test run Id.</td>
</tr>
<tr>
    <td><a href="#list_test_runs"><CopyableCode code="list_test_runs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-testId"><code>testId</code></a>, <a href="#parameter-executionFrom"><code>executionFrom</code></a>, <a href="#parameter-executionTo"><code>executionTo</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-createdByTypes"><code>createdByTypes</code></a>, <a href="#parameter-testIds"><code>testIds</code></a></td>
    <td>Get all test runs for the given filters. Get all test runs for the given filters.</td>
</tr>
<tr>
    <td><a href="#delete_test_run"><CopyableCode code="delete_test_run" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an existing load test run. Delete an existing load test run by providing the testRunId.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-test_run_id">
    <td><CopyableCode code="test_run_id" /></td>
    <td><code>string</code></td>
    <td>Unique test run identifier for the load test run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr id="parameter-createdByTypes">
    <td><CopyableCode code="createdByTypes" /></td>
    <td><code>array</code></td>
    <td>Comma separated list of type of entities that have created the test run. Default value is None.</td>
</tr>
<tr id="parameter-executionFrom">
    <td><CopyableCode code="executionFrom" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime(RFC 3339 literal format) of test-run execution time filter range. Default value is None.</td>
</tr>
<tr id="parameter-executionTo">
    <td><CopyableCode code="executionTo" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime(RFC 3339 literal format) of test-run execution time filter range. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>string</code></td>
    <td>Sort on the supported fields in (field asc/desc) format. eg: createdDateTime asc. Supported fields - createdDateTime, executedDateTime (legacy). Default value is None.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Prefix based, case sensitive search on searchable fields - description, executedUser. For example, to search for a test run, with description 500 VUs, the search parameter can be 500. Default value is None.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of test run status. Default value is None.</td>
</tr>
<tr id="parameter-testId">
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Unique name of an existing load test. Default value is None.</td>
</tr>
<tr id="parameter-testIds">
    <td><CopyableCode code="testIds" /></td>
    <td><code>array</code></td>
    <td>Comma-separated list of test IDs. If you are using testIds, do not send a value for testId. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_test_run"
    values={[
        { label: 'get_test_run', value: 'get_test_run' },
        { label: 'list_test_runs', value: 'list_test_runs' }
    ]}
>
<TabItem value="get_test_run">

Get test run details by test run Id. Get test run details by test run Id.

```sql
SELECT
autoStopCriteria,
certificate,
createdBy,
createdByType,
createdByUri,
createdDateTime,
debugLogsEnabled,
description,
displayName,
duration,
endDateTime,
environmentVariables,
errorDetails,
estimatedVirtualUserHours,
executedDateTime,
executionEndDateTime,
executionStartDateTime,
kind,
lastModifiedBy,
lastModifiedDateTime,
loadTestConfiguration,
passFailCriteria,
portalUrl,
publicIPDisabled,
regionalStatistics,
requestDataLevel,
secrets,
startDateTime,
status,
subnetId,
testArtifacts,
testId,
testResult,
testRunId,
testRunStatistics,
virtualUserHours,
virtualUsers
FROM azure.developer_loadtesting.test_runs
WHERE test_run_id = '{{ test_run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_test_runs">

Get all test runs for the given filters. Get all test runs for the given filters.

```sql
SELECT
autoStopCriteria,
certificate,
createdBy,
createdByType,
createdByUri,
createdDateTime,
debugLogsEnabled,
description,
displayName,
duration,
endDateTime,
environmentVariables,
errorDetails,
estimatedVirtualUserHours,
executedDateTime,
executionEndDateTime,
executionStartDateTime,
kind,
lastModifiedBy,
lastModifiedDateTime,
loadTestConfiguration,
passFailCriteria,
portalUrl,
publicIPDisabled,
regionalStatistics,
requestDataLevel,
secrets,
startDateTime,
status,
subnetId,
testArtifacts,
testId,
testResult,
testRunId,
testRunStatistics,
virtualUserHours,
virtualUsers
FROM azure.developer_loadtesting.test_runs
WHERE endpoint = '{{ endpoint }}' -- required
AND orderby = '{{ orderby }}'
AND search = '{{ search }}'
AND testId = '{{ testId }}'
AND executionFrom = '{{ executionFrom }}'
AND executionTo = '{{ executionTo }}'
AND status = '{{ status }}'
AND maxpagesize = '{{ maxpagesize }}'
AND createdByTypes = '{{ createdByTypes }}'
AND testIds = '{{ testIds }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_test_run"
    values={[
        { label: 'delete_test_run', value: 'delete_test_run' }
    ]}
>
<TabItem value="delete_test_run">

Delete an existing load test run. Delete an existing load test run by providing the testRunId.

```sql
DELETE FROM azure.developer_loadtesting.test_runs
WHERE test_run_id = '{{ test_run_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
