--- 
title: test_files
hide_title: false
hide_table_of_contents: false
keywords:
  - test_files
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

Creates, updates, deletes, gets or lists a <code>test_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_files" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.test_files" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_test_file"
    values={[
        { label: 'get_test_file', value: 'get_test_file' },
        { label: 'list_test_files', value: 'list_test_files' }
    ]}
>
<TabItem value="get_test_file">

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
<TabItem value="list_test_files">

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
    <td><a href="#get_test_file"><CopyableCode code="get_test_file" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get all the files that are associated with a test. Get all the files that are associated with a test.</td>
</tr>
<tr>
    <td><a href="#list_test_files"><CopyableCode code="list_test_files" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get all test files. Get all test files.</td>
</tr>
<tr>
    <td><a href="#delete_test_file"><CopyableCode code="delete_test_file" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete file by the file name for a test. Delete file by the file name for a test.</td>
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
<tr id="parameter-file_name">
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>Name of the file. Required.</td>
</tr>
<tr id="parameter-test_id">
    <td><CopyableCode code="test_id" /></td>
    <td><code>string</code></td>
    <td>Unique test identifier for the load test, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_test_file"
    values={[
        { label: 'get_test_file', value: 'get_test_file' },
        { label: 'list_test_files', value: 'list_test_files' }
    ]}
>
<TabItem value="get_test_file">

Get all the files that are associated with a test. Get all the files that are associated with a test.

```sql
SELECT
expireDateTime,
fileName,
fileType,
url,
validationFailureDetails,
validationStatus
FROM azure.developer_loadtesting.test_files
WHERE test_id = '{{ test_id }}' -- required
AND file_name = '{{ file_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_test_files">

Get all test files. Get all test files.

```sql
SELECT
expireDateTime,
fileName,
fileType,
url,
validationFailureDetails,
validationStatus
FROM azure.developer_loadtesting.test_files
WHERE test_id = '{{ test_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_test_file"
    values={[
        { label: 'delete_test_file', value: 'delete_test_file' }
    ]}
>
<TabItem value="delete_test_file">

Delete file by the file name for a test. Delete file by the file name for a test.

```sql
DELETE FROM azure.developer_loadtesting.test_files
WHERE test_id = '{{ test_id }}' --required
AND file_name = '{{ file_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
