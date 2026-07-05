--- 
title: certificate_contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_contacts
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

Creates, updates, deletes, gets or lists a <code>certificate_contacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_contacts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.certificate_contacts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_certificate_contacts"
    values={[
        { label: 'get_certificate_contacts', value: 'get_certificate_contacts' }
    ]}
>
<TabItem value="get_certificate_contacts">

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
    <td>Identifier for the contacts collection.</td>
</tr>
<tr>
    <td><CopyableCode code="contacts" /></td>
    <td><code>array</code></td>
    <td>The contact list for the vault certificates.</td>
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
    <td><a href="#get_certificate_contacts"><CopyableCode code="get_certificate_contacts" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Lists the certificate contacts for a specified key vault. The GetCertificateContacts operation returns the set of certificate contact resources in the specified key vault. This operation requires the certificates/managecontacts permission.</td>
</tr>
<tr>
    <td><a href="#set_certificate_contacts"><CopyableCode code="set_certificate_contacts" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Sets the certificate contacts for the specified key vault. Sets the certificate contacts for the specified key vault. This operation requires the certificates/managecontacts permission.</td>
</tr>
<tr>
    <td><a href="#delete_certificate_contacts"><CopyableCode code="delete_certificate_contacts" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Deletes the certificate contacts for a specified key vault. Deletes the certificate contacts for a specified key vault certificate. This operation requires the certificates/managecontacts permission.</td>
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
    defaultValue="get_certificate_contacts"
    values={[
        { label: 'get_certificate_contacts', value: 'get_certificate_contacts' }
    ]}
>
<TabItem value="get_certificate_contacts">

Lists the certificate contacts for a specified key vault. The GetCertificateContacts operation returns the set of certificate contact resources in the specified key vault. This operation requires the certificates/managecontacts permission.

```sql
SELECT
id,
contacts
FROM azure.keyvault_certificates.certificate_contacts
WHERE vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_certificate_contacts"
    values={[
        { label: 'set_certificate_contacts', value: 'set_certificate_contacts' }
    ]}
>
<TabItem value="set_certificate_contacts">

Sets the certificate contacts for the specified key vault. Sets the certificate contacts for the specified key vault. This operation requires the certificates/managecontacts permission.

```sql
REPLACE azure.keyvault_certificates.certificate_contacts
SET 
contacts = '{{ contacts }}'
WHERE 
vault_base_url = '{{ vault_base_url }}' --required
RETURNING
id,
contacts;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_certificate_contacts"
    values={[
        { label: 'delete_certificate_contacts', value: 'delete_certificate_contacts' }
    ]}
>
<TabItem value="delete_certificate_contacts">

Deletes the certificate contacts for a specified key vault. Deletes the certificate contacts for a specified key vault certificate. This operation requires the certificates/managecontacts permission.

```sql
DELETE FROM azure.keyvault_certificates.certificate_contacts
WHERE vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>
