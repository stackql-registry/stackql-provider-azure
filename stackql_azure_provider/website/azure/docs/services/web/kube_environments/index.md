--- 
title: kube_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - kube_environments
  - web
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

Creates, updates, deletes, gets or lists a <code>kube_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kube_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.kube_environments" /></td></tr>
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
    <td><CopyableCode code="aksResourceID" /></td>
    <td><code>string</code></td>
    <td>:vartype aks_resource_id: str</td>
</tr>
<tr>
    <td><CopyableCode code="appLogsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which enables the log daemon to export app logs to a destination. Currently only "log-analytics" is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="arcConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which determines the ARC cluster components types. Eg: Choosing between BuildService kind, FrontEnd Service ArtifactsStorageType etc.</td>
</tr>
<tr>
    <td><CopyableCode code="containerAppsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration.</td>
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
    <td><CopyableCode code="environmentType" /></td>
    <td><code>string</code></td>
    <td>Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="internalLoadBalancerEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Only visible within Vnet/Subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Kubernetes Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", "ScheduledForDelete", "UpgradeRequested", and "UpgradeFailed". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete, UpgradeRequested, UpgradeFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the KubeEnvironment.</td>
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
    <td><CopyableCode code="aksResourceID" /></td>
    <td><code>string</code></td>
    <td>:vartype aks_resource_id: str</td>
</tr>
<tr>
    <td><CopyableCode code="appLogsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which enables the log daemon to export app logs to a destination. Currently only "log-analytics" is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="arcConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which determines the ARC cluster components types. Eg: Choosing between BuildService kind, FrontEnd Service ArtifactsStorageType etc.</td>
</tr>
<tr>
    <td><CopyableCode code="containerAppsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration.</td>
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
    <td><CopyableCode code="environmentType" /></td>
    <td><code>string</code></td>
    <td>Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="internalLoadBalancerEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Only visible within Vnet/Subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Kubernetes Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", "ScheduledForDelete", "UpgradeRequested", and "UpgradeFailed". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete, UpgradeRequested, UpgradeFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the KubeEnvironment.</td>
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
    <td><CopyableCode code="aksResourceID" /></td>
    <td><code>string</code></td>
    <td>:vartype aks_resource_id: str</td>
</tr>
<tr>
    <td><CopyableCode code="appLogsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which enables the log daemon to export app logs to a destination. Currently only "log-analytics" is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="arcConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which determines the ARC cluster components types. Eg: Choosing between BuildService kind, FrontEnd Service ArtifactsStorageType etc.</td>
</tr>
<tr>
    <td><CopyableCode code="containerAppsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration.</td>
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
    <td><CopyableCode code="environmentType" /></td>
    <td><code>string</code></td>
    <td>Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="internalLoadBalancerEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Only visible within Vnet/Subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Kubernetes Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", "ScheduledForDelete", "UpgradeRequested", and "UpgradeFailed". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete, UpgradeRequested, UpgradeFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the KubeEnvironment.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a Kubernetes Environment. Description for Get the properties of a Kubernetes Environment.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all the Kubernetes Environments in a resource group. Description for Get all the Kubernetes Environments in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Kubernetes Environments for a subscription. Description for Get all Kubernetes Environments for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Kubernetes Environment. Description for Creates or updates a Kubernetes Environment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Kubernetes Environment. Description for Creates or updates a Kubernetes Environment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Kubernetes Environment. Description for Creates or updates a Kubernetes Environment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Kubernetes Environment. Description for Delete a Kubernetes Environment.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the Kubernetes Environment. Required.</td>
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

Get the properties of a Kubernetes Environment. Description for Get the properties of a Kubernetes Environment.

```sql
SELECT
id,
name,
aksResourceID,
appLogsConfiguration,
arcConfiguration,
containerAppsConfiguration,
defaultDomain,
deploymentErrors,
environmentType,
extendedLocation,
internalLoadBalancerEnabled,
kind,
location,
provisioningState,
staticIp,
systemData,
tags,
type
FROM azure.web.kube_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all the Kubernetes Environments in a resource group. Description for Get all the Kubernetes Environments in a resource group.

```sql
SELECT
id,
name,
aksResourceID,
appLogsConfiguration,
arcConfiguration,
containerAppsConfiguration,
defaultDomain,
deploymentErrors,
environmentType,
extendedLocation,
internalLoadBalancerEnabled,
kind,
location,
provisioningState,
staticIp,
systemData,
tags,
type
FROM azure.web.kube_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get all Kubernetes Environments for a subscription. Description for Get all Kubernetes Environments for a subscription.

```sql
SELECT
id,
name,
aksResourceID,
appLogsConfiguration,
arcConfiguration,
containerAppsConfiguration,
defaultDomain,
deploymentErrors,
environmentType,
extendedLocation,
internalLoadBalancerEnabled,
kind,
location,
provisioningState,
staticIp,
systemData,
tags,
type
FROM azure.web.kube_environments
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

Creates or updates a Kubernetes Environment. Description for Creates or updates a Kubernetes Environment.

```sql
INSERT INTO azure.web.kube_environments (
tags,
location,
properties,
extendedLocation,
kind,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
kind,
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
- name: kube_environments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the kube_environments resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the kube_environments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the kube_environments resource.
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
        KubeEnvironment resource specific properties.
      value:
        provisioningState: "{{ provisioningState }}"
        deploymentErrors: "{{ deploymentErrors }}"
        internalLoadBalancerEnabled: {{ internalLoadBalancerEnabled }}
        defaultDomain: "{{ defaultDomain }}"
        staticIp: "{{ staticIp }}"
        environmentType: "{{ environmentType }}"
        arcConfiguration:
          artifactsStorageType: "{{ artifactsStorageType }}"
          artifactStorageClassName: "{{ artifactStorageClassName }}"
          artifactStorageMountPath: "{{ artifactStorageMountPath }}"
          artifactStorageNodeName: "{{ artifactStorageNodeName }}"
          artifactStorageAccessMode: "{{ artifactStorageAccessMode }}"
          frontEndServiceConfiguration:
            kind: "{{ kind }}"
          kubeConfig: "{{ kubeConfig }}"
        appLogsConfiguration:
          destination: "{{ destination }}"
          logAnalyticsConfiguration:
            customerId: "{{ customerId }}"
            sharedKey: "{{ sharedKey }}"
        containerAppsConfiguration:
          daprAIInstrumentationKey: "{{ daprAIInstrumentationKey }}"
          platformReservedCidr: "{{ platformReservedCidr }}"
          platformReservedDnsIP: "{{ platformReservedDnsIP }}"
          controlPlaneSubnetResourceId: "{{ controlPlaneSubnetResourceId }}"
          appSubnetResourceId: "{{ appSubnetResourceId }}"
          dockerBridgeCidr: "{{ dockerBridgeCidr }}"
        aksResourceID: "{{ aksResourceID }}"
    - name: extendedLocation
      description: |
        Extended Location.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource.
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

Creates or updates a Kubernetes Environment. Description for Creates or updates a Kubernetes Environment.

```sql
UPDATE azure.web.kube_environments
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
kind,
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

Creates or updates a Kubernetes Environment. Description for Creates or updates a Kubernetes Environment.

```sql
REPLACE azure.web.kube_environments
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
kind,
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

Delete a Kubernetes Environment. Description for Delete a Kubernetes Environment.

```sql
DELETE FROM azure.web.kube_environments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
