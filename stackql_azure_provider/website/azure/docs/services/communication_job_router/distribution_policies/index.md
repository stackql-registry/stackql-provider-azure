--- 
title: distribution_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - distribution_policies
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

Creates, updates, deletes, gets or lists a <code>distribution_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="distribution_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_job_router.distribution_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_distribution_policy"
    values={[
        { label: 'get_distribution_policy', value: 'get_distribution_policy' },
        { label: 'list_distribution_policies', value: 'list_distribution_policies' }
    ]}
>
<TabItem value="get_distribution_policy">

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
    <td>Id of a distribution policy. Required.</td>
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
    <td><CopyableCode code="mode" /></td>
    <td><code>object</code></td>
    <td>Mode governing the specific distribution method.</td>
</tr>
<tr>
    <td><CopyableCode code="offerExpiresAfterSeconds" /></td>
    <td><code>number</code></td>
    <td>Number of seconds after which any offers created under this policy will be expired.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_distribution_policies">

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
    <td>Id of a distribution policy. Required.</td>
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
    <td><CopyableCode code="mode" /></td>
    <td><code>object</code></td>
    <td>Mode governing the specific distribution method.</td>
</tr>
<tr>
    <td><CopyableCode code="offerExpiresAfterSeconds" /></td>
    <td><code>number</code></td>
    <td>Number of seconds after which any offers created under this policy will be expired.</td>
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
    <td><a href="#get_distribution_policy"><CopyableCode code="get_distribution_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-distribution_policy_id"><code>distribution_policy_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves an existing distribution policy by Id. Retrieves an existing distribution policy by Id.</td>
</tr>
<tr>
    <td><a href="#list_distribution_policies"><CopyableCode code="list_distribution_policies" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Retrieves existing distribution policies. Retrieves existing distribution policies.</td>
</tr>
<tr>
    <td><a href="#delete_distribution_policy"><CopyableCode code="delete_distribution_policy" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-distribution_policy_id"><code>distribution_policy_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a distribution policy by Id. Delete a distribution policy by Id.</td>
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
<tr id="parameter-distribution_policy_id">
    <td><CopyableCode code="distribution_policy_id" /></td>
    <td><code>string</code></td>
    <td>Id of a distribution policy. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
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
    defaultValue="get_distribution_policy"
    values={[
        { label: 'get_distribution_policy', value: 'get_distribution_policy' },
        { label: 'list_distribution_policies', value: 'list_distribution_policies' }
    ]}
>
<TabItem value="get_distribution_policy">

Retrieves an existing distribution policy by Id. Retrieves an existing distribution policy by Id.

```sql
SELECT
id,
name,
etag,
mode,
offerExpiresAfterSeconds
FROM azure.communication_job_router.distribution_policies
WHERE distribution_policy_id = '{{ distribution_policy_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_distribution_policies">

Retrieves existing distribution policies. Retrieves existing distribution policies.

```sql
SELECT
id,
name,
etag,
mode,
offerExpiresAfterSeconds
FROM azure.communication_job_router.distribution_policies
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_distribution_policy"
    values={[
        { label: 'delete_distribution_policy', value: 'delete_distribution_policy' }
    ]}
>
<TabItem value="delete_distribution_policy">

Delete a distribution policy by Id. Delete a distribution policy by Id.

```sql
DELETE FROM azure.communication_job_router.distribution_policies
WHERE distribution_policy_id = '{{ distribution_policy_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
