--- 
title: managed_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments
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

Creates, updates, deletes, gets or lists a <code>managed_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app.managed_environments" /></td></tr>
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
    <td><CopyableCode code="appLogsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which enables the log daemon to export app logs to a destination. Currently only "log-analytics" is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIInstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDomain" /></td>
    <td><code>string</code></td>
    <td>Default Domain Name for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Required. The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Environment. Possible values include: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", "ScheduledForDelete", "UpgradeRequested", "UpgradeFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the Environment.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vnetConfiguration" /></td>
    <td><code>object</code></td>
    <td>Vnet configuration for the environment.</td>
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
    <td>Get the properties of a Managed Environment. Get the properties of a Managed Environment used to host container apps.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Get all Environments for a subscription. Get all Managed Environments for a subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Get all the Environments in a resource group. Get all the Managed Environments in a resource group.</td>
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

Get the properties of a Managed Environment. Get the properties of a Managed Environment used to host container apps.

```sql
SELECT
id,
name,
appLogsConfiguration,
daprAIInstrumentationKey,
defaultDomain,
deploymentErrors,
location,
provisioningState,
staticIp,
systemData,
tags,
type,
vnetConfiguration
FROM azure.app.managed_environments
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_subscription"
    values={[
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
    ]}
>
<TabItem value="list_by_subscription">

Get all Environments for a subscription. Get all Managed Environments for a subscription.

```sql
EXEC azure.app.managed_environments.list_by_subscription 

;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all the Environments in a resource group. Get all the Managed Environments in a resource group.

```sql
EXEC azure.app.managed_environments.list_by_resource_group 

;
```
</TabItem>
</Tabs>
