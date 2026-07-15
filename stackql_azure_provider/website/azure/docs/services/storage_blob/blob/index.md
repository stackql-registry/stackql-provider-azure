--- 
title: blob
hide_title: false
hide_table_of_contents: false
keywords:
  - blob
  - storage_blob
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

Creates, updates, deletes, gets or lists a <code>blob</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="blob" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_blob.blob" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-snapshot"><code>snapshot</code></a>, <a href="#parameter-versionid"><code>versionid</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-lease-id"><code>x-ms-lease-id</code></a>, <a href="#parameter-x-ms-delete-snapshots"><code>x-ms-delete-snapshots</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a>, <a href="#parameter-x-ms-if-tags"><code>x-ms-if-tags</code></a>, <a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-deletetype"><code>deletetype</code></a>, <a href="#parameter-x-ms-access-tier-if-modified-since"><code>x-ms-access-tier-if-modified-since</code></a>, <a href="#parameter-x-ms-access-tier-if-unmodified-since"><code>x-ms-access-tier-if-unmodified-since</code></a></td>
    <td>If the storage account's soft delete feature is disabled then, when a blob is deleted, it is permanently removed from the storage account. If the storage account's soft delete feature is enabled, then, when a blob is deleted, it is marked for deletion and becomes inaccessible immediately. However, the blob service retains the blob or snapshot for the number of days specified by the DeleteRetentionPolicy section of [Storage service properties] (Set-Blob-Service-Properties.md). After the specified number of days has passed, the blob's data is permanently removed from the storage account. Note that you continue to be charged for the soft-deleted blob's storage until it is permanently removed. Use the List Blobs API and specify the "include=deleted" query parameter to discover which blobs and snapshots have been soft deleted. You can then use the Undelete Blob API to restore a soft-deleted blob. All other operations on a soft-deleted blob or snapshot causes the service to return an HTTP status code of 404 (ResourceNotFound).</td>
</tr>
<tr>
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-snapshot"><code>snapshot</code></a>, <a href="#parameter-versionid"><code>versionid</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-lease-id"><code>x-ms-lease-id</code></a>, <a href="#parameter-x-ms-encryption-key"><code>x-ms-encryption-key</code></a>, <a href="#parameter-x-ms-encryption-key-sha256"><code>x-ms-encryption-key-sha256</code></a>, <a href="#parameter-x-ms-encryption-algorithm"><code>x-ms-encryption-algorithm</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a>, <a href="#parameter-x-ms-if-tags"><code>x-ms-if-tags</code></a>, <a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a></td>
    <td>The Get Properties operation returns all user-defined metadata, standard HTTP properties, and system properties for the blob. It does not return the content of the blob.</td>
</tr>
<tr>
    <td><a href="#get_account_info"><CopyableCode code="get_account_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a></td>
    <td>Returns the sku name and account kind.</td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-snapshot"><code>snapshot</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-lease-id"><code>x-ms-lease-id</code></a>, <a href="#parameter-x-ms-encryption-key"><code>x-ms-encryption-key</code></a>, <a href="#parameter-x-ms-encryption-key-sha256"><code>x-ms-encryption-key-sha256</code></a>, <a href="#parameter-x-ms-encryption-algorithm"><code>x-ms-encryption-algorithm</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a>, <a href="#parameter-x-ms-if-tags"><code>x-ms-if-tags</code></a>, <a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a></td>
    <td>The Query operation enables users to select/project on blob data by providing simple query expressions.</td>
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
<tr id="parameter-account">
    <td><CopyableCode code="account" /></td>
    <td><code>string</code></td>
    <td>Storage account name. (default: )</td>
</tr>
<tr id="parameter-x-ms-version">
    <td><CopyableCode code="x-ms-version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Modified-Since">
    <td><CopyableCode code="If-Modified-Since" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-deletetype">
    <td><CopyableCode code="deletetype" /></td>
    <td><code>string</code></td>
    <td>Optional. Only possible value is 'permanent', which specifies to permanently delete a blob if blob soft delete is enabled. Known values are "Permanent" and None. Default value is "Permanent".</td>
</tr>
<tr id="parameter-snapshot">
    <td><CopyableCode code="snapshot" /></td>
    <td><code>string</code></td>
    <td>The snapshot parameter is an opaque DateTime value that, when present, specifies the blob snapshot to retrieve. For more information on working with blob snapshots, see Creating a Snapshot of a Blob.. Default value is None.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see</td>
</tr>
<tr id="parameter-versionid">
    <td><CopyableCode code="versionid" /></td>
    <td><code>string</code></td>
    <td>The version id parameter is an opaque DateTime value that, when present, specifies the version of the blob to operate on. It's for service version 2019-10-10 and newer. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-access-tier-if-modified-since">
    <td><CopyableCode code="x-ms-access-tier-if-modified-since" /></td>
    <td><code>string</code></td>
    <td>Specify this header value to operate only on a blob if the access-tier has been modified since the specified date/time. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-access-tier-if-unmodified-since">
    <td><CopyableCode code="x-ms-access-tier-if-unmodified-since" /></td>
    <td><code>string</code></td>
    <td>Specify this header value to operate only on a blob if the access-tier has not been modified since the specified date/time. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-client-request-id">
    <td><CopyableCode code="x-ms-client-request-id" /></td>
    <td><code>string</code></td>
    <td>Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-delete-snapshots">
    <td><CopyableCode code="x-ms-delete-snapshots" /></td>
    <td><code>string</code></td>
    <td>Required if the blob has associated snapshots. Specify one of the following two options: include: Delete the base blob and all of its snapshots. only: Delete only the blob's snapshots and not the blob itself. Known values are: "include" and "only". Default value is None.</td>
</tr>
<tr id="parameter-x-ms-encryption-algorithm">
    <td><CopyableCode code="x-ms-encryption-algorithm" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-encryption-key">
    <td><CopyableCode code="x-ms-encryption-key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-encryption-key-sha256">
    <td><CopyableCode code="x-ms-encryption-key-sha256" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-if-tags">
    <td><CopyableCode code="x-ms-if-tags" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-lease-id">
    <td><CopyableCode code="x-ms-lease-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

If the storage account's soft delete feature is disabled then, when a blob is deleted, it is permanently removed from the storage account. If the storage account's soft delete feature is enabled, then, when a blob is deleted, it is marked for deletion and becomes inaccessible immediately. However, the blob service retains the blob or snapshot for the number of days specified by the DeleteRetentionPolicy section of [Storage service properties] (Set-Blob-Service-Properties.md). After the specified number of days has passed, the blob's data is permanently removed from the storage account. Note that you continue to be charged for the soft-deleted blob's storage until it is permanently removed. Use the List Blobs API and specify the "include=deleted" query parameter to discover which blobs and snapshots have been soft deleted. You can then use the Undelete Blob API to restore a soft-deleted blob. All other operations on a soft-deleted blob or snapshot causes the service to return an HTTP status code of 404 (ResourceNotFound).

```sql
DELETE FROM azure.storage_blob.blob
WHERE x-ms-version = '{{ x-ms-version }}' --required
AND account = '{{ account }}' --required
AND snapshot = '{{ snapshot }}'
AND versionid = '{{ versionid }}'
AND timeout = '{{ timeout }}'
AND x-ms-lease-id = '{{ x-ms-lease-id }}'
AND x-ms-delete-snapshots = '{{ x-ms-delete-snapshots }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
AND If-Match = '{{ If-Match }}'
AND If-None-Match = '{{ If-None-Match }}'
AND x-ms-if-tags = '{{ x-ms-if-tags }}'
AND x-ms-client-request-id = '{{ x-ms-client-request-id }}'
AND deletetype = '{{ deletetype }}'
AND x-ms-access-tier-if-modified-since = '{{ x-ms-access-tier-if-modified-since }}'
AND x-ms-access-tier-if-unmodified-since = '{{ x-ms-access-tier-if-unmodified-since }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' },
        { label: 'get_account_info', value: 'get_account_info' },
        { label: 'query', value: 'query' }
    ]}
>
<TabItem value="get_properties">

The Get Properties operation returns all user-defined metadata, standard HTTP properties, and system properties for the blob. It does not return the content of the blob.

```sql
EXEC azure.storage_blob.blob.get_properties 
@x-ms-version='{{ x-ms-version }}' --required, 
@account='{{ account }}' --required, 
@snapshot='{{ snapshot }}', 
@versionid='{{ versionid }}', 
@timeout='{{ timeout }}', 
@x-ms-lease-id='{{ x-ms-lease-id }}', 
@x-ms-encryption-key='{{ x-ms-encryption-key }}', 
@x-ms-encryption-key-sha256='{{ x-ms-encryption-key-sha256 }}', 
@x-ms-encryption-algorithm='{{ x-ms-encryption-algorithm }}', 
@If-Modified-Since='{{ If-Modified-Since }}', 
@If-Unmodified-Since='{{ If-Unmodified-Since }}', 
@If-Match='{{ If-Match }}', 
@If-None-Match='{{ If-None-Match }}', 
@x-ms-if-tags='{{ x-ms-if-tags }}', 
@x-ms-client-request-id='{{ x-ms-client-request-id }}' 
@@json=
'{
"leaseId": "{{ leaseId }}"
}'
;
```
</TabItem>
<TabItem value="get_account_info">

Returns the sku name and account kind.

```sql
EXEC azure.storage_blob.blob.get_account_info 
@x-ms-version='{{ x-ms-version }}' --required, 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}', 
@x-ms-client-request-id='{{ x-ms-client-request-id }}'
;
```
</TabItem>
<TabItem value="query">

The Query operation enables users to select/project on blob data by providing simple query expressions.

```sql
EXEC azure.storage_blob.blob.query 
@x-ms-version='{{ x-ms-version }}' --required, 
@account='{{ account }}' --required, 
@snapshot='{{ snapshot }}', 
@timeout='{{ timeout }}', 
@x-ms-lease-id='{{ x-ms-lease-id }}', 
@x-ms-encryption-key='{{ x-ms-encryption-key }}', 
@x-ms-encryption-key-sha256='{{ x-ms-encryption-key-sha256 }}', 
@x-ms-encryption-algorithm='{{ x-ms-encryption-algorithm }}', 
@If-Modified-Since='{{ If-Modified-Since }}', 
@If-Unmodified-Since='{{ If-Unmodified-Since }}', 
@If-Match='{{ If-Match }}', 
@If-None-Match='{{ If-None-Match }}', 
@x-ms-if-tags='{{ x-ms-if-tags }}', 
@x-ms-client-request-id='{{ x-ms-client-request-id }}' 
@@json=
'{
"leaseId": "{{ leaseId }}"
}'
;
```
</TabItem>
</Tabs>
