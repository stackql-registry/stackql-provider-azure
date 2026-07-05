--- 
title: redeem_invitation_codes
hide_title: false
hide_table_of_contents: false
keywords:
  - redeem_invitation_codes
  - education
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>redeem_invitation_codes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="redeem_invitation_codes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.education.redeem_invitation_codes" /></td></tr>
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
    <td><a href="#redeem_invitation_code"><CopyableCode code="redeem_invitation_code" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-redeemCode"><code>redeemCode</code></a>, <a href="#parameter-firstName"><code>firstName</code></a>, <a href="#parameter-lastName"><code>lastName</code></a></td>
    <td></td>
    <td>Redeem invite code to join a redeemable lab.</td>
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
    defaultValue="redeem_invitation_code"
    values={[
        { label: 'redeem_invitation_code', value: 'redeem_invitation_code' }
    ]}
>
<TabItem value="redeem_invitation_code">

Redeem invite code to join a redeemable lab.

```sql
EXEC azure_extras.education.redeem_invitation_codes.redeem_invitation_code 
@@json=
'{
"redeemCode": "{{ redeemCode }}", 
"firstName": "{{ firstName }}", 
"lastName": "{{ lastName }}"
}'
;
```
</TabItem>
</Tabs>
