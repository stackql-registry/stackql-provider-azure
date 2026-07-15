--- 
title: storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts
  - storage
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

Creates, updates, deletes, gets or lists a <code>storage_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.storage_accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_account_sas"
    values={[
        { label: 'list_account_sas', value: 'list_account_sas' },
        { label: 'list_service_sas', value: 'list_service_sas' },
        { label: 'get_customer_initiated_migration', value: 'get_customer_initiated_migration' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_account_sas">

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
    <td><CopyableCode code="accountSasToken" /></td>
    <td><code>string</code></td>
    <td>List SAS credentials of storage account.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_service_sas">

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
    <td><CopyableCode code="serviceSasToken" /></td>
    <td><code>string</code></td>
    <td>List service SAS credentials of specific resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_customer_initiated_migration">

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
    <td><CopyableCode code="migrationFailedDetailedReason" /></td>
    <td><code>string</code></td>
    <td>Reason for migration failure.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationFailedReason" /></td>
    <td><code>string</code></td>
    <td>Error code for migration failure.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationStatus" /></td>
    <td><code>string</code></td>
    <td>Current status of migration. Known values are: "Invalid", "SubmittedForConversion", "InProgress", "Complete", and "Failed". (Invalid, SubmittedForConversion, InProgress, Complete, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSkuName" /></td>
    <td><code>string</code></td>
    <td>Target sku name for the account. Required. Known values are: "Standard_LRS", "Standard_GRS", "Standard_RAGRS", "Standard_ZRS", "Premium_LRS", "Premium_ZRS", "Standard_GZRS", "Standard_RAGZRS", "StandardV2_LRS", "StandardV2_GRS", "StandardV2_ZRS", "StandardV2_GZRS", "PremiumV2_LRS", and "PremiumV2_ZRS". (Standard_LRS, Standard_GRS, Standard_RAGRS, Standard_ZRS, Premium_LRS, Premium_ZRS, Standard_GZRS, Standard_RAGZRS, StandardV2_LRS, StandardV2_GRS, StandardV2_ZRS, StandardV2_GZRS, PremiumV2_LRS, PremiumV2_ZRS)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_keys">

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
    <td><CopyableCode code="keys" /></td>
    <td><code>array</code></td>
    <td>Gets the list of storage account keys and their properties for the specified storage account.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Gets an error message explaining the Reason value in more detail.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Gets a boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or is invalid and cannot be used.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Gets the reason that a storage account name could not be used. The Reason element is only returned if NameAvailable is false. Known values are: "AccountNameInvalid" and "AlreadyExists". (AccountNameInvalid, AlreadyExists)</td>
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
    <td><CopyableCode code="accessTier" /></td>
    <td><code>string</code></td>
    <td>Required for storage accounts where kind = BlobStorage. The access tier is used for billing. The 'Premium' access tier is the default value for premium block blobs storage account type and it cannot be changed for the premium block blobs storage account type. Known values are: "Hot", "Cool", "Premium", "Cold", and "Smart". (Hot, Cool, Premium, Cold, Smart)</td>
</tr>
<tr>
    <td><CopyableCode code="accountMigrationInProgress" /></td>
    <td><code>boolean</code></td>
    <td>If customer initiated account migration is in progress, the value will be true else it will be null.</td>
</tr>
<tr>
    <td><CopyableCode code="allowBlobPublicAccess" /></td>
    <td><code>boolean</code></td>
    <td>Allow or disallow public access to all blobs or containers in the storage account. The default interpretation is false for this property.</td>
</tr>
<tr>
    <td><CopyableCode code="allowCrossTenantReplication" /></td>
    <td><code>boolean</code></td>
    <td>Allow or disallow cross AAD tenant object replication. Set this property to true for new or existing accounts only if object replication policies will involve storage accounts in different AAD tenants. The default interpretation is false for new accounts to follow best security practices by default.</td>
</tr>
<tr>
    <td><CopyableCode code="allowSharedKeyAccess" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the storage account permits requests to be authorized with the account access key via Shared Key. If false, then all requests, including shared access signatures, must be authorized with Azure Active Directory (Azure AD). The default value is null, which is equivalent to true.</td>
</tr>
<tr>
    <td><CopyableCode code="allowSharedKeyAccessForServices" /></td>
    <td><code>object</code></td>
    <td>Indicate shared key access properties at service level.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedCopyScope" /></td>
    <td><code>string</code></td>
    <td>Restrict copy to and from Storage Accounts within an AAD tenant or with Private Links to the same VNet. Known values are: "PrivateLink", "AAD", and "All". (PrivateLink, AAD, All)</td>
</tr>
<tr>
    <td><CopyableCode code="azureFilesIdentityBasedAuthentication" /></td>
    <td><code>object</code></td>
    <td>Provides the identity based authentication settings for Azure Files.</td>
</tr>
<tr>
    <td><CopyableCode code="blobRestoreStatus" /></td>
    <td><code>object</code></td>
    <td>Blob restore status.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the creation date and time of the storage account in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomain" /></td>
    <td><code>object</code></td>
    <td>Gets the custom domain the user assigned to this storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollaborationPolicyProperties" /></td>
    <td><code>object</code></td>
    <td>Data Collaboration policy for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultToOAuthAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>A boolean flag which indicates whether the default authentication is OAuth or not. The default interpretation is false for this property.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsEndpointType" /></td>
    <td><code>string</code></td>
    <td>Allows you to specify the type of endpoint. Set this to AzureDNSZone to create a large number of accounts in a single subscription, which creates accounts in an Azure DNS Zone and the endpoint URL will have an alphanumeric DNS Zone identifier. Known values are: "Standard" and "AzureDnsZone". (Standard, AzureDnsZone)</td>
</tr>
<tr>
    <td><CopyableCode code="dualStackEndpointPreference" /></td>
    <td><code>object</code></td>
    <td>Maintains information about the Internet protocol opted by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="enableExtendedGroups" /></td>
    <td><code>boolean</code></td>
    <td>Enables extended group support with local users feature, if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption settings to be used for server-side encryption for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverInProgress" /></td>
    <td><code>boolean</code></td>
    <td>If the failover is in progress, the value will be true, otherwise, it will be null.</td>
</tr>
<tr>
    <td><CopyableCode code="geoPriorityReplicationStatus" /></td>
    <td><code>object</code></td>
    <td>Status indicating whether Geo Priority Replication is enabled for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="geoReplicationStats" /></td>
    <td><code>object</code></td>
    <td>Geo Replication Stats.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableStorageWithVersioning" /></td>
    <td><code>object</code></td>
    <td>The property is immutable and can only be set to true at the account creation time. When set to true, it enables object level immutability for all the containers in the account by default.</td>
</tr>
<tr>
    <td><CopyableCode code="isHnsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Account HierarchicalNamespace enabled if sets to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalUserEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enables local users feature, if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isNfsV3Enabled" /></td>
    <td><code>boolean</code></td>
    <td>NFS 3.0 protocol support enabled if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSftpEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enables Secure File Transfer Protocol, if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSkuConversionBlocked" /></td>
    <td><code>boolean</code></td>
    <td>This property will be set to true or false on an event of ongoing migration. Default value is null.</td>
</tr>
<tr>
    <td><CopyableCode code="keyCreationTime" /></td>
    <td><code>object</code></td>
    <td>Storage account keys creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="keyPolicy" /></td>
    <td><code>object</code></td>
    <td>KeyPolicy assigned to the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Gets the Kind. Known values are: "Storage", "StorageV2", "BlobStorage", "FileStorage", and "BlockBlobStorage". (Storage, StorageV2, BlobStorage, FileStorage, BlockBlobStorage)</td>
</tr>
<tr>
    <td><CopyableCode code="largeFileSharesState" /></td>
    <td><code>string</code></td>
    <td>Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="lastGeoFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Set the minimum TLS version to be permitted on requests to storage. The default interpretation is TLS 1.0 for this property. Minimum TLS version 1.3 version is not supported. Known values are: "TLS1_0", "TLS1_1", "TLS1_2", and "TLS1_3". (TLS1_0, TLS1_1, TLS1_2, TLS1_3)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Network rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Optional. Gets or sets the zonal placement details for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryEndpoints" /></td>
    <td><code>object</code></td>
    <td>Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object. Note that Standard_ZRS and Premium_LRS accounts only return the blob endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryLocation" /></td>
    <td><code>string</code></td>
    <td>Gets the location of the primary data center for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the storage account at the time the operation was called. Known values are: "Creating", "ResolvingDNS", and "Succeeded". (Creating, ResolvingDNS, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Allow, disallow, or let Network Security Perimeter configuration to evaluate public network access to Storage Account. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="routingPreference" /></td>
    <td><code>object</code></td>
    <td>Maintains information about the network routing choice opted by the user for data transfer.</td>
</tr>
<tr>
    <td><CopyableCode code="sasPolicy" /></td>
    <td><code>object</code></td>
    <td>SasPolicy assigned to the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryEndpoints" /></td>
    <td><code>object</code></td>
    <td>Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object from the secondary location of the storage account. Only available if the SKU name is Standard_RAGRS.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryLocation" /></td>
    <td><code>string</code></td>
    <td>Gets the location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Gets the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="statusOfPrimary" /></td>
    <td><code>string</code></td>
    <td>Gets the status indicating whether the primary location of the storage account is available or unavailable. Known values are: "available" and "unavailable". (available, unavailable)</td>
</tr>
<tr>
    <td><CopyableCode code="statusOfSecondary" /></td>
    <td><code>string</code></td>
    <td>Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS. Known values are: "available" and "unavailable". (available, unavailable)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountSkuConversionStatus" /></td>
    <td><code>object</code></td>
    <td>This property is readOnly and is set by server during asynchronous storage account sku conversion operations.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHttpsTrafficOnly" /></td>
    <td><code>boolean</code></td>
    <td>Allows https traffic only to storage service if sets to true.</td>
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
    <td><CopyableCode code="accessTier" /></td>
    <td><code>string</code></td>
    <td>Required for storage accounts where kind = BlobStorage. The access tier is used for billing. The 'Premium' access tier is the default value for premium block blobs storage account type and it cannot be changed for the premium block blobs storage account type. Known values are: "Hot", "Cool", "Premium", "Cold", and "Smart". (Hot, Cool, Premium, Cold, Smart)</td>
</tr>
<tr>
    <td><CopyableCode code="accountMigrationInProgress" /></td>
    <td><code>boolean</code></td>
    <td>If customer initiated account migration is in progress, the value will be true else it will be null.</td>
</tr>
<tr>
    <td><CopyableCode code="allowBlobPublicAccess" /></td>
    <td><code>boolean</code></td>
    <td>Allow or disallow public access to all blobs or containers in the storage account. The default interpretation is false for this property.</td>
</tr>
<tr>
    <td><CopyableCode code="allowCrossTenantReplication" /></td>
    <td><code>boolean</code></td>
    <td>Allow or disallow cross AAD tenant object replication. Set this property to true for new or existing accounts only if object replication policies will involve storage accounts in different AAD tenants. The default interpretation is false for new accounts to follow best security practices by default.</td>
</tr>
<tr>
    <td><CopyableCode code="allowSharedKeyAccess" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the storage account permits requests to be authorized with the account access key via Shared Key. If false, then all requests, including shared access signatures, must be authorized with Azure Active Directory (Azure AD). The default value is null, which is equivalent to true.</td>
</tr>
<tr>
    <td><CopyableCode code="allowSharedKeyAccessForServices" /></td>
    <td><code>object</code></td>
    <td>Indicate shared key access properties at service level.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedCopyScope" /></td>
    <td><code>string</code></td>
    <td>Restrict copy to and from Storage Accounts within an AAD tenant or with Private Links to the same VNet. Known values are: "PrivateLink", "AAD", and "All". (PrivateLink, AAD, All)</td>
</tr>
<tr>
    <td><CopyableCode code="azureFilesIdentityBasedAuthentication" /></td>
    <td><code>object</code></td>
    <td>Provides the identity based authentication settings for Azure Files.</td>
</tr>
<tr>
    <td><CopyableCode code="blobRestoreStatus" /></td>
    <td><code>object</code></td>
    <td>Blob restore status.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the creation date and time of the storage account in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomain" /></td>
    <td><code>object</code></td>
    <td>Gets the custom domain the user assigned to this storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollaborationPolicyProperties" /></td>
    <td><code>object</code></td>
    <td>Data Collaboration policy for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultToOAuthAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>A boolean flag which indicates whether the default authentication is OAuth or not. The default interpretation is false for this property.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsEndpointType" /></td>
    <td><code>string</code></td>
    <td>Allows you to specify the type of endpoint. Set this to AzureDNSZone to create a large number of accounts in a single subscription, which creates accounts in an Azure DNS Zone and the endpoint URL will have an alphanumeric DNS Zone identifier. Known values are: "Standard" and "AzureDnsZone". (Standard, AzureDnsZone)</td>
</tr>
<tr>
    <td><CopyableCode code="dualStackEndpointPreference" /></td>
    <td><code>object</code></td>
    <td>Maintains information about the Internet protocol opted by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="enableExtendedGroups" /></td>
    <td><code>boolean</code></td>
    <td>Enables extended group support with local users feature, if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption settings to be used for server-side encryption for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverInProgress" /></td>
    <td><code>boolean</code></td>
    <td>If the failover is in progress, the value will be true, otherwise, it will be null.</td>
</tr>
<tr>
    <td><CopyableCode code="geoPriorityReplicationStatus" /></td>
    <td><code>object</code></td>
    <td>Status indicating whether Geo Priority Replication is enabled for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="geoReplicationStats" /></td>
    <td><code>object</code></td>
    <td>Geo Replication Stats.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableStorageWithVersioning" /></td>
    <td><code>object</code></td>
    <td>The property is immutable and can only be set to true at the account creation time. When set to true, it enables object level immutability for all the containers in the account by default.</td>
</tr>
<tr>
    <td><CopyableCode code="isHnsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Account HierarchicalNamespace enabled if sets to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalUserEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enables local users feature, if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isNfsV3Enabled" /></td>
    <td><code>boolean</code></td>
    <td>NFS 3.0 protocol support enabled if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSftpEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enables Secure File Transfer Protocol, if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSkuConversionBlocked" /></td>
    <td><code>boolean</code></td>
    <td>This property will be set to true or false on an event of ongoing migration. Default value is null.</td>
</tr>
<tr>
    <td><CopyableCode code="keyCreationTime" /></td>
    <td><code>object</code></td>
    <td>Storage account keys creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="keyPolicy" /></td>
    <td><code>object</code></td>
    <td>KeyPolicy assigned to the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Gets the Kind. Known values are: "Storage", "StorageV2", "BlobStorage", "FileStorage", and "BlockBlobStorage". (Storage, StorageV2, BlobStorage, FileStorage, BlockBlobStorage)</td>
</tr>
<tr>
    <td><CopyableCode code="largeFileSharesState" /></td>
    <td><code>string</code></td>
    <td>Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="lastGeoFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Set the minimum TLS version to be permitted on requests to storage. The default interpretation is TLS 1.0 for this property. Minimum TLS version 1.3 version is not supported. Known values are: "TLS1_0", "TLS1_1", "TLS1_2", and "TLS1_3". (TLS1_0, TLS1_1, TLS1_2, TLS1_3)</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Network rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Optional. Gets or sets the zonal placement details for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryEndpoints" /></td>
    <td><code>object</code></td>
    <td>Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object. Note that Standard_ZRS and Premium_LRS accounts only return the blob endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryLocation" /></td>
    <td><code>string</code></td>
    <td>Gets the location of the primary data center for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the storage account at the time the operation was called. Known values are: "Creating", "ResolvingDNS", and "Succeeded". (Creating, ResolvingDNS, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Allow, disallow, or let Network Security Perimeter configuration to evaluate public network access to Storage Account. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="routingPreference" /></td>
    <td><code>object</code></td>
    <td>Maintains information about the network routing choice opted by the user for data transfer.</td>
</tr>
<tr>
    <td><CopyableCode code="sasPolicy" /></td>
    <td><code>object</code></td>
    <td>SasPolicy assigned to the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryEndpoints" /></td>
    <td><code>object</code></td>
    <td>Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object from the secondary location of the storage account. Only available if the SKU name is Standard_RAGRS.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryLocation" /></td>
    <td><code>string</code></td>
    <td>Gets the location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Gets the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="statusOfPrimary" /></td>
    <td><code>string</code></td>
    <td>Gets the status indicating whether the primary location of the storage account is available or unavailable. Known values are: "available" and "unavailable". (available, unavailable)</td>
</tr>
<tr>
    <td><CopyableCode code="statusOfSecondary" /></td>
    <td><code>string</code></td>
    <td>Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS. Known values are: "available" and "unavailable". (available, unavailable)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountSkuConversionStatus" /></td>
    <td><code>object</code></td>
    <td>This property is readOnly and is set by server during asynchronous storage account sku conversion operations.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHttpsTrafficOnly" /></td>
    <td><code>boolean</code></td>
    <td>Allows https traffic only to storage service if sets to true.</td>
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
    <td><a href="#list_account_sas"><CopyableCode code="list_account_sas" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List SAS credentials of a storage account.</td>
</tr>
<tr>
    <td><a href="#list_service_sas"><CopyableCode code="list_service_sas" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List service SAS credentials of a specific resource.</td>
</tr>
<tr>
    <td><a href="#get_customer_initiated_migration"><CopyableCode code="get_customer_initiated_migration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of the ongoing migration for the specified storage account.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists the access keys or Kerberos keys (if active directory enabled) for the specified storage account.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks that the storage account name is valid and is not already in use.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sku"><code>sku</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Asynchronously creates a new storage account with the specified parameters. If an account is already created and a subsequent create request is issued with different properties, the account properties will be updated. If an account is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The update operation can be used to update the SKU, encryption, access tier, or tags for a storage account. It can also be used to map the account to a custom domain. Only one custom domain is supported per storage account; the replacement/change of custom domain is not supported. In order to replace an old custom domain, the old value must be cleared/unregistered before a new value can be set. The update of multiple properties is supported. This call does not change the storage keys for the account. If you want to change the storage account keys, use the regenerate keys operation. The location and name of the storage account cannot be changed after creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a storage account in Microsoft Azure.</td>
</tr>
<tr>
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyName"><code>keyName</code></a></td>
    <td></td>
    <td>Regenerates one of the access keys or Kerberos keys for the specified storage account.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-failoverType"><code>failoverType</code></a></td>
    <td>A failover request can be triggered for a storage account in the event a primary endpoint becomes unavailable for any reason. The failover occurs from the storage account's primary cluster to the secondary cluster for RA-GRS accounts. The secondary cluster will become primary after failover and the account is converted to LRS. In the case of a Planned Failover, the primary and secondary clusters are swapped after failover and the account remains geo-replicated. Failover should continue to be used in the event of availability issues as Planned failover is only available while the primary and secondary endpoints are available. The primary use case of a Planned Failover is disaster recovery testing drills. This type of failover is invoked by setting FailoverType parameter to 'Planned'. Learn more about the failover options here- `https://learn.microsoft.com/azure/storage/common/storage-disaster-recovery-guidance `_.</td>
</tr>
<tr>
    <td><a href="#hierarchical_namespace_migration"><CopyableCode code="hierarchical_namespace_migration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-requestType"><code>requestType</code></a></td>
    <td></td>
    <td>Live Migration of storage account to enable Hns.</td>
</tr>
<tr>
    <td><a href="#abort_hierarchical_namespace_migration"><CopyableCode code="abort_hierarchical_namespace_migration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Abort live Migration of storage account to enable Hns.</td>
</tr>
<tr>
    <td><a href="#customer_initiated_migration"><CopyableCode code="customer_initiated_migration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Account Migration request can be triggered for a storage account to change its redundancy level. The migration updates the non-zonal redundant storage account to a zonal redundant account or vice-versa in order to have better reliability and availability. Zone-redundant storage (ZRS) replicates your storage account synchronously across three Azure availability zones in the primary region.</td>
</tr>
<tr>
    <td><a href="#restore_blob_ranges"><CopyableCode code="restore_blob_ranges" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-timeToRestore"><code>timeToRestore</code></a>, <a href="#parameter-blobRanges"><code>blobRanges</code></a></td>
    <td></td>
    <td>Restore blobs in the specified blob ranges.</td>
</tr>
<tr>
    <td><a href="#revoke_user_delegation_keys"><CopyableCode code="revoke_user_delegation_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revoke user delegation keys.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. Required.</td>
</tr>
<tr id="parameter-migration_name">
    <td><CopyableCode code="migration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Storage Account Migration. It should always be 'default'. "default" Required.</td>
</tr>
<tr id="parameter-requestType">
    <td><CopyableCode code="requestType" /></td>
    <td><code>string</code></td>
    <td>Required. Hierarchical namespace migration type can either be a hierarchical namespace validation request 'HnsOnValidationRequest' or a hydration request 'HnsOnHydrationRequest'. The validation request will validate the migration whereas the hydration request will migrate the account. Required.</td>
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
    <td>May be used to expand the properties within account's properties. By default, data is not included when fetching properties. Currently we only support geoReplicationStats and blobRestoreStatus. Known values are: "geoReplicationStats" and "blobRestoreStatus". Default value is None.</td>
</tr>
<tr id="parameter-failoverType">
    <td><CopyableCode code="failoverType" /></td>
    <td><code>string</code></td>
    <td>The parameter is set to 'Planned' to indicate whether a Planned failover is requested. Known values are "Planned" and None. Default value is "Planned".</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_account_sas"
    values={[
        { label: 'list_account_sas', value: 'list_account_sas' },
        { label: 'list_service_sas', value: 'list_service_sas' },
        { label: 'get_customer_initiated_migration', value: 'get_customer_initiated_migration' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_account_sas">

List SAS credentials of a storage account.

```sql
SELECT
accountSasToken
FROM azure.storage.storage_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_service_sas">

List service SAS credentials of a specific resource.

```sql
SELECT
serviceSasToken
FROM azure.storage.storage_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_customer_initiated_migration">

Gets the status of the ongoing migration for the specified storage account.

```sql
SELECT
id,
name,
migrationFailedDetailedReason,
migrationFailedReason,
migrationStatus,
systemData,
targetSkuName,
type
FROM azure.storage.storage_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND migration_name = '{{ migration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_keys">

Lists the access keys or Kerberos keys (if active directory enabled) for the specified storage account.

```sql
SELECT
keys
FROM azure.storage.storage_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks that the storage account name is valid and is not already in use.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.storage.storage_accounts
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this.

```sql
SELECT
id,
name,
accessTier,
accountMigrationInProgress,
allowBlobPublicAccess,
allowCrossTenantReplication,
allowSharedKeyAccess,
allowSharedKeyAccessForServices,
allowedCopyScope,
azureFilesIdentityBasedAuthentication,
blobRestoreStatus,
creationTime,
customDomain,
dataCollaborationPolicyProperties,
defaultToOAuthAuthentication,
dnsEndpointType,
dualStackEndpointPreference,
enableExtendedGroups,
encryption,
extendedLocation,
failoverInProgress,
geoPriorityReplicationStatus,
geoReplicationStats,
identity,
immutableStorageWithVersioning,
isHnsEnabled,
isLocalUserEnabled,
isNfsV3Enabled,
isSftpEnabled,
isSkuConversionBlocked,
keyCreationTime,
keyPolicy,
kind,
largeFileSharesState,
lastGeoFailoverTime,
location,
minimumTlsVersion,
networkAcls,
placement,
primaryEndpoints,
primaryLocation,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
routingPreference,
sasPolicy,
secondaryEndpoints,
secondaryLocation,
sku,
statusOfPrimary,
statusOfSecondary,
storageAccountSkuConversionStatus,
supportsHttpsTrafficOnly,
systemData,
tags,
type,
zones
FROM azure.storage.storage_accounts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this.

```sql
SELECT
id,
name,
accessTier,
accountMigrationInProgress,
allowBlobPublicAccess,
allowCrossTenantReplication,
allowSharedKeyAccess,
allowSharedKeyAccessForServices,
allowedCopyScope,
azureFilesIdentityBasedAuthentication,
blobRestoreStatus,
creationTime,
customDomain,
dataCollaborationPolicyProperties,
defaultToOAuthAuthentication,
dnsEndpointType,
dualStackEndpointPreference,
enableExtendedGroups,
encryption,
extendedLocation,
failoverInProgress,
geoPriorityReplicationStatus,
geoReplicationStats,
identity,
immutableStorageWithVersioning,
isHnsEnabled,
isLocalUserEnabled,
isNfsV3Enabled,
isSftpEnabled,
isSkuConversionBlocked,
keyCreationTime,
keyPolicy,
kind,
largeFileSharesState,
lastGeoFailoverTime,
location,
minimumTlsVersion,
networkAcls,
placement,
primaryEndpoints,
primaryLocation,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
routingPreference,
sasPolicy,
secondaryEndpoints,
secondaryLocation,
sku,
statusOfPrimary,
statusOfSecondary,
storageAccountSkuConversionStatus,
supportsHttpsTrafficOnly,
systemData,
tags,
type,
zones
FROM azure.storage.storage_accounts
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

Asynchronously creates a new storage account with the specified parameters. If an account is already created and a subsequent create request is issued with different properties, the account properties will be updated. If an account is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed.

```sql
INSERT INTO azure.storage.storage_accounts (
sku,
kind,
location,
extendedLocation,
zones,
placement,
tags,
identity,
properties,
resource_group_name,
account_name,
subscription_id
)
SELECT 
'{{ sku }}' /* required */,
'{{ kind }}' /* required */,
'{{ location }}' /* required */,
'{{ extendedLocation }}',
'{{ zones }}',
'{{ placement }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
placement,
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
- name: storage_accounts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the storage_accounts resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the storage_accounts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the storage_accounts resource.
    - name: sku
      description: |
        Required. Gets or sets the SKU name. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Required. Indicates the type of storage account. Required. Known values are: "Storage", "StorageV2", "BlobStorage", "FileStorage", and "BlockBlobStorage".
      valid_values: ['Storage', 'StorageV2', 'BlobStorage', 'FileStorage', 'BlockBlobStorage']
    - name: location
      value: "{{ location }}"
      description: |
        Required. Gets or sets the location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo region is specified on update, the request will succeed. Required.
    - name: extendedLocation
      description: |
        Optional. Set the extended location of the resource. If not set, the storage account will be created in Azure main region. Otherwise it will be created in the specified extended location.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        Optional. Gets or sets the pinned logical availability zone for the storage account.
    - name: placement
      description: |
        Optional. Gets or sets the zonal placement details for the storage account.
      value:
        zonePlacementPolicy: "{{ zonePlacementPolicy }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Gets or sets a list of key value pairs that describe the resource. These tags can be used for viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no greater than 128 characters and a value with a length no greater than 256 characters.
    - name: identity
      description: |
        The identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      description: |
        The parameters used to create the storage account.
      value:
        allowedCopyScope: "{{ allowedCopyScope }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        sasPolicy:
          sasExpirationPeriod: "{{ sasExpirationPeriod }}"
          expirationAction: "{{ expirationAction }}"
        keyPolicy:
          keyExpirationPeriodInDays: {{ keyExpirationPeriodInDays }}
        customDomain:
          name: "{{ name }}"
          useSubDomainName: {{ useSubDomainName }}
        encryption:
          services:
            blob:
              enabled: {{ enabled }}
              lastEnabledTime: "{{ lastEnabledTime }}"
              keyType: "{{ keyType }}"
            file:
              enabled: {{ enabled }}
              lastEnabledTime: "{{ lastEnabledTime }}"
              keyType: "{{ keyType }}"
            table:
              enabled: {{ enabled }}
              lastEnabledTime: "{{ lastEnabledTime }}"
              keyType: "{{ keyType }}"
            queue:
              enabled: {{ enabled }}
              lastEnabledTime: "{{ lastEnabledTime }}"
              keyType: "{{ keyType }}"
          keySource: "{{ keySource }}"
          requireInfrastructureEncryption: {{ requireInfrastructureEncryption }}
          keyvaultproperties:
            keyname: "{{ keyname }}"
            keyversion: "{{ keyversion }}"
            keyvaulturi: "{{ keyvaulturi }}"
            currentVersionedKeyIdentifier: "{{ currentVersionedKeyIdentifier }}"
            lastKeyRotationTimestamp: "{{ lastKeyRotationTimestamp }}"
            currentVersionedKeyExpirationTimestamp: "{{ currentVersionedKeyExpirationTimestamp }}"
          identity:
            userAssignedIdentity: "{{ userAssignedIdentity }}"
            federatedIdentityClientId: "{{ federatedIdentityClientId }}"
        networkAcls:
          bypass: "{{ bypass }}"
          resourceAccessRules:
            - tenantId: "{{ tenantId }}"
              resourceId: "{{ resourceId }}"
          virtualNetworkRules:
            - id: "{{ id }}"
              action: "{{ action }}"
              state: "{{ state }}"
          ipRules:
            - value: "{{ value }}"
              action: "{{ action }}"
          ipv6Rules:
            - value: "{{ value }}"
              action: "{{ action }}"
          defaultAction: "{{ defaultAction }}"
        accessTier: "{{ accessTier }}"
        azureFilesIdentityBasedAuthentication:
          directoryServiceOptions: "{{ directoryServiceOptions }}"
          activeDirectoryProperties:
            domainName: "{{ domainName }}"
            netBiosDomainName: "{{ netBiosDomainName }}"
            forestName: "{{ forestName }}"
            domainGuid: "{{ domainGuid }}"
            domainSid: "{{ domainSid }}"
            azureStorageSid: "{{ azureStorageSid }}"
            samAccountName: "{{ samAccountName }}"
            accountType: "{{ accountType }}"
          defaultSharePermission: "{{ defaultSharePermission }}"
          smbOAuthSettings:
            isSmbOAuthEnabled: {{ isSmbOAuthEnabled }}
        supportsHttpsTrafficOnly: {{ supportsHttpsTrafficOnly }}
        isSftpEnabled: {{ isSftpEnabled }}
        isLocalUserEnabled: {{ isLocalUserEnabled }}
        enableExtendedGroups: {{ enableExtendedGroups }}
        isHnsEnabled: {{ isHnsEnabled }}
        largeFileSharesState: "{{ largeFileSharesState }}"
        routingPreference:
          routingChoice: "{{ routingChoice }}"
          publishMicrosoftEndpoints: {{ publishMicrosoftEndpoints }}
          publishInternetEndpoints: {{ publishInternetEndpoints }}
        dualStackEndpointPreference:
          publishIpv6Endpoint: {{ publishIpv6Endpoint }}
        allowBlobPublicAccess: {{ allowBlobPublicAccess }}
        minimumTlsVersion: "{{ minimumTlsVersion }}"
        allowSharedKeyAccess: {{ allowSharedKeyAccess }}
        isNfsV3Enabled: {{ isNfsV3Enabled }}
        allowCrossTenantReplication: {{ allowCrossTenantReplication }}
        defaultToOAuthAuthentication: {{ defaultToOAuthAuthentication }}
        immutableStorageWithVersioning:
          enabled: {{ enabled }}
          immutabilityPolicy:
            immutabilityPeriodSinceCreationInDays: {{ immutabilityPeriodSinceCreationInDays }}
            state: "{{ state }}"
            allowProtectedAppendWrites: {{ allowProtectedAppendWrites }}
        dnsEndpointType: "{{ dnsEndpointType }}"
        geoPriorityReplicationStatus:
          isBlobEnabled: {{ isBlobEnabled }}
        allowSharedKeyAccessForServices:
          blob:
            enabled: {{ enabled }}
          file:
            enabled: {{ enabled }}
          table:
            enabled: {{ enabled }}
          queue:
            enabled: {{ enabled }}
        dataCollaborationPolicyProperties:
          allowStorageConnectors: {{ allowStorageConnectors }}
          allowStorageDataShares: {{ allowStorageDataShares }}
          allowCrossTenantDataSharing: {{ allowCrossTenantDataSharing }}
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

The update operation can be used to update the SKU, encryption, access tier, or tags for a storage account. It can also be used to map the account to a custom domain. Only one custom domain is supported per storage account; the replacement/change of custom domain is not supported. In order to replace an old custom domain, the old value must be cleared/unregistered before a new value can be set. The update of multiple properties is supported. This call does not change the storage keys for the account. If you want to change the storage account keys, use the regenerate keys operation. The location and name of the storage account cannot be changed after creation.

```sql
UPDATE azure.storage.storage_accounts
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
kind = '{{ kind }}',
zones = '{{ zones }}',
placement = '{{ placement }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
placement,
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

Deletes a storage account in Microsoft Azure.

```sql
DELETE FROM azure.storage.storage_accounts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'failover', value: 'failover' },
        { label: 'hierarchical_namespace_migration', value: 'hierarchical_namespace_migration' },
        { label: 'abort_hierarchical_namespace_migration', value: 'abort_hierarchical_namespace_migration' },
        { label: 'customer_initiated_migration', value: 'customer_initiated_migration' },
        { label: 'restore_blob_ranges', value: 'restore_blob_ranges' },
        { label: 'revoke_user_delegation_keys', value: 'revoke_user_delegation_keys' }
    ]}
>
<TabItem value="get_properties">

Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys.

```sql
EXEC azure.storage.storage_accounts.get_properties 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerates one of the access keys or Kerberos keys for the specified storage account.

```sql
EXEC azure.storage.storage_accounts.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}"
}'
;
```
</TabItem>
<TabItem value="failover">

A failover request can be triggered for a storage account in the event a primary endpoint becomes unavailable for any reason. The failover occurs from the storage account's primary cluster to the secondary cluster for RA-GRS accounts. The secondary cluster will become primary after failover and the account is converted to LRS. In the case of a Planned Failover, the primary and secondary clusters are swapped after failover and the account remains geo-replicated. Failover should continue to be used in the event of availability issues as Planned failover is only available while the primary and secondary endpoints are available. The primary use case of a Planned Failover is disaster recovery testing drills. This type of failover is invoked by setting FailoverType parameter to 'Planned'. Learn more about the failover options here- `https://learn.microsoft.com/azure/storage/common/storage-disaster-recovery-guidance `_.

```sql
EXEC azure.storage.storage_accounts.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@failoverType='{{ failoverType }}'
;
```
</TabItem>
<TabItem value="hierarchical_namespace_migration">

Live Migration of storage account to enable Hns.

```sql
EXEC azure.storage.storage_accounts.hierarchical_namespace_migration 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@requestType='{{ requestType }}' --required
;
```
</TabItem>
<TabItem value="abort_hierarchical_namespace_migration">

Abort live Migration of storage account to enable Hns.

```sql
EXEC azure.storage.storage_accounts.abort_hierarchical_namespace_migration 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="customer_initiated_migration">

Account Migration request can be triggered for a storage account to change its redundancy level. The migration updates the non-zonal redundant storage account to a zonal redundant account or vice-versa in order to have better reliability and availability. Zone-redundant storage (ZRS) replicates your storage account synchronously across three Azure availability zones in the primary region.

```sql
EXEC azure.storage.storage_accounts.customer_initiated_migration 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="restore_blob_ranges">

Restore blobs in the specified blob ranges.

```sql
EXEC azure.storage.storage_accounts.restore_blob_ranges 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"timeToRestore": "{{ timeToRestore }}", 
"blobRanges": "{{ blobRanges }}"
}'
;
```
</TabItem>
<TabItem value="revoke_user_delegation_keys">

Revoke user delegation keys.

```sql
EXEC azure.storage.storage_accounts.revoke_user_delegation_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
