--- 
title: check_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - check_revisions
  - appconfiguration_dataplane
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

Creates, updates, deletes, gets or lists a <code>check_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="check_revisions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appconfiguration_dataplane.check_revisions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#check_revisions"><CopyableCode code="check_revisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-key"><code>key</code></a>, <a href="#parameter-label"><code>label</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a>, <a href="#parameter-After"><code>After</code></a>, <a href="#parameter-Accept-Datetime"><code>Accept-Datetime</code></a>, <a href="#parameter-$Select"><code>$Select</code></a></td>
    <td>Requests the headers and status of the given resource. Requests the headers and status of the given resource.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-$Select">
    <td><CopyableCode code="$Select" /></td>
    <td><code>array</code></td>
    <td>Used to select what fields are present in the returned resource(s). Default value is None.</td>
</tr>
<tr id="parameter-Accept-Datetime">
    <td><CopyableCode code="Accept-Datetime" /></td>
    <td><code>string</code></td>
    <td>Requests the server to respond with the state of the resource at the specified time. Default value is None.</td>
</tr>
<tr id="parameter-After">
    <td><CopyableCode code="After" /></td>
    <td><code>string</code></td>
    <td>Instructs the server to return elements that appear after the element referred to by the specified token. Default value is None.</td>
</tr>
<tr id="parameter-Sync-Token">
    <td><CopyableCode code="Sync-Token" /></td>
    <td><code>string</code></td>
    <td>Used to guarantee real-time consistency between requests. Default value is None.</td>
</tr>
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>A filter used to match keys. Syntax reference: `https://aka.ms/azconfig/docs/restapirevisions `_. Default value is None.</td>
</tr>
<tr id="parameter-label">
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>A filter used to match labels. Syntax reference: `https://aka.ms/azconfig/docs/restapirevisions `_. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="check_revisions"
    values={[
        { label: 'check_revisions', value: 'check_revisions' }
    ]}
>
<TabItem value="check_revisions">

Requests the headers and status of the given resource. Requests the headers and status of the given resource.

```sql
EXEC azure.appconfiguration_dataplane.check_revisions.check_revisions 
@endpoint='{{ endpoint }}' --required, 
@key='{{ key }}', 
@label='{{ label }}', 
@Sync-Token='{{ Sync-Token }}', 
@After='{{ After }}', 
@Accept-Datetime='{{ Accept-Datetime }}', 
@$Select='{{ $Select }}'
;
```
</TabItem>
</Tabs>
