--- 
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - storage_file_share
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

Creates, updates, deletes, gets or lists a <code>service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_file_share.service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user_delegation_key"
    values={[
        { label: 'get_user_delegation_key', value: 'get_user_delegation_key' }
    ]}
>
<TabItem value="get_user_delegation_key">

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
    <td><CopyableCode code="SignedDelegatedUserTid" /></td>
    <td><code>string</code></td>
    <td>The delegated user tenant id in Azure AD. Return if DelegatedUserTid is specified.</td>
</tr>
<tr>
    <td><CopyableCode code="SignedExpiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date-time the key expires. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="SignedOid" /></td>
    <td><code>string</code></td>
    <td>The Azure Active Directory object ID in GUID format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="SignedService" /></td>
    <td><code>string</code></td>
    <td>Abbreviation of the Azure Storage service that accepts the key. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="SignedStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date-time the key is active. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="SignedTid" /></td>
    <td><code>string</code></td>
    <td>The Azure Active Directory tenant ID in GUID format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="SignedVersion" /></td>
    <td><code>string</code></td>
    <td>The service version that created the key. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Value" /></td>
    <td><code>string</code></td>
    <td>The key as a base64 string. Required.</td>
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
    <td><a href="#get_user_delegation_key"><CopyableCode code="get_user_delegation_key" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a></td>
    <td>Retrieves a user delegation key for the File service. This is only a valid operation when using bearer token authentication.</td>
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
<tr id="parameter-account">
    <td><CopyableCode code="account" /></td>
    <td><code>string</code></td>
    <td>Storage account name. (default: )</td>
</tr>
<tr id="parameter-x-ms-version">
    <td><CopyableCode code="x-ms-version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see</td>
</tr>
<tr id="parameter-x-ms-client-request-id">
    <td><CopyableCode code="x-ms-client-request-id" /></td>
    <td><code>string</code></td>
    <td>Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_user_delegation_key"
    values={[
        { label: 'get_user_delegation_key', value: 'get_user_delegation_key' }
    ]}
>
<TabItem value="get_user_delegation_key">

Retrieves a user delegation key for the File service. This is only a valid operation when using bearer token authentication.

```sql
SELECT
SignedDelegatedUserTid,
SignedExpiry,
SignedOid,
SignedService,
SignedStart,
SignedTid,
SignedVersion,
Value
FROM azure.storage_file_share.service
WHERE x-ms-version = '{{ x-ms-version }}' -- required
AND account = '{{ account }}' -- required
AND timeout = '{{ timeout }}'
AND x-ms-client-request-id = '{{ x-ms-client-request-id }}'
;
```
</TabItem>
</Tabs>
