--- 
title: user_defined_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - user_defined_endpoints
  - confidentialledger_dataplane
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

Creates, updates, deletes, gets or lists a <code>user_defined_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user_defined_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.user_defined_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user_defined_endpoint"
    values={[
        { label: 'get_user_defined_endpoint', value: 'get_user_defined_endpoint' }
    ]}
>
<TabItem value="get_user_defined_endpoint">

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
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata information for the bundle. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modules" /></td>
    <td><code>array</code></td>
    <td>Any object. Required.</td>
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
    <td><a href="#get_user_defined_endpoint"><CopyableCode code="get_user_defined_endpoint" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets a user defined endpoint. Returns the user defined endpoint in the ACL instance.</td>
</tr>
<tr>
    <td><a href="#create_user_defined_endpoint"><CopyableCode code="create_user_defined_endpoint" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-metadata"><code>metadata</code></a>, <a href="#parameter-modules"><code>modules</code></a></td>
    <td></td>
    <td>Creates a user defined endpoint. Creates the user defined endpoint in the ACL instance.</td>
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
<tr id="parameter-ledger_endpoint">
    <td><CopyableCode code="ledger_endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `ledgerEndpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_user_defined_endpoint"
    values={[
        { label: 'get_user_defined_endpoint', value: 'get_user_defined_endpoint' }
    ]}
>
<TabItem value="get_user_defined_endpoint">

Gets a user defined endpoint. Returns the user defined endpoint in the ACL instance.

```sql
SELECT
metadata,
modules
FROM azure.confidentialledger_dataplane.user_defined_endpoints
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_user_defined_endpoint"
    values={[
        { label: 'create_user_defined_endpoint', value: 'create_user_defined_endpoint' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_user_defined_endpoint">

Creates a user defined endpoint. Creates the user defined endpoint in the ACL instance.

```sql
INSERT INTO azure.confidentialledger_dataplane.user_defined_endpoints (
metadata,
modules,
ledger_endpoint
)
SELECT 
'{{ metadata }}' /* required */,
'{{ modules }}' /* required */,
'{{ ledger_endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: user_defined_endpoints
  props:
    - name: ledger_endpoint
      value: "{{ ledger_endpoint }}"
      description: Required parameter for the user_defined_endpoints resource.
    - name: metadata
      description: |
        Metadata information for the bundle. Required.
      value:
        endpoints: "{{ endpoints }}"
    - name: modules
      description: |
        Any object. Required.
      value:
        - module: "{{ module }}"
          name: "{{ name }}"
`}</CodeBlock>

</TabItem>
</Tabs>
