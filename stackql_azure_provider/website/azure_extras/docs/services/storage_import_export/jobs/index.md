--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storage_import_export
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storage_import_export.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td>Specifies the resource identifier of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="backupDriveManifest" /></td>
    <td><code>boolean</code></td>
    <td>Default value is false. Indicates whether the manifest files on the drives should be copied to block blobs.</td>
</tr>
<tr>
    <td><CopyableCode code="cancelRequested" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether a request has been submitted to cancel the job.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryPackage" /></td>
    <td><code>object</code></td>
    <td>Contains information about the package being shipped by the customer to the Microsoft data center.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsPath" /></td>
    <td><code>string</code></td>
    <td>The virtual blob directory to which the copy logs and backups of drive manifest files (if enabled) will be stored.</td>
</tr>
<tr>
    <td><CopyableCode code="driveList" /></td>
    <td><code>array</code></td>
    <td>List of up to ten drives that comprise the job. The drive list is a required element for an import job; it is not specified for export jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionKey" /></td>
    <td><code>object</code></td>
    <td>Contains information about the encryption key.</td>
</tr>
<tr>
    <td><CopyableCode code="export" /></td>
    <td><code>object</code></td>
    <td>A property containing information about the blobs to be exported for an export job. This property is included for export jobs only.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Specifies the job identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="incompleteBlobListUri" /></td>
    <td><code>string</code></td>
    <td>A blob path that points to a block blob containing a list of blob names that were not exported due to insufficient drive space. If all blobs were exported successfully, then this element is not included in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>The type of job.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure location where the job is created.</td>
</tr>
<tr>
    <td><CopyableCode code="logLevel" /></td>
    <td><code>string</code></td>
    <td>Default value is Error. Indicates whether error logging or verbose logging will be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>Overall percentage completed for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Specifies the provisioning state of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="returnAddress" /></td>
    <td><code>object</code></td>
    <td>Specifies the return address information for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="returnPackage" /></td>
    <td><code>object</code></td>
    <td>Contains information about the package being shipped from the Microsoft data center to the customer to return the drives. The format is the same as the deliveryPackage property above. This property is not included if the drives have not yet been returned.</td>
</tr>
<tr>
    <td><CopyableCode code="returnShipping" /></td>
    <td><code>object</code></td>
    <td>Specifies the return carrier and customer's account with the carrier.</td>
</tr>
<tr>
    <td><CopyableCode code="shippingInformation" /></td>
    <td><code>object</code></td>
    <td>Contains information about the Microsoft datacenter to which the drives should be shipped.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the storage account where data will be imported to or exported from.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>SystemData of ImportExport Jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the job resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>Specifies the resource identifier of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="backupDriveManifest" /></td>
    <td><code>boolean</code></td>
    <td>Default value is false. Indicates whether the manifest files on the drives should be copied to block blobs.</td>
</tr>
<tr>
    <td><CopyableCode code="cancelRequested" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether a request has been submitted to cancel the job.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryPackage" /></td>
    <td><code>object</code></td>
    <td>Contains information about the package being shipped by the customer to the Microsoft data center.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsPath" /></td>
    <td><code>string</code></td>
    <td>The virtual blob directory to which the copy logs and backups of drive manifest files (if enabled) will be stored.</td>
</tr>
<tr>
    <td><CopyableCode code="driveList" /></td>
    <td><code>array</code></td>
    <td>List of up to ten drives that comprise the job. The drive list is a required element for an import job; it is not specified for export jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionKey" /></td>
    <td><code>object</code></td>
    <td>Contains information about the encryption key.</td>
</tr>
<tr>
    <td><CopyableCode code="export" /></td>
    <td><code>object</code></td>
    <td>A property containing information about the blobs to be exported for an export job. This property is included for export jobs only.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Specifies the job identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="incompleteBlobListUri" /></td>
    <td><code>string</code></td>
    <td>A blob path that points to a block blob containing a list of blob names that were not exported due to insufficient drive space. If all blobs were exported successfully, then this element is not included in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>The type of job.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure location where the job is created.</td>
</tr>
<tr>
    <td><CopyableCode code="logLevel" /></td>
    <td><code>string</code></td>
    <td>Default value is Error. Indicates whether error logging or verbose logging will be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>Overall percentage completed for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Specifies the provisioning state of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="returnAddress" /></td>
    <td><code>object</code></td>
    <td>Specifies the return address information for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="returnPackage" /></td>
    <td><code>object</code></td>
    <td>Contains information about the package being shipped from the Microsoft data center to the customer to return the drives. The format is the same as the deliveryPackage property above. This property is not included if the drives have not yet been returned.</td>
</tr>
<tr>
    <td><CopyableCode code="returnShipping" /></td>
    <td><code>object</code></td>
    <td>Specifies the return carrier and customer's account with the carrier.</td>
</tr>
<tr>
    <td><CopyableCode code="shippingInformation" /></td>
    <td><code>object</code></td>
    <td>Contains information about the Microsoft datacenter to which the drives should be shipped.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the storage account where data will be imported to or exported from.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>SystemData of ImportExport Jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the job resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td>Specifies the resource identifier of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="backupDriveManifest" /></td>
    <td><code>boolean</code></td>
    <td>Default value is false. Indicates whether the manifest files on the drives should be copied to block blobs.</td>
</tr>
<tr>
    <td><CopyableCode code="cancelRequested" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether a request has been submitted to cancel the job.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryPackage" /></td>
    <td><code>object</code></td>
    <td>Contains information about the package being shipped by the customer to the Microsoft data center.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsPath" /></td>
    <td><code>string</code></td>
    <td>The virtual blob directory to which the copy logs and backups of drive manifest files (if enabled) will be stored.</td>
</tr>
<tr>
    <td><CopyableCode code="driveList" /></td>
    <td><code>array</code></td>
    <td>List of up to ten drives that comprise the job. The drive list is a required element for an import job; it is not specified for export jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionKey" /></td>
    <td><code>object</code></td>
    <td>Contains information about the encryption key.</td>
</tr>
<tr>
    <td><CopyableCode code="export" /></td>
    <td><code>object</code></td>
    <td>A property containing information about the blobs to be exported for an export job. This property is included for export jobs only.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Specifies the job identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="incompleteBlobListUri" /></td>
    <td><code>string</code></td>
    <td>A blob path that points to a block blob containing a list of blob names that were not exported due to insufficient drive space. If all blobs were exported successfully, then this element is not included in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>The type of job.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure location where the job is created.</td>
</tr>
<tr>
    <td><CopyableCode code="logLevel" /></td>
    <td><code>string</code></td>
    <td>Default value is Error. Indicates whether error logging or verbose logging will be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>Overall percentage completed for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Specifies the provisioning state of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="returnAddress" /></td>
    <td><code>object</code></td>
    <td>Specifies the return address information for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="returnPackage" /></td>
    <td><code>object</code></td>
    <td>Contains information about the package being shipped from the Microsoft data center to the customer to return the drives. The format is the same as the deliveryPackage property above. This property is not included if the drives have not yet been returned.</td>
</tr>
<tr>
    <td><CopyableCode code="returnShipping" /></td>
    <td><code>object</code></td>
    <td>Specifies the return carrier and customer's account with the carrier.</td>
</tr>
<tr>
    <td><CopyableCode code="shippingInformation" /></td>
    <td><code>object</code></td>
    <td>Contains information about the Microsoft datacenter to which the drives should be shipped.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the storage account where data will be imported to or exported from.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>SystemData of ImportExport Jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the job resource.</td>
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
    <td><a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Gets information about an existing job.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Returns all active and completed jobs in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Returns all active and completed jobs in a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-client-tenant-id"><code>x-ms-client-tenant-id</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Creates a new job or updates an existing job in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Deletes an existing job. Only jobs in the Creating or Completed states can be deleted.</td>
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
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The name of the import/export job. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name uniquely identifies the resource group within the user subscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Can be used to restrict the results to certain conditions. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100. Default value is None.</td>
</tr>
<tr id="parameter-Accept-Language">
    <td><CopyableCode code="Accept-Language" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-client-tenant-id">
    <td><CopyableCode code="x-ms-client-tenant-id" /></td>
    <td><code>string</code></td>
    <td>The tenant ID of the client making the request. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets information about an existing job.

```sql
SELECT
id,
name,
backupDriveManifest,
cancelRequested,
deliveryPackage,
diagnosticsPath,
driveList,
encryptionKey,
export,
identity,
incompleteBlobListUri,
jobType,
location,
logLevel,
percentComplete,
provisioningState,
returnAddress,
returnPackage,
returnShipping,
shippingInformation,
state,
storageAccountId,
systemData,
tags,
type
FROM azure_extras.storage_import_export.jobs
WHERE job_name = '{{ job_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND Accept-Language = '{{ Accept-Language }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns all active and completed jobs in a resource group.

```sql
SELECT
id,
name,
backupDriveManifest,
cancelRequested,
deliveryPackage,
diagnosticsPath,
driveList,
encryptionKey,
export,
identity,
incompleteBlobListUri,
jobType,
location,
logLevel,
percentComplete,
provisioningState,
returnAddress,
returnPackage,
returnShipping,
shippingInformation,
state,
storageAccountId,
systemData,
tags,
type
FROM azure_extras.storage_import_export.jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
AND Accept-Language = '{{ Accept-Language }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Returns all active and completed jobs in a subscription.

```sql
SELECT
id,
name,
backupDriveManifest,
cancelRequested,
deliveryPackage,
diagnosticsPath,
driveList,
encryptionKey,
export,
identity,
incompleteBlobListUri,
jobType,
location,
logLevel,
percentComplete,
provisioningState,
returnAddress,
returnPackage,
returnShipping,
shippingInformation,
state,
storageAccountId,
systemData,
tags,
type
FROM azure_extras.storage_import_export.jobs
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
AND Accept-Language = '{{ Accept-Language }}'
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

Creates a new job or updates an existing job in the specified subscription.

```sql
INSERT INTO azure_extras.storage_import_export.jobs (
location,
tags,
properties,
job_name,
resource_group_name,
subscription_id,
x-ms-client-tenant-id,
Accept-Language
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ job_name }}',
'{{ resource_group_name }}',
'{{ subscription_id }}',
'{{ x-ms-client-tenant-id }}',
'{{ Accept-Language }}'
RETURNING
id,
name,
identity,
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
- name: jobs
  props:
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the jobs resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the jobs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the jobs resource.
    - name: location
      value: "{{ location }}"
      description: |
        Specifies the supported Azure location where the job should be created.
    - name: tags
      value: "{{ tags }}"
      description: |
        Specifies the tags that will be assigned to the job.
    - name: properties
      description: |
        Specifies the job properties.
      value:
        storageAccountId: "{{ storageAccountId }}"
        jobType: "{{ jobType }}"
        returnAddress:
          recipientName: "{{ recipientName }}"
          streetAddress1: "{{ streetAddress1 }}"
          streetAddress2: "{{ streetAddress2 }}"
          city: "{{ city }}"
          stateOrProvince: "{{ stateOrProvince }}"
          postalCode: "{{ postalCode }}"
          countryOrRegion: "{{ countryOrRegion }}"
          phone: "{{ phone }}"
          email: "{{ email }}"
        returnShipping:
          carrierName: "{{ carrierName }}"
          carrierAccountNumber: "{{ carrierAccountNumber }}"
        shippingInformation:
          recipientName: "{{ recipientName }}"
          streetAddress1: "{{ streetAddress1 }}"
          streetAddress2: "{{ streetAddress2 }}"
          city: "{{ city }}"
          stateOrProvince: "{{ stateOrProvince }}"
          postalCode: "{{ postalCode }}"
          countryOrRegion: "{{ countryOrRegion }}"
          phone: "{{ phone }}"
          additionalInformation: "{{ additionalInformation }}"
        deliveryPackage:
          carrierName: "{{ carrierName }}"
          trackingNumber: "{{ trackingNumber }}"
          driveCount: {{ driveCount }}
          shipDate: "{{ shipDate }}"
        returnPackage:
          carrierName: "{{ carrierName }}"
          trackingNumber: "{{ trackingNumber }}"
          driveCount: {{ driveCount }}
          shipDate: "{{ shipDate }}"
        diagnosticsPath: "{{ diagnosticsPath }}"
        logLevel: "{{ logLevel }}"
        backupDriveManifest: {{ backupDriveManifest }}
        state: "{{ state }}"
        cancelRequested: {{ cancelRequested }}
        percentComplete: {{ percentComplete }}
        incompleteBlobListUri: "{{ incompleteBlobListUri }}"
        driveList:
          - driveId: "{{ driveId }}"
            bitLockerKey: "{{ bitLockerKey }}"
            manifestFile: "{{ manifestFile }}"
            manifestHash: "{{ manifestHash }}"
            driveHeaderHash: "{{ driveHeaderHash }}"
            state: "{{ state }}"
            copyStatus: "{{ copyStatus }}"
            percentComplete: {{ percentComplete }}
            verboseLogUri: "{{ verboseLogUri }}"
            errorLogUri: "{{ errorLogUri }}"
            manifestUri: "{{ manifestUri }}"
            bytesSucceeded: {{ bytesSucceeded }}
        export:
          blobListBlobPath: "{{ blobListBlobPath }}"
          blobList:
            blobPath:
              - "{{ blobPath }}"
            blobPathPrefix:
              - "{{ blobPathPrefix }}"
        provisioningState: "{{ provisioningState }}"
        encryptionKey:
          kekType: "{{ kekType }}"
          kekUrl: "{{ kekUrl }}"
          kekVaultResourceID: "{{ kekVaultResourceID }}"
    - name: x-ms-client-tenant-id
      value: "{{ x-ms-client-tenant-id }}"
      description: The tenant ID of the client making the request. Default value is None.
      description: The tenant ID of the client making the request. Default value is None.
    - name: Accept-Language
      value: "{{ Accept-Language }}"
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

Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job.

```sql
UPDATE azure_extras.storage_import_export.jobs
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
job_name = '{{ job_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND Accept-Language = '{{ Accept-Language}}'
RETURNING
id,
name,
identity,
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

Deletes an existing job. Only jobs in the Creating or Completed states can be deleted.

```sql
DELETE FROM azure_extras.storage_import_export.jobs
WHERE job_name = '{{ job_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND Accept-Language = '{{ Accept-Language }}'
;
```
</TabItem>
</Tabs>
