--- 
title: analysis_results
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis_results
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

Creates, updates, deletes, gets or lists an <code>analysis_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analysis_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.analysis_results" /></td></tr>
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
    <td><CopyableCode code="analysisResultType" /></td>
    <td><code>string</code></td>
    <td>Type of the Analysis Result. Known values are: "ScriptExecution", "Reliability", "CPUUtilization", "MemoryUtilization", "CPURegression", "MemoryRegression", and "TestAnalysis".</td>
</tr>
<tr>
    <td><CopyableCode code="grade" /></td>
    <td><code>string</code></td>
    <td>The grade of the test. Known values are: "None", "NotAvailable", "Pass", and "Fail".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><CopyableCode code="analysisResultType" /></td>
    <td><code>string</code></td>
    <td>Type of the Analysis Result. Known values are: "ScriptExecution", "Reliability", "CPUUtilization", "MemoryUtilization", "CPURegression", "MemoryRegression", and "TestAnalysis".</td>
</tr>
<tr>
    <td><CopyableCode code="grade" /></td>
    <td><code>string</code></td>
    <td>The grade of the test. Known values are: "None", "NotAvailable", "Pass", and "Fail".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-test_result_name"><code>test_result_name</code></a>, <a href="#parameter-analysis_result_name"><code>analysis_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Analysis Result of a Test Result by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-test_result_name"><code>test_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-analysisResultType"><code>analysisResultType</code></a></td>
    <td></td>
    <td>Lists the Analysis Results of a Test Result. The result collection will only contain one element as all the data will be nested in a singleton object.</td>
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
<tr id="parameter-analysisResultType">
    <td><CopyableCode code="analysisResultType" /></td>
    <td><code>string</code></td>
    <td>The type of the Analysis Result of a Test Result. Known values are: "ScriptExecution", "Reliability", "CPUUtilization", "MemoryUtilization", "CPURegression", "MemoryRegression", and "TestAnalysis". Required.</td>
</tr>
<tr id="parameter-analysis_result_name">
    <td><CopyableCode code="analysis_result_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Analysis Result of a Test Result. Known values are: "scriptExecution", "reliability", "memoryUtilization", "cpuUtilization", "memoryRegression", "cpuRegression", and "testAnalysis". Required.</td>
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

Gets an Analysis Result of a Test Result by name.

```sql
SELECT
id,
name,
analysisResultType,
grade,
systemData,
type
FROM azure_extras.testbase.analysis_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND package_name = '{{ package_name }}' -- required
AND test_result_name = '{{ test_result_name }}' -- required
AND analysis_result_name = '{{ analysis_result_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the Analysis Results of a Test Result. The result collection will only contain one element as all the data will be nested in a singleton object.

```sql
SELECT
id,
name,
analysisResultType,
grade,
systemData,
type
FROM azure_extras.testbase.analysis_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND package_name = '{{ package_name }}' -- required
AND test_result_name = '{{ test_result_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND analysisResultType = '{{ analysisResultType }}' -- required
;
```
</TabItem>
</Tabs>
