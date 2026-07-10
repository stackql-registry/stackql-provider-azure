--- 
title: issue
hide_title: false
hide_table_of_contents: false
keywords:
  - issue
  - monitorworkspaces
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

Creates, updates, deletes, gets or lists an <code>issue</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="issue" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitorworkspaces.issue" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="fetch_investigation_result"
    values={[
        { label: 'fetch_investigation_result', value: 'fetch_investigation_result' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="fetch_investigation_result">

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
    <td>The identifier of the investigation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the investigation (in UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last update time of the investigation (in UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>object</code></td>
    <td>The origin of the investigation.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>string</code></td>
    <td>The result of this investigation. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="background" /></td>
    <td><code>object</code></td>
    <td>The issue background information.</td>
</tr>
<tr>
    <td><CopyableCode code="impactTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The issue impact time (in UTC). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="investigations" /></td>
    <td><code>array</code></td>
    <td>The list of investigations in the issue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="investigationsCount" /></td>
    <td><code>integer</code></td>
    <td>The number of investigations in the issue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>object</code></td>
    <td>The issue notification settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The issue severity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The issue status. Required. Known values are: "New", "InProgress", "Mitigated", "Closed", and "Canceled". (New, InProgress, Mitigated, Closed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The issue title. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="background" /></td>
    <td><code>object</code></td>
    <td>The issue background information.</td>
</tr>
<tr>
    <td><CopyableCode code="impactTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The issue impact time (in UTC). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="investigations" /></td>
    <td><code>array</code></td>
    <td>The list of investigations in the issue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="investigationsCount" /></td>
    <td><code>integer</code></td>
    <td>The number of investigations in the issue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>object</code></td>
    <td>The issue notification settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The issue severity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The issue status. Required. Known values are: "New", "InProgress", "Mitigated", "Closed", and "Canceled". (New, InProgress, Mitigated, Closed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The issue title. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#fetch_investigation_result"><CopyableCode code="fetch_investigation_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetch investigation result.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get issue properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all issues under the parent.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-related"><code>related</code></a></td>
    <td>Create a new issue or updates an existing one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an issue.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an issue.</td>
</tr>
<tr>
    <td><a href="#list_alerts"><CopyableCode code="list_alerts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all alerts in the issue - this method uses pagination to return all alerts.</td>
</tr>
<tr>
    <td><a href="#list_resources"><CopyableCode code="list_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all resources in the issue - this method uses pagination to return all resources.</td>
</tr>
<tr>
    <td><a href="#add_investigation_result"><CopyableCode code="add_investigation_result" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-result"><code>result</code></a></td>
    <td></td>
    <td>Adds investigation result.</td>
</tr>
<tr>
    <td><a href="#add_or_update_alerts"><CopyableCode code="add_or_update_alerts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Add or update alerts associated with an issue.</td>
</tr>
<tr>
    <td><a href="#add_or_update_resources"><CopyableCode code="add_or_update_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Add or update resources associated with an issue.</td>
</tr>
<tr>
    <td><a href="#fetch_background_visualization"><CopyableCode code="fetch_background_visualization" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetch the background visualization of the issue.</td>
</tr>
<tr>
    <td><a href="#set_background_visualization"><CopyableCode code="set_background_visualization" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-issue_name"><code>issue_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-visualization"><code>visualization</code></a></td>
    <td></td>
    <td>Set the background visualization for the issue.</td>
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
<tr id="parameter-azure_monitor_workspace_name">
    <td><CopyableCode code="azure_monitor_workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure Monitor Workspace. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-issue_name">
    <td><CopyableCode code="issue_name" /></td>
    <td><code>string</code></td>
    <td>The name of the IssueResource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-related">
    <td><CopyableCode code="related" /></td>
    <td><code>string</code></td>
    <td>Related resource or alert that is to be added to the issue (default: empty - the issue will be created without any related resources or alerts). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="fetch_investigation_result"
    values={[
        { label: 'fetch_investigation_result', value: 'fetch_investigation_result' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="fetch_investigation_result">

Fetch investigation result.

```sql
SELECT
id,
createdAt,
lastModifiedAt,
origin,
result
FROM azure.monitorworkspaces.issue
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' -- required
AND issue_name = '{{ issue_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get issue properties.

```sql
SELECT
id,
name,
background,
impactTime,
investigations,
investigationsCount,
notifications,
provisioningState,
severity,
status,
systemData,
title,
type
FROM azure.monitorworkspaces.issue
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' -- required
AND issue_name = '{{ issue_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all issues under the parent.

```sql
SELECT
id,
name,
background,
impactTime,
investigations,
investigationsCount,
notifications,
provisioningState,
severity,
status,
systemData,
title,
type
FROM azure.monitorworkspaces.issue
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new issue or updates an existing one.

```sql
INSERT INTO azure.monitorworkspaces.issue (
properties,
resource_group_name,
azure_monitor_workspace_name,
issue_name,
subscription_id,
related
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ azure_monitor_workspace_name }}',
'{{ issue_name }}',
'{{ subscription_id }}',
'{{ related }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: issue
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the issue resource.
    - name: azure_monitor_workspace_name
      value: "{{ azure_monitor_workspace_name }}"
      description: Required parameter for the issue resource.
    - name: issue_name
      value: "{{ issue_name }}"
      description: Required parameter for the issue resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the issue resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        title: "{{ title }}"
        status: "{{ status }}"
        severity: "{{ severity }}"
        investigations:
          - id: "{{ id }}"
            createdAt: "{{ createdAt }}"
        impactTime: "{{ impactTime }}"
        investigationsCount: {{ investigationsCount }}
        background:
          type: "{{ type }}"
          text: "{{ text }}"
          details:
            - name: "{{ name }}"
              value: "{{ value }}"
        notifications:
          updateTypes:
            - updateType: "{{ updateType }}"
          actionGroupIds:
            - "{{ actionGroupIds }}"
          excludeDefaultActionGroups: {{ excludeDefaultActionGroups }}
        provisioningState: "{{ provisioningState }}"
    - name: related
      value: "{{ related }}"
      description: Related resource or alert that is to be added to the issue (default: empty - the issue will be created without any related resources or alerts). Default value is None.
      description: Related resource or alert that is to be added to the issue (default: empty - the issue will be created without any related resources or alerts). Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an issue.

```sql
UPDATE azure.monitorworkspaces.issue
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' --required
AND issue_name = '{{ issue_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete an issue.

```sql
DELETE FROM azure.monitorworkspaces.issue
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' --required
AND issue_name = '{{ issue_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_alerts"
    values={[
        { label: 'list_alerts', value: 'list_alerts' },
        { label: 'list_resources', value: 'list_resources' },
        { label: 'add_investigation_result', value: 'add_investigation_result' },
        { label: 'add_or_update_alerts', value: 'add_or_update_alerts' },
        { label: 'add_or_update_resources', value: 'add_or_update_resources' },
        { label: 'fetch_background_visualization', value: 'fetch_background_visualization' },
        { label: 'set_background_visualization', value: 'set_background_visualization' }
    ]}
>
<TabItem value="list_alerts">

List all alerts in the issue - this method uses pagination to return all alerts.

```sql
EXEC azure.monitorworkspaces.issue.list_alerts 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_monitor_workspace_name='{{ azure_monitor_workspace_name }}' --required, 
@issue_name='{{ issue_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filter": "{{ filter }}"
}'
;
```
</TabItem>
<TabItem value="list_resources">

List all resources in the issue - this method uses pagination to return all resources.

```sql
EXEC azure.monitorworkspaces.issue.list_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_monitor_workspace_name='{{ azure_monitor_workspace_name }}' --required, 
@issue_name='{{ issue_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filter": "{{ filter }}"
}'
;
```
</TabItem>
<TabItem value="add_investigation_result">

Adds investigation result.

```sql
EXEC azure.monitorworkspaces.issue.add_investigation_result 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_monitor_workspace_name='{{ azure_monitor_workspace_name }}' --required, 
@issue_name='{{ issue_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"origin": "{{ origin }}", 
"createdAt": "{{ createdAt }}", 
"lastModifiedAt": "{{ lastModifiedAt }}", 
"result": "{{ result }}"
}'
;
```
</TabItem>
<TabItem value="add_or_update_alerts">

Add or update alerts associated with an issue.

```sql
EXEC azure.monitorworkspaces.issue.add_or_update_alerts 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_monitor_workspace_name='{{ azure_monitor_workspace_name }}' --required, 
@issue_name='{{ issue_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="add_or_update_resources">

Add or update resources associated with an issue.

```sql
EXEC azure.monitorworkspaces.issue.add_or_update_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_monitor_workspace_name='{{ azure_monitor_workspace_name }}' --required, 
@issue_name='{{ issue_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="fetch_background_visualization">

Fetch the background visualization of the issue.

```sql
EXEC azure.monitorworkspaces.issue.fetch_background_visualization 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_monitor_workspace_name='{{ azure_monitor_workspace_name }}' --required, 
@issue_name='{{ issue_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_background_visualization">

Set the background visualization for the issue.

```sql
EXEC azure.monitorworkspaces.issue.set_background_visualization 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_monitor_workspace_name='{{ azure_monitor_workspace_name }}' --required, 
@issue_name='{{ issue_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"visualization": "{{ visualization }}"
}'
;
```
</TabItem>
</Tabs>
