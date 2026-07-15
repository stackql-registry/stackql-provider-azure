--- 
title: accept_job_offers
hide_title: false
hide_table_of_contents: false
keywords:
  - accept_job_offers
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

Creates, updates, deletes, gets or lists an <code>accept_job_offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accept_job_offers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_job_router.accept_job_offers" /></td></tr>
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
    <td><a href="#accept_job_offer"><CopyableCode code="accept_job_offer" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-worker_id"><code>worker_id</code></a>, <a href="#parameter-offer_id"><code>offer_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Accepts an offer to work on a job and returns a 409/Conflict if another agent accepted the job already. Accepts an offer to work on a job and returns a 409/Conflict if another agent accepted the job already.</td>
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
<tr id="parameter-offer_id">
    <td><CopyableCode code="offer_id" /></td>
    <td><code>string</code></td>
    <td>Id of an offer. Required.</td>
</tr>
<tr id="parameter-worker_id">
    <td><CopyableCode code="worker_id" /></td>
    <td><code>string</code></td>
    <td>Id of a worker. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="accept_job_offer"
    values={[
        { label: 'accept_job_offer', value: 'accept_job_offer' }
    ]}
>
<TabItem value="accept_job_offer">

Accepts an offer to work on a job and returns a 409/Conflict if another agent accepted the job already. Accepts an offer to work on a job and returns a 409/Conflict if another agent accepted the job already.

```sql
EXEC azure.communication_job_router.accept_job_offers.accept_job_offer 
@worker_id='{{ worker_id }}' --required, 
@offer_id='{{ offer_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
