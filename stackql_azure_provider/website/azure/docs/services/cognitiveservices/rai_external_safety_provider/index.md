--- 
title: rai_external_safety_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_external_safety_provider
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

Creates, updates, deletes, gets or lists a <code>rai_external_safety_provider</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rai_external_safety_provider" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitiveservices.rai_external_safety_provider" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of the safety provider.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultUri" /></td>
    <td><code>string</code></td>
    <td>The Key Vault URI that contains the api key for safety provider urls.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last modified time of the safety provider.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentity" /></td>
    <td><code>string</code></td>
    <td>The managed identity to access the Key Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Safety provider mode sync/async.</td>
</tr>
<tr>
    <td><CopyableCode code="providerId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the safety provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Name of the safety provider.</td>
</tr>
<tr>
    <td><CopyableCode code="secretName" /></td>
    <td><code>string</code></td>
    <td>The name of the secret in Key Vault that contains the api key to access the webhook.</td>
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
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Webhook URL for the safety provider.</td>
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
    <td><a href="#parameter-safety_provider_name"><code>safety_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified external safety provider associated with the Subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-safety_provider_name"><code>safety_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create the rai safety provider associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-safety_provider_name"><code>safety_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create the rai safety provider associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-safety_provider_name"><code>safety_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified custom topic associated with the subscription.</td>
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
<tr id="parameter-safety_provider_name">
    <td><CopyableCode code="safety_provider_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Rai External Safety Provider associated with the Cognitive Services Account. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the specified external safety provider associated with the Subscription.

```sql
SELECT
id,
name,
createdAt,
etag,
keyVaultUri,
lastModifiedAt,
managedIdentity,
mode,
providerId,
providerName,
secretName,
systemData,
tags,
type,
url
FROM azure.cognitiveservices.rai_external_safety_provider
WHERE safety_provider_name = '{{ safety_provider_name }}' -- required
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

Create the rai safety provider associated with the subscription.

```sql
INSERT INTO azure.cognitiveservices.rai_external_safety_provider (
properties,
safety_provider_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ safety_provider_name }}',
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
- name: rai_external_safety_provider
  props:
    - name: safety_provider_name
      value: "{{ safety_provider_name }}"
      description: Required parameter for the rai_external_safety_provider resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the rai_external_safety_provider resource.
    - name: properties
      description: |
        Properties of Cognitive Services Rai External Safety provider.
      value:
        providerId: "{{ providerId }}"
        providerName: "{{ providerName }}"
        mode: "{{ mode }}"
        url: "{{ url }}"
        secretName: "{{ secretName }}"
        managedIdentity: "{{ managedIdentity }}"
        keyVaultUri: "{{ keyVaultUri }}"
        createdAt: "{{ createdAt }}"
        lastModifiedAt: "{{ lastModifiedAt }}"
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

Create the rai safety provider associated with the subscription.

```sql
REPLACE azure.cognitiveservices.rai_external_safety_provider
SET 
properties = '{{ properties }}'
WHERE 
safety_provider_name = '{{ safety_provider_name }}' --required
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

Deletes the specified custom topic associated with the subscription.

```sql
DELETE FROM azure.cognitiveservices.rai_external_safety_provider
WHERE safety_provider_name = '{{ safety_provider_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
