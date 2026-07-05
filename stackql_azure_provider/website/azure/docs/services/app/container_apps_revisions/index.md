--- 
title: container_apps_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_revisions
  - app
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

Creates, updates, deletes, gets or lists a <code>container_apps_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps_revisions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app.container_apps_revisions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_revisions"
    values={[
        { label: 'list_revisions', value: 'list_revisions' }
    ]}
>
<TabItem value="list_revisions">

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
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>Link to next page of resources.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>Required. Collection of resources.</td>
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
    <td><a href="#list_revisions"><CopyableCode code="list_revisions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get the Revisions for a given Container App. Get the Revisions for a given Container App.</td>
</tr>
<tr>
    <td><a href="#get_revision"><CopyableCode code="get_revision" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Get a revision of a Container App. Get a revision of a Container App.</td>
</tr>
<tr>
    <td><a href="#activate_revision"><CopyableCode code="activate_revision" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Activates a revision for a Container App. Activates a revision for a Container App.</td>
</tr>
<tr>
    <td><a href="#deactivate_revision"><CopyableCode code="deactivate_revision" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Deactivates a revision for a Container App. Deactivates a revision for a Container App.</td>
</tr>
<tr>
    <td><a href="#restart_revision"><CopyableCode code="restart_revision" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Restarts a revision for a Container App. Restarts a revision for a Container App.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_revisions"
    values={[
        { label: 'list_revisions', value: 'list_revisions' }
    ]}
>
<TabItem value="list_revisions">

Get the Revisions for a given Container App. Get the Revisions for a given Container App.

```sql
SELECT
nextLink,
value
FROM azure.app.container_apps_revisions
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_revision"
    values={[
        { label: 'get_revision', value: 'get_revision' },
        { label: 'activate_revision', value: 'activate_revision' },
        { label: 'deactivate_revision', value: 'deactivate_revision' },
        { label: 'restart_revision', value: 'restart_revision' }
    ]}
>
<TabItem value="get_revision">

Get a revision of a Container App. Get a revision of a Container App.

```sql
EXEC azure.app.container_apps_revisions.get_revision 

;
```
</TabItem>
<TabItem value="activate_revision">

Activates a revision for a Container App. Activates a revision for a Container App.

```sql
EXEC azure.app.container_apps_revisions.activate_revision 

;
```
</TabItem>
<TabItem value="deactivate_revision">

Deactivates a revision for a Container App. Deactivates a revision for a Container App.

```sql
EXEC azure.app.container_apps_revisions.deactivate_revision 

;
```
</TabItem>
<TabItem value="restart_revision">

Restarts a revision for a Container App. Restarts a revision for a Container App.

```sql
EXEC azure.app.container_apps_revisions.restart_revision 

;
```
</TabItem>
</Tabs>
