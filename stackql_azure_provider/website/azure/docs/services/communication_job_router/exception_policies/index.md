--- 
title: exception_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - exception_policies
  - communication_job_router
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

Creates, updates, deletes, gets or lists an <code>exception_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="exception_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_job_router.exception_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_exception_policy"
    values={[
        { label: 'get_exception_policy', value: 'get_exception_policy' },
        { label: 'list_exception_policies', value: 'list_exception_policies' }
    ]}
>
<TabItem value="get_exception_policy">

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
    <td>Id of an exception policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Friendly name of this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exceptionRules" /></td>
    <td><code>array</code></td>
    <td>A collection of exception rules on the exception policy.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_exception_policies">

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
    <td>Id of an exception policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Friendly name of this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exceptionRules" /></td>
    <td><code>array</code></td>
    <td>A collection of exception rules on the exception policy.</td>
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
    <td><a href="#get_exception_policy"><CopyableCode code="get_exception_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-exception_policy_id"><code>exception_policy_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves an existing exception policy by Id. Retrieves an existing exception policy by Id.</td>
</tr>
<tr>
    <td><a href="#list_exception_policies"><CopyableCode code="list_exception_policies" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Retrieves existing exception policies. Retrieves existing exception policies.</td>
</tr>
<tr>
    <td><a href="#delete_exception_policy"><CopyableCode code="delete_exception_policy" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-exception_policy_id"><code>exception_policy_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a exception policy by Id. Deletes a exception policy by Id.</td>
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
<tr id="parameter-exception_policy_id">
    <td><CopyableCode code="exception_policy_id" /></td>
    <td><code>string</code></td>
    <td>Id of an exception policy. Required.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_exception_policy"
    values={[
        { label: 'get_exception_policy', value: 'get_exception_policy' },
        { label: 'list_exception_policies', value: 'list_exception_policies' }
    ]}
>
<TabItem value="get_exception_policy">

Retrieves an existing exception policy by Id. Retrieves an existing exception policy by Id.

```sql
SELECT
id,
name,
etag,
exceptionRules
FROM azure.communication_job_router.exception_policies
WHERE exception_policy_id = '{{ exception_policy_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_exception_policies">

Retrieves existing exception policies. Retrieves existing exception policies.

```sql
SELECT
id,
name,
etag,
exceptionRules
FROM azure.communication_job_router.exception_policies
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_exception_policy"
    values={[
        { label: 'delete_exception_policy', value: 'delete_exception_policy' }
    ]}
>
<TabItem value="delete_exception_policy">

Deletes a exception policy by Id. Deletes a exception policy by Id.

```sql
DELETE FROM azure.communication_job_router.exception_policies
WHERE exception_policy_id = '{{ exception_policy_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
