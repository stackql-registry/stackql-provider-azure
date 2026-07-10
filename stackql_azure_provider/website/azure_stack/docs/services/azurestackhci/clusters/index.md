--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - azurestackhci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azurestackhci.clusters" /></td></tr>
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
    <td><CopyableCode code="aadApplicationObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="aadClientId" /></td>
    <td><code>string</code></td>
    <td>App id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="aadServicePrincipalObjectId" /></td>
    <td><code>string</code></td>
    <td>Id of cluster identity service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="aadTenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="billingModel" /></td>
    <td><code>string</code></td>
    <td>Type of billing applied to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProperties" /></td>
    <td><code>object</code></td>
    <td>Billing properties of the cluster, including upcoming billing model details.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint configured for management from the Azure portal.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterPattern" /></td>
    <td><code>string</code></td>
    <td>Supported Storage Type for HCI Cluster. Known values are: "Standard" and "RackAware". (Standard, RackAware)</td>
</tr>
<tr>
    <td><CopyableCode code="confidentialVmProperties" /></td>
    <td><code>object</code></td>
    <td>Represents the Confidential Virtual Machine (CVM) support intent and current status for the cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>Overall connectivity status for the cluster resource. Indicates whether the cluster is connected to Azure, partially connected, or has not recently communicated. Known values are: "NotYetRegistered", "Connected", "NotConnectedRecently", "PartiallyConnected", "Disconnected", and "NotSpecified". (NotYetRegistered, Connected, NotConnectedRecently, PartiallyConnected, Disconnected, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="desiredProperties" /></td>
    <td><code>object</code></td>
    <td>Desired properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProvider" /></td>
    <td><code>string</code></td>
    <td>Identity Provider for the cluster. Known values are: "ActiveDirectory" and "LocalIdentity". (ActiveDirectory, LocalIdentity)</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementCluster" /></td>
    <td><code>boolean</code></td>
    <td>Is Management Cluster, when true indicates that the cluster is used for managing other clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="isolatedVmAttestationConfiguration" /></td>
    <td><code>object</code></td>
    <td>Attestation configurations for isolated VM (e.g. TVM, CVM) of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>This property identifies the purpose of the Cluster deployment. For example, a valid value is AzureLocal.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBillingTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Most recent billing meter timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Most recent cluster sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="localAvailabilityZones" /></td>
    <td><code>array</code></td>
    <td>Local Availability Zone information for HCI cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logCollectionProperties" /></td>
    <td><code>object</code></td>
    <td>Log Collection properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Indicates the current lifecycle status of the resource, including creation, update, deletion, connectivity, and error states. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>First cluster sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteSupportProperties" /></td>
    <td><code>object</code></td>
    <td>RemoteSupport properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Properties reported by cluster agent.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProviderObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of RP Service Principal.</td>
</tr>
<tr>
    <td><CopyableCode code="ring" /></td>
    <td><code>string</code></td>
    <td>The ring to which this cluster belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="sdnProperties" /></td>
    <td><code>object</code></td>
    <td>Software Defined Networking Properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="secretsLocations" /></td>
    <td><code>array</code></td>
    <td>List of secret locations.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoint" /></td>
    <td><code>string</code></td>
    <td>Region specific DataPath Endpoint of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareAssuranceProperties" /></td>
    <td><code>object</code></td>
    <td>Software Assurance properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the cluster agent. Indicates the current connectivity, validation, and deployment state of the agent within the cluster. Known values are: "NotYetRegistered", "ConnectedRecently", "NotConnectedRecently", "Disconnected", "Error", "NotSpecified", "ValidationInProgress", "ValidationSuccess", "ValidationFailed", "DeploymentInProgress", "DeploymentFailed", and "DeploymentSuccess". (NotYetRegistered, ConnectedRecently, NotConnectedRecently, Disconnected, Error, NotSpecified, ValidationInProgress, ValidationSuccess, ValidationFailed, DeploymentInProgress, DeploymentFailed, DeploymentSuccess)</td>
</tr>
<tr>
    <td><CopyableCode code="storageType" /></td>
    <td><code>string</code></td>
    <td>Storage type of the cluster. Indicates whether the cluster uses S2D, SAN, or a combination. Known values are: "S2D", "SAN", and "SANS2D". (S2D, SAN, SANS2D)</td>
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
    <td><CopyableCode code="trialDaysRemaining" /></td>
    <td><code>number</code></td>
    <td>Number of days remaining in the trial period.</td>
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
    <td><CopyableCode code="aadApplicationObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="aadClientId" /></td>
    <td><code>string</code></td>
    <td>App id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="aadServicePrincipalObjectId" /></td>
    <td><code>string</code></td>
    <td>Id of cluster identity service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="aadTenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="billingModel" /></td>
    <td><code>string</code></td>
    <td>Type of billing applied to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProperties" /></td>
    <td><code>object</code></td>
    <td>Billing properties of the cluster, including upcoming billing model details.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint configured for management from the Azure portal.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterPattern" /></td>
    <td><code>string</code></td>
    <td>Supported Storage Type for HCI Cluster. Known values are: "Standard" and "RackAware". (Standard, RackAware)</td>
</tr>
<tr>
    <td><CopyableCode code="confidentialVmProperties" /></td>
    <td><code>object</code></td>
    <td>Represents the Confidential Virtual Machine (CVM) support intent and current status for the cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>Overall connectivity status for the cluster resource. Indicates whether the cluster is connected to Azure, partially connected, or has not recently communicated. Known values are: "NotYetRegistered", "Connected", "NotConnectedRecently", "PartiallyConnected", "Disconnected", and "NotSpecified". (NotYetRegistered, Connected, NotConnectedRecently, PartiallyConnected, Disconnected, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="desiredProperties" /></td>
    <td><code>object</code></td>
    <td>Desired properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProvider" /></td>
    <td><code>string</code></td>
    <td>Identity Provider for the cluster. Known values are: "ActiveDirectory" and "LocalIdentity". (ActiveDirectory, LocalIdentity)</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementCluster" /></td>
    <td><code>boolean</code></td>
    <td>Is Management Cluster, when true indicates that the cluster is used for managing other clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="isolatedVmAttestationConfiguration" /></td>
    <td><code>object</code></td>
    <td>Attestation configurations for isolated VM (e.g. TVM, CVM) of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>This property identifies the purpose of the Cluster deployment. For example, a valid value is AzureLocal.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBillingTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Most recent billing meter timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Most recent cluster sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="localAvailabilityZones" /></td>
    <td><code>array</code></td>
    <td>Local Availability Zone information for HCI cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logCollectionProperties" /></td>
    <td><code>object</code></td>
    <td>Log Collection properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Indicates the current lifecycle status of the resource, including creation, update, deletion, connectivity, and error states. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>First cluster sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteSupportProperties" /></td>
    <td><code>object</code></td>
    <td>RemoteSupport properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Properties reported by cluster agent.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProviderObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of RP Service Principal.</td>
</tr>
<tr>
    <td><CopyableCode code="ring" /></td>
    <td><code>string</code></td>
    <td>The ring to which this cluster belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="sdnProperties" /></td>
    <td><code>object</code></td>
    <td>Software Defined Networking Properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="secretsLocations" /></td>
    <td><code>array</code></td>
    <td>List of secret locations.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoint" /></td>
    <td><code>string</code></td>
    <td>Region specific DataPath Endpoint of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareAssuranceProperties" /></td>
    <td><code>object</code></td>
    <td>Software Assurance properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the cluster agent. Indicates the current connectivity, validation, and deployment state of the agent within the cluster. Known values are: "NotYetRegistered", "ConnectedRecently", "NotConnectedRecently", "Disconnected", "Error", "NotSpecified", "ValidationInProgress", "ValidationSuccess", "ValidationFailed", "DeploymentInProgress", "DeploymentFailed", and "DeploymentSuccess". (NotYetRegistered, ConnectedRecently, NotConnectedRecently, Disconnected, Error, NotSpecified, ValidationInProgress, ValidationSuccess, ValidationFailed, DeploymentInProgress, DeploymentFailed, DeploymentSuccess)</td>
</tr>
<tr>
    <td><CopyableCode code="storageType" /></td>
    <td><code>string</code></td>
    <td>Storage type of the cluster. Indicates whether the cluster uses S2D, SAN, or a combination. Known values are: "S2D", "SAN", and "SANS2D". (S2D, SAN, SANS2D)</td>
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
    <td><CopyableCode code="trialDaysRemaining" /></td>
    <td><code>number</code></td>
    <td>Number of days remaining in the trial period.</td>
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
    <td><CopyableCode code="aadApplicationObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="aadClientId" /></td>
    <td><code>string</code></td>
    <td>App id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="aadServicePrincipalObjectId" /></td>
    <td><code>string</code></td>
    <td>Id of cluster identity service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="aadTenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant id of cluster AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="billingModel" /></td>
    <td><code>string</code></td>
    <td>Type of billing applied to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProperties" /></td>
    <td><code>object</code></td>
    <td>Billing properties of the cluster, including upcoming billing model details.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint configured for management from the Azure portal.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterPattern" /></td>
    <td><code>string</code></td>
    <td>Supported Storage Type for HCI Cluster. Known values are: "Standard" and "RackAware". (Standard, RackAware)</td>
</tr>
<tr>
    <td><CopyableCode code="confidentialVmProperties" /></td>
    <td><code>object</code></td>
    <td>Represents the Confidential Virtual Machine (CVM) support intent and current status for the cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>Overall connectivity status for the cluster resource. Indicates whether the cluster is connected to Azure, partially connected, or has not recently communicated. Known values are: "NotYetRegistered", "Connected", "NotConnectedRecently", "PartiallyConnected", "Disconnected", and "NotSpecified". (NotYetRegistered, Connected, NotConnectedRecently, PartiallyConnected, Disconnected, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="desiredProperties" /></td>
    <td><code>object</code></td>
    <td>Desired properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProvider" /></td>
    <td><code>string</code></td>
    <td>Identity Provider for the cluster. Known values are: "ActiveDirectory" and "LocalIdentity". (ActiveDirectory, LocalIdentity)</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementCluster" /></td>
    <td><code>boolean</code></td>
    <td>Is Management Cluster, when true indicates that the cluster is used for managing other clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="isolatedVmAttestationConfiguration" /></td>
    <td><code>object</code></td>
    <td>Attestation configurations for isolated VM (e.g. TVM, CVM) of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>This property identifies the purpose of the Cluster deployment. For example, a valid value is AzureLocal.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBillingTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Most recent billing meter timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Most recent cluster sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="localAvailabilityZones" /></td>
    <td><code>array</code></td>
    <td>Local Availability Zone information for HCI cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logCollectionProperties" /></td>
    <td><code>object</code></td>
    <td>Log Collection properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Indicates the current lifecycle status of the resource, including creation, update, deletion, connectivity, and error states. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>First cluster sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteSupportProperties" /></td>
    <td><code>object</code></td>
    <td>RemoteSupport properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Properties reported by cluster agent.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProviderObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of RP Service Principal.</td>
</tr>
<tr>
    <td><CopyableCode code="ring" /></td>
    <td><code>string</code></td>
    <td>The ring to which this cluster belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="sdnProperties" /></td>
    <td><code>object</code></td>
    <td>Software Defined Networking Properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="secretsLocations" /></td>
    <td><code>array</code></td>
    <td>List of secret locations.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoint" /></td>
    <td><code>string</code></td>
    <td>Region specific DataPath Endpoint of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareAssuranceProperties" /></td>
    <td><code>object</code></td>
    <td>Software Assurance properties of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the cluster agent. Indicates the current connectivity, validation, and deployment state of the agent within the cluster. Known values are: "NotYetRegistered", "ConnectedRecently", "NotConnectedRecently", "Disconnected", "Error", "NotSpecified", "ValidationInProgress", "ValidationSuccess", "ValidationFailed", "DeploymentInProgress", "DeploymentFailed", and "DeploymentSuccess". (NotYetRegistered, ConnectedRecently, NotConnectedRecently, Disconnected, Error, NotSpecified, ValidationInProgress, ValidationSuccess, ValidationFailed, DeploymentInProgress, DeploymentFailed, DeploymentSuccess)</td>
</tr>
<tr>
    <td><CopyableCode code="storageType" /></td>
    <td><code>string</code></td>
    <td>Storage type of the cluster. Indicates whether the cluster uses S2D, SAN, or a combination. Known values are: "S2D", "SAN", and "SANS2D". (S2D, SAN, SANS2D)</td>
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
    <td><CopyableCode code="trialDaysRemaining" /></td>
    <td><code>number</code></td>
    <td>Number of days remaining in the trial period.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get HCI cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all HCI clusters in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all HCI clusters in a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create an HCI cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an HCI cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an HCI cluster.</td>
</tr>
<tr>
    <td><a href="#update_secrets_locations"><CopyableCode code="update_secrets_locations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update cluster secrets locations.</td>
</tr>
<tr>
    <td><a href="#upload_certificate"><CopyableCode code="upload_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upload certificate.</td>
</tr>
<tr>
    <td><a href="#create_identity"><CopyableCode code="create_identity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create cluster identity.</td>
</tr>
<tr>
    <td><a href="#extend_software_assurance_benefit"><CopyableCode code="extend_software_assurance_benefit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Extends Software Assurance Benefit to a cluster.</td>
</tr>
<tr>
    <td><a href="#change_ring"><CopyableCode code="change_ring" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Changes ring of a cluster.</td>
</tr>
<tr>
    <td><a href="#trigger_log_collection"><CopyableCode code="trigger_log_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Trigger Log Collection on a cluster.</td>
</tr>
<tr>
    <td><a href="#configure_remote_support"><CopyableCode code="configure_remote_support" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Configure RemoteSupport on a cluster.</td>
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

Get HCI cluster.

```sql
SELECT
id,
name,
aadApplicationObjectId,
aadClientId,
aadServicePrincipalObjectId,
aadTenantId,
billingModel,
billingProperties,
cloudId,
cloudManagementEndpoint,
clusterPattern,
confidentialVmProperties,
connectivityStatus,
desiredProperties,
identity,
identityProvider,
isManagementCluster,
isolatedVmAttestationConfiguration,
kind,
lastBillingTimestamp,
lastSyncTimestamp,
localAvailabilityZones,
location,
logCollectionProperties,
provisioningState,
registrationTimestamp,
remoteSupportProperties,
reportedProperties,
resourceProviderObjectId,
ring,
sdnProperties,
secretsLocations,
serviceEndpoint,
softwareAssuranceProperties,
status,
storageType,
systemData,
tags,
trialDaysRemaining,
type
FROM azure_stack.azurestackhci.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all HCI clusters in a resource group.

```sql
SELECT
id,
name,
aadApplicationObjectId,
aadClientId,
aadServicePrincipalObjectId,
aadTenantId,
billingModel,
billingProperties,
cloudId,
cloudManagementEndpoint,
clusterPattern,
confidentialVmProperties,
connectivityStatus,
desiredProperties,
identity,
identityProvider,
isManagementCluster,
isolatedVmAttestationConfiguration,
kind,
lastBillingTimestamp,
lastSyncTimestamp,
localAvailabilityZones,
location,
logCollectionProperties,
provisioningState,
registrationTimestamp,
remoteSupportProperties,
reportedProperties,
resourceProviderObjectId,
ring,
sdnProperties,
secretsLocations,
serviceEndpoint,
softwareAssuranceProperties,
status,
storageType,
systemData,
tags,
trialDaysRemaining,
type
FROM azure_stack.azurestackhci.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all HCI clusters in a subscription.

```sql
SELECT
id,
name,
aadApplicationObjectId,
aadClientId,
aadServicePrincipalObjectId,
aadTenantId,
billingModel,
billingProperties,
cloudId,
cloudManagementEndpoint,
clusterPattern,
confidentialVmProperties,
connectivityStatus,
desiredProperties,
identity,
identityProvider,
isManagementCluster,
isolatedVmAttestationConfiguration,
kind,
lastBillingTimestamp,
lastSyncTimestamp,
localAvailabilityZones,
location,
logCollectionProperties,
provisioningState,
registrationTimestamp,
remoteSupportProperties,
reportedProperties,
resourceProviderObjectId,
ring,
sdnProperties,
secretsLocations,
serviceEndpoint,
softwareAssuranceProperties,
status,
storageType,
systemData,
tags,
trialDaysRemaining,
type
FROM azure_stack.azurestackhci.clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create an HCI cluster.

```sql
INSERT INTO azure_stack.azurestackhci.clusters (
tags,
location,
properties,
identity,
kind,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
        Cluster properties.
      value:
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        connectivityStatus: "{{ connectivityStatus }}"
        cloudId: "{{ cloudId }}"
        ring: "{{ ring }}"
        cloudManagementEndpoint: "{{ cloudManagementEndpoint }}"
        aadClientId: "{{ aadClientId }}"
        aadTenantId: "{{ aadTenantId }}"
        aadApplicationObjectId: "{{ aadApplicationObjectId }}"
        aadServicePrincipalObjectId: "{{ aadServicePrincipalObjectId }}"
        softwareAssuranceProperties:
          softwareAssuranceStatus: "{{ softwareAssuranceStatus }}"
          softwareAssuranceIntent: "{{ softwareAssuranceIntent }}"
          lastUpdated: "{{ lastUpdated }}"
        isManagementCluster: {{ isManagementCluster }}
        logCollectionProperties:
          fromDate: "{{ fromDate }}"
          toDate: "{{ toDate }}"
          lastLogGenerated: "{{ lastLogGenerated }}"
          logCollectionSessionDetails:
            - logStartTime: "{{ logStartTime }}"
              logEndTime: "{{ logEndTime }}"
              timeCollected: "{{ timeCollected }}"
              logSize: {{ logSize }}
              logCollectionStatus: "{{ logCollectionStatus }}"
              correlationId: "{{ correlationId }}"
              logCollectionJobType: "{{ logCollectionJobType }}"
              endTimeCollected: "{{ endTimeCollected }}"
              logCollectionError:
                errorCode: "{{ errorCode }}"
                errorMessage: "{{ errorMessage }}"
        remoteSupportProperties:
          accessLevel: "{{ accessLevel }}"
          expirationTimeStamp: "{{ expirationTimeStamp }}"
          remoteSupportType: "{{ remoteSupportType }}"
          remoteSupportNodeSettings:
            - arcResourceId: "{{ arcResourceId }}"
              state: "{{ state }}"
              createdAt: "{{ createdAt }}"
              updatedAt: "{{ updatedAt }}"
              connectionStatus: "{{ connectionStatus }}"
              connectionErrorMessage: "{{ connectionErrorMessage }}"
              transcriptLocation: "{{ transcriptLocation }}"
          remoteSupportSessionDetails:
            - sessionStartTime: "{{ sessionStartTime }}"
              sessionEndTime: "{{ sessionEndTime }}"
              nodeName: "{{ nodeName }}"
              duration: {{ duration }}
              accessLevel: "{{ accessLevel }}"
              transcriptLocation: "{{ transcriptLocation }}"
          remoteSupportProvisioningState: "{{ remoteSupportProvisioningState }}"
        desiredProperties:
          windowsServerSubscription: "{{ windowsServerSubscription }}"
          diagnosticLevel: "{{ diagnosticLevel }}"
        reportedProperties:
          clusterName: "{{ clusterName }}"
          clusterId: "{{ clusterId }}"
          clusterVersion: "{{ clusterVersion }}"
          nodes:
            - name: "{{ name }}"
              id: {{ id }}
              windowsServerSubscription: "{{ windowsServerSubscription }}"
              nodeType: "{{ nodeType }}"
              ehcResourceId: "{{ ehcResourceId }}"
              manufacturer: "{{ manufacturer }}"
              model: "{{ model }}"
              osName: "{{ osName }}"
              osVersion: "{{ osVersion }}"
              osDisplayVersion: "{{ osDisplayVersion }}"
              serialNumber: "{{ serialNumber }}"
              coreCount: {{ coreCount }}
              memoryInGiB: {{ memoryInGiB }}
              lastLicensingTimestamp: "{{ lastLicensingTimestamp }}"
              oemActivation: "{{ oemActivation }}"
          lastUpdated: "{{ lastUpdated }}"
          msiExpirationTimeStamp: "{{ msiExpirationTimeStamp }}"
          imdsAttestation: "{{ imdsAttestation }}"
          diagnosticLevel: "{{ diagnosticLevel }}"
          supportedCapabilities:
            - "{{ supportedCapabilities }}"
          clusterType: "{{ clusterType }}"
          manufacturer: "{{ manufacturer }}"
          oemActivation: "{{ oemActivation }}"
          hardwareClass: "{{ hardwareClass }}"
        isolatedVmAttestationConfiguration:
          attestationResourceId: "{{ attestationResourceId }}"
          relyingPartyServiceEndpoint: "{{ relyingPartyServiceEndpoint }}"
          attestationServiceEndpoint: "{{ attestationServiceEndpoint }}"
        trialDaysRemaining: {{ trialDaysRemaining }}
        billingModel: "{{ billingModel }}"
        billingProperties:
          nextBillingModel:
            billingModel: "{{ billingModel }}"
            capabilitiesEnabled:
              - "{{ capabilitiesEnabled }}"
            trialDaysRemaining: {{ trialDaysRemaining }}
        registrationTimestamp: "{{ registrationTimestamp }}"
        lastSyncTimestamp: "{{ lastSyncTimestamp }}"
        lastBillingTimestamp: "{{ lastBillingTimestamp }}"
        serviceEndpoint: "{{ serviceEndpoint }}"
        resourceProviderObjectId: "{{ resourceProviderObjectId }}"
        secretsLocations:
          - secretsType: "{{ secretsType }}"
            secretsLocation: "{{ secretsLocation }}"
        clusterPattern: "{{ clusterPattern }}"
        confidentialVmProperties:
          confidentialVmIntent: "{{ confidentialVmIntent }}"
          confidentialVmStatus: "{{ confidentialVmStatus }}"
          confidentialVmStatusSummary: "{{ confidentialVmStatusSummary }}"
        sdnProperties:
          sdnStatus: "{{ sdnStatus }}"
          sdnDomainName: "{{ sdnDomainName }}"
          sdnApiAddress: "{{ sdnApiAddress }}"
          sdnIntegrationIntent: "{{ sdnIntegrationIntent }}"
        localAvailabilityZones:
          - localAvailabilityZoneName: "{{ localAvailabilityZoneName }}"
            nodes: "{{ nodes }}"
        identityProvider: "{{ identityProvider }}"
        storageType: "{{ storageType }}"
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
        This property identifies the purpose of the Cluster deployment. For example, a valid value is AzureLocal.
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

Update an HCI cluster.

```sql
UPDATE azure_stack.azurestackhci.clusters
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete an HCI cluster.

```sql
DELETE FROM azure_stack.azurestackhci.clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_secrets_locations"
    values={[
        { label: 'update_secrets_locations', value: 'update_secrets_locations' },
        { label: 'upload_certificate', value: 'upload_certificate' },
        { label: 'create_identity', value: 'create_identity' },
        { label: 'extend_software_assurance_benefit', value: 'extend_software_assurance_benefit' },
        { label: 'change_ring', value: 'change_ring' },
        { label: 'trigger_log_collection', value: 'trigger_log_collection' },
        { label: 'configure_remote_support', value: 'configure_remote_support' }
    ]}
>
<TabItem value="update_secrets_locations">

Update cluster secrets locations.

```sql
EXEC azure_stack.azurestackhci.clusters.update_secrets_locations 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="upload_certificate">

Upload certificate.

```sql
EXEC azure_stack.azurestackhci.clusters.upload_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_identity">

Create cluster identity.

```sql
EXEC azure_stack.azurestackhci.clusters.create_identity 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="extend_software_assurance_benefit">

Extends Software Assurance Benefit to a cluster.

```sql
EXEC azure_stack.azurestackhci.clusters.extend_software_assurance_benefit 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="change_ring">

Changes ring of a cluster.

```sql
EXEC azure_stack.azurestackhci.clusters.change_ring 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="trigger_log_collection">

Trigger Log Collection on a cluster.

```sql
EXEC azure_stack.azurestackhci.clusters.trigger_log_collection 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="configure_remote_support">

Configure RemoteSupport on a cluster.

```sql
EXEC azure_stack.azurestackhci.clusters.configure_remote_support 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
