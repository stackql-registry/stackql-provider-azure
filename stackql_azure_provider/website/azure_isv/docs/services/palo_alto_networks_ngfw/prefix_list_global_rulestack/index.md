--- 
title: prefix_list_global_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - prefix_list_global_rulestack
  - palo_alto_networks_ngfw
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>prefix_list_global_rulestack</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="prefix_list_global_rulestack" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.palo_alto_networks_ngfw.prefix_list_global_rulestack" /></td></tr>
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
    <td><CopyableCode code="auditComment" /></td>
    <td><code>string</code></td>
    <td>comment for this object.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>prefix description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag info.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixList" /></td>
    <td><code>array</code></td>
    <td>prefix list. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><CopyableCode code="auditComment" /></td>
    <td><code>string</code></td>
    <td>comment for this object.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>prefix description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag info.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixList" /></td>
    <td><code>array</code></td>
    <td>prefix list. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Get a PrefixListGlobalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a></td>
    <td></td>
    <td>List PrefixListGlobalRulestackResource resources by Tenant.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a PrefixListGlobalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a PrefixListGlobalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Delete a PrefixListGlobalRulestackResource.</td>
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
<tr id="parameter-global_rulestack_name">
    <td><CopyableCode code="global_rulestack_name" /></td>
    <td><code>string</code></td>
    <td>GlobalRulestack resource name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Local Rule priority. Required.</td>
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

Get a PrefixListGlobalRulestackResource.

```sql
SELECT
id,
name,
auditComment,
description,
etag,
prefixList,
provisioningState,
systemData,
type
FROM azure_isv.palo_alto_networks_ngfw.prefix_list_global_rulestack
WHERE global_rulestack_name = '{{ global_rulestack_name }}' -- required
AND name = '{{ name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List PrefixListGlobalRulestackResource resources by Tenant.

```sql
SELECT
id,
name,
auditComment,
description,
etag,
prefixList,
provisioningState,
systemData,
type
FROM azure_isv.palo_alto_networks_ngfw.prefix_list_global_rulestack
WHERE global_rulestack_name = '{{ global_rulestack_name }}' -- required
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

Create a PrefixListGlobalRulestackResource.

```sql
INSERT INTO azure_isv.palo_alto_networks_ngfw.prefix_list_global_rulestack (
properties,
global_rulestack_name,
name
)
SELECT 
'{{ properties }}' /* required */,
'{{ global_rulestack_name }}',
'{{ name }}'
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
- name: prefix_list_global_rulestack
  props:
    - name: global_rulestack_name
      value: "{{ global_rulestack_name }}"
      description: Required parameter for the prefix_list_global_rulestack resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the prefix_list_global_rulestack resource.
    - name: properties
      value:
        description: "{{ description }}"
        prefixList:
          - "{{ prefixList }}"
        etag: "{{ etag }}"
        auditComment: "{{ auditComment }}"
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

Create a PrefixListGlobalRulestackResource.

```sql
REPLACE azure_isv.palo_alto_networks_ngfw.prefix_list_global_rulestack
SET 
properties = '{{ properties }}'
WHERE 
global_rulestack_name = '{{ global_rulestack_name }}' --required
AND name = '{{ name }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
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

Delete a PrefixListGlobalRulestackResource.

```sql
DELETE FROM azure_isv.palo_alto_networks_ngfw.prefix_list_global_rulestack
WHERE global_rulestack_name = '{{ global_rulestack_name }}' --required
AND name = '{{ name }}' --required
;
```
</TabItem>
</Tabs>
