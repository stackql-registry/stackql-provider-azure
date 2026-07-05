--- 
title: recover_deleted_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - recover_deleted_certificates
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

Creates, updates, deletes, gets or lists a <code>recover_deleted_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recover_deleted_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.recover_deleted_certificates" /></td></tr>
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
    <td><a href="#recover_deleted_certificate"><CopyableCode code="recover_deleted_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Recovers the deleted certificate back to its current version under /certificates. The RecoverDeletedCertificate operation performs the reversal of the Delete operation. The operation is applicable in vaults enabled for soft-delete, and must be issued during the retention interval (available in the deleted certificate's attributes). This operation requires the certificates/recover permission.</td>
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
    <td>The name of the deleted certificate. Required.</td>
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
    defaultValue="recover_deleted_certificate"
    values={[
        { label: 'recover_deleted_certificate', value: 'recover_deleted_certificate' }
    ]}
>
<TabItem value="recover_deleted_certificate">

Recovers the deleted certificate back to its current version under /certificates. The RecoverDeletedCertificate operation performs the reversal of the Delete operation. The operation is applicable in vaults enabled for soft-delete, and must be issued during the retention interval (available in the deleted certificate's attributes). This operation requires the certificates/recover permission.

```sql
EXEC azure.keyvault_certificates.recover_deleted_certificates.recover_deleted_certificate 
@certificate_name='{{ certificate_name }}' --required, 
@vault_base_url='{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>
