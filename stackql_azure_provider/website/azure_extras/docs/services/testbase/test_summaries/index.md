--- 
title: test_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - test_summaries
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

Creates, updates, deletes, gets or lists a <code>test_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_summaries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.test_summaries" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
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
    <td><CopyableCode code="executionStatus" /></td>
    <td><code>string</code></td>
    <td>The execution status of last test. Known values are: "None", "InProgress", "Processing", "Completed", "NotExecuted", "Incomplete", "Failed", and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="featureUpdatesTestSummary" /></td>
    <td><code>object</code></td>
    <td>The result summary of tests triggered by feature updates.</td>
</tr>
<tr>
    <td><CopyableCode code="grade" /></td>
    <td><code>string</code></td>
    <td>The grade of the test. Known values are: "None", "NotAvailable", "Pass", and "Fail".</td>
</tr>
<tr>
    <td><CopyableCode code="packageId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource Id of package.</td>
</tr>
<tr>
    <td><CopyableCode code="packageTags" /></td>
    <td><code>object</code></td>
    <td>The tags of Package resource that are associated with the testSummary.</td>
</tr>
<tr>
    <td><CopyableCode code="securityUpdatesTestSummary" /></td>
    <td><code>object</code></td>
    <td>The result summary of tests triggered by security updates.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunTime" /></td>
    <td><code>string</code></td>
    <td>The run time of the last test.</td>
</tr>
<tr>
    <td><CopyableCode code="testStatus" /></td>
    <td><code>string</code></td>
    <td>The status of last test. Known values are: "None", "TestExecutionInProgress", "DataProcessing", "TestFailure", "UpdateFailure", "TestAndUpdateFailure", "InfrastructureFailure", and "Completed".</td>
</tr>
<tr>
    <td><CopyableCode code="testSummaryId" /></td>
    <td><code>string</code></td>
    <td>The Id of the current Test Summary.</td>
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
    <td><CopyableCode code="executionStatus" /></td>
    <td><code>string</code></td>
    <td>The execution status of last test. Known values are: "None", "InProgress", "Processing", "Completed", "NotExecuted", "Incomplete", "Failed", and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="featureUpdatesTestSummary" /></td>
    <td><code>object</code></td>
    <td>The result summary of tests triggered by feature updates.</td>
</tr>
<tr>
    <td><CopyableCode code="grade" /></td>
    <td><code>string</code></td>
    <td>The grade of the test. Known values are: "None", "NotAvailable", "Pass", and "Fail".</td>
</tr>
<tr>
    <td><CopyableCode code="packageId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource Id of package.</td>
</tr>
<tr>
    <td><CopyableCode code="packageTags" /></td>
    <td><code>object</code></td>
    <td>The tags of Package resource that are associated with the testSummary.</td>
</tr>
<tr>
    <td><CopyableCode code="securityUpdatesTestSummary" /></td>
    <td><code>object</code></td>
    <td>The result summary of tests triggered by security updates.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="testRunTime" /></td>
    <td><code>string</code></td>
    <td>The run time of the last test.</td>
</tr>
<tr>
    <td><CopyableCode code="testStatus" /></td>
    <td><code>string</code></td>
    <td>The status of last test. Known values are: "None", "TestExecutionInProgress", "DataProcessing", "TestFailure", "UpdateFailure", "TestAndUpdateFailure", "InfrastructureFailure", and "Completed".</td>
</tr>
<tr>
    <td><CopyableCode code="testSummaryId" /></td>
    <td><code>string</code></td>
    <td>The Id of the current Test Summary.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-test_summary_name"><code>test_summary_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Test Summary with specific name from all the Test Summaries of all the packages under a Test Base Account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Test Summaries of all the packages under a Test Base Account.</td>
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
<tr id="parameter-test_summary_name">
    <td><CopyableCode code="test_summary_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Test Summary. Required.</td>
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

Gets a Test Summary with specific name from all the Test Summaries of all the packages under a Test Base Account.

```sql
SELECT
id,
name,
applicationName,
applicationVersion,
executionStatus,
featureUpdatesTestSummary,
grade,
packageId,
packageTags,
securityUpdatesTestSummary,
systemData,
testRunTime,
testStatus,
testSummaryId,
type
FROM azure_extras.testbase.test_summaries
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND test_summary_name = '{{ test_summary_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the Test Summaries of all the packages under a Test Base Account.

```sql
SELECT
id,
name,
applicationName,
applicationVersion,
executionStatus,
featureUpdatesTestSummary,
grade,
packageId,
packageTags,
securityUpdatesTestSummary,
systemData,
testRunTime,
testStatus,
testSummaryId,
type
FROM azure_extras.testbase.test_summaries
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
