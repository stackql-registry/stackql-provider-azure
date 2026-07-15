--- 
title: all_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - all_environments
  - developer_devcenter
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

Creates, updates, deletes, gets or lists an <code>all_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="all_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.all_environments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_all_environments"
    values={[
        { label: 'list_all_environments', value: 'list_all_environments' }
    ]}
>
<TabItem value="list_all_environments">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Environment name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="catalogName" /></td>
    <td><code>string</code></td>
    <td>Name of the catalog. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Name of the environment definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentType" /></td>
    <td><code>string</code></td>
    <td>Environment type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Provisioning error details. Populated only for error states.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Parameters object for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the environment. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Accepted", "Deleting", "Updating", "Preparing", "Running", "Syncing", "MovingResources", "TransientFailure", and "StorageProvisioningFailed". (Succeeded, Failed, Canceled, Creating, Accepted, Deleting, Updating, Preparing, Running, Syncing, MovingResources, TransientFailure, StorageProvisioningFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the resource group containing the environment's resources.</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>string</code></td>
    <td>The AAD object id of the owner of this Environment.</td>
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
    <td><a href="#list_all_environments"><CopyableCode code="list_all_environments" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists the environments for a project.</td>
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
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The DevCenter Project upon which to execute operations. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_all_environments"
    values={[
        { label: 'list_all_environments', value: 'list_all_environments' }
    ]}
>
<TabItem value="list_all_environments">

Lists the environments for a project.

```sql
SELECT
name,
catalogName,
environmentDefinitionName,
environmentType,
error,
parameters,
provisioningState,
resourceGroupId,
user
FROM azure.developer_devcenter.all_environments
WHERE project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
