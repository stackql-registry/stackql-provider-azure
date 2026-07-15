--- 
title: active_directory_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - active_directory_configs
  - netapp
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

Creates, updates, deletes, gets or lists an <code>active_directory_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="active_directory_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.active_directory_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="activeDirectoryStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Active Directory. Known values are: "Created", "InUse", "Deleted", "Error", and "Updating". (Created, InUse, Deleted, Error, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>array</code></td>
    <td>Users to be added to the Built-in Administrators active directory group. A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="backupOperators" /></td>
    <td><code>array</code></td>
    <td>Users to be added to the Built-in Backup Operator active directory group. A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="dns" /></td>
    <td><code>array</code></td>
    <td>An array of DNS server IP addresses(IPv4 only) for the Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Name of the Active Directory domain. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="organizationalUnit" /></td>
    <td><code>string</code></td>
    <td>The Organizational Unit (OU) within the Windows Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="secretPassword" /></td>
    <td><code>object</code></td>
    <td>Access password from Azure KeyVault Secrets to connect Active Directory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="securityOperators" /></td>
    <td><code>array</code></td>
    <td>Domain Users in the Active directory to be given SecurityPrivilege privilege (Needed for SMB Continuously available shares for SQL). A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="site" /></td>
    <td><code>string</code></td>
    <td>The Active Directory site the service will limit Domain Controller discovery to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="smbServerName" /></td>
    <td><code>string</code></td>
    <td>NetBIOS name of the SMB server. This name will be registered as a computer account in the AD and used to mount volumes.</td>
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
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>A domain user account with permission to create machine accounts.</td>
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
    <td><CopyableCode code="activeDirectoryStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Active Directory. Known values are: "Created", "InUse", "Deleted", "Error", and "Updating". (Created, InUse, Deleted, Error, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>array</code></td>
    <td>Users to be added to the Built-in Administrators active directory group. A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="backupOperators" /></td>
    <td><code>array</code></td>
    <td>Users to be added to the Built-in Backup Operator active directory group. A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="dns" /></td>
    <td><code>array</code></td>
    <td>An array of DNS server IP addresses(IPv4 only) for the Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Name of the Active Directory domain. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="organizationalUnit" /></td>
    <td><code>string</code></td>
    <td>The Organizational Unit (OU) within the Windows Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="secretPassword" /></td>
    <td><code>object</code></td>
    <td>Access password from Azure KeyVault Secrets to connect Active Directory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="securityOperators" /></td>
    <td><code>array</code></td>
    <td>Domain Users in the Active directory to be given SecurityPrivilege privilege (Needed for SMB Continuously available shares for SQL). A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="site" /></td>
    <td><code>string</code></td>
    <td>The Active Directory site the service will limit Domain Controller discovery to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="smbServerName" /></td>
    <td><code>string</code></td>
    <td>NetBIOS name of the SMB server. This name will be registered as a computer account in the AD and used to mount volumes.</td>
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
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>A domain user account with permission to create machine accounts.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="activeDirectoryStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Active Directory. Known values are: "Created", "InUse", "Deleted", "Error", and "Updating". (Created, InUse, Deleted, Error, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>array</code></td>
    <td>Users to be added to the Built-in Administrators active directory group. A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="backupOperators" /></td>
    <td><code>array</code></td>
    <td>Users to be added to the Built-in Backup Operator active directory group. A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="dns" /></td>
    <td><code>array</code></td>
    <td>An array of DNS server IP addresses(IPv4 only) for the Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Name of the Active Directory domain. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="organizationalUnit" /></td>
    <td><code>string</code></td>
    <td>The Organizational Unit (OU) within the Windows Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="secretPassword" /></td>
    <td><code>object</code></td>
    <td>Access password from Azure KeyVault Secrets to connect Active Directory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="securityOperators" /></td>
    <td><code>array</code></td>
    <td>Domain Users in the Active directory to be given SecurityPrivilege privilege (Needed for SMB Continuously available shares for SQL). A list of unique usernames without domain specifier.</td>
</tr>
<tr>
    <td><CopyableCode code="site" /></td>
    <td><code>string</code></td>
    <td>The Active Directory site the service will limit Domain Controller discovery to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="smbServerName" /></td>
    <td><code>string</code></td>
    <td>NetBIOS name of the SMB server. This name will be registered as a computer account in the AD and used to mount volumes.</td>
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
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>A domain user account with permission to create machine accounts.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-active_directory_config_name"><code>active_directory_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the details of the specified active directory configuration.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all active directory configurations within the resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all active directory configurations within the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-active_directory_config_name"><code>active_directory_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified active directory configuration.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-active_directory_config_name"><code>active_directory_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the specified active directory configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-active_directory_config_name"><code>active_directory_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified active directory configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-active_directory_config_name"><code>active_directory_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the specified Active Directory configuration.</td>
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
<tr id="parameter-active_directory_config_name">
    <td><CopyableCode code="active_directory_config_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ActiveDirectoryConfig. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get the details of the specified active directory configuration.

```sql
SELECT
id,
name,
activeDirectoryStatus,
administrators,
backupOperators,
dns,
domain,
etag,
identity,
location,
organizationalUnit,
provisioningState,
secretPassword,
securityOperators,
site,
smbServerName,
systemData,
tags,
type,
userName
FROM azure.netapp.active_directory_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND active_directory_config_name = '{{ active_directory_config_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all active directory configurations within the resource group.

```sql
SELECT
id,
name,
activeDirectoryStatus,
administrators,
backupOperators,
dns,
domain,
etag,
identity,
location,
organizationalUnit,
provisioningState,
secretPassword,
securityOperators,
site,
smbServerName,
systemData,
tags,
type,
userName
FROM azure.netapp.active_directory_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all active directory configurations within the subscription.

```sql
SELECT
id,
name,
activeDirectoryStatus,
administrators,
backupOperators,
dns,
domain,
etag,
identity,
location,
organizationalUnit,
provisioningState,
secretPassword,
securityOperators,
site,
smbServerName,
systemData,
tags,
type,
userName
FROM azure.netapp.active_directory_configs
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

Create or update the specified active directory configuration.

```sql
INSERT INTO azure.netapp.active_directory_configs (
tags,
location,
properties,
identity,
resource_group_name,
active_directory_config_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ active_directory_config_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: active_directory_configs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the active_directory_configs resource.
    - name: active_directory_config_name
      value: "{{ active_directory_config_name }}"
      description: Required parameter for the active_directory_configs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the active_directory_configs resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        userName: "{{ userName }}"
        dns:
          - "{{ dns }}"
        smbServerName: "{{ smbServerName }}"
        organizationalUnit: "{{ organizationalUnit }}"
        site: "{{ site }}"
        backupOperators:
          - "{{ backupOperators }}"
        administrators:
          - "{{ administrators }}"
        securityOperators:
          - "{{ securityOperators }}"
        activeDirectoryStatus: "{{ activeDirectoryStatus }}"
        provisioningState: "{{ provisioningState }}"
        domain: "{{ domain }}"
        secretPassword:
          keyVaultProperties:
            keyVaultUri: "{{ keyVaultUri }}"
            secretName: "{{ secretName }}"
          identity:
            principalId: "{{ principalId }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Patch the specified active directory configuration.

```sql
UPDATE azure.netapp.active_directory_configs
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND active_directory_config_name = '{{ active_directory_config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Create or update the specified active directory configuration.

```sql
REPLACE azure.netapp.active_directory_configs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND active_directory_config_name = '{{ active_directory_config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
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

Delete the specified Active Directory configuration.

```sql
DELETE FROM azure.netapp.active_directory_configs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND active_directory_config_name = '{{ active_directory_config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
