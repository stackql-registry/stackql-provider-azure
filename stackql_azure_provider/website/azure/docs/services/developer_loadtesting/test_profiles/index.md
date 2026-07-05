--- 
title: test_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - test_profiles
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

Creates, updates, deletes, gets or lists a <code>test_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.test_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_test_profile"
    values={[
        { label: 'get_test_profile', value: 'get_test_profile' },
        { label: 'list_test_profiles', value: 'list_test_profiles' }
    ]}
>
<TabItem value="get_test_profile">

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
    <td>Description for the test profile.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the test profile.</td>
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
    <td><CopyableCode code="targetResourceConfigurations" /></td>
    <td><code>object</code></td>
    <td>Configurations of the target resource on which testing would be done.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Target resource ID on which the test profile is created. This property is required for creating a Test Profile and it's not allowed to be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Associated test ID for the test profile. This property is required for creating a Test Profile and it's not allowed to be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="testProfileId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the test profile, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_test_profiles">

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
    <td>Description for the test profile.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the test profile.</td>
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
    <td><CopyableCode code="targetResourceConfigurations" /></td>
    <td><code>object</code></td>
    <td>Configurations of the target resource on which testing would be done.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Target resource ID on which the test profile is created. This property is required for creating a Test Profile and it's not allowed to be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Associated test ID for the test profile. This property is required for creating a Test Profile and it's not allowed to be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="testProfileId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the test profile, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
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
    <td><a href="#get_test_profile"><CopyableCode code="get_test_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_profile_id"><code>test_profile_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get load test profile details. Get load test profile details by test profile Id.</td>
</tr>
<tr>
    <td><a href="#list_test_profiles"><CopyableCode code="list_test_profiles" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-lastModifiedStartTime"><code>lastModifiedStartTime</code></a>, <a href="#parameter-lastModifiedEndTime"><code>lastModifiedEndTime</code></a>, <a href="#parameter-testProfileIds"><code>testProfileIds</code></a>, <a href="#parameter-testIds"><code>testIds</code></a></td>
    <td>List test profiles. Get all test profiles for the given filters.</td>
</tr>
<tr>
    <td><a href="#create_or_update_test_profile"><CopyableCode code="create_or_update_test_profile" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-test_profile_id"><code>test_profile_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new test profile or update an existing test profile. Create a new test profile or update an existing test profile by providing the test profile Id.</td>
</tr>
<tr>
    <td><a href="#create_or_update_test_profile"><CopyableCode code="create_or_update_test_profile" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-test_profile_id"><code>test_profile_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new test profile or update an existing test profile. Create a new test profile or update an existing test profile by providing the test profile Id.</td>
</tr>
<tr>
    <td><a href="#delete_test_profile"><CopyableCode code="delete_test_profile" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-test_profile_id"><code>test_profile_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a test profile. Delete a test profile by its test profile Id.</td>
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
<tr id="parameter-test_profile_id">
    <td><CopyableCode code="test_profile_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the test profile, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr id="parameter-lastModifiedEndTime">
    <td><CopyableCode code="lastModifiedEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime(RFC 3339 literal format) of the last updated time range to filter test profiles. Default value is None.</td>
</tr>
<tr id="parameter-lastModifiedStartTime">
    <td><CopyableCode code="lastModifiedStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime(RFC 3339 literal format) of the last updated time range to filter test profiles. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-testIds">
    <td><CopyableCode code="testIds" /></td>
    <td><code>array</code></td>
    <td>Comma separated list IDs of the tests which should be associated with the test profiles to fetch. Default value is None.</td>
</tr>
<tr id="parameter-testProfileIds">
    <td><CopyableCode code="testProfileIds" /></td>
    <td><code>array</code></td>
    <td>Comma separated list of IDs of the test profiles to filter. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_test_profile"
    values={[
        { label: 'get_test_profile', value: 'get_test_profile' },
        { label: 'list_test_profiles', value: 'list_test_profiles' }
    ]}
>
<TabItem value="get_test_profile">

Get load test profile details. Get load test profile details by test profile Id.

```sql
SELECT
createdBy,
createdDateTime,
description,
displayName,
lastModifiedBy,
lastModifiedDateTime,
targetResourceConfigurations,
targetResourceId,
testId,
testProfileId
FROM azure.developer_loadtesting.test_profiles
WHERE test_profile_id = '{{ test_profile_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_test_profiles">

List test profiles. Get all test profiles for the given filters.

```sql
SELECT
createdBy,
createdDateTime,
description,
displayName,
lastModifiedBy,
lastModifiedDateTime,
targetResourceConfigurations,
targetResourceId,
testId,
testProfileId
FROM azure.developer_loadtesting.test_profiles
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
AND lastModifiedStartTime = '{{ lastModifiedStartTime }}'
AND lastModifiedEndTime = '{{ lastModifiedEndTime }}'
AND testProfileIds = '{{ testProfileIds }}'
AND testIds = '{{ testIds }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_test_profile"
    values={[
        { label: 'create_or_update_test_profile', value: 'create_or_update_test_profile' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_test_profile">

Create a new test profile or update an existing test profile. Create a new test profile or update an existing test profile by providing the test profile Id.

```sql
INSERT INTO azure.developer_loadtesting.test_profiles (
displayName,
description,
testId,
targetResourceId,
targetResourceConfigurations,
test_profile_id,
endpoint
)
SELECT 
'{{ displayName }}',
'{{ description }}',
'{{ testId }}',
'{{ targetResourceId }}',
'{{ targetResourceConfigurations }}',
'{{ test_profile_id }}',
'{{ endpoint }}'
RETURNING
createdBy,
createdDateTime,
description,
displayName,
lastModifiedBy,
lastModifiedDateTime,
targetResourceConfigurations,
targetResourceId,
testId,
testProfileId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: test_profiles
  props:
    - name: test_profile_id
      value: "{{ test_profile_id }}"
      description: Required parameter for the test_profiles resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the test_profiles resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name of the test profile.
    - name: description
      value: "{{ description }}"
      description: |
        Description for the test profile.
    - name: testId
      value: "{{ testId }}"
      description: |
        Associated test ID for the test profile. This property is required for creating a Test Profile and it's not allowed to be updated.
    - name: targetResourceId
      value: "{{ targetResourceId }}"
      description: |
        Target resource ID on which the test profile is created. This property is required for creating a Test Profile and it's not allowed to be updated.
    - name: targetResourceConfigurations
      description: |
        Configurations of the target resource on which testing would be done.
      value:
        kind: "{{ kind }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_test_profile"
    values={[
        { label: 'create_or_update_test_profile', value: 'create_or_update_test_profile' }
    ]}
>
<TabItem value="create_or_update_test_profile">

Create a new test profile or update an existing test profile. Create a new test profile or update an existing test profile by providing the test profile Id.

```sql
REPLACE azure.developer_loadtesting.test_profiles
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
testId = '{{ testId }}',
targetResourceId = '{{ targetResourceId }}',
targetResourceConfigurations = '{{ targetResourceConfigurations }}'
WHERE 
test_profile_id = '{{ test_profile_id }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
createdBy,
createdDateTime,
description,
displayName,
lastModifiedBy,
lastModifiedDateTime,
targetResourceConfigurations,
targetResourceId,
testId,
testProfileId;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_test_profile"
    values={[
        { label: 'delete_test_profile', value: 'delete_test_profile' }
    ]}
>
<TabItem value="delete_test_profile">

Delete a test profile. Delete a test profile by its test profile Id.

```sql
DELETE FROM azure.developer_loadtesting.test_profiles
WHERE test_profile_id = '{{ test_profile_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
