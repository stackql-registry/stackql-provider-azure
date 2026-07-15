--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric_managed_clusters
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.applications" /></td></tr>
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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Describes the managed identities for an Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentities" /></td>
    <td><code>array</code></td>
    <td>List of user assigned identities for the application, each mapped to a friendly name.</td>
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
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>Describes the policy for a monitored application upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the application type as defined in the application manifest. This name must be the full Arm Resource ID for the referenced application type version.</td>
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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Describes the managed identities for an Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentities" /></td>
    <td><code>array</code></td>
    <td>List of user assigned identities for the application, each mapped to a friendly name.</td>
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
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>Describes the policy for a monitored application upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the application type as defined in the application manifest. This name must be the full Arm Resource ID for the referenced application type version.</td>
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
    <td>Get a Service Fabric managed application resource created or in the process of being created in the Service Fabric cluster resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all managed application resources created or in the process of being created in the Service Fabric cluster resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Service Fabric managed application resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an application resource of a given managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Service Fabric managed application resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Service Fabric managed application resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#read_upgrade"><CopyableCode code="read_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of the latest application upgrade. It will query the cluster to find the status of the latest application upgrade.</td>
</tr>
<tr>
    <td><a href="#resume_upgrade"><CopyableCode code="resume_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Send a request to resume the current application upgrade. This will resume the application upgrade from where it was paused.</td>
</tr>
<tr>
    <td><a href="#start_rollback"><CopyableCode code="start_rollback" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Send a request to start a rollback of the current application upgrade. This will start rolling back the application to the previous version.</td>
</tr>
<tr>
    <td><a href="#update_upgrade"><CopyableCode code="update_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-upgradeKind"><code>upgradeKind</code></a></td>
    <td></td>
    <td>Send a request to update the current application upgrade.</td>
</tr>
<tr>
    <td><a href="#fetch_health"><CopyableCode code="fetch_health" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of the deployed application health. It will query the cluster to find the health of the deployed application.</td>
</tr>
<tr>
    <td><a href="#restart_deployed_code_package"><CopyableCode code="restart_deployed_code_package" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-nodeName"><code>nodeName</code></a>, <a href="#parameter-serviceManifestName"><code>serviceManifestName</code></a>, <a href="#parameter-codePackageName"><code>codePackageName</code></a>, <a href="#parameter-codePackageInstanceId"><code>codePackageInstanceId</code></a></td>
    <td></td>
    <td>Restart a code package instance of a service replica or instance. This is a potentially destabilizing operation that should be used with immense care.</td>
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

Get a Service Fabric managed application resource created or in the process of being created in the Service Fabric cluster resource.

```sql
SELECT
id,
name,
identity,
location,
managedIdentities,
parameters,
provisioningState,
systemData,
tags,
type,
upgradePolicy,
version
FROM azure.service_fabric_managed_clusters.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND application_name = '{{ application_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all managed application resources created or in the process of being created in the Service Fabric cluster resource.

```sql
SELECT
id,
name,
identity,
location,
managedIdentities,
parameters,
provisioningState,
systemData,
tags,
type,
upgradePolicy,
version
FROM azure.service_fabric_managed_clusters.applications
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

Create or update a Service Fabric managed application resource with the specified name.

```sql
INSERT INTO azure.service_fabric_managed_clusters.applications (
properties,
tags,
identity,
location,
resource_group_name,
cluster_name,
application_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ identity }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ application_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
        managedIdentities:
          - name: "{{ name }}"
            principalId: "{{ principalId }}"
        provisioningState: "{{ provisioningState }}"
        version: "{{ version }}"
        parameters: "{{ parameters }}"
        upgradePolicy:
          applicationHealthPolicy:
            considerWarningAsError: {{ considerWarningAsError }}
            maxPercentUnhealthyDeployedApplications: {{ maxPercentUnhealthyDeployedApplications }}
            defaultServiceTypeHealthPolicy:
              maxPercentUnhealthyServices: {{ maxPercentUnhealthyServices }}
              maxPercentUnhealthyPartitionsPerService: {{ maxPercentUnhealthyPartitionsPerService }}
              maxPercentUnhealthyReplicasPerPartition: {{ maxPercentUnhealthyReplicasPerPartition }}
            serviceTypeHealthPolicyMap: "{{ serviceTypeHealthPolicyMap }}"
          forceRestart: {{ forceRestart }}
          rollingUpgradeMonitoringPolicy:
            failureAction: "{{ failureAction }}"
            healthCheckWaitDuration: "{{ healthCheckWaitDuration }}"
            healthCheckStableDuration: "{{ healthCheckStableDuration }}"
            healthCheckRetryTimeout: "{{ healthCheckRetryTimeout }}"
            upgradeTimeout: "{{ upgradeTimeout }}"
            upgradeDomainTimeout: "{{ upgradeDomainTimeout }}"
          instanceCloseDelayDuration: {{ instanceCloseDelayDuration }}
          upgradeMode: "{{ upgradeMode }}"
          upgradeReplicaSetCheckTimeout: {{ upgradeReplicaSetCheckTimeout }}
          recreateApplication: {{ recreateApplication }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: identity
      description: |
        Describes the managed identities for an Azure resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
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

Updates an application resource of a given managed cluster.

```sql
UPDATE azure.service_fabric_managed_clusters.applications
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update a Service Fabric managed application resource with the specified name.

```sql
REPLACE azure.service_fabric_managed_clusters.applications
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete a Service Fabric managed application resource with the specified name.

```sql
DELETE FROM azure.service_fabric_managed_clusters.applications
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="read_upgrade"
    values={[
        { label: 'read_upgrade', value: 'read_upgrade' },
        { label: 'resume_upgrade', value: 'resume_upgrade' },
        { label: 'start_rollback', value: 'start_rollback' },
        { label: 'update_upgrade', value: 'update_upgrade' },
        { label: 'fetch_health', value: 'fetch_health' },
        { label: 'restart_deployed_code_package', value: 'restart_deployed_code_package' }
    ]}
>
<TabItem value="read_upgrade">

Get the status of the latest application upgrade. It will query the cluster to find the status of the latest application upgrade.

```sql
EXEC azure.service_fabric_managed_clusters.applications.read_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume_upgrade">

Send a request to resume the current application upgrade. This will resume the application upgrade from where it was paused.

```sql
EXEC azure.service_fabric_managed_clusters.applications.resume_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"upgradeDomainName": "{{ upgradeDomainName }}"
}'
;
```
</TabItem>
<TabItem value="start_rollback">

Send a request to start a rollback of the current application upgrade. This will start rolling back the application to the previous version.

```sql
EXEC azure.service_fabric_managed_clusters.applications.start_rollback 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_upgrade">

Send a request to update the current application upgrade.

```sql
EXEC azure.service_fabric_managed_clusters.applications.update_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"upgradeKind": "{{ upgradeKind }}", 
"applicationHealthPolicy": "{{ applicationHealthPolicy }}", 
"updateDescription": "{{ updateDescription }}"
}'
;
```
</TabItem>
<TabItem value="fetch_health">

Get the status of the deployed application health. It will query the cluster to find the health of the deployed application.

```sql
EXEC azure.service_fabric_managed_clusters.applications.fetch_health 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"eventsHealthStateFilter": "{{ eventsHealthStateFilter }}", 
"deployedApplicationsHealthStateFilter": "{{ deployedApplicationsHealthStateFilter }}", 
"servicesHealthStateFilter": "{{ servicesHealthStateFilter }}", 
"excludeHealthStatistics": {{ excludeHealthStatistics }}, 
"timeout": {{ timeout }}
}'
;
```
</TabItem>
<TabItem value="restart_deployed_code_package">

Restart a code package instance of a service replica or instance. This is a potentially destabilizing operation that should be used with immense care.

```sql
EXEC azure.service_fabric_managed_clusters.applications.restart_deployed_code_package 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodeName": "{{ nodeName }}", 
"serviceManifestName": "{{ serviceManifestName }}", 
"codePackageName": "{{ codePackageName }}", 
"codePackageInstanceId": "{{ codePackageInstanceId }}", 
"servicePackageActivationId": "{{ servicePackageActivationId }}"
}'
;
```
</TabItem>
</Tabs>
