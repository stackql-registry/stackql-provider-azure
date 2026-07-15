--- 
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
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

Creates, updates, deletes, gets or lists a <code>policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_attestation.policy" /></td></tr>
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
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
    <td>An RFC7519 JSON Web Token structure whose body is an PolicyResult object.</td>
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
    <td><a href="#parameter-attestation_type"><code>attestation_type</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves the current policy for an attestation type. Retrieves the current policy for an attestation type.</td>
</tr>
<tr>
    <td><a href="#set"><CopyableCode code="set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-attestation_type"><code>attestation_type</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Sets the policy for a given attestation type. Sets the policy for a given attestation type.</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-attestation_type"><code>attestation_type</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resets the attestation policy for the specified tenant and reverts to the default policy. Resets the attestation policy for the specified tenant and reverts to the default policy.</td>
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
<tr id="parameter-attestation_type">
    <td><CopyableCode code="attestation_type" /></td>
    <td><code>string</code></td>
    <td>Specifies the trusted execution environment to be used to validate the evidence. Known values are: "SgxEnclave", "OpenEnclave", "AzureGuest", "SevSnpVm", "Tpm", and "TdxVm". Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
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

Retrieves the current policy for an attestation type. Retrieves the current policy for an attestation type.

```sql
SELECT
token
FROM azure.security_attestation.policy
WHERE attestation_type = '{{ attestation_type }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="set"
    values={[
        { label: 'set', value: 'set' },
        { label: 'reset', value: 'reset' }
    ]}
>
<TabItem value="set">

Sets the policy for a given attestation type. Sets the policy for a given attestation type.

```sql
EXEC azure.security_attestation.policy.set 
@attestation_type='{{ attestation_type }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="reset">

Resets the attestation policy for the specified tenant and reverts to the default policy. Resets the attestation policy for the specified tenant and reverts to the default policy.

```sql
EXEC azure.security_attestation.policy.reset 
@attestation_type='{{ attestation_type }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
