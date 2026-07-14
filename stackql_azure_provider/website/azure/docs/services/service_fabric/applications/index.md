--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric
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

Creates, updates, deletes, gets or lists an <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.applications" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Azure resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>It will be deprecated in New API, resource location depends on the parent resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentities" /></td>
    <td><code>array</code></td>
    <td>List of user assigned identities for the application, each mapped to a friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNodes" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. By default, the value of this property is zero and it means that the services can be placed on any node.</td>
</tr>
<tr>
    <td><CopyableCode code="metrics" /></td>
    <td><code>array</code></td>
    <td>List of application capacity metric description.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumNodes" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. If this property is set to zero, no capacity will be reserved. The value of this property cannot be more than the value of the MaximumNodes property.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>List of application parameters with overridden values from their default values specified in the application manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="removeApplicationCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Remove the current application capacity settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Azure resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="typeName" /></td>
    <td><code>string</code></td>
    <td>The application type name as defined in the application manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="typeVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the application type as defined in the application manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>Describes the policy for a monitored application upgrade.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Azure resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>It will be deprecated in New API, resource location depends on the parent resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentities" /></td>
    <td><code>array</code></td>
    <td>List of user assigned identities for the application, each mapped to a friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNodes" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. By default, the value of this property is zero and it means that the services can be placed on any node.</td>
</tr>
<tr>
    <td><CopyableCode code="metrics" /></td>
    <td><code>array</code></td>
    <td>List of application capacity metric description.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumNodes" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. If this property is set to zero, no capacity will be reserved. The value of this property cannot be more than the value of the MaximumNodes property.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>List of application parameters with overridden values from their default values specified in the application manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="removeApplicationCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Remove the current application capacity settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Azure resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="typeName" /></td>
    <td><code>string</code></td>
    <td>The application type name as defined in the application manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="typeVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the application type as defined in the application manifest.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>Describes the policy for a monitored application upgrade.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Service Fabric application resource. Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of application resources created in the specified Service Fabric cluster resource. Gets all application resources created or in the process of being created in the Service Fabric cluster resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Service Fabric application resource. Create or update a Service Fabric application resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a Service Fabric application resource. Update a Service Fabric application resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Service Fabric application resource. Create or update a Service Fabric application resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Service Fabric application resource. Delete a Service Fabric application resource with the specified name.</td>
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
<tr id="parameter-application_name">
    <td><CopyableCode code="application_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application resource. Required.</td>
</tr>
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster resource. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a Service Fabric application resource. Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource.

```sql
SELECT
id,
name,
etag,
identity,
location,
managedIdentities,
maximumNodes,
metrics,
minimumNodes,
parameters,
provisioningState,
removeApplicationCapacity,
systemData,
tags,
type,
typeName,
typeVersion,
upgradePolicy
FROM azure.service_fabric.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND application_name = '{{ application_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of application resources created in the specified Service Fabric cluster resource. Gets all application resources created or in the process of being created in the Service Fabric cluster resource.

```sql
SELECT
id,
name,
etag,
identity,
location,
managedIdentities,
maximumNodes,
metrics,
minimumNodes,
parameters,
provisioningState,
removeApplicationCapacity,
systemData,
tags,
type,
typeName,
typeVersion,
upgradePolicy
FROM azure.service_fabric.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a Service Fabric application resource. Create or update a Service Fabric application resource with the specified name.

```sql
INSERT INTO azure.service_fabric.applications (
properties,
location,
tags,
identity,
resource_group_name,
cluster_name,
application_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ application_name }}',
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
- name: applications
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the applications resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the applications resource.
    - name: application_name
      value: "{{ application_name }}"
      description: Required parameter for the applications resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the applications resource.
    - name: properties
      description: |
        The application resource properties.
      value:
        typeVersion: "{{ typeVersion }}"
        parameters: "{{ parameters }}"
        upgradePolicy:
          upgradeReplicaSetCheckTimeout: "{{ upgradeReplicaSetCheckTimeout }}"
          forceRestart: {{ forceRestart }}
          rollingUpgradeMonitoringPolicy:
            failureAction: "{{ failureAction }}"
            healthCheckWaitDuration: "{{ healthCheckWaitDuration }}"
            healthCheckStableDuration: "{{ healthCheckStableDuration }}"
            healthCheckRetryTimeout: "{{ healthCheckRetryTimeout }}"
            upgradeTimeout: "{{ upgradeTimeout }}"
            upgradeDomainTimeout: "{{ upgradeDomainTimeout }}"
          applicationHealthPolicy:
            considerWarningAsError: {{ considerWarningAsError }}
            maxPercentUnhealthyDeployedApplications: {{ maxPercentUnhealthyDeployedApplications }}
            defaultServiceTypeHealthPolicy:
              maxPercentUnhealthyServices: {{ maxPercentUnhealthyServices }}
              maxPercentUnhealthyPartitionsPerService: {{ maxPercentUnhealthyPartitionsPerService }}
              maxPercentUnhealthyReplicasPerPartition: {{ maxPercentUnhealthyReplicasPerPartition }}
            serviceTypeHealthPolicyMap: "{{ serviceTypeHealthPolicyMap }}"
          upgradeMode: "{{ upgradeMode }}"
          recreateApplication: {{ recreateApplication }}
        minimumNodes: {{ minimumNodes }}
        maximumNodes: {{ maximumNodes }}
        removeApplicationCapacity: {{ removeApplicationCapacity }}
        metrics:
          - name: "{{ name }}"
            maximumCapacity: {{ maximumCapacity }}
            reservationCapacity: {{ reservationCapacity }}
            totalApplicationCapacity: {{ totalApplicationCapacity }}
        managedIdentities:
          - name: "{{ name }}"
            principalId: "{{ principalId }}"
        provisioningState: "{{ provisioningState }}"
        typeName: "{{ typeName }}"
    - name: location
      value: "{{ location }}"
      description: |
        It will be deprecated in New API, resource location depends on the parent resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Azure resource tags.
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

Updates a Service Fabric application resource. Update a Service Fabric application resource with the specified name.

```sql
UPDATE azure.service_fabric.applications
SET 
location = '{{ location }}',
tags = '{{ tags }}',
systemData = '{{ systemData }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
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

Creates or updates a Service Fabric application resource. Create or update a Service Fabric application resource with the specified name.

```sql
REPLACE azure.service_fabric.applications
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a Service Fabric application resource. Delete a Service Fabric application resource with the specified name.

```sql
DELETE FROM azure.service_fabric.applications
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
