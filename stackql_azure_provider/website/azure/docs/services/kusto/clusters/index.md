--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - kusto
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kusto.clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name that was checked.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Message indicating an unavailable name due to a conflict, or a description of the naming rules that are violated.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Specifies a Boolean value that indicates if the name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Message providing the reason why the given name is invalid. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
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
    <td><CopyableCode code="acceptedAudiences" /></td>
    <td><code>array</code></td>
    <td>The cluster's accepted audiences.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>List of allowed FQDNs(Fully Qualified Domain Name) for egress from Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedIpRangeList" /></td>
    <td><code>array</code></td>
    <td>The list of ips in the format of CIDR allowed to connect to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="calloutPolicies" /></td>
    <td><code>array</code></td>
    <td>List of callout policies for egress from Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="dataIngestionUri" /></td>
    <td><code>string</code></td>
    <td>The cluster data ingestion URI.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoStop" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the cluster could be automatically stopped (due to lack of data or no activity for many days).</td>
</tr>
<tr>
    <td><CopyableCode code="enableDiskEncryption" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the cluster's disks are encrypted.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDoubleEncryption" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if double encryption is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurge" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the purge operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableStreamingIngest" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the streaming ingest is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="engineType" /></td>
    <td><code>string</code></td>
    <td>The engine type. Known values are: "V2" and "V3". (V2, V3)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>KeyVault properties for the cluster encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="languageExtensions" /></td>
    <td><code>object</code></td>
    <td>List of the cluster's language extensions.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationCluster" /></td>
    <td><code>object</code></td>
    <td>Properties of the peer cluster involved in a migration to/from this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedAutoscale" /></td>
    <td><code>object</code></td>
    <td>Optimized auto scale definition.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>A list of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled". (Running, Creating, Deleting, Succeeded, Failed, Moving, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPType" /></td>
    <td><code>string</code></td>
    <td>Indicates what public IP type to create - IPv4 (default), or DualStack (both IPv4 and IPv6). Known values are: "IPv4" and "DualStack". (IPv4, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Public network access to the cluster is enabled by default. When disabled, only private endpoint connection to the cluster is allowed. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not to restrict outbound network access. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the resource. Known values are: "Creating", "Unavailable", "Running", "Deleting", "Deleted", "Stopping", "Stopped", "Starting", "Updating", and "Migrated". (Creating, Unavailable, Running, Deleting, Deleted, Stopping, Stopped, Starting, Updating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="stateReason" /></td>
    <td><code>string</code></td>
    <td>The reason for the cluster's current state.</td>
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
    <td><CopyableCode code="trustedExternalTenants" /></td>
    <td><code>array</code></td>
    <td>The cluster's external tenants.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>The cluster URI.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualClusterGraduationProperties" /></td>
    <td><code>string</code></td>
    <td>Virtual Cluster graduation properties.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Virtual network definition.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the cluster is zonal or non-zonal. Known values are: "NonZonal", "ZonalInconsistency", and "Zonal". (NonZonal, ZonalInconsistency, Zonal)</td>
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
    <td><CopyableCode code="acceptedAudiences" /></td>
    <td><code>array</code></td>
    <td>The cluster's accepted audiences.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>List of allowed FQDNs(Fully Qualified Domain Name) for egress from Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedIpRangeList" /></td>
    <td><code>array</code></td>
    <td>The list of ips in the format of CIDR allowed to connect to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="calloutPolicies" /></td>
    <td><code>array</code></td>
    <td>List of callout policies for egress from Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="dataIngestionUri" /></td>
    <td><code>string</code></td>
    <td>The cluster data ingestion URI.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoStop" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the cluster could be automatically stopped (due to lack of data or no activity for many days).</td>
</tr>
<tr>
    <td><CopyableCode code="enableDiskEncryption" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the cluster's disks are encrypted.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDoubleEncryption" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if double encryption is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurge" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the purge operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableStreamingIngest" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the streaming ingest is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="engineType" /></td>
    <td><code>string</code></td>
    <td>The engine type. Known values are: "V2" and "V3". (V2, V3)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>KeyVault properties for the cluster encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="languageExtensions" /></td>
    <td><code>object</code></td>
    <td>List of the cluster's language extensions.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationCluster" /></td>
    <td><code>object</code></td>
    <td>Properties of the peer cluster involved in a migration to/from this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedAutoscale" /></td>
    <td><code>object</code></td>
    <td>Optimized auto scale definition.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>A list of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled". (Running, Creating, Deleting, Succeeded, Failed, Moving, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPType" /></td>
    <td><code>string</code></td>
    <td>Indicates what public IP type to create - IPv4 (default), or DualStack (both IPv4 and IPv6). Known values are: "IPv4" and "DualStack". (IPv4, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Public network access to the cluster is enabled by default. When disabled, only private endpoint connection to the cluster is allowed. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not to restrict outbound network access. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the resource. Known values are: "Creating", "Unavailable", "Running", "Deleting", "Deleted", "Stopping", "Stopped", "Starting", "Updating", and "Migrated". (Creating, Unavailable, Running, Deleting, Deleted, Stopping, Stopped, Starting, Updating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="stateReason" /></td>
    <td><code>string</code></td>
    <td>The reason for the cluster's current state.</td>
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
    <td><CopyableCode code="trustedExternalTenants" /></td>
    <td><code>array</code></td>
    <td>The cluster's external tenants.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>The cluster URI.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualClusterGraduationProperties" /></td>
    <td><code>string</code></td>
    <td>Virtual Cluster graduation properties.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Virtual network definition.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the cluster is zonal or non-zonal. Known values are: "NonZonal", "ZonalInconsistency", and "Zonal". (NonZonal, ZonalInconsistency, Zonal)</td>
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
    <td><CopyableCode code="acceptedAudiences" /></td>
    <td><code>array</code></td>
    <td>The cluster's accepted audiences.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>List of allowed FQDNs(Fully Qualified Domain Name) for egress from Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedIpRangeList" /></td>
    <td><code>array</code></td>
    <td>The list of ips in the format of CIDR allowed to connect to the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="calloutPolicies" /></td>
    <td><code>array</code></td>
    <td>List of callout policies for egress from Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="dataIngestionUri" /></td>
    <td><code>string</code></td>
    <td>The cluster data ingestion URI.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoStop" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the cluster could be automatically stopped (due to lack of data or no activity for many days).</td>
</tr>
<tr>
    <td><CopyableCode code="enableDiskEncryption" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the cluster's disks are encrypted.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDoubleEncryption" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if double encryption is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurge" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the purge operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableStreamingIngest" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the streaming ingest is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="engineType" /></td>
    <td><code>string</code></td>
    <td>The engine type. Known values are: "V2" and "V3". (V2, V3)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>KeyVault properties for the cluster encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="languageExtensions" /></td>
    <td><code>object</code></td>
    <td>List of the cluster's language extensions.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationCluster" /></td>
    <td><code>object</code></td>
    <td>Properties of the peer cluster involved in a migration to/from this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedAutoscale" /></td>
    <td><code>object</code></td>
    <td>Optimized auto scale definition.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>A list of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled". (Running, Creating, Deleting, Succeeded, Failed, Moving, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPType" /></td>
    <td><code>string</code></td>
    <td>Indicates what public IP type to create - IPv4 (default), or DualStack (both IPv4 and IPv6). Known values are: "IPv4" and "DualStack". (IPv4, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Public network access to the cluster is enabled by default. When disabled, only private endpoint connection to the cluster is allowed. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not to restrict outbound network access. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the resource. Known values are: "Creating", "Unavailable", "Running", "Deleting", "Deleted", "Stopping", "Stopped", "Starting", "Updating", and "Migrated". (Creating, Unavailable, Running, Deleting, Deleted, Stopping, Stopped, Starting, Updating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="stateReason" /></td>
    <td><code>string</code></td>
    <td>The reason for the cluster's current state.</td>
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
    <td><CopyableCode code="trustedExternalTenants" /></td>
    <td><code>array</code></td>
    <td>The cluster's external tenants.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>The cluster URI.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualClusterGraduationProperties" /></td>
    <td><code>string</code></td>
    <td>Virtual Cluster graduation properties.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Virtual network definition.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the cluster is zonal or non-zonal. Known values are: "NonZonal", "ZonalInconsistency", and "Zonal". (NonZonal, ZonalInconsistency, Zonal)</td>
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
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks that the cluster name is valid and is not already in use.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Kusto clusters within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Kusto clusters within a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#list_follower_databases_get"><CopyableCode code="list_follower_databases_get" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of databases that are owned by this cluster and were followed by another cluster.</td>
</tr>
<tr>
    <td><a href="#list_follower_databases"><CopyableCode code="list_follower_databases" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of databases that are owned by this cluster and were followed by another cluster.</td>
</tr>
<tr>
    <td><a href="#list_skus_by_resource"><CopyableCode code="list_skus_by_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the SKUs available for the provided resource.</td>
</tr>
<tr>
    <td><a href="#list_outbound_network_dependencies_endpoints"><CopyableCode code="list_outbound_network_dependencies_endpoints" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the network endpoints of all outbound dependencies of a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#list_callout_policies"><CopyableCode code="list_callout_policies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the allowed callout policies for the specified service.</td>
</tr>
<tr>
    <td><a href="#list_language_extensions"><CopyableCode code="list_language_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of language extensions that can run within KQL queries.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists eligible SKUs for Kusto resource provider.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a Kusto cluster.</td>
</tr>
<tr>
    <td><a href="#migrate"><CopyableCode code="migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-clusterResourceId"><code>clusterResourceId</code></a></td>
    <td></td>
    <td>Migrate data from a Kusto cluster to another cluster.</td>
</tr>
<tr>
    <td><a href="#detach_follower_databases"><CopyableCode code="detach_follower_databases" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-clusterResourceId"><code>clusterResourceId</code></a>, <a href="#parameter-attachedDatabaseConfigurationName"><code>attachedDatabaseConfigurationName</code></a></td>
    <td></td>
    <td>Detaches all followers of a database owned by this cluster.</td>
</tr>
<tr>
    <td><a href="#diagnose_virtual_network"><CopyableCode code="diagnose_virtual_network" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Diagnoses network connectivity status for external resources on which the service is dependent on.</td>
</tr>
<tr>
    <td><a href="#add_callout_policies"><CopyableCode code="add_callout_policies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Adds a list of callout policies for engine services.</td>
</tr>
<tr>
    <td><a href="#remove_callout_policy"><CopyableCode code="remove_callout_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes callout policy for engine services.</td>
</tr>
<tr>
    <td><a href="#add_language_extensions"><CopyableCode code="add_language_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add a list of language extensions that can run within KQL queries.</td>
</tr>
<tr>
    <td><a href="#remove_language_extensions"><CopyableCode code="remove_language_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove a list of language extensions that can run within KQL queries.</td>
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
    <td>The name of the Kusto cluster. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
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
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="check_name_availability">

Checks that the cluster name is valid and is not already in use.

```sql
SELECT
name,
message,
nameAvailable,
reason
FROM azure.kusto.clusters
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a Kusto cluster.

```sql
SELECT
id,
name,
acceptedAudiences,
allowedFqdnList,
allowedIpRangeList,
calloutPolicies,
dataIngestionUri,
enableAutoStop,
enableDiskEncryption,
enableDoubleEncryption,
enablePurge,
enableStreamingIngest,
engineType,
etag,
identity,
keyVaultProperties,
languageExtensions,
location,
migrationCluster,
optimizedAutoscale,
privateEndpointConnections,
provisioningState,
publicIPType,
publicNetworkAccess,
restrictOutboundNetworkAccess,
sku,
state,
stateReason,
systemData,
tags,
trustedExternalTenants,
type,
uri,
virtualClusterGraduationProperties,
virtualNetworkConfiguration,
zoneStatus,
zones
FROM azure.kusto.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all Kusto clusters within a resource group.

```sql
SELECT
id,
name,
acceptedAudiences,
allowedFqdnList,
allowedIpRangeList,
calloutPolicies,
dataIngestionUri,
enableAutoStop,
enableDiskEncryption,
enableDoubleEncryption,
enablePurge,
enableStreamingIngest,
engineType,
etag,
identity,
keyVaultProperties,
languageExtensions,
location,
migrationCluster,
optimizedAutoscale,
privateEndpointConnections,
provisioningState,
publicIPType,
publicNetworkAccess,
restrictOutboundNetworkAccess,
sku,
state,
stateReason,
systemData,
tags,
trustedExternalTenants,
type,
uri,
virtualClusterGraduationProperties,
virtualNetworkConfiguration,
zoneStatus,
zones
FROM azure.kusto.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Kusto clusters within a subscription.

```sql
SELECT
id,
name,
acceptedAudiences,
allowedFqdnList,
allowedIpRangeList,
calloutPolicies,
dataIngestionUri,
enableAutoStop,
enableDiskEncryption,
enableDoubleEncryption,
enablePurge,
enableStreamingIngest,
engineType,
etag,
identity,
keyVaultProperties,
languageExtensions,
location,
migrationCluster,
optimizedAutoscale,
privateEndpointConnections,
provisioningState,
publicIPType,
publicNetworkAccess,
restrictOutboundNetworkAccess,
sku,
state,
stateReason,
systemData,
tags,
trustedExternalTenants,
type,
uri,
virtualClusterGraduationProperties,
virtualNetworkConfiguration,
zoneStatus,
zones
FROM azure.kusto.clusters
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

Create or update a Kusto cluster.

```sql
INSERT INTO azure.kusto.clusters (
tags,
location,
properties,
sku,
zones,
identity,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ zones }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
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
        The cluster properties.
      value:
        state: "{{ state }}"
        provisioningState: "{{ provisioningState }}"
        uri: "{{ uri }}"
        dataIngestionUri: "{{ dataIngestionUri }}"
        stateReason: "{{ stateReason }}"
        trustedExternalTenants:
          - value: "{{ value }}"
        optimizedAutoscale:
          version: {{ version }}
          isEnabled: {{ isEnabled }}
          minimum: {{ minimum }}
          maximum: {{ maximum }}
        enableDiskEncryption: {{ enableDiskEncryption }}
        enableStreamingIngest: {{ enableStreamingIngest }}
        virtualNetworkConfiguration:
          subnetId: "{{ subnetId }}"
          enginePublicIpId: "{{ enginePublicIpId }}"
          dataManagementPublicIpId: "{{ dataManagementPublicIpId }}"
          state: "{{ state }}"
        keyVaultProperties:
          keyName: "{{ keyName }}"
          keyVersion: "{{ keyVersion }}"
          keyVaultUri: "{{ keyVaultUri }}"
          userIdentity: "{{ userIdentity }}"
          federatedIdentityClientId: "{{ federatedIdentityClientId }}"
        enablePurge: {{ enablePurge }}
        languageExtensions:
          value:
            - languageExtensionName: "{{ languageExtensionName }}"
              languageExtensionImageName: "{{ languageExtensionImageName }}"
              languageExtensionCustomImageName: "{{ languageExtensionCustomImageName }}"
          nextLink: "{{ nextLink }}"
        enableDoubleEncryption: {{ enableDoubleEncryption }}
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        allowedIpRangeList:
          - "{{ allowedIpRangeList }}"
        engineType: "{{ engineType }}"
        acceptedAudiences:
          - value: "{{ value }}"
        enableAutoStop: {{ enableAutoStop }}
        restrictOutboundNetworkAccess: "{{ restrictOutboundNetworkAccess }}"
        allowedFqdnList:
          - "{{ allowedFqdnList }}"
        calloutPolicies:
          - calloutUriRegex: "{{ calloutUriRegex }}"
            calloutType: "{{ calloutType }}"
            outboundAccess: "{{ outboundAccess }}"
            calloutId: "{{ calloutId }}"
        publicIPType: "{{ publicIPType }}"
        virtualClusterGraduationProperties: "{{ virtualClusterGraduationProperties }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              groupId: "{{ groupId }}"
              provisioningState: "{{ provisioningState }}"
        migrationCluster:
          id: "{{ id }}"
          uri: "{{ uri }}"
          dataIngestionUri: "{{ dataIngestionUri }}"
          role: "{{ role }}"
        zoneStatus: "{{ zoneStatus }}"
    - name: sku
      description: |
        The SKU of the cluster. Required.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
        tier: "{{ tier }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
    - name: identity
      description: |
        The identity of the cluster, if configured.
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

Update a Kusto cluster.

```sql
UPDATE azure.kusto.clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
zones = '{{ zones }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
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

Create or update a Kusto cluster.

```sql
REPLACE azure.kusto.clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
zones = '{{ zones }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Deletes a Kusto cluster.

```sql
DELETE FROM azure.kusto.clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_follower_databases_get"
    values={[
        { label: 'list_follower_databases_get', value: 'list_follower_databases_get' },
        { label: 'list_follower_databases', value: 'list_follower_databases' },
        { label: 'list_skus_by_resource', value: 'list_skus_by_resource' },
        { label: 'list_outbound_network_dependencies_endpoints', value: 'list_outbound_network_dependencies_endpoints' },
        { label: 'list_callout_policies', value: 'list_callout_policies' },
        { label: 'list_language_extensions', value: 'list_language_extensions' },
        { label: 'list_skus', value: 'list_skus' },
        { label: 'stop', value: 'stop' },
        { label: 'start', value: 'start' },
        { label: 'migrate', value: 'migrate' },
        { label: 'detach_follower_databases', value: 'detach_follower_databases' },
        { label: 'diagnose_virtual_network', value: 'diagnose_virtual_network' },
        { label: 'add_callout_policies', value: 'add_callout_policies' },
        { label: 'remove_callout_policy', value: 'remove_callout_policy' },
        { label: 'add_language_extensions', value: 'add_language_extensions' },
        { label: 'remove_language_extensions', value: 'remove_language_extensions' }
    ]}
>
<TabItem value="list_follower_databases_get">

Returns a list of databases that are owned by this cluster and were followed by another cluster.

```sql
EXEC azure.kusto.clusters.list_follower_databases_get 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_follower_databases">

Returns a list of databases that are owned by this cluster and were followed by another cluster.

```sql
EXEC azure.kusto.clusters.list_follower_databases 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_skus_by_resource">

Returns the SKUs available for the provided resource.

```sql
EXEC azure.kusto.clusters.list_skus_by_resource 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_outbound_network_dependencies_endpoints">

Gets the network endpoints of all outbound dependencies of a Kusto cluster.

```sql
EXEC azure.kusto.clusters.list_outbound_network_dependencies_endpoints 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_callout_policies">

Returns the allowed callout policies for the specified service.

```sql
EXEC azure.kusto.clusters.list_callout_policies 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_language_extensions">

Returns a list of language extensions that can run within KQL queries.

```sql
EXEC azure.kusto.clusters.list_language_extensions 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_skus">

Lists eligible SKUs for Kusto resource provider.

```sql
EXEC azure.kusto.clusters.list_skus 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a Kusto cluster.

```sql
EXEC azure.kusto.clusters.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts a Kusto cluster.

```sql
EXEC azure.kusto.clusters.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate">

Migrate data from a Kusto cluster to another cluster.

```sql
EXEC azure.kusto.clusters.migrate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"clusterResourceId": "{{ clusterResourceId }}"
}'
;
```
</TabItem>
<TabItem value="detach_follower_databases">

Detaches all followers of a database owned by this cluster.

```sql
EXEC azure.kusto.clusters.detach_follower_databases 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"clusterResourceId": "{{ clusterResourceId }}", 
"attachedDatabaseConfigurationName": "{{ attachedDatabaseConfigurationName }}"
}'
;
```
</TabItem>
<TabItem value="diagnose_virtual_network">

Diagnoses network connectivity status for external resources on which the service is dependent on.

```sql
EXEC azure.kusto.clusters.diagnose_virtual_network 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="add_callout_policies">

Adds a list of callout policies for engine services.

```sql
EXEC azure.kusto.clusters.add_callout_policies 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}", 
"nextLink": "{{ nextLink }}"
}'
;
```
</TabItem>
<TabItem value="remove_callout_policy">

Removes callout policy for engine services.

```sql
EXEC azure.kusto.clusters.remove_callout_policy 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"calloutId": "{{ calloutId }}"
}'
;
```
</TabItem>
<TabItem value="add_language_extensions">

Add a list of language extensions that can run within KQL queries.

```sql
EXEC azure.kusto.clusters.add_language_extensions 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}", 
"nextLink": "{{ nextLink }}"
}'
;
```
</TabItem>
<TabItem value="remove_language_extensions">

Remove a list of language extensions that can run within KQL queries.

```sql
EXEC azure.kusto.clusters.remove_language_extensions 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}", 
"nextLink": "{{ nextLink }}"
}'
;
```
</TabItem>
</Tabs>
