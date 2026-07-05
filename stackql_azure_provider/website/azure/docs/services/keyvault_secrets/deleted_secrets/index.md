--- 
title: deleted_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_secrets
  - keyvault_secrets
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

Creates, updates, deletes, gets or lists a <code>deleted_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deleted_secrets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_secrets.deleted_secrets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_deleted_secret"
    values={[
        { label: 'get_deleted_secret', value: 'get_deleted_secret' },
        { label: 'get_deleted_secrets', value: 'get_deleted_secrets' }
    ]}
>
<TabItem value="get_deleted_secret">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The secret id.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The secret management attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type of the secret.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the secret was deleted, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="kid" /></td>
    <td><code>string</code></td>
    <td>If this is a secret backing a KV certificate, then this field specifies the corresponding key backing the KV certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="managed" /></td>
    <td><code>boolean</code></td>
    <td>True if the secret's lifetime is managed by key vault. If this is a secret backing a certificate, then managed will be true.</td>
</tr>
<tr>
    <td><CopyableCode code="previousVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the previous certificate, if applicable. Applies only to certificates created after June 1, 2025. Certificates created before this date are not retroactively updated.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryId" /></td>
    <td><code>string</code></td>
    <td>The url of the recovery object, used to identify and recover the deleted secret.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the secret is scheduled to be purged, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Application specific metadata in the form of key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>The secret value.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_deleted_secrets">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Secret identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The secret management attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>Type of the secret value such as a password.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the secret was deleted, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="managed" /></td>
    <td><code>boolean</code></td>
    <td>True if the secret's lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryId" /></td>
    <td><code>string</code></td>
    <td>The url of the recovery object, used to identify and recover the deleted secret.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the secret is scheduled to be purged, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Application specific metadata in the form of key-value pairs.</td>
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
    <td><a href="#get_deleted_secret"><CopyableCode code="get_deleted_secret" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-secret_name"><code>secret_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Gets the specified deleted secret. The Get Deleted Secret operation returns the specified deleted secret along with its attributes. This operation requires the secrets/get permission.</td>
</tr>
<tr>
    <td><a href="#get_deleted_secrets"><CopyableCode code="get_deleted_secrets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a></td>
    <td>Lists deleted secrets for the specified vault. The Get Deleted Secrets operation returns the secrets that have been deleted for a vault enabled for soft-delete. This operation requires the secrets/list permission.</td>
</tr>
<tr>
    <td><a href="#purge_deleted_secret"><CopyableCode code="purge_deleted_secret" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-secret_name"><code>secret_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Permanently deletes the specified secret. The purge deleted secret operation removes the secret permanently, without the possibility of recovery. This operation can only be enabled on a soft-delete enabled vault. This operation requires the secrets/purge permission.</td>
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
<tr id="parameter-secret_name">
    <td><CopyableCode code="secret_name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results to return in a page. If not specified the service will return up to 25 results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_deleted_secret"
    values={[
        { label: 'get_deleted_secret', value: 'get_deleted_secret' },
        { label: 'get_deleted_secrets', value: 'get_deleted_secrets' }
    ]}
>
<TabItem value="get_deleted_secret">

Gets the specified deleted secret. The Get Deleted Secret operation returns the specified deleted secret along with its attributes. This operation requires the secrets/get permission.

```sql
SELECT
id,
attributes,
contentType,
deletedDate,
kid,
managed,
previousVersion,
recoveryId,
scheduledPurgeDate,
tags,
value
FROM azure.keyvault_secrets.deleted_secrets
WHERE secret_name = '{{ secret_name }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
<TabItem value="get_deleted_secrets">

Lists deleted secrets for the specified vault. The Get Deleted Secrets operation returns the secrets that have been deleted for a vault enabled for soft-delete. This operation requires the secrets/list permission.

```sql
SELECT
id,
attributes,
contentType,
deletedDate,
managed,
recoveryId,
scheduledPurgeDate,
tags
FROM azure.keyvault_secrets.deleted_secrets
WHERE vault_base_url = '{{ vault_base_url }}' -- required
AND maxresults = '{{ maxresults }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="purge_deleted_secret"
    values={[
        { label: 'purge_deleted_secret', value: 'purge_deleted_secret' }
    ]}
>
<TabItem value="purge_deleted_secret">

Permanently deletes the specified secret. The purge deleted secret operation removes the secret permanently, without the possibility of recovery. This operation can only be enabled on a soft-delete enabled vault. This operation requires the secrets/purge permission.

```sql
DELETE FROM azure.keyvault_secrets.deleted_secrets
WHERE secret_name = '{{ secret_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>
