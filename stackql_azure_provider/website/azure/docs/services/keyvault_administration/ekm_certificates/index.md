--- 
title: ekm_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - ekm_certificates
  - keyvault_administration
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

Creates, updates, deletes, gets or lists an <code>ekm_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ekm_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_administration.ekm_certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ekm_certificate"
    values={[
        { label: 'get_ekm_certificate', value: 'get_ekm_certificate' }
    ]}
>
<TabItem value="get_ekm_certificate">

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
    <td><CopyableCode code="subject_common_name" /></td>
    <td><code>string</code></td>
    <td>The subject common name of the client certificate used to authenticate to the EKM proxy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ca_certificates" /></td>
    <td><code>array</code></td>
    <td>The client root CA certificate chain to authenticate to the EKM proxy. An array of certificates in the certificate chain, each in DER format and base64 encoded. Required.</td>
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
    <td><a href="#get_ekm_certificate"><CopyableCode code="get_ekm_certificate" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Gets the EKM proxy client certificate. The External Key Manager (EKM) Certificate Get operation returns Proxy client certificate. This operation requires ekm/read permission.</td>
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
    defaultValue="get_ekm_certificate"
    values={[
        { label: 'get_ekm_certificate', value: 'get_ekm_certificate' }
    ]}
>
<TabItem value="get_ekm_certificate">

Gets the EKM proxy client certificate. The External Key Manager (EKM) Certificate Get operation returns Proxy client certificate. This operation requires ekm/read permission.

```sql
SELECT
subject_common_name,
ca_certificates
FROM azure.keyvault_administration.ekm_certificates
WHERE vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>
