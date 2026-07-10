--- 
title: upsert_distribution_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - upsert_distribution_policies
  - communication_jobrouter
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

Creates, updates, deletes, gets or lists a <code>upsert_distribution_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="upsert_distribution_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_jobrouter.upsert_distribution_policies" /></td></tr>
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
    <td><a href="#upsert_distribution_policy"><CopyableCode code="upsert_distribution_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-distribution_policy_id"><code>distribution_policy_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a></td>
    <td>Creates or updates a distribution policy. Creates or updates a distribution policy.</td>
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
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td>The request should only proceed if the entity was not modified after this time. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="upsert_distribution_policy"
    values={[
        { label: 'upsert_distribution_policy', value: 'upsert_distribution_policy' }
    ]}
>
<TabItem value="upsert_distribution_policy">

Creates or updates a distribution policy. Creates or updates a distribution policy.

```sql
EXEC azure.communication_jobrouter.upsert_distribution_policies.upsert_distribution_policy 
@distribution_policy_id='{{ distribution_policy_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@If-Unmodified-Since='{{ If-Unmodified-Since }}' 
@@json=
'{
"name": "{{ name }}", 
"offerExpiresAfterSeconds": {{ offerExpiresAfterSeconds }}, 
"mode": "{{ mode }}"
}'
;
```
</TabItem>
</Tabs>
