--- 
title: integration_service_environment_managed_api_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_managed_api_operations
  - logic
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

Creates, updates, deletes, gets or lists an <code>integration_service_environment_managed_api_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_service_environment_managed_api_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.integration_service_environment_managed_api_operations" /></td></tr>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>object</code></td>
    <td>The annotation of api operation.</td>
</tr>
<tr>
    <td><CopyableCode code="api" /></td>
    <td><code>object</code></td>
    <td>The api reference.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the api operation.</td>
</tr>
<tr>
    <td><CopyableCode code="inputsDefinition" /></td>
    <td><code>object</code></td>
    <td>The operation inputs definition schema.</td>
</tr>
<tr>
    <td><CopyableCode code="isNotification" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the API operation is notification or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isWebhook" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the API operation is webhook or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="pageable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the api operation is pageable.</td>
</tr>
<tr>
    <td><CopyableCode code="responsesDefinition" /></td>
    <td><code>object</code></td>
    <td>The operation responses definition schemas.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>The summary of the api operation.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>string</code></td>
    <td>The trigger type of api operation.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerHint" /></td>
    <td><code>string</code></td>
    <td>The trigger hint for the api operation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="visibility" /></td>
    <td><code>string</code></td>
    <td>The visibility of the api operation.</td>
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
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-api_name"><code>api_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the managed Api operations.</td>
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
<tr id="parameter-api_name">
    <td><CopyableCode code="api_name" /></td>
    <td><code>string</code></td>
    <td>The api name. Required.</td>
</tr>
<tr id="parameter-integration_service_environment_name">
    <td><CopyableCode code="integration_service_environment_name" /></td>
    <td><code>string</code></td>
    <td>The integration service environment name. Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>The resource group. Required.</td>
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

Gets the managed Api operations.

```sql
SELECT
id,
name,
annotation,
api,
description,
inputsDefinition,
isNotification,
isWebhook,
location,
pageable,
responsesDefinition,
summary,
tags,
trigger,
triggerHint,
type,
visibility
FROM azure.logic.integration_service_environment_managed_api_operations
WHERE resource_group = '{{ resource_group }}' -- required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' -- required
AND api_name = '{{ api_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
