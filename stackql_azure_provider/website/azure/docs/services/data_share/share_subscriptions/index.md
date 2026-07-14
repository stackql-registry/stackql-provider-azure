--- 
title: share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - share_subscriptions
  - data_share
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

Creates, updates, deletes, gets or lists a <code>share_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="share_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.share_subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_synchronization_details"
    values={[
        { label: 'list_synchronization_details', value: 'list_synchronization_details' },
        { label: 'get', value: 'get' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_synchronization_details">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the data set.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSetId" /></td>
    <td><code>string</code></td>
    <td>Id of data set.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSetType" /></td>
    <td><code>string</code></td>
    <td>Type of the data set. Known values are: "Blob", "Container", "BlobFolder", "AdlsGen2FileSystem", "AdlsGen2Folder", "AdlsGen2File", "AdlsGen1Folder", "AdlsGen1File", "KustoCluster", "KustoDatabase", "SqlDBTable", "SqlDWTable", and "SynapseWorkspaceSqlPoolTable".</td>
</tr>
<tr>
    <td><CopyableCode code="durationMs" /></td>
    <td><code>integer</code></td>
    <td>Duration of data set level copy.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of data set level copy.</td>
</tr>
<tr>
    <td><CopyableCode code="filesRead" /></td>
    <td><code>integer</code></td>
    <td>The number of files read from the source data set.</td>
</tr>
<tr>
    <td><CopyableCode code="filesWritten" /></td>
    <td><code>integer</code></td>
    <td>The number of files written into the sink data set.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Error message if any.</td>
</tr>
<tr>
    <td><CopyableCode code="rowsCopied" /></td>
    <td><code>integer</code></td>
    <td>The number of files copied into the sink data set.</td>
</tr>
<tr>
    <td><CopyableCode code="rowsRead" /></td>
    <td><code>integer</code></td>
    <td>The number of rows read from the source data set.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeRead" /></td>
    <td><code>integer</code></td>
    <td>The size of the data read from the source data set in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeWritten" /></td>
    <td><code>integer</code></td>
    <td>The size of the data written into the sink data set in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of data set level copy.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Raw Status.</td>
</tr>
<tr>
    <td><CopyableCode code="vCore" /></td>
    <td><code>integer</code></td>
    <td>The vCore units consumed for the data set synchronization.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the share subscription was created.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date of the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationId" /></td>
    <td><code>string</code></td>
    <td>The invitation id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="providerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Name of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerTenantName" /></td>
    <td><code>string</code></td>
    <td>Tenant name of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the share subscription. Known values are: "Succeeded", "Creating", "Deleting", "Moving", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="shareDescription" /></td>
    <td><code>string</code></td>
    <td>Description of share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareKind" /></td>
    <td><code>string</code></td>
    <td>Kind of share. Known values are: "CopyBased" and "InPlace".</td>
</tr>
<tr>
    <td><CopyableCode code="shareName" /></td>
    <td><code>string</code></td>
    <td>Name of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Gets the current status of share subscription. Known values are: "Active", "Revoked", "SourceDeleted", and "Revoking".</td>
</tr>
<tr>
    <td><CopyableCode code="shareTerms" /></td>
    <td><code>string</code></td>
    <td>Terms of a share.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceShareLocation" /></td>
    <td><code>string</code></td>
    <td>Source share location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the user who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>Name of the user who created the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the share subscription was created.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date of the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationId" /></td>
    <td><code>string</code></td>
    <td>The invitation id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="providerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Name of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerTenantName" /></td>
    <td><code>string</code></td>
    <td>Tenant name of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the share subscription. Known values are: "Succeeded", "Creating", "Deleting", "Moving", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="shareDescription" /></td>
    <td><code>string</code></td>
    <td>Description of share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareKind" /></td>
    <td><code>string</code></td>
    <td>Kind of share. Known values are: "CopyBased" and "InPlace".</td>
</tr>
<tr>
    <td><CopyableCode code="shareName" /></td>
    <td><code>string</code></td>
    <td>Name of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Gets the current status of share subscription. Known values are: "Active", "Revoked", "SourceDeleted", and "Revoking".</td>
</tr>
<tr>
    <td><CopyableCode code="shareTerms" /></td>
    <td><code>string</code></td>
    <td>Terms of a share.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceShareLocation" /></td>
    <td><code>string</code></td>
    <td>Source share location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the user who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>Name of the user who created the resource.</td>
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
    <td><a href="#list_synchronization_details"><CopyableCode code="list_synchronization_details" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List data set level details for a share subscription synchronization. List synchronization details.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get shareSubscription in an account. Get a shareSubscription in an account.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List of available share subscriptions under an account. List share subscriptions in an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create shareSubscription in an account. Create a shareSubscription in an account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete shareSubscription in an account. Delete a shareSubscription in an account.</td>
</tr>
<tr>
    <td><a href="#list_source_share_synchronization_settings"><CopyableCode code="list_source_share_synchronization_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get source share synchronization settings for a shareSubscription. Get synchronization settings set on a share.</td>
</tr>
<tr>
    <td><a href="#list_synchronizations"><CopyableCode code="list_synchronizations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List Synchronizations in a share subscription. List synchronizations of a share subscription.</td>
</tr>
<tr>
    <td><a href="#cancel_synchronization"><CopyableCode code="cancel_synchronization" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-synchronizationId"><code>synchronizationId</code></a></td>
    <td></td>
    <td>Request cancellation of a data share snapshot. Request to cancel a synchronization.</td>
</tr>
<tr>
    <td><a href="#synchronize"><CopyableCode code="synchronize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiate an asynchronous data share job. Initiate a copy.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share account. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-share_subscription_name">
    <td><CopyableCode code="share_subscription_name" /></td>
    <td><code>string</code></td>
    <td>The name of share subscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filters the results using OData syntax. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Sorts the results using OData syntax. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Continuation token. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_synchronization_details"
    values={[
        { label: 'list_synchronization_details', value: 'list_synchronization_details' },
        { label: 'get', value: 'get' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_synchronization_details">

List data set level details for a share subscription synchronization. List synchronization details.

```sql
SELECT
name,
dataSetId,
dataSetType,
durationMs,
endTime,
filesRead,
filesWritten,
message,
rowsCopied,
rowsRead,
sizeRead,
sizeWritten,
startTime,
status,
vCore
FROM azure.data_share.share_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_subscription_name = '{{ share_subscription_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
<TabItem value="get">

Get shareSubscription in an account. Get a shareSubscription in an account.

```sql
SELECT
id,
name,
createdAt,
expirationDate,
invitationId,
providerEmail,
providerName,
providerTenantName,
provisioningState,
shareDescription,
shareKind,
shareName,
shareSubscriptionStatus,
shareTerms,
sourceShareLocation,
systemData,
type,
userEmail,
userName
FROM azure.data_share.share_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_subscription_name = '{{ share_subscription_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

List of available share subscriptions under an account. List share subscriptions in an account.

```sql
SELECT
id,
name,
createdAt,
expirationDate,
invitationId,
providerEmail,
providerName,
providerTenantName,
provisioningState,
shareDescription,
shareKind,
shareName,
shareSubscriptionStatus,
shareTerms,
sourceShareLocation,
systemData,
type,
userEmail,
userName
FROM azure.data_share.share_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create shareSubscription in an account. Create a shareSubscription in an account.

```sql
INSERT INTO azure.data_share.share_subscriptions (
properties,
resource_group_name,
account_name,
share_subscription_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ share_subscription_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: share_subscriptions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the share_subscriptions resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the share_subscriptions resource.
    - name: share_subscription_name
      value: "{{ share_subscription_name }}"
      description: Required parameter for the share_subscriptions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the share_subscriptions resource.
    - name: properties
      value:
        expirationDate: "{{ expirationDate }}"
        invitationId: "{{ invitationId }}"
        sourceShareLocation: "{{ sourceShareLocation }}"
`}</CodeBlock>

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

Delete shareSubscription in an account. Delete a shareSubscription in an account.

```sql
DELETE FROM azure.data_share.share_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND share_subscription_name = '{{ share_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_source_share_synchronization_settings"
    values={[
        { label: 'list_source_share_synchronization_settings', value: 'list_source_share_synchronization_settings' },
        { label: 'list_synchronizations', value: 'list_synchronizations' },
        { label: 'cancel_synchronization', value: 'cancel_synchronization' },
        { label: 'synchronize', value: 'synchronize' }
    ]}
>
<TabItem value="list_source_share_synchronization_settings">

Get source share synchronization settings for a shareSubscription. Get synchronization settings set on a share.

```sql
EXEC azure.data_share.share_subscriptions.list_source_share_synchronization_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_subscription_name='{{ share_subscription_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$skipToken='{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_synchronizations">

List Synchronizations in a share subscription. List synchronizations of a share subscription.

```sql
EXEC azure.data_share.share_subscriptions.list_synchronizations 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_subscription_name='{{ share_subscription_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$skipToken='{{ $skipToken }}', 
@$filter='{{ $filter }}', 
@$orderby='{{ $orderby }}'
;
```
</TabItem>
<TabItem value="cancel_synchronization">

Request cancellation of a data share snapshot. Request to cancel a synchronization.

```sql
EXEC azure.data_share.share_subscriptions.cancel_synchronization 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_subscription_name='{{ share_subscription_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"synchronizationId": "{{ synchronizationId }}"
}'
;
```
</TabItem>
<TabItem value="synchronize">

Initiate an asynchronous data share job. Initiate a copy.

```sql
EXEC azure.data_share.share_subscriptions.synchronize 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_subscription_name='{{ share_subscription_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"synchronizationMode": "{{ synchronizationMode }}"
}'
;
```
</TabItem>
</Tabs>
