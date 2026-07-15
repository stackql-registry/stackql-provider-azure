--- 
title: attestation
hide_title: false
hide_table_of_contents: false
keywords:
  - attestation
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

Creates, updates, deletes, gets or lists an <code>attestation</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="attestation" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_attestation.attestation" /></td></tr>
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
    <td><a href="#attest_open_enclave"><CopyableCode code="attest_open_enclave" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Attest to an SGX enclave. Processes an OpenEnclave report , producing an artifact. The type of artifact produced is dependent upon attestation policy.</td>
</tr>
<tr>
    <td><a href="#attest_sgx_enclave"><CopyableCode code="attest_sgx_enclave" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Attest to an SGX enclave. Processes an SGX enclave quote, producing an artifact. The type of artifact produced is dependent upon attestation policy.</td>
</tr>
<tr>
    <td><a href="#attest_azure_guest"><CopyableCode code="attest_azure_guest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Attest to an Azure Guest VM. Processes an Azure Guest TCG Log, producing an artifact. The type of artifact produced is dependent upon attestation policy.</td>
</tr>
<tr>
    <td><a href="#attest_tpm"><CopyableCode code="attest_tpm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Attest a Virtualization-based Security (VBS) enclave. Processes attestation evidence from a VBS enclave, producing an attestation result. The attestation result produced is dependent upon the attestation policy.</td>
</tr>
<tr>
    <td><a href="#attest_sev_snp_vm"><CopyableCode code="attest_sev_snp_vm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Attest to an SEV SNP Virtual Machine. Processes a SEV SNP Boot chain. The type of artifact produced is dependent upon attestation policy.</td>
</tr>
<tr>
    <td><a href="#attest_tdx_vm"><CopyableCode code="attest_tdx_vm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Attest to a TDX Virtual Machine. Processes an TDX quote, producing an artifact. The type of artifact produced is dependent upon attestation policy.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="attest_open_enclave"
    values={[
        { label: 'attest_open_enclave', value: 'attest_open_enclave' },
        { label: 'attest_sgx_enclave', value: 'attest_sgx_enclave' },
        { label: 'attest_azure_guest', value: 'attest_azure_guest' },
        { label: 'attest_tpm', value: 'attest_tpm' },
        { label: 'attest_sev_snp_vm', value: 'attest_sev_snp_vm' },
        { label: 'attest_tdx_vm', value: 'attest_tdx_vm' }
    ]}
>
<TabItem value="attest_open_enclave">

Attest to an SGX enclave. Processes an OpenEnclave report , producing an artifact. The type of artifact produced is dependent upon attestation policy.

```sql
EXEC azure.security_attestation.attestation.attest_open_enclave 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="attest_sgx_enclave">

Attest to an SGX enclave. Processes an SGX enclave quote, producing an artifact. The type of artifact produced is dependent upon attestation policy.

```sql
EXEC azure.security_attestation.attestation.attest_sgx_enclave 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="attest_azure_guest">

Attest to an Azure Guest VM. Processes an Azure Guest TCG Log, producing an artifact. The type of artifact produced is dependent upon attestation policy.

```sql
EXEC azure.security_attestation.attestation.attest_azure_guest 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="attest_tpm">

Attest a Virtualization-based Security (VBS) enclave. Processes attestation evidence from a VBS enclave, producing an attestation result. The attestation result produced is dependent upon the attestation policy.

```sql
EXEC azure.security_attestation.attestation.attest_tpm 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="attest_sev_snp_vm">

Attest to an SEV SNP Virtual Machine. Processes a SEV SNP Boot chain. The type of artifact produced is dependent upon attestation policy.

```sql
EXEC azure.security_attestation.attestation.attest_sev_snp_vm 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="attest_tdx_vm">

Attest to a TDX Virtual Machine. Processes an TDX quote, producing an artifact. The type of artifact produced is dependent upon attestation policy.

```sql
EXEC azure.security_attestation.attestation.attest_tdx_vm 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
