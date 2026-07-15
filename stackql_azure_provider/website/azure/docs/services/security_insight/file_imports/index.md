--- 
title: file_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - file_imports
  - security_insight
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

Creates, updates, deletes, gets or lists a <code>file_imports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="file_imports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.file_imports" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type of this file. Required. Known values are: "BasicIndicator", "StixIndicator", and "Unspecified". (BasicIndicator, StixIndicator, Unspecified)</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the file was imported.</td>
</tr>
<tr>
    <td><CopyableCode code="errorFile" /></td>
    <td><code>object</code></td>
    <td>Represents the error file (if the import was ingested with errors or failed the validation).</td>
</tr>
<tr>
    <td><CopyableCode code="errorsPreview" /></td>
    <td><code>array</code></td>
    <td>An ordered list of some of the errors that were encountered during validation.</td>
</tr>
<tr>
    <td><CopyableCode code="filesValidUntilTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the files associated with this import are deleted from the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="importFile" /></td>
    <td><code>object</code></td>
    <td>Represents the imported file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="importValidUntilTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the file import record is soft deleted from the database and history.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestedRecordCount" /></td>
    <td><code>integer</code></td>
    <td>The number of records that have been successfully ingested.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestionMode" /></td>
    <td><code>string</code></td>
    <td>Describes how to ingest the records in the file. Required. Known values are: "IngestOnlyIfAllAreValid", "IngestAnyValidRecords", and "Unspecified". (IngestOnlyIfAllAreValid, IngestAnyValidRecords, Unspecified)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source for the data in the file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the file import. Known values are: "FatalError", "Ingested", "IngestedWithErrors", "InProgress", "Invalid", "WaitingForUpload", and "Unspecified". (FatalError, Ingested, IngestedWithErrors, InProgress, Invalid, WaitingForUpload, Unspecified)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRecordCount" /></td>
    <td><code>integer</code></td>
    <td>The number of records in the file.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validRecordCount" /></td>
    <td><code>integer</code></td>
    <td>The number of records that have passed validation.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type of this file. Required. Known values are: "BasicIndicator", "StixIndicator", and "Unspecified". (BasicIndicator, StixIndicator, Unspecified)</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the file was imported.</td>
</tr>
<tr>
    <td><CopyableCode code="errorFile" /></td>
    <td><code>object</code></td>
    <td>Represents the error file (if the import was ingested with errors or failed the validation).</td>
</tr>
<tr>
    <td><CopyableCode code="errorsPreview" /></td>
    <td><code>array</code></td>
    <td>An ordered list of some of the errors that were encountered during validation.</td>
</tr>
<tr>
    <td><CopyableCode code="filesValidUntilTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the files associated with this import are deleted from the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="importFile" /></td>
    <td><code>object</code></td>
    <td>Represents the imported file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="importValidUntilTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the file import record is soft deleted from the database and history.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestedRecordCount" /></td>
    <td><code>integer</code></td>
    <td>The number of records that have been successfully ingested.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestionMode" /></td>
    <td><code>string</code></td>
    <td>Describes how to ingest the records in the file. Required. Known values are: "IngestOnlyIfAllAreValid", "IngestAnyValidRecords", and "Unspecified". (IngestOnlyIfAllAreValid, IngestAnyValidRecords, Unspecified)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source for the data in the file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the file import. Known values are: "FatalError", "Ingested", "IngestedWithErrors", "InProgress", "Invalid", "WaitingForUpload", and "Unspecified". (FatalError, Ingested, IngestedWithErrors, InProgress, Invalid, WaitingForUpload, Unspecified)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRecordCount" /></td>
    <td><code>integer</code></td>
    <td>The number of records in the file.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validRecordCount" /></td>
    <td><code>integer</code></td>
    <td>The number of records that have passed validation.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-file_import_id"><code>file_import_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a file import.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Gets all file imports.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-file_import_id"><code>file_import_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates the file import.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-file_import_id"><code>file_import_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the file import.</td>
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
<tr id="parameter-file_import_id">
    <td><CopyableCode code="file_import_id" /></td>
    <td><code>string</code></td>
    <td>File import ID. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filters the results, based on a Boolean condition. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Sorts the results. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Returns only the first n results. Optional. Default value is None.</td>
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

Gets a file import.

```sql
SELECT
id,
name,
contentType,
createdTimeUTC,
errorFile,
errorsPreview,
filesValidUntilTimeUTC,
importFile,
importValidUntilTimeUTC,
ingestedRecordCount,
ingestionMode,
source,
state,
systemData,
totalRecordCount,
type,
validRecordCount
FROM azure.security_insight.file_imports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND file_import_id = '{{ file_import_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all file imports.

```sql
SELECT
id,
name,
contentType,
createdTimeUTC,
errorFile,
errorsPreview,
filesValidUntilTimeUTC,
importFile,
importValidUntilTimeUTC,
ingestedRecordCount,
ingestionMode,
source,
state,
systemData,
totalRecordCount,
type,
validRecordCount
FROM azure.security_insight.file_imports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Creates the file import.

```sql
INSERT INTO azure.security_insight.file_imports (
properties,
resource_group_name,
workspace_name,
file_import_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ file_import_id }}',
'{{ subscription_id }}'
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
- name: file_imports
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the file_imports resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the file_imports resource.
    - name: file_import_id
      value: "{{ file_import_id }}"
      description: Required parameter for the file_imports resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the file_imports resource.
    - name: properties
      description: |
        File import properties.
      value:
        ingestionMode: "{{ ingestionMode }}"
        contentType: "{{ contentType }}"
        createdTimeUTC: "{{ createdTimeUTC }}"
        errorFile:
          fileFormat: "{{ fileFormat }}"
          fileName: "{{ fileName }}"
          fileSize: {{ fileSize }}
          fileContentUri: "{{ fileContentUri }}"
          deleteStatus: "{{ deleteStatus }}"
        errorsPreview:
          - recordIndex: {{ recordIndex }}
            errorMessages: "{{ errorMessages }}"
        importFile:
          fileFormat: "{{ fileFormat }}"
          fileName: "{{ fileName }}"
          fileSize: {{ fileSize }}
          fileContentUri: "{{ fileContentUri }}"
          deleteStatus: "{{ deleteStatus }}"
        ingestedRecordCount: {{ ingestedRecordCount }}
        source: "{{ source }}"
        state: "{{ state }}"
        totalRecordCount: {{ totalRecordCount }}
        validRecordCount: {{ validRecordCount }}
        filesValidUntilTimeUTC: "{{ filesValidUntilTimeUTC }}"
        importValidUntilTimeUTC: "{{ importValidUntilTimeUTC }}"
`}</CodeBlock>

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

Delete the file import.

```sql
DELETE FROM azure.security_insight.file_imports
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND file_import_id = '{{ file_import_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
