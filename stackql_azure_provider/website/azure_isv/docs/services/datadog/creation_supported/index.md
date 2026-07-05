--- 
title: creation_supported
hide_title: false
hide_table_of_contents: false
keywords:
  - creation_supported
  - datadog
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>creation_supported</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="creation_supported" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.creation_supported" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The ARM id of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="creationSupported" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if selected subscription supports Datadog resource creation, if not it is already being monitored for the selected organization via multi subscription feature.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-datadogOrganizationId"><code>datadogOrganizationId</code></a></td>
    <td></td>
    <td>Informs if the current subscription is being already monitored for selected Datadog organization. Informs if the current subscription is being already monitored for selected Datadog organization.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-datadogOrganizationId"><code>datadogOrganizationId</code></a></td>
    <td></td>
    <td>Informs if the current subscription is being already monitored for selected Datadog organization. Informs if the current subscription is being already monitored for selected Datadog organization.</td>
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
<tr id="parameter-datadogOrganizationId">
    <td><CopyableCode code="datadogOrganizationId" /></td>
    <td><code>string</code></td>
    <td>Datadog Organization Id. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Informs if the current subscription is being already monitored for selected Datadog organization. Informs if the current subscription is being already monitored for selected Datadog organization.

```sql
SELECT
name,
creationSupported
FROM azure_isv.datadog.creation_supported
WHERE subscription_id = '{{ subscription_id }}' -- required
AND datadogOrganizationId = '{{ datadogOrganizationId }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

Informs if the current subscription is being already monitored for selected Datadog organization. Informs if the current subscription is being already monitored for selected Datadog organization.

```sql
EXEC azure_isv.datadog.creation_supported.list_raw 
@subscription_id='{{ subscription_id }}' --required, 
@datadogOrganizationId='{{ datadogOrganizationId }}' --required
;
```
</TabItem>
</Tabs>
