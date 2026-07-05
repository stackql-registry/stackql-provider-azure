--- 
title: container_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps
  - appcontainers
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.container_apps" /></td></tr>
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
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of environment.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the container app.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The complex type of the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>managed identities for the Container App to interact with other Azure services without maintaining any secrets or credentials in code.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata to represent the container app kind, representing if a container app is workflowapp or functionapp. Known values are: "workflowapp" and "functionapp". (workflowapp, functionapp)</td>
</tr>
<tr>
    <td><CopyableCode code="latestReadyRevisionName" /></td>
    <td><code>string</code></td>
    <td>Name of the latest ready revision of the Container App.</td>
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
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Deprecated. Resource ID of the Container App's environment.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound IP Addresses for container app.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Container App. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="runningStatus" /></td>
    <td><code>string</code></td>
    <td>Running status of the Container App. Known values are: "Progressing", "Running", "Stopped", "Suspended", and "Ready". (Progressing, Running, Stopped, Suspended, Ready)</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container App versioned application definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name to pin for container app execution.</td>
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
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of environment.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the container app.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The complex type of the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>managed identities for the Container App to interact with other Azure services without maintaining any secrets or credentials in code.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata to represent the container app kind, representing if a container app is workflowapp or functionapp. Known values are: "workflowapp" and "functionapp". (workflowapp, functionapp)</td>
</tr>
<tr>
    <td><CopyableCode code="latestReadyRevisionName" /></td>
    <td><code>string</code></td>
    <td>Name of the latest ready revision of the Container App.</td>
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
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Deprecated. Resource ID of the Container App's environment.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound IP Addresses for container app.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Container App. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="runningStatus" /></td>
    <td><code>string</code></td>
    <td>Running status of the Container App. Known values are: "Progressing", "Running", "Stopped", "Suspended", and "Ready". (Progressing, Running, Stopped, Suspended, Ready)</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container App versioned application definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name to pin for container app execution.</td>
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
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of environment.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the container app.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The complex type of the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>managed identities for the Container App to interact with other Azure services without maintaining any secrets or credentials in code.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata to represent the container app kind, representing if a container app is workflowapp or functionapp. Known values are: "workflowapp" and "functionapp". (workflowapp, functionapp)</td>
</tr>
<tr>
    <td><CopyableCode code="latestReadyRevisionName" /></td>
    <td><code>string</code></td>
    <td>Name of the latest ready revision of the Container App.</td>
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
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Deprecated. Resource ID of the Container App's environment.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound IP Addresses for container app.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Container App. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="runningStatus" /></td>
    <td><code>string</code></td>
    <td>Running status of the Container App. Known values are: "Progressing", "Running", "Stopped", "Suspended", and "Ready". (Progressing, Running, Stopped, Suspended, Ready)</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container App versioned application definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name to pin for container app execution.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a Container App. Get the properties of a Container App.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Container Apps in a given resource group. Get the Container Apps in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Container Apps in a given subscription. Get the Container Apps in a given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a Container App. Create or update a Container App.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Update properties of a Container App. Patches a Container App using JSON Merge Patch.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a Container App. Create or update a Container App.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Container App. Delete a Container App.</td>
</tr>
<tr>
    <td><a href="#list_custom_host_name_analysis"><CopyableCode code="list_custom_host_name_analysis" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-customHostname"><code>customHostname</code></a></td>
    <td>Analyzes a custom hostname for a Container App. Analyzes a custom hostname for a Container App.</td>
</tr>
<tr>
    <td><a href="#list_secrets"><CopyableCode code="list_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List secrets for a container app. List secrets for a container app.</td>
</tr>
<tr>
    <td><a href="#get_auth_token"><CopyableCode code="get_auth_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get auth token for a container app. Get auth token for a container app.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start a container app. Start a container app.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop a container app. Stop a container app.</td>
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
<tr id="parameter-container_app_name">
    <td><CopyableCode code="container_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App. Required.</td>
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
<tr id="parameter-customHostname">
    <td><CopyableCode code="customHostname" /></td>
    <td><code>string</code></td>
    <td>Custom hostname. Default value is None.</td>
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

Get the properties of a Container App. Get the properties of a Container App.

```sql
SELECT
id,
name,
configuration,
customDomainVerificationId,
environmentId,
eventStreamEndpoint,
extendedLocation,
identity,
kind,
latestReadyRevisionName,
latestRevisionFqdn,
latestRevisionName,
location,
managedBy,
managedEnvironmentId,
outboundIpAddresses,
provisioningState,
runningStatus,
systemData,
tags,
template,
type,
workloadProfileName
FROM azure.appcontainers.container_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get the Container Apps in a given resource group. Get the Container Apps in a given resource group.

```sql
SELECT
id,
name,
configuration,
customDomainVerificationId,
environmentId,
eventStreamEndpoint,
extendedLocation,
identity,
kind,
latestReadyRevisionName,
latestRevisionFqdn,
latestRevisionName,
location,
managedBy,
managedEnvironmentId,
outboundIpAddresses,
provisioningState,
runningStatus,
systemData,
tags,
template,
type,
workloadProfileName
FROM azure.appcontainers.container_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get the Container Apps in a given subscription. Get the Container Apps in a given subscription.

```sql
SELECT
id,
name,
configuration,
customDomainVerificationId,
environmentId,
eventStreamEndpoint,
extendedLocation,
identity,
kind,
latestReadyRevisionName,
latestRevisionFqdn,
latestRevisionName,
location,
managedBy,
managedEnvironmentId,
outboundIpAddresses,
provisioningState,
runningStatus,
systemData,
tags,
template,
type,
workloadProfileName
FROM azure.appcontainers.container_apps
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

Create or update a Container App. Create or update a Container App.

```sql
INSERT INTO azure.appcontainers.container_apps (
tags,
location,
properties,
extendedLocation,
identity,
managedBy,
kind,
resource_group_name,
container_app_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}',
'{{ identity }}',
'{{ managedBy }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ container_app_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: container_apps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the container_apps resource.
    - name: container_app_name
      value: "{{ container_app_name }}"
      description: Required parameter for the container_apps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the container_apps resource.
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
        ContainerApp resource specific properties.
      value:
        provisioningState: "{{ provisioningState }}"
        runningStatus: "{{ runningStatus }}"
        managedEnvironmentId: "{{ managedEnvironmentId }}"
        environmentId: "{{ environmentId }}"
        workloadProfileName: "{{ workloadProfileName }}"
        latestRevisionName: "{{ latestRevisionName }}"
        latestReadyRevisionName: "{{ latestReadyRevisionName }}"
        latestRevisionFqdn: "{{ latestRevisionFqdn }}"
        customDomainVerificationId: "{{ customDomainVerificationId }}"
        configuration:
          secrets:
            - name: "{{ name }}"
              value: "{{ value }}"
              identity: "{{ identity }}"
              keyVaultUrl: "{{ keyVaultUrl }}"
          activeRevisionsMode: "{{ activeRevisionsMode }}"
          ingress:
            fqdn: "{{ fqdn }}"
            external: {{ external }}
            targetPort: {{ targetPort }}
            exposedPort: {{ exposedPort }}
            transport: "{{ transport }}"
            traffic:
              - revisionName: "{{ revisionName }}"
                weight: {{ weight }}
                latestRevision: {{ latestRevision }}
                label: "{{ label }}"
            customDomains:
              - name: "{{ name }}"
                bindingType: "{{ bindingType }}"
                certificateId: "{{ certificateId }}"
            allowInsecure: {{ allowInsecure }}
            ipSecurityRestrictions:
              - name: "{{ name }}"
                description: "{{ description }}"
                ipAddressRange: "{{ ipAddressRange }}"
                action: "{{ action }}"
            stickySessions:
              affinity: "{{ affinity }}"
            clientCertificateMode: "{{ clientCertificateMode }}"
            corsPolicy:
              allowedOrigins:
                - "{{ allowedOrigins }}"
              allowedMethods:
                - "{{ allowedMethods }}"
              allowedHeaders:
                - "{{ allowedHeaders }}"
              exposeHeaders:
                - "{{ exposeHeaders }}"
              maxAge: {{ maxAge }}
              allowCredentials: {{ allowCredentials }}
            additionalPortMappings:
              - external: {{ external }}
                targetPort: {{ targetPort }}
                exposedPort: {{ exposedPort }}
          registries:
            - server: "{{ server }}"
              username: "{{ username }}"
              passwordSecretRef: "{{ passwordSecretRef }}"
              identity: "{{ identity }}"
          dapr:
            enabled: {{ enabled }}
            appId: "{{ appId }}"
            appProtocol: "{{ appProtocol }}"
            appPort: {{ appPort }}
            httpReadBufferSize: {{ httpReadBufferSize }}
            httpMaxRequestSize: {{ httpMaxRequestSize }}
            logLevel: "{{ logLevel }}"
            enableApiLogging: {{ enableApiLogging }}
            appHealth:
              enabled: {{ enabled }}
              path: "{{ path }}"
              probeIntervalSeconds: {{ probeIntervalSeconds }}
              probeTimeoutMilliseconds: {{ probeTimeoutMilliseconds }}
              threshold: {{ threshold }}
            maxConcurrency: {{ maxConcurrency }}
          runtime:
            java:
              enableMetrics: {{ enableMetrics }}
          maxInactiveRevisions: {{ maxInactiveRevisions }}
          service:
            type: "{{ type }}"
          identitySettings:
            - identity: "{{ identity }}"
              lifecycle: "{{ lifecycle }}"
        template:
          revisionSuffix: "{{ revisionSuffix }}"
          terminationGracePeriodSeconds: {{ terminationGracePeriodSeconds }}
          initContainers:
            - image: "{{ image }}"
              name: "{{ name }}"
              command: "{{ command }}"
              args: "{{ args }}"
              env: "{{ env }}"
              resources:
                cpu: {{ cpu }}
                memory: "{{ memory }}"
                ephemeralStorage: "{{ ephemeralStorage }}"
              volumeMounts: "{{ volumeMounts }}"
          containers:
            - image: "{{ image }}"
              name: "{{ name }}"
              command: "{{ command }}"
              args: "{{ args }}"
              env: "{{ env }}"
              resources:
                cpu: {{ cpu }}
                memory: "{{ memory }}"
                ephemeralStorage: "{{ ephemeralStorage }}"
              volumeMounts: "{{ volumeMounts }}"
              probes: "{{ probes }}"
          scale:
            minReplicas: {{ minReplicas }}
            maxReplicas: {{ maxReplicas }}
            cooldownPeriod: {{ cooldownPeriod }}
            pollingInterval: {{ pollingInterval }}
            rules:
              - name: "{{ name }}"
                azureQueue:
                  accountName: "{{ accountName }}"
                  queueName: "{{ queueName }}"
                  queueLength: {{ queueLength }}
                  auth: "{{ auth }}"
                  identity: "{{ identity }}"
                custom:
                  type: "{{ type }}"
                  metadata: "{{ metadata }}"
                  auth: "{{ auth }}"
                  identity: "{{ identity }}"
                http:
                  metadata: "{{ metadata }}"
                  auth: "{{ auth }}"
                  identity: "{{ identity }}"
                tcp:
                  metadata: "{{ metadata }}"
                  auth: "{{ auth }}"
                  identity: "{{ identity }}"
          volumes:
            - name: "{{ name }}"
              storageType: "{{ storageType }}"
              storageName: "{{ storageName }}"
              secrets: "{{ secrets }}"
              mountOptions: "{{ mountOptions }}"
          serviceBinds:
            - serviceId: "{{ serviceId }}"
              name: "{{ name }}"
        outboundIpAddresses:
          - "{{ outboundIpAddresses }}"
        eventStreamEndpoint: "{{ eventStreamEndpoint }}"
    - name: extendedLocation
      description: |
        The complex type of the extended location.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: identity
      description: |
        managed identities for the Container App to interact with other Azure services without maintaining any secrets or credentials in code.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata to represent the container app kind, representing if a container app is workflowapp or functionapp. Known values are: "workflowapp" and "functionapp".
      valid_values: ['workflowapp', 'functionapp']
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

Update properties of a Container App. Patches a Container App using JSON Merge Patch.

```sql
UPDATE azure.appcontainers.container_apps
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}',
managedBy = '{{ managedBy }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
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

Create or update a Container App. Create or update a Container App.

```sql
REPLACE azure.appcontainers.container_apps
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}',
managedBy = '{{ managedBy }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
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

Delete a Container App. Delete a Container App.

```sql
DELETE FROM azure.appcontainers.container_apps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_custom_host_name_analysis"
    values={[
        { label: 'list_custom_host_name_analysis', value: 'list_custom_host_name_analysis' },
        { label: 'list_secrets', value: 'list_secrets' },
        { label: 'get_auth_token', value: 'get_auth_token' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="list_custom_host_name_analysis">

Analyzes a custom hostname for a Container App. Analyzes a custom hostname for a Container App.

```sql
EXEC azure.appcontainers.container_apps.list_custom_host_name_analysis 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@customHostname='{{ customHostname }}'
;
```
</TabItem>
<TabItem value="list_secrets">

List secrets for a container app. List secrets for a container app.

```sql
EXEC azure.appcontainers.container_apps.list_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_auth_token">

Get auth token for a container app. Get auth token for a container app.

```sql
EXEC azure.appcontainers.container_apps.get_auth_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start a container app. Start a container app.

```sql
EXEC azure.appcontainers.container_apps.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop a container app. Stop a container app.

```sql
EXEC azure.appcontainers.container_apps.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
