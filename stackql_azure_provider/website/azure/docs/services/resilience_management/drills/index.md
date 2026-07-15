--- 
title: drills
hide_title: false
hide_table_of_contents: false
keywords:
  - drills
  - resilience_management
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

Creates, updates, deletes, gets or lists a <code>drills</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="drills" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resilience_management.drills" /></td></tr>
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
    <td><CopyableCode code="attentionReason" /></td>
    <td><code>object</code></td>
    <td>Attention reason if the ReadinessState is 'NeedsAttention'.</td>
</tr>
<tr>
    <td><CopyableCode code="chaosResourceProperties" /></td>
    <td><code>object</code></td>
    <td>Chaos Resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="drillAssetProperties" /></td>
    <td><code>object</code></td>
    <td>Properties for internal resources that are created for the Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="drillType" /></td>
    <td><code>string</code></td>
    <td>The discriminator for the Drill object hierarchy. Required. Known values are: "Zonal" and "Regional".</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Error details associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="executionReadinessState" /></td>
    <td><code>string</code></td>
    <td>Readiness state of the Drill. Known values are: "Ready" and "NeedsAttention". (Ready, NeedsAttention)</td>
</tr>
<tr>
    <td><CopyableCode code="executionState" /></td>
    <td><code>string</code></td>
    <td>Execution state of the Drill. Whether it is currently running or not. Known values are: "NotRunning", "Running", and "Paused". (NotRunning, Running, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastResyncReadinessCheckTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last resync and readiness check time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRunProperties" /></td>
    <td><code>object</code></td>
    <td>Last run properties.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last sync time.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed RG v2 properties.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringProperties" /></td>
    <td><code>object</code></td>
    <td>Monitoring properties of the Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rbacSetupMode" /></td>
    <td><code>string</code></td>
    <td>RBAC setup mode. Known values are: "AutomatedCustomRole", "AutomatedBuiltinRoles", and "Manual". (AutomatedCustomRole, AutomatedBuiltinRoles, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPlanProperties" /></td>
    <td><code>object</code></td>
    <td>ROPlan properties.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGroupId" /></td>
    <td><code>string</code></td>
    <td>Parent SG resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemMetadata" /></td>
    <td><code>object</code></td>
    <td>Internal System Metadata, to be used by internal components only.</td>
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
    <td><CopyableCode code="attentionReason" /></td>
    <td><code>object</code></td>
    <td>Attention reason if the ReadinessState is 'NeedsAttention'.</td>
</tr>
<tr>
    <td><CopyableCode code="chaosResourceProperties" /></td>
    <td><code>object</code></td>
    <td>Chaos Resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="drillAssetProperties" /></td>
    <td><code>object</code></td>
    <td>Properties for internal resources that are created for the Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="drillType" /></td>
    <td><code>string</code></td>
    <td>The discriminator for the Drill object hierarchy. Required. Known values are: "Zonal" and "Regional".</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Error details associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="executionReadinessState" /></td>
    <td><code>string</code></td>
    <td>Readiness state of the Drill. Known values are: "Ready" and "NeedsAttention". (Ready, NeedsAttention)</td>
</tr>
<tr>
    <td><CopyableCode code="executionState" /></td>
    <td><code>string</code></td>
    <td>Execution state of the Drill. Whether it is currently running or not. Known values are: "NotRunning", "Running", and "Paused". (NotRunning, Running, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastResyncReadinessCheckTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last resync and readiness check time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRunProperties" /></td>
    <td><code>object</code></td>
    <td>Last run properties.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last sync time.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed RG v2 properties.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringProperties" /></td>
    <td><code>object</code></td>
    <td>Monitoring properties of the Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rbacSetupMode" /></td>
    <td><code>string</code></td>
    <td>RBAC setup mode. Known values are: "AutomatedCustomRole", "AutomatedBuiltinRoles", and "Manual". (AutomatedCustomRole, AutomatedBuiltinRoles, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPlanProperties" /></td>
    <td><code>object</code></td>
    <td>ROPlan properties.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGroupId" /></td>
    <td><code>string</code></td>
    <td>Parent SG resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemMetadata" /></td>
    <td><code>object</code></td>
    <td>Internal System Metadata, to be used by internal components only.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a></td>
    <td></td>
    <td>Get a Drill.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List Drill resources by tenant.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a></td>
    <td></td>
    <td>Create a Drill.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a></td>
    <td></td>
    <td>Update a Drill.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a></td>
    <td></td>
    <td>Delete a Drill.</td>
</tr>
<tr>
    <td><a href="#validate_for_execution"><CopyableCode code="validate_for_execution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This returns eligible resource to be faulted or failed over.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-mode"><code>mode</code></a></td>
    <td></td>
    <td>This starts a new running instance of the Drill.</td>
</tr>
<tr>
    <td><a href="#end"><CopyableCode code="end" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-attestation"><code>attestation</code></a>, <a href="#parameter-attestationNotes"><code>attestationNotes</code></a></td>
    <td></td>
    <td>This ends the currently running instance of the Drill.</td>
</tr>
<tr>
    <td><a href="#add_or_update_resources"><CopyableCode code="add_or_update_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-faultDurationInMin"><code>faultDurationInMin</code></a></td>
    <td></td>
    <td>This enables the user to include, exclude or update resources from their Drill.</td>
</tr>
<tr>
    <td><a href="#resync_readiness_check"><CopyableCode code="resync_readiness_check" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This triggers detection of any drifts from the desired state of Resources and RBAC.</td>
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
<tr id="parameter-drill_name">
    <td><CopyableCode code="drill_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Drill. Required.</td>
</tr>
<tr id="parameter-operation-id">
    <td><CopyableCode code="operation-id" /></td>
    <td><code>string</code></td>
    <td>A GUID that represents the Long Running OperationId. Required.</td>
</tr>
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip over when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Default value is None.</td>
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

Get a Drill.

```sql
SELECT
id,
name,
attentionReason,
chaosResourceProperties,
drillAssetProperties,
drillType,
errorDetails,
executionReadinessState,
executionState,
identity,
lastResyncReadinessCheckTime,
lastRunProperties,
lastSyncTime,
managedOnBehalfOfConfiguration,
monitoringProperties,
provisioningState,
rbacSetupMode,
recoveryPlanProperties,
serviceGroupId,
systemData,
systemMetadata,
type
FROM azure.resilience_management.drills
WHERE service_group_name = '{{ service_group_name }}' -- required
AND drill_name = '{{ drill_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Drill resources by tenant.

```sql
SELECT
id,
name,
attentionReason,
chaosResourceProperties,
drillAssetProperties,
drillType,
errorDetails,
executionReadinessState,
executionState,
identity,
lastResyncReadinessCheckTime,
lastRunProperties,
lastSyncTime,
managedOnBehalfOfConfiguration,
monitoringProperties,
provisioningState,
rbacSetupMode,
recoveryPlanProperties,
serviceGroupId,
systemData,
systemMetadata,
type
FROM azure.resilience_management.drills
WHERE service_group_name = '{{ service_group_name }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
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

Create a Drill.

```sql
INSERT INTO azure.resilience_management.drills (
properties,
identity,
service_group_name,
drill_name
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ service_group_name }}',
'{{ drill_name }}'
RETURNING
id,
name,
identity,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: drills
  props:
    - name: service_group_name
      value: "{{ service_group_name }}"
      description: Required parameter for the drills resource.
    - name: drill_name
      value: "{{ drill_name }}"
      description: Required parameter for the drills resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        serviceGroupId: "{{ serviceGroupId }}"
        recoveryPlanProperties:
          identity:
            type: "{{ type }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
          recoveryPlanId: "{{ recoveryPlanId }}"
          recoveryPlanResourceExcludedCount: {{ recoveryPlanResourceExcludedCount }}
        drillAssetProperties:
          subscription: "{{ subscription }}"
          region: "{{ region }}"
          resourceGroup: "{{ resourceGroup }}"
        chaosResourceProperties:
          identity:
            type: "{{ type }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
          chaosResourceIdentityForFaults:
            type: "{{ type }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
          chaosResourceId: "{{ chaosResourceId }}"
          faultDurationInMin: {{ faultDurationInMin }}
        executionState: "{{ executionState }}"
        executionReadinessState: "{{ executionReadinessState }}"
        rbacSetupMode: "{{ rbacSetupMode }}"
        attentionReason:
          drillRbacOnChaosResource: "{{ drillRbacOnChaosResource }}"
          rbacNeededForDrillOnChaosResource:
            - "{{ rbacNeededForDrillOnChaosResource }}"
          drillRbacOnRecoveryPlan: "{{ drillRbacOnRecoveryPlan }}"
          rbacNeededForDrillOnRecoveryPlan:
            - "{{ rbacNeededForDrillOnRecoveryPlan }}"
          roReadiness: "{{ roReadiness }}"
          rbacOnTargetResources: "{{ rbacOnTargetResources }}"
          runbookFaultRbacOnTargets: "{{ runbookFaultRbacOnTargets }}"
          chaosResource: "{{ chaosResource }}"
          chaosResourceCreationFailureReasons:
            - "{{ chaosResourceCreationFailureReasons }}"
          recoveryPlanAndDrillResourcesState: "{{ recoveryPlanAndDrillResourcesState }}"
          serviceGroupAndDrillResourcesState: "{{ serviceGroupAndDrillResourcesState }}"
          drillUserMsi: "{{ drillUserMsi }}"
          chaosResourceUserMsi: "{{ chaosResourceUserMsi }}"
          includedResourceInDrill: "{{ includedResourceInDrill }}"
          drillRbacOnMonitoringResources: "{{ drillRbacOnMonitoringResources }}"
          drillMonitoringErrors:
            - code: "{{ code }}"
              message: "{{ message }}"
              recommendations: "{{ recommendations }}"
          drillMonitoringResources: "{{ drillMonitoringResources }}"
          monitoringRbacOnDrillResources: "{{ monitoringRbacOnDrillResources }}"
          rbacNeededForDrillOnDrillMonitoringResources:
            - "{{ rbacNeededForDrillOnDrillMonitoringResources }}"
          rbacNeededForDrillOnDrillResources:
            - "{{ rbacNeededForDrillOnDrillResources }}"
          missingRequiredResourceProviders:
            - "{{ missingRequiredResourceProviders }}"
        systemMetadata:
          initialConfig: "{{ initialConfig }}"
          resourceTypeCategories:
            - "{{ resourceTypeCategories }}"
        lastRunProperties:
          lastRunTime: "{{ lastRunTime }}"
          lastRunState: "{{ lastRunState }}"
          lastRunDuration: "{{ lastRunDuration }}"
          lastRunAttestation: "{{ lastRunAttestation }}"
        lastSyncTime: "{{ lastSyncTime }}"
        lastResyncReadinessCheckTime: "{{ lastResyncReadinessCheckTime }}"
        managedOnBehalfOfConfiguration:
          moboBrokerResources:
            - id: "{{ id }}"
        drillType: "{{ drillType }}"
        monitoringProperties:
          identity:
            type: "{{ type }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
          logAnalyticsWorkspaceId: "{{ logAnalyticsWorkspaceId }}"
          rawMetricsDataCollectionRuleId: "{{ rawMetricsDataCollectionRuleId }}"
          serviceGroupMetricsDataCollectionRuleId: "{{ serviceGroupMetricsDataCollectionRuleId }}"
          dataCollectionEndpointId: "{{ dataCollectionEndpointId }}"
        errorDetails:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          details:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
          additionalInfo:
            - type: "{{ type }}"
              info: "{{ info }}"
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

Update a Drill.

```sql
UPDATE azure.resilience_management.drills
SET 
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND drill_name = '{{ drill_name }}' --required;
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

Delete a Drill.

```sql
DELETE FROM azure.resilience_management.drills
WHERE service_group_name = '{{ service_group_name }}' --required
AND drill_name = '{{ drill_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_for_execution"
    values={[
        { label: 'validate_for_execution', value: 'validate_for_execution' },
        { label: 'start', value: 'start' },
        { label: 'end', value: 'end' },
        { label: 'add_or_update_resources', value: 'add_or_update_resources' },
        { label: 'resync_readiness_check', value: 'resync_readiness_check' }
    ]}
>
<TabItem value="validate_for_execution">

This returns eligible resource to be faulted or failed over.

```sql
EXEC azure.resilience_management.drills.validate_for_execution 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"validateForExecutionProperties": "{{ validateForExecutionProperties }}"
}'
;
```
</TabItem>
<TabItem value="start">

This starts a new running instance of the Drill.

```sql
EXEC azure.resilience_management.drills.start 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"mode": "{{ mode }}"
}'
;
```
</TabItem>
<TabItem value="end">

This ends the currently running instance of the Drill.

```sql
EXEC azure.resilience_management.drills.end 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"attestation": "{{ attestation }}", 
"attestationNotes": "{{ attestationNotes }}"
}'
;
```
</TabItem>
<TabItem value="add_or_update_resources">

This enables the user to include, exclude or update resources from their Drill.

```sql
EXEC azure.resilience_management.drills.add_or_update_resources 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"faultDurationInMin": {{ faultDurationInMin }}, 
"resourceLists": "{{ resourceLists }}", 
"forceInclusionAndUpdate": "{{ forceInclusionAndUpdate }}"
}'
;
```
</TabItem>
<TabItem value="resync_readiness_check">

This triggers detection of any drifts from the desired state of Resources and RBAC.

```sql
EXEC azure.resilience_management.drills.resync_readiness_check 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
</Tabs>
