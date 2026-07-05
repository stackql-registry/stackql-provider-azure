--- 
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
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

Creates, updates, deletes, gets or lists a <code>source_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="source_controls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.source_controls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_source_control"
    values={[
        { label: 'get_source_control', value: 'get_source_control' },
        { label: 'list_source_controls', value: 'list_source_controls' }
    ]}
>
<TabItem value="get_source_control">

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
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>OAuth token expiration.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="refreshToken" /></td>
    <td><code>string</code></td>
    <td>OAuth refresh token.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
    <td>OAuth access token.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenSecret" /></td>
    <td><code>string</code></td>
    <td>OAuth access token secret.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_source_controls">

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
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>OAuth token expiration.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="refreshToken" /></td>
    <td><code>string</code></td>
    <td>OAuth refresh token.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
    <td>OAuth access token.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenSecret" /></td>
    <td><code>string</code></td>
    <td>OAuth access token secret.</td>
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
    <td><a href="#get_source_control"><CopyableCode code="get_source_control" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-source_control_type"><code>source_control_type</code></a></td>
    <td></td>
    <td>Gets source control token. Description for Gets source control token.</td>
</tr>
<tr>
    <td><a href="#list_source_controls"><CopyableCode code="list_source_controls" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets the source controls available for Azure websites. Description for Gets the source controls available for Azure websites.</td>
</tr>
<tr>
    <td><a href="#update_source_control"><CopyableCode code="update_source_control" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-source_control_type"><code>source_control_type</code></a></td>
    <td></td>
    <td>Updates source control token. Description for Updates source control token.</td>
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
<tr id="parameter-source_control_type">
    <td><CopyableCode code="source_control_type" /></td>
    <td><code>string</code></td>
    <td>Type of source control. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_source_control"
    values={[
        { label: 'get_source_control', value: 'get_source_control' },
        { label: 'list_source_controls', value: 'list_source_controls' }
    ]}
>
<TabItem value="get_source_control">

Gets source control token. Description for Gets source control token.

```sql
SELECT
id,
name,
expirationTime,
kind,
refreshToken,
systemData,
token,
tokenSecret,
type
FROM azure.web.source_controls
WHERE source_control_type = '{{ source_control_type }}' -- required
;
```
</TabItem>
<TabItem value="list_source_controls">

Gets the source controls available for Azure websites. Description for Gets the source controls available for Azure websites.

```sql
SELECT
id,
name,
expirationTime,
kind,
refreshToken,
systemData,
token,
tokenSecret,
type
FROM azure.web.source_controls
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_source_control"
    values={[
        { label: 'update_source_control', value: 'update_source_control' }
    ]}
>
<TabItem value="update_source_control">

Updates source control token. Description for Updates source control token.

```sql
UPDATE azure.web.source_controls
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
source_control_type = '{{ source_control_type }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
