--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - networkcloud
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.networkcloud.clusters" /></td></tr>
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
    <td><CopyableCode code="actionStates" /></td>
    <td><code>array</code></td>
    <td>The current state of any in progress or completed actions. The most recent known instance of each action type is shown.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregatorOrSingleRackDefinition" /></td>
    <td><code>object</code></td>
    <td>RackDefinition represents details regarding the rack.</td>
</tr>
<tr>
    <td><CopyableCode code="analyticsOutputSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the log analytics workspace used for output of logs from this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="analyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated. The resource ID of the Log Analytics Workspace that will be used for storing relevant logs.</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgradeVersions" /></td>
    <td><code>array</code></td>
    <td>The list of cluster runtime version upgrades available for this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCapacity" /></td>
    <td><code>object</code></td>
    <td>The capacity supported by this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The latest heartbeat status between the cluster manager and the cluster. Known values are: "Connected", "Disconnected", "Timeout", and "Undefined". (Connected, Disconnected, Timeout, Undefined)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location (custom location) that represents the cluster's control plane location. This extended location is used to route the requests of child objects of the cluster that are handled by the platform operator.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterLocation" /></td>
    <td><code>string</code></td>
    <td>The customer-provided location information to identify where the cluster resides.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The latest connectivity status between cluster manager and the cluster. Known values are: "Connected" and "Unreachable". (Connected, Unreachable)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster manager that manages this cluster. This is set by the Cluster Manager when the cluster is created.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterServicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Field Deprecated: Use managed identity to provide cluster privileges. The service principal to be used by the cluster during Arc Appliance installation.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>The type of rack configuration for the cluster. Required. Known values are: "SingleRack" and "MultiRack". (SingleRack, MultiRack)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersion" /></td>
    <td><code>string</code></td>
    <td>The current runtime version of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="commandOutputSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for commands run in this cluster, such as bare metal machine run read only commands and data extracts.</td>
</tr>
<tr>
    <td><CopyableCode code="computeDeploymentThreshold" /></td>
    <td><code>object</code></td>
    <td>The validation threshold indicating the allowable failures of compute machines during environment validation and deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="computeRackDefinitions" /></td>
    <td><code>array</code></td>
    <td>The list of rack definitions for the compute racks in a multi-rack cluster, or an empty list in a single-rack cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current detailed status of the cluster. Known values are: "PendingDeployment", "Deploying", "Running", "Updating", "UpdatePaused", "Degraded", "Deleting", "Disconnected", and "Failed". (PendingDeployment, Deploying, Running, Updating, UpdatePaused, Degraded, Deleting, Disconnected, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>Field Deprecated. This field will not be populated in an upcoming version. The extended location (custom location) that represents the Hybrid AKS control plane location. This extended location is used when creating provisioned clusters (Hybrid AKS clusters).</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The type (kind) of the cluster. When specified, the value must exactly match the kind configured on the cluster manager that manages the cluster. If omitted, the service will default the value to the kind value of the cluster manager. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulVersionUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the end of the last successful version update for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedCredentials" /></td>
    <td><code>array</code></td>
    <td>The list of credentials that are managed for the cluster and can be rotated on-demand.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the managed resource group associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="manualActionCount" /></td>
    <td><code>integer</code></td>
    <td>The count of Manual Action Taken (MAT) events that have not been validated.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Fabric associated with the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Validating", and "Updating". (Succeeded, Failed, Canceled, Accepted, Validating, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeProtectionConfiguration" /></td>
    <td><code>object</code></td>
    <td>The settings for cluster runtime protection.</td>
</tr>
<tr>
    <td><CopyableCode code="secretArchive" /></td>
    <td><code>object</code></td>
    <td>The configuration for use of a key vault to store secrets for later retrieval by the operator.</td>
</tr>
<tr>
    <td><CopyableCode code="secretArchiveSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the secret archive used to hold credentials for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="supportExpiryDate" /></td>
    <td><code>string</code></td>
    <td>The support end date of the runtime version of the cluster.</td>
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
    <td><CopyableCode code="updateStrategy" /></td>
    <td><code>object</code></td>
    <td>The strategy for updating the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="vulnerabilityScanningSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for how security vulnerability scanning is applied to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of workload resource IDs that are hosted within this cluster.</td>
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
    <td><CopyableCode code="actionStates" /></td>
    <td><code>array</code></td>
    <td>The current state of any in progress or completed actions. The most recent known instance of each action type is shown.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregatorOrSingleRackDefinition" /></td>
    <td><code>object</code></td>
    <td>RackDefinition represents details regarding the rack.</td>
</tr>
<tr>
    <td><CopyableCode code="analyticsOutputSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the log analytics workspace used for output of logs from this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="analyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated. The resource ID of the Log Analytics Workspace that will be used for storing relevant logs.</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgradeVersions" /></td>
    <td><code>array</code></td>
    <td>The list of cluster runtime version upgrades available for this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCapacity" /></td>
    <td><code>object</code></td>
    <td>The capacity supported by this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The latest heartbeat status between the cluster manager and the cluster. Known values are: "Connected", "Disconnected", "Timeout", and "Undefined". (Connected, Disconnected, Timeout, Undefined)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location (custom location) that represents the cluster's control plane location. This extended location is used to route the requests of child objects of the cluster that are handled by the platform operator.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterLocation" /></td>
    <td><code>string</code></td>
    <td>The customer-provided location information to identify where the cluster resides.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The latest connectivity status between cluster manager and the cluster. Known values are: "Connected" and "Unreachable". (Connected, Unreachable)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster manager that manages this cluster. This is set by the Cluster Manager when the cluster is created.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterServicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Field Deprecated: Use managed identity to provide cluster privileges. The service principal to be used by the cluster during Arc Appliance installation.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>The type of rack configuration for the cluster. Required. Known values are: "SingleRack" and "MultiRack". (SingleRack, MultiRack)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersion" /></td>
    <td><code>string</code></td>
    <td>The current runtime version of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="commandOutputSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for commands run in this cluster, such as bare metal machine run read only commands and data extracts.</td>
</tr>
<tr>
    <td><CopyableCode code="computeDeploymentThreshold" /></td>
    <td><code>object</code></td>
    <td>The validation threshold indicating the allowable failures of compute machines during environment validation and deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="computeRackDefinitions" /></td>
    <td><code>array</code></td>
    <td>The list of rack definitions for the compute racks in a multi-rack cluster, or an empty list in a single-rack cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current detailed status of the cluster. Known values are: "PendingDeployment", "Deploying", "Running", "Updating", "UpdatePaused", "Degraded", "Deleting", "Disconnected", and "Failed". (PendingDeployment, Deploying, Running, Updating, UpdatePaused, Degraded, Deleting, Disconnected, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>Field Deprecated. This field will not be populated in an upcoming version. The extended location (custom location) that represents the Hybrid AKS control plane location. This extended location is used when creating provisioned clusters (Hybrid AKS clusters).</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The type (kind) of the cluster. When specified, the value must exactly match the kind configured on the cluster manager that manages the cluster. If omitted, the service will default the value to the kind value of the cluster manager. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulVersionUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the end of the last successful version update for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedCredentials" /></td>
    <td><code>array</code></td>
    <td>The list of credentials that are managed for the cluster and can be rotated on-demand.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the managed resource group associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="manualActionCount" /></td>
    <td><code>integer</code></td>
    <td>The count of Manual Action Taken (MAT) events that have not been validated.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Fabric associated with the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Validating", and "Updating". (Succeeded, Failed, Canceled, Accepted, Validating, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeProtectionConfiguration" /></td>
    <td><code>object</code></td>
    <td>The settings for cluster runtime protection.</td>
</tr>
<tr>
    <td><CopyableCode code="secretArchive" /></td>
    <td><code>object</code></td>
    <td>The configuration for use of a key vault to store secrets for later retrieval by the operator.</td>
</tr>
<tr>
    <td><CopyableCode code="secretArchiveSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the secret archive used to hold credentials for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="supportExpiryDate" /></td>
    <td><code>string</code></td>
    <td>The support end date of the runtime version of the cluster.</td>
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
    <td><CopyableCode code="updateStrategy" /></td>
    <td><code>object</code></td>
    <td>The strategy for updating the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="vulnerabilityScanningSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for how security vulnerability scanning is applied to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of workload resource IDs that are hosted within this cluster.</td>
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
    <td><CopyableCode code="actionStates" /></td>
    <td><code>array</code></td>
    <td>The current state of any in progress or completed actions. The most recent known instance of each action type is shown.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregatorOrSingleRackDefinition" /></td>
    <td><code>object</code></td>
    <td>RackDefinition represents details regarding the rack.</td>
</tr>
<tr>
    <td><CopyableCode code="analyticsOutputSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the log analytics workspace used for output of logs from this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="analyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated. The resource ID of the Log Analytics Workspace that will be used for storing relevant logs.</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgradeVersions" /></td>
    <td><code>array</code></td>
    <td>The list of cluster runtime version upgrades available for this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCapacity" /></td>
    <td><code>object</code></td>
    <td>The capacity supported by this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The latest heartbeat status between the cluster manager and the cluster. Known values are: "Connected", "Disconnected", "Timeout", and "Undefined". (Connected, Disconnected, Timeout, Undefined)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location (custom location) that represents the cluster's control plane location. This extended location is used to route the requests of child objects of the cluster that are handled by the platform operator.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterLocation" /></td>
    <td><code>string</code></td>
    <td>The customer-provided location information to identify where the cluster resides.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The latest connectivity status between cluster manager and the cluster. Known values are: "Connected" and "Unreachable". (Connected, Unreachable)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterManagerId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster manager that manages this cluster. This is set by the Cluster Manager when the cluster is created.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterServicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Field Deprecated: Use managed identity to provide cluster privileges. The service principal to be used by the cluster during Arc Appliance installation.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>The type of rack configuration for the cluster. Required. Known values are: "SingleRack" and "MultiRack". (SingleRack, MultiRack)</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersion" /></td>
    <td><code>string</code></td>
    <td>The current runtime version of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="commandOutputSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for commands run in this cluster, such as bare metal machine run read only commands and data extracts.</td>
</tr>
<tr>
    <td><CopyableCode code="computeDeploymentThreshold" /></td>
    <td><code>object</code></td>
    <td>The validation threshold indicating the allowable failures of compute machines during environment validation and deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="computeRackDefinitions" /></td>
    <td><code>array</code></td>
    <td>The list of rack definitions for the compute racks in a multi-rack cluster, or an empty list in a single-rack cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current detailed status of the cluster. Known values are: "PendingDeployment", "Deploying", "Running", "Updating", "UpdatePaused", "Degraded", "Deleting", "Disconnected", and "Failed". (PendingDeployment, Deploying, Running, Updating, UpdatePaused, Degraded, Deleting, Disconnected, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>Field Deprecated. This field will not be populated in an upcoming version. The extended location (custom location) that represents the Hybrid AKS control plane location. This extended location is used when creating provisioned clusters (Hybrid AKS clusters).</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The type (kind) of the cluster. When specified, the value must exactly match the kind configured on the cluster manager that manages the cluster. If omitted, the service will default the value to the kind value of the cluster manager. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulVersionUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the end of the last successful version update for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedCredentials" /></td>
    <td><code>array</code></td>
    <td>The list of credentials that are managed for the cluster and can be rotated on-demand.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the managed resource group associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="manualActionCount" /></td>
    <td><code>integer</code></td>
    <td>The count of Manual Action Taken (MAT) events that have not been validated.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Fabric associated with the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Validating", and "Updating". (Succeeded, Failed, Canceled, Accepted, Validating, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeProtectionConfiguration" /></td>
    <td><code>object</code></td>
    <td>The settings for cluster runtime protection.</td>
</tr>
<tr>
    <td><CopyableCode code="secretArchive" /></td>
    <td><code>object</code></td>
    <td>The configuration for use of a key vault to store secrets for later retrieval by the operator.</td>
</tr>
<tr>
    <td><CopyableCode code="secretArchiveSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the secret archive used to hold credentials for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="supportExpiryDate" /></td>
    <td><code>string</code></td>
    <td>The support end date of the runtime version of the cluster.</td>
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
    <td><CopyableCode code="updateStrategy" /></td>
    <td><code>object</code></td>
    <td>The strategy for updating the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="vulnerabilityScanningSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for how security vulnerability scanning is applied to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of workload resource IDs that are hosted within this cluster.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of clusters in the provided resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of clusters in the provided subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new cluster or update the properties of the cluster if it exists.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the properties of the provided cluster, or update the tags associated with the cluster. Properties and tag updates can be done independently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new cluster or update the properties of the cluster if it exists.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided cluster.</td>
</tr>
<tr>
    <td><a href="#continue_update_version"><CopyableCode code="continue_update_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Trigger the continuation of an update for a cluster with a matching update strategy that has paused after completing a segment of the update.</td>
</tr>
<tr>
    <td><a href="#deploy"><CopyableCode code="deploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deploy the cluster using the rack configuration provided during creation.</td>
</tr>
<tr>
    <td><a href="#inspect"><CopyableCode code="inspect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Trigger an inspection of the cluster to perform validation and optional corrective actions based on the supplied additional actions and filters.</td>
</tr>
<tr>
    <td><a href="#rotate_credential"><CopyableCode code="rotate_credential" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-credentials"><code>credentials</code></a></td>
    <td></td>
    <td>Rotate the specified cluster credential.</td>
</tr>
<tr>
    <td><a href="#scan_runtime"><CopyableCode code="scan_runtime" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Triggers the execution of a runtime protection scan to detect and remediate detected issues, in accordance with the cluster configuration.</td>
</tr>
<tr>
    <td><a href="#update_version"><CopyableCode code="update_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetClusterVersion"><code>targetClusterVersion</code></a></td>
    <td></td>
    <td>Update the version of the provided cluster to one of the available supported versions.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The opaque token that the server returns to indicate where to continue listing resources from. This is used for paging through large result sets. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
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

Get properties of the provided cluster.

```sql
SELECT
id,
name,
actionStates,
aggregatorOrSingleRackDefinition,
analyticsOutputSettings,
analyticsWorkspaceId,
availableUpgradeVersions,
clusterCapacity,
clusterConnectionStatus,
clusterExtendedLocation,
clusterLocation,
clusterManagerConnectionStatus,
clusterManagerId,
clusterServicePrincipal,
clusterType,
clusterVersion,
commandOutputSettings,
computeDeploymentThreshold,
computeRackDefinitions,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hybridAksExtendedLocation,
identity,
kind,
lastSuccessfulVersionUpdateTime,
location,
managedCredentials,
managedResourceGroupConfiguration,
manualActionCount,
networkFabricId,
provisioningState,
runtimeProtectionConfiguration,
secretArchive,
secretArchiveSettings,
supportExpiryDate,
systemData,
tags,
type,
updateStrategy,
vulnerabilityScanningSettings,
workloadResourceIds
FROM azure.networkcloud.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of clusters in the provided resource group.

```sql
SELECT
id,
name,
actionStates,
aggregatorOrSingleRackDefinition,
analyticsOutputSettings,
analyticsWorkspaceId,
availableUpgradeVersions,
clusterCapacity,
clusterConnectionStatus,
clusterExtendedLocation,
clusterLocation,
clusterManagerConnectionStatus,
clusterManagerId,
clusterServicePrincipal,
clusterType,
clusterVersion,
commandOutputSettings,
computeDeploymentThreshold,
computeRackDefinitions,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hybridAksExtendedLocation,
identity,
kind,
lastSuccessfulVersionUpdateTime,
location,
managedCredentials,
managedResourceGroupConfiguration,
manualActionCount,
networkFabricId,
provisioningState,
runtimeProtectionConfiguration,
secretArchive,
secretArchiveSettings,
supportExpiryDate,
systemData,
tags,
type,
updateStrategy,
vulnerabilityScanningSettings,
workloadResourceIds
FROM azure.networkcloud.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of clusters in the provided subscription.

```sql
SELECT
id,
name,
actionStates,
aggregatorOrSingleRackDefinition,
analyticsOutputSettings,
analyticsWorkspaceId,
availableUpgradeVersions,
clusterCapacity,
clusterConnectionStatus,
clusterExtendedLocation,
clusterLocation,
clusterManagerConnectionStatus,
clusterManagerId,
clusterServicePrincipal,
clusterType,
clusterVersion,
commandOutputSettings,
computeDeploymentThreshold,
computeRackDefinitions,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hybridAksExtendedLocation,
identity,
kind,
lastSuccessfulVersionUpdateTime,
location,
managedCredentials,
managedResourceGroupConfiguration,
manualActionCount,
networkFabricId,
provisioningState,
runtimeProtectionConfiguration,
secretArchive,
secretArchiveSettings,
supportExpiryDate,
systemData,
tags,
type,
updateStrategy,
vulnerabilityScanningSettings,
workloadResourceIds
FROM azure.networkcloud.clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Create a new cluster or update the properties of the cluster if it exists.

```sql
INSERT INTO azure.networkcloud.clusters (
tags,
location,
properties,
extendedLocation,
identity,
kind,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}' /* required */,
'{{ identity }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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
- name: clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the clusters resource.
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
        The list of the resource properties. Required.
      value:
        aggregatorOrSingleRackDefinition:
          availabilityZone: "{{ availabilityZone }}"
          bareMetalMachineConfigurationData:
            - bmcConnectionString: "{{ bmcConnectionString }}"
              bmcCredentials:
                password: "{{ password }}"
                username: "{{ username }}"
              bmcMacAddress: "{{ bmcMacAddress }}"
              bootMacAddress: "{{ bootMacAddress }}"
              machineDetails: "{{ machineDetails }}"
              machineName: "{{ machineName }}"
              rackSlot: {{ rackSlot }}
              serialNumber: "{{ serialNumber }}"
          networkRackId: "{{ networkRackId }}"
          rackLocation: "{{ rackLocation }}"
          rackSerialNumber: "{{ rackSerialNumber }}"
          rackSkuId: "{{ rackSkuId }}"
          storageApplianceConfigurationData:
            - adminCredentials:
                password: "{{ password }}"
                username: "{{ username }}"
              rackSlot: {{ rackSlot }}
              serialNumber: "{{ serialNumber }}"
              storageApplianceName: "{{ storageApplianceName }}"
        analyticsOutputSettings:
          analyticsWorkspaceId: "{{ analyticsWorkspaceId }}"
          associatedIdentity:
            identityType: "{{ identityType }}"
            userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
        analyticsWorkspaceId: "{{ analyticsWorkspaceId }}"
        clusterLocation: "{{ clusterLocation }}"
        clusterServicePrincipal:
          applicationId: "{{ applicationId }}"
          password: "{{ password }}"
          principalId: "{{ principalId }}"
          tenantId: "{{ tenantId }}"
        clusterType: "{{ clusterType }}"
        clusterVersion: "{{ clusterVersion }}"
        commandOutputSettings:
          associatedIdentity:
            identityType: "{{ identityType }}"
            userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
          containerUrl: "{{ containerUrl }}"
          overrides:
            - associatedIdentity:
                identityType: "{{ identityType }}"
                userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
              commandOutputType: "{{ commandOutputType }}"
              containerUrl: "{{ containerUrl }}"
        computeDeploymentThreshold:
          grouping: "{{ grouping }}"
          type: "{{ type }}"
          value: {{ value }}
        computeRackDefinitions:
          - availabilityZone: "{{ availabilityZone }}"
            bareMetalMachineConfigurationData: "{{ bareMetalMachineConfigurationData }}"
            networkRackId: "{{ networkRackId }}"
            rackLocation: "{{ rackLocation }}"
            rackSerialNumber: "{{ rackSerialNumber }}"
            rackSkuId: "{{ rackSkuId }}"
            storageApplianceConfigurationData: "{{ storageApplianceConfigurationData }}"
        managedResourceGroupConfiguration:
          location: "{{ location }}"
          name: "{{ name }}"
        networkFabricId: "{{ networkFabricId }}"
        runtimeProtectionConfiguration:
          definitionUpdateMode: "{{ definitionUpdateMode }}"
          enforcementLevel: "{{ enforcementLevel }}"
        secretArchive:
          keyVaultId: "{{ keyVaultId }}"
          useKeyVault: "{{ useKeyVault }}"
        secretArchiveSettings:
          associatedIdentity:
            identityType: "{{ identityType }}"
            userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
          vaultUri: "{{ vaultUri }}"
        updateStrategy:
          maxUnavailable: {{ maxUnavailable }}
          strategyType: "{{ strategyType }}"
          thresholdType: "{{ thresholdType }}"
          thresholdValue: {{ thresholdValue }}
          waitTimeMinutes: {{ waitTimeMinutes }}
        vulnerabilityScanningSettings:
          containerScan: "{{ containerScan }}"
        actionStates:
          - actionType: "{{ actionType }}"
            correlationId: "{{ correlationId }}"
            endTime: "{{ endTime }}"
            message: "{{ message }}"
            startTime: "{{ startTime }}"
            status: "{{ status }}"
            stepStates: "{{ stepStates }}"
        availableUpgradeVersions:
          - controlImpact: "{{ controlImpact }}"
            expectedDuration: "{{ expectedDuration }}"
            impactDescription: "{{ impactDescription }}"
            supportExpiryDate: "{{ supportExpiryDate }}"
            targetClusterVersion: "{{ targetClusterVersion }}"
            workloadImpact: "{{ workloadImpact }}"
        clusterCapacity:
          availableApplianceStorageGB: {{ availableApplianceStorageGB }}
          availableCoreCount: {{ availableCoreCount }}
          availableHostStorageGB: {{ availableHostStorageGB }}
          availableMemoryGB: {{ availableMemoryGB }}
          totalApplianceStorageGB: {{ totalApplianceStorageGB }}
          totalCoreCount: {{ totalCoreCount }}
          totalHostStorageGB: {{ totalHostStorageGB }}
          totalMemoryGB: {{ totalMemoryGB }}
        clusterConnectionStatus: "{{ clusterConnectionStatus }}"
        clusterExtendedLocation:
          name: "{{ name }}"
          type: "{{ type }}"
        clusterManagerConnectionStatus: "{{ clusterManagerConnectionStatus }}"
        clusterManagerId: "{{ clusterManagerId }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        hybridAksExtendedLocation:
          name: "{{ name }}"
          type: "{{ type }}"
        lastSuccessfulVersionUpdateTime: "{{ lastSuccessfulVersionUpdateTime }}"
        managedCredentials:
          - "{{ managedCredentials }}"
        manualActionCount: {{ manualActionCount }}
        supportExpiryDate: "{{ supportExpiryDate }}"
        workloadResourceIds:
          - "{{ workloadResourceIds }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extended location of the resource. This property is required when creating the resource. Required.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The type (kind) of the cluster. When specified, the value must exactly match the kind configured on the cluster manager that manages the cluster. If omitted, the service will default the value to the kind value of the cluster manager. Known values are: "Nexus" and "AzureLocal".
      valid_values: ['Nexus', 'AzureLocal']
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

Patch the properties of the provided cluster, or update the tags associated with the cluster. Properties and tag updates can be done independently.

```sql
UPDATE azure.networkcloud.clusters
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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

Create a new cluster or update the properties of the cluster if it exists.

```sql
REPLACE azure.networkcloud.clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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

Delete the provided cluster.

```sql
DELETE FROM azure.networkcloud.clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="continue_update_version"
    values={[
        { label: 'continue_update_version', value: 'continue_update_version' },
        { label: 'deploy', value: 'deploy' },
        { label: 'inspect', value: 'inspect' },
        { label: 'rotate_credential', value: 'rotate_credential' },
        { label: 'scan_runtime', value: 'scan_runtime' },
        { label: 'update_version', value: 'update_version' }
    ]}
>
<TabItem value="continue_update_version">

Trigger the continuation of an update for a cluster with a matching update strategy that has paused after completing a segment of the update.

```sql
EXEC azure.networkcloud.clusters.continue_update_version 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"machineGroupTargetingMode": "{{ machineGroupTargetingMode }}", 
"safeguardMode": "{{ safeguardMode }}"
}'
;
```
</TabItem>
<TabItem value="deploy">

Deploy the cluster using the rack configuration provided during creation.

```sql
EXEC azure.networkcloud.clusters.deploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"skipValidationsForMachines": "{{ skipValidationsForMachines }}"
}'
;
```
</TabItem>
<TabItem value="inspect">

Trigger an inspection of the cluster to perform validation and optional corrective actions based on the supplied additional actions and filters.

```sql
EXEC azure.networkcloud.clusters.inspect 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"additionalActions": "{{ additionalActions }}", 
"filterDevices": "{{ filterDevices }}"
}'
;
```
</TabItem>
<TabItem value="rotate_credential">

Rotate the specified cluster credential.

```sql
EXEC azure.networkcloud.clusters.rotate_credential 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"credentials": "{{ credentials }}"
}'
;
```
</TabItem>
<TabItem value="scan_runtime">

Triggers the execution of a runtime protection scan to detect and remediate detected issues, in accordance with the cluster configuration.

```sql
EXEC azure.networkcloud.clusters.scan_runtime 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"scanActivity": "{{ scanActivity }}"
}'
;
```
</TabItem>
<TabItem value="update_version">

Update the version of the provided cluster to one of the available supported versions.

```sql
EXEC azure.networkcloud.clusters.update_version 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"safeguardMode": "{{ safeguardMode }}", 
"targetClusterVersion": "{{ targetClusterVersion }}"
}'
;
```
</TabItem>
</Tabs>
