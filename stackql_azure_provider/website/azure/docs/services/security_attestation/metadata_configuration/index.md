--- 
title: metadata_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_configuration
  - security_attestation
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

Creates, updates, deletes, gets or lists a <code>metadata_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metadata_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_attestation.metadata_configuration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="claims_supported" /></td>
    <td><code>array</code></td>
    <td>Set of claims supported by the OpenID metadata endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="id_token_signing_alg_values_supported" /></td>
    <td><code>array</code></td>
    <td>List of the supported signing algorithms.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>Issuer tenant base endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="jwks_uri" /></td>
    <td><code>string</code></td>
    <td>The URI to retrieve the signing keys.</td>
</tr>
<tr>
    <td><CopyableCode code="response_types_supported" /></td>
    <td><code>array</code></td>
    <td>Types supported in the OpenID metadata API.</td>
</tr>
<tr>
    <td><CopyableCode code="revocation_endpoint" /></td>
    <td><code>string</code></td>
    <td>Revocation endpoint.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves the OpenID Configuration data for the Azure Attestation Service. Retrieves metadata about the attestation signing keys in use by the attestation service.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieves the OpenID Configuration data for the Azure Attestation Service. Retrieves metadata about the attestation signing keys in use by the attestation service.

```sql
SELECT
claims_supported,
id_token_signing_alg_values_supported,
issuer,
jwks_uri,
response_types_supported,
revocation_endpoint
FROM azure.security_attestation.metadata_configuration
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
