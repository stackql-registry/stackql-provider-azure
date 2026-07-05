--- 
title: sent_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - sent_shares
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

Creates, updates, deletes, gets or lists a <code>sent_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sent_shares" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_sharing.sent_shares" /></td></tr>
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
    <td><a href="#create_invitation"><CopyableCode code="create_invitation" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-sent_share_invitation_id"><code>sent_share_invitation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a sent share invitation. Create a recipient for a given sent share.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or replace a sent share. Create or replace a sent share.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or replace a sent share. Create or replace a sent share.</td>
</tr>
<tr>
    <td><a href="#delete_invitation"><CopyableCode code="delete_invitation" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-sent_share_invitation_id"><code>sent_share_invitation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Invitation in a share. Delete a sent share invitation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a sent share. Delete a sent share.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a sent share by guid. Get a sent share.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-referenceName"><code>referenceName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderby"><code>orderby</code></a></td>
    <td>Get a list of sent shares. List sent shares.</td>
</tr>
<tr>
    <td><a href="#list_invitations"><CopyableCode code="list_invitations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderby"><code>orderby</code></a></td>
    <td>List all sent share invitations in a sent share. List sent share recipients.</td>
</tr>
<tr>
    <td><a href="#get_invitation"><CopyableCode code="get_invitation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-sent_share_invitation_id"><code>sent_share_invitation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get sent share invitation for a given sent share. Get recipient for a given sent share.</td>
</tr>
<tr>
    <td><a href="#notify_user_invitation"><CopyableCode code="notify_user_invitation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sent_share_id"><code>sent_share_id</code></a>, <a href="#parameter-sent_share_invitation_id"><code>sent_share_invitation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-repeatability-request-id"><code>repeatability-request-id</code></a></td>
    <td>Notifies the recipient of the sent share invitation. Notifies the user recipient of the sent share invitation, does not apply to service invitations.</td>
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
<tr id="parameter-referenceName">
    <td><CopyableCode code="referenceName" /></td>
    <td><code>string</code></td>
    <td>A name that references a data store. Required.</td>
</tr>
<tr id="parameter-sent_share_id">
    <td><CopyableCode code="sent_share_id" /></td>
    <td><code>string</code></td>
    <td>Id of the sent share. Required.</td>
</tr>
<tr id="parameter-sent_share_invitation_id">
    <td><CopyableCode code="sent_share_invitation_id" /></td>
    <td><code>string</code></td>
    <td>Id of the sent share invitation. Required.</td>
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
    defaultValue="create_invitation"
    values={[
        { label: 'create_invitation', value: 'create_invitation' },
        { label: 'create_or_replace', value: 'create_or_replace' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_invitation">

Create a sent share invitation. Create a recipient for a given sent share.

```sql
INSERT INTO azure.purview_sharing.sent_shares (
sent_share_id,
sent_share_invitation_id,
endpoint
)
SELECT 
'{{ sent_share_id }}',
'{{ sent_share_invitation_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="create_or_replace">

Create or replace a sent share. Create or replace a sent share.

```sql
INSERT INTO azure.purview_sharing.sent_shares (
sent_share_id,
endpoint
)
SELECT 
'{{ sent_share_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sent_shares
  props:
    - name: sent_share_id
      value: "{{ sent_share_id }}"
      description: Required parameter for the sent_shares resource.
    - name: sent_share_invitation_id
      value: "{{ sent_share_invitation_id }}"
      description: Required parameter for the sent_shares resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the sent_shares resource.
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

Create or replace a sent share. Create or replace a sent share.

```sql
REPLACE azure.purview_sharing.sent_shares
SET 
-- No updatable properties
WHERE 
sent_share_id = '{{ sent_share_id }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_invitation"
    values={[
        { label: 'delete_invitation', value: 'delete_invitation' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_invitation">

Delete Invitation in a share. Delete a sent share invitation.

```sql
DELETE FROM azure.purview_sharing.sent_shares
WHERE sent_share_id = '{{ sent_share_id }}' --required
AND sent_share_invitation_id = '{{ sent_share_invitation_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a sent share. Delete a sent share.

```sql
DELETE FROM azure.purview_sharing.sent_shares
WHERE sent_share_id = '{{ sent_share_id }}' --required
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
        { label: 'list_raw', value: 'list_raw' },
        { label: 'list_invitations', value: 'list_invitations' },
        { label: 'get_invitation', value: 'get_invitation' },
        { label: 'notify_user_invitation', value: 'notify_user_invitation' }
    ]}
>
<TabItem value="get_raw">

Get a sent share by guid. Get a sent share.

```sql
EXEC azure.purview_sharing.sent_shares.get_raw 
@sent_share_id='{{ sent_share_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Get a list of sent shares. List sent shares.

```sql
EXEC azure.purview_sharing.sent_shares.list_raw 
@referenceName='{{ referenceName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@orderby='{{ orderby }}'
;
```
</TabItem>
<TabItem value="list_invitations">

List all sent share invitations in a sent share. List sent share recipients.

```sql
EXEC azure.purview_sharing.sent_shares.list_invitations 
@sent_share_id='{{ sent_share_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@orderby='{{ orderby }}'
;
```
</TabItem>
<TabItem value="get_invitation">

Get sent share invitation for a given sent share. Get recipient for a given sent share.

```sql
EXEC azure.purview_sharing.sent_shares.get_invitation 
@sent_share_id='{{ sent_share_id }}' --required, 
@sent_share_invitation_id='{{ sent_share_invitation_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="notify_user_invitation">

Notifies the recipient of the sent share invitation. Notifies the user recipient of the sent share invitation, does not apply to service invitations.

```sql
EXEC azure.purview_sharing.sent_shares.notify_user_invitation 
@sent_share_id='{{ sent_share_id }}' --required, 
@sent_share_invitation_id='{{ sent_share_invitation_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@repeatability-request-id='{{ repeatability-request-id }}'
;
```
</TabItem>
</Tabs>
