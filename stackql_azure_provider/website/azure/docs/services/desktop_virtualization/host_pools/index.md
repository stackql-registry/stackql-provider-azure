--- 
title: host_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - host_pools
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>host_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="host_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.host_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="agentUpdate" /></td>
    <td><code>object</code></td>
    <td>The session host configuration for updating agent, monitoring agent, and stack component.</td>
</tr>
<tr>
    <td><CopyableCode code="appAttachPackageReferences" /></td>
    <td><code>array</code></td>
    <td>List of App Attach Package links.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGroupReferences" /></td>
    <td><code>array</code></td>
    <td>List of applicationGroup links.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudPcResource" /></td>
    <td><code>boolean</code></td>
    <td>Is cloud pc resource.</td>
</tr>
<tr>
    <td><CopyableCode code="customRdpProperty" /></td>
    <td><code>string</code></td>
    <td>Custom rdp property of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPoolType" /></td>
    <td><code>string</code></td>
    <td>HostPool type for desktop. Required. Known values are: "Personal", "Pooled", and "BYODesktop".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerType" /></td>
    <td><code>string</code></td>
    <td>The type of the load balancer. Required. Known values are: "BreadthFirst", "DepthFirst", and "Persistent".</td>
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
    <td><CopyableCode code="maxSessionLimit" /></td>
    <td><code>integer</code></td>
    <td>The max session limit of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of HostPool. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="personalDesktopAssignmentType" /></td>
    <td><code>string</code></td>
    <td>PersonalDesktopAssignment type for HostPool. Known values are: "Automatic" and "Direct".</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>:vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan</td>
</tr>
<tr>
    <td><CopyableCode code="preferredAppGroupType" /></td>
    <td><code>string</code></td>
    <td>The type of preferred application group type, default to Desktop Application Group. Required. Known values are: "None", "Desktop", and "RailApplications".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enabled allows this resource to be accessed from both public and private networks, Disabled allows this resource to only be accessed via private endpoints. Known values are: "Enabled", "Disabled", "EnabledForSessionHostsOnly", and "EnabledForClientsOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="registrationInfo" /></td>
    <td><code>object</code></td>
    <td>The registration info of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="ring" /></td>
    <td><code>integer</code></td>
    <td>The ring number of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku</td>
</tr>
<tr>
    <td><CopyableCode code="ssoClientId" /></td>
    <td><code>string</code></td>
    <td>ClientId for the registered Relying Party used to issue WVD SSO certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoClientSecretKeyVaultPath" /></td>
    <td><code>string</code></td>
    <td>Path to Azure KeyVault storing the secret used for communication to ADFS.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoSecretType" /></td>
    <td><code>string</code></td>
    <td>The type of single sign on Secret Type. Known values are: "SharedKey", "Certificate", "SharedKeyInKeyVault", and "CertificateInKeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="ssoadfsAuthority" /></td>
    <td><code>string</code></td>
    <td>URL to customer ADFS server for signing WVD SSO certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="startVMOnConnect" /></td>
    <td><code>boolean</code></td>
    <td>The flag to turn on/off StartVMOnConnect feature.</td>
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
    <td><CopyableCode code="validationEnvironment" /></td>
    <td><code>boolean</code></td>
    <td>Is validation environment.</td>
</tr>
<tr>
    <td><CopyableCode code="vmTemplate" /></td>
    <td><code>string</code></td>
    <td>VM template for sessionhosts configuration within hostpool.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="agentUpdate" /></td>
    <td><code>object</code></td>
    <td>The session host configuration for updating agent, monitoring agent, and stack component.</td>
</tr>
<tr>
    <td><CopyableCode code="appAttachPackageReferences" /></td>
    <td><code>array</code></td>
    <td>List of App Attach Package links.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGroupReferences" /></td>
    <td><code>array</code></td>
    <td>List of applicationGroup links.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudPcResource" /></td>
    <td><code>boolean</code></td>
    <td>Is cloud pc resource.</td>
</tr>
<tr>
    <td><CopyableCode code="customRdpProperty" /></td>
    <td><code>string</code></td>
    <td>Custom rdp property of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPoolType" /></td>
    <td><code>string</code></td>
    <td>HostPool type for desktop. Required. Known values are: "Personal", "Pooled", and "BYODesktop".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerType" /></td>
    <td><code>string</code></td>
    <td>The type of the load balancer. Required. Known values are: "BreadthFirst", "DepthFirst", and "Persistent".</td>
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
    <td><CopyableCode code="maxSessionLimit" /></td>
    <td><code>integer</code></td>
    <td>The max session limit of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of HostPool. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="personalDesktopAssignmentType" /></td>
    <td><code>string</code></td>
    <td>PersonalDesktopAssignment type for HostPool. Known values are: "Automatic" and "Direct".</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>:vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan</td>
</tr>
<tr>
    <td><CopyableCode code="preferredAppGroupType" /></td>
    <td><code>string</code></td>
    <td>The type of preferred application group type, default to Desktop Application Group. Required. Known values are: "None", "Desktop", and "RailApplications".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enabled allows this resource to be accessed from both public and private networks, Disabled allows this resource to only be accessed via private endpoints. Known values are: "Enabled", "Disabled", "EnabledForSessionHostsOnly", and "EnabledForClientsOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="registrationInfo" /></td>
    <td><code>object</code></td>
    <td>The registration info of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="ring" /></td>
    <td><code>integer</code></td>
    <td>The ring number of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku</td>
</tr>
<tr>
    <td><CopyableCode code="ssoClientId" /></td>
    <td><code>string</code></td>
    <td>ClientId for the registered Relying Party used to issue WVD SSO certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoClientSecretKeyVaultPath" /></td>
    <td><code>string</code></td>
    <td>Path to Azure KeyVault storing the secret used for communication to ADFS.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoSecretType" /></td>
    <td><code>string</code></td>
    <td>The type of single sign on Secret Type. Known values are: "SharedKey", "Certificate", "SharedKeyInKeyVault", and "CertificateInKeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="ssoadfsAuthority" /></td>
    <td><code>string</code></td>
    <td>URL to customer ADFS server for signing WVD SSO certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="startVMOnConnect" /></td>
    <td><code>boolean</code></td>
    <td>The flag to turn on/off StartVMOnConnect feature.</td>
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
    <td><CopyableCode code="validationEnvironment" /></td>
    <td><code>boolean</code></td>
    <td>Is validation environment.</td>
</tr>
<tr>
    <td><CopyableCode code="vmTemplate" /></td>
    <td><code>string</code></td>
    <td>VM template for sessionhosts configuration within hostpool.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="agentUpdate" /></td>
    <td><code>object</code></td>
    <td>The session host configuration for updating agent, monitoring agent, and stack component.</td>
</tr>
<tr>
    <td><CopyableCode code="appAttachPackageReferences" /></td>
    <td><code>array</code></td>
    <td>List of App Attach Package links.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGroupReferences" /></td>
    <td><code>array</code></td>
    <td>List of applicationGroup links.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudPcResource" /></td>
    <td><code>boolean</code></td>
    <td>Is cloud pc resource.</td>
</tr>
<tr>
    <td><CopyableCode code="customRdpProperty" /></td>
    <td><code>string</code></td>
    <td>Custom rdp property of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPoolType" /></td>
    <td><code>string</code></td>
    <td>HostPool type for desktop. Required. Known values are: "Personal", "Pooled", and "BYODesktop".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerType" /></td>
    <td><code>string</code></td>
    <td>The type of the load balancer. Required. Known values are: "BreadthFirst", "DepthFirst", and "Persistent".</td>
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
    <td><CopyableCode code="maxSessionLimit" /></td>
    <td><code>integer</code></td>
    <td>The max session limit of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of HostPool. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="personalDesktopAssignmentType" /></td>
    <td><code>string</code></td>
    <td>PersonalDesktopAssignment type for HostPool. Known values are: "Automatic" and "Direct".</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>:vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan</td>
</tr>
<tr>
    <td><CopyableCode code="preferredAppGroupType" /></td>
    <td><code>string</code></td>
    <td>The type of preferred application group type, default to Desktop Application Group. Required. Known values are: "None", "Desktop", and "RailApplications".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enabled allows this resource to be accessed from both public and private networks, Disabled allows this resource to only be accessed via private endpoints. Known values are: "Enabled", "Disabled", "EnabledForSessionHostsOnly", and "EnabledForClientsOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="registrationInfo" /></td>
    <td><code>object</code></td>
    <td>The registration info of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="ring" /></td>
    <td><code>integer</code></td>
    <td>The ring number of HostPool.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku</td>
</tr>
<tr>
    <td><CopyableCode code="ssoClientId" /></td>
    <td><code>string</code></td>
    <td>ClientId for the registered Relying Party used to issue WVD SSO certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoClientSecretKeyVaultPath" /></td>
    <td><code>string</code></td>
    <td>Path to Azure KeyVault storing the secret used for communication to ADFS.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoSecretType" /></td>
    <td><code>string</code></td>
    <td>The type of single sign on Secret Type. Known values are: "SharedKey", "Certificate", "SharedKeyInKeyVault", and "CertificateInKeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="ssoadfsAuthority" /></td>
    <td><code>string</code></td>
    <td>URL to customer ADFS server for signing WVD SSO certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="startVMOnConnect" /></td>
    <td><code>boolean</code></td>
    <td>The flag to turn on/off StartVMOnConnect feature.</td>
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
    <td><CopyableCode code="validationEnvironment" /></td>
    <td><code>boolean</code></td>
    <td>Is validation environment.</td>
</tr>
<tr>
    <td><CopyableCode code="vmTemplate" /></td>
    <td><code>string</code></td>
    <td>VM template for sessionhosts configuration within hostpool.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a host pool.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List hostPools.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List hostPools in subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a host pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a host pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a host pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Remove a host pool.</td>
</tr>
<tr>
    <td><a href="#list_registration_tokens"><CopyableCode code="list_registration_tokens" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to list the RegistrationTokens associated with the HostPool.</td>
</tr>
<tr>
    <td><a href="#retrieve_registration_token"><CopyableCode code="retrieve_registration_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Registration token of the host pool.</td>
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
<tr id="parameter-host_pool_name">
    <td><CopyableCode code="host_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the host pool within the specified resource group. Required.</td>
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
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Force flag to delete sessionHost. Default value is None.</td>
</tr>
<tr id="parameter-initialSkip">
    <td><CopyableCode code="initialSkip" /></td>
    <td><code>integer</code></td>
    <td>Initial number of items to skip. Default value is None.</td>
</tr>
<tr id="parameter-isDescending">
    <td><CopyableCode code="isDescending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the collection is descending. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Number of items per page. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a host pool.

```sql
SELECT
id,
name,
agentUpdate,
appAttachPackageReferences,
applicationGroupReferences,
cloudPcResource,
customRdpProperty,
description,
etag,
friendlyName,
hostPoolType,
identity,
kind,
loadBalancerType,
location,
managedBy,
maxSessionLimit,
objectId,
personalDesktopAssignmentType,
plan,
preferredAppGroupType,
privateEndpointConnections,
publicNetworkAccess,
registrationInfo,
ring,
sku,
ssoClientId,
ssoClientSecretKeyVaultPath,
ssoSecretType,
ssoadfsAuthority,
startVMOnConnect,
systemData,
tags,
type,
validationEnvironment,
vmTemplate
FROM azure.desktop_virtualization.host_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List hostPools.

```sql
SELECT
id,
name,
agentUpdate,
appAttachPackageReferences,
applicationGroupReferences,
cloudPcResource,
customRdpProperty,
description,
etag,
friendlyName,
hostPoolType,
identity,
kind,
loadBalancerType,
location,
managedBy,
maxSessionLimit,
objectId,
personalDesktopAssignmentType,
plan,
preferredAppGroupType,
privateEndpointConnections,
publicNetworkAccess,
registrationInfo,
ring,
sku,
ssoClientId,
ssoClientSecretKeyVaultPath,
ssoSecretType,
ssoadfsAuthority,
startVMOnConnect,
systemData,
tags,
type,
validationEnvironment,
vmTemplate
FROM azure.desktop_virtualization.host_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
;
```
</TabItem>
<TabItem value="list">

List hostPools in subscription.

```sql
SELECT
id,
name,
agentUpdate,
appAttachPackageReferences,
applicationGroupReferences,
cloudPcResource,
customRdpProperty,
description,
etag,
friendlyName,
hostPoolType,
identity,
kind,
loadBalancerType,
location,
managedBy,
maxSessionLimit,
objectId,
personalDesktopAssignmentType,
plan,
preferredAppGroupType,
privateEndpointConnections,
publicNetworkAccess,
registrationInfo,
ring,
sku,
ssoClientId,
ssoClientSecretKeyVaultPath,
ssoSecretType,
ssoadfsAuthority,
startVMOnConnect,
systemData,
tags,
type,
validationEnvironment,
vmTemplate
FROM azure.desktop_virtualization.host_pools
WHERE subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
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

Create or update a host pool.

```sql
INSERT INTO azure.desktop_virtualization.host_pools (
tags,
location,
managedBy,
kind,
identity,
sku,
plan,
properties,
resource_group_name,
host_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ managedBy }}',
'{{ kind }}',
'{{ identity }}',
'{{ sku }}',
'{{ plan }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ host_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: host_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the host_pools resource.
    - name: host_pool_name
      value: "{{ host_pool_name }}"
      description: Required parameter for the host_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the host_pools resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
    - name: identity
      description: |
        :vartype identity: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetIdentity
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: sku
      description: |
        :vartype sku: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetSku
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: plan
      description: |
        :vartype plan: ~azure.mgmt.desktopvirtualization.models.ResourceModelWithAllowedPropertySetPlan
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
    - name: properties
      value:
        friendlyName: "{{ friendlyName }}"
        description: "{{ description }}"
        hostPoolType: "{{ hostPoolType }}"
        personalDesktopAssignmentType: "{{ personalDesktopAssignmentType }}"
        customRdpProperty: "{{ customRdpProperty }}"
        maxSessionLimit: {{ maxSessionLimit }}
        loadBalancerType: "{{ loadBalancerType }}"
        ring: {{ ring }}
        validationEnvironment: {{ validationEnvironment }}
        registrationInfo:
          expirationTime: "{{ expirationTime }}"
          token: "{{ token }}"
          registrationTokenOperation: "{{ registrationTokenOperation }}"
        vmTemplate: "{{ vmTemplate }}"
        ssoadfsAuthority: "{{ ssoadfsAuthority }}"
        ssoClientId: "{{ ssoClientId }}"
        ssoClientSecretKeyVaultPath: "{{ ssoClientSecretKeyVaultPath }}"
        ssoSecretType: "{{ ssoSecretType }}"
        preferredAppGroupType: "{{ preferredAppGroupType }}"
        startVMOnConnect: {{ startVMOnConnect }}
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        agentUpdate:
          type: "{{ type }}"
          useSessionHostLocalTime: {{ useSessionHostLocalTime }}
          maintenanceWindowTimeZone: "{{ maintenanceWindowTimeZone }}"
          maintenanceWindows:
            - hour: {{ hour }}
              dayOfWeek: "{{ dayOfWeek }}"
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

Update a host pool.

```sql
UPDATE azure.desktop_virtualization.host_pools
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
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

Create or update a host pool.

```sql
REPLACE azure.desktop_virtualization.host_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
managedBy = '{{ managedBy }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
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

Remove a host pool.

```sql
DELETE FROM azure.desktop_virtualization.host_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_registration_tokens"
    values={[
        { label: 'list_registration_tokens', value: 'list_registration_tokens' },
        { label: 'retrieve_registration_token', value: 'retrieve_registration_token' }
    ]}
>
<TabItem value="list_registration_tokens">

Operation to list the RegistrationTokens associated with the HostPool.

```sql
EXEC azure.desktop_virtualization.host_pools.list_registration_tokens 
@resource_group_name='{{ resource_group_name }}' --required, 
@host_pool_name='{{ host_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="retrieve_registration_token">

Registration token of the host pool.

```sql
EXEC azure.desktop_virtualization.host_pools.retrieve_registration_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@host_pool_name='{{ host_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
