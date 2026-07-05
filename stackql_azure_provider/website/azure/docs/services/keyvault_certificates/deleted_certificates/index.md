--- 
title: deleted_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_certificates
  - keyvault_certificates
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

Creates, updates, deletes, gets or lists a <code>deleted_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deleted_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.deleted_certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_deleted_certificate"
    values={[
        { label: 'get_deleted_certificate', value: 'get_deleted_certificate' },
        { label: 'get_deleted_certificates', value: 'get_deleted_certificates' }
    ]}
>
<TabItem value="get_deleted_certificate">

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
    <td>The certificate id.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The certificate attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="cer" /></td>
    <td><code>string (byte)</code></td>
    <td>CER contents of x509 certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type of the secret. eg. 'application/x-pem-file' or 'application/x-pkcs12'.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was deleted, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="kid" /></td>
    <td><code>string</code></td>
    <td>The key id.</td>
</tr>
<tr>
    <td><CopyableCode code="policy" /></td>
    <td><code>object</code></td>
    <td>The management policy.</td>
</tr>
<tr>
    <td><CopyableCode code="preserveCertOrder" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the certificate chain preserves its original order. The default value is false, which sets the leaf certificate at index 0.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryId" /></td>
    <td><code>string</code></td>
    <td>The url of the recovery object, used to identify and recover the deleted certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate is scheduled to be purged, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="sid" /></td>
    <td><code>string</code></td>
    <td>The secret id.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Application specific metadata in the form of key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="x5t" /></td>
    <td><code>string (byte)</code></td>
    <td>Thumbprint of the certificate.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_deleted_certificates">

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
    <td>Certificate identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The certificate management attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was deleted, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryId" /></td>
    <td><code>string</code></td>
    <td>The url of the recovery object, used to identify and recover the deleted certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate is scheduled to be purged, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Application specific metadata in the form of key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="x5t" /></td>
    <td><code>string (byte)</code></td>
    <td>Thumbprint of the certificate.</td>
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
    <td><a href="#get_deleted_certificate"><CopyableCode code="get_deleted_certificate" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Retrieves information about the specified deleted certificate. The GetDeletedCertificate operation retrieves the deleted certificate information plus its attributes, such as retention interval, scheduled permanent deletion and the current deletion recovery level. This operation requires the certificates/get permission.</td>
</tr>
<tr>
    <td><a href="#get_deleted_certificates"><CopyableCode code="get_deleted_certificates" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-includePending"><code>includePending</code></a></td>
    <td>Lists the deleted certificates in the specified vault currently available for recovery. The GetDeletedCertificates operation retrieves the certificates in the current vault which are in a deleted state and ready for recovery or purging. This operation includes deletion-specific information. This operation requires the certificates/get/list permission. This operation can only be enabled on soft-delete enabled vaults.</td>
</tr>
<tr>
    <td><a href="#purge_deleted_certificate"><CopyableCode code="purge_deleted_certificate" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Permanently deletes the specified deleted certificate. The PurgeDeletedCertificate operation performs an irreversible deletion of the specified certificate, without possibility for recovery. The operation is not available if the recovery level does not specify 'Purgeable'. This operation requires the certificate/purge permission.</td>
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
<tr id="parameter-certificate_name">
    <td><CopyableCode code="certificate_name" /></td>
    <td><code>string</code></td>
    <td>The name of the certificate. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
<tr id="parameter-includePending">
    <td><CopyableCode code="includePending" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to include certificates which are not completely provisioned. Default value is None.</td>
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
    defaultValue="get_deleted_certificate"
    values={[
        { label: 'get_deleted_certificate', value: 'get_deleted_certificate' },
        { label: 'get_deleted_certificates', value: 'get_deleted_certificates' }
    ]}
>
<TabItem value="get_deleted_certificate">

Retrieves information about the specified deleted certificate. The GetDeletedCertificate operation retrieves the deleted certificate information plus its attributes, such as retention interval, scheduled permanent deletion and the current deletion recovery level. This operation requires the certificates/get permission.

```sql
SELECT
id,
attributes,
cer,
contentType,
deletedDate,
kid,
policy,
preserveCertOrder,
recoveryId,
scheduledPurgeDate,
sid,
tags,
x5t
FROM azure.keyvault_certificates.deleted_certificates
WHERE certificate_name = '{{ certificate_name }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
<TabItem value="get_deleted_certificates">

Lists the deleted certificates in the specified vault currently available for recovery. The GetDeletedCertificates operation retrieves the certificates in the current vault which are in a deleted state and ready for recovery or purging. This operation includes deletion-specific information. This operation requires the certificates/get/list permission. This operation can only be enabled on soft-delete enabled vaults.

```sql
SELECT
id,
attributes,
deletedDate,
recoveryId,
scheduledPurgeDate,
tags,
x5t
FROM azure.keyvault_certificates.deleted_certificates
WHERE vault_base_url = '{{ vault_base_url }}' -- required
AND maxresults = '{{ maxresults }}'
AND includePending = '{{ includePending }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="purge_deleted_certificate"
    values={[
        { label: 'purge_deleted_certificate', value: 'purge_deleted_certificate' }
    ]}
>
<TabItem value="purge_deleted_certificate">

Permanently deletes the specified deleted certificate. The PurgeDeletedCertificate operation performs an irreversible deletion of the specified certificate, without possibility for recovery. The operation is not available if the recovery level does not specify 'Purgeable'. This operation requires the certificate/purge permission.

```sql
DELETE FROM azure.keyvault_certificates.deleted_certificates
WHERE certificate_name = '{{ certificate_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>
