--- 
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secrets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_secrets.secrets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_secret"
    values={[
        { label: 'get_secret', value: 'get_secret' },
        { label: 'get_secrets', value: 'get_secrets' }
    ]}
>
<TabItem value="get_secret">

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
<TabItem value="get_secrets">

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
    <td><CopyableCode code="managed" /></td>
    <td><code>boolean</code></td>
    <td>True if the secret's lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true.</td>
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
    <td><a href="#get_secret"><CopyableCode code="get_secret" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-secret_name"><code>secret_name</code></a>, <a href="#parameter-secret_version"><code>secret_version</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td><a href="#parameter-outContentType"><code>outContentType</code></a></td>
    <td>Get a specified secret from a given key vault. The GET operation is applicable to any secret stored in Azure Key Vault. This operation requires the secrets/get permission.</td>
</tr>
<tr>
    <td><a href="#get_secrets"><CopyableCode code="get_secrets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a></td>
    <td>List secrets in a specified key vault. The Get Secrets operation is applicable to the entire vault. However, only the base secret identifier and its attributes are provided in the response. Individual secret versions are not listed in the response. This operation requires the secrets/list permission.</td>
</tr>
<tr>
    <td><a href="#update_secret"><CopyableCode code="update_secret" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-secret_name"><code>secret_name</code></a>, <a href="#parameter-secret_version"><code>secret_version</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Updates the attributes associated with a specified secret in a given key vault. The UPDATE operation changes specified attributes of an existing stored secret. Attributes that are not specified in the request are left unchanged. The value of a secret itself cannot be changed. This operation requires the secrets/set permission.</td>
</tr>
<tr>
    <td><a href="#set_secret"><CopyableCode code="set_secret" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-secret_name"><code>secret_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Sets a secret in a specified key vault. The SET operation adds a secret to the Azure Key Vault. If the named secret already exists, Azure Key Vault creates a new version of that secret. This operation requires the secrets/set permission.</td>
</tr>
<tr>
    <td><a href="#delete_secret"><CopyableCode code="delete_secret" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-secret_name"><code>secret_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Deletes a secret from a specified key vault. The DELETE operation applies to any secret stored in Azure Key Vault. DELETE cannot be applied to an individual version of a secret. This operation requires the secrets/delete permission.</td>
</tr>
<tr>
    <td><a href="#backup_secret"><CopyableCode code="backup_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-secret_name"><code>secret_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Backs up the specified secret. Requests that a backup of the specified secret be downloaded to the client. All versions of the secret will be downloaded. This operation requires the secrets/backup permission.</td>
</tr>
<tr>
    <td><a href="#restore_secret"><CopyableCode code="restore_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Restores a backed up secret to a vault. Restores a backed up secret, and all its versions, to a vault. This operation requires the secrets/restore permission.</td>
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
<tr id="parameter-secret_version">
    <td><CopyableCode code="secret_version" /></td>
    <td><code>string</code></td>
    <td>The version of the secret. Required.</td>
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
<tr id="parameter-outContentType">
    <td><CopyableCode code="outContentType" /></td>
    <td><code>string</code></td>
    <td>The media type (MIME type) of the certificate. If a supported format is specified, the certificate content is converted to the requested format. Currently, only PFX to PEM conversion is supported. If an unsupported format is specified, the request is rejected. If not specified, the certificate is returned in its original format without conversion. Known values are: "application/x-pkcs12" and "application/x-pem-file". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_secret"
    values={[
        { label: 'get_secret', value: 'get_secret' },
        { label: 'get_secrets', value: 'get_secrets' }
    ]}
>
<TabItem value="get_secret">

Get a specified secret from a given key vault. The GET operation is applicable to any secret stored in Azure Key Vault. This operation requires the secrets/get permission.

```sql
SELECT
id,
attributes,
contentType,
kid,
managed,
previousVersion,
tags,
value
FROM azure.keyvault_secrets.secrets
WHERE secret_name = '{{ secret_name }}' -- required
AND secret_version = '{{ secret_version }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
AND outContentType = '{{ outContentType }}'
;
```
</TabItem>
<TabItem value="get_secrets">

List secrets in a specified key vault. The Get Secrets operation is applicable to the entire vault. However, only the base secret identifier and its attributes are provided in the response. Individual secret versions are not listed in the response. This operation requires the secrets/list permission.

```sql
SELECT
id,
attributes,
contentType,
managed,
tags
FROM azure.keyvault_secrets.secrets
WHERE vault_base_url = '{{ vault_base_url }}' -- required
AND maxresults = '{{ maxresults }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_secret"
    values={[
        { label: 'update_secret', value: 'update_secret' }
    ]}
>
<TabItem value="update_secret">

Updates the attributes associated with a specified secret in a given key vault. The UPDATE operation changes specified attributes of an existing stored secret. Attributes that are not specified in the request are left unchanged. The value of a secret itself cannot be changed. This operation requires the secrets/set permission.

```sql
UPDATE azure.keyvault_secrets.secrets
SET 
contentType = '{{ contentType }}',
attributes = '{{ attributes }}',
tags = '{{ tags }}'
WHERE 
secret_name = '{{ secret_name }}' --required
AND secret_version = '{{ secret_version }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
RETURNING
id,
attributes,
contentType,
kid,
managed,
previousVersion,
tags,
value;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_secret"
    values={[
        { label: 'set_secret', value: 'set_secret' }
    ]}
>
<TabItem value="set_secret">

Sets a secret in a specified key vault. The SET operation adds a secret to the Azure Key Vault. If the named secret already exists, Azure Key Vault creates a new version of that secret. This operation requires the secrets/set permission.

```sql
REPLACE azure.keyvault_secrets.secrets
SET 
value = '{{ value }}',
tags = '{{ tags }}',
contentType = '{{ contentType }}',
attributes = '{{ attributes }}'
WHERE 
secret_name = '{{ secret_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
AND value = '{{ value }}' --required
RETURNING
id,
attributes,
contentType,
kid,
managed,
previousVersion,
tags,
value;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_secret"
    values={[
        { label: 'delete_secret', value: 'delete_secret' }
    ]}
>
<TabItem value="delete_secret">

Deletes a secret from a specified key vault. The DELETE operation applies to any secret stored in Azure Key Vault. DELETE cannot be applied to an individual version of a secret. This operation requires the secrets/delete permission.

```sql
DELETE FROM azure.keyvault_secrets.secrets
WHERE secret_name = '{{ secret_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="backup_secret"
    values={[
        { label: 'backup_secret', value: 'backup_secret' },
        { label: 'restore_secret', value: 'restore_secret' }
    ]}
>
<TabItem value="backup_secret">

Backs up the specified secret. Requests that a backup of the specified secret be downloaded to the client. All versions of the secret will be downloaded. This operation requires the secrets/backup permission.

```sql
EXEC azure.keyvault_secrets.secrets.backup_secret 
@secret_name='{{ secret_name }}' --required, 
@vault_base_url='{{ vault_base_url }}' --required
;
```
</TabItem>
<TabItem value="restore_secret">

Restores a backed up secret to a vault. Restores a backed up secret, and all its versions, to a vault. This operation requires the secrets/restore permission.

```sql
EXEC azure.keyvault_secrets.secrets.restore_secret 
@vault_base_url='{{ vault_base_url }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
</Tabs>
