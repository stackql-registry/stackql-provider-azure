--- 
title: path
hide_title: false
hide_table_of_contents: false
keywords:
  - path
  - storage_file_datalake
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

Creates, updates, deletes, gets or lists a <code>path</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="path" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_file_datalake.path" /></td></tr>
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
    <td><a href="#lease"><CopyableCode code="lease" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-x-ms-lease-action"><code>x-ms-lease-action</code></a>, <a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-lease-break-period"><code>x-ms-lease-break-period</code></a>, <a href="#parameter-x-ms-lease-id"><code>x-ms-lease-id</code></a>, <a href="#parameter-x-ms-proposed-lease-id"><code>x-ms-proposed-lease-id</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-x-ms-lease-duration"><code>x-ms-lease-duration</code></a></td>
    <td>Lease Path. Create and manage a lease to restrict write and delete access to the path. This operation supports conditional HTTP requests. For more information, see `Specifying Conditional Headers for Blob Service Operations `_.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-x-ms-lease-action">
    <td><CopyableCode code="x-ms-lease-action" /></td>
    <td><code>string</code></td>
    <td>There are five lease actions: "acquire", "break", "change", "renew", and "release". Use "acquire" and specify the "x-ms-proposed-lease-id" and "x-ms-lease-duration" to acquire a new lease. Use "break" to break an existing lease. When a lease is broken, the lease break period is allowed to elapse, during which time no lease operation except break and release can be performed on the file. When a lease is successfully broken, the response indicates the interval in seconds until a new lease can be acquired. Use "change" and specify the current lease ID in "x-ms-lease-id" and the new lease ID in "x-ms-proposed-lease-id" to change the lease ID of an active lease. Use "renew" and specify the "x-ms-lease-id" to renew an existing lease. Use "release" and specify the "x-ms-lease-id" to release a lease. Known values are: "acquire", "break", "change", "renew", and "release". Required.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see</td>
</tr>
<tr id="parameter-x-ms-client-request-id">
    <td><CopyableCode code="x-ms-client-request-id" /></td>
    <td><code>string</code></td>
    <td>Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-lease-break-period">
    <td><CopyableCode code="x-ms-lease-break-period" /></td>
    <td><code>integer</code></td>
    <td>The lease break period duration is optional to break a lease, and specifies the break period of the lease in seconds. The lease break duration must be between 0 and 60 seconds. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-lease-duration">
    <td><CopyableCode code="x-ms-lease-duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-lease-id">
    <td><CopyableCode code="x-ms-lease-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-proposed-lease-id">
    <td><CopyableCode code="x-ms-proposed-lease-id" /></td>
    <td><code>string</code></td>
    <td>Proposed lease ID, in a GUID string format. The Blob service returns 400 (Invalid request) if the proposed lease ID is not in the correct format. See Guid Constructor (String) for a list of valid GUID string formats. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="lease"
    values={[
        { label: 'lease', value: 'lease' }
    ]}
>
<TabItem value="lease">

Lease Path. Create and manage a lease to restrict write and delete access to the path. This operation supports conditional HTTP requests. For more information, see `Specifying Conditional Headers for Blob Service Operations `_.

```sql
EXEC azure.storage_file_datalake.path.lease 
@x-ms-lease-action='{{ x-ms-lease-action }}' --required, 
@x-ms-version='{{ x-ms-version }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-request-id='{{ x-ms-client-request-id }}', 
@timeout='{{ timeout }}', 
@x-ms-lease-break-period='{{ x-ms-lease-break-period }}', 
@x-ms-lease-id='{{ x-ms-lease-id }}', 
@x-ms-proposed-lease-id='{{ x-ms-proposed-lease-id }}', 
@If-Match='{{ If-Match }}', 
@If-None-Match='{{ If-None-Match }}', 
@If-Modified-Since='{{ If-Modified-Since }}', 
@If-Unmodified-Since='{{ If-Unmodified-Since }}', 
@x-ms-lease-duration='{{ x-ms-lease-duration }}' 
@@json=
'{
"leaseId": "{{ leaseId }}"
}'
;
```
</TabItem>
</Tabs>
