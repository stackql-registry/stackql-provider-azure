--- 
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
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

Creates, updates, deletes, gets or lists a <code>packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="packages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.packages" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_test_base_account', value: 'list_by_test_base_account' }
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
    <td><CopyableCode code="blobPath" /></td>
    <td><code>string</code></td>
    <td>The file path of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="flightingRing" /></td>
    <td><code>string</code></td>
    <td>The flighting ring for feature update.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag showing that whether the package is enabled. It doesn't schedule test for package which is not enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC timestamp when the package was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="packageStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the package. Known values are: "Unknown", "Registered", "Ready", "Error", "ValidatingPackage", "PreValidationCheckPass", "Deleted", "ValidationLongerThanUsual", and "VerifyingPackage".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Cancelled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetOSList" /></td>
    <td><code>array</code></td>
    <td>Specifies the target OSs of specific OS Update types.</td>
</tr>
<tr>
    <td><CopyableCode code="testTypes" /></td>
    <td><code>array</code></td>
    <td>OOB, functional or both. Mapped to the data in 'tests' property.</td>
</tr>
<tr>
    <td><CopyableCode code="tests" /></td>
    <td><code>array</code></td>
    <td>The detailed test information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="validationResults" /></td>
    <td><code>array</code></td>
    <td>The validation results. There's validation on package when it's created or updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Application version.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_test_base_account">

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
    <td><CopyableCode code="blobPath" /></td>
    <td><code>string</code></td>
    <td>The file path of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="flightingRing" /></td>
    <td><code>string</code></td>
    <td>The flighting ring for feature update.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag showing that whether the package is enabled. It doesn't schedule test for package which is not enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC timestamp when the package was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="packageStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the package. Known values are: "Unknown", "Registered", "Ready", "Error", "ValidatingPackage", "PreValidationCheckPass", "Deleted", "ValidationLongerThanUsual", and "VerifyingPackage".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Cancelled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetOSList" /></td>
    <td><code>array</code></td>
    <td>Specifies the target OSs of specific OS Update types.</td>
</tr>
<tr>
    <td><CopyableCode code="testTypes" /></td>
    <td><code>array</code></td>
    <td>OOB, functional or both. Mapped to the data in 'tests' property.</td>
</tr>
<tr>
    <td><CopyableCode code="tests" /></td>
    <td><code>array</code></td>
    <td>The detailed test information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="validationResults" /></td>
    <td><code>array</code></td>
    <td>The validation results. There's validation on package when it's created or updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Application version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Test Base Package.</td>
</tr>
<tr>
    <td><a href="#list_by_test_base_account"><CopyableCode code="list_by_test_base_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the packages under a Test Base Account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or replace (overwrite/recreate, with potential downtime) a Test Base Package.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing Test Base Package.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Test Base Package.</td>
</tr>
<tr>
    <td><a href="#get_download_url"><CopyableCode code="get_download_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the download URL of a package.</td>
</tr>
<tr>
    <td><a href="#hard_delete"><CopyableCode code="hard_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Hard Delete a Test Base Package.</td>
</tr>
<tr>
    <td><a href="#run_test"><CopyableCode code="run_test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-package_name"><code>package_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-testType"><code>testType</code></a>, <a href="#parameter-osName"><code>osName</code></a></td>
    <td></td>
    <td>Trigger a test run on the package.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_test_base_account', value: 'list_by_test_base_account' }
    ]}
>
<TabItem value="get">

Gets a Test Base Package.

```sql
SELECT
id,
name,
applicationName,
blobPath,
etag,
flightingRing,
isEnabled,
lastModifiedTime,
location,
packageStatus,
provisioningState,
systemData,
tags,
targetOSList,
testTypes,
tests,
type,
validationResults,
version
FROM azure_extras.testbase.packages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND package_name = '{{ package_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_test_base_account">

Lists all the packages under a Test Base Account.

```sql
SELECT
id,
name,
applicationName,
blobPath,
etag,
flightingRing,
isEnabled,
lastModifiedTime,
location,
packageStatus,
provisioningState,
systemData,
tags,
targetOSList,
testTypes,
tests,
type,
validationResults,
version
FROM azure_extras.testbase.packages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create or replace (overwrite/recreate, with potential downtime) a Test Base Package.

```sql
INSERT INTO azure_extras.testbase.packages (
tags,
location,
properties,
resource_group_name,
test_base_account_name,
package_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ test_base_account_name }}',
'{{ package_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: packages
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the packages resource.
    - name: test_base_account_name
      value: "{{ test_base_account_name }}"
      description: Required parameter for the packages resource.
    - name: package_name
      value: "{{ package_name }}"
      description: Required parameter for the packages resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the packages resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags of the resource.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        applicationName: "{{ applicationName }}"
        version: "{{ version }}"
        targetOSList:
          - osUpdateType: "{{ osUpdateType }}"
            targetOSs: "{{ targetOSs }}"
            baselineOSs: "{{ baselineOSs }}"
        flightingRing: "{{ flightingRing }}"
        blobPath: "{{ blobPath }}"
        tests:
          - testType: "{{ testType }}"
            validationRunStatus: "{{ validationRunStatus }}"
            validationResultId: "{{ validationResultId }}"
            isActive: {{ isActive }}
            commands: "{{ commands }}"
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

Update an existing Test Base Package.

```sql
UPDATE azure_extras.testbase.packages
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND test_base_account_name = '{{ test_base_account_name }}' --required
AND package_name = '{{ package_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
systemData,
tags,
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

Deletes a Test Base Package.

```sql
DELETE FROM azure_extras.testbase.packages
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND test_base_account_name = '{{ test_base_account_name }}' --required
AND package_name = '{{ package_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_download_url"
    values={[
        { label: 'get_download_url', value: 'get_download_url' },
        { label: 'hard_delete', value: 'hard_delete' },
        { label: 'run_test', value: 'run_test' }
    ]}
>
<TabItem value="get_download_url">

Gets the download URL of a package.

```sql
EXEC azure_extras.testbase.packages.get_download_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@package_name='{{ package_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="hard_delete">

Hard Delete a Test Base Package.

```sql
EXEC azure_extras.testbase.packages.hard_delete 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@package_name='{{ package_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_test">

Trigger a test run on the package.

```sql
EXEC azure_extras.testbase.packages.run_test 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@package_name='{{ package_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"testType": "{{ testType }}", 
"osUpdateType": "{{ osUpdateType }}", 
"osName": "{{ osName }}", 
"releaseName": "{{ releaseName }}", 
"flightingRing": "{{ flightingRing }}"
}'
;
```
</TabItem>
</Tabs>
