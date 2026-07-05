--- 
title: certificate_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_operations
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

Creates, updates, deletes, gets or lists a <code>certificate_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.certificate_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_certificate_operation"
    values={[
        { label: 'get_certificate_operation', value: 'get_certificate_operation' }
    ]}
>
<TabItem value="get_certificate_operation">

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
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td>Identifier for the certificate operation.</td>
</tr>
<tr>
    <td><CopyableCode code="cancellation_requested" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if cancellation was requested on the certificate operation.</td>
</tr>
<tr>
    <td><CopyableCode code="csr" /></td>
    <td><code>string (byte)</code></td>
    <td>The certificate signing request (CSR) that is being used in the certificate operation.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error encountered, if any, during the certificate operation.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>object</code></td>
    <td>Parameters for the issuer of the X509 component of a certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="preserveCertOrder" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the certificate chain preserves its original order. The default value is false, which sets the leaf certificate at index 0.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the certificate operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status_details" /></td>
    <td><code>string</code></td>
    <td>The status details of the certificate operation.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>Location which contains the result of the certificate operation.</td>
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
    <td><a href="#get_certificate_operation"><CopyableCode code="get_certificate_operation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Gets the creation operation of a certificate. Gets the creation operation associated with a specified certificate. This operation requires the certificates/get permission.</td>
</tr>
<tr>
    <td><a href="#update_certificate_operation"><CopyableCode code="update_certificate_operation" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-cancellation_requested"><code>cancellation_requested</code></a></td>
    <td></td>
    <td>Updates a certificate operation. Updates a certificate creation operation that is already in progress. This operation requires the certificates/update permission.</td>
</tr>
<tr>
    <td><a href="#delete_certificate_operation"><CopyableCode code="delete_certificate_operation" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Deletes the creation operation for a specific certificate. Deletes the creation operation for a specified certificate that is in the process of being created. The certificate is no longer created. This operation requires the certificates/update permission.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_certificate_operation"
    values={[
        { label: 'get_certificate_operation', value: 'get_certificate_operation' }
    ]}
>
<TabItem value="get_certificate_operation">

Gets the creation operation of a certificate. Gets the creation operation associated with a specified certificate. This operation requires the certificates/get permission.

```sql
SELECT
id,
request_id,
cancellation_requested,
csr,
error,
issuer,
preserveCertOrder,
status,
status_details,
target
FROM azure.keyvault_certificates.certificate_operations
WHERE certificate_name = '{{ certificate_name }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_certificate_operation"
    values={[
        { label: 'update_certificate_operation', value: 'update_certificate_operation' }
    ]}
>
<TabItem value="update_certificate_operation">

Updates a certificate operation. Updates a certificate creation operation that is already in progress. This operation requires the certificates/update permission.

```sql
UPDATE azure.keyvault_certificates.certificate_operations
SET 
cancellation_requested = {{ cancellation_requested }}
WHERE 
certificate_name = '{{ certificate_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
AND cancellation_requested = {{ cancellation_requested }} --required
RETURNING
id,
request_id,
cancellation_requested,
csr,
error,
issuer,
preserveCertOrder,
status,
status_details,
target;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_certificate_operation"
    values={[
        { label: 'delete_certificate_operation', value: 'delete_certificate_operation' }
    ]}
>
<TabItem value="delete_certificate_operation">

Deletes the creation operation for a specific certificate. Deletes the creation operation for a specified certificate that is in the process of being created. The certificate is no longer created. This operation requires the certificates/update permission.

```sql
DELETE FROM azure.keyvault_certificates.certificate_operations
WHERE certificate_name = '{{ certificate_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>
