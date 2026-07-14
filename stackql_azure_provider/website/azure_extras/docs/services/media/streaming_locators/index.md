--- 
title: streaming_locators
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_locators
  - media
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>streaming_locators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="streaming_locators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.media.streaming_locators" /></td></tr>
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
    <td><CopyableCode code="alternativeMediaId" /></td>
    <td><code>string</code></td>
    <td>Alternative Media ID of this Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="assetName" /></td>
    <td><code>string</code></td>
    <td>Asset Name.</td>
</tr>
<tr>
    <td><CopyableCode code="contentKeys" /></td>
    <td><code>array</code></td>
    <td>The ContentKeys used by this Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultContentKeyPolicyName" /></td>
    <td><code>string</code></td>
    <td>Name of the default ContentKeyPolicy used by this Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>A list of asset or account filters which apply to this streaming locator.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingLocatorId" /></td>
    <td><code>string</code></td>
    <td>The StreamingLocatorId of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingPolicyName" /></td>
    <td><code>string</code></td>
    <td>Name of the Streaming Policy used by this Streaming Locator. Either specify the name of Streaming Policy you created or use one of the predefined Streaming Policies. The predefined Streaming Policies available are: 'Predefined_DownloadOnly', 'Predefined_ClearStreamingOnly', 'Predefined_DownloadAndClearStreaming', 'Predefined_ClearKey', 'Predefined_MultiDrmCencStreaming' and 'Predefined_MultiDrmStreaming'.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="alternativeMediaId" /></td>
    <td><code>string</code></td>
    <td>Alternative Media ID of this Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="assetName" /></td>
    <td><code>string</code></td>
    <td>Asset Name.</td>
</tr>
<tr>
    <td><CopyableCode code="contentKeys" /></td>
    <td><code>array</code></td>
    <td>The ContentKeys used by this Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultContentKeyPolicyName" /></td>
    <td><code>string</code></td>
    <td>Name of the default ContentKeyPolicy used by this Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>A list of asset or account filters which apply to this streaming locator.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingLocatorId" /></td>
    <td><code>string</code></td>
    <td>The StreamingLocatorId of the Streaming Locator.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingPolicyName" /></td>
    <td><code>string</code></td>
    <td>Name of the Streaming Policy used by this Streaming Locator. Either specify the name of Streaming Policy you created or use one of the predefined Streaming Policies. The predefined Streaming Policies available are: 'Predefined_DownloadOnly', 'Predefined_ClearStreamingOnly', 'Predefined_DownloadAndClearStreaming', 'Predefined_ClearKey', 'Predefined_MultiDrmCencStreaming' and 'Predefined_MultiDrmStreaming'.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_locator_name"><code>streaming_locator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Streaming Locator. Get the details of a Streaming Locator in the Media Services account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List Streaming Locators. Lists the Streaming Locators in the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_locator_name"><code>streaming_locator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Streaming Locator. Create a Streaming Locator in the Media Services account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_locator_name"><code>streaming_locator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Streaming Locator. Deletes a Streaming Locator in the Media Services account.</td>
</tr>
<tr>
    <td><a href="#list_content_keys"><CopyableCode code="list_content_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_locator_name"><code>streaming_locator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Content Keys. List Content Keys used by this Streaming Locator.</td>
</tr>
<tr>
    <td><a href="#list_paths"><CopyableCode code="list_paths" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_locator_name"><code>streaming_locator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Paths. List Paths supported by this Streaming Locator.</td>
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
    <td>The Media Services account name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group within the Azure subscription. Required.</td>
</tr>
<tr id="parameter-streaming_locator_name">
    <td><CopyableCode code="streaming_locator_name" /></td>
    <td><code>string</code></td>
    <td>The Streaming Locator name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Restricts the set of items returned. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Specifies the key by which the result collection should be ordered. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. Default value is None.</td>
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

Get a Streaming Locator. Get the details of a Streaming Locator in the Media Services account.

```sql
SELECT
id,
name,
alternativeMediaId,
assetName,
contentKeys,
created,
defaultContentKeyPolicyName,
endTime,
filters,
startTime,
streamingLocatorId,
streamingPolicyName,
systemData,
type
FROM azure_extras.media.streaming_locators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND streaming_locator_name = '{{ streaming_locator_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Streaming Locators. Lists the Streaming Locators in the account.

```sql
SELECT
id,
name,
alternativeMediaId,
assetName,
contentKeys,
created,
defaultContentKeyPolicyName,
endTime,
filters,
startTime,
streamingLocatorId,
streamingPolicyName,
systemData,
type
FROM azure_extras.media.streaming_locators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
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

Create a Streaming Locator. Create a Streaming Locator in the Media Services account.

```sql
INSERT INTO azure_extras.media.streaming_locators (
properties,
resource_group_name,
account_name,
streaming_locator_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ streaming_locator_name }}',
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
- name: streaming_locators
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the streaming_locators resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the streaming_locators resource.
    - name: streaming_locator_name
      value: "{{ streaming_locator_name }}"
      description: Required parameter for the streaming_locators resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the streaming_locators resource.
    - name: properties
      value:
        assetName: "{{ assetName }}"
        startTime: "{{ startTime }}"
        endTime: "{{ endTime }}"
        streamingLocatorId: "{{ streamingLocatorId }}"
        streamingPolicyName: "{{ streamingPolicyName }}"
        defaultContentKeyPolicyName: "{{ defaultContentKeyPolicyName }}"
        contentKeys:
          - id: "{{ id }}"
            type: "{{ type }}"
            labelReferenceInStreamingPolicy: "{{ labelReferenceInStreamingPolicy }}"
            value: "{{ value }}"
            policyName: "{{ policyName }}"
            tracks: "{{ tracks }}"
        alternativeMediaId: "{{ alternativeMediaId }}"
        filters:
          - "{{ filters }}"
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

Delete a Streaming Locator. Deletes a Streaming Locator in the Media Services account.

```sql
DELETE FROM azure_extras.media.streaming_locators
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND streaming_locator_name = '{{ streaming_locator_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_content_keys"
    values={[
        { label: 'list_content_keys', value: 'list_content_keys' },
        { label: 'list_paths', value: 'list_paths' }
    ]}
>
<TabItem value="list_content_keys">

List Content Keys. List Content Keys used by this Streaming Locator.

```sql
EXEC azure_extras.media.streaming_locators.list_content_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@streaming_locator_name='{{ streaming_locator_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_paths">

List Paths. List Paths supported by this Streaming Locator.

```sql
EXEC azure_extras.media.streaming_locators.list_paths 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@streaming_locator_name='{{ streaming_locator_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
