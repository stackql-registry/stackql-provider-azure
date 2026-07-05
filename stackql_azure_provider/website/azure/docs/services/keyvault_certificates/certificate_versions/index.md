--- 
title: certificate_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_versions
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

Creates, updates, deletes, gets or lists a <code>certificate_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_certificates.certificate_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_certificate_versions"
    values={[
        { label: 'get_certificate_versions', value: 'get_certificate_versions' }
    ]}
>
<TabItem value="get_certificate_versions">

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
    <td><a href="#get_certificate_versions"><CopyableCode code="get_certificate_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a></td>
    <td>List the versions of a certificate. The GetCertificateVersions operation returns the versions of a certificate in the specified key vault. This operation requires the certificates/list permission.</td>
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
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results to return in a page. If not specified the service will return up to 25 results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_certificate_versions"
    values={[
        { label: 'get_certificate_versions', value: 'get_certificate_versions' }
    ]}
>
<TabItem value="get_certificate_versions">

List the versions of a certificate. The GetCertificateVersions operation returns the versions of a certificate in the specified key vault. This operation requires the certificates/list permission.

```sql
SELECT
id,
attributes,
tags,
x5t
FROM azure.keyvault_certificates.certificate_versions
WHERE certificate_name = '{{ certificate_name }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
AND maxresults = '{{ maxresults }}'
;
```
</TabItem>
</Tabs>
