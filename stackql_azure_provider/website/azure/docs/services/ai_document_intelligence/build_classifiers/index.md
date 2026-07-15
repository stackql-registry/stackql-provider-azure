--- 
title: build_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - build_classifiers
  - ai_document_intelligence
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

Creates, updates, deletes, gets or lists a <code>build_classifiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="build_classifiers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_document_intelligence.build_classifiers" /></td></tr>
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
    <td><a href="#build_classifier"><CopyableCode code="build_classifier" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-classifierId"><code>classifierId</code></a>, <a href="#parameter-docTypes"><code>docTypes</code></a></td>
    <td></td>
    <td>Builds a custom document classifier.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="build_classifier"
    values={[
        { label: 'build_classifier', value: 'build_classifier' }
    ]}
>
<TabItem value="build_classifier">

Builds a custom document classifier.

```sql
EXEC azure.ai_document_intelligence.build_classifiers.build_classifier 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"classifierId": "{{ classifierId }}", 
"description": "{{ description }}", 
"baseClassifierId": "{{ baseClassifierId }}", 
"docTypes": "{{ docTypes }}", 
"allowOverwrite": {{ allowOverwrite }}
}'
;
```
</TabItem>
</Tabs>
