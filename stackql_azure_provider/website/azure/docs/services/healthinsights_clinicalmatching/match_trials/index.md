--- 
title: match_trials
hide_title: false
hide_table_of_contents: false
keywords:
  - match_trials
  - healthinsights_clinicalmatching
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

Creates, updates, deletes, gets or lists a <code>match_trials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="match_trials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.healthinsights_clinicalmatching.match_trials" /></td></tr>
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
    <td><a href="#match_trials"><CopyableCode code="match_trials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-patients"><code>patients</code></a></td>
    <td><a href="#parameter-Repeatability-Request-ID"><code>Repeatability-Request-ID</code></a>, <a href="#parameter-Repeatability-First-Sent"><code>Repeatability-First-Sent</code></a></td>
    <td>Create Trial Matcher job. Creates a Trial Matcher job with the given request body.</td>
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
<tr id="parameter-Repeatability-First-Sent">
    <td><CopyableCode code="Repeatability-First-Sent" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the date and time at which the request was first created. Default value is None.</td>
</tr>
<tr id="parameter-Repeatability-Request-ID">
    <td><CopyableCode code="Repeatability-Request-ID" /></td>
    <td><code>string</code></td>
    <td>An opaque, globally-unique, client-generated string identifier for the request. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="match_trials"
    values={[
        { label: 'match_trials', value: 'match_trials' }
    ]}
>
<TabItem value="match_trials">

Create Trial Matcher job. Creates a Trial Matcher job with the given request body.

```sql
EXEC azure.healthinsights_clinicalmatching.match_trials.match_trials 
@endpoint='{{ endpoint }}' --required, 
@Repeatability-Request-ID='{{ Repeatability-Request-ID }}', 
@Repeatability-First-Sent='{{ Repeatability-First-Sent }}' 
@@json=
'{
"patients": "{{ patients }}", 
"configuration": "{{ configuration }}"
}'
;
```
</TabItem>
</Tabs>
