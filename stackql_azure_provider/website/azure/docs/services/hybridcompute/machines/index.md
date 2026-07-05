--- 
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
  - hybridcompute
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

Creates, updates, deletes, gets or lists a <code>machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="machines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridcompute.machines" /></td></tr>
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
    <td><CopyableCode code="adFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the AD fully qualified display name.</td>
</tr>
<tr>
    <td><CopyableCode code="agentConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configurable properties that the user can set locally via the azcmagent config command, or remotely via ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="agentUpgrade" /></td>
    <td><code>object</code></td>
    <td>The info of the machine w.r.t Agent Upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>The hybrid machine agent full version.</td>
</tr>
<tr>
    <td><CopyableCode code="clientPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public Key that the client provides to be used during initial resource onboarding.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudMetadata" /></td>
    <td><code>object</code></td>
    <td>The metadata of the cloud environment (Azure/GCP/AWS/OCI...).</td>
</tr>
<tr>
    <td><CopyableCode code="detectedProperties" /></td>
    <td><code>object</code></td>
    <td>Detected properties from the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine display name.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the DNS fully qualified display name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainName" /></td>
    <td><code>string</code></td>
    <td>Specifies the Windows domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>Details about the error state.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Machine Extensions information (deprecated field).</td>
</tr>
<tr>
    <td><CopyableCode code="firmwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's firmware.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's hardware.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareResourceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the resource ID of the associated hardware device. Only settable by HCI RP.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identityKeyStore" /></td>
    <td><code>string</code></td>
    <td>Specifies the identity key store a machine is using. Known values are: "TPM" and "Default". (TPM, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates which kind of Arc machine placement on-premises, such as HCI, SCVMM or VMware etc. Known values are: "AVS", "HCI", "SCVMM", "VMware", "EPS", "GCP", and "AWS". (AVS, HCI, SCVMM, VMware, EPS, GCP, AWS)</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusChange" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the last status change.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the License related properties for a machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="locationData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to the geographic location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="machineFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine FQDN.</td>
</tr>
<tr>
    <td><CopyableCode code="mssqlDiscovered" /></td>
    <td><code>string</code></td>
    <td>Specifies whether any MS SQL instance is discovered on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the network the machine is on.</td>
</tr>
<tr>
    <td><CopyableCode code="osEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of the Operating System.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>The Operating System running on the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osSku" /></td>
    <td><code>string</code></td>
    <td>Specifies the Operating System product SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The type of Operating System (windows/linux).</td>
</tr>
<tr>
    <td><CopyableCode code="osVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Operating System running on the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="parentClusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the parent cluster (Azure HCI) this machine is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopeResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the private link scope this machine is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The list of extensions affiliated to the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceStatuses" /></td>
    <td><code>object</code></td>
    <td>Statuses of dependent services that are reported back to ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the hybrid machine agent. Known values are: "Connected", "Disconnected", "Error", and "AwaitingConnection". (Connected, Disconnected, Error, AwaitingConnection)</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's storage.</td>
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
    <td><CopyableCode code="tpmEkCertificate" /></td>
    <td><code>string</code></td>
    <td>Endorsement Key Certificate of the Trusted Platform Module (TPM) that the client provides to be used during initial resource onboarding.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="vmUuid" /></td>
    <td><code>string</code></td>
    <td>Specifies the Arc Machine's unique SMBIOS ID.</td>
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
    <td><CopyableCode code="adFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the AD fully qualified display name.</td>
</tr>
<tr>
    <td><CopyableCode code="agentConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configurable properties that the user can set locally via the azcmagent config command, or remotely via ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="agentUpgrade" /></td>
    <td><code>object</code></td>
    <td>The info of the machine w.r.t Agent Upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>The hybrid machine agent full version.</td>
</tr>
<tr>
    <td><CopyableCode code="clientPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public Key that the client provides to be used during initial resource onboarding.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudMetadata" /></td>
    <td><code>object</code></td>
    <td>The metadata of the cloud environment (Azure/GCP/AWS/OCI...).</td>
</tr>
<tr>
    <td><CopyableCode code="detectedProperties" /></td>
    <td><code>object</code></td>
    <td>Detected properties from the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine display name.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the DNS fully qualified display name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainName" /></td>
    <td><code>string</code></td>
    <td>Specifies the Windows domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>Details about the error state.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Machine Extensions information (deprecated field).</td>
</tr>
<tr>
    <td><CopyableCode code="firmwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's firmware.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's hardware.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareResourceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the resource ID of the associated hardware device. Only settable by HCI RP.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identityKeyStore" /></td>
    <td><code>string</code></td>
    <td>Specifies the identity key store a machine is using. Known values are: "TPM" and "Default". (TPM, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates which kind of Arc machine placement on-premises, such as HCI, SCVMM or VMware etc. Known values are: "AVS", "HCI", "SCVMM", "VMware", "EPS", "GCP", and "AWS". (AVS, HCI, SCVMM, VMware, EPS, GCP, AWS)</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusChange" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the last status change.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the License related properties for a machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="locationData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to the geographic location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="machineFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine FQDN.</td>
</tr>
<tr>
    <td><CopyableCode code="mssqlDiscovered" /></td>
    <td><code>string</code></td>
    <td>Specifies whether any MS SQL instance is discovered on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the network the machine is on.</td>
</tr>
<tr>
    <td><CopyableCode code="osEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of the Operating System.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>The Operating System running on the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osSku" /></td>
    <td><code>string</code></td>
    <td>Specifies the Operating System product SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The type of Operating System (windows/linux).</td>
</tr>
<tr>
    <td><CopyableCode code="osVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Operating System running on the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="parentClusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the parent cluster (Azure HCI) this machine is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopeResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the private link scope this machine is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The list of extensions affiliated to the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceStatuses" /></td>
    <td><code>object</code></td>
    <td>Statuses of dependent services that are reported back to ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the hybrid machine agent. Known values are: "Connected", "Disconnected", "Error", and "AwaitingConnection". (Connected, Disconnected, Error, AwaitingConnection)</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's storage.</td>
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
    <td><CopyableCode code="tpmEkCertificate" /></td>
    <td><code>string</code></td>
    <td>Endorsement Key Certificate of the Trusted Platform Module (TPM) that the client provides to be used during initial resource onboarding.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="vmUuid" /></td>
    <td><code>string</code></td>
    <td>Specifies the Arc Machine's unique SMBIOS ID.</td>
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
    <td><CopyableCode code="adFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the AD fully qualified display name.</td>
</tr>
<tr>
    <td><CopyableCode code="agentConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configurable properties that the user can set locally via the azcmagent config command, or remotely via ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="agentUpgrade" /></td>
    <td><code>object</code></td>
    <td>The info of the machine w.r.t Agent Upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>The hybrid machine agent full version.</td>
</tr>
<tr>
    <td><CopyableCode code="clientPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public Key that the client provides to be used during initial resource onboarding.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudMetadata" /></td>
    <td><code>object</code></td>
    <td>The metadata of the cloud environment (Azure/GCP/AWS/OCI...).</td>
</tr>
<tr>
    <td><CopyableCode code="detectedProperties" /></td>
    <td><code>object</code></td>
    <td>Detected properties from the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine display name.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the DNS fully qualified display name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainName" /></td>
    <td><code>string</code></td>
    <td>Specifies the Windows domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>Details about the error state.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Machine Extensions information (deprecated field).</td>
</tr>
<tr>
    <td><CopyableCode code="firmwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's firmware.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's hardware.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareResourceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the resource ID of the associated hardware device. Only settable by HCI RP.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identityKeyStore" /></td>
    <td><code>string</code></td>
    <td>Specifies the identity key store a machine is using. Known values are: "TPM" and "Default". (TPM, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Indicates which kind of Arc machine placement on-premises, such as HCI, SCVMM or VMware etc. Known values are: "AVS", "HCI", "SCVMM", "VMware", "EPS", "GCP", and "AWS". (AVS, HCI, SCVMM, VMware, EPS, GCP, AWS)</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusChange" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the last status change.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the License related properties for a machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="locationData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to the geographic location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="machineFqdn" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine FQDN.</td>
</tr>
<tr>
    <td><CopyableCode code="mssqlDiscovered" /></td>
    <td><code>string</code></td>
    <td>Specifies whether any MS SQL instance is discovered on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the network the machine is on.</td>
</tr>
<tr>
    <td><CopyableCode code="osEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of the Operating System.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>The Operating System running on the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osSku" /></td>
    <td><code>string</code></td>
    <td>Specifies the Operating System product SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The type of Operating System (windows/linux).</td>
</tr>
<tr>
    <td><CopyableCode code="osVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Operating System running on the hybrid machine.</td>
</tr>
<tr>
    <td><CopyableCode code="parentClusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the parent cluster (Azure HCI) this machine is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopeResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the private link scope this machine is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The list of extensions affiliated to the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceStatuses" /></td>
    <td><code>object</code></td>
    <td>Statuses of dependent services that are reported back to ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the hybrid machine agent. Known values are: "Connected", "Disconnected", "Error", and "AwaitingConnection". (Connected, Disconnected, Error, AwaitingConnection)</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Information about the machine's storage.</td>
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
    <td><CopyableCode code="tpmEkCertificate" /></td>
    <td><code>string</code></td>
    <td>Endorsement Key Certificate of the Trusted Platform Module (TPM) that the client provides to be used during initial resource onboarding.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Specifies the hybrid machine unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="vmUuid" /></td>
    <td><code>string</code></td>
    <td>Specifies the Arc Machine's unique SMBIOS ID.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieves information about the model view or the instance view of a hybrid machine.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to create or update a hybrid machine. Please note some properties can be set only during machine creation.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update a hybrid machine.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to create or update a hybrid machine. Please note some properties can be set only during machine creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete a hybrid machine.</td>
</tr>
<tr>
    <td><a href="#assess_patches"><CopyableCode code="assess_patches" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to assess patches on a hybrid machine identity in Azure.</td>
</tr>
<tr>
    <td><a href="#install_patches"><CopyableCode code="install_patches" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-maximumDuration"><code>maximumDuration</code></a>, <a href="#parameter-rebootSetting"><code>rebootSetting</code></a></td>
    <td></td>
    <td>The operation to install patches on a hybrid machine identity in Azure.</td>
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
<tr id="parameter-machine_name">
    <td><CopyableCode code="machine_name" /></td>
    <td><code>string</code></td>
    <td>The name of the hybrid machine. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the hybrid machine. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands referenced resources. Default value is None.</td>
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

Retrieves information about the model view or the instance view of a hybrid machine.

```sql
SELECT
id,
name,
adFqdn,
agentConfiguration,
agentUpgrade,
agentVersion,
clientPublicKey,
cloudMetadata,
detectedProperties,
displayName,
dnsFqdn,
domainName,
errorDetails,
extensions,
firmwareProfile,
hardwareProfile,
hardwareResourceId,
identity,
identityKeyStore,
kind,
lastStatusChange,
licenseProfile,
location,
locationData,
machineFqdn,
mssqlDiscovered,
networkProfile,
osEdition,
osName,
osProfile,
osSku,
osType,
osVersion,
parentClusterResourceId,
privateLinkScopeResourceId,
provisioningState,
resources,
serviceStatuses,
status,
storageProfile,
systemData,
tags,
tpmEkCertificate,
type,
vmId,
vmUuid
FROM azure.hybridcompute.machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND machine_name = '{{ machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines.

```sql
SELECT
id,
name,
adFqdn,
agentConfiguration,
agentUpgrade,
agentVersion,
clientPublicKey,
cloudMetadata,
detectedProperties,
displayName,
dnsFqdn,
domainName,
errorDetails,
extensions,
firmwareProfile,
hardwareProfile,
hardwareResourceId,
identity,
identityKeyStore,
kind,
lastStatusChange,
licenseProfile,
location,
locationData,
machineFqdn,
mssqlDiscovered,
networkProfile,
osEdition,
osName,
osProfile,
osSku,
osType,
osVersion,
parentClusterResourceId,
privateLinkScopeResourceId,
provisioningState,
resources,
serviceStatuses,
status,
storageProfile,
systemData,
tags,
tpmEkCertificate,
type,
vmId,
vmUuid
FROM azure.hybridcompute.machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines.

```sql
SELECT
id,
name,
adFqdn,
agentConfiguration,
agentUpgrade,
agentVersion,
clientPublicKey,
cloudMetadata,
detectedProperties,
displayName,
dnsFqdn,
domainName,
errorDetails,
extensions,
firmwareProfile,
hardwareProfile,
hardwareResourceId,
identity,
identityKeyStore,
kind,
lastStatusChange,
licenseProfile,
location,
locationData,
machineFqdn,
mssqlDiscovered,
networkProfile,
osEdition,
osName,
osProfile,
osSku,
osType,
osVersion,
parentClusterResourceId,
privateLinkScopeResourceId,
provisioningState,
resources,
serviceStatuses,
status,
storageProfile,
systemData,
tags,
tpmEkCertificate,
type,
vmId,
vmUuid
FROM azure.hybridcompute.machines
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

The operation to create or update a hybrid machine. Please note some properties can be set only during machine creation.

```sql
INSERT INTO azure.hybridcompute.machines (
tags,
location,
properties,
identity,
kind,
resource_group_name,
machine_name,
subscription_id,
$expand
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ machine_name }}',
'{{ subscription_id }}',
'{{ $expand }}'
RETURNING
id,
name,
identity,
kind,
location,
properties,
resources,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: machines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the machines resource.
    - name: machine_name
      value: "{{ machine_name }}"
      description: Required parameter for the machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the machines resource.
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
        Hybrid Compute Machine properties.
      value:
        locationData:
          name: "{{ name }}"
          city: "{{ city }}"
          district: "{{ district }}"
          countryOrRegion: "{{ countryOrRegion }}"
        agentConfiguration:
          proxyUrl: "{{ proxyUrl }}"
          incomingConnectionsPorts:
            - "{{ incomingConnectionsPorts }}"
          extensionsAllowList:
            - publisher: "{{ publisher }}"
              type: "{{ type }}"
          extensionsBlockList:
            - publisher: "{{ publisher }}"
              type: "{{ type }}"
          proxyBypass:
            - "{{ proxyBypass }}"
          extensionsEnabled: "{{ extensionsEnabled }}"
          guestConfigurationEnabled: "{{ guestConfigurationEnabled }}"
          configMode: "{{ configMode }}"
        serviceStatuses:
          extensionService:
            status: "{{ status }}"
            startupType: "{{ startupType }}"
          guestConfigurationService:
            status: "{{ status }}"
            startupType: "{{ startupType }}"
        hardwareProfile:
          totalPhysicalMemoryInBytes: {{ totalPhysicalMemoryInBytes }}
          numberOfCpuSockets: {{ numberOfCpuSockets }}
          processors:
            - name: "{{ name }}"
              numberOfCores: {{ numberOfCores }}
        storageProfile:
          disks:
            - path: "{{ path }}"
              diskType: "{{ diskType }}"
              generatedId: "{{ generatedId }}"
              id: "{{ id }}"
              name: "{{ name }}"
              maxSizeInBytes: {{ maxSizeInBytes }}
              usedSpaceInBytes: {{ usedSpaceInBytes }}
        firmwareProfile:
          serialNumber: "{{ serialNumber }}"
          type: "{{ type }}"
        cloudMetadata:
          provider: "{{ provider }}"
        agentUpgrade:
          desiredVersion: "{{ desiredVersion }}"
          correlationId: "{{ correlationId }}"
          enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
          lastAttemptDesiredVersion: "{{ lastAttemptDesiredVersion }}"
          lastAttemptTimestamp: "{{ lastAttemptTimestamp }}"
          lastAttemptStatus: "{{ lastAttemptStatus }}"
          lastAttemptMessage: "{{ lastAttemptMessage }}"
        osProfile:
          computerName: "{{ computerName }}"
          windowsConfiguration:
            patchSettings:
              assessmentMode: "{{ assessmentMode }}"
              patchMode: "{{ patchMode }}"
              enableHotpatching: {{ enableHotpatching }}
              status:
                hotpatchEnablementStatus: "{{ hotpatchEnablementStatus }}"
                error: "{{ error }}"
          linuxConfiguration:
            patchSettings:
              assessmentMode: "{{ assessmentMode }}"
              patchMode: "{{ patchMode }}"
              enableHotpatching: {{ enableHotpatching }}
              status:
                hotpatchEnablementStatus: "{{ hotpatchEnablementStatus }}"
                error: "{{ error }}"
        licenseProfile:
          licenseStatus: "{{ licenseStatus }}"
          licenseChannel: "{{ licenseChannel }}"
          softwareAssurance:
            softwareAssuranceCustomer: {{ softwareAssuranceCustomer }}
          esuProfile:
            assignedLicenseImmutableId: "{{ assignedLicenseImmutableId }}"
            esuKeys:
              - sku: "{{ sku }}"
                licenseStatus: {{ licenseStatus }}
            serverType: "{{ serverType }}"
            esuEligibility: "{{ esuEligibility }}"
            esuKeyState: "{{ esuKeyState }}"
            assignedLicense:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              systemData:
                createdBy: "{{ createdBy }}"
                createdByType: "{{ createdByType }}"
                createdAt: "{{ createdAt }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedByType: "{{ lastModifiedByType }}"
                lastModifiedAt: "{{ lastModifiedAt }}"
              tags: "{{ tags }}"
              location: "{{ location }}"
              properties:
                provisioningState: "{{ provisioningState }}"
                tenantId: "{{ tenantId }}"
                licenseType: "{{ licenseType }}"
                licenseDetails: "{{ licenseDetails }}"
            licenseAssignmentState: "{{ licenseAssignmentState }}"
          productProfile:
            subscriptionStatus: "{{ subscriptionStatus }}"
            productType: "{{ productType }}"
            enrollmentDate: "{{ enrollmentDate }}"
            billingStartDate: "{{ billingStartDate }}"
            disenrollmentDate: "{{ disenrollmentDate }}"
            billingEndDate: "{{ billingEndDate }}"
            error:
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
            productFeatures:
              - name: "{{ name }}"
                subscriptionStatus: "{{ subscriptionStatus }}"
                enrollmentDate: "{{ enrollmentDate }}"
                billingStartDate: "{{ billingStartDate }}"
                disenrollmentDate: "{{ disenrollmentDate }}"
                billingEndDate: "{{ billingEndDate }}"
                error:
                  code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
                  additionalInfo: "{{ additionalInfo }}"
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        lastStatusChange: "{{ lastStatusChange }}"
        errorDetails:
          - code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details: "{{ details }}"
            additionalInfo: "{{ additionalInfo }}"
        agentVersion: "{{ agentVersion }}"
        vmId: "{{ vmId }}"
        displayName: "{{ displayName }}"
        machineFqdn: "{{ machineFqdn }}"
        clientPublicKey: "{{ clientPublicKey }}"
        identityKeyStore: "{{ identityKeyStore }}"
        tpmEkCertificate: "{{ tpmEkCertificate }}"
        osName: "{{ osName }}"
        osVersion: "{{ osVersion }}"
        osType: "{{ osType }}"
        vmUuid: "{{ vmUuid }}"
        extensions:
          - name: "{{ name }}"
            type: "{{ type }}"
            typeHandlerVersion: "{{ typeHandlerVersion }}"
            status:
              code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        osSku: "{{ osSku }}"
        osEdition: "{{ osEdition }}"
        domainName: "{{ domainName }}"
        adFqdn: "{{ adFqdn }}"
        dnsFqdn: "{{ dnsFqdn }}"
        privateLinkScopeResourceId: "{{ privateLinkScopeResourceId }}"
        parentClusterResourceId: "{{ parentClusterResourceId }}"
        hardwareResourceId: "{{ hardwareResourceId }}"
        mssqlDiscovered: "{{ mssqlDiscovered }}"
        detectedProperties: "{{ detectedProperties }}"
        networkProfile:
          networkInterfaces:
            - macAddress: "{{ macAddress }}"
              id: "{{ id }}"
              name: "{{ name }}"
              ipAddresses: "{{ ipAddresses }}"
    - name: identity
      description: |
        Identity for the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Indicates which kind of Arc machine placement on-premises, such as HCI, SCVMM or VMware etc. Known values are: "AVS", "HCI", "SCVMM", "VMware", "EPS", "GCP", and "AWS".
      valid_values: ['AVS', 'HCI', 'SCVMM', 'VMware', 'EPS', 'GCP', 'AWS']
    - name: $expand
      value: "{{ $expand }}"
      description: Expands referenced resources. Default value is None.
      description: Expands referenced resources. Default value is None.
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

The operation to update a hybrid machine.

```sql
UPDATE azure.hybridcompute.machines
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
kind,
location,
properties,
resources,
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

The operation to create or update a hybrid machine. Please note some properties can be set only during machine creation.

```sql
REPLACE azure.hybridcompute.machines
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND $expand = '{{ $expand}}'
RETURNING
id,
name,
identity,
kind,
location,
properties,
resources,
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

The operation to delete a hybrid machine.

```sql
DELETE FROM azure.hybridcompute.machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="assess_patches"
    values={[
        { label: 'assess_patches', value: 'assess_patches' },
        { label: 'install_patches', value: 'install_patches' }
    ]}
>
<TabItem value="assess_patches">

The operation to assess patches on a hybrid machine identity in Azure.

```sql
EXEC azure.hybridcompute.machines.assess_patches 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="install_patches">

The operation to install patches on a hybrid machine identity in Azure.

```sql
EXEC azure.hybridcompute.machines.install_patches 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"maximumDuration": "{{ maximumDuration }}", 
"rebootSetting": "{{ rebootSetting }}", 
"windowsParameters": "{{ windowsParameters }}", 
"linuxParameters": "{{ linuxParameters }}"
}'
;
```
</TabItem>
</Tabs>
