--- 
title: container_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps
  - app
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

Creates, updates, deletes, gets or lists a <code>container_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app.container_apps" /></td></tr>
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
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>Non versioned Container App configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomainVerificationId" /></td>
    <td><code>string</code></td>
    <td>Id used to verify domain name ownership.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>managed identities for the Container App to interact with other Azure services without maintaining any secrets or credentials in code.</td>
</tr>
<tr>
    <td><CopyableCode code="latestRevisionFqdn" /></td>
    <td><code>string</code></td>
    <td>Fully Qualified Domain Name of the latest revision of the Container App.</td>
</tr>
<tr>
    <td><CopyableCode code="latestRevisionName" /></td>
    <td><code>string</code></td>
    <td>Name of the latest revision of the Container App.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Required. The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="managedEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Container App's environment.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound IP Addresses for container app.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Container App. Possible values include: "InProgress", "Succeeded", "Failed", "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>A set of tags. Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container App versioned application definition.</td>
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
    <td></td>
    <td></td>
    <td>Get the properties of a Container App. Get the properties of a Container App.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Get the Container Apps in a given subscription. Get the Container Apps in a given subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Get the Container Apps in a given resource group. Get the Container Apps in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list_custom_host_name_analysis"><CopyableCode code="list_custom_host_name_analysis" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Analyzes a custom hostname for a Container App. Analyzes a custom hostname for a Container App.</td>
</tr>
<tr>
    <td><a href="#list_secrets"><CopyableCode code="list_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>List secrets for a container app. List secrets for a container app.</td>
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

Get the properties of a Container App. Get the properties of a Container App.

```sql
SELECT
id,
name,
configuration,
customDomainVerificationId,
identity,
latestRevisionFqdn,
latestRevisionName,
location,
managedEnvironmentId,
outboundIPAddresses,
provisioningState,
systemData,
tags,
template,
type
FROM azure.app.container_apps
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_subscription"
    values={[
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_custom_host_name_analysis', value: 'list_custom_host_name_analysis' },
        { label: 'list_secrets', value: 'list_secrets' }
    ]}
>
<TabItem value="list_by_subscription">

Get the Container Apps in a given subscription. Get the Container Apps in a given subscription.

```sql
EXEC azure.app.container_apps.list_by_subscription 

;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get the Container Apps in a given resource group. Get the Container Apps in a given resource group.

```sql
EXEC azure.app.container_apps.list_by_resource_group 

;
```
</TabItem>
<TabItem value="list_custom_host_name_analysis">

Analyzes a custom hostname for a Container App. Analyzes a custom hostname for a Container App.

```sql
EXEC azure.app.container_apps.list_custom_host_name_analysis 

;
```
</TabItem>
<TabItem value="list_secrets">

List secrets for a container app. List secrets for a container app.

```sql
EXEC azure.app.container_apps.list_secrets 

;
```
</TabItem>
</Tabs>
