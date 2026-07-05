--- 
title: test_run_files
hide_title: false
hide_table_of_contents: false
keywords:
  - test_run_files
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

Creates, updates, deletes, gets or lists a <code>test_run_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_run_files" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.test_run_files" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_test_run_file"
    values={[
        { label: 'get_test_run_file', value: 'get_test_run_file' }
    ]}
>
<TabItem value="get_test_run_file">

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
    <td><CopyableCode code="expireDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry time of the file (RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="fileName" /></td>
    <td><code>string</code></td>
    <td>Name of the file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fileType" /></td>
    <td><code>string</code></td>
    <td>File type. Known values are: "JMX_FILE", "USER_PROPERTIES", "ADDITIONAL_ARTIFACTS", "ZIPPED_ARTIFACTS", "URL_TEST_CONFIG", "TEST_SCRIPT", "BROWSER_RECORDING", and "TEST_PLAN_RECOMMENDATIONS". (JMX_FILE, USER_PROPERTIES, ADDITIONAL_ARTIFACTS, ZIPPED_ARTIFACTS, URL_TEST_CONFIG, TEST_SCRIPT, BROWSER_RECORDING, TEST_PLAN_RECOMMENDATIONS)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>File URL.</td>
</tr>
<tr>
    <td><CopyableCode code="validationFailureDetails" /></td>
    <td><code>string</code></td>
    <td>Validation failure error details.</td>
</tr>
<tr>
    <td><CopyableCode code="validationStatus" /></td>
    <td><code>string</code></td>
    <td>Validation status of the file. Known values are: "NOT_VALIDATED", "VALIDATION_SUCCESS", "VALIDATION_FAILURE", "VALIDATION_INITIATED", and "VALIDATION_NOT_REQUIRED". (NOT_VALIDATED, VALIDATION_SUCCESS, VALIDATION_FAILURE, VALIDATION_INITIATED, VALIDATION_NOT_REQUIRED)</td>
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
    <td><a href="#get_test_run_file"><CopyableCode code="get_test_run_file" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get test run file by file name. Get test run file by file name.</td>
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
<tr id="parameter-file_name">
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>Name of the file. Required.</td>
</tr>
<tr id="parameter-test_run_id">
    <td><CopyableCode code="test_run_id" /></td>
    <td><code>string</code></td>
    <td>Unique test run identifier for the load test run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_test_run_file"
    values={[
        { label: 'get_test_run_file', value: 'get_test_run_file' }
    ]}
>
<TabItem value="get_test_run_file">

Get test run file by file name. Get test run file by file name.

```sql
SELECT
expireDateTime,
fileName,
fileType,
url,
validationFailureDetails,
validationStatus
FROM azure.developer_loadtesting.test_run_files
WHERE test_run_id = '{{ test_run_id }}' -- required
AND file_name = '{{ file_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
