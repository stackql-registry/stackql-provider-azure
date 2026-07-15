--- 
title: cassandra_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters
  - cosmosdb
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

Creates, updates, deletes, gets or lists a <code>cassandra_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cassandra_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.cassandra_clusters" /></td></tr>
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
    <td><CopyableCode code="authenticationMethod" /></td>
    <td><code>string</code></td>
    <td>Which authentication method Cassandra should use to authenticate clients. 'None' turns off authentication, so should not be used except in emergencies. 'Cassandra' is the default password based authentication. The default is 'Cassandra'. Known values are: "None", "Cassandra", and "Ldap". (None, Cassandra, Ldap)</td>
</tr>
<tr>
    <td><CopyableCode code="autoReplicate" /></td>
    <td><code>string</code></td>
    <td>The form of AutoReplicate that is being used by this cluster. Known values are: "None", "SystemKeyspaces", and "AllKeyspaces". (None, SystemKeyspaces, AllKeyspaces)</td>
</tr>
<tr>
    <td><CopyableCode code="azureConnectionMethod" /></td>
    <td><code>string</code></td>
    <td>How to connect to the azure services needed for running the cluster. Known values are: "None" and "VPN". (None, VPN)</td>
</tr>
<tr>
    <td><CopyableCode code="backupSchedules" /></td>
    <td><code>array</code></td>
    <td>List of backup schedules that define when you want to back up your data.</td>
</tr>
<tr>
    <td><CopyableCode code="cassandraAuditLoggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cassandra audit logging is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="cassandraVersion" /></td>
    <td><code>string</code></td>
    <td>Which version of Cassandra should this cluster converge to running (e.g., 3.11). When updated, the cluster may take some time to migrate to the new version.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates used to authorize clients connecting to the cluster. All connections are TLS encrypted whether clientCertificates is set or not, but if clientCertificates is set, the managed Cassandra cluster will reject all connections not bearing a TLS client certificate that can be validated from one or more of the public certificates in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterNameOverride" /></td>
    <td><code>string</code></td>
    <td>If you need to set the clusterName property in cassandra.yaml to something besides the resource name of the cluster, set the value to use on this property.</td>
</tr>
<tr>
    <td><CopyableCode code="deallocated" /></td>
    <td><code>boolean</code></td>
    <td>Whether the cluster and associated data centers has been deallocated.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagementSubnetId" /></td>
    <td><code>string</code></td>
    <td>Resource id of a subnet that this cluster's management service should have its network interface attached to. The subnet must be routable to all subnets that will be delegated to data centers. The resource id must be of the form '/subscriptions//resourceGroups//providers/Microsoft.Network/virtualNetworks//subnets/'.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Extensions to be added or updated on cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="externalDataCenters" /></td>
    <td><code>array</code></td>
    <td>List of the data center names for unmanaged data centers in this cluster to be included in auto-replication.</td>
</tr>
<tr>
    <td><CopyableCode code="externalGossipCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates used to authorize gossip from unmanaged data centers. The TLS certificates of all nodes in unmanaged data centers must be verifiable using one of the certificates provided in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="externalSeedNodes" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses of seed nodes in unmanaged data centers. These will be added to the seed node lists of all managed nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="gossipCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates that unmanaged nodes must trust for gossip with managed nodes. All managed nodes will present TLS client certificates that are verifiable using one of the certificates provided in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="hoursBetweenBackups" /></td>
    <td><code>integer</code></td>
    <td>(Deprecated) Number of hours to wait between taking a backup of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="initialCassandraAdminPassword" /></td>
    <td><code>string</code></td>
    <td>Initial password for clients connecting as admin to the cluster. Should be changed after cluster creation. Returns null on GET. This field only applies when the authenticationMethod field is 'Cassandra'.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>If the Connection Method is Vpn, this is the Id of the private link resource that the datacenters need to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="prometheusEndpoint" /></td>
    <td><code>object</code></td>
    <td>SeedNode.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionError" /></td>
    <td><code>object</code></td>
    <td>Error related to resource provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the resource at the time the operation was called. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="repairEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Should automatic repairs run on this cluster? If omitted, this is true, and should stay true unless you are running a hybrid cluster where you are already doing your own repairs.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreFromBackupId" /></td>
    <td><code>string</code></td>
    <td>To create an empty cluster, omit this field or set it to null. To restore a backup into a new cluster, set this field to the resource id of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventStrategy" /></td>
    <td><code>string</code></td>
    <td>How the nodes in the cluster react to scheduled events. Known values are: "Ignore", "StopAny", and "StopByRack". (Ignore, StopAny, StopByRack)</td>
</tr>
<tr>
    <td><CopyableCode code="seedNodes" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses of seed nodes in the managed data centers. These should be added to the seed node lists of all unmanaged nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \"defaultExperience\": \"Cassandra\". Current \"defaultExperience\" values also include \"Table\", \"Graph\", \"DocumentDB\", and \"MongoDB\".</td>
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
    <td><CopyableCode code="authenticationMethod" /></td>
    <td><code>string</code></td>
    <td>Which authentication method Cassandra should use to authenticate clients. 'None' turns off authentication, so should not be used except in emergencies. 'Cassandra' is the default password based authentication. The default is 'Cassandra'. Known values are: "None", "Cassandra", and "Ldap". (None, Cassandra, Ldap)</td>
</tr>
<tr>
    <td><CopyableCode code="autoReplicate" /></td>
    <td><code>string</code></td>
    <td>The form of AutoReplicate that is being used by this cluster. Known values are: "None", "SystemKeyspaces", and "AllKeyspaces". (None, SystemKeyspaces, AllKeyspaces)</td>
</tr>
<tr>
    <td><CopyableCode code="azureConnectionMethod" /></td>
    <td><code>string</code></td>
    <td>How to connect to the azure services needed for running the cluster. Known values are: "None" and "VPN". (None, VPN)</td>
</tr>
<tr>
    <td><CopyableCode code="backupSchedules" /></td>
    <td><code>array</code></td>
    <td>List of backup schedules that define when you want to back up your data.</td>
</tr>
<tr>
    <td><CopyableCode code="cassandraAuditLoggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cassandra audit logging is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="cassandraVersion" /></td>
    <td><code>string</code></td>
    <td>Which version of Cassandra should this cluster converge to running (e.g., 3.11). When updated, the cluster may take some time to migrate to the new version.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates used to authorize clients connecting to the cluster. All connections are TLS encrypted whether clientCertificates is set or not, but if clientCertificates is set, the managed Cassandra cluster will reject all connections not bearing a TLS client certificate that can be validated from one or more of the public certificates in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterNameOverride" /></td>
    <td><code>string</code></td>
    <td>If you need to set the clusterName property in cassandra.yaml to something besides the resource name of the cluster, set the value to use on this property.</td>
</tr>
<tr>
    <td><CopyableCode code="deallocated" /></td>
    <td><code>boolean</code></td>
    <td>Whether the cluster and associated data centers has been deallocated.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagementSubnetId" /></td>
    <td><code>string</code></td>
    <td>Resource id of a subnet that this cluster's management service should have its network interface attached to. The subnet must be routable to all subnets that will be delegated to data centers. The resource id must be of the form '/subscriptions//resourceGroups//providers/Microsoft.Network/virtualNetworks//subnets/'.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Extensions to be added or updated on cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="externalDataCenters" /></td>
    <td><code>array</code></td>
    <td>List of the data center names for unmanaged data centers in this cluster to be included in auto-replication.</td>
</tr>
<tr>
    <td><CopyableCode code="externalGossipCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates used to authorize gossip from unmanaged data centers. The TLS certificates of all nodes in unmanaged data centers must be verifiable using one of the certificates provided in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="externalSeedNodes" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses of seed nodes in unmanaged data centers. These will be added to the seed node lists of all managed nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="gossipCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates that unmanaged nodes must trust for gossip with managed nodes. All managed nodes will present TLS client certificates that are verifiable using one of the certificates provided in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="hoursBetweenBackups" /></td>
    <td><code>integer</code></td>
    <td>(Deprecated) Number of hours to wait between taking a backup of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="initialCassandraAdminPassword" /></td>
    <td><code>string</code></td>
    <td>Initial password for clients connecting as admin to the cluster. Should be changed after cluster creation. Returns null on GET. This field only applies when the authenticationMethod field is 'Cassandra'.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>If the Connection Method is Vpn, this is the Id of the private link resource that the datacenters need to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="prometheusEndpoint" /></td>
    <td><code>object</code></td>
    <td>SeedNode.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionError" /></td>
    <td><code>object</code></td>
    <td>Error related to resource provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the resource at the time the operation was called. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="repairEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Should automatic repairs run on this cluster? If omitted, this is true, and should stay true unless you are running a hybrid cluster where you are already doing your own repairs.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreFromBackupId" /></td>
    <td><code>string</code></td>
    <td>To create an empty cluster, omit this field or set it to null. To restore a backup into a new cluster, set this field to the resource id of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventStrategy" /></td>
    <td><code>string</code></td>
    <td>How the nodes in the cluster react to scheduled events. Known values are: "Ignore", "StopAny", and "StopByRack". (Ignore, StopAny, StopByRack)</td>
</tr>
<tr>
    <td><CopyableCode code="seedNodes" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses of seed nodes in the managed data centers. These should be added to the seed node lists of all unmanaged nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \"defaultExperience\": \"Cassandra\". Current \"defaultExperience\" values also include \"Table\", \"Graph\", \"DocumentDB\", and \"MongoDB\".</td>
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
    <td><CopyableCode code="authenticationMethod" /></td>
    <td><code>string</code></td>
    <td>Which authentication method Cassandra should use to authenticate clients. 'None' turns off authentication, so should not be used except in emergencies. 'Cassandra' is the default password based authentication. The default is 'Cassandra'. Known values are: "None", "Cassandra", and "Ldap". (None, Cassandra, Ldap)</td>
</tr>
<tr>
    <td><CopyableCode code="autoReplicate" /></td>
    <td><code>string</code></td>
    <td>The form of AutoReplicate that is being used by this cluster. Known values are: "None", "SystemKeyspaces", and "AllKeyspaces". (None, SystemKeyspaces, AllKeyspaces)</td>
</tr>
<tr>
    <td><CopyableCode code="azureConnectionMethod" /></td>
    <td><code>string</code></td>
    <td>How to connect to the azure services needed for running the cluster. Known values are: "None" and "VPN". (None, VPN)</td>
</tr>
<tr>
    <td><CopyableCode code="backupSchedules" /></td>
    <td><code>array</code></td>
    <td>List of backup schedules that define when you want to back up your data.</td>
</tr>
<tr>
    <td><CopyableCode code="cassandraAuditLoggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cassandra audit logging is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="cassandraVersion" /></td>
    <td><code>string</code></td>
    <td>Which version of Cassandra should this cluster converge to running (e.g., 3.11). When updated, the cluster may take some time to migrate to the new version.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates used to authorize clients connecting to the cluster. All connections are TLS encrypted whether clientCertificates is set or not, but if clientCertificates is set, the managed Cassandra cluster will reject all connections not bearing a TLS client certificate that can be validated from one or more of the public certificates in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterNameOverride" /></td>
    <td><code>string</code></td>
    <td>If you need to set the clusterName property in cassandra.yaml to something besides the resource name of the cluster, set the value to use on this property.</td>
</tr>
<tr>
    <td><CopyableCode code="deallocated" /></td>
    <td><code>boolean</code></td>
    <td>Whether the cluster and associated data centers has been deallocated.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedManagementSubnetId" /></td>
    <td><code>string</code></td>
    <td>Resource id of a subnet that this cluster's management service should have its network interface attached to. The subnet must be routable to all subnets that will be delegated to data centers. The resource id must be of the form '/subscriptions//resourceGroups//providers/Microsoft.Network/virtualNetworks//subnets/'.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Extensions to be added or updated on cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="externalDataCenters" /></td>
    <td><code>array</code></td>
    <td>List of the data center names for unmanaged data centers in this cluster to be included in auto-replication.</td>
</tr>
<tr>
    <td><CopyableCode code="externalGossipCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates used to authorize gossip from unmanaged data centers. The TLS certificates of all nodes in unmanaged data centers must be verifiable using one of the certificates provided in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="externalSeedNodes" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses of seed nodes in unmanaged data centers. These will be added to the seed node lists of all managed nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="gossipCertificates" /></td>
    <td><code>array</code></td>
    <td>List of TLS certificates that unmanaged nodes must trust for gossip with managed nodes. All managed nodes will present TLS client certificates that are verifiable using one of the certificates provided in this property.</td>
</tr>
<tr>
    <td><CopyableCode code="hoursBetweenBackups" /></td>
    <td><code>integer</code></td>
    <td>(Deprecated) Number of hours to wait between taking a backup of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="initialCassandraAdminPassword" /></td>
    <td><code>string</code></td>
    <td>Initial password for clients connecting as admin to the cluster. Should be changed after cluster creation. Returns null on GET. This field only applies when the authenticationMethod field is 'Cassandra'.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource group to which the resource belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>If the Connection Method is Vpn, this is the Id of the private link resource that the datacenters need to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="prometheusEndpoint" /></td>
    <td><code>object</code></td>
    <td>SeedNode.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionError" /></td>
    <td><code>object</code></td>
    <td>Error related to resource provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the resource at the time the operation was called. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="repairEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Should automatic repairs run on this cluster? If omitted, this is true, and should stay true unless you are running a hybrid cluster where you are already doing your own repairs.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreFromBackupId" /></td>
    <td><code>string</code></td>
    <td>To create an empty cluster, omit this field or set it to null. To restore a backup into a new cluster, set this field to the resource id of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventStrategy" /></td>
    <td><code>string</code></td>
    <td>How the nodes in the cluster react to scheduled events. Known values are: "Ignore", "StopAny", and "StopByRack". (Ignore, StopAny, StopByRack)</td>
</tr>
<tr>
    <td><CopyableCode code="seedNodes" /></td>
    <td><code>array</code></td>
    <td>List of IP addresses of seed nodes in the managed data centers. These should be added to the seed node lists of all unmanaged nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \"defaultExperience\": \"Cassandra\". Current \"defaultExperience\" values also include \"Table\", \"Graph\", \"DocumentDB\", and \"MongoDB\".</td>
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
    <td>Get the properties of a managed Cassandra cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all managed Cassandra clusters in this resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all managed Cassandra clusters in this subscription.</td>
</tr>
<tr>
    <td><a href="#create_update"><CopyableCode code="create_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a managed Cassandra cluster. When updating, you must specify all writable properties. To update only some properties, use PATCH.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates some of the properties of a managed Cassandra cluster.</td>
</tr>
<tr>
    <td><a href="#create_update"><CopyableCode code="create_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a managed Cassandra cluster. When updating, you must specify all writable properties. To update only some properties, use PATCH.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a managed Cassandra cluster.</td>
</tr>
<tr>
    <td><a href="#invoke_command"><CopyableCode code="invoke_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-command"><code>command</code></a>, <a href="#parameter-host"><code>host</code></a></td>
    <td></td>
    <td>Invoke a command like nodetool for cassandra maintenance.</td>
</tr>
<tr>
    <td><a href="#deallocate"><CopyableCode code="deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-force-deallocate"><code>x-ms-force-deallocate</code></a></td>
    <td>Deallocate the Managed Cassandra Cluster and Associated Data Centers. Deallocation will deallocate the host virtual machine of this cluster, and reserved the data disk. This won't do anything on an already deallocated cluster. Use Start to restart the cluster.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start the Managed Cassandra Cluster and Associated Data Centers. Start will start the host virtual machine of this cluster with reserved data disk. This won't do anything on an already running cluster. Use Deallocate to deallocate the cluster.</td>
</tr>
<tr>
    <td><a href="#status"><CopyableCode code="status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the CPU, memory, and disk usage statistics for each Cassandra node in a cluster.</td>
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
    <td>Managed Cassandra cluster name. Required.</td>
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
<tr id="parameter-x-ms-force-deallocate">
    <td><CopyableCode code="x-ms-force-deallocate" /></td>
    <td><code>string</code></td>
    <td>Force to deallocate a cluster of Cluster Type Production. Force to deallocate a cluster of Cluster Type Production might cause data loss. Default value is None.</td>
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

Get the properties of a managed Cassandra cluster.

```sql
SELECT
id,
name,
authenticationMethod,
autoReplicate,
azureConnectionMethod,
backupSchedules,
cassandraAuditLoggingEnabled,
cassandraVersion,
clientCertificates,
clusterNameOverride,
deallocated,
delegatedManagementSubnetId,
extensions,
externalDataCenters,
externalGossipCertificates,
externalSeedNodes,
gossipCertificates,
hoursBetweenBackups,
identity,
initialCassandraAdminPassword,
location,
privateLinkResourceId,
prometheusEndpoint,
provisionError,
provisioningState,
repairEnabled,
restoreFromBackupId,
scheduledEventStrategy,
seedNodes,
systemData,
tags,
type
FROM azure.cosmosdb.cassandra_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all managed Cassandra clusters in this resource group.

```sql
SELECT
id,
name,
authenticationMethod,
autoReplicate,
azureConnectionMethod,
backupSchedules,
cassandraAuditLoggingEnabled,
cassandraVersion,
clientCertificates,
clusterNameOverride,
deallocated,
delegatedManagementSubnetId,
extensions,
externalDataCenters,
externalGossipCertificates,
externalSeedNodes,
gossipCertificates,
hoursBetweenBackups,
identity,
initialCassandraAdminPassword,
location,
privateLinkResourceId,
prometheusEndpoint,
provisionError,
provisioningState,
repairEnabled,
restoreFromBackupId,
scheduledEventStrategy,
seedNodes,
systemData,
tags,
type
FROM azure.cosmosdb.cassandra_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all managed Cassandra clusters in this subscription.

```sql
SELECT
id,
name,
authenticationMethod,
autoReplicate,
azureConnectionMethod,
backupSchedules,
cassandraAuditLoggingEnabled,
cassandraVersion,
clientCertificates,
clusterNameOverride,
deallocated,
delegatedManagementSubnetId,
extensions,
externalDataCenters,
externalGossipCertificates,
externalSeedNodes,
gossipCertificates,
hoursBetweenBackups,
identity,
initialCassandraAdminPassword,
location,
privateLinkResourceId,
prometheusEndpoint,
provisionError,
provisioningState,
repairEnabled,
restoreFromBackupId,
scheduledEventStrategy,
seedNodes,
systemData,
tags,
type
FROM azure.cosmosdb.cassandra_clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_update"
    values={[
        { label: 'create_update', value: 'create_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_update">

Create or update a managed Cassandra cluster. When updating, you must specify all writable properties. To update only some properties, use PATCH.

```sql
INSERT INTO azure.cosmosdb.cassandra_clusters (
properties,
location,
tags,
identity,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: cassandra_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cassandra_clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the cassandra_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cassandra_clusters resource.
    - name: properties
      description: |
        Properties of a managed Cassandra cluster.
      value:
        provisioningState: "{{ provisioningState }}"
        restoreFromBackupId: "{{ restoreFromBackupId }}"
        delegatedManagementSubnetId: "{{ delegatedManagementSubnetId }}"
        cassandraVersion: "{{ cassandraVersion }}"
        clusterNameOverride: "{{ clusterNameOverride }}"
        authenticationMethod: "{{ authenticationMethod }}"
        initialCassandraAdminPassword: "{{ initialCassandraAdminPassword }}"
        prometheusEndpoint:
          ipAddress: "{{ ipAddress }}"
        repairEnabled: {{ repairEnabled }}
        autoReplicate: "{{ autoReplicate }}"
        clientCertificates:
          - pem: "{{ pem }}"
        externalGossipCertificates:
          - pem: "{{ pem }}"
        gossipCertificates:
          - pem: "{{ pem }}"
        externalSeedNodes:
          - ipAddress: "{{ ipAddress }}"
        seedNodes:
          - ipAddress: "{{ ipAddress }}"
        externalDataCenters:
          - "{{ externalDataCenters }}"
        hoursBetweenBackups: {{ hoursBetweenBackups }}
        deallocated: {{ deallocated }}
        cassandraAuditLoggingEnabled: {{ cassandraAuditLoggingEnabled }}
        provisionError:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          additionalErrorInfo: "{{ additionalErrorInfo }}"
        extensions:
          - "{{ extensions }}"
        backupSchedules:
          - scheduleName: "{{ scheduleName }}"
            cronExpression: "{{ cronExpression }}"
            retentionInHours: {{ retentionInHours }}
        scheduledEventStrategy: "{{ scheduledEventStrategy }}"
        azureConnectionMethod: "{{ azureConnectionMethod }}"
        privateLinkResourceId: "{{ privateLinkResourceId }}"
    - name: location
      value: "{{ location }}"
      description: |
        The location of the resource group to which the resource belongs.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \"defaultExperience\": \"Cassandra\". Current \"defaultExperience\" values also include \"Table\", \"Graph\", \"DocumentDB\", and \"MongoDB\".
    - name: identity
      description: |
        Identity for the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
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

Updates some of the properties of a managed Cassandra cluster.

```sql
UPDATE azure.cosmosdb.cassandra_clusters
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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
    defaultValue="create_update"
    values={[
        { label: 'create_update', value: 'create_update' }
    ]}
>
<TabItem value="create_update">

Create or update a managed Cassandra cluster. When updating, you must specify all writable properties. To update only some properties, use PATCH.

```sql
REPLACE azure.cosmosdb.cassandra_clusters
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Deletes a managed Cassandra cluster.

```sql
DELETE FROM azure.cosmosdb.cassandra_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="invoke_command"
    values={[
        { label: 'invoke_command', value: 'invoke_command' },
        { label: 'deallocate', value: 'deallocate' },
        { label: 'start', value: 'start' },
        { label: 'status', value: 'status' }
    ]}
>
<TabItem value="invoke_command">

Invoke a command like nodetool for cassandra maintenance.

```sql
EXEC azure.cosmosdb.cassandra_clusters.invoke_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"command": "{{ command }}", 
"arguments": "{{ arguments }}", 
"host": "{{ host }}", 
"cassandra-stop-start": {{ cassandra-stop-start }}, 
"readwrite": {{ readwrite }}
}'
;
```
</TabItem>
<TabItem value="deallocate">

Deallocate the Managed Cassandra Cluster and Associated Data Centers. Deallocation will deallocate the host virtual machine of this cluster, and reserved the data disk. This won't do anything on an already deallocated cluster. Use Start to restart the cluster.

```sql
EXEC azure.cosmosdb.cassandra_clusters.deallocate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@x-ms-force-deallocate='{{ x-ms-force-deallocate }}'
;
```
</TabItem>
<TabItem value="start">

Start the Managed Cassandra Cluster and Associated Data Centers. Start will start the host virtual machine of this cluster with reserved data disk. This won't do anything on an already running cluster. Use Deallocate to deallocate the cluster.

```sql
EXEC azure.cosmosdb.cassandra_clusters.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="status">

Gets the CPU, memory, and disk usage statistics for each Cassandra node in a cluster.

```sql
EXEC azure.cosmosdb.cassandra_clusters.status 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
