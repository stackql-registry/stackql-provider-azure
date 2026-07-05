--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - datalake_analytics
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datalake_analytics.accounts" /></td></tr>
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
    <td>The unique identifier associated with this Data Lake Analytics account.</td>
</tr>
<tr>
    <td><CopyableCode code="computePolicies" /></td>
    <td><code>array</code></td>
    <td>The list of compute policies associated with this account.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The account creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="currentTier" /></td>
    <td><code>string</code></td>
    <td>The commitment tier in use for the current month. Known values are: "Consumption", "Commitment_100AUHours", "Commitment_500AUHours", "Commitment_1000AUHours", "Commitment_5000AUHours", "Commitment_10000AUHours", "Commitment_50000AUHours", "Commitment_100000AUHours", and "Commitment_500000AUHours".</td>
</tr>
<tr>
    <td><CopyableCode code="dataLakeStoreAccounts" /></td>
    <td><code>array</code></td>
    <td>The list of Data Lake Store accounts associated with this account.</td>
</tr>
<tr>
    <td><CopyableCode code="debugDataAccessLevel" /></td>
    <td><code>string</code></td>
    <td>The current state of the DebugDataAccessLevel for this account. Known values are: "All", "Customer", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDataLakeStoreAccount" /></td>
    <td><code>string</code></td>
    <td>The default Data Lake Store account associated with this account.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDataLakeStoreAccountType" /></td>
    <td><code>string</code></td>
    <td>The type of the default Data Lake Store account associated with this account.</td>
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
    <td>The list of firewall rules associated with this account.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallState" /></td>
    <td><code>string</code></td>
    <td>The current state of the IP address firewall for this account. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="hiveMetastores" /></td>
    <td><code>array</code></td>
    <td>The list of hiveMetastores associated with this account.</td>
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
    <td><CopyableCode code="maxActiveJobCountPerUser" /></td>
    <td><code>integer</code></td>
    <td>The maximum supported active jobs under the account at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDegreeOfParallelism" /></td>
    <td><code>integer</code></td>
    <td>The maximum supported degree of parallelism for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDegreeOfParallelismPerJob" /></td>
    <td><code>integer</code></td>
    <td>The maximum supported degree of parallelism per job for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="maxJobCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum supported jobs running under the account at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="maxJobRunningTimeInMin" /></td>
    <td><code>integer</code></td>
    <td>The maximum supported active jobs under the account at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="maxQueuedJobCountPerUser" /></td>
    <td><code>integer</code></td>
    <td>The maximum supported jobs queued under the account at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="minPriorityPerJob" /></td>
    <td><code>integer</code></td>
    <td>The minimum supported priority per job for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="newTier" /></td>
    <td><code>string</code></td>
    <td>The commitment tier for the next month. Known values are: "Consumption", "Commitment_100AUHours", "Commitment_500AUHours", "Commitment_1000AUHours", "Commitment_5000AUHours", "Commitment_10000AUHours", "Commitment_50000AUHours", "Commitment_100000AUHours", and "Commitment_500000AUHours".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the Data Lake Analytics account. Known values are: "Failed", "Creating", "Running", "Succeeded", "Patching", "Suspending", "Resuming", "Deleting", "Deleted", "Undeleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="publicDataLakeStoreAccounts" /></td>
    <td><code>array</code></td>
    <td>The list of Data Lake Store accounts associated with this account.</td>
</tr>
<tr>
    <td><CopyableCode code="queryStoreRetention" /></td>
    <td><code>integer</code></td>
    <td>The number of days that job metadata is retained.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the Data Lake Analytics account. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccounts" /></td>
    <td><code>array</code></td>
    <td>The list of Azure Blob Storage accounts associated with this account.</td>
</tr>
<tr>
    <td><CopyableCode code="systemMaxDegreeOfParallelism" /></td>
    <td><code>integer</code></td>
    <td>The system defined maximum supported degree of parallelism for this account, which restricts the maximum value of parallelism the user can set for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="systemMaxJobCount" /></td>
    <td><code>integer</code></td>
    <td>The system defined maximum supported jobs running under the account at the same time, which restricts the maximum number of running jobs the user can set for the account.</td>
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
<tr>
    <td><CopyableCode code="virtualNetworkRules" /></td>
    <td><code>array</code></td>
    <td>The list of virtualNetwork rules associated with this account.</td>
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
    <td>The unique identifier associated with this Data Lake Analytics account.</td>
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
    <td>The provisioning status of the Data Lake Analytics account. Known values are: "Failed", "Creating", "Running", "Succeeded", "Patching", "Suspending", "Resuming", "Deleting", "Deleted", "Undeleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the Data Lake Analytics account. Known values are: "Active" and "Suspended".</td>
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
    <td>The unique identifier associated with this Data Lake Analytics account.</td>
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
    <td>The provisioning status of the Data Lake Analytics account. Known values are: "Failed", "Creating", "Running", "Succeeded", "Patching", "Suspending", "Resuming", "Deleting", "Deleted", "Undeleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the Data Lake Analytics account. Known values are: "Active" and "Suspended".</td>
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
    <td>Gets details of the specified Data Lake Analytics account.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$count"><code>$count</code></a></td>
    <td>Gets the first page of Data Lake Analytics accounts, if any, within a specific resource group. This includes a link to the next page, if any.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$count"><code>$count</code></a></td>
    <td>Gets the first page of Data Lake Analytics accounts, if any, within the current subscription. This includes a link to the next page, if any.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates the specified Data Lake Analytics account. This supplies the user with computation services for Data Lake Analytics workloads.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Data Lake Analytics account object specified by the accountName with the contents of the account object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Begins the delete process for the Data Lake Analytics account object specified by the account name.</td>
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
    <td>The name of the Data Lake Analytics account. Required.</td>
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

Gets details of the specified Data Lake Analytics account.

```sql
SELECT
id,
name,
accountId,
computePolicies,
creationTime,
currentTier,
dataLakeStoreAccounts,
debugDataAccessLevel,
defaultDataLakeStoreAccount,
defaultDataLakeStoreAccountType,
endpoint,
firewallAllowAzureIps,
firewallRules,
firewallState,
hiveMetastores,
lastModifiedTime,
location,
maxActiveJobCountPerUser,
maxDegreeOfParallelism,
maxDegreeOfParallelismPerJob,
maxJobCount,
maxJobRunningTimeInMin,
maxQueuedJobCountPerUser,
minPriorityPerJob,
newTier,
provisioningState,
publicDataLakeStoreAccounts,
queryStoreRetention,
state,
storageAccounts,
systemMaxDegreeOfParallelism,
systemMaxJobCount,
tags,
type,
virtualNetworkRules
FROM azure.datalake_analytics.accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets the first page of Data Lake Analytics accounts, if any, within a specific resource group. This includes a link to the next page, if any.

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
FROM azure.datalake_analytics.accounts
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

Gets the first page of Data Lake Analytics accounts, if any, within the current subscription. This includes a link to the next page, if any.

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
FROM azure.datalake_analytics.accounts
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

Creates the specified Data Lake Analytics account. This supplies the user with computation services for Data Lake Analytics workloads.

```sql
INSERT INTO azure.datalake_analytics.accounts (
location,
tags,
properties,
resource_group_name,
account_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
    - name: properties
      value:
        defaultDataLakeStoreAccount: "{{ defaultDataLakeStoreAccount }}"
        dataLakeStoreAccounts:
          - name: "{{ name }}"
            properties:
              suffix: "{{ suffix }}"
        storageAccounts:
          - name: "{{ name }}"
            properties:
              accessKey: "{{ accessKey }}"
              suffix: "{{ suffix }}"
        computePolicies:
          - name: "{{ name }}"
            properties:
              objectId: "{{ objectId }}"
              objectType: "{{ objectType }}"
              maxDegreeOfParallelismPerJob: {{ maxDegreeOfParallelismPerJob }}
              minPriorityPerJob: {{ minPriorityPerJob }}
        firewallRules:
          - name: "{{ name }}"
            properties:
              startIpAddress: "{{ startIpAddress }}"
              endIpAddress: "{{ endIpAddress }}"
        firewallState: "{{ firewallState }}"
        firewallAllowAzureIps: "{{ firewallAllowAzureIps }}"
        newTier: "{{ newTier }}"
        maxJobCount: {{ maxJobCount }}
        maxDegreeOfParallelism: {{ maxDegreeOfParallelism }}
        maxDegreeOfParallelismPerJob: {{ maxDegreeOfParallelismPerJob }}
        minPriorityPerJob: {{ minPriorityPerJob }}
        queryStoreRetention: {{ queryStoreRetention }}
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

Updates the Data Lake Analytics account object specified by the accountName with the contents of the account object.

```sql
UPDATE azure.datalake_analytics.accounts
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

Begins the delete process for the Data Lake Analytics account object specified by the account name.

```sql
DELETE FROM azure.datalake_analytics.accounts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="check_name_availability">

Checks whether the specified account name is available or taken.

```sql
EXEC azure.datalake_analytics.accounts.check_name_availability 
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
