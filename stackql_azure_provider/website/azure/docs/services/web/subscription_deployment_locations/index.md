--- 
title: subscription_deployment_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_deployment_locations
  - web
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

Creates, updates, deletes, gets or lists a <code>subscription_deployment_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscription_deployment_locations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.subscription_deployment_locations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_subscription_deployment_locations"
    values={[
        { label: 'get_subscription_deployment_locations', value: 'get_subscription_deployment_locations' }
    ]}
>
<TabItem value="get_subscription_deployment_locations">

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
    <td><CopyableCode code="hostingEnvironmentDeploymentInfos" /></td>
    <td><code>array</code></td>
    <td>Available App Service Environments with basic information.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironments" /></td>
    <td><code>array</code></td>
    <td>Available App Service Environments with full descriptions of the environments.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>Available regions.</td>
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
    <td><a href="#get_subscription_deployment_locations"><CopyableCode code="get_subscription_deployment_locations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets list of available geo regions plus ministamps. Description for Gets list of available geo regions plus ministamps.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_subscription_deployment_locations"
    values={[
        { label: 'get_subscription_deployment_locations', value: 'get_subscription_deployment_locations' }
    ]}
>
<TabItem value="get_subscription_deployment_locations">

Gets list of available geo regions plus ministamps. Description for Gets list of available geo regions plus ministamps.

```sql
SELECT
hostingEnvironmentDeploymentInfos,
hostingEnvironments,
locations
FROM azure.web.subscription_deployment_locations
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
