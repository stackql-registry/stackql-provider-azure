--- 
title: connected_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments
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

Creates, updates, deletes, gets or lists a <code>connected_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connected_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.connected_environments" /></td></tr>
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
    <td><CopyableCode code="customDomainConfiguration" /></td>
    <td><code>object</code></td>
    <td>Custom domain configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights connection string used by Dapr to export Service to Service communication telemetry.</td>
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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The complex type of the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Kubernetes Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", and "ScheduledForDelete". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the connectedEnvironment.</td>
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
    <td><CopyableCode code="customDomainConfiguration" /></td>
    <td><code>object</code></td>
    <td>Custom domain configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights connection string used by Dapr to export Service to Service communication telemetry.</td>
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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The complex type of the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Kubernetes Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", and "ScheduledForDelete". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the connectedEnvironment.</td>
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
    <td><CopyableCode code="customDomainConfiguration" /></td>
    <td><code>object</code></td>
    <td>Custom domain configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights connection string used by Dapr to export Service to Service communication telemetry.</td>
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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The complex type of the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Kubernetes Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", and "ScheduledForDelete". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the connectedEnvironment.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of an connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all connectedEnvironments in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all connectedEnvironments for a subscription. Get all connectedEnvironments for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update connected Environment's properties. Patches a Managed Environment. Only patching of tags is supported currently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an connectedEnvironment. Delete an connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the resource connectedEnvironmentName availability. Checks if resource connectedEnvironmentName is available.</td>
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
<tr id="parameter-connected_environment_name">
    <td><CopyableCode code="connected_environment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the connectedEnvironment. Required.</td>
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

Get the properties of an connectedEnvironment.

```sql
SELECT
id,
name,
customDomainConfiguration,
daprAIConnectionString,
defaultDomain,
deploymentErrors,
extendedLocation,
location,
provisioningState,
staticIp,
systemData,
tags,
type
FROM azure.appcontainers.connected_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND connected_environment_name = '{{ connected_environment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all connectedEnvironments in a resource group.

```sql
SELECT
id,
name,
customDomainConfiguration,
daprAIConnectionString,
defaultDomain,
deploymentErrors,
extendedLocation,
location,
provisioningState,
staticIp,
systemData,
tags,
type
FROM azure.appcontainers.connected_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get all connectedEnvironments for a subscription. Get all connectedEnvironments for a subscription.

```sql
SELECT
id,
name,
customDomainConfiguration,
daprAIConnectionString,
defaultDomain,
deploymentErrors,
extendedLocation,
location,
provisioningState,
staticIp,
systemData,
tags,
type
FROM azure.appcontainers.connected_environments
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

Creates or updates an connectedEnvironment.

```sql
INSERT INTO azure.appcontainers.connected_environments (
tags,
location,
properties,
extendedLocation,
resource_group_name,
connected_environment_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ connected_environment_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
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
- name: connected_environments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connected_environments resource.
    - name: connected_environment_name
      value: "{{ connected_environment_name }}"
      description: Required parameter for the connected_environments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connected_environments resource.
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
        ConnectedEnvironment resource specific properties.
      value:
        provisioningState: "{{ provisioningState }}"
        deploymentErrors: "{{ deploymentErrors }}"
        defaultDomain: "{{ defaultDomain }}"
        staticIp: "{{ staticIp }}"
        daprAIConnectionString: "{{ daprAIConnectionString }}"
        customDomainConfiguration:
          customDomainVerificationId: "{{ customDomainVerificationId }}"
          dnsSuffix: "{{ dnsSuffix }}"
          certificateKeyVaultProperties:
            identity: "{{ identity }}"
            keyVaultUrl: "{{ keyVaultUrl }}"
          certificateValue: "{{ certificateValue }}"
          certificatePassword: "{{ certificatePassword }}"
          expirationDate: "{{ expirationDate }}"
          thumbprint: "{{ thumbprint }}"
          subjectName: "{{ subjectName }}"
    - name: extendedLocation
      description: |
        The complex type of the extended location.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Update connected Environment's properties. Patches a Managed Environment. Only patching of tags is supported currently.

```sql
UPDATE azure.appcontainers.connected_environments
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND connected_environment_name = '{{ connected_environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
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

Creates or updates an connectedEnvironment.

```sql
REPLACE azure.appcontainers.connected_environments
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND connected_environment_name = '{{ connected_environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
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

Delete an connectedEnvironment. Delete an connectedEnvironment.

```sql
DELETE FROM azure.appcontainers.connected_environments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND connected_environment_name = '{{ connected_environment_name }}' --required
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

Checks the resource connectedEnvironmentName availability. Checks if resource connectedEnvironmentName is available.

```sql
EXEC azure.appcontainers.connected_environments.check_name_availability 
@resource_group_name='{{ resource_group_name }}' --required, 
@connected_environment_name='{{ connected_environment_name }}' --required, 
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
