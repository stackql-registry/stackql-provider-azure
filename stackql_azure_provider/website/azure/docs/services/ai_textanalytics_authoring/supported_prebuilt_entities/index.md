--- 
title: supported_prebuilt_entities
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_prebuilt_entities
  - ai_textanalytics_authoring
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

Creates, updates, deletes, gets or lists a <code>supported_prebuilt_entities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="supported_prebuilt_entities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_textanalytics_authoring.supported_prebuilt_entities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_supported_prebuilt_entities"
    values={[
        { label: 'list_supported_prebuilt_entities', value: 'list_supported_prebuilt_entities' }
    ]}
>
<TabItem value="list_supported_prebuilt_entities">

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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The prebuilt entity category. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="examples" /></td>
    <td><code>string</code></td>
    <td>English examples for the entity. Required.</td>
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
    <td><a href="#list_supported_prebuilt_entities"><CopyableCode code="list_supported_prebuilt_entities" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists the supported prebuilt entities that can be used while creating composed entities.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_supported_prebuilt_entities"
    values={[
        { label: 'list_supported_prebuilt_entities', value: 'list_supported_prebuilt_entities' }
    ]}
>
<TabItem value="list_supported_prebuilt_entities">

Lists the supported prebuilt entities that can be used while creating composed entities.

```sql
SELECT
category,
description,
examples
FROM azure.ai_textanalytics_authoring.supported_prebuilt_entities
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
