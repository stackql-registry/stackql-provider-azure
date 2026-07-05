--- 
title: ledger_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger_identities
  - confidentialledger_certificate
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

Creates, updates, deletes, gets or lists a <code>ledger_identities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ledger_identities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_certificate.ledger_identities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ledger_identity"
    values={[
        { label: 'get_ledger_identity', value: 'get_ledger_identity' }
    ]}
>
<TabItem value="get_ledger_identity">

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
    <td><CopyableCode code="ledgerId" /></td>
    <td><code>string</code></td>
    <td>Id for the ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerTlsCertificate" /></td>
    <td><code>string</code></td>
    <td>PEM-encoded certificate used for TLS by the Confidential Ledger. Required.</td>
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
    <td><a href="#get_ledger_identity"><CopyableCode code="get_ledger_identity" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_id"><code>ledger_id</code></a>, <a href="#parameter-certificate_endpoint"><code>certificate_endpoint</code></a></td>
    <td></td>
    <td>Gets identity information for a Confidential Ledger instance. Gets identity information for a Confidential Ledger instance.</td>
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
<tr id="parameter-certificate_endpoint">
    <td><CopyableCode code="certificate_endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `certificateEndpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-ledger_id">
    <td><CopyableCode code="ledger_id" /></td>
    <td><code>string</code></td>
    <td>Id of the Confidential Ledger instance to get information for. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_ledger_identity"
    values={[
        { label: 'get_ledger_identity', value: 'get_ledger_identity' }
    ]}
>
<TabItem value="get_ledger_identity">

Gets identity information for a Confidential Ledger instance. Gets identity information for a Confidential Ledger instance.

```sql
SELECT
ledgerId,
ledgerTlsCertificate
FROM azure.confidentialledger_certificate.ledger_identities
WHERE ledger_id = '{{ ledger_id }}' -- required
AND certificate_endpoint = '{{ certificate_endpoint }}' -- required
;
```
</TabItem>
</Tabs>
