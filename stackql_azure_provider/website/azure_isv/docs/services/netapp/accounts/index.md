--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - netapp
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

Creates, updates, deletes, gets or lists an <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
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
    <td><CopyableCode code="activeDirectories" /></td>
    <td><code>array</code></td>
    <td>Active Directories.</td>
</tr>
<tr>
    <td><CopyableCode code="disableShowmount" /></td>
    <td><code>boolean</code></td>
    <td>Shows the status of disableShowmount for all volumes under the subscription, null equals false.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption settings.</td>
</tr>
<tr>
    <td><CopyableCode code="entraIdConfig" /></td>
    <td><code>object</code></td>
    <td>Entra ID configuration for the account.</td>
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
    <td><CopyableCode code="ldapConfiguration" /></td>
    <td><code>object</code></td>
    <td>LDAP Configuration for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="multiAdStatus" /></td>
    <td><code>string</code></td>
    <td>MultiAD Status for the account. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nfsV4IDDomain" /></td>
    <td><code>string</code></td>
    <td>Domain for NFSv4 user ID mapping. This property will be set for all NetApp accounts in the subscription and region and only affect non ldap NFSv4 volumes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
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
    <td><CopyableCode code="activeDirectories" /></td>
    <td><code>array</code></td>
    <td>Active Directories.</td>
</tr>
<tr>
    <td><CopyableCode code="disableShowmount" /></td>
    <td><code>boolean</code></td>
    <td>Shows the status of disableShowmount for all volumes under the subscription, null equals false.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption settings.</td>
</tr>
<tr>
    <td><CopyableCode code="entraIdConfig" /></td>
    <td><code>object</code></td>
    <td>Entra ID configuration for the account.</td>
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
    <td><CopyableCode code="ldapConfiguration" /></td>
    <td><code>object</code></td>
    <td>LDAP Configuration for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="multiAdStatus" /></td>
    <td><code>string</code></td>
    <td>MultiAD Status for the account. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nfsV4IDDomain" /></td>
    <td><code>string</code></td>
    <td>Domain for NFSv4 user ID mapping. This property will be set for all NetApp accounts in the subscription and region and only affect non ldap NFSv4 volumes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
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
    <td><CopyableCode code="activeDirectories" /></td>
    <td><code>array</code></td>
    <td>Active Directories.</td>
</tr>
<tr>
    <td><CopyableCode code="disableShowmount" /></td>
    <td><code>boolean</code></td>
    <td>Shows the status of disableShowmount for all volumes under the subscription, null equals false.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption settings.</td>
</tr>
<tr>
    <td><CopyableCode code="entraIdConfig" /></td>
    <td><code>object</code></td>
    <td>Entra ID configuration for the account.</td>
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
    <td><CopyableCode code="ldapConfiguration" /></td>
    <td><code>object</code></td>
    <td>LDAP Configuration for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="multiAdStatus" /></td>
    <td><code>string</code></td>
    <td>MultiAD Status for the account. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nfsV4IDDomain" /></td>
    <td><code>string</code></td>
    <td>Domain for NFSv4 user ID mapping. This property will be set for all NetApp accounts in the subscription and region and only affect non ldap NFSv4 volumes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the NetApp account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List and describe all NetApp accounts in the resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List and describe all NetApp accounts in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified NetApp account within the resource group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the specified NetApp account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified NetApp account within the resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the specified NetApp account.</td>
</tr>
<tr>
    <td><a href="#get_change_key_vault_information"><CopyableCode code="get_change_key_vault_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Contains data from encryption.keyVaultProperties as well as information about which private endpoint is used by each encryption sibling set. Response from this endpoint can be modified and used as request body for POST request.</td>
</tr>
<tr>
    <td><a href="#renew_credentials"><CopyableCode code="renew_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Renew identity credentials that are used to authenticate to key vault, for customer-managed key encryption. If encryption.identity.principalId does not match identity.principalId, running this operation will fix it.</td>
</tr>
<tr>
    <td><a href="#transition_to_cmk"><CopyableCode code="transition_to_cmk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-virtualNetworkId"><code>virtualNetworkId</code></a>, <a href="#parameter-privateEndpointId"><code>privateEndpointId</code></a></td>
    <td></td>
    <td>Transitions all volumes in a VNet to a different encryption key source (Microsoft-managed key or Azure Key Vault). Operation fails if targeted volumes share encryption sibling set with volumes from another account.</td>
</tr>
<tr>
    <td><a href="#change_key_vault"><CopyableCode code="change_key_vault" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyVaultUri"><code>keyVaultUri</code></a>, <a href="#parameter-keyName"><code>keyName</code></a>, <a href="#parameter-keyVaultPrivateEndpoints"><code>keyVaultPrivateEndpoints</code></a></td>
    <td></td>
    <td>Affects existing volumes that are encrypted with Key Vault/Managed HSM, and new volumes. Supports HSM to Key Vault, Key Vault to HSM, HSM to HSM and Key Vault to Key Vault.</td>
</tr>
<tr>
    <td><a href="#refresh_ldap_bind_password"><CopyableCode code="refresh_ldap_bind_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refresh LDAP Bind DN password by fetching the latest password from Azure Key Vault.</td>
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
    <td>The name of the NetApp account. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get the NetApp account.

```sql
SELECT
id,
name,
activeDirectories,
disableShowmount,
encryption,
entraIdConfig,
etag,
identity,
ldapConfiguration,
location,
multiAdStatus,
nfsV4IDDomain,
provisioningState,
systemData,
tags,
type
FROM azure_isv.netapp.accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List and describe all NetApp accounts in the resource group.

```sql
SELECT
id,
name,
activeDirectories,
disableShowmount,
encryption,
entraIdConfig,
etag,
identity,
ldapConfiguration,
location,
multiAdStatus,
nfsV4IDDomain,
provisioningState,
systemData,
tags,
type
FROM azure_isv.netapp.accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List and describe all NetApp accounts in the subscription.

```sql
SELECT
id,
name,
activeDirectories,
disableShowmount,
encryption,
entraIdConfig,
etag,
identity,
ldapConfiguration,
location,
multiAdStatus,
nfsV4IDDomain,
provisioningState,
systemData,
tags,
type
FROM azure_isv.netapp.accounts
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

Create or update the specified NetApp account within the resource group.

```sql
INSERT INTO azure_isv.netapp.accounts (
tags,
location,
properties,
identity,
resource_group_name,
account_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ account_name }}',
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
- name: accounts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the accounts resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the accounts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the accounts resource.
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
        NetApp Account properties.
      value:
        provisioningState: "{{ provisioningState }}"
        activeDirectories:
          - activeDirectoryId: "{{ activeDirectoryId }}"
            username: "{{ username }}"
            password: "{{ password }}"
            domain: "{{ domain }}"
            dns: "{{ dns }}"
            status: "{{ status }}"
            statusDetails: "{{ statusDetails }}"
            smbServerName: "{{ smbServerName }}"
            organizationalUnit: "{{ organizationalUnit }}"
            site: "{{ site }}"
            backupOperators: "{{ backupOperators }}"
            administrators: "{{ administrators }}"
            kdcIP: "{{ kdcIP }}"
            adName: "{{ adName }}"
            serverRootCACertificate: "{{ serverRootCACertificate }}"
            aesEncryption: {{ aesEncryption }}
            ldapSigning: {{ ldapSigning }}
            securityOperators: "{{ securityOperators }}"
            ldapOverTLS: {{ ldapOverTLS }}
            allowLocalNfsUsersWithLdap: {{ allowLocalNfsUsersWithLdap }}
            encryptDCConnections: {{ encryptDCConnections }}
            ldapSearchScope:
              userDN: "{{ userDN }}"
              groupDN: "{{ groupDN }}"
              groupMembershipFilter: "{{ groupMembershipFilter }}"
            preferredServersForLdapClient: "{{ preferredServersForLdapClient }}"
        entraIdConfig:
          applicationId: "{{ applicationId }}"
          domain: "{{ domain }}"
          serverNamePrefix: "{{ serverNamePrefix }}"
          entraIdAkvConfig:
            azureKeyVaultUri: "{{ azureKeyVaultUri }}"
            certificateName: "{{ certificateName }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
        encryption:
          keySource: "{{ keySource }}"
          keyVaultProperties:
            keyVaultId: "{{ keyVaultId }}"
            keyVaultUri: "{{ keyVaultUri }}"
            keyName: "{{ keyName }}"
            keyVaultResourceId: "{{ keyVaultResourceId }}"
            status: "{{ status }}"
          identity:
            principalId: "{{ principalId }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
            federatedClientId: "{{ federatedClientId }}"
        disableShowmount: {{ disableShowmount }}
        nfsV4IDDomain: "{{ nfsV4IDDomain }}"
        multiAdStatus: "{{ multiAdStatus }}"
        ldapConfiguration:
          domain: "{{ domain }}"
          ldapServers:
            - "{{ ldapServers }}"
          ldapOverTLS: {{ ldapOverTLS }}
          serverCACertificate: "{{ serverCACertificate }}"
          certificateCNHost: "{{ certificateCNHost }}"
          bindAuthenticationLevel: "{{ bindAuthenticationLevel }}"
          bindDN: "{{ bindDN }}"
          bindPasswordAkvConfig:
            azureKeyVaultUri: "{{ azureKeyVaultUri }}"
            secretName: "{{ secretName }}"
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

Patch the specified NetApp account.

```sql
UPDATE azure_isv.netapp.accounts
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
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

Create or update the specified NetApp account within the resource group.

```sql
REPLACE azure_isv.netapp.accounts
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
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

Delete the specified NetApp account.

```sql
DELETE FROM azure_isv.netapp.accounts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_change_key_vault_information"
    values={[
        { label: 'get_change_key_vault_information', value: 'get_change_key_vault_information' },
        { label: 'renew_credentials', value: 'renew_credentials' },
        { label: 'transition_to_cmk', value: 'transition_to_cmk' },
        { label: 'change_key_vault', value: 'change_key_vault' },
        { label: 'refresh_ldap_bind_password', value: 'refresh_ldap_bind_password' }
    ]}
>
<TabItem value="get_change_key_vault_information">

Contains data from encryption.keyVaultProperties as well as information about which private endpoint is used by each encryption sibling set. Response from this endpoint can be modified and used as request body for POST request.

```sql
EXEC azure_isv.netapp.accounts.get_change_key_vault_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="renew_credentials">

Renew identity credentials that are used to authenticate to key vault, for customer-managed key encryption. If encryption.identity.principalId does not match identity.principalId, running this operation will fix it.

```sql
EXEC azure_isv.netapp.accounts.renew_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="transition_to_cmk">

Transitions all volumes in a VNet to a different encryption key source (Microsoft-managed key or Azure Key Vault). Operation fails if targeted volumes share encryption sibling set with volumes from another account.

```sql
EXEC azure_isv.netapp.accounts.transition_to_cmk 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"virtualNetworkId": "{{ virtualNetworkId }}", 
"privateEndpointId": "{{ privateEndpointId }}"
}'
;
```
</TabItem>
<TabItem value="change_key_vault">

Affects existing volumes that are encrypted with Key Vault/Managed HSM, and new volumes. Supports HSM to Key Vault, Key Vault to HSM, HSM to HSM and Key Vault to Key Vault.

```sql
EXEC azure_isv.netapp.accounts.change_key_vault 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyVaultUri": "{{ keyVaultUri }}", 
"keyName": "{{ keyName }}", 
"keyVaultResourceId": "{{ keyVaultResourceId }}", 
"keyVaultPrivateEndpoints": "{{ keyVaultPrivateEndpoints }}"
}'
;
```
</TabItem>
<TabItem value="refresh_ldap_bind_password">

Refresh LDAP Bind DN password by fetching the latest password from Azure Key Vault.

```sql
EXEC azure_isv.netapp.accounts.refresh_ldap_bind_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
