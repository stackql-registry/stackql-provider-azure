--- 
title: certificate_issuers
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_issuers
  - key_vault_certificates
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

Creates, updates, deletes, gets or lists a <code>certificate_issuers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_issuers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault_certificates.certificate_issuers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_certificate_issuer"
    values={[
        { label: 'get_certificate_issuer', value: 'get_certificate_issuer' },
        { label: 'get_certificate_issuers', value: 'get_certificate_issuers' }
    ]}
>
<TabItem value="get_certificate_issuer">

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
    <td>Identifier for the issuer object.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>Attributes of the issuer object.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials" /></td>
    <td><code>object</code></td>
    <td>The credentials to be used for the issuer.</td>
</tr>
<tr>
    <td><CopyableCode code="org_details" /></td>
    <td><code>object</code></td>
    <td>Details of the organization as provided to the issuer.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>The issuer provider.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_certificate_issuers">

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
    <td>Certificate Identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>The issuer provider.</td>
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
    <td><a href="#get_certificate_issuer"><CopyableCode code="get_certificate_issuer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-issuer_name"><code>issuer_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Lists the specified certificate issuer. The GetCertificateIssuer operation returns the specified certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.</td>
</tr>
<tr>
    <td><a href="#get_certificate_issuers"><CopyableCode code="get_certificate_issuers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a></td>
    <td>List certificate issuers for a specified key vault. The GetCertificateIssuers operation returns the set of certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.</td>
</tr>
<tr>
    <td><a href="#update_certificate_issuer"><CopyableCode code="update_certificate_issuer" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-issuer_name"><code>issuer_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Updates the specified certificate issuer. The UpdateCertificateIssuer operation performs an update on the specified certificate issuer entity. This operation requires the certificates/setissuers permission.</td>
</tr>
<tr>
    <td><a href="#set_certificate_issuer"><CopyableCode code="set_certificate_issuer" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-issuer_name"><code>issuer_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-provider"><code>provider</code></a></td>
    <td></td>
    <td>Sets the specified certificate issuer. The SetCertificateIssuer operation adds or updates the specified certificate issuer. This operation requires the certificates/setissuers permission.</td>
</tr>
<tr>
    <td><a href="#delete_certificate_issuer"><CopyableCode code="delete_certificate_issuer" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-issuer_name"><code>issuer_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Deletes the specified certificate issuer. The DeleteCertificateIssuer operation permanently removes the specified certificate issuer from the vault. This operation requires the certificates/manageissuers/deleteissuers permission.</td>
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
<tr id="parameter-issuer_name">
    <td><CopyableCode code="issuer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the issuer. Required.</td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>Key vault name. (default: )</td>
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
    defaultValue="get_certificate_issuer"
    values={[
        { label: 'get_certificate_issuer', value: 'get_certificate_issuer' },
        { label: 'get_certificate_issuers', value: 'get_certificate_issuers' }
    ]}
>
<TabItem value="get_certificate_issuer">

Lists the specified certificate issuer. The GetCertificateIssuer operation returns the specified certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

```sql
SELECT
id,
attributes,
credentials,
org_details,
provider
FROM azure.key_vault_certificates.certificate_issuers
WHERE issuer_name = '{{ issuer_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
;
```
</TabItem>
<TabItem value="get_certificate_issuers">

List certificate issuers for a specified key vault. The GetCertificateIssuers operation returns the set of certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

```sql
SELECT
id,
provider
FROM azure.key_vault_certificates.certificate_issuers
WHERE vault_name = '{{ vault_name }}' -- required
AND maxresults = '{{ maxresults }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_certificate_issuer"
    values={[
        { label: 'update_certificate_issuer', value: 'update_certificate_issuer' }
    ]}
>
<TabItem value="update_certificate_issuer">

Updates the specified certificate issuer. The UpdateCertificateIssuer operation performs an update on the specified certificate issuer entity. This operation requires the certificates/setissuers permission.

```sql
UPDATE azure.key_vault_certificates.certificate_issuers
SET 
provider = '{{ provider }}',
credentials = '{{ credentials }}',
org_details = '{{ org_details }}',
attributes = '{{ attributes }}'
WHERE 
issuer_name = '{{ issuer_name }}' --required
AND vault_name = '{{ vault_name }}' --required
RETURNING
id,
attributes,
credentials,
org_details,
provider;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_certificate_issuer"
    values={[
        { label: 'set_certificate_issuer', value: 'set_certificate_issuer' }
    ]}
>
<TabItem value="set_certificate_issuer">

Sets the specified certificate issuer. The SetCertificateIssuer operation adds or updates the specified certificate issuer. This operation requires the certificates/setissuers permission.

```sql
REPLACE azure.key_vault_certificates.certificate_issuers
SET 
provider = '{{ provider }}',
credentials = '{{ credentials }}',
org_details = '{{ org_details }}',
attributes = '{{ attributes }}'
WHERE 
issuer_name = '{{ issuer_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND provider = '{{ provider }}' --required
RETURNING
id,
attributes,
credentials,
org_details,
provider;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_certificate_issuer"
    values={[
        { label: 'delete_certificate_issuer', value: 'delete_certificate_issuer' }
    ]}
>
<TabItem value="delete_certificate_issuer">

Deletes the specified certificate issuer. The DeleteCertificateIssuer operation permanently removes the specified certificate issuer from the vault. This operation requires the certificates/manageissuers/deleteissuers permission.

```sql
DELETE FROM azure.key_vault_certificates.certificate_issuers
WHERE issuer_name = '{{ issuer_name }}' --required
AND vault_name = '{{ vault_name }}' --required
;
```
</TabItem>
</Tabs>
