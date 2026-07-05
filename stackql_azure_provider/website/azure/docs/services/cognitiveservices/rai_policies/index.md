--- 
title: rai_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_policies
  - cognitiveservices
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

Creates, updates, deletes, gets or lists a <code>rai_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rai_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitiveservices.rai_policies" /></td></tr>
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
    <td><CopyableCode code="basePolicyName" /></td>
    <td><code>string</code></td>
    <td>Name of Rai policy.</td>
</tr>
<tr>
    <td><CopyableCode code="contentFilters" /></td>
    <td><code>array</code></td>
    <td>The list of Content Filters.</td>
</tr>
<tr>
    <td><CopyableCode code="customBlocklists" /></td>
    <td><code>array</code></td>
    <td>The list of custom Blocklist.</td>
</tr>
<tr>
    <td><CopyableCode code="egressPolicy" /></td>
    <td><code>object</code></td>
    <td>Egress (outbound network) policy controlling which external endpoints sandboxed agents can reach. Includes rules with Allow/Deny/Transform/Rewrite actions.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Rai policy mode. The enum value mapping is as below: Default = 0, Deferred=1, Blocking=2, Asynchronous_filter =3. Please use 'Asynchronous_filter' after 2025-06-01. It is the same as 'Deferred' in previous version. Known values are: "Default", "Deferred", "Blocking", and "Asynchronous_filter". (Default, Deferred, Blocking, Asynchronous_filter)</td>
</tr>
<tr>
    <td><CopyableCode code="safetyProviders" /></td>
    <td><code>array</code></td>
    <td>The list of Safety Providers.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><CopyableCode code="basePolicyName" /></td>
    <td><code>string</code></td>
    <td>Name of Rai policy.</td>
</tr>
<tr>
    <td><CopyableCode code="contentFilters" /></td>
    <td><code>array</code></td>
    <td>The list of Content Filters.</td>
</tr>
<tr>
    <td><CopyableCode code="customBlocklists" /></td>
    <td><code>array</code></td>
    <td>The list of custom Blocklist.</td>
</tr>
<tr>
    <td><CopyableCode code="egressPolicy" /></td>
    <td><code>object</code></td>
    <td>Egress (outbound network) policy controlling which external endpoints sandboxed agents can reach. Includes rules with Allow/Deny/Transform/Rewrite actions.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Rai policy mode. The enum value mapping is as below: Default = 0, Deferred=1, Blocking=2, Asynchronous_filter =3. Please use 'Asynchronous_filter' after 2025-06-01. It is the same as 'Deferred' in previous version. Known values are: "Default", "Deferred", "Blocking", and "Asynchronous_filter". (Default, Deferred, Blocking, Asynchronous_filter)</td>
</tr>
<tr>
    <td><CopyableCode code="safetyProviders" /></td>
    <td><code>array</code></td>
    <td>The list of Safety Providers.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_policy_name"><code>rai_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified Content Filters associated with the Azure OpenAI account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the content filters associated with the Azure OpenAI account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_policy_name"><code>rai_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified Content Filters associated with the Azure OpenAI account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_policy_name"><code>rai_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified Content Filters associated with the Azure OpenAI account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_policy_name"><code>rai_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Content Filters associated with the Azure OpenAI account.</td>
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
    <td>The name of Cognitive Services account. Required.</td>
</tr>
<tr id="parameter-rai_policy_name">
    <td><CopyableCode code="rai_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the RaiPolicy associated with the Cognitive Services Account. Required.</td>
</tr>
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

Gets the specified Content Filters associated with the Azure OpenAI account.

```sql
SELECT
id,
name,
basePolicyName,
contentFilters,
customBlocklists,
egressPolicy,
etag,
mode,
safetyProviders,
systemData,
tags,
type
FROM azure.cognitiveservices.rai_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND rai_policy_name = '{{ rai_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the content filters associated with the Azure OpenAI account.

```sql
SELECT
id,
name,
basePolicyName,
contentFilters,
customBlocklists,
egressPolicy,
etag,
mode,
safetyProviders,
systemData,
tags,
type
FROM azure.cognitiveservices.rai_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Update the state of specified Content Filters associated with the Azure OpenAI account.

```sql
INSERT INTO azure.cognitiveservices.rai_policies (
properties,
tags,
resource_group_name,
account_name,
rai_policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ rai_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: rai_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the rai_policies resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the rai_policies resource.
    - name: rai_policy_name
      value: "{{ rai_policy_name }}"
      description: Required parameter for the rai_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the rai_policies resource.
    - name: properties
      description: |
        Properties of Cognitive Services RaiPolicy.
      value:
        type: "{{ type }}"
        mode: "{{ mode }}"
        basePolicyName: "{{ basePolicyName }}"
        contentFilters:
          - name: "{{ name }}"
            enabled: {{ enabled }}
            severityThreshold: "{{ severityThreshold }}"
            blocking: {{ blocking }}
            source: "{{ source }}"
            action: "{{ action }}"
        customBlocklists:
          - blocklistName: "{{ blocklistName }}"
            blocking: {{ blocking }}
            source: "{{ source }}"
        safetyProviders:
          - safetyProviderName: "{{ safetyProviderName }}"
            blocking: {{ blocking }}
            source: "{{ source }}"
        egressPolicy:
          mode: "{{ mode }}"
          defaultAction: "{{ defaultAction }}"
          description: "{{ description }}"
          rules:
            - name: "{{ name }}"
              description: "{{ description }}"
              ruleType: "{{ ruleType }}"
              match:
                host: "{{ host }}"
                path: "{{ path }}"
              action:
                actionType: "{{ actionType }}"
                headers:
                  - operation: "{{ operation }}"
                    name: "{{ name }}"
                    value: "{{ value }}"
                    valueRef:
                      secretRef: "{{ secretRef }}"
                      managedIdentityRef: "{{ managedIdentityRef }}"
                rewrite:
                  scheme: "{{ scheme }}"
                  host: "{{ host }}"
                  path: "{{ path }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
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

Update the state of specified Content Filters associated with the Azure OpenAI account.

```sql
REPLACE azure.cognitiveservices.rai_policies
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND rai_policy_name = '{{ rai_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
tags,
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

Deletes the specified Content Filters associated with the Azure OpenAI account.

```sql
DELETE FROM azure.cognitiveservices.rai_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND rai_policy_name = '{{ rai_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
