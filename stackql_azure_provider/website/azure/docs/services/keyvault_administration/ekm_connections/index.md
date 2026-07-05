--- 
title: ekm_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - ekm_connections
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

Creates, updates, deletes, gets or lists an <code>ekm_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ekm_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_administration.ekm_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ekm_connection"
    values={[
        { label: 'get_ekm_connection', value: 'get_ekm_connection' }
    ]}
>
<TabItem value="get_ekm_connection">

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
    <td><CopyableCode code="server_subject_common_name" /></td>
    <td><code>string</code></td>
    <td>The subject common name of the server certificate of EKM Proxy.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td>EKM proxy FQDN (Fully Qualified Domain Name). Only allowed characters are a-z, A-Z, 0-9, hyphen (-), dot (.), and colon (:). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="path_prefix" /></td>
    <td><code>string</code></td>
    <td>Optional path prefix for the EKM proxy (if any).</td>
</tr>
<tr>
    <td><CopyableCode code="server_ca_certificates" /></td>
    <td><code>array</code></td>
    <td>The root CA certificate chain that issued the proxy server's certificate. An array of certificates in the certificate chain, each in DER format and base64 encoded. Required.</td>
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
    <td><a href="#get_ekm_connection"><CopyableCode code="get_ekm_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Gets the EKM connection. The External Key Manager (EKM) Get operation returns EKM connection. This operation requires ekm/read permission.</td>
</tr>
<tr>
    <td><a href="#create_ekm_connection"><CopyableCode code="create_ekm_connection" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-server_ca_certificates"><code>server_ca_certificates</code></a></td>
    <td></td>
    <td>Creates the EKM connection. The External Key Manager (EKM) sets up the EKM connection. If the EKM connection already exists, this operation fails. This operation requires ekm/write permission.</td>
</tr>
<tr>
    <td><a href="#update_ekm_connection"><CopyableCode code="update_ekm_connection" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-server_ca_certificates"><code>server_ca_certificates</code></a></td>
    <td></td>
    <td>Updates the EKM connection. The External Key Manager (EKM) updates the existing EKM connection. If the EKM connection does not exist, this operation fails. This operation requires ekm/write permission.</td>
</tr>
<tr>
    <td><a href="#delete_ekm_connection"><CopyableCode code="delete_ekm_connection" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Deletes the EKM connection. The External Key Manager (EKM) deletes the existing EKM connection. If the EKM connection does not already exists, this operation fails. This operation requires ekm/delete permission.</td>
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
    defaultValue="get_ekm_connection"
    values={[
        { label: 'get_ekm_connection', value: 'get_ekm_connection' }
    ]}
>
<TabItem value="get_ekm_connection">

Gets the EKM connection. The External Key Manager (EKM) Get operation returns EKM connection. This operation requires ekm/read permission.

```sql
SELECT
server_subject_common_name,
host,
path_prefix,
server_ca_certificates
FROM azure.keyvault_administration.ekm_connections
WHERE vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_ekm_connection"
    values={[
        { label: 'create_ekm_connection', value: 'create_ekm_connection' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_ekm_connection">

Creates the EKM connection. The External Key Manager (EKM) sets up the EKM connection. If the EKM connection already exists, this operation fails. This operation requires ekm/write permission.

```sql
INSERT INTO azure.keyvault_administration.ekm_connections (
host,
path_prefix,
server_ca_certificates,
server_subject_common_name,
vault_base_url
)
SELECT 
'{{ host }}' /* required */,
'{{ path_prefix }}',
'{{ server_ca_certificates }}' /* required */,
'{{ server_subject_common_name }}',
'{{ vault_base_url }}'
RETURNING
server_subject_common_name,
host,
path_prefix,
server_ca_certificates
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ekm_connections
  props:
    - name: vault_base_url
      value: "{{ vault_base_url }}"
      description: Required parameter for the ekm_connections resource.
    - name: host
      value: "{{ host }}"
      description: |
        EKM proxy FQDN (Fully Qualified Domain Name). Only allowed characters are a-z, A-Z, 0-9, hyphen (-), dot (.), and colon (:). Required.
    - name: path_prefix
      value: "{{ path_prefix }}"
      description: |
        Optional path prefix for the EKM proxy (if any).
    - name: server_ca_certificates
      value:
        - "{{ server_ca_certificates }}"
      description: |
        The root CA certificate chain that issued the proxy server's certificate. An array of certificates in the certificate chain, each in DER format and base64 encoded. Required.
    - name: server_subject_common_name
      value: "{{ server_subject_common_name }}"
      description: |
        The subject common name of the server certificate of EKM Proxy.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_ekm_connection"
    values={[
        { label: 'update_ekm_connection', value: 'update_ekm_connection' }
    ]}
>
<TabItem value="update_ekm_connection">

Updates the EKM connection. The External Key Manager (EKM) updates the existing EKM connection. If the EKM connection does not exist, this operation fails. This operation requires ekm/write permission.

```sql
UPDATE azure.keyvault_administration.ekm_connections
SET 
host = '{{ host }}',
path_prefix = '{{ path_prefix }}',
server_ca_certificates = '{{ server_ca_certificates }}',
server_subject_common_name = '{{ server_subject_common_name }}'
WHERE 
vault_base_url = '{{ vault_base_url }}' --required
AND host = '{{ host }}' --required
AND server_ca_certificates = '{{ server_ca_certificates }}' --required
RETURNING
server_subject_common_name,
host,
path_prefix,
server_ca_certificates;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_ekm_connection"
    values={[
        { label: 'delete_ekm_connection', value: 'delete_ekm_connection' }
    ]}
>
<TabItem value="delete_ekm_connection">

Deletes the EKM connection. The External Key Manager (EKM) deletes the existing EKM connection. If the EKM connection does not already exists, this operation fails. This operation requires ekm/delete permission.

```sql
DELETE FROM azure.keyvault_administration.ekm_connections
WHERE vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>
