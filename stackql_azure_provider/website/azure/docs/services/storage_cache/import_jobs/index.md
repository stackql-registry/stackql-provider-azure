--- 
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
  - storage_cache
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

Creates, updates, deletes, gets or lists an <code>import_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="import_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.import_jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_aml_filesystem', value: 'list_by_aml_filesystem' }
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
    <td><CopyableCode code="adminStatus" /></td>
    <td><code>string</code></td>
    <td>The administrative status of the import job. Possible values: 'Active', 'Cancel'. Passing in a value of 'Cancel' will cancel the current active import job. By default it is set to 'Active'. Known values are: "Active" and "Cancel". (Active, Cancel)</td>
</tr>
<tr>
    <td><CopyableCode code="conflictResolutionMode" /></td>
    <td><code>string</code></td>
    <td>How the import job will handle conflicts. For example, if the import job is trying to bring in a directory, but a file is at that path, how it handles it. Fail indicates that the import job should stop immediately and not do anything with the conflict. Skip indicates that it should pass over the conflict. OverwriteIfDirty causes the import job to delete and re-import the file or directory if it is a conflicting type, is dirty, or was not previously imported. OverwriteAlways extends OverwriteIfDirty to include releasing files that had been restored but were not dirty. Please reference `https://learn.microsoft.com/en-us/azure/azure-managed-lustre/ `_ for a thorough explanation of these resolution modes. Known values are: "Fail", "Skip", "OverwriteIfDirty", and "OverwriteAlways". (Fail, Skip, OverwriteIfDirty, OverwriteAlways)</td>
</tr>
<tr>
    <td><CopyableCode code="importPrefixes" /></td>
    <td><code>array</code></td>
    <td>An array of blob paths/prefixes that get imported into the cluster namespace. It has '/' as the default value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumErrors" /></td>
    <td><code>integer</code></td>
    <td>Total non-conflict oriented errors the import job will tolerate before exiting with failure. -1 means infinite. 0 means exit immediately and is the default.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state. Known values are: "Succeeded", "Failed", "Creating", "Deleting", "Updating", and "Canceled". (Succeeded, Failed, Creating, Deleting, Updating, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status of the import.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_aml_filesystem">

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
    <td><CopyableCode code="adminStatus" /></td>
    <td><code>string</code></td>
    <td>The administrative status of the import job. Possible values: 'Active', 'Cancel'. Passing in a value of 'Cancel' will cancel the current active import job. By default it is set to 'Active'. Known values are: "Active" and "Cancel". (Active, Cancel)</td>
</tr>
<tr>
    <td><CopyableCode code="conflictResolutionMode" /></td>
    <td><code>string</code></td>
    <td>How the import job will handle conflicts. For example, if the import job is trying to bring in a directory, but a file is at that path, how it handles it. Fail indicates that the import job should stop immediately and not do anything with the conflict. Skip indicates that it should pass over the conflict. OverwriteIfDirty causes the import job to delete and re-import the file or directory if it is a conflicting type, is dirty, or was not previously imported. OverwriteAlways extends OverwriteIfDirty to include releasing files that had been restored but were not dirty. Please reference `https://learn.microsoft.com/en-us/azure/azure-managed-lustre/ `_ for a thorough explanation of these resolution modes. Known values are: "Fail", "Skip", "OverwriteIfDirty", and "OverwriteAlways". (Fail, Skip, OverwriteIfDirty, OverwriteAlways)</td>
</tr>
<tr>
    <td><CopyableCode code="importPrefixes" /></td>
    <td><code>array</code></td>
    <td>An array of blob paths/prefixes that get imported into the cluster namespace. It has '/' as the default value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumErrors" /></td>
    <td><code>integer</code></td>
    <td>Total non-conflict oriented errors the import job will tolerate before exiting with failure. -1 means infinite. 0 means exit immediately and is the default.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state. Known values are: "Succeeded", "Failed", "Creating", "Deleting", "Updating", and "Canceled". (Succeeded, Failed, Creating, Deleting, Updating, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status of the import.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-import_job_name"><code>import_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns an import job.</td>
</tr>
<tr>
    <td><a href="#list_by_aml_filesystem"><CopyableCode code="list_by_aml_filesystem" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all import jobs the user has access to under an AML File System.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-import_job_name"><code>import_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an import job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-import_job_name"><code>import_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an import job instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-import_job_name"><code>import_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an import job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-import_job_name"><code>import_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Schedules an import job for deletion.</td>
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
<tr id="parameter-aml_filesystem_name">
    <td><CopyableCode code="aml_filesystem_name" /></td>
    <td><code>string</code></td>
    <td>Name for the AML file system. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric. Required.</td>
</tr>
<tr id="parameter-import_job_name">
    <td><CopyableCode code="import_job_name" /></td>
    <td><code>string</code></td>
    <td>Name for the import job. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_aml_filesystem', value: 'list_by_aml_filesystem' }
    ]}
>
<TabItem value="get">

Returns an import job.

```sql
SELECT
id,
name,
adminStatus,
conflictResolutionMode,
importPrefixes,
location,
maximumErrors,
provisioningState,
status,
systemData,
tags,
type
FROM azure.storage_cache.import_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' -- required
AND import_job_name = '{{ import_job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_aml_filesystem">

Returns all import jobs the user has access to under an AML File System.

```sql
SELECT
id,
name,
adminStatus,
conflictResolutionMode,
importPrefixes,
location,
maximumErrors,
provisioningState,
status,
systemData,
tags,
type
FROM azure.storage_cache.import_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update an import job.

```sql
INSERT INTO azure.storage_cache.import_jobs (
tags,
location,
properties,
resource_group_name,
aml_filesystem_name,
import_job_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ aml_filesystem_name }}',
'{{ import_job_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: import_jobs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the import_jobs resource.
    - name: aml_filesystem_name
      value: "{{ aml_filesystem_name }}"
      description: Required parameter for the import_jobs resource.
    - name: import_job_name
      value: "{{ import_job_name }}"
      description: Required parameter for the import_jobs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the import_jobs resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of the import job.
      value:
        provisioningState: "{{ provisioningState }}"
        adminStatus: "{{ adminStatus }}"
        importPrefixes:
          - "{{ importPrefixes }}"
        conflictResolutionMode: "{{ conflictResolutionMode }}"
        maximumErrors: {{ maximumErrors }}
        status:
          state: "{{ state }}"
          statusMessage: "{{ statusMessage }}"
          totalBlobsWalked: {{ totalBlobsWalked }}
          blobsWalkedPerSecond: {{ blobsWalkedPerSecond }}
          totalBlobsImported: {{ totalBlobsImported }}
          importedFiles: {{ importedFiles }}
          importedDirectories: {{ importedDirectories }}
          importedSymlinks: {{ importedSymlinks }}
          preexistingFiles: {{ preexistingFiles }}
          preexistingDirectories: {{ preexistingDirectories }}
          preexistingSymlinks: {{ preexistingSymlinks }}
          blobsImportedPerSecond: {{ blobsImportedPerSecond }}
          lastCompletionTime: "{{ lastCompletionTime }}"
          lastStartedTime: "{{ lastStartedTime }}"
          totalErrors: {{ totalErrors }}
          totalConflicts: {{ totalConflicts }}
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

Update an import job instance.

```sql
UPDATE azure.storage_cache.import_jobs
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' --required
AND import_job_name = '{{ import_job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update an import job.

```sql
REPLACE azure.storage_cache.import_jobs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' --required
AND import_job_name = '{{ import_job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Schedules an import job for deletion.

```sql
DELETE FROM azure.storage_cache.import_jobs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' --required
AND import_job_name = '{{ import_job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
