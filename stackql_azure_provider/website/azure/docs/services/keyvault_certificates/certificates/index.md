--- 
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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

Creates, updates, deletes, gets or lists a <code>certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_certificate"
    values={[
        { label: 'get_certificate', value: 'get_certificate' },
        { label: 'get_certificates', value: 'get_certificates' }
    ]}
>
<TabItem value="get_certificate">

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
<TabItem value="get_certificates">

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
    <td><a href="#get_certificate"><CopyableCode code="get_certificate" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-certificate_version"><code>certificate_version</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Gets information about a certificate. Gets information about a specific certificate. This operation requires the certificates/get permission.</td>
</tr>
<tr>
    <td><a href="#get_certificates"><CopyableCode code="get_certificates" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-includePending"><code>includePending</code></a></td>
    <td>List certificates in a specified key vault. The GetCertificates operation returns the set of certificates resources in the specified key vault. This operation requires the certificates/list permission.</td>
</tr>
<tr>
    <td><a href="#create_certificate"><CopyableCode code="create_certificate" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Creates a new certificate. If this is the first version, the certificate resource is created. This operation requires the certificates/create permission.</td>
</tr>
<tr>
    <td><a href="#update_certificate"><CopyableCode code="update_certificate" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-certificate_version"><code>certificate_version</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Updates the specified attributes associated with the given certificate. The UpdateCertificate operation applies the specified update on the given certificate; the only elements updated are the certificate's attributes. This operation requires the certificates/update permission.</td>
</tr>
<tr>
    <td><a href="#delete_certificate"><CopyableCode code="delete_certificate" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Deletes a certificate from a specified key vault. Deletes all versions of a certificate object along with its associated policy. Delete certificate cannot be used to remove individual versions of a certificate object. This operation requires the certificates/delete permission.</td>
</tr>
<tr>
    <td><a href="#backup_certificate"><CopyableCode code="backup_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Backs up the specified certificate. Requests that a backup of the specified certificate be downloaded to the client. All versions of the certificate will be downloaded. This operation requires the certificates/backup permission.</td>
</tr>
<tr>
    <td><a href="#restore_certificate"><CopyableCode code="restore_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Restores a backed up certificate to a vault. Restores a backed up certificate, and all its versions, to a vault. This operation requires the certificates/restore permission.</td>
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
<tr id="parameter-certificate_version">
    <td><CopyableCode code="certificate_version" /></td>
    <td><code>string</code></td>
    <td>The version of the certificate. Required.</td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>Key vault name. (default: )</td>
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
    defaultValue="get_certificate"
    values={[
        { label: 'get_certificate', value: 'get_certificate' },
        { label: 'get_certificates', value: 'get_certificates' }
    ]}
>
<TabItem value="get_certificate">

Gets information about a certificate. Gets information about a specific certificate. This operation requires the certificates/get permission.

```sql
SELECT
id,
attributes,
cer,
contentType,
kid,
policy,
preserveCertOrder,
sid,
tags,
x5t
FROM azure.keyvault_certificates.certificates
WHERE certificate_name = '{{ certificate_name }}' -- required
AND certificate_version = '{{ certificate_version }}' -- required
AND vault_name = '{{ vault_name }}' -- required
;
```
</TabItem>
<TabItem value="get_certificates">

List certificates in a specified key vault. The GetCertificates operation returns the set of certificates resources in the specified key vault. This operation requires the certificates/list permission.

```sql
SELECT
id,
attributes,
tags,
x5t
FROM azure.keyvault_certificates.certificates
WHERE vault_name = '{{ vault_name }}' -- required
AND maxresults = '{{ maxresults }}'
AND includePending = '{{ includePending }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_certificate"
    values={[
        { label: 'create_certificate', value: 'create_certificate' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_certificate">

Creates a new certificate. If this is the first version, the certificate resource is created. This operation requires the certificates/create permission.

```sql
INSERT INTO azure.keyvault_certificates.certificates (
policy,
attributes,
tags,
preserveCertOrder,
certificate_name,
vault_name
)
SELECT 
'{{ policy }}',
'{{ attributes }}',
'{{ tags }}',
{{ preserveCertOrder }},
'{{ certificate_name }}',
'{{ vault_name }}'
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
target
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: certificates
  props:
    - name: certificate_name
      value: "{{ certificate_name }}"
      description: Required parameter for the certificates resource.
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the certificates resource.
    - name: policy
      description: |
        The management policy for the certificate.
      value:
        id: "{{ id }}"
        key_props:
          exportable: {{ exportable }}
          kty: "{{ kty }}"
          key_size: {{ key_size }}
          reuse_key: {{ reuse_key }}
          crv: "{{ crv }}"
        secret_props:
          contentType: "{{ contentType }}"
        x509_props:
          subject: "{{ subject }}"
          ekus:
            - "{{ ekus }}"
          sans:
            emails:
              - "{{ emails }}"
            dns_names:
              - "{{ dns_names }}"
            upns:
              - "{{ upns }}"
            uris:
              - "{{ uris }}"
            ipAddresses:
              - "{{ ipAddresses }}"
          key_usage:
            - "{{ key_usage }}"
          validity_months: {{ validity_months }}
        lifetime_actions:
          - trigger:
              lifetime_percentage: {{ lifetime_percentage }}
              days_before_expiry: {{ days_before_expiry }}
            action:
              action_type: "{{ action_type }}"
        issuer:
          name: "{{ name }}"
          cty: "{{ cty }}"
          cert_transparency: {{ cert_transparency }}
        attributes:
          enabled: {{ enabled }}
          nbf: "{{ nbf }}"
          exp: "{{ exp }}"
          created: "{{ created }}"
          updated: "{{ updated }}"
          recoverableDays: {{ recoverableDays }}
          recoveryLevel: "{{ recoveryLevel }}"
        platformManaged:
          certificateUsage: "{{ certificateUsage }}"
          metadata: "{{ metadata }}"
    - name: attributes
      description: |
        The attributes of the certificate (optional).
      value:
        enabled: {{ enabled }}
        nbf: "{{ nbf }}"
        exp: "{{ exp }}"
        created: "{{ created }}"
        updated: "{{ updated }}"
        recoverableDays: {{ recoverableDays }}
        recoveryLevel: "{{ recoveryLevel }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Application specific metadata in the form of key-value pairs.
    - name: preserveCertOrder
      value: {{ preserveCertOrder }}
      description: |
        Specifies whether the certificate chain preserves its original order. The default value is false, which sets the leaf certificate at index 0.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_certificate"
    values={[
        { label: 'update_certificate', value: 'update_certificate' }
    ]}
>
<TabItem value="update_certificate">

Updates the specified attributes associated with the given certificate. The UpdateCertificate operation applies the specified update on the given certificate; the only elements updated are the certificate's attributes. This operation requires the certificates/update permission.

```sql
UPDATE azure.keyvault_certificates.certificates
SET 
policy = '{{ policy }}',
attributes = '{{ attributes }}',
tags = '{{ tags }}'
WHERE 
certificate_name = '{{ certificate_name }}' --required
AND certificate_version = '{{ certificate_version }}' --required
AND vault_name = '{{ vault_name }}' --required
RETURNING
id,
attributes,
cer,
contentType,
kid,
policy,
preserveCertOrder,
sid,
tags,
x5t;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_certificate"
    values={[
        { label: 'delete_certificate', value: 'delete_certificate' }
    ]}
>
<TabItem value="delete_certificate">

Deletes a certificate from a specified key vault. Deletes all versions of a certificate object along with its associated policy. Delete certificate cannot be used to remove individual versions of a certificate object. This operation requires the certificates/delete permission.

```sql
DELETE FROM azure.keyvault_certificates.certificates
WHERE certificate_name = '{{ certificate_name }}' --required
AND vault_name = '{{ vault_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="backup_certificate"
    values={[
        { label: 'backup_certificate', value: 'backup_certificate' },
        { label: 'restore_certificate', value: 'restore_certificate' }
    ]}
>
<TabItem value="backup_certificate">

Backs up the specified certificate. Requests that a backup of the specified certificate be downloaded to the client. All versions of the certificate will be downloaded. This operation requires the certificates/backup permission.

```sql
EXEC azure.keyvault_certificates.certificates.backup_certificate 
@certificate_name='{{ certificate_name }}' --required, 
@vault_name='{{ vault_name }}' --required
;
```
</TabItem>
<TabItem value="restore_certificate">

Restores a backed up certificate to a vault. Restores a backed up certificate, and all its versions, to a vault. This operation requires the certificates/restore permission.

```sql
EXEC azure.keyvault_certificates.certificates.restore_certificate 
@vault_name='{{ vault_name }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
</Tabs>
