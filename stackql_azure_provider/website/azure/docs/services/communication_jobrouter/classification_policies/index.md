--- 
title: classification_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - classification_policies
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

Creates, updates, deletes, gets or lists a <code>classification_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="classification_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_jobrouter.classification_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_classification_policy"
    values={[
        { label: 'get_classification_policy', value: 'get_classification_policy' },
        { label: 'list_classification_policies', value: 'list_classification_policies' }
    ]}
>
<TabItem value="get_classification_policy">

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
    <td>Id of a classification policy. Required.</td>
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
    <td><CopyableCode code="fallbackQueueId" /></td>
    <td><code>string</code></td>
    <td>Id of a fallback queue to select if queue selector attachments doesn't find a match.</td>
</tr>
<tr>
    <td><CopyableCode code="prioritizationRule" /></td>
    <td><code>object</code></td>
    <td>A rule to determine a priority score for a job.</td>
</tr>
<tr>
    <td><CopyableCode code="queueSelectorAttachments" /></td>
    <td><code>array</code></td>
    <td>Queue selector attachments used to resolve a queue for a job.</td>
</tr>
<tr>
    <td><CopyableCode code="workerSelectorAttachments" /></td>
    <td><code>array</code></td>
    <td>Worker selector attachments used to attach worker selectors to a job.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_classification_policies">

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
    <td>Id of a classification policy. Required.</td>
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
    <td><CopyableCode code="fallbackQueueId" /></td>
    <td><code>string</code></td>
    <td>Id of a fallback queue to select if queue selector attachments doesn't find a match.</td>
</tr>
<tr>
    <td><CopyableCode code="prioritizationRule" /></td>
    <td><code>object</code></td>
    <td>A rule to determine a priority score for a job.</td>
</tr>
<tr>
    <td><CopyableCode code="queueSelectorAttachments" /></td>
    <td><code>array</code></td>
    <td>Queue selector attachments used to resolve a queue for a job.</td>
</tr>
<tr>
    <td><CopyableCode code="workerSelectorAttachments" /></td>
    <td><code>array</code></td>
    <td>Worker selector attachments used to attach worker selectors to a job.</td>
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
    <td><a href="#get_classification_policy"><CopyableCode code="get_classification_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-classification_policy_id"><code>classification_policy_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves an existing classification policy by Id. Retrieves an existing classification policy by Id.</td>
</tr>
<tr>
    <td><a href="#list_classification_policies"><CopyableCode code="list_classification_policies" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Retrieves existing classification policies. Retrieves existing classification policies.</td>
</tr>
<tr>
    <td><a href="#delete_classification_policy"><CopyableCode code="delete_classification_policy" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-classification_policy_id"><code>classification_policy_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a classification policy by Id. Delete a classification policy by Id.</td>
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
<tr id="parameter-classification_policy_id">
    <td><CopyableCode code="classification_policy_id" /></td>
    <td><code>string</code></td>
    <td>Id of a classification policy. Required.</td>
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
    defaultValue="get_classification_policy"
    values={[
        { label: 'get_classification_policy', value: 'get_classification_policy' },
        { label: 'list_classification_policies', value: 'list_classification_policies' }
    ]}
>
<TabItem value="get_classification_policy">

Retrieves an existing classification policy by Id. Retrieves an existing classification policy by Id.

```sql
SELECT
id,
name,
etag,
fallbackQueueId,
prioritizationRule,
queueSelectorAttachments,
workerSelectorAttachments
FROM azure.communication_jobrouter.classification_policies
WHERE classification_policy_id = '{{ classification_policy_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_classification_policies">

Retrieves existing classification policies. Retrieves existing classification policies.

```sql
SELECT
id,
name,
etag,
fallbackQueueId,
prioritizationRule,
queueSelectorAttachments,
workerSelectorAttachments
FROM azure.communication_jobrouter.classification_policies
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_classification_policy"
    values={[
        { label: 'delete_classification_policy', value: 'delete_classification_policy' }
    ]}
>
<TabItem value="delete_classification_policy">

Delete a classification policy by Id. Delete a classification policy by Id.

```sql
DELETE FROM azure.communication_jobrouter.classification_policies
WHERE classification_policy_id = '{{ classification_policy_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
