--- 
title: watchlists
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlists
  - security_insight
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

Creates, updates, deletes, gets or lists a <code>watchlists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="watchlists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.watchlists" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type of the raw content. Example : text/csv or text/tsv.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the watchlist was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that created the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDuration" /></td>
    <td><code>string</code></td>
    <td>The default duration of a watchlist (in ISO 8601 duration format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the watchlist. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeleted" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicates if the watchlist is deleted or not.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsSearchKey" /></td>
    <td><code>string</code></td>
    <td>The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>List of labels relevant to this watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfLinesToSkip" /></td>
    <td><code>integer</code></td>
    <td>The number of lines in a csv/tsv content to skip before the header.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>The provider of the watchlist. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Describes provisioning state. Known values are: "Accepted", "InProgress", "Succeeded", "Failed", and "Canceled". (Accepted, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rawContent" /></td>
    <td><code>string</code></td>
    <td>The raw content that represents to watchlist items to create. In case of csv/tsv content type, it's the content of the file that will parsed by the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The filename of the watchlist, called 'source'.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceType" /></td>
    <td><code>string</code></td>
    <td>The sourceType of the watchlist. Known values are: "Local" and "AzureStorage". (Local, AzureStorage)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId where the watchlist belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the watchlist was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that updated the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Watchlist upload : New, InProgress or Complete. **Note**</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistAlias" /></td>
    <td><code>string</code></td>
    <td>The alias of the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistId" /></td>
    <td><code>string</code></td>
    <td>The id (a Guid) of the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistType" /></td>
    <td><code>string</code></td>
    <td>The type of the watchlist.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type of the raw content. Example : text/csv or text/tsv.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the watchlist was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that created the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDuration" /></td>
    <td><code>string</code></td>
    <td>The default duration of a watchlist (in ISO 8601 duration format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the watchlist. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeleted" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicates if the watchlist is deleted or not.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsSearchKey" /></td>
    <td><code>string</code></td>
    <td>The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>List of labels relevant to this watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfLinesToSkip" /></td>
    <td><code>integer</code></td>
    <td>The number of lines in a csv/tsv content to skip before the header.</td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>The provider of the watchlist. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Describes provisioning state. Known values are: "Accepted", "InProgress", "Succeeded", "Failed", and "Canceled". (Accepted, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rawContent" /></td>
    <td><code>string</code></td>
    <td>The raw content that represents to watchlist items to create. In case of csv/tsv content type, it's the content of the file that will parsed by the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The filename of the watchlist, called 'source'.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceType" /></td>
    <td><code>string</code></td>
    <td>The sourceType of the watchlist. Known values are: "Local" and "AzureStorage". (Local, AzureStorage)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId where the watchlist belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the watchlist was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that updated the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Watchlist upload : New, InProgress or Complete. **Note**</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistAlias" /></td>
    <td><code>string</code></td>
    <td>The alias of the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistId" /></td>
    <td><code>string</code></td>
    <td>The id (a Guid) of the watchlist.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistType" /></td>
    <td><code>string</code></td>
    <td>The type of the watchlist.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a watchlist, without its watchlist items.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get all watchlists, without watchlist items.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with rawContent and contentType properties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with rawContent and contentType properties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a watchlist.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-watchlist_alias">
    <td><CopyableCode code="watchlist_alias" /></td>
    <td><code>string</code></td>
    <td>The watchlist alias. Required.</td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the monitor workspace. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a watchlist, without its watchlist items.

```sql
SELECT
id,
name,
contentType,
created,
createdBy,
defaultDuration,
description,
displayName,
etag,
isDeleted,
itemsSearchKey,
labels,
numberOfLinesToSkip,
provider,
provisioningState,
rawContent,
source,
sourceType,
systemData,
tenantId,
type,
updated,
updatedBy,
uploadStatus,
watchlistAlias,
watchlistId,
watchlistType
FROM azure.security_insight.watchlists
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND watchlist_alias = '{{ watchlist_alias }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all watchlists, without watchlist items.

```sql
SELECT
id,
name,
contentType,
created,
createdBy,
defaultDuration,
description,
displayName,
etag,
isDeleted,
itemsSearchKey,
labels,
numberOfLinesToSkip,
provider,
provisioningState,
rawContent,
source,
sourceType,
systemData,
tenantId,
type,
updated,
updatedBy,
uploadStatus,
watchlistAlias,
watchlistId,
watchlistType
FROM azure.security_insight.watchlists
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with rawContent and contentType properties.

```sql
INSERT INTO azure.security_insight.watchlists (
properties,
etag,
resource_group_name,
workspace_name,
watchlist_alias,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ watchlist_alias }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: watchlists
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the watchlists resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the watchlists resource.
    - name: watchlist_alias
      value: "{{ watchlist_alias }}"
      description: Required parameter for the watchlists resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the watchlists resource.
    - name: properties
      description: |
        Watchlist properties.
      value:
        watchlistId: "{{ watchlistId }}"
        displayName: "{{ displayName }}"
        provider: "{{ provider }}"
        source: "{{ source }}"
        sourceType: "{{ sourceType }}"
        created: "{{ created }}"
        updated: "{{ updated }}"
        createdBy:
          email: "{{ email }}"
          name: "{{ name }}"
          objectId: "{{ objectId }}"
        updatedBy:
          email: "{{ email }}"
          name: "{{ name }}"
          objectId: "{{ objectId }}"
        description: "{{ description }}"
        watchlistType: "{{ watchlistType }}"
        watchlistAlias: "{{ watchlistAlias }}"
        isDeleted: {{ isDeleted }}
        labels:
          - "{{ labels }}"
        defaultDuration: "{{ defaultDuration }}"
        tenantId: "{{ tenantId }}"
        numberOfLinesToSkip: {{ numberOfLinesToSkip }}
        rawContent: "{{ rawContent }}"
        itemsSearchKey: "{{ itemsSearchKey }}"
        contentType: "{{ contentType }}"
        uploadStatus: "{{ uploadStatus }}"
        provisioningState: "{{ provisioningState }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with rawContent and contentType properties.

```sql
REPLACE azure.security_insight.watchlists
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND watchlist_alias = '{{ watchlist_alias }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
type;
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

Delete a watchlist.

```sql
DELETE FROM azure.security_insight.watchlists
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND watchlist_alias = '{{ watchlist_alias }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
