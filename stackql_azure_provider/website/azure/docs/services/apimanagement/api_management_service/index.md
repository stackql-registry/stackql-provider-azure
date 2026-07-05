--- 
title: api_management_service
hide_title: false
hide_table_of_contents: false
keywords:
  - api_management_service
  - apimanagement
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

Creates, updates, deletes, gets or lists an <code>api_management_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="api_management_service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.apimanagement.api_management_service" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalLocations" /></td>
    <td><code>array</code></td>
    <td>Additional datacenter locations of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionConstraint" /></td>
    <td><code>object</code></td>
    <td>Control Plane Apis version constraint for the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationApi" /></td>
    <td><code>object</code></td>
    <td>Configuration API configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAtUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation UTC date of the API Management service.The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties of the API Management service.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1, 2018 and `False` otherwise. Http2 setting's default value is `False`.You can disable any of the following ciphers by using settings `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]`: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA. For example, `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256`:`false`. The default value is `true` for them. Note: The following ciphers can't be disabled since they are required by internal platform components: TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256.</td>
</tr>
<tr>
    <td><CopyableCode code="developerPortalStatus" /></td>
    <td><code>string</code></td>
    <td>Status of developer portal in this API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="developerPortalUrl" /></td>
    <td><code>string</code></td>
    <td>DEveloper Portal endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="disableGateway" /></td>
    <td><code>boolean</code></td>
    <td>Property only valid for an Api Management service deployed in multiple locations. This can be used to disable the gateway in master region.</td>
</tr>
<tr>
    <td><CopyableCode code="enableClientCertificate" /></td>
    <td><code>boolean</code></td>
    <td>Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>ETag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayRegionalUrl" /></td>
    <td><code>string</code></td>
    <td>Gateway URL of the API Management service in the Default Region.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayUrl" /></td>
    <td><code>string</code></td>
    <td>Gateway URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnameConfigurations" /></td>
    <td><code>array</code></td>
    <td>Custom hostname configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the Api Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="legacyPortalStatus" /></td>
    <td><code>string</code></td>
    <td>Status of legacy portal in the API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementApiUrl" /></td>
    <td><code>string</code></td>
    <td>Management API endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="natGatewayState" /></td>
    <td><code>string</code></td>
    <td>Property can be used to enable NAT Gateway for this API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSenderEmail" /></td>
    <td><code>string</code></td>
    <td>Email address from which the notification will be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundPublicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound public IPV4 address prefixes associated with NAT Gateway deployed service. Available only for Premium SKU on stv2 platform.</td>
</tr>
<tr>
    <td><CopyableCode code="platformVersion" /></td>
    <td><code>string</code></td>
    <td>Compute Platform Version running the service in this location. Known values are: "undetermined", "stv1", "stv2", "mtv1", and "stv2.1". (undetermined, stv1, stv2, mtv1, stv2.1)</td>
</tr>
<tr>
    <td><CopyableCode code="portalUrl" /></td>
    <td><code>string</code></td>
    <td>Publisher portal endpoint Url of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections of this service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Private Static Load Balanced IP addresses of the API Management service in Primary region which is deployed in an Internal Virtual Network. Available only for Basic, Standard, Premium and Isolated SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Public Static Load Balanced IP addresses of the API Management service in Primary region. Available only for Basic, Standard, Premium and Isolated SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddressId" /></td>
    <td><code>string</code></td>
    <td>Public Standard SKU IP V4 based IP address to be associated with Virtual Network deployed service in the region. Supported only for Developer and Premium SKU being deployed in Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this API Management service. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints are the exclusive access method. Default value is 'Enabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="publisherEmail" /></td>
    <td><code>string</code></td>
    <td>Publisher email. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherName" /></td>
    <td><code>string</code></td>
    <td>Publisher name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseChannel" /></td>
    <td><code>string</code></td>
    <td>Release Channel of this API Management service. Known values are: "Preview", "Default", and "Stable". (Preview, Default, Stable)</td>
</tr>
<tr>
    <td><CopyableCode code="restore" /></td>
    <td><code>boolean</code></td>
    <td>Undelete Api Management Service if it was previously soft-deleted. If this flag is specified and set to True all other properties will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="scmUrl" /></td>
    <td><code>string</code></td>
    <td>SCM endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU properties of the API Management service. Required.</td>
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
    <td><CopyableCode code="targetProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the API Management service, which is targeted by the long running operation started on the service.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Virtual network configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkType" /></td>
    <td><code>string</code></td>
    <td>The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only. Known values are: "None", "External", and "Internal". (None, External, Internal)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Zone Redundant Requirement when creating StandardV2 and PremiumV2. If this flag is set to True, will return a APIM service with Zone redundant or fail the request if any underneath component cannot be zone redundant.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="additionalLocations" /></td>
    <td><code>array</code></td>
    <td>Additional datacenter locations of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionConstraint" /></td>
    <td><code>object</code></td>
    <td>Control Plane Apis version constraint for the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationApi" /></td>
    <td><code>object</code></td>
    <td>Configuration API configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAtUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation UTC date of the API Management service.The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties of the API Management service.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1, 2018 and `False` otherwise. Http2 setting's default value is `False`.You can disable any of the following ciphers by using settings `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]`: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA. For example, `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256`:`false`. The default value is `true` for them. Note: The following ciphers can't be disabled since they are required by internal platform components: TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256.</td>
</tr>
<tr>
    <td><CopyableCode code="developerPortalStatus" /></td>
    <td><code>string</code></td>
    <td>Status of developer portal in this API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="developerPortalUrl" /></td>
    <td><code>string</code></td>
    <td>DEveloper Portal endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="disableGateway" /></td>
    <td><code>boolean</code></td>
    <td>Property only valid for an Api Management service deployed in multiple locations. This can be used to disable the gateway in master region.</td>
</tr>
<tr>
    <td><CopyableCode code="enableClientCertificate" /></td>
    <td><code>boolean</code></td>
    <td>Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>ETag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayRegionalUrl" /></td>
    <td><code>string</code></td>
    <td>Gateway URL of the API Management service in the Default Region.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayUrl" /></td>
    <td><code>string</code></td>
    <td>Gateway URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnameConfigurations" /></td>
    <td><code>array</code></td>
    <td>Custom hostname configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the Api Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="legacyPortalStatus" /></td>
    <td><code>string</code></td>
    <td>Status of legacy portal in the API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementApiUrl" /></td>
    <td><code>string</code></td>
    <td>Management API endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="natGatewayState" /></td>
    <td><code>string</code></td>
    <td>Property can be used to enable NAT Gateway for this API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSenderEmail" /></td>
    <td><code>string</code></td>
    <td>Email address from which the notification will be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundPublicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound public IPV4 address prefixes associated with NAT Gateway deployed service. Available only for Premium SKU on stv2 platform.</td>
</tr>
<tr>
    <td><CopyableCode code="platformVersion" /></td>
    <td><code>string</code></td>
    <td>Compute Platform Version running the service in this location. Known values are: "undetermined", "stv1", "stv2", "mtv1", and "stv2.1". (undetermined, stv1, stv2, mtv1, stv2.1)</td>
</tr>
<tr>
    <td><CopyableCode code="portalUrl" /></td>
    <td><code>string</code></td>
    <td>Publisher portal endpoint Url of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections of this service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Private Static Load Balanced IP addresses of the API Management service in Primary region which is deployed in an Internal Virtual Network. Available only for Basic, Standard, Premium and Isolated SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Public Static Load Balanced IP addresses of the API Management service in Primary region. Available only for Basic, Standard, Premium and Isolated SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddressId" /></td>
    <td><code>string</code></td>
    <td>Public Standard SKU IP V4 based IP address to be associated with Virtual Network deployed service in the region. Supported only for Developer and Premium SKU being deployed in Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this API Management service. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints are the exclusive access method. Default value is 'Enabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="publisherEmail" /></td>
    <td><code>string</code></td>
    <td>Publisher email. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherName" /></td>
    <td><code>string</code></td>
    <td>Publisher name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseChannel" /></td>
    <td><code>string</code></td>
    <td>Release Channel of this API Management service. Known values are: "Preview", "Default", and "Stable". (Preview, Default, Stable)</td>
</tr>
<tr>
    <td><CopyableCode code="restore" /></td>
    <td><code>boolean</code></td>
    <td>Undelete Api Management Service if it was previously soft-deleted. If this flag is specified and set to True all other properties will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="scmUrl" /></td>
    <td><code>string</code></td>
    <td>SCM endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU properties of the API Management service. Required.</td>
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
    <td><CopyableCode code="targetProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the API Management service, which is targeted by the long running operation started on the service.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Virtual network configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkType" /></td>
    <td><code>string</code></td>
    <td>The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only. Known values are: "None", "External", and "Internal". (None, External, Internal)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Zone Redundant Requirement when creating StandardV2 and PremiumV2. If this flag is set to True, will return a APIM service with Zone redundant or fail the request if any underneath component cannot be zone redundant.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="additionalLocations" /></td>
    <td><code>array</code></td>
    <td>Additional datacenter locations of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionConstraint" /></td>
    <td><code>object</code></td>
    <td>Control Plane Apis version constraint for the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationApi" /></td>
    <td><code>object</code></td>
    <td>Configuration API configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAtUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation UTC date of the API Management service.The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties of the API Management service.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1, 2018 and `False` otherwise. Http2 setting's default value is `False`.You can disable any of the following ciphers by using settings `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]`: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA. For example, `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256`:`false`. The default value is `true` for them. Note: The following ciphers can't be disabled since they are required by internal platform components: TLS_AES_256_GCM_SHA384,TLS_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256.</td>
</tr>
<tr>
    <td><CopyableCode code="developerPortalStatus" /></td>
    <td><code>string</code></td>
    <td>Status of developer portal in this API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="developerPortalUrl" /></td>
    <td><code>string</code></td>
    <td>DEveloper Portal endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="disableGateway" /></td>
    <td><code>boolean</code></td>
    <td>Property only valid for an Api Management service deployed in multiple locations. This can be used to disable the gateway in master region.</td>
</tr>
<tr>
    <td><CopyableCode code="enableClientCertificate" /></td>
    <td><code>boolean</code></td>
    <td>Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>ETag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayRegionalUrl" /></td>
    <td><code>string</code></td>
    <td>Gateway URL of the API Management service in the Default Region.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayUrl" /></td>
    <td><code>string</code></td>
    <td>Gateway URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnameConfigurations" /></td>
    <td><code>array</code></td>
    <td>Custom hostname configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the Api Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="legacyPortalStatus" /></td>
    <td><code>string</code></td>
    <td>Status of legacy portal in the API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementApiUrl" /></td>
    <td><code>string</code></td>
    <td>Management API endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="natGatewayState" /></td>
    <td><code>string</code></td>
    <td>Property can be used to enable NAT Gateway for this API Management service. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSenderEmail" /></td>
    <td><code>string</code></td>
    <td>Email address from which the notification will be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundPublicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound public IPV4 address prefixes associated with NAT Gateway deployed service. Available only for Premium SKU on stv2 platform.</td>
</tr>
<tr>
    <td><CopyableCode code="platformVersion" /></td>
    <td><code>string</code></td>
    <td>Compute Platform Version running the service in this location. Known values are: "undetermined", "stv1", "stv2", "mtv1", and "stv2.1". (undetermined, stv1, stv2, mtv1, stv2.1)</td>
</tr>
<tr>
    <td><CopyableCode code="portalUrl" /></td>
    <td><code>string</code></td>
    <td>Publisher portal endpoint Url of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections of this service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Private Static Load Balanced IP addresses of the API Management service in Primary region which is deployed in an Internal Virtual Network. Available only for Basic, Standard, Premium and Isolated SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>Public Static Load Balanced IP addresses of the API Management service in Primary region. Available only for Basic, Standard, Premium and Isolated SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddressId" /></td>
    <td><code>string</code></td>
    <td>Public Standard SKU IP V4 based IP address to be associated with Virtual Network deployed service in the region. Supported only for Developer and Premium SKU being deployed in Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this API Management service. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints are the exclusive access method. Default value is 'Enabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="publisherEmail" /></td>
    <td><code>string</code></td>
    <td>Publisher email. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherName" /></td>
    <td><code>string</code></td>
    <td>Publisher name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseChannel" /></td>
    <td><code>string</code></td>
    <td>Release Channel of this API Management service. Known values are: "Preview", "Default", and "Stable". (Preview, Default, Stable)</td>
</tr>
<tr>
    <td><CopyableCode code="restore" /></td>
    <td><code>boolean</code></td>
    <td>Undelete Api Management Service if it was previously soft-deleted. If this flag is specified and set to True all other properties will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="scmUrl" /></td>
    <td><code>string</code></td>
    <td>SCM endpoint URL of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU properties of the API Management service. Required.</td>
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
    <td><CopyableCode code="targetProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the API Management service, which is targeted by the long running operation started on the service.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Virtual network configuration of the API Management service.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkType" /></td>
    <td><code>string</code></td>
    <td>The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only. Known values are: "None", "External", and "Internal". (None, External, Internal)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Zone Redundant Requirement when creating StandardV2 and PremiumV2. If this flag is set to True, will return a APIM service with Zone redundant or fail the request if any underneath component cannot be zone redundant.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an API Management service resource description.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all API Management services within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all API Management services within an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates or updates an API Management service. This is long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing API Management service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates or updates an API Management service. This is long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing API Management service.</td>
</tr>
<tr>
    <td><a href="#get_sso_token"><CopyableCode code="get_sso_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Single-Sign-On token for the API Management Service which is valid for 5 Minutes.</td>
</tr>
<tr>
    <td><a href="#get_domain_ownership_identifier"><CopyableCode code="get_domain_ownership_identifier" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the custom domain ownership identifier for an API Management service.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-storageAccount"><code>storageAccount</code></a>, <a href="#parameter-containerName"><code>containerName</code></a>, <a href="#parameter-backupName"><code>backupName</code></a></td>
    <td></td>
    <td>Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#backup"><CopyableCode code="backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-storageAccount"><code>storageAccount</code></a>, <a href="#parameter-containerName"><code>containerName</code></a>, <a href="#parameter-backupName"><code>backupName</code></a></td>
    <td></td>
    <td>Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#migrate_to_stv2"><CopyableCode code="migrate_to_stv2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrades an API Management service to the Stv2 platform. For details refer to `https://aka.ms/apim-migrate-stv2 `_. This change is not reversible. This is long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#apply_network_configuration_updates"><CopyableCode code="apply_network_configuration_updates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated DNS changes.</td>
</tr>
<tr>
    <td><a href="#refresh_hostnames"><CopyableCode code="refresh_hostnames" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Force Refresh the SSL certificate attached to the Custom Hostnames configured using secret from KeyVault on the Api Management service.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Checks availability and correctness of a name for an API Management service.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets an API Management service resource description.

```sql
SELECT
id,
name,
additionalLocations,
apiVersionConstraint,
certificates,
configurationApi,
createdAtUtc,
customProperties,
developerPortalStatus,
developerPortalUrl,
disableGateway,
enableClientCertificate,
etag,
gatewayRegionalUrl,
gatewayUrl,
hostnameConfigurations,
identity,
legacyPortalStatus,
location,
managementApiUrl,
natGatewayState,
notificationSenderEmail,
outboundPublicIPAddresses,
platformVersion,
portalUrl,
privateEndpointConnections,
privateIPAddresses,
provisioningState,
publicIPAddresses,
publicIpAddressId,
publicNetworkAccess,
publisherEmail,
publisherName,
releaseChannel,
restore,
scmUrl,
sku,
systemData,
tags,
targetProvisioningState,
type,
virtualNetworkConfiguration,
virtualNetworkType,
zoneRedundant,
zones
FROM azure.apimanagement.api_management_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all API Management services within a resource group.

```sql
SELECT
id,
name,
additionalLocations,
apiVersionConstraint,
certificates,
configurationApi,
createdAtUtc,
customProperties,
developerPortalStatus,
developerPortalUrl,
disableGateway,
enableClientCertificate,
etag,
gatewayRegionalUrl,
gatewayUrl,
hostnameConfigurations,
identity,
legacyPortalStatus,
location,
managementApiUrl,
natGatewayState,
notificationSenderEmail,
outboundPublicIPAddresses,
platformVersion,
portalUrl,
privateEndpointConnections,
privateIPAddresses,
provisioningState,
publicIPAddresses,
publicIpAddressId,
publicNetworkAccess,
publisherEmail,
publisherName,
releaseChannel,
restore,
scmUrl,
sku,
systemData,
tags,
targetProvisioningState,
type,
virtualNetworkConfiguration,
virtualNetworkType,
zoneRedundant,
zones
FROM azure.apimanagement.api_management_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all API Management services within an Azure subscription.

```sql
SELECT
id,
name,
additionalLocations,
apiVersionConstraint,
certificates,
configurationApi,
createdAtUtc,
customProperties,
developerPortalStatus,
developerPortalUrl,
disableGateway,
enableClientCertificate,
etag,
gatewayRegionalUrl,
gatewayUrl,
hostnameConfigurations,
identity,
legacyPortalStatus,
location,
managementApiUrl,
natGatewayState,
notificationSenderEmail,
outboundPublicIPAddresses,
platformVersion,
portalUrl,
privateEndpointConnections,
privateIPAddresses,
provisioningState,
publicIPAddresses,
publicIpAddressId,
publicNetworkAccess,
publisherEmail,
publisherName,
releaseChannel,
restore,
scmUrl,
sku,
systemData,
tags,
targetProvisioningState,
type,
virtualNetworkConfiguration,
virtualNetworkType,
zoneRedundant,
zones
FROM azure.apimanagement.api_management_service
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

Creates or updates an API Management service. This is long running operation and could take several minutes to complete.

```sql
INSERT INTO azure.apimanagement.api_management_service (
tags,
location,
properties,
sku,
identity,
zones,
resource_group_name,
service_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ sku }}' /* required */,
'{{ identity }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
sku,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: api_management_service
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the api_management_service resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the api_management_service resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the api_management_service resource.
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
        Properties of the API Management service. Required.
      value:
        notificationSenderEmail: "{{ notificationSenderEmail }}"
        provisioningState: "{{ provisioningState }}"
        targetProvisioningState: "{{ targetProvisioningState }}"
        createdAtUtc: "{{ createdAtUtc }}"
        gatewayUrl: "{{ gatewayUrl }}"
        gatewayRegionalUrl: "{{ gatewayRegionalUrl }}"
        portalUrl: "{{ portalUrl }}"
        managementApiUrl: "{{ managementApiUrl }}"
        scmUrl: "{{ scmUrl }}"
        developerPortalUrl: "{{ developerPortalUrl }}"
        hostnameConfigurations:
          - type: "{{ type }}"
            hostName: "{{ hostName }}"
            keyVaultId: "{{ keyVaultId }}"
            identityClientId: "{{ identityClientId }}"
            encodedCertificate: "{{ encodedCertificate }}"
            certificatePassword: "{{ certificatePassword }}"
            defaultSslBinding: {{ defaultSslBinding }}
            negotiateClientCertificate: {{ negotiateClientCertificate }}
            certificate:
              expiry: "{{ expiry }}"
              thumbprint: "{{ thumbprint }}"
              subject: "{{ subject }}"
            certificateSource: "{{ certificateSource }}"
            certificateStatus: "{{ certificateStatus }}"
        publicIPAddresses:
          - "{{ publicIPAddresses }}"
        privateIPAddresses:
          - "{{ privateIPAddresses }}"
        publicIpAddressId: "{{ publicIpAddressId }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        configurationApi:
          legacyApi: "{{ legacyApi }}"
        virtualNetworkConfiguration:
          vnetid: "{{ vnetid }}"
          subnetname: "{{ subnetname }}"
          subnetResourceId: "{{ subnetResourceId }}"
        additionalLocations:
          - location: "{{ location }}"
            sku:
              name: "{{ name }}"
              capacity: {{ capacity }}
            zones: "{{ zones }}"
            publicIPAddresses: "{{ publicIPAddresses }}"
            privateIPAddresses: "{{ privateIPAddresses }}"
            publicIpAddressId: "{{ publicIpAddressId }}"
            virtualNetworkConfiguration:
              vnetid: "{{ vnetid }}"
              subnetname: "{{ subnetname }}"
              subnetResourceId: "{{ subnetResourceId }}"
            gatewayRegionalUrl: "{{ gatewayRegionalUrl }}"
            natGatewayState: "{{ natGatewayState }}"
            outboundPublicIPAddresses: "{{ outboundPublicIPAddresses }}"
            disableGateway: {{ disableGateway }}
            platformVersion: "{{ platformVersion }}"
        customProperties: "{{ customProperties }}"
        certificates:
          - encodedCertificate: "{{ encodedCertificate }}"
            certificatePassword: "{{ certificatePassword }}"
            storeName: "{{ storeName }}"
            certificate:
              expiry: "{{ expiry }}"
              thumbprint: "{{ thumbprint }}"
              subject: "{{ subject }}"
        enableClientCertificate: {{ enableClientCertificate }}
        natGatewayState: "{{ natGatewayState }}"
        outboundPublicIPAddresses:
          - "{{ outboundPublicIPAddresses }}"
        disableGateway: {{ disableGateway }}
        virtualNetworkType: "{{ virtualNetworkType }}"
        apiVersionConstraint:
          minApiVersion: "{{ minApiVersion }}"
        restore: {{ restore }}
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
              groupIds:
                - "{{ groupIds }}"
        platformVersion: "{{ platformVersion }}"
        legacyPortalStatus: "{{ legacyPortalStatus }}"
        developerPortalStatus: "{{ developerPortalStatus }}"
        releaseChannel: "{{ releaseChannel }}"
        zoneRedundant: {{ zoneRedundant }}
        publisherEmail: "{{ publisherEmail }}"
        publisherName: "{{ publisherName }}"
    - name: sku
      description: |
        SKU properties of the API Management service. Required.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Managed service identity of the Api Management service.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
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

Updates an existing API Management service.

```sql
UPDATE azure.apimanagement.api_management_service
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
sku,
systemData,
tags,
type,
zones;
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

Creates or updates an API Management service. This is long running operation and could take several minutes to complete.

```sql
REPLACE azure.apimanagement.api_management_service
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
sku,
systemData,
tags,
type,
zones;
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

Deletes an existing API Management service.

```sql
DELETE FROM azure.apimanagement.api_management_service
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_sso_token"
    values={[
        { label: 'get_sso_token', value: 'get_sso_token' },
        { label: 'get_domain_ownership_identifier', value: 'get_domain_ownership_identifier' },
        { label: 'restore', value: 'restore' },
        { label: 'backup', value: 'backup' },
        { label: 'migrate_to_stv2', value: 'migrate_to_stv2' },
        { label: 'apply_network_configuration_updates', value: 'apply_network_configuration_updates' },
        { label: 'refresh_hostnames', value: 'refresh_hostnames' },
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="get_sso_token">

Gets the Single-Sign-On token for the API Management Service which is valid for 5 Minutes.

```sql
EXEC azure.apimanagement.api_management_service.get_sso_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_domain_ownership_identifier">

Get the custom domain ownership identifier for an API Management service.

```sql
EXEC azure.apimanagement.api_management_service.get_domain_ownership_identifier 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restore">

Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete.

```sql
EXEC azure.apimanagement.api_management_service.restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"storageAccount": "{{ storageAccount }}", 
"containerName": "{{ containerName }}", 
"backupName": "{{ backupName }}", 
"accessType": "{{ accessType }}", 
"accessKey": "{{ accessKey }}", 
"clientId": "{{ clientId }}"
}'
;
```
</TabItem>
<TabItem value="backup">

Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.

```sql
EXEC azure.apimanagement.api_management_service.backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"storageAccount": "{{ storageAccount }}", 
"containerName": "{{ containerName }}", 
"backupName": "{{ backupName }}", 
"accessType": "{{ accessType }}", 
"accessKey": "{{ accessKey }}", 
"clientId": "{{ clientId }}"
}'
;
```
</TabItem>
<TabItem value="migrate_to_stv2">

Upgrades an API Management service to the Stv2 platform. For details refer to `https://aka.ms/apim-migrate-stv2 `_. This change is not reversible. This is long running operation and could take several minutes to complete.

```sql
EXEC azure.apimanagement.api_management_service.migrate_to_stv2 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"mode": "{{ mode }}"
}'
;
```
</TabItem>
<TabItem value="apply_network_configuration_updates">

Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated DNS changes.

```sql
EXEC azure.apimanagement.api_management_service.apply_network_configuration_updates 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}"
}'
;
```
</TabItem>
<TabItem value="refresh_hostnames">

Force Refresh the SSL certificate attached to the Custom Hostnames configured using secret from KeyVault on the Api Management service.

```sql
EXEC azure.apimanagement.api_management_service.refresh_hostnames 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks availability and correctness of a name for an API Management service.

```sql
EXEC azure.apimanagement.api_management_service.check_name_availability 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}"
}'
;
```
</TabItem>
</Tabs>
