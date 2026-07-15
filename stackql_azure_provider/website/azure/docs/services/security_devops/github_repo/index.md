--- 
title: github_repo
hide_title: false
hide_table_of_contents: false
keywords:
  - github_repo
  - security_devops
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

Creates, updates, deletes, gets or lists a <code>github_repo</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="github_repo" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_devops.github_repo" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_connector', value: 'list_by_connector' }
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
    <td><CopyableCode code="accountId" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets gitHub repo account id.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Owner Name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="repoUrl" /></td>
    <td><code>string</code></td>
    <td>Gets or sets gitHub repo url.</td>
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
    <td><CopyableCode code="accountId" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets gitHub repo account id.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Owner Name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="repoUrl" /></td>
    <td><code>string</code></td>
    <td>Gets or sets gitHub repo url.</td>
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
<TabItem value="list_by_connector">

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
    <td><CopyableCode code="accountId" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets gitHub repo account id.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets GitHub Owner Name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="repoUrl" /></td>
    <td><code>string</code></td>
    <td>Gets or sets gitHub repo url.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-git_hub_connector_name"><code>git_hub_connector_name</code></a>, <a href="#parameter-git_hub_owner_name"><code>git_hub_owner_name</code></a>, <a href="#parameter-git_hub_repo_name"><code>git_hub_repo_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a monitored GitHub repository. Returns a monitored GitHub repository.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-git_hub_connector_name"><code>git_hub_connector_name</code></a>, <a href="#parameter-git_hub_owner_name"><code>git_hub_owner_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of monitored GitHub repositories. Returns a list of monitored GitHub repositories.</td>
</tr>
<tr>
    <td><a href="#list_by_connector"><CopyableCode code="list_by_connector" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-git_hub_connector_name"><code>git_hub_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of monitored GitHub repositories. Returns a list of monitored GitHub repositories.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-git_hub_connector_name"><code>git_hub_connector_name</code></a>, <a href="#parameter-git_hub_owner_name"><code>git_hub_owner_name</code></a>, <a href="#parameter-git_hub_repo_name"><code>git_hub_repo_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a monitored GitHub repository. Create or update a monitored GitHub repository.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-git_hub_connector_name"><code>git_hub_connector_name</code></a>, <a href="#parameter-git_hub_owner_name"><code>git_hub_owner_name</code></a>, <a href="#parameter-git_hub_repo_name"><code>git_hub_repo_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a monitored GitHub repository. Update a monitored GitHub repository.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-git_hub_connector_name"><code>git_hub_connector_name</code></a>, <a href="#parameter-git_hub_owner_name"><code>git_hub_owner_name</code></a>, <a href="#parameter-git_hub_repo_name"><code>git_hub_repo_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a monitored GitHub repository. Create or update a monitored GitHub repository.</td>
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
<tr id="parameter-git_hub_connector_name">
    <td><CopyableCode code="git_hub_connector_name" /></td>
    <td><code>string</code></td>
    <td>Name of the GitHub Connector. Required.</td>
</tr>
<tr id="parameter-git_hub_owner_name">
    <td><CopyableCode code="git_hub_owner_name" /></td>
    <td><code>string</code></td>
    <td>Name of the GitHub Owner. Required.</td>
</tr>
<tr id="parameter-git_hub_repo_name">
    <td><CopyableCode code="git_hub_repo_name" /></td>
    <td><code>string</code></td>
    <td>Name of the GitHub Repo. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_by_connector', value: 'list_by_connector' }
    ]}
>
<TabItem value="get">

Returns a monitored GitHub repository. Returns a monitored GitHub repository.

```sql
SELECT
id,
name,
accountId,
ownerName,
provisioningState,
repoUrl,
systemData,
type
FROM azure.security_devops.github_repo
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND git_hub_connector_name = '{{ git_hub_connector_name }}' -- required
AND git_hub_owner_name = '{{ git_hub_owner_name }}' -- required
AND git_hub_repo_name = '{{ git_hub_repo_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of monitored GitHub repositories. Returns a list of monitored GitHub repositories.

```sql
SELECT
id,
name,
accountId,
ownerName,
provisioningState,
repoUrl,
systemData,
type
FROM azure.security_devops.github_repo
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND git_hub_connector_name = '{{ git_hub_connector_name }}' -- required
AND git_hub_owner_name = '{{ git_hub_owner_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_connector">

Returns a list of monitored GitHub repositories. Returns a list of monitored GitHub repositories.

```sql
SELECT
id,
name,
accountId,
ownerName,
provisioningState,
repoUrl,
systemData,
type
FROM azure.security_devops.github_repo
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND git_hub_connector_name = '{{ git_hub_connector_name }}' -- required
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

Create or update a monitored GitHub repository. Create or update a monitored GitHub repository.

```sql
INSERT INTO azure.security_devops.github_repo (
properties,
resource_group_name,
git_hub_connector_name,
git_hub_owner_name,
git_hub_repo_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ git_hub_connector_name }}',
'{{ git_hub_owner_name }}',
'{{ git_hub_repo_name }}',
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
- name: github_repo
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the github_repo resource.
    - name: git_hub_connector_name
      value: "{{ git_hub_connector_name }}"
      description: Required parameter for the github_repo resource.
    - name: git_hub_owner_name
      value: "{{ git_hub_owner_name }}"
      description: Required parameter for the github_repo resource.
    - name: git_hub_repo_name
      value: "{{ git_hub_repo_name }}"
      description: Required parameter for the github_repo resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the github_repo resource.
    - name: properties
      description: |
        GitHub Repo properties.
      value:
        provisioningState: "{{ provisioningState }}"
        accountId: {{ accountId }}
        repoUrl: "{{ repoUrl }}"
        ownerName: "{{ ownerName }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a monitored GitHub repository. Update a monitored GitHub repository.

```sql
UPDATE azure.security_devops.github_repo
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND git_hub_connector_name = '{{ git_hub_connector_name }}' --required
AND git_hub_owner_name = '{{ git_hub_owner_name }}' --required
AND git_hub_repo_name = '{{ git_hub_repo_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
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

Create or update a monitored GitHub repository. Create or update a monitored GitHub repository.

```sql
REPLACE azure.security_devops.github_repo
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND git_hub_connector_name = '{{ git_hub_connector_name }}' --required
AND git_hub_owner_name = '{{ git_hub_owner_name }}' --required
AND git_hub_repo_name = '{{ git_hub_repo_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
