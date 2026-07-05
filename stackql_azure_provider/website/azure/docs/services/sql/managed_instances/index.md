--- 
title: managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_instance_pool', value: 'list_by_instance_pool' },
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password (required for managed instance creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory administrator can be utilized during instance creation and for instance updates, except for the azureADOnlyAuthentication property. To update the azureADOnlyAuthentication property, individual API must be used.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationMetadata" /></td>
    <td><code>string</code></td>
    <td>The managed instance's authentication metadata lookup mode. Known values are: "AzureAD", "Paired", and "Windows". (AzureAD, Paired, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the Managed Instance creation.</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="databaseFormat" /></td>
    <td><code>string</code></td>
    <td>Specifies the internal format of instance databases specific to the SQL engine version. Known values are: "AlwaysUpToDate", "SQLServer2022", and "SQLServer2025". (AlwaysUpToDate, SQLServer2022, SQLServer2025)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZone" /></td>
    <td><code>string</code></td>
    <td>The Dns Zone that the managed instance is in.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZonePartner" /></td>
    <td><code>string</code></td>
    <td>The resource id of another managed instance whose DNS zone this managed instance will share after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="externalGovernanceStatus" /></td>
    <td><code>string</code></td>
    <td>Status of external governance. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsage" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage. Possible values are 'Active' (default value) and 'Passive' (customer uses the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsageDetected" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage detected. Possible values are 'Active' (customer does not meet the requirements to use the secondary as Passive DR) and 'Passive' (customer meets the requirements to use the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="instancePoolId" /></td>
    <td><code>string</code></td>
    <td>The Id of the instance pool this managed server belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="isGeneralPurposeV2" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this is a GPv2 variant of General Purpose edition.</td>
</tr>
<tr>
    <td><CopyableCode code="keyId" /></td>
    <td><code>string</code></td>
    <td>A CMK URI of the key to use for encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses). Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Specifies maintenance configuration id to apply to this managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceCreateMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of database creation. Default: Regular instance creation. Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified. Known values are: "Default" and "PointInTimeRestore". (Default, PointInTimeRestore)</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Memory size in GB. Minimum value: 28. Maximum value: 870. Minimum and maximum value depend on the number of vCores and service tier. Read more about resource limits: `https://aka.ms/mi-resource-limits-api `_.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Minimal TLS version. Allowed values: 'None', '1.0', '1.1', '1.2'.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingModel" /></td>
    <td><code>string</code></td>
    <td>Pricing model of Managed Instance. Known values are: "Regular" and "Freemium". (Regular, Freemium)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryUserAssignedIdentityId" /></td>
    <td><code>string</code></td>
    <td>The resource id of a user assigned identity to be used by default.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of managed instance. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="proxyOverride" /></td>
    <td><code>string</code></td>
    <td>Connection type used for connecting to the instance. Known values are: "Proxy", "Redirect", and "Default". (Proxy, Redirect, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="publicDataEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the public data endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type to be used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedLogicalAvailabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the logical availability zone Managed Instance is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code>object</code></td>
    <td>The managed instance's service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Managed instance SKU. Allowed values for sku.name: GP_Gen5 (General Purpose, Standard-series); GP_G8IM (General Purpose, Premium-series); GP_G8IH (General Purpose, Premium-series memory optimized); BC_Gen5 (Business Critical, Standard-Series); BC_G8IM (Business Critical, Premium-series); BC_G8IH (Business Critical, Premium-series memory optimized).</td>
</tr>
<tr>
    <td><CopyableCode code="sourceManagedInstanceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source managed instance associated with create operation of this instance.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="storageIOps" /></td>
    <td><code>integer</code></td>
    <td>Storage IOps. Minimum value: 300. Maximum value: 80000. Increments of 1 IOps allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Storage size in GB. Minimum value: 32. Maximum value: 32768. Increments of 32 GB allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageThroughputMBps" /></td>
    <td><code>integer</code></td>
    <td>Storage throughput MBps parameter is not supported in the instance create/update operation.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet resource ID for the managed instance.</td>
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
    <td><CopyableCode code="timezoneId" /></td>
    <td><code>string</code></td>
    <td>Id of the timezone. Allowed values are timezones supported by Windows. Windows keeps details on supported timezones, including the id, in registry under KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones. You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info. List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. An example of valid timezone id is "Pacific Standard Time" or "W. Europe Standard Time".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>The number of vCores. Allowed values: 4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 128. Supported vCores depends on the selected hardware family and service tier.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualClusterId" /></td>
    <td><code>string</code></td>
    <td>Virtual cluster resource id for the Managed Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the zone-redundancy is enabled.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_instance_pool">

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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password (required for managed instance creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory administrator can be utilized during instance creation and for instance updates, except for the azureADOnlyAuthentication property. To update the azureADOnlyAuthentication property, individual API must be used.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationMetadata" /></td>
    <td><code>string</code></td>
    <td>The managed instance's authentication metadata lookup mode. Known values are: "AzureAD", "Paired", and "Windows". (AzureAD, Paired, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the Managed Instance creation.</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="databaseFormat" /></td>
    <td><code>string</code></td>
    <td>Specifies the internal format of instance databases specific to the SQL engine version. Known values are: "AlwaysUpToDate", "SQLServer2022", and "SQLServer2025". (AlwaysUpToDate, SQLServer2022, SQLServer2025)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZone" /></td>
    <td><code>string</code></td>
    <td>The Dns Zone that the managed instance is in.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZonePartner" /></td>
    <td><code>string</code></td>
    <td>The resource id of another managed instance whose DNS zone this managed instance will share after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="externalGovernanceStatus" /></td>
    <td><code>string</code></td>
    <td>Status of external governance. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsage" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage. Possible values are 'Active' (default value) and 'Passive' (customer uses the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsageDetected" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage detected. Possible values are 'Active' (customer does not meet the requirements to use the secondary as Passive DR) and 'Passive' (customer meets the requirements to use the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="instancePoolId" /></td>
    <td><code>string</code></td>
    <td>The Id of the instance pool this managed server belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="isGeneralPurposeV2" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this is a GPv2 variant of General Purpose edition.</td>
</tr>
<tr>
    <td><CopyableCode code="keyId" /></td>
    <td><code>string</code></td>
    <td>A CMK URI of the key to use for encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses). Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Specifies maintenance configuration id to apply to this managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceCreateMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of database creation. Default: Regular instance creation. Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified. Known values are: "Default" and "PointInTimeRestore". (Default, PointInTimeRestore)</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Memory size in GB. Minimum value: 28. Maximum value: 870. Minimum and maximum value depend on the number of vCores and service tier. Read more about resource limits: `https://aka.ms/mi-resource-limits-api `_.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Minimal TLS version. Allowed values: 'None', '1.0', '1.1', '1.2'.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingModel" /></td>
    <td><code>string</code></td>
    <td>Pricing model of Managed Instance. Known values are: "Regular" and "Freemium". (Regular, Freemium)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryUserAssignedIdentityId" /></td>
    <td><code>string</code></td>
    <td>The resource id of a user assigned identity to be used by default.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of managed instance. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="proxyOverride" /></td>
    <td><code>string</code></td>
    <td>Connection type used for connecting to the instance. Known values are: "Proxy", "Redirect", and "Default". (Proxy, Redirect, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="publicDataEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the public data endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type to be used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedLogicalAvailabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the logical availability zone Managed Instance is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code>object</code></td>
    <td>The managed instance's service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Managed instance SKU. Allowed values for sku.name: GP_Gen5 (General Purpose, Standard-series); GP_G8IM (General Purpose, Premium-series); GP_G8IH (General Purpose, Premium-series memory optimized); BC_Gen5 (Business Critical, Standard-Series); BC_G8IM (Business Critical, Premium-series); BC_G8IH (Business Critical, Premium-series memory optimized).</td>
</tr>
<tr>
    <td><CopyableCode code="sourceManagedInstanceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source managed instance associated with create operation of this instance.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="storageIOps" /></td>
    <td><code>integer</code></td>
    <td>Storage IOps. Minimum value: 300. Maximum value: 80000. Increments of 1 IOps allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Storage size in GB. Minimum value: 32. Maximum value: 32768. Increments of 32 GB allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageThroughputMBps" /></td>
    <td><code>integer</code></td>
    <td>Storage throughput MBps parameter is not supported in the instance create/update operation.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet resource ID for the managed instance.</td>
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
    <td><CopyableCode code="timezoneId" /></td>
    <td><code>string</code></td>
    <td>Id of the timezone. Allowed values are timezones supported by Windows. Windows keeps details on supported timezones, including the id, in registry under KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones. You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info. List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. An example of valid timezone id is "Pacific Standard Time" or "W. Europe Standard Time".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>The number of vCores. Allowed values: 4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 128. Supported vCores depends on the selected hardware family and service tier.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualClusterId" /></td>
    <td><code>string</code></td>
    <td>Virtual cluster resource id for the Managed Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the zone-redundancy is enabled.</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password (required for managed instance creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory administrator can be utilized during instance creation and for instance updates, except for the azureADOnlyAuthentication property. To update the azureADOnlyAuthentication property, individual API must be used.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationMetadata" /></td>
    <td><code>string</code></td>
    <td>The managed instance's authentication metadata lookup mode. Known values are: "AzureAD", "Paired", and "Windows". (AzureAD, Paired, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the Managed Instance creation.</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="databaseFormat" /></td>
    <td><code>string</code></td>
    <td>Specifies the internal format of instance databases specific to the SQL engine version. Known values are: "AlwaysUpToDate", "SQLServer2022", and "SQLServer2025". (AlwaysUpToDate, SQLServer2022, SQLServer2025)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZone" /></td>
    <td><code>string</code></td>
    <td>The Dns Zone that the managed instance is in.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZonePartner" /></td>
    <td><code>string</code></td>
    <td>The resource id of another managed instance whose DNS zone this managed instance will share after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="externalGovernanceStatus" /></td>
    <td><code>string</code></td>
    <td>Status of external governance. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsage" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage. Possible values are 'Active' (default value) and 'Passive' (customer uses the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsageDetected" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage detected. Possible values are 'Active' (customer does not meet the requirements to use the secondary as Passive DR) and 'Passive' (customer meets the requirements to use the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="instancePoolId" /></td>
    <td><code>string</code></td>
    <td>The Id of the instance pool this managed server belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="isGeneralPurposeV2" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this is a GPv2 variant of General Purpose edition.</td>
</tr>
<tr>
    <td><CopyableCode code="keyId" /></td>
    <td><code>string</code></td>
    <td>A CMK URI of the key to use for encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses). Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Specifies maintenance configuration id to apply to this managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceCreateMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of database creation. Default: Regular instance creation. Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified. Known values are: "Default" and "PointInTimeRestore". (Default, PointInTimeRestore)</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Memory size in GB. Minimum value: 28. Maximum value: 870. Minimum and maximum value depend on the number of vCores and service tier. Read more about resource limits: `https://aka.ms/mi-resource-limits-api `_.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Minimal TLS version. Allowed values: 'None', '1.0', '1.1', '1.2'.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingModel" /></td>
    <td><code>string</code></td>
    <td>Pricing model of Managed Instance. Known values are: "Regular" and "Freemium". (Regular, Freemium)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryUserAssignedIdentityId" /></td>
    <td><code>string</code></td>
    <td>The resource id of a user assigned identity to be used by default.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of managed instance. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="proxyOverride" /></td>
    <td><code>string</code></td>
    <td>Connection type used for connecting to the instance. Known values are: "Proxy", "Redirect", and "Default". (Proxy, Redirect, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="publicDataEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the public data endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type to be used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedLogicalAvailabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the logical availability zone Managed Instance is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code>object</code></td>
    <td>The managed instance's service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Managed instance SKU. Allowed values for sku.name: GP_Gen5 (General Purpose, Standard-series); GP_G8IM (General Purpose, Premium-series); GP_G8IH (General Purpose, Premium-series memory optimized); BC_Gen5 (Business Critical, Standard-Series); BC_G8IM (Business Critical, Premium-series); BC_G8IH (Business Critical, Premium-series memory optimized).</td>
</tr>
<tr>
    <td><CopyableCode code="sourceManagedInstanceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source managed instance associated with create operation of this instance.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="storageIOps" /></td>
    <td><code>integer</code></td>
    <td>Storage IOps. Minimum value: 300. Maximum value: 80000. Increments of 1 IOps allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Storage size in GB. Minimum value: 32. Maximum value: 32768. Increments of 32 GB allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageThroughputMBps" /></td>
    <td><code>integer</code></td>
    <td>Storage throughput MBps parameter is not supported in the instance create/update operation.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet resource ID for the managed instance.</td>
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
    <td><CopyableCode code="timezoneId" /></td>
    <td><code>string</code></td>
    <td>Id of the timezone. Allowed values are timezones supported by Windows. Windows keeps details on supported timezones, including the id, in registry under KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones. You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info. List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. An example of valid timezone id is "Pacific Standard Time" or "W. Europe Standard Time".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>The number of vCores. Allowed values: 4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 128. Supported vCores depends on the selected hardware family and service tier.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualClusterId" /></td>
    <td><code>string</code></td>
    <td>Virtual cluster resource id for the Managed Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the zone-redundancy is enabled.</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password (required for managed instance creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory administrator can be utilized during instance creation and for instance updates, except for the azureADOnlyAuthentication property. To update the azureADOnlyAuthentication property, individual API must be used.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationMetadata" /></td>
    <td><code>string</code></td>
    <td>The managed instance's authentication metadata lookup mode. Known values are: "AzureAD", "Paired", and "Windows". (AzureAD, Paired, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the Managed Instance creation.</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="databaseFormat" /></td>
    <td><code>string</code></td>
    <td>Specifies the internal format of instance databases specific to the SQL engine version. Known values are: "AlwaysUpToDate", "SQLServer2022", and "SQLServer2025". (AlwaysUpToDate, SQLServer2022, SQLServer2025)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZone" /></td>
    <td><code>string</code></td>
    <td>The Dns Zone that the managed instance is in.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZonePartner" /></td>
    <td><code>string</code></td>
    <td>The resource id of another managed instance whose DNS zone this managed instance will share after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="externalGovernanceStatus" /></td>
    <td><code>string</code></td>
    <td>Status of external governance. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsage" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage. Possible values are 'Active' (default value) and 'Passive' (customer uses the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="hybridSecondaryUsageDetected" /></td>
    <td><code>string</code></td>
    <td>Hybrid secondary usage detected. Possible values are 'Active' (customer does not meet the requirements to use the secondary as Passive DR) and 'Passive' (customer meets the requirements to use the secondary as Passive DR). Known values are: "Active" and "Passive". (Active, Passive)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="instancePoolId" /></td>
    <td><code>string</code></td>
    <td>The Id of the instance pool this managed server belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="isGeneralPurposeV2" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this is a GPv2 variant of General Purpose edition.</td>
</tr>
<tr>
    <td><CopyableCode code="keyId" /></td>
    <td><code>string</code></td>
    <td>A CMK URI of the key to use for encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses). Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Specifies maintenance configuration id to apply to this managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceCreateMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of database creation. Default: Regular instance creation. Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified. Known values are: "Default" and "PointInTimeRestore". (Default, PointInTimeRestore)</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Memory size in GB. Minimum value: 28. Maximum value: 870. Minimum and maximum value depend on the number of vCores and service tier. Read more about resource limits: `https://aka.ms/mi-resource-limits-api `_.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Minimal TLS version. Allowed values: 'None', '1.0', '1.1', '1.2'.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingModel" /></td>
    <td><code>string</code></td>
    <td>Pricing model of Managed Instance. Known values are: "Regular" and "Freemium". (Regular, Freemium)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryUserAssignedIdentityId" /></td>
    <td><code>string</code></td>
    <td>The resource id of a user assigned identity to be used by default.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of managed instance. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="proxyOverride" /></td>
    <td><code>string</code></td>
    <td>Connection type used for connecting to the instance. Known values are: "Proxy", "Redirect", and "Default". (Proxy, Redirect, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="publicDataEndpointEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the public data endpoint is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type to be used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage). Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedLogicalAvailabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the logical availability zone Managed Instance is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code>object</code></td>
    <td>The managed instance's service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Managed instance SKU. Allowed values for sku.name: GP_Gen5 (General Purpose, Standard-series); GP_G8IM (General Purpose, Premium-series); GP_G8IH (General Purpose, Premium-series memory optimized); BC_Gen5 (Business Critical, Standard-Series); BC_G8IM (Business Critical, Premium-series); BC_G8IH (Business Critical, Premium-series memory optimized).</td>
</tr>
<tr>
    <td><CopyableCode code="sourceManagedInstanceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source managed instance associated with create operation of this instance.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the managed instance.</td>
</tr>
<tr>
    <td><CopyableCode code="storageIOps" /></td>
    <td><code>integer</code></td>
    <td>Storage IOps. Minimum value: 300. Maximum value: 80000. Increments of 1 IOps allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSizeInGB" /></td>
    <td><code>integer</code></td>
    <td>Storage size in GB. Minimum value: 32. Maximum value: 32768. Increments of 32 GB allowed only. Maximum value depends on the selected hardware family and number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="storageThroughputMBps" /></td>
    <td><code>integer</code></td>
    <td>Storage throughput MBps parameter is not supported in the instance create/update operation.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet resource ID for the managed instance.</td>
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
    <td><CopyableCode code="timezoneId" /></td>
    <td><code>string</code></td>
    <td>Id of the timezone. Allowed values are timezones supported by Windows. Windows keeps details on supported timezones, including the id, in registry under KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones. You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info. List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. An example of valid timezone id is "Pacific Standard Time" or "W. Europe Standard Time".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>The number of vCores. Allowed values: 4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 128. Supported vCores depends on the selected hardware family and service tier.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualClusterId" /></td>
    <td><code>string</code></td>
    <td>Virtual cluster resource id for the Managed Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the zone-redundancy is enabled.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a managed instance.</td>
</tr>
<tr>
    <td><a href="#list_by_instance_pool"><CopyableCode code="list_by_instance_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_pool_name"><code>instance_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a list of all managed instances in an instance pool.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a list of managed instances in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a list of all managed instances in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a managed instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a managed instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a managed instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a managed instance.</td>
</tr>
<tr>
    <td><a href="#list_by_managed_instance"><CopyableCode code="list_by_managed_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-numberOfQueries"><code>numberOfQueries</code></a>, <a href="#parameter-databases"><code>databases</code></a>, <a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-aggregationFunction"><code>aggregationFunction</code></a>, <a href="#parameter-observationMetric"><code>observationMetric</code></a></td>
    <td>Get top resource consuming queries of a managed instance.</td>
</tr>
<tr>
    <td><a href="#list_outbound_network_dependencies_by_managed_instance"><CopyableCode code="list_outbound_network_dependencies_by_managed_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the collection of outbound network dependencies for the given managed instance.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-replicaType"><code>replicaType</code></a></td>
    <td>Failovers a managed instance.</td>
</tr>
<tr>
    <td><a href="#reevaluate_inaccessible_database_state"><CopyableCode code="reevaluate_inaccessible_database_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reevaluates the inaccessibility state of all managed databases.</td>
</tr>
<tr>
    <td><a href="#refresh_status"><CopyableCode code="refresh_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refresh external governance enablement status.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts the managed instance.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops the managed instance.</td>
</tr>
<tr>
    <td><a href="#validate_azure_key_vault_encryption_key"><CopyableCode code="validate_azure_key_vault_encryption_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-tdeKeyUri"><code>tdeKeyUri</code></a></td>
    <td></td>
    <td>Validates customer managed key.</td>
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
<tr id="parameter-instance_pool_name">
    <td><CopyableCode code="instance_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the instance pool to be retrieved. Required.</td>
</tr>
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
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
    <td>The child resources to include in the response. Default value is None.</td>
</tr>
<tr id="parameter-aggregationFunction">
    <td><CopyableCode code="aggregationFunction" /></td>
    <td><code>string</code></td>
    <td>Aggregation function to be used, default value is 'sum'. Known values are: "avg", "min", "max", "stdev", and "sum". Default value is None.</td>
</tr>
<tr id="parameter-databases">
    <td><CopyableCode code="databases" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of databases to be included into search. All DB's are included if this parameter is not specified. Default value is None.</td>
</tr>
<tr id="parameter-endTime">
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>End time for observed period. Default value is None.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The time step to be used to summarize the metric values. Default value is PT1H. Known values are: "PT1H" and "P1D". Default value is None.</td>
</tr>
<tr id="parameter-numberOfQueries">
    <td><CopyableCode code="numberOfQueries" /></td>
    <td><code>integer</code></td>
    <td>How many 'top queries' to return. Default is 5. Default value is None.</td>
</tr>
<tr id="parameter-observationMetric">
    <td><CopyableCode code="observationMetric" /></td>
    <td><code>string</code></td>
    <td>Metric to be used for ranking top queries. Default is 'cpu'. Known values are: "cpu", "io", "logIo", "duration", and "dtu". Default value is None.</td>
</tr>
<tr id="parameter-replicaType">
    <td><CopyableCode code="replicaType" /></td>
    <td><code>string</code></td>
    <td>The type of replica to be failed over. Known values are: "Primary" and "ReadableSecondary". Default value is None.</td>
</tr>
<tr id="parameter-startTime">
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>Start time for observed period. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_instance_pool', value: 'list_by_instance_pool' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a managed instance.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
administrators,
authenticationMetadata,
collation,
createTime,
currentBackupStorageRedundancy,
databaseFormat,
dnsZone,
dnsZonePartner,
externalGovernanceStatus,
fullyQualifiedDomainName,
hybridSecondaryUsage,
hybridSecondaryUsageDetected,
identity,
instancePoolId,
isGeneralPurposeV2,
keyId,
licenseType,
location,
maintenanceConfigurationId,
managedInstanceCreateMode,
memorySizeInGB,
minimalTlsVersion,
pricingModel,
primaryUserAssignedIdentityId,
privateEndpointConnections,
provisioningState,
proxyOverride,
publicDataEndpointEnabled,
requestedBackupStorageRedundancy,
requestedLogicalAvailabilityZone,
restorePointInTime,
servicePrincipal,
sku,
sourceManagedInstanceId,
state,
storageIOps,
storageSizeInGB,
storageThroughputMBps,
subnetId,
systemData,
tags,
timezoneId,
type,
vCores,
virtualClusterId,
zoneRedundant
FROM azure.sql.managed_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_instance_pool">

Gets a list of all managed instances in an instance pool.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
administrators,
authenticationMetadata,
collation,
createTime,
currentBackupStorageRedundancy,
databaseFormat,
dnsZone,
dnsZonePartner,
externalGovernanceStatus,
fullyQualifiedDomainName,
hybridSecondaryUsage,
hybridSecondaryUsageDetected,
identity,
instancePoolId,
isGeneralPurposeV2,
keyId,
licenseType,
location,
maintenanceConfigurationId,
managedInstanceCreateMode,
memorySizeInGB,
minimalTlsVersion,
pricingModel,
primaryUserAssignedIdentityId,
privateEndpointConnections,
provisioningState,
proxyOverride,
publicDataEndpointEnabled,
requestedBackupStorageRedundancy,
requestedLogicalAvailabilityZone,
restorePointInTime,
servicePrincipal,
sku,
sourceManagedInstanceId,
state,
storageIOps,
storageSizeInGB,
storageThroughputMBps,
subnetId,
systemData,
tags,
timezoneId,
type,
vCores,
virtualClusterId,
zoneRedundant
FROM azure.sql.managed_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_pool_name = '{{ instance_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of managed instances in a resource group.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
administrators,
authenticationMetadata,
collation,
createTime,
currentBackupStorageRedundancy,
databaseFormat,
dnsZone,
dnsZonePartner,
externalGovernanceStatus,
fullyQualifiedDomainName,
hybridSecondaryUsage,
hybridSecondaryUsageDetected,
identity,
instancePoolId,
isGeneralPurposeV2,
keyId,
licenseType,
location,
maintenanceConfigurationId,
managedInstanceCreateMode,
memorySizeInGB,
minimalTlsVersion,
pricingModel,
primaryUserAssignedIdentityId,
privateEndpointConnections,
provisioningState,
proxyOverride,
publicDataEndpointEnabled,
requestedBackupStorageRedundancy,
requestedLogicalAvailabilityZone,
restorePointInTime,
servicePrincipal,
sku,
sourceManagedInstanceId,
state,
storageIOps,
storageSizeInGB,
storageThroughputMBps,
subnetId,
systemData,
tags,
timezoneId,
type,
vCores,
virtualClusterId,
zoneRedundant
FROM azure.sql.managed_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of all managed instances in the subscription.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
administrators,
authenticationMetadata,
collation,
createTime,
currentBackupStorageRedundancy,
databaseFormat,
dnsZone,
dnsZonePartner,
externalGovernanceStatus,
fullyQualifiedDomainName,
hybridSecondaryUsage,
hybridSecondaryUsageDetected,
identity,
instancePoolId,
isGeneralPurposeV2,
keyId,
licenseType,
location,
maintenanceConfigurationId,
managedInstanceCreateMode,
memorySizeInGB,
minimalTlsVersion,
pricingModel,
primaryUserAssignedIdentityId,
privateEndpointConnections,
provisioningState,
proxyOverride,
publicDataEndpointEnabled,
requestedBackupStorageRedundancy,
requestedLogicalAvailabilityZone,
restorePointInTime,
servicePrincipal,
sku,
sourceManagedInstanceId,
state,
storageIOps,
storageSizeInGB,
storageThroughputMBps,
subnetId,
systemData,
tags,
timezoneId,
type,
vCores,
virtualClusterId,
zoneRedundant
FROM azure.sql.managed_instances
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
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

Creates or updates a managed instance.

```sql
INSERT INTO azure.sql.managed_instances (
tags,
location,
properties,
identity,
sku,
resource_group_name,
managed_instance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ managed_instance_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
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
- name: managed_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_instances resource.
    - name: managed_instance_name
      value: "{{ managed_instance_name }}"
      description: Required parameter for the managed_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_instances resource.
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
        Resource properties.
      value:
        provisioningState: "{{ provisioningState }}"
        managedInstanceCreateMode: "{{ managedInstanceCreateMode }}"
        fullyQualifiedDomainName: "{{ fullyQualifiedDomainName }}"
        isGeneralPurposeV2: {{ isGeneralPurposeV2 }}
        administratorLogin: "{{ administratorLogin }}"
        administratorLoginPassword: "{{ administratorLoginPassword }}"
        subnetId: "{{ subnetId }}"
        state: "{{ state }}"
        licenseType: "{{ licenseType }}"
        hybridSecondaryUsage: "{{ hybridSecondaryUsage }}"
        hybridSecondaryUsageDetected: "{{ hybridSecondaryUsageDetected }}"
        vCores: {{ vCores }}
        storageSizeInGB: {{ storageSizeInGB }}
        storageIOps: {{ storageIOps }}
        storageThroughputMBps: {{ storageThroughputMBps }}
        memorySizeInGB: {{ memorySizeInGB }}
        collation: "{{ collation }}"
        dnsZone: "{{ dnsZone }}"
        dnsZonePartner: "{{ dnsZonePartner }}"
        publicDataEndpointEnabled: {{ publicDataEndpointEnabled }}
        sourceManagedInstanceId: "{{ sourceManagedInstanceId }}"
        restorePointInTime: "{{ restorePointInTime }}"
        proxyOverride: "{{ proxyOverride }}"
        timezoneId: "{{ timezoneId }}"
        instancePoolId: "{{ instancePoolId }}"
        maintenanceConfigurationId: "{{ maintenanceConfigurationId }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        minimalTlsVersion: "{{ minimalTlsVersion }}"
        currentBackupStorageRedundancy: "{{ currentBackupStorageRedundancy }}"
        requestedBackupStorageRedundancy: "{{ requestedBackupStorageRedundancy }}"
        zoneRedundant: {{ zoneRedundant }}
        primaryUserAssignedIdentityId: "{{ primaryUserAssignedIdentityId }}"
        keyId: "{{ keyId }}"
        administrators:
          administratorType: "{{ administratorType }}"
          principalType: "{{ principalType }}"
          login: "{{ login }}"
          sid: "{{ sid }}"
          tenantId: "{{ tenantId }}"
          azureADOnlyAuthentication: {{ azureADOnlyAuthentication }}
        servicePrincipal:
          principalId: "{{ principalId }}"
          clientId: "{{ clientId }}"
          tenantId: "{{ tenantId }}"
          type: "{{ type }}"
        virtualClusterId: "{{ virtualClusterId }}"
        externalGovernanceStatus: "{{ externalGovernanceStatus }}"
        pricingModel: "{{ pricingModel }}"
        createTime: "{{ createTime }}"
        authenticationMetadata: "{{ authenticationMetadata }}"
        databaseFormat: "{{ databaseFormat }}"
        requestedLogicalAvailabilityZone: "{{ requestedLogicalAvailabilityZone }}"
    - name: identity
      description: |
        The Azure Active Directory identity of the managed instance.
      value:
        userAssignedIdentities: "{{ userAssignedIdentities }}"
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
    - name: sku
      description: |
        Managed instance SKU. Allowed values for sku.name: GP_Gen5 (General Purpose, Standard-series); GP_G8IM (General Purpose, Premium-series); GP_G8IH (General Purpose, Premium-series memory optimized); BC_Gen5 (Business Critical, Standard-Series); BC_G8IM (Business Critical, Premium-series); BC_G8IH (Business Critical, Premium-series memory optimized).
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
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

Updates a managed instance.

```sql
UPDATE azure.sql.managed_instances
SET 
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
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

Creates or updates a managed instance.

```sql
REPLACE azure.sql.managed_instances
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
location,
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

Deletes a managed instance.

```sql
DELETE FROM azure.sql.managed_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_managed_instance"
    values={[
        { label: 'list_by_managed_instance', value: 'list_by_managed_instance' },
        { label: 'list_outbound_network_dependencies_by_managed_instance', value: 'list_outbound_network_dependencies_by_managed_instance' },
        { label: 'failover', value: 'failover' },
        { label: 'reevaluate_inaccessible_database_state', value: 'reevaluate_inaccessible_database_state' },
        { label: 'refresh_status', value: 'refresh_status' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'validate_azure_key_vault_encryption_key', value: 'validate_azure_key_vault_encryption_key' }
    ]}
>
<TabItem value="list_by_managed_instance">

Get top resource consuming queries of a managed instance.

```sql
EXEC azure.sql.managed_instances.list_by_managed_instance 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@numberOfQueries='{{ numberOfQueries }}', 
@databases='{{ databases }}', 
@startTime='{{ startTime }}', 
@endTime='{{ endTime }}', 
@interval='{{ interval }}', 
@aggregationFunction='{{ aggregationFunction }}', 
@observationMetric='{{ observationMetric }}'
;
```
</TabItem>
<TabItem value="list_outbound_network_dependencies_by_managed_instance">

Gets the collection of outbound network dependencies for the given managed instance.

```sql
EXEC azure.sql.managed_instances.list_outbound_network_dependencies_by_managed_instance 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="failover">

Failovers a managed instance.

```sql
EXEC azure.sql.managed_instances.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@replicaType='{{ replicaType }}'
;
```
</TabItem>
<TabItem value="reevaluate_inaccessible_database_state">

Reevaluates the inaccessibility state of all managed databases.

```sql
EXEC azure.sql.managed_instances.reevaluate_inaccessible_database_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="refresh_status">

Refresh external governance enablement status.

```sql
EXEC azure.sql.managed_instances.refresh_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts the managed instance.

```sql
EXEC azure.sql.managed_instances.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops the managed instance.

```sql
EXEC azure.sql.managed_instances.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_azure_key_vault_encryption_key">

Validates customer managed key.

```sql
EXEC azure.sql.managed_instances.validate_azure_key_vault_encryption_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tdeKeyUri": "{{ tdeKeyUri }}"
}'
;
```
</TabItem>
</Tabs>
