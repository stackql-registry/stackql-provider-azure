--- 
title: copy_classifier_tos
hide_title: false
hide_table_of_contents: false
keywords:
  - copy_classifier_tos
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

Creates, updates, deletes, gets or lists a <code>copy_classifier_tos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="copy_classifier_tos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_document_intelligence.copy_classifier_tos" /></td></tr>
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
    <td><a href="#copy_classifier_to"><CopyableCode code="copy_classifier_to" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-classifier_id"><code>classifier_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-targetResourceRegion"><code>targetResourceRegion</code></a>, <a href="#parameter-targetClassifierId"><code>targetClassifierId</code></a>, <a href="#parameter-targetClassifierLocation"><code>targetClassifierLocation</code></a>, <a href="#parameter-accessToken"><code>accessToken</code></a>, <a href="#parameter-expirationDateTime"><code>expirationDateTime</code></a></td>
    <td></td>
    <td>Copies document classifier to the target resource, region, and classifierId.</td>
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
<tr id="parameter-classifier_id">
    <td><CopyableCode code="classifier_id" /></td>
    <td><code>string</code></td>
    <td>Unique document classifier name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="copy_classifier_to"
    values={[
        { label: 'copy_classifier_to', value: 'copy_classifier_to' }
    ]}
>
<TabItem value="copy_classifier_to">

Copies document classifier to the target resource, region, and classifierId.

```sql
EXEC azure.ai_document_intelligence.copy_classifier_tos.copy_classifier_to 
@classifier_id='{{ classifier_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}", 
"targetResourceRegion": "{{ targetResourceRegion }}", 
"targetClassifierId": "{{ targetClassifierId }}", 
"targetClassifierLocation": "{{ targetClassifierLocation }}", 
"accessToken": "{{ accessToken }}", 
"expirationDateTime": "{{ expirationDateTime }}"
}'
;
```
</TabItem>
</Tabs>
