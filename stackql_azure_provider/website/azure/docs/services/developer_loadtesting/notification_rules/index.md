--- 
title: notification_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rules
  - developer_loadtesting
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

Creates, updates, deletes, gets or lists a <code>notification_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="notification_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.notification_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_notification_rule"
    values={[
        { label: 'get_notification_rule', value: 'get_notification_rule' },
        { label: 'list_notification_rules', value: 'list_notification_rules' }
    ]}
>
<TabItem value="get_notification_rule">

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
    <td><CopyableCode code="actionGroupIds" /></td>
    <td><code>array</code></td>
    <td>The action groups to notify. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the notification rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="notificationRuleId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the notification rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the notification rule. Required. "Tests"</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_notification_rules">

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
    <td><CopyableCode code="actionGroupIds" /></td>
    <td><code>array</code></td>
    <td>The action groups to notify. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the notification rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="notificationRuleId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the notification rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the notification rule. Required. "Tests"</td>
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
    <td><a href="#get_notification_rule"><CopyableCode code="get_notification_rule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-notification_rule_id"><code>notification_rule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resource read operation template.</td>
</tr>
<tr>
    <td><a href="#list_notification_rules"><CopyableCode code="list_notification_rules" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-testIds"><code>testIds</code></a>, <a href="#parameter-scopes"><code>scopes</code></a>, <a href="#parameter-lastModifiedStartTime"><code>lastModifiedStartTime</code></a>, <a href="#parameter-lastModifiedEndTime"><code>lastModifiedEndTime</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Resource list operation template.</td>
</tr>
<tr>
    <td><a href="#create_or_update_notification_rule"><CopyableCode code="create_or_update_notification_rule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-notification_rule_id"><code>notification_rule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-actionGroupIds"><code>actionGroupIds</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Create or update operation template.</td>
</tr>
<tr>
    <td><a href="#create_or_update_notification_rule"><CopyableCode code="create_or_update_notification_rule" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-notification_rule_id"><code>notification_rule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-actionGroupIds"><code>actionGroupIds</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Create or update operation template.</td>
</tr>
<tr>
    <td><a href="#delete_notification_rule"><CopyableCode code="delete_notification_rule" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-notification_rule_id"><code>notification_rule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resource delete operation template.</td>
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
<tr id="parameter-notification_rule_id">
    <td><CopyableCode code="notification_rule_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the notification rule. Required.</td>
</tr>
<tr id="parameter-lastModifiedEndTime">
    <td><CopyableCode code="lastModifiedEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime(RFC 3339 literal format) of the last updated time range to filter notification rules. Default value is None.</td>
</tr>
<tr id="parameter-lastModifiedStartTime">
    <td><CopyableCode code="lastModifiedStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime(RFC 3339 literal format) of the last updated time range to filter notification rules. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-scopes">
    <td><CopyableCode code="scopes" /></td>
    <td><code>string</code></td>
    <td>Search based on notification rules for the provided scopes. Default value is None.</td>
</tr>
<tr id="parameter-testIds">
    <td><CopyableCode code="testIds" /></td>
    <td><code>string</code></td>
    <td>Search based on notification rules associated with the provided test ids. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_notification_rule"
    values={[
        { label: 'get_notification_rule', value: 'get_notification_rule' },
        { label: 'list_notification_rules', value: 'list_notification_rules' }
    ]}
>
<TabItem value="get_notification_rule">

Resource read operation template.

```sql
SELECT
actionGroupIds,
createdBy,
createdDateTime,
displayName,
lastModifiedBy,
lastModifiedDateTime,
notificationRuleId,
scope
FROM azure.developer_loadtesting.notification_rules
WHERE notification_rule_id = '{{ notification_rule_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_notification_rules">

Resource list operation template.

```sql
SELECT
actionGroupIds,
createdBy,
createdDateTime,
displayName,
lastModifiedBy,
lastModifiedDateTime,
notificationRuleId,
scope
FROM azure.developer_loadtesting.notification_rules
WHERE endpoint = '{{ endpoint }}' -- required
AND testIds = '{{ testIds }}'
AND scopes = '{{ scopes }}'
AND lastModifiedStartTime = '{{ lastModifiedStartTime }}'
AND lastModifiedEndTime = '{{ lastModifiedEndTime }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_notification_rule"
    values={[
        { label: 'create_or_update_notification_rule', value: 'create_or_update_notification_rule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_notification_rule">

Create or update operation template.

```sql
INSERT INTO azure.developer_loadtesting.notification_rules (
displayName,
actionGroupIds,
scope,
notification_rule_id,
endpoint
)
SELECT 
'{{ displayName }}' /* required */,
'{{ actionGroupIds }}' /* required */,
'{{ scope }}' /* required */,
'{{ notification_rule_id }}',
'{{ endpoint }}'
RETURNING
actionGroupIds,
createdBy,
createdDateTime,
displayName,
lastModifiedBy,
lastModifiedDateTime,
notificationRuleId,
scope
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: notification_rules
  props:
    - name: notification_rule_id
      value: "{{ notification_rule_id }}"
      description: Required parameter for the notification_rules resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the notification_rules resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The name of the notification rule. Required.
    - name: actionGroupIds
      value:
        - "{{ actionGroupIds }}"
      description: |
        The action groups to notify. Required.
    - name: scope
      value: "{{ scope }}"
      description: |
        The scope of the notification rule. Required. "Tests"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_notification_rule"
    values={[
        { label: 'create_or_update_notification_rule', value: 'create_or_update_notification_rule' }
    ]}
>
<TabItem value="create_or_update_notification_rule">

Create or update operation template.

```sql
REPLACE azure.developer_loadtesting.notification_rules
SET 
displayName = '{{ displayName }}',
actionGroupIds = '{{ actionGroupIds }}',
scope = '{{ scope }}'
WHERE 
notification_rule_id = '{{ notification_rule_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND displayName = '{{ displayName }}' --required
AND actionGroupIds = '{{ actionGroupIds }}' --required
AND scope = '{{ scope }}' --required
RETURNING
actionGroupIds,
createdBy,
createdDateTime,
displayName,
lastModifiedBy,
lastModifiedDateTime,
notificationRuleId,
scope;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_notification_rule"
    values={[
        { label: 'delete_notification_rule', value: 'delete_notification_rule' }
    ]}
>
<TabItem value="delete_notification_rule">

Resource delete operation template.

```sql
DELETE FROM azure.developer_loadtesting.notification_rules
WHERE notification_rule_id = '{{ notification_rule_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
