--- 
title: access_review_history_definition_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definition_instances
  - authorization
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

Creates, updates, deletes, gets or lists an <code>access_review_history_definition_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_review_history_definition_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_history_definition_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>The access review history definition instance id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The access review history definition instance unique id.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the parent history definition.</td>
</tr>
<tr>
    <td><CopyableCode code="downloadUri" /></td>
    <td><code>string</code></td>
    <td>Uri which can be used to retrieve review history data. To generate this Uri, generateDownloadUri() must be called for a specific accessReviewHistoryDefinitionInstance. The link expires after a 24 hour period. Callers can see the expiration date time by looking at the 'se' parameter in the generated uri.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time when history data report expires and the associated data is deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="fulfilledDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time when the history data report is scheduled to be generated.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time used when selecting review data, all reviews included in data end on or before this date. For use only with one-time/non-recurring reports.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time used when selecting review data, all reviews included in data start on or after this date. For use only with one-time/non-recurring reports.</td>
</tr>
<tr>
    <td><CopyableCode code="runDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time when the history data report is scheduled to be generated.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the requested review history instance data. This is either requested, in-progress, done or error. The state transitions are as follows - Requested -&gt; InProgress -&gt; Done -&gt; Expired. Known values are: "Requested", "InProgress", "Done", and "Error". (Requested, InProgress, Done, Error)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-history_definition_id"><code>history_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get access review history definition instances by definition Id.</td>
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
<tr id="parameter-history_definition_id">
    <td><CopyableCode code="history_definition_id" /></td>
    <td><code>string</code></td>
    <td>The id of the access review history definition. Required.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get access review history definition instances by definition Id.

```sql
SELECT
id,
name,
displayName,
downloadUri,
expiration,
fulfilledDateTime,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
runDateTime,
status,
type
FROM azure.authorization.access_review_history_definition_instances
WHERE history_definition_id = '{{ history_definition_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
