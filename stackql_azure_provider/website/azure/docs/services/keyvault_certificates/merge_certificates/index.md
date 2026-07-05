--- 
title: merge_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - merge_certificates
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

Creates, updates, deletes, gets or lists a <code>merge_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="merge_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.merge_certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#merge_certificate"><CopyableCode code="merge_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-x5c"><code>x5c</code></a></td>
    <td></td>
    <td>Merges a certificate or a certificate chain with a key pair existing on the server. The MergeCertificate operation performs the merging of a certificate or certificate chain with a key pair currently available in the service. This operation requires the certificates/create permission.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="merge_certificate"
    values={[
        { label: 'merge_certificate', value: 'merge_certificate' }
    ]}
>
<TabItem value="merge_certificate">

Merges a certificate or a certificate chain with a key pair existing on the server. The MergeCertificate operation performs the merging of a certificate or certificate chain with a key pair currently available in the service. This operation requires the certificates/create permission.

```sql
EXEC azure.keyvault_certificates.merge_certificates.merge_certificate 
@certificate_name='{{ certificate_name }}' --required, 
@vault_base_url='{{ vault_base_url }}' --required 
@@json=
'{
"x5c": "{{ x5c }}", 
"attributes": "{{ attributes }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
</Tabs>
