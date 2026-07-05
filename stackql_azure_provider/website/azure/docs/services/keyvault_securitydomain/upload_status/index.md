--- 
title: upload_status
hide_title: false
hide_table_of_contents: false
keywords:
  - upload_status
  - keyvault_securitydomain
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

Creates, updates, deletes, gets or lists a <code>upload_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="upload_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_securitydomain.upload_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_upload_status"
    values={[
        { label: 'get_upload_status', value: 'get_upload_status' }
    ]}
>
<TabItem value="get_upload_status">

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
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. Known values are: "Success", "InProgress", and "Failed". (Success, InProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="status_details" /></td>
    <td><code>string</code></td>
    <td>Details of the operation status.</td>
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
    <td><a href="#get_upload_status"><CopyableCode code="get_upload_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Get Security Domain upload operation status.</td>
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
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_upload_status"
    values={[
        { label: 'get_upload_status', value: 'get_upload_status' }
    ]}
>
<TabItem value="get_upload_status">

Get Security Domain upload operation status.

```sql
SELECT
status,
status_details
FROM azure.keyvault_securitydomain.upload_status
WHERE vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>
