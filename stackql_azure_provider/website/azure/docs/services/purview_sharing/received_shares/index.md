--- 
title: received_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - received_shares
  - purview_sharing
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

Creates, updates, deletes, gets or lists a <code>received_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="received_shares" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_sharing.received_shares" /></td></tr>
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
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-received_share_id"><code>received_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or replace a received share. Update changes to a received share.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-received_share_id"><code>received_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or replace a received share. Update changes to a received share.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-received_share_id"><code>received_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a received share. Delete a received share.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-received_share_id"><code>received_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a received share by unique id. Get a received share.</td>
</tr>
<tr>
    <td><a href="#list_attached"><CopyableCode code="list_attached" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-referenceName"><code>referenceName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderby"><code>orderby</code></a></td>
    <td>Get a list of attached received shares. List attached received shares.</td>
</tr>
<tr>
    <td><a href="#list_detached"><CopyableCode code="list_detached" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderby"><code>orderby</code></a></td>
    <td>Get a list of detached received shares. List detached received shares.</td>
</tr>
<tr>
    <td><a href="#activate_tenant_email_registration"><CopyableCode code="activate_tenant_email_registration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-repeatability-request-id"><code>repeatability-request-id</code></a></td>
    <td>Activates the tenant and email combination using the activation code received. Activates the email registration for current tenant.</td>
</tr>
<tr>
    <td><a href="#register_tenant_email_registration"><CopyableCode code="register_tenant_email_registration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-repeatability-request-id"><code>repeatability-request-id</code></a></td>
    <td>Registers the tenant and email combination for activation. Register an email for the current tenant.</td>
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
<tr id="parameter-received_share_id">
    <td><CopyableCode code="received_share_id" /></td>
    <td><code>string</code></td>
    <td>Id of the received share. Required.</td>
</tr>
<tr id="parameter-referenceName">
    <td><CopyableCode code="referenceName" /></td>
    <td><code>string</code></td>
    <td>A name that references a data store. Required.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Filters the results using OData syntax. Default value is None.</td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>string</code></td>
    <td>Sorts the results using OData syntax. Default value is None.</td>
</tr>
<tr id="parameter-repeatability-request-id">
    <td><CopyableCode code="repeatability-request-id" /></td>
    <td><code>string</code></td>
    <td>If specified, the client directs that the request is repeatable; that is, that the client can make the request multiple times with the same Repeatability-Request-Id and get back an appropriate response without the server executing the request multiple times. The value of the Repeatability-Request-Id is an opaque string representing a client-generated, globally unique for all time, identifier for the request. It is recommended to use version 4 (random) UUIDs. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_replace">

Create or replace a received share. Update changes to a received share.

```sql
INSERT INTO azure.purview_sharing.received_shares (
received_share_id,
endpoint
)
SELECT 
'{{ received_share_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: received_shares
  props:
    - name: received_share_id
      value: "{{ received_share_id }}"
      description: Required parameter for the received_shares resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the received_shares resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' }
    ]}
>
<TabItem value="create_or_replace">

Create or replace a received share. Update changes to a received share.

```sql
REPLACE azure.purview_sharing.received_shares
SET 
-- No updatable properties
WHERE 
received_share_id = '{{ received_share_id }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a received share. Delete a received share.

```sql
DELETE FROM azure.purview_sharing.received_shares
WHERE received_share_id = '{{ received_share_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_raw"
    values={[
        { label: 'get_raw', value: 'get_raw' },
        { label: 'list_attached', value: 'list_attached' },
        { label: 'list_detached', value: 'list_detached' },
        { label: 'activate_tenant_email_registration', value: 'activate_tenant_email_registration' },
        { label: 'register_tenant_email_registration', value: 'register_tenant_email_registration' }
    ]}
>
<TabItem value="get_raw">

Get a received share by unique id. Get a received share.

```sql
EXEC azure.purview_sharing.received_shares.get_raw 
@received_share_id='{{ received_share_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_attached">

Get a list of attached received shares. List attached received shares.

```sql
EXEC azure.purview_sharing.received_shares.list_attached 
@referenceName='{{ referenceName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@orderby='{{ orderby }}'
;
```
</TabItem>
<TabItem value="list_detached">

Get a list of detached received shares. List detached received shares.

```sql
EXEC azure.purview_sharing.received_shares.list_detached 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@orderby='{{ orderby }}'
;
```
</TabItem>
<TabItem value="activate_tenant_email_registration">

Activates the tenant and email combination using the activation code received. Activates the email registration for current tenant.

```sql
EXEC azure.purview_sharing.received_shares.activate_tenant_email_registration 
@endpoint='{{ endpoint }}' --required, 
@repeatability-request-id='{{ repeatability-request-id }}'
;
```
</TabItem>
<TabItem value="register_tenant_email_registration">

Registers the tenant and email combination for activation. Register an email for the current tenant.

```sql
EXEC azure.purview_sharing.received_shares.register_tenant_email_registration 
@endpoint='{{ endpoint }}' --required, 
@repeatability-request-id='{{ repeatability-request-id }}'
;
```
</TabItem>
</Tabs>
