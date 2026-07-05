--- 
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - agrifood
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

Creates, updates, deletes, gets or lists a <code>solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="solutions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood.solutions" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag value to implement optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplacePublisherId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Publisher Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="offerId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Offer Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerId" /></td>
    <td><code>string</code></td>
    <td>Partner Id of the Solution.</td>
</tr>
<tr>
    <td><CopyableCode code="planId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Plan Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="saasSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>SaaS subscriptionId of the installed SaaS application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="saasSubscriptionName" /></td>
    <td><code>string</code></td>
    <td>SaaS subscription name of the installed SaaS application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="solutionId" /></td>
    <td><code>string</code></td>
    <td>Solution Id.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="termId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Term Id. Required.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag value to implement optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplacePublisherId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Publisher Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="offerId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Offer Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerId" /></td>
    <td><code>string</code></td>
    <td>Partner Id of the Solution.</td>
</tr>
<tr>
    <td><CopyableCode code="planId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Plan Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="saasSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>SaaS subscriptionId of the installed SaaS application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="saasSubscriptionName" /></td>
    <td><code>string</code></td>
    <td>SaaS subscription name of the installed SaaS application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="solutionId" /></td>
    <td><code>string</code></td>
    <td>Solution Id.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="termId" /></td>
    <td><code>string</code></td>
    <td>SaaS application Term Id. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solution_id"><code>solution_id</code></a></td>
    <td></td>
    <td>Get installed Solution details by Solution id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-$maxPageSize"><code>$maxPageSize</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get installed Solutions details.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solution_id"><code>solution_id</code></a></td>
    <td></td>
    <td>Install Or Update Solution.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solution_id"><code>solution_id</code></a></td>
    <td></td>
    <td>Install Or Update Solution.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-farm_beats_resource_name"><code>farm_beats_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-solution_id"><code>solution_id</code></a></td>
    <td></td>
    <td>Uninstall Solution.</td>
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
<tr id="parameter-farm_beats_resource_name">
    <td><CopyableCode code="farm_beats_resource_name" /></td>
    <td><code>string</code></td>
    <td>FarmBeats resource name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-solution_id">
    <td><CopyableCode code="solution_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$maxPageSize">
    <td><CopyableCode code="$maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of items needed (inclusive). Minimum = 10, Maximum = 1000, Default value = 50. Default value is 50.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
<tr id="parameter-maxCreatedDateTime">
    <td><CopyableCode code="maxCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxLastModifiedDateTime">
    <td><CopyableCode code="maxLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum last modified date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minCreatedDateTime">
    <td><CopyableCode code="minCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minLastModifiedDateTime">
    <td><CopyableCode code="minLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum last modified date of resource (inclusive). Default value is None.</td>
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

Get installed Solution details by Solution id.

```sql
SELECT
id,
name,
,
eTag,
marketplacePublisherId,
offerId,
partnerId,
planId,
saasSubscriptionId,
saasSubscriptionName,
solutionId,
systemData,
termId,
type
FROM azure_extras.agrifood.solutions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND solution_id = '{{ solution_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get installed Solutions details.

```sql
SELECT
id,
name,
,
eTag,
marketplacePublisherId,
offerId,
partnerId,
planId,
saasSubscriptionId,
saasSubscriptionName,
solutionId,
systemData,
termId,
type
FROM azure_extras.agrifood.solutions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND minCreatedDateTime = '{{ minCreatedDateTime }}'
AND maxCreatedDateTime = '{{ maxCreatedDateTime }}'
AND minLastModifiedDateTime = '{{ minLastModifiedDateTime }}'
AND maxLastModifiedDateTime = '{{ maxLastModifiedDateTime }}'
AND $maxPageSize = '{{ $maxPageSize }}'
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

Install Or Update Solution.

```sql
INSERT INTO azure_extras.agrifood.solutions (
properties,
resource_group_name,
farm_beats_resource_name,
subscription_id,
solution_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ farm_beats_resource_name }}',
'{{ subscription_id }}',
'{{ solution_id }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: solutions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the solutions resource.
    - name: farm_beats_resource_name
      value: "{{ farm_beats_resource_name }}"
      description: Required parameter for the solutions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the solutions resource.
    - name: solution_id
      value: "{{ solution_id }}"
      description: Required parameter for the solutions resource.
    - name: properties
      description: |
        Solution resource properties.
      value:
        : "{{  }}"
        solutionId: "{{ solutionId }}"
        partnerId: "{{ partnerId }}"
        saasSubscriptionId: "{{ saasSubscriptionId }}"
        saasSubscriptionName: "{{ saasSubscriptionName }}"
        marketplacePublisherId: "{{ marketplacePublisherId }}"
        planId: "{{ planId }}"
        offerId: "{{ offerId }}"
        termId: "{{ termId }}"
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

Install Or Update Solution.

```sql
REPLACE azure_extras.agrifood.solutions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND solution_id = '{{ solution_id }}' --required
RETURNING
id,
name,
eTag,
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

Uninstall Solution.

```sql
DELETE FROM azure_extras.agrifood.solutions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND farm_beats_resource_name = '{{ farm_beats_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND solution_id = '{{ solution_id }}' --required
;
```
</TabItem>
</Tabs>
