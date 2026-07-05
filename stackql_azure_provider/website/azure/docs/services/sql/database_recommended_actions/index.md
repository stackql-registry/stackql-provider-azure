--- 
title: database_recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_recommended_actions
  - sql
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

Creates, updates, deletes, gets or lists a <code>database_recommended_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database_recommended_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_recommended_actions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_database_advisor', value: 'list_by_database_advisor' }
    ]}
>
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
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Gets additional details specific to this recommended action.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Gets the error details if and why this recommended action is put to error state.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedImpact" /></td>
    <td><code>array</code></td>
    <td>Gets the estimated impact info for this recommended action e.g., Estimated CPU gain, Estimated Disk Space change.</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionDuration" /></td>
    <td><code>string</code></td>
    <td>Gets the time taken for applying this recommended action on user resource. e.g., time taken for index creation.</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionInitiatedBy" /></td>
    <td><code>string</code></td>
    <td>Gets if approval for applying this recommended action was given by user/system. Known values are: "User" and "System". (User, System)</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionInitiatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when this recommended action was approved for execution.</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when system started applying this recommended action on the user resource. e.g., index creation start time.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationDetails" /></td>
    <td><code>object</code></td>
    <td>Gets the implementation details of this recommended action for user to apply it manually.</td>
</tr>
<tr>
    <td><CopyableCode code="isArchivedAction" /></td>
    <td><code>boolean</code></td>
    <td>Gets if this recommended action was suggested some time ago but user chose to ignore this and system added a new recommended action again.</td>
</tr>
<tr>
    <td><CopyableCode code="isExecutableAction" /></td>
    <td><code>boolean</code></td>
    <td>Gets if this recommended action is actionable by user.</td>
</tr>
<tr>
    <td><CopyableCode code="isRevertableAction" /></td>
    <td><code>boolean</code></td>
    <td>Gets if changes applied by this recommended action can be reverted by user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Resource kind.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRefresh" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets time when this recommended action was last refreshed.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedObjects" /></td>
    <td><code>array</code></td>
    <td>Gets the linked objects, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="observedImpact" /></td>
    <td><code>array</code></td>
    <td>Gets the observed/actual impact info for this recommended action e.g., Actual CPU gain, Actual Disk Space change.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationReason" /></td>
    <td><code>string</code></td>
    <td>Gets the reason for recommending this action. e.g., DuplicateIndex.</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionDuration" /></td>
    <td><code>string</code></td>
    <td>Gets the time taken for reverting changes of this recommended action on user resource. e.g., time taken for dropping the created index.</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionInitiatedBy" /></td>
    <td><code>string</code></td>
    <td>Gets if approval for reverting this recommended action was given by user/system. Known values are: "User" and "System". (User, System)</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionInitiatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when this recommended action was approved for revert.</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when system started reverting changes of this recommended action on user resource. e.g., time when index drop is executed.</td>
</tr>
<tr>
    <td><CopyableCode code="score" /></td>
    <td><code>integer</code></td>
    <td>Gets the impact of this recommended action. Possible values are 1 - Low impact, 2 - Medium Impact and 3 - High Impact.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td>Gets the info of the current state the recommended action is in. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeSeries" /></td>
    <td><code>array</code></td>
    <td>Gets the time series info of metrics for this recommended action e.g., CPU consumption time series.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validSince" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time since when this recommended action is valid.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_database_advisor">

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
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Gets additional details specific to this recommended action.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Gets the error details if and why this recommended action is put to error state.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedImpact" /></td>
    <td><code>array</code></td>
    <td>Gets the estimated impact info for this recommended action e.g., Estimated CPU gain, Estimated Disk Space change.</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionDuration" /></td>
    <td><code>string</code></td>
    <td>Gets the time taken for applying this recommended action on user resource. e.g., time taken for index creation.</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionInitiatedBy" /></td>
    <td><code>string</code></td>
    <td>Gets if approval for applying this recommended action was given by user/system. Known values are: "User" and "System". (User, System)</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionInitiatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when this recommended action was approved for execution.</td>
</tr>
<tr>
    <td><CopyableCode code="executeActionStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when system started applying this recommended action on the user resource. e.g., index creation start time.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationDetails" /></td>
    <td><code>object</code></td>
    <td>Gets the implementation details of this recommended action for user to apply it manually.</td>
</tr>
<tr>
    <td><CopyableCode code="isArchivedAction" /></td>
    <td><code>boolean</code></td>
    <td>Gets if this recommended action was suggested some time ago but user chose to ignore this and system added a new recommended action again.</td>
</tr>
<tr>
    <td><CopyableCode code="isExecutableAction" /></td>
    <td><code>boolean</code></td>
    <td>Gets if this recommended action is actionable by user.</td>
</tr>
<tr>
    <td><CopyableCode code="isRevertableAction" /></td>
    <td><code>boolean</code></td>
    <td>Gets if changes applied by this recommended action can be reverted by user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Resource kind.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRefresh" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets time when this recommended action was last refreshed.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedObjects" /></td>
    <td><code>array</code></td>
    <td>Gets the linked objects, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="observedImpact" /></td>
    <td><code>array</code></td>
    <td>Gets the observed/actual impact info for this recommended action e.g., Actual CPU gain, Actual Disk Space change.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationReason" /></td>
    <td><code>string</code></td>
    <td>Gets the reason for recommending this action. e.g., DuplicateIndex.</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionDuration" /></td>
    <td><code>string</code></td>
    <td>Gets the time taken for reverting changes of this recommended action on user resource. e.g., time taken for dropping the created index.</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionInitiatedBy" /></td>
    <td><code>string</code></td>
    <td>Gets if approval for reverting this recommended action was given by user/system. Known values are: "User" and "System". (User, System)</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionInitiatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when this recommended action was approved for revert.</td>
</tr>
<tr>
    <td><CopyableCode code="revertActionStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when system started reverting changes of this recommended action on user resource. e.g., time when index drop is executed.</td>
</tr>
<tr>
    <td><CopyableCode code="score" /></td>
    <td><code>integer</code></td>
    <td>Gets the impact of this recommended action. Possible values are 1 - Low impact, 2 - Medium Impact and 3 - High Impact.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td>Gets the info of the current state the recommended action is in. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeSeries" /></td>
    <td><code>array</code></td>
    <td>Gets the time series info of metrics for this recommended action e.g., CPU consumption time series.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validSince" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time since when this recommended action is valid.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-advisor_name"><code>advisor_name</code></a>, <a href="#parameter-recommended_action_name"><code>recommended_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a database recommended action.</td>
</tr>
<tr>
    <td><a href="#list_by_database_advisor"><CopyableCode code="list_by_database_advisor" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-advisor_name"><code>advisor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets list of Database Recommended Actions.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-advisor_name"><code>advisor_name</code></a>, <a href="#parameter-recommended_action_name"><code>recommended_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a database recommended action.</td>
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
<tr id="parameter-advisor_name">
    <td><CopyableCode code="advisor_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Database Advisor. Required.</td>
</tr>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-recommended_action_name">
    <td><CopyableCode code="recommended_action_name" /></td>
    <td><code>string</code></td>
    <td>The name of Database Recommended Action. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_database_advisor', value: 'list_by_database_advisor' }
    ]}
>
<TabItem value="get">

Gets a database recommended action.

```sql
SELECT
id,
name,
details,
errorDetails,
estimatedImpact,
executeActionDuration,
executeActionInitiatedBy,
executeActionInitiatedTime,
executeActionStartTime,
implementationDetails,
isArchivedAction,
isExecutableAction,
isRevertableAction,
kind,
lastRefresh,
linkedObjects,
location,
observedImpact,
recommendationReason,
revertActionDuration,
revertActionInitiatedBy,
revertActionInitiatedTime,
revertActionStartTime,
score,
state,
systemData,
timeSeries,
type,
validSince
FROM azure.sql.database_recommended_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND advisor_name = '{{ advisor_name }}' -- required
AND recommended_action_name = '{{ recommended_action_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_database_advisor">

Gets list of Database Recommended Actions.

```sql
SELECT
id,
name,
details,
errorDetails,
estimatedImpact,
executeActionDuration,
executeActionInitiatedBy,
executeActionInitiatedTime,
executeActionStartTime,
implementationDetails,
isArchivedAction,
isExecutableAction,
isRevertableAction,
kind,
lastRefresh,
linkedObjects,
location,
observedImpact,
recommendationReason,
revertActionDuration,
revertActionInitiatedBy,
revertActionInitiatedTime,
revertActionStartTime,
score,
state,
systemData,
timeSeries,
type,
validSince
FROM azure.sql.database_recommended_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND advisor_name = '{{ advisor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
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

Updates a database recommended action.

```sql
UPDATE azure.sql.database_recommended_actions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND advisor_name = '{{ advisor_name }}' --required
AND recommended_action_name = '{{ recommended_action_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
location,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
