--- 
title: check_ekm_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - check_ekm_connections
  - key_vault_administration
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

Creates, updates, deletes, gets or lists a <code>check_ekm_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="check_ekm_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault_administration.check_ekm_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="check_ekm_connection"
    values={[
        { label: 'check_ekm_connection', value: 'check_ekm_connection' }
    ]}
>
<TabItem value="check_ekm_connection">

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
    <td><CopyableCode code="proxy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the proxy product and its version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="api_version" /></td>
    <td><code>string</code></td>
    <td>The highest version of proxy interface API supported by the EKM Proxy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ekm_product" /></td>
    <td><code>string</code></td>
    <td>The name of the EKM product and its version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ekm_vendor" /></td>
    <td><code>string</code></td>
    <td>The name of the EKM vendor. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="proxy_vendor" /></td>
    <td><code>string</code></td>
    <td>The name of the proxy vendor. Required.</td>
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
    <td><a href="#check_ekm_connection"><CopyableCode code="check_ekm_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Checks the connectivity and authentication with the EKM proxy. The External Key Manager (EKM) Check operation checks the connectivity and authentication with the EKM proxy. This operation requires ekm/read permission.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="check_ekm_connection"
    values={[
        { label: 'check_ekm_connection', value: 'check_ekm_connection' }
    ]}
>
<TabItem value="check_ekm_connection">

Checks the connectivity and authentication with the EKM proxy. The External Key Manager (EKM) Check operation checks the connectivity and authentication with the EKM proxy. This operation requires ekm/read permission.

```sql
SELECT
proxy_name,
api_version,
ekm_product,
ekm_vendor,
proxy_vendor
FROM azure.key_vault_administration.check_ekm_connections
WHERE vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>
