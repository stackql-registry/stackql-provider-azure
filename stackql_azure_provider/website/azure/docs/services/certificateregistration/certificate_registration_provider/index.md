--- 
title: certificate_registration_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_registration_provider
  - certificateregistration
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

Creates, updates, deletes, gets or lists a <code>certificate_registration_provider</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_registration_provider" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.certificateregistration.certificate_registration_provider" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_operations"
    values={[
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="list_operations">

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
    <td>:vartype name: str</td>
</tr>
<tr>
    <td><CopyableCode code="display" /></td>
    <td><code>object</code></td>
    <td>Meta data about operation used for display in portal.</td>
</tr>
<tr>
    <td><CopyableCode code="isDataAction" /></td>
    <td><code>boolean</code></td>
    <td>:vartype is_data_action: bool</td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td>:vartype origin: str</td>
</tr>
<tr>
    <td><CopyableCode code="serviceSpecification" /></td>
    <td><code>object</code></td>
    <td>Resource metrics service provided by Microsoft.Insights resource provider.</td>
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
    <td><a href="#list_operations"><CopyableCode code="list_operations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider. Description for Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider.</td>
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
    defaultValue="list_operations"
    values={[
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="list_operations">

Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider. Description for Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider.

```sql
SELECT
name,
display,
isDataAction,
origin,
serviceSpecification
FROM azure.certificateregistration.certificate_registration_provider
;
```
</TabItem>
</Tabs>
