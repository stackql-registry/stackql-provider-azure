--- 
title: protected_items_operation_group
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_items_operation_group
  - commvault_content_store
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

Creates, updates, deletes, gets or lists a <code>protected_items_operation_group</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="protected_items_operation_group" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.commvault_content_store.protected_items_operation_group" /></td></tr>
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
    <td><a href="#count_by_protection_groups"><CopyableCode code="count_by_protection_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resourceIds"><code>resourceIds</code></a></td>
    <td></td>
    <td>Gets the count of protected items for provided CCA resource IDs across subscriptions.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="count_by_protection_groups"
    values={[
        { label: 'count_by_protection_groups', value: 'count_by_protection_groups' }
    ]}
>
<TabItem value="count_by_protection_groups">

Gets the count of protected items for provided CCA resource IDs across subscriptions.

```sql
EXEC azure_isv.commvault_content_store.protected_items_operation_group.count_by_protection_groups 
@@json=
'{
"resourceIds": "{{ resourceIds }}"
}'
;
```
</TabItem>
</Tabs>
