--- 
title: account_capability_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - account_capability_hosts
  - cognitive_services
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

Creates, updates, deletes, gets or lists an <code>account_capability_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_capability_hosts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.account_capability_hosts" /></td></tr>
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
    <td><CopyableCode code="aiServicesConnections" /></td>
    <td><code>array</code></td>
    <td>List of AI services connections.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilityHostKind" /></td>
    <td><code>string</code></td>
    <td>Kind of this capability host. "Agents" (Agents)</td>
</tr>
<tr>
    <td><CopyableCode code="customerSubnet" /></td>
    <td><code>string</code></td>
    <td>Customer subnet info to help set up this capability host.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePublicHostingEnvironment" /></td>
    <td><code>boolean</code></td>
    <td>Whether public hosting environment is enabled for the capability host.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state for the CapabilityHost. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="storageConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names from those available in the account or project to be used as a storage resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="threadStorageConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names from those available in the account or project to be used for Thread storage.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vectorStoreConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names from those available in the account or project to be used for vector database (e.g. CosmosDB).</td>
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
    <td><CopyableCode code="aiServicesConnections" /></td>
    <td><code>array</code></td>
    <td>List of AI services connections.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilityHostKind" /></td>
    <td><code>string</code></td>
    <td>Kind of this capability host. "Agents" (Agents)</td>
</tr>
<tr>
    <td><CopyableCode code="customerSubnet" /></td>
    <td><code>string</code></td>
    <td>Customer subnet info to help set up this capability host.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePublicHostingEnvironment" /></td>
    <td><code>boolean</code></td>
    <td>Whether public hosting environment is enabled for the capability host.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state for the CapabilityHost. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="storageConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names from those available in the account or project to be used as a storage resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="threadStorageConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names from those available in the account or project to be used for Thread storage.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vectorStoreConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names from those available in the account or project to be used for vector database (e.g. CosmosDB).</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-capability_host_name"><code>capability_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get account capabilityHost. Get account capabilityHost.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List capabilityHost. List capabilityHost.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-capability_host_name"><code>capability_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update account capabilityHost. Create or update account capabilityHost.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-capability_host_name"><code>capability_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update account capabilityHost. Create or update account capabilityHost.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-capability_host_name"><code>capability_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete account capabilityHost. Delete account capabilityHost.</td>
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
<tr id="parameter-capability_host_name">
    <td><CopyableCode code="capability_host_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capability host associated with the Cognitive Services Resource. Required.</td>
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

Get account capabilityHost. Get account capabilityHost.

```sql
SELECT
id,
name,
aiServicesConnections,
capabilityHostKind,
customerSubnet,
description,
enablePublicHostingEnvironment,
provisioningState,
storageConnections,
systemData,
tags,
threadStorageConnections,
type,
vectorStoreConnections
FROM azure.cognitive_services.account_capability_hosts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND capability_host_name = '{{ capability_host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List capabilityHost. List capabilityHost.

```sql
SELECT
id,
name,
aiServicesConnections,
capabilityHostKind,
customerSubnet,
description,
enablePublicHostingEnvironment,
provisioningState,
storageConnections,
systemData,
tags,
threadStorageConnections,
type,
vectorStoreConnections
FROM azure.cognitive_services.account_capability_hosts
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

Create or update account capabilityHost. Create or update account capabilityHost.

```sql
INSERT INTO azure.cognitive_services.account_capability_hosts (
properties,
resource_group_name,
account_name,
capability_host_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ capability_host_name }}',
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
- name: account_capability_hosts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the account_capability_hosts resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the account_capability_hosts resource.
    - name: capability_host_name
      value: "{{ capability_host_name }}"
      description: Required parameter for the account_capability_hosts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the account_capability_hosts resource.
    - name: properties
      description: |
        [Required] Additional attributes of the entity. Required.
      value:
        description: "{{ description }}"
        tags: "{{ tags }}"
        aiServicesConnections:
          - "{{ aiServicesConnections }}"
        capabilityHostKind: "{{ capabilityHostKind }}"
        customerSubnet: "{{ customerSubnet }}"
        provisioningState: "{{ provisioningState }}"
        storageConnections:
          - "{{ storageConnections }}"
        threadStorageConnections:
          - "{{ threadStorageConnections }}"
        vectorStoreConnections:
          - "{{ vectorStoreConnections }}"
        enablePublicHostingEnvironment: {{ enablePublicHostingEnvironment }}
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

Create or update account capabilityHost. Create or update account capabilityHost.

```sql
REPLACE azure.cognitive_services.account_capability_hosts
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND capability_host_name = '{{ capability_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Delete account capabilityHost. Delete account capabilityHost.

```sql
DELETE FROM azure.cognitive_services.account_capability_hosts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND capability_host_name = '{{ capability_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
