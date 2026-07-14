--- 
title: redis
hide_title: false
hide_table_of_contents: false
keywords:
  - redis
  - redis
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

Creates, updates, deletes, gets or lists a <code>redis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="redis" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.redis.redis" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_upgrade_notifications"
    values={[
        { label: 'list_upgrade_notifications', value: 'list_upgrade_notifications' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_upgrade_notifications">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of upgrade notification.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when upgrade notification occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="upsellNotification" /></td>
    <td><code>object</code></td>
    <td>Details about this upgrade notification.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="accessKeys" /></td>
    <td><code>object</code></td>
    <td>The keys of the Redis cache - not set if this object is not the response to Create or Update redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="disableAccessKeyAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>Authentication to Redis through access keys is disabled when set as true. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNonSslPort" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the non-ssl Redis server port (6379) is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>Redis host name.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>List of the Redis instances associated with the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedServers" /></td>
    <td><code>array</code></td>
    <td>List of the linked servers associated with the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, '1.0', '1.1', '1.2'). Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Redis non-SSL port.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Redis instance provisioning status. Known values are: "Creating", "Deleting", "Disabled", "Failed", "Linking", "Provisioning", "RecoveringScaleFailure", "Scaling", "Succeeded", "Unlinking", "Unprovisioning", "Updating", "ConfiguringAAD", "Migrating", "MigrationFailed", "MigrationSucceeded", "MigrationCancelling", and "MigrationCancellationFailed". (Creating, Deleting, Disabled, Failed, Linking, Provisioning, RecoveringScaleFailure, Scaling, Succeeded, Unlinking, Unprovisioning, Updating, ConfiguringAAD, Migrating, MigrationFailed, MigrationSucceeded, MigrationCancelling, MigrationCancellationFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this cache. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints are the exclusive access method. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redisConfiguration" /></td>
    <td><code>object</code></td>
    <td>All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta, maxmemory-policy,notify-keyspace-events, aof-backup-enabled, aof-storage-connection-string-0, aof-storage-connection-string-1 etc.</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Redis version. This should be in the form 'major[.minor]' (only 'major' is required) or the value 'latest' which refers to the latest stable Redis version that is available. Supported versions: 4.0, 6.0 (latest). Default value is 'latest'.</td>
</tr>
<tr>
    <td><CopyableCode code="replicasPerMaster" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas to be created per primary.</td>
</tr>
<tr>
    <td><CopyableCode code="replicasPerPrimary" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas to be created per primary.</td>
</tr>
<tr>
    <td><CopyableCode code="shardCount" /></td>
    <td><code>integer</code></td>
    <td>The number of shards to be created on a Premium Cluster Cache.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the Redis cache to deploy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sslPort" /></td>
    <td><code>integer</code></td>
    <td>Redis SSL port.</td>
</tr>
<tr>
    <td><CopyableCode code="staticIP" /></td>
    <td><code>string</code></td>
    <td>Static IP address. Optionally, may be specified when deploying a Redis cache inside an existing Azure Virtual Network; auto assigned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/Microsoft.&#123;Network|ClassicNetwork&#125;/VirtualNetworks/vnet1/subnets/subnet1.</td>
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
    <td><CopyableCode code="targetAmrResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the target Azure Managed Redis resource that this Azure Cache for Redis resource is being migrated to.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantSettings" /></td>
    <td><code>object</code></td>
    <td>A dictionary of tenant settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateChannel" /></td>
    <td><code>string</code></td>
    <td>Optional: Specifies the update channel for the monthly Redis updates your Redis Cache will receive. Caches using 'Preview' update channel get latest Redis updates at least 4 weeks ahead of 'Stable' channel caches. Default value is 'Stable'. Known values are: "Stable" and "Preview". (Stable, Preview)</td>
</tr>
<tr>
    <td><CopyableCode code="zonalAllocationPolicy" /></td>
    <td><code>string</code></td>
    <td>Optional: Specifies how availability zones are allocated to the Redis cache. 'Automatic' enables zone redundancy and Azure will automatically select zones based on regional availability and capacity. 'UserDefined' will select availability zones passed in by you using the 'zones' parameter. 'NoZones' will produce a non-zonal cache. If 'zonalAllocationPolicy' is not passed, it will be set to 'UserDefined' when zones are passed in, otherwise, it will be set to 'Automatic' in regions where zones are supported and 'NoZones' in regions where zones are not supported. Known values are: "Automatic", "UserDefined", and "NoZones". (Automatic, UserDefined, NoZones)</td>
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
    <td><CopyableCode code="accessKeys" /></td>
    <td><code>object</code></td>
    <td>The keys of the Redis cache - not set if this object is not the response to Create or Update redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="disableAccessKeyAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>Authentication to Redis through access keys is disabled when set as true. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNonSslPort" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the non-ssl Redis server port (6379) is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>Redis host name.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>List of the Redis instances associated with the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedServers" /></td>
    <td><code>array</code></td>
    <td>List of the linked servers associated with the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, '1.0', '1.1', '1.2'). Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Redis non-SSL port.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Redis instance provisioning status. Known values are: "Creating", "Deleting", "Disabled", "Failed", "Linking", "Provisioning", "RecoveringScaleFailure", "Scaling", "Succeeded", "Unlinking", "Unprovisioning", "Updating", "ConfiguringAAD", "Migrating", "MigrationFailed", "MigrationSucceeded", "MigrationCancelling", and "MigrationCancellationFailed". (Creating, Deleting, Disabled, Failed, Linking, Provisioning, RecoveringScaleFailure, Scaling, Succeeded, Unlinking, Unprovisioning, Updating, ConfiguringAAD, Migrating, MigrationFailed, MigrationSucceeded, MigrationCancelling, MigrationCancellationFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this cache. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints are the exclusive access method. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redisConfiguration" /></td>
    <td><code>object</code></td>
    <td>All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta, maxmemory-policy,notify-keyspace-events, aof-backup-enabled, aof-storage-connection-string-0, aof-storage-connection-string-1 etc.</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Redis version. This should be in the form 'major[.minor]' (only 'major' is required) or the value 'latest' which refers to the latest stable Redis version that is available. Supported versions: 4.0, 6.0 (latest). Default value is 'latest'.</td>
</tr>
<tr>
    <td><CopyableCode code="replicasPerMaster" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas to be created per primary.</td>
</tr>
<tr>
    <td><CopyableCode code="replicasPerPrimary" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas to be created per primary.</td>
</tr>
<tr>
    <td><CopyableCode code="shardCount" /></td>
    <td><code>integer</code></td>
    <td>The number of shards to be created on a Premium Cluster Cache.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the Redis cache to deploy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sslPort" /></td>
    <td><code>integer</code></td>
    <td>Redis SSL port.</td>
</tr>
<tr>
    <td><CopyableCode code="staticIP" /></td>
    <td><code>string</code></td>
    <td>Static IP address. Optionally, may be specified when deploying a Redis cache inside an existing Azure Virtual Network; auto assigned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/Microsoft.&#123;Network|ClassicNetwork&#125;/VirtualNetworks/vnet1/subnets/subnet1.</td>
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
    <td><CopyableCode code="targetAmrResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the target Azure Managed Redis resource that this Azure Cache for Redis resource is being migrated to.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantSettings" /></td>
    <td><code>object</code></td>
    <td>A dictionary of tenant settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateChannel" /></td>
    <td><code>string</code></td>
    <td>Optional: Specifies the update channel for the monthly Redis updates your Redis Cache will receive. Caches using 'Preview' update channel get latest Redis updates at least 4 weeks ahead of 'Stable' channel caches. Default value is 'Stable'. Known values are: "Stable" and "Preview". (Stable, Preview)</td>
</tr>
<tr>
    <td><CopyableCode code="zonalAllocationPolicy" /></td>
    <td><code>string</code></td>
    <td>Optional: Specifies how availability zones are allocated to the Redis cache. 'Automatic' enables zone redundancy and Azure will automatically select zones based on regional availability and capacity. 'UserDefined' will select availability zones passed in by you using the 'zones' parameter. 'NoZones' will produce a non-zonal cache. If 'zonalAllocationPolicy' is not passed, it will be set to 'UserDefined' when zones are passed in, otherwise, it will be set to 'Automatic' in regions where zones are supported and 'NoZones' in regions where zones are not supported. Known values are: "Automatic", "UserDefined", and "NoZones". (Automatic, UserDefined, NoZones)</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="accessKeys" /></td>
    <td><code>object</code></td>
    <td>The keys of the Redis cache - not set if this object is not the response to Create or Update redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="disableAccessKeyAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>Authentication to Redis through access keys is disabled when set as true. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNonSslPort" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the non-ssl Redis server port (6379) is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>Redis host name.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>List of the Redis instances associated with the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedServers" /></td>
    <td><code>array</code></td>
    <td>List of the linked servers associated with the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, '1.0', '1.1', '1.2'). Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Redis non-SSL port.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection associated with the specified redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Redis instance provisioning status. Known values are: "Creating", "Deleting", "Disabled", "Failed", "Linking", "Provisioning", "RecoveringScaleFailure", "Scaling", "Succeeded", "Unlinking", "Unprovisioning", "Updating", "ConfiguringAAD", "Migrating", "MigrationFailed", "MigrationSucceeded", "MigrationCancelling", and "MigrationCancellationFailed". (Creating, Deleting, Disabled, Failed, Linking, Provisioning, RecoveringScaleFailure, Scaling, Succeeded, Unlinking, Unprovisioning, Updating, ConfiguringAAD, Migrating, MigrationFailed, MigrationSucceeded, MigrationCancelling, MigrationCancellationFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this cache. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints are the exclusive access method. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redisConfiguration" /></td>
    <td><code>object</code></td>
    <td>All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta, maxmemory-policy,notify-keyspace-events, aof-backup-enabled, aof-storage-connection-string-0, aof-storage-connection-string-1 etc.</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Redis version. This should be in the form 'major[.minor]' (only 'major' is required) or the value 'latest' which refers to the latest stable Redis version that is available. Supported versions: 4.0, 6.0 (latest). Default value is 'latest'.</td>
</tr>
<tr>
    <td><CopyableCode code="replicasPerMaster" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas to be created per primary.</td>
</tr>
<tr>
    <td><CopyableCode code="replicasPerPrimary" /></td>
    <td><code>integer</code></td>
    <td>The number of replicas to be created per primary.</td>
</tr>
<tr>
    <td><CopyableCode code="shardCount" /></td>
    <td><code>integer</code></td>
    <td>The number of shards to be created on a Premium Cluster Cache.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the Redis cache to deploy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sslPort" /></td>
    <td><code>integer</code></td>
    <td>Redis SSL port.</td>
</tr>
<tr>
    <td><CopyableCode code="staticIP" /></td>
    <td><code>string</code></td>
    <td>Static IP address. Optionally, may be specified when deploying a Redis cache inside an existing Azure Virtual Network; auto assigned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/Microsoft.&#123;Network|ClassicNetwork&#125;/VirtualNetworks/vnet1/subnets/subnet1.</td>
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
    <td><CopyableCode code="targetAmrResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the target Azure Managed Redis resource that this Azure Cache for Redis resource is being migrated to.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantSettings" /></td>
    <td><code>object</code></td>
    <td>A dictionary of tenant settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateChannel" /></td>
    <td><code>string</code></td>
    <td>Optional: Specifies the update channel for the monthly Redis updates your Redis Cache will receive. Caches using 'Preview' update channel get latest Redis updates at least 4 weeks ahead of 'Stable' channel caches. Default value is 'Stable'. Known values are: "Stable" and "Preview". (Stable, Preview)</td>
</tr>
<tr>
    <td><CopyableCode code="zonalAllocationPolicy" /></td>
    <td><code>string</code></td>
    <td>Optional: Specifies how availability zones are allocated to the Redis cache. 'Automatic' enables zone redundancy and Azure will automatically select zones based on regional availability and capacity. 'UserDefined' will select availability zones passed in by you using the 'zones' parameter. 'NoZones' will produce a non-zonal cache. If 'zonalAllocationPolicy' is not passed, it will be set to 'UserDefined' when zones are passed in, otherwise, it will be set to 'Automatic' in regions where zones are supported and 'NoZones' in regions where zones are not supported. Known values are: "Automatic", "UserDefined", and "NoZones". (Automatic, UserDefined, NoZones)</td>
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
    <td><a href="#list_upgrade_notifications"><CopyableCode code="list_upgrade_notifications" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-history"><code>history</code></a></td>
    <td></td>
    <td>[Deprecated] Gets any upgrade notifications for a Redis cache.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Redis cache (resource description).</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Redis caches in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all Redis caches in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing Redis cache.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Redis cache.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a Redis cache's access keys. This operation requires write permission to the cache resource.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyType"><code>keyType</code></a></td>
    <td></td>
    <td>Regenerate Redis cache's access keys. This operation requires write permission to the cache resource.</td>
</tr>
<tr>
    <td><a href="#force_reboot"><CopyableCode code="force_reboot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss.</td>
</tr>
<tr>
    <td><a href="#import_data"><CopyableCode code="import_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-files"><code>files</code></a></td>
    <td></td>
    <td>Import data into Redis cache.</td>
</tr>
<tr>
    <td><a href="#export_data"><CopyableCode code="export_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-container"><code>container</code></a></td>
    <td></td>
    <td>Export data from the redis cache to blobs in a container.</td>
</tr>
<tr>
    <td><a href="#flush_cache"><CopyableCode code="flush_cache" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes all of the keys in a cache.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Checks that the redis cache name is valid and is not already in use.</td>
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
<tr id="parameter-cache_name">
    <td><CopyableCode code="cache_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Redis cache. Required.</td>
</tr>
<tr id="parameter-history">
    <td><CopyableCode code="history" /></td>
    <td><code>number</code></td>
    <td>how many minutes in past to look for upgrade notifications. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the RedisResource. Required.</td>
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
    defaultValue="list_upgrade_notifications"
    values={[
        { label: 'list_upgrade_notifications', value: 'list_upgrade_notifications' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_upgrade_notifications">

[Deprecated] Gets any upgrade notifications for a Redis cache.

```sql
SELECT
name,
timestamp,
upsellNotification
FROM azure.redis.redis
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND history = '{{ history }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a Redis cache (resource description).

```sql
SELECT
id,
name,
accessKeys,
disableAccessKeyAuthentication,
enableNonSslPort,
hostName,
identity,
instances,
linkedServers,
location,
minimumTlsVersion,
port,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
redisConfiguration,
redisVersion,
replicasPerMaster,
replicasPerPrimary,
shardCount,
sku,
sslPort,
staticIP,
subnetId,
systemData,
tags,
targetAmrResourceId,
tenantSettings,
type,
updateChannel,
zonalAllocationPolicy,
zones
FROM azure.redis.redis
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all Redis caches in a resource group.

```sql
SELECT
id,
name,
accessKeys,
disableAccessKeyAuthentication,
enableNonSslPort,
hostName,
identity,
instances,
linkedServers,
location,
minimumTlsVersion,
port,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
redisConfiguration,
redisVersion,
replicasPerMaster,
replicasPerPrimary,
shardCount,
sku,
sslPort,
staticIP,
subnetId,
systemData,
tags,
targetAmrResourceId,
tenantSettings,
type,
updateChannel,
zonalAllocationPolicy,
zones
FROM azure.redis.redis
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all Redis caches in the specified subscription.

```sql
SELECT
id,
name,
accessKeys,
disableAccessKeyAuthentication,
enableNonSslPort,
hostName,
identity,
instances,
linkedServers,
location,
minimumTlsVersion,
port,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
redisConfiguration,
redisVersion,
replicasPerMaster,
replicasPerPrimary,
shardCount,
sku,
sslPort,
staticIP,
subnetId,
systemData,
tags,
targetAmrResourceId,
tenantSettings,
type,
updateChannel,
zonalAllocationPolicy,
zones
FROM azure.redis.redis
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

Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache.

```sql
INSERT INTO azure.redis.redis (
properties,
zones,
location,
tags,
identity,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ zones }}',
'{{ location }}' /* required */,
'{{ tags }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: redis
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the redis resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the redis resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the redis resource.
    - name: properties
      description: |
        Redis cache properties. Required.
      value:
        redisConfiguration:
          rdb-backup-enabled: "{{ rdb-backup-enabled }}"
          rdb-backup-frequency: "{{ rdb-backup-frequency }}"
          rdb-backup-max-snapshot-count: "{{ rdb-backup-max-snapshot-count }}"
          rdb-storage-connection-string: "{{ rdb-storage-connection-string }}"
          aof-backup-enabled: "{{ aof-backup-enabled }}"
          aof-storage-connection-string-0: "{{ aof-storage-connection-string-0 }}"
          aof-storage-connection-string-1: "{{ aof-storage-connection-string-1 }}"
          maxfragmentationmemory-reserved: "{{ maxfragmentationmemory-reserved }}"
          maxmemory-policy: "{{ maxmemory-policy }}"
          maxmemory-reserved: "{{ maxmemory-reserved }}"
          maxmemory-delta: "{{ maxmemory-delta }}"
          maxclients: "{{ maxclients }}"
          notify-keyspace-events: "{{ notify-keyspace-events }}"
          preferred-data-archive-auth-method: "{{ preferred-data-archive-auth-method }}"
          preferred-data-persistence-auth-method: "{{ preferred-data-persistence-auth-method }}"
          zonal-configuration: "{{ zonal-configuration }}"
          authnotrequired: "{{ authnotrequired }}"
          storage-subscription-id: "{{ storage-subscription-id }}"
          aad-enabled: "{{ aad-enabled }}"
        redisVersion: "{{ redisVersion }}"
        enableNonSslPort: {{ enableNonSslPort }}
        replicasPerMaster: {{ replicasPerMaster }}
        replicasPerPrimary: {{ replicasPerPrimary }}
        tenantSettings: "{{ tenantSettings }}"
        shardCount: {{ shardCount }}
        minimumTlsVersion: "{{ minimumTlsVersion }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        updateChannel: "{{ updateChannel }}"
        disableAccessKeyAuthentication: {{ disableAccessKeyAuthentication }}
        zonalAllocationPolicy: "{{ zonalAllocationPolicy }}"
        sku:
          name: "{{ name }}"
          family: "{{ family }}"
          capacity: {{ capacity }}
        subnetId: "{{ subnetId }}"
        staticIP: "{{ staticIP }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting where the resource needs to come from.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: identity
      description: |
        The identity of the resource.
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

Update an existing Redis cache.

```sql
UPDATE azure.redis.redis
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
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

Deletes a Redis cache.

```sql
DELETE FROM azure.redis.redis
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'force_reboot', value: 'force_reboot' },
        { label: 'import_data', value: 'import_data' },
        { label: 'export_data', value: 'export_data' },
        { label: 'flush_cache', value: 'flush_cache' },
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="list_keys">

Retrieve a Redis cache's access keys. This operation requires write permission to the cache resource.

```sql
EXEC azure.redis.redis.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerate Redis cache's access keys. This operation requires write permission to the cache resource.

```sql
EXEC azure.redis.redis.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyType": "{{ keyType }}"
}'
;
```
</TabItem>
<TabItem value="force_reboot">

Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss.

```sql
EXEC azure.redis.redis.force_reboot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"rebootType": "{{ rebootType }}", 
"shardId": {{ shardId }}, 
"ports": "{{ ports }}"
}'
;
```
</TabItem>
<TabItem value="import_data">

Import data into Redis cache.

```sql
EXEC azure.redis.redis.import_data 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"format": "{{ format }}", 
"files": "{{ files }}", 
"preferred-data-archive-auth-method": "{{ preferred-data-archive-auth-method }}", 
"storage-subscription-id": "{{ storage-subscription-id }}"
}'
;
```
</TabItem>
<TabItem value="export_data">

Export data from the redis cache to blobs in a container.

```sql
EXEC azure.redis.redis.export_data 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"format": "{{ format }}", 
"prefix": "{{ prefix }}", 
"container": "{{ container }}", 
"preferred-data-archive-auth-method": "{{ preferred-data-archive-auth-method }}", 
"storage-subscription-id": "{{ storage-subscription-id }}"
}'
;
```
</TabItem>
<TabItem value="flush_cache">

Deletes all of the keys in a cache.

```sql
EXEC azure.redis.redis.flush_cache 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks that the redis cache name is valid and is not already in use.

```sql
EXEC azure.redis.redis.check_name_availability 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
