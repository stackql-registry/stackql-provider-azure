--- 
title: factories
hide_title: false
hide_table_of_contents: false
keywords:
  - factories
  - datafactory
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

Creates, updates, deletes, gets or lists a <code>factories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="factories" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datafactory.factories" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the factory was created in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Properties to enable Customer Managed Key for the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="globalParameters" /></td>
    <td><code>object</code></td>
    <td>List of parameters for factory.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Factory provisioning state, example Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for the data factory. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purviewConfiguration" /></td>
    <td><code>object</code></td>
    <td>Purview information of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="repoConfiguration" /></td>
    <td><code>object</code></td>
    <td>Git repo information of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the factory.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the factory was created in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Properties to enable Customer Managed Key for the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="globalParameters" /></td>
    <td><code>object</code></td>
    <td>List of parameters for factory.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Factory provisioning state, example Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for the data factory. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purviewConfiguration" /></td>
    <td><code>object</code></td>
    <td>Purview information of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="repoConfiguration" /></td>
    <td><code>object</code></td>
    <td>Git repo information of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the factory.</td>
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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the factory was created in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Properties to enable Customer Managed Key for the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="globalParameters" /></td>
    <td><code>object</code></td>
    <td>List of parameters for factory.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Factory provisioning state, example Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for the data factory. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purviewConfiguration" /></td>
    <td><code>object</code></td>
    <td>Purview information of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="repoConfiguration" /></td>
    <td><code>object</code></td>
    <td>Git repo information of the factory.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the factory.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a factory.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists factories.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists factories under the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a factory.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a factory.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a factory.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a factory.</td>
</tr>
<tr>
    <td><a href="#get_git_hub_access_token"><CopyableCode code="get_git_hub_access_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-gitHubAccessCode"><code>gitHubAccessCode</code></a>, <a href="#parameter-gitHubAccessTokenBaseUrl"><code>gitHubAccessTokenBaseUrl</code></a></td>
    <td></td>
    <td>Get GitHub Access Token.</td>
</tr>
<tr>
    <td><a href="#get_data_plane_access"><CopyableCode code="get_data_plane_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Data Plane access.</td>
</tr>
<tr>
    <td><a href="#configure_factory_repo"><CopyableCode code="configure_factory_repo" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_id"><code>location_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a factory's repo information.</td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>The factory name. Required.</td>
</tr>
<tr id="parameter-location_id">
    <td><CopyableCode code="location_id" /></td>
    <td><code>string</code></td>
    <td>The location identifier. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a factory.

```sql
SELECT
id,
name,
createTime,
eTag,
encryption,
globalParameters,
identity,
location,
provisioningState,
publicNetworkAccess,
purviewConfiguration,
repoConfiguration,
systemData,
tags,
type,
version
FROM azure.datafactory.factories
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists factories.

```sql
SELECT
id,
name,
createTime,
eTag,
encryption,
globalParameters,
identity,
location,
provisioningState,
publicNetworkAccess,
purviewConfiguration,
repoConfiguration,
systemData,
tags,
type,
version
FROM azure.datafactory.factories
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists factories under the specified subscription.

```sql
SELECT
id,
name,
createTime,
eTag,
encryption,
globalParameters,
identity,
location,
provisioningState,
publicNetworkAccess,
purviewConfiguration,
repoConfiguration,
systemData,
tags,
type,
version
FROM azure.datafactory.factories
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a factory.

```sql
INSERT INTO azure.datafactory.factories (
properties,
identity,
location,
tags,
resource_group_name,
factory_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ location }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ factory_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: factories
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the factories resource.
    - name: factory_name
      value: "{{ factory_name }}"
      description: Required parameter for the factories resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the factories resource.
    - name: properties
      description: |
        Properties of the factory.
      value:
        provisioningState: "{{ provisioningState }}"
        createTime: "{{ createTime }}"
        version: "{{ version }}"
        purviewConfiguration:
          purviewResourceId: "{{ purviewResourceId }}"
        repoConfiguration:
          type: "{{ type }}"
          accountName: "{{ accountName }}"
          repositoryName: "{{ repositoryName }}"
          collaborationBranch: "{{ collaborationBranch }}"
          rootFolder: "{{ rootFolder }}"
          lastCommitId: "{{ lastCommitId }}"
          disablePublish: {{ disablePublish }}
        globalParameters: "{{ globalParameters }}"
        encryption:
          keyName: "{{ keyName }}"
          vaultBaseUrl: "{{ vaultBaseUrl }}"
          keyVersion: "{{ keyVersion }}"
          identity:
            userAssignedIdentity: "{{ userAssignedIdentity }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
    - name: identity
      description: |
        Managed service identity of the factory.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: location
      value: "{{ location }}"
      description: |
        The resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
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

Updates a factory.

```sql
UPDATE azure.datafactory.factories
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
identity,
location,
properties,
systemData,
tags,
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

Creates or updates a factory.

```sql
REPLACE azure.datafactory.factories
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
identity,
location,
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

Deletes a factory.

```sql
DELETE FROM azure.datafactory.factories
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_git_hub_access_token"
    values={[
        { label: 'get_git_hub_access_token', value: 'get_git_hub_access_token' },
        { label: 'get_data_plane_access', value: 'get_data_plane_access' },
        { label: 'configure_factory_repo', value: 'configure_factory_repo' }
    ]}
>
<TabItem value="get_git_hub_access_token">

Get GitHub Access Token.

```sql
EXEC azure.datafactory.factories.get_git_hub_access_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"gitHubAccessCode": "{{ gitHubAccessCode }}", 
"gitHubClientId": "{{ gitHubClientId }}", 
"gitHubClientSecret": "{{ gitHubClientSecret }}", 
"gitHubAccessTokenBaseUrl": "{{ gitHubAccessTokenBaseUrl }}"
}'
;
```
</TabItem>
<TabItem value="get_data_plane_access">

Get Data Plane access.

```sql
EXEC azure.datafactory.factories.get_data_plane_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"permissions": "{{ permissions }}", 
"accessResourcePath": "{{ accessResourcePath }}", 
"profileName": "{{ profileName }}", 
"startTime": "{{ startTime }}", 
"expireTime": "{{ expireTime }}"
}'
;
```
</TabItem>
<TabItem value="configure_factory_repo">

Updates a factory's repo information.

```sql
EXEC azure.datafactory.factories.configure_factory_repo 
@location_id='{{ location_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"factoryResourceId": "{{ factoryResourceId }}", 
"repoConfiguration": "{{ repoConfiguration }}"
}'
;
```
</TabItem>
</Tabs>
