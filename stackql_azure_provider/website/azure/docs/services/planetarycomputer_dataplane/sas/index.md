--- 
title: sas
hide_title: false
hide_table_of_contents: false
keywords:
  - sas
  - planetarycomputer_dataplane
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

Creates, updates, deletes, gets or lists a <code>sas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.planetarycomputer_dataplane.sas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_url"
    values={[
        { label: 'get_url', value: 'get_url' },
        { label: 'get_token', value: 'get_token' }
    ]}
>
<TabItem value="get_url">

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
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>Href. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="msft:expiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>Msft:Expiry.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_token">

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
    <td><CopyableCode code="msft:expiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>Msft:Expiry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
    <td>Token. Required.</td>
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
    <td><a href="#get_url"><CopyableCode code="get_url" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-href"><code>href</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-duration"><code>duration</code></a></td>
    <td>sign an HREF in the format of a URL and returns a SharedAccessSignatureSignedHrefResponse. Signs a HREF (a link URL) by appending a `SAS Token `_. If the HREF is not a Azure Blob Storage HREF, then pass back the HREF unsigned.</td>
</tr>
<tr>
    <td><a href="#get_token"><CopyableCode code="get_token" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-duration"><code>duration</code></a></td>
    <td>generate a SAS Token for the given Azure Blob storage account and container. Generate a `SAS Token `_ for the given storage account and container. The storage account and container must be associated with a Planetary Computer dataset indexed by the STAC API.</td>
</tr>
<tr>
    <td><a href="#revoke_token"><CopyableCode code="revoke_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-duration"><code>duration</code></a></td>
    <td>Revoke SAS token for the managed storage account of this GeoCatalog. Revoke a `SAS Token `_ for managed storage account of this GeoCatalog.</td>
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
<tr id="parameter-collection_id">
    <td><CopyableCode code="collection_id" /></td>
    <td><code>string</code></td>
    <td>Collection Id. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-href">
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>Href. Required.</td>
</tr>
<tr id="parameter-duration">
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td>Duration. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_url"
    values={[
        { label: 'get_url', value: 'get_url' },
        { label: 'get_token', value: 'get_token' }
    ]}
>
<TabItem value="get_url">

sign an HREF in the format of a URL and returns a SharedAccessSignatureSignedHrefResponse. Signs a HREF (a link URL) by appending a `SAS Token `_. If the HREF is not a Azure Blob Storage HREF, then pass back the HREF unsigned.

```sql
SELECT
href,
msft:expiry
FROM azure.planetarycomputer_dataplane.sas
WHERE href = '{{ href }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND duration = '{{ duration }}'
;
```
</TabItem>
<TabItem value="get_token">

generate a SAS Token for the given Azure Blob storage account and container. Generate a `SAS Token `_ for the given storage account and container. The storage account and container must be associated with a Planetary Computer dataset indexed by the STAC API.

```sql
SELECT
msft:expiry,
token
FROM azure.planetarycomputer_dataplane.sas
WHERE collection_id = '{{ collection_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND duration = '{{ duration }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revoke_token"
    values={[
        { label: 'revoke_token', value: 'revoke_token' }
    ]}
>
<TabItem value="revoke_token">

Revoke SAS token for the managed storage account of this GeoCatalog. Revoke a `SAS Token `_ for managed storage account of this GeoCatalog.

```sql
EXEC azure.planetarycomputer_dataplane.sas.revoke_token 
@endpoint='{{ endpoint }}' --required, 
@duration='{{ duration }}'
;
```
</TabItem>
</Tabs>
