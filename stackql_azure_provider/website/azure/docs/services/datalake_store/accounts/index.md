--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - datalake_store
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

Creates, updates, deletes, gets or lists an <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datalake_store.accounts" /></td></tr>
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
    <td>The resource identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier associated with this Data Lake Store account.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The account creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="currentTier" /></td>
    <td><code>string</code></td>
    <td>The commitment tier in use for the current month. Known values are: "Consumption", "Commitment_1TB", "Commitment_10TB", "Commitment_100TB", "Commitment_500TB", "Commitment_1PB", and "Commitment_5PB".</td>
</tr>
<tr>
    <td><CopyableCode code="defaultGroup" /></td>
    <td><code>string</code></td>
    <td>The default owner group for all new folders and files created in the Data Lake Store account.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionConfig" /></td>
    <td><code>object</code></td>
    <td>The Key Vault encryption configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of encryption provisioning for this Data Lake Store account. Known values are: "Creating" and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionState" /></td>
    <td><code>string</code></td>
    <td>The current state of encryption for this Data Lake Store account. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The full CName endpoint for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallAllowAzureIps" /></td>
    <td><code>string</code></td>
    <td>The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="firewallRules" /></td>
    <td><code>array</code></td>
    <td>The list of firewall rules associated with this Data Lake Store account.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallState" /></td>
    <td><code>string</code></td>
    <td>The current state of the IP address firewall for this Data Lake Store account. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Key Vault encryption identity, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The account last modified time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="newTier" /></td>
    <td><code>string</code></td>
    <td>The commitment tier to use for next month. Known values are: "Consumption", "Commitment_1TB", "Commitment_10TB", "Commitment_100TB", "Commitment_500TB", "Commitment_1PB", and "Commitment_5PB".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the Data Lake Store account. Known values are: "Failed", "Creating", "Running", "Succeeded", "Patching", "Suspending", "Resuming", "Deleting", "Deleted", "Undeleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the Data Lake Store account. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedIdProviderState" /></td>
    <td><code>string</code></td>
    <td>The current state of the trusted identity provider feature for this Data Lake Store account. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="trustedIdProviders" /></td>
    <td><code>array</code></td>
    <td>The list of trusted identity providers associated with this Data Lake Store account.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkRules" /></td>
    <td><code>array</code></td>
    <td>The list of virtual network rules associated with this Data Lake Store account.</td>
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
    <td>The resource identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier associated with this Data Lake Store account.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The account creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The full CName endpoint for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The account last modified time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the Data Lake Store account. Known values are: "Failed", "Creating", "Running", "Succeeded", "Patching", "Suspending", "Resuming", "Deleting", "Deleted", "Undeleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the Data Lake Store account. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td>The resource identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier associated with this Data Lake Store account.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The account creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The full CName endpoint for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The account last modified time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the Data Lake Store account. Known values are: "Failed", "Creating", "Running", "Succeeded", "Patching", "Suspending", "Resuming", "Deleting", "Deleted", "Undeleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the Data Lake Store account. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td>Gets the specified Data Lake Store account.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$count"><code>$count</code></a></td>
    <td>Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$count"><code>$count</code></a></td>
    <td>Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates the specified Data Lake Store account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specified Data Lake Store account information.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Data Lake Store account.</td>
</tr>
<tr>
    <td><a href="#enable_key_vault"><CopyableCode code="enable_key_vault" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Checks whether the specified account name is available or taken.</td>
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
    <td>The name of the Data Lake Store account. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location without whitespace. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$count">
    <td><CopyableCode code="$count" /></td>
    <td><code>boolean</code></td>
    <td>The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>OrderBy clause. One or more comma-separated expressions with an optional "asc" (the default) or "desc" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of items to skip over before returning elements. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of items to return. Optional. Default value is None.</td>
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

Gets the specified Data Lake Store account.

```sql
SELECT
id,
name,
accountId,
creationTime,
currentTier,
defaultGroup,
encryptionConfig,
encryptionProvisioningState,
encryptionState,
endpoint,
firewallAllowAzureIps,
firewallRules,
firewallState,
identity,
lastModifiedTime,
location,
newTier,
provisioningState,
state,
tags,
trustedIdProviderState,
trustedIdProviders,
type,
virtualNetworkRules
FROM azure.datalake_store.accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any.

```sql
SELECT
id,
name,
accountId,
creationTime,
endpoint,
lastModifiedTime,
location,
provisioningState,
state,
tags,
type
FROM azure.datalake_store.accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $select = '{{ $select }}'
AND $orderby = '{{ $orderby }}'
AND $count = '{{ $count }}'
;
```
</TabItem>
<TabItem value="list">

Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any.

```sql
SELECT
id,
name,
accountId,
creationTime,
endpoint,
lastModifiedTime,
location,
provisioningState,
state,
tags,
type
FROM azure.datalake_store.accounts
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $select = '{{ $select }}'
AND $orderby = '{{ $orderby }}'
AND $count = '{{ $count }}'
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

Creates the specified Data Lake Store account.

```sql
INSERT INTO azure.datalake_store.accounts (
location,
tags,
identity,
properties,
resource_group_name,
account_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
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
    - name: location
      value: "{{ location }}"
      description: |
        The resource location. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: identity
      description: |
        The Key Vault encryption identity, if any.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
    - name: properties
      value:
        defaultGroup: "{{ defaultGroup }}"
        encryptionConfig:
          type: "{{ type }}"
          keyVaultMetaInfo:
            keyVaultResourceId: "{{ keyVaultResourceId }}"
            encryptionKeyName: "{{ encryptionKeyName }}"
            encryptionKeyVersion: "{{ encryptionKeyVersion }}"
        encryptionState: "{{ encryptionState }}"
        firewallRules:
          - name: "{{ name }}"
            properties:
              startIpAddress: "{{ startIpAddress }}"
              endIpAddress: "{{ endIpAddress }}"
        virtualNetworkRules:
          - name: "{{ name }}"
            properties:
              subnetId: "{{ subnetId }}"
        firewallState: "{{ firewallState }}"
        firewallAllowAzureIps: "{{ firewallAllowAzureIps }}"
        trustedIdProviders:
          - name: "{{ name }}"
            properties:
              idProvider: "{{ idProvider }}"
        trustedIdProviderState: "{{ trustedIdProviderState }}"
        newTier: "{{ newTier }}"
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

Updates the specified Data Lake Store account information.

```sql
UPDATE azure.datalake_store.accounts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
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

Deletes the specified Data Lake Store account.

```sql
DELETE FROM azure.datalake_store.accounts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="enable_key_vault"
    values={[
        { label: 'enable_key_vault', value: 'enable_key_vault' },
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="enable_key_vault">

Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account.

```sql
EXEC azure.datalake_store.accounts.enable_key_vault 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks whether the specified account name is available or taken.

```sql
EXEC azure.datalake_store.accounts.check_name_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
