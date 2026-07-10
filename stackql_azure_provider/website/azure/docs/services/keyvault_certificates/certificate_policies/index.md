--- 
title: certificate_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_policies
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

Creates, updates, deletes, gets or lists a <code>certificate_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.certificate_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_certificate_policy"
    values={[
        { label: 'get_certificate_policy', value: 'get_certificate_policy' }
    ]}
>
<TabItem value="get_certificate_policy">

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
    <td><CopyableCode code="issuer" /></td>
    <td><code>object</code></td>
    <td>Parameters for the issuer of the X509 component of a certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="key_props" /></td>
    <td><code>object</code></td>
    <td>Properties of the key backing a certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="lifetime_actions" /></td>
    <td><code>array</code></td>
    <td>Actions that will be performed by Key Vault over the lifetime of a certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="platformManaged" /></td>
    <td><code>object</code></td>
    <td>Configuration that enables the platform to manage the certificate on behalf of the user. This feature is currently intended for internal use only.</td>
</tr>
<tr>
    <td><CopyableCode code="secret_props" /></td>
    <td><code>object</code></td>
    <td>Properties of the secret backing a certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="x509_props" /></td>
    <td><code>object</code></td>
    <td>Properties of the X509 component of a certificate.</td>
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
    <td><a href="#get_certificate_policy"><CopyableCode code="get_certificate_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Lists the policy for a certificate. The GetCertificatePolicy operation returns the specified certificate policy resources in the specified key vault. This operation requires the certificates/get permission.</td>
</tr>
<tr>
    <td><a href="#update_certificate_policy"><CopyableCode code="update_certificate_policy" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Updates the policy for a certificate. Set specified members in the certificate policy. Leave others as null. This operation requires the certificates/update permission.</td>
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
    <td>The name of the certificate in the given vault. Required.</td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>Key vault name. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_certificate_policy"
    values={[
        { label: 'get_certificate_policy', value: 'get_certificate_policy' }
    ]}
>
<TabItem value="get_certificate_policy">

Lists the policy for a certificate. The GetCertificatePolicy operation returns the specified certificate policy resources in the specified key vault. This operation requires the certificates/get permission.

```sql
SELECT
id,
attributes,
issuer,
key_props,
lifetime_actions,
platformManaged,
secret_props,
x509_props
FROM azure.keyvault_certificates.certificate_policies
WHERE certificate_name = '{{ certificate_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_certificate_policy"
    values={[
        { label: 'update_certificate_policy', value: 'update_certificate_policy' }
    ]}
>
<TabItem value="update_certificate_policy">

Updates the policy for a certificate. Set specified members in the certificate policy. Leave others as null. This operation requires the certificates/update permission.

```sql
UPDATE azure.keyvault_certificates.certificate_policies
SET 
key_props = '{{ key_props }}',
secret_props = '{{ secret_props }}',
x509_props = '{{ x509_props }}',
lifetime_actions = '{{ lifetime_actions }}',
issuer = '{{ issuer }}',
attributes = '{{ attributes }}',
platformManaged = '{{ platformManaged }}'
WHERE 
certificate_name = '{{ certificate_name }}' --required
AND vault_name = '{{ vault_name }}' --required
RETURNING
id,
attributes,
issuer,
key_props,
lifetime_actions,
platformManaged,
secret_props,
x509_props;
```
</TabItem>
</Tabs>
