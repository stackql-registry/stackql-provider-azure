--- 
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - netapp
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="volumes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volumes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_get_group_id_list_for_ldap_user"
    values={[
        { label: 'list_get_group_id_list_for_ldap_user', value: 'list_get_group_id_list_for_ldap_user' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_get_group_id_list_for_ldap_user">

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
    <td><CopyableCode code="groupIdsForLdapUser" /></td>
    <td><code>array</code></td>
    <td>Group Id list.</td>
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
    <td><CopyableCode code="acceptGrowCapacityPoolForShortTermCloneSplit" /></td>
    <td><code>string</code></td>
    <td>While auto splitting the short term clone volume, if the parent pool does not have enough space to accommodate the volume after split, it will be automatically resized, which will lead to increased billing. To accept capacity pool size auto grow and create a short term clone volume, set the property as accepted. Known values are: "Accepted" and "Declined". (Accepted, Declined)</td>
</tr>
<tr>
    <td><CopyableCode code="actualThroughputMibps" /></td>
    <td><code>number</code></td>
    <td>Actual throughput in MiB/s for auto qosType volumes calculated based on size and serviceLevel.</td>
</tr>
<tr>
    <td><CopyableCode code="avsDataStore" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the volume is enabled for Azure VMware Solution (AVS) datastore purpose. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="backupId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="baremetalTenantId" /></td>
    <td><code>string</code></td>
    <td>Unique Baremetal Tenant Identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="breakthroughMode" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the volume operates in Breakthrough Mode. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="capacityPoolResourceId" /></td>
    <td><code>string</code></td>
    <td>Pool Resource Id used in case of creating a volume through volume group.</td>
</tr>
<tr>
    <td><CopyableCode code="cloneProgress" /></td>
    <td><code>integer</code></td>
    <td>When a volume is being restored from another volume's snapshot, will show the percentage completion of this cloning process. When this value is empty/null there is no cloning process currently happening on this volume. This value will update every 5 minutes during cloning.</td>
</tr>
<tr>
    <td><CopyableCode code="coolAccess" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether Cool Access(tiering) is enabled for the volume.</td>
</tr>
<tr>
    <td><CopyableCode code="coolAccessRetrievalPolicy" /></td>
    <td><code>string</code></td>
    <td>coolAccessRetrievalPolicy determines the data retrieval behavior from the cool tier to standard storage based on the read pattern for cool access enabled volumes. The possible values for this field are: Default - Data will be pulled from cool tier to standard storage on random reads. This policy is the default. OnRead - All client-driven data read is pulled from cool tier to standard storage on both sequential and random reads. Never - No client-driven data is pulled from cool tier to standard storage. Known values are: "Default", "OnRead", and "Never". (Default, OnRead, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="coolAccessTieringPolicy" /></td>
    <td><code>string</code></td>
    <td>coolAccessTieringPolicy determines which cold data blocks are moved to cool tier. The possible values for this field are: Auto - Moves cold user data blocks in both the Snapshot copies and the active file system to the cool tier tier. This policy is the default. SnapshotOnly - Moves user data blocks of the Volume Snapshot copies that are not associated with the active file system to the cool tier. Known values are: "Auto" and "SnapshotOnly". (Auto, SnapshotOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="coolnessPeriod" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days after which data that is not accessed by clients will be tiered.</td>
</tr>
<tr>
    <td><CopyableCode code="creationToken" /></td>
    <td><code>string</code></td>
    <td>A unique file path for the volume. Used when creating mount targets. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataProtection" /></td>
    <td><code>object</code></td>
    <td>DataProtection type volumes include an object containing details of the replication.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStoreResourceId" /></td>
    <td><code>array</code></td>
    <td>Data store resource unique identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultGroupQuotaInKiBs" /></td>
    <td><code>integer</code></td>
    <td>Default group quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultUserQuotaInKiBs" /></td>
    <td><code>integer</code></td>
    <td>Default user quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies .</td>
</tr>
<tr>
    <td><CopyableCode code="deleteBaseSnapshot" /></td>
    <td><code>boolean</code></td>
    <td>If enabled (true) the snapshot the volume was created from will be automatically deleted after the volume create operation has finished. Defaults to false.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveNetworkFeatures" /></td>
    <td><code>string</code></td>
    <td>The effective value of the network features type available to the volume, or current effective state of update. Known values are: "Basic", "Standard", "Basic_Standard", and "Standard_Basic". (Basic, Standard, Basic_Standard, Standard_Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="enableSubvolumes" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether subvolume operations are enabled on the volume. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="encrypted" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the volume is encrypted or not. Only available on volumes created or updated after 2022-01-01.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionKeySource" /></td>
    <td><code>string</code></td>
    <td>Source of key used to encrypt data in volume. Applicable if NetApp account has encryption.keySource = 'Microsoft.KeyVault'. Possible values (case-insensitive) are: 'Microsoft.NetApp, Microsoft.KeyVault'. Known values are: "Microsoft.NetApp" and "Microsoft.KeyVault". (Microsoft.NetApp, Microsoft.KeyVault)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="exportPolicy" /></td>
    <td><code>object</code></td>
    <td>Set of export policy rules.</td>
</tr>
<tr>
    <td><CopyableCode code="fileAccessLogs" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether file access logs are enabled for the volume, based on active diagnostic settings present on the volume. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemId" /></td>
    <td><code>string</code></td>
    <td>Unique FileSystem Identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="inheritedSizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Space shared by short term clone volume with parent volume in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultQuotaEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if default quota is enabled for the volume.</td>
</tr>
<tr>
    <td><CopyableCode code="isLargeVolume" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether volume is a Large Volume or Regular Volume.</td>
</tr>
<tr>
    <td><CopyableCode code="isRestoring" /></td>
    <td><code>boolean</code></td>
    <td>Restoring.</td>
</tr>
<tr>
    <td><CopyableCode code="kerberosEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultPrivateEndpointResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of private endpoint for KeyVault. It must reside in the same VNET as the volume. Only applicable if encryptionKeySource = 'Microsoft.KeyVault'.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Language supported for volume. Known values are: "c.utf-8", "utf8mb4", "ar", "ar.utf-8", "hr", "hr.utf-8", "cs", "cs.utf-8", "da", "da.utf-8", "nl", "nl.utf-8", "en", "en.utf-8", "fi", "fi.utf-8", "fr", "fr.utf-8", "de", "de.utf-8", "he", "he.utf-8", "hu", "hu.utf-8", "it", "it.utf-8", "ja", "ja.utf-8", "ja-v1", "ja-v1.utf-8", "ja-jp.pck", "ja-jp.pck.utf-8", "ja-jp.932", "ja-jp.932.utf-8", "ja-jp.pck-v2", "ja-jp.pck-v2.utf-8", "ko", "ko.utf-8", "no", "no.utf-8", "pl", "pl.utf-8", "pt", "pt.utf-8", "c", "ro", "ro.utf-8", "ru", "ru.utf-8", "zh", "zh.utf-8", "zh.gbk", "zh.gbk.utf-8", "zh-tw.big5", "zh-tw.big5.utf-8", "zh-tw", "zh-tw.utf-8", "sk", "sk.utf-8", "sl", "sl.utf-8", "es", "es.utf-8", "sv", "sv.utf-8", "tr", "tr.utf-8", "en-us", and "en-us.utf-8". (c.utf-8, utf8mb4, ar, ar.utf-8, hr, hr.utf-8, cs, cs.utf-8, da, da.utf-8, nl, nl.utf-8, en, en.utf-8, fi, fi.utf-8, fr, fr.utf-8, de, de.utf-8, he, he.utf-8, hu, hu.utf-8, it, it.utf-8, ja, ja.utf-8, ja-v1, ja-v1.utf-8, ja-jp.pck, ja-jp.pck.utf-8, ja-jp.932, ja-jp.932.utf-8, ja-jp.pck-v2, ja-jp.pck-v2.utf-8, ko, ko.utf-8, no, no.utf-8, pl, pl.utf-8, pt, pt.utf-8, c, ro, ro.utf-8, ru, ru.utf-8, zh, zh.utf-8, zh.gbk, zh.gbk.utf-8, zh-tw.big5, zh-tw.big5.utf-8, zh-tw, zh-tw.utf-8, sk, sk.utf-8, sl, sl.utf-8, es, es.utf-8, sv, sv.utf-8, tr, tr.utf-8, en-us, en-us.utf-8)</td>
</tr>
<tr>
    <td><CopyableCode code="largeVolumeType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the Large Volume. When set to 'LargeVolume', the large volume is created with standard configuration. If it is set to 'ExtraLargeVolume7Dot2PiB', the extra large volume is created with higher capacity limit 7.2PiB with cool access enabled, delivering higher capacity limit with lower costs. Known values are: "LargeVolume" and "PremExtraLargeVolume7Dot2PiB". (LargeVolume, PremExtraLargeVolume7Dot2PiB)</td>
</tr>
<tr>
    <td><CopyableCode code="ldapEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether LDAP is enabled or not for a given NFS volume.</td>
</tr>
<tr>
    <td><CopyableCode code="ldapServerType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of LDAP server for a given NFS volume. Known values are: "ActiveDirectory" and "OpenLDAP". (ActiveDirectory, OpenLDAP)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfFiles" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of files allowed. Needs a service request in order to be changed. Only allowed to be changed if volume quota is more than 4TiB.</td>
</tr>
<tr>
    <td><CopyableCode code="mountTargets" /></td>
    <td><code>array</code></td>
    <td>List of mount targets.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFeatures" /></td>
    <td><code>string</code></td>
    <td>The original value of the network features type available to the volume at the time it was created. Known values are: "Basic", "Standard", "Basic_Standard", and "Standard_Basic". (Basic, Standard, Basic_Standard, Standard_Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSiblingSetId" /></td>
    <td><code>string</code></td>
    <td>Network Sibling Set ID for the the group of volumes sharing networking resources.</td>
</tr>
<tr>
    <td><CopyableCode code="originatingResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the snapshot or backup that the volume is restored from.</td>
</tr>
<tr>
    <td><CopyableCode code="placementRules" /></td>
    <td><code>array</code></td>
    <td>Application specific placement rules for the particular volume.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolTypes" /></td>
    <td><code>array</code></td>
    <td>Set of protocol types, default NFSv3, CIFS for SMB protocol.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedAvailabilityZone" /></td>
    <td><code>string</code></td>
    <td>The availability zone where the volume is provisioned. This refers to the logical availability zone where the volume resides.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Proximity placement group associated with the volume.</td>
</tr>
<tr>
    <td><CopyableCode code="securityStyle" /></td>
    <td><code>string</code></td>
    <td>The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol. Known values are: "ntfs" and "unix". (ntfs, unix)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevel" /></td>
    <td><code>string</code></td>
    <td>The service level of the file system. Known values are: "Standard", "Premium", "Ultra", "StandardZRS", and "Flexible". (Standard, Premium, Ultra, StandardZRS, Flexible)</td>
</tr>
<tr>
    <td><CopyableCode code="smbAccessBasedEnumeration" /></td>
    <td><code>string</code></td>
    <td>Enables access-based enumeration share property for SMB Shares. Only applicable for SMB/DualProtocol volume. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="smbContinuouslyAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Enables continuously available share property for smb volume. Only applicable for SMB volume.</td>
</tr>
<tr>
    <td><CopyableCode code="smbEncryption" /></td>
    <td><code>boolean</code></td>
    <td>Enables encryption for in-flight smb3 data. Only applicable for SMB/DualProtocol volume. To be used with swagger version 2020-08-01 or later.</td>
</tr>
<tr>
    <td><CopyableCode code="smbNonBrowsable" /></td>
    <td><code>string</code></td>
    <td>Enables non-browsable property for SMB Shares. Only applicable for SMB/DualProtocol volume. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotDirectoryVisible" /></td>
    <td><code>boolean</code></td>
    <td>If enabled (true) the volume will contain a read-only snapshot directory which provides access to each of the volume's snapshots (defaults to true).</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="storageToNetworkProximity" /></td>
    <td><code>string</code></td>
    <td>Provides storage to network proximity information for the volume. Known values are: "Default", "T1", "T2", and "AcrossT2". (Default, T1, T2, AcrossT2)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="t2Network" /></td>
    <td><code>string</code></td>
    <td>T2 network information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="throughputMibps" /></td>
    <td><code>number</code></td>
    <td>Maximum throughput in MiB/s that can be achieved by this volume and this will be accepted as input only for manual qosType volume.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unixPermissions" /></td>
    <td><code>string</code></td>
    <td>UNIX permissions for NFS volume accepted in octal 4 digit format. First digit selects the set user ID(4), set group ID (2) and sticky (1) attributes. Second digit selects permission for the owner of the file: read (4), write (2) and execute (1). Third selects permissions for other users in the same group. the fourth for other users not in the group. 0755 - gives read/write/execute permissions to owner and read/execute to group and other users.</td>
</tr>
<tr>
    <td><CopyableCode code="usageThreshold" /></td>
    <td><code>integer</code></td>
    <td>Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. For regular volumes, valid values are in the range 50GiB to 100TiB. For large volumes, valid values are in the range 100TiB to 500TiB, and on an exceptional basis, from to 2400GiB to 2400TiB. For extra large volumes, valid values are in the range 2400GiB to 7200TiB. Values expressed in bytes as multiples of 1 GiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeGroupName" /></td>
    <td><code>string</code></td>
    <td>Volume Group Name.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeSpecName" /></td>
    <td><code>string</code></td>
    <td>Volume spec name is the application specific designation or identifier for the particular volume in a volume group for e.g. data, log.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeType" /></td>
    <td><code>string</code></td>
    <td>What type of volume is this. For destination volumes in Cross Region Replication, set type to DataProtection. For creating clone volume, set type to ShortTermClone.</td>
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
    <td><CopyableCode code="acceptGrowCapacityPoolForShortTermCloneSplit" /></td>
    <td><code>string</code></td>
    <td>While auto splitting the short term clone volume, if the parent pool does not have enough space to accommodate the volume after split, it will be automatically resized, which will lead to increased billing. To accept capacity pool size auto grow and create a short term clone volume, set the property as accepted. Known values are: "Accepted" and "Declined". (Accepted, Declined)</td>
</tr>
<tr>
    <td><CopyableCode code="actualThroughputMibps" /></td>
    <td><code>number</code></td>
    <td>Actual throughput in MiB/s for auto qosType volumes calculated based on size and serviceLevel.</td>
</tr>
<tr>
    <td><CopyableCode code="avsDataStore" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the volume is enabled for Azure VMware Solution (AVS) datastore purpose. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="backupId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="baremetalTenantId" /></td>
    <td><code>string</code></td>
    <td>Unique Baremetal Tenant Identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="breakthroughMode" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the volume operates in Breakthrough Mode. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="capacityPoolResourceId" /></td>
    <td><code>string</code></td>
    <td>Pool Resource Id used in case of creating a volume through volume group.</td>
</tr>
<tr>
    <td><CopyableCode code="cloneProgress" /></td>
    <td><code>integer</code></td>
    <td>When a volume is being restored from another volume's snapshot, will show the percentage completion of this cloning process. When this value is empty/null there is no cloning process currently happening on this volume. This value will update every 5 minutes during cloning.</td>
</tr>
<tr>
    <td><CopyableCode code="coolAccess" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether Cool Access(tiering) is enabled for the volume.</td>
</tr>
<tr>
    <td><CopyableCode code="coolAccessRetrievalPolicy" /></td>
    <td><code>string</code></td>
    <td>coolAccessRetrievalPolicy determines the data retrieval behavior from the cool tier to standard storage based on the read pattern for cool access enabled volumes. The possible values for this field are: Default - Data will be pulled from cool tier to standard storage on random reads. This policy is the default. OnRead - All client-driven data read is pulled from cool tier to standard storage on both sequential and random reads. Never - No client-driven data is pulled from cool tier to standard storage. Known values are: "Default", "OnRead", and "Never". (Default, OnRead, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="coolAccessTieringPolicy" /></td>
    <td><code>string</code></td>
    <td>coolAccessTieringPolicy determines which cold data blocks are moved to cool tier. The possible values for this field are: Auto - Moves cold user data blocks in both the Snapshot copies and the active file system to the cool tier tier. This policy is the default. SnapshotOnly - Moves user data blocks of the Volume Snapshot copies that are not associated with the active file system to the cool tier. Known values are: "Auto" and "SnapshotOnly". (Auto, SnapshotOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="coolnessPeriod" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days after which data that is not accessed by clients will be tiered.</td>
</tr>
<tr>
    <td><CopyableCode code="creationToken" /></td>
    <td><code>string</code></td>
    <td>A unique file path for the volume. Used when creating mount targets. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataProtection" /></td>
    <td><code>object</code></td>
    <td>DataProtection type volumes include an object containing details of the replication.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStoreResourceId" /></td>
    <td><code>array</code></td>
    <td>Data store resource unique identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultGroupQuotaInKiBs" /></td>
    <td><code>integer</code></td>
    <td>Default group quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultUserQuotaInKiBs" /></td>
    <td><code>integer</code></td>
    <td>Default user quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies .</td>
</tr>
<tr>
    <td><CopyableCode code="deleteBaseSnapshot" /></td>
    <td><code>boolean</code></td>
    <td>If enabled (true) the snapshot the volume was created from will be automatically deleted after the volume create operation has finished. Defaults to false.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveNetworkFeatures" /></td>
    <td><code>string</code></td>
    <td>The effective value of the network features type available to the volume, or current effective state of update. Known values are: "Basic", "Standard", "Basic_Standard", and "Standard_Basic". (Basic, Standard, Basic_Standard, Standard_Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="enableSubvolumes" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether subvolume operations are enabled on the volume. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="encrypted" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the volume is encrypted or not. Only available on volumes created or updated after 2022-01-01.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionKeySource" /></td>
    <td><code>string</code></td>
    <td>Source of key used to encrypt data in volume. Applicable if NetApp account has encryption.keySource = 'Microsoft.KeyVault'. Possible values (case-insensitive) are: 'Microsoft.NetApp, Microsoft.KeyVault'. Known values are: "Microsoft.NetApp" and "Microsoft.KeyVault". (Microsoft.NetApp, Microsoft.KeyVault)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="exportPolicy" /></td>
    <td><code>object</code></td>
    <td>Set of export policy rules.</td>
</tr>
<tr>
    <td><CopyableCode code="fileAccessLogs" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether file access logs are enabled for the volume, based on active diagnostic settings present on the volume. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemId" /></td>
    <td><code>string</code></td>
    <td>Unique FileSystem Identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="inheritedSizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Space shared by short term clone volume with parent volume in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultQuotaEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if default quota is enabled for the volume.</td>
</tr>
<tr>
    <td><CopyableCode code="isLargeVolume" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether volume is a Large Volume or Regular Volume.</td>
</tr>
<tr>
    <td><CopyableCode code="isRestoring" /></td>
    <td><code>boolean</code></td>
    <td>Restoring.</td>
</tr>
<tr>
    <td><CopyableCode code="kerberosEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultPrivateEndpointResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of private endpoint for KeyVault. It must reside in the same VNET as the volume. Only applicable if encryptionKeySource = 'Microsoft.KeyVault'.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Language supported for volume. Known values are: "c.utf-8", "utf8mb4", "ar", "ar.utf-8", "hr", "hr.utf-8", "cs", "cs.utf-8", "da", "da.utf-8", "nl", "nl.utf-8", "en", "en.utf-8", "fi", "fi.utf-8", "fr", "fr.utf-8", "de", "de.utf-8", "he", "he.utf-8", "hu", "hu.utf-8", "it", "it.utf-8", "ja", "ja.utf-8", "ja-v1", "ja-v1.utf-8", "ja-jp.pck", "ja-jp.pck.utf-8", "ja-jp.932", "ja-jp.932.utf-8", "ja-jp.pck-v2", "ja-jp.pck-v2.utf-8", "ko", "ko.utf-8", "no", "no.utf-8", "pl", "pl.utf-8", "pt", "pt.utf-8", "c", "ro", "ro.utf-8", "ru", "ru.utf-8", "zh", "zh.utf-8", "zh.gbk", "zh.gbk.utf-8", "zh-tw.big5", "zh-tw.big5.utf-8", "zh-tw", "zh-tw.utf-8", "sk", "sk.utf-8", "sl", "sl.utf-8", "es", "es.utf-8", "sv", "sv.utf-8", "tr", "tr.utf-8", "en-us", and "en-us.utf-8". (c.utf-8, utf8mb4, ar, ar.utf-8, hr, hr.utf-8, cs, cs.utf-8, da, da.utf-8, nl, nl.utf-8, en, en.utf-8, fi, fi.utf-8, fr, fr.utf-8, de, de.utf-8, he, he.utf-8, hu, hu.utf-8, it, it.utf-8, ja, ja.utf-8, ja-v1, ja-v1.utf-8, ja-jp.pck, ja-jp.pck.utf-8, ja-jp.932, ja-jp.932.utf-8, ja-jp.pck-v2, ja-jp.pck-v2.utf-8, ko, ko.utf-8, no, no.utf-8, pl, pl.utf-8, pt, pt.utf-8, c, ro, ro.utf-8, ru, ru.utf-8, zh, zh.utf-8, zh.gbk, zh.gbk.utf-8, zh-tw.big5, zh-tw.big5.utf-8, zh-tw, zh-tw.utf-8, sk, sk.utf-8, sl, sl.utf-8, es, es.utf-8, sv, sv.utf-8, tr, tr.utf-8, en-us, en-us.utf-8)</td>
</tr>
<tr>
    <td><CopyableCode code="largeVolumeType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the Large Volume. When set to 'LargeVolume', the large volume is created with standard configuration. If it is set to 'ExtraLargeVolume7Dot2PiB', the extra large volume is created with higher capacity limit 7.2PiB with cool access enabled, delivering higher capacity limit with lower costs. Known values are: "LargeVolume" and "PremExtraLargeVolume7Dot2PiB". (LargeVolume, PremExtraLargeVolume7Dot2PiB)</td>
</tr>
<tr>
    <td><CopyableCode code="ldapEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether LDAP is enabled or not for a given NFS volume.</td>
</tr>
<tr>
    <td><CopyableCode code="ldapServerType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of LDAP server for a given NFS volume. Known values are: "ActiveDirectory" and "OpenLDAP". (ActiveDirectory, OpenLDAP)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfFiles" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of files allowed. Needs a service request in order to be changed. Only allowed to be changed if volume quota is more than 4TiB.</td>
</tr>
<tr>
    <td><CopyableCode code="mountTargets" /></td>
    <td><code>array</code></td>
    <td>List of mount targets.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFeatures" /></td>
    <td><code>string</code></td>
    <td>The original value of the network features type available to the volume at the time it was created. Known values are: "Basic", "Standard", "Basic_Standard", and "Standard_Basic". (Basic, Standard, Basic_Standard, Standard_Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSiblingSetId" /></td>
    <td><code>string</code></td>
    <td>Network Sibling Set ID for the the group of volumes sharing networking resources.</td>
</tr>
<tr>
    <td><CopyableCode code="originatingResourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the snapshot or backup that the volume is restored from.</td>
</tr>
<tr>
    <td><CopyableCode code="placementRules" /></td>
    <td><code>array</code></td>
    <td>Application specific placement rules for the particular volume.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolTypes" /></td>
    <td><code>array</code></td>
    <td>Set of protocol types, default NFSv3, CIFS for SMB protocol.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedAvailabilityZone" /></td>
    <td><code>string</code></td>
    <td>The availability zone where the volume is provisioned. This refers to the logical availability zone where the volume resides.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Proximity placement group associated with the volume.</td>
</tr>
<tr>
    <td><CopyableCode code="securityStyle" /></td>
    <td><code>string</code></td>
    <td>The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol. Known values are: "ntfs" and "unix". (ntfs, unix)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevel" /></td>
    <td><code>string</code></td>
    <td>The service level of the file system. Known values are: "Standard", "Premium", "Ultra", "StandardZRS", and "Flexible". (Standard, Premium, Ultra, StandardZRS, Flexible)</td>
</tr>
<tr>
    <td><CopyableCode code="smbAccessBasedEnumeration" /></td>
    <td><code>string</code></td>
    <td>Enables access-based enumeration share property for SMB Shares. Only applicable for SMB/DualProtocol volume. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="smbContinuouslyAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Enables continuously available share property for smb volume. Only applicable for SMB volume.</td>
</tr>
<tr>
    <td><CopyableCode code="smbEncryption" /></td>
    <td><code>boolean</code></td>
    <td>Enables encryption for in-flight smb3 data. Only applicable for SMB/DualProtocol volume. To be used with swagger version 2020-08-01 or later.</td>
</tr>
<tr>
    <td><CopyableCode code="smbNonBrowsable" /></td>
    <td><code>string</code></td>
    <td>Enables non-browsable property for SMB Shares. Only applicable for SMB/DualProtocol volume. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotDirectoryVisible" /></td>
    <td><code>boolean</code></td>
    <td>If enabled (true) the volume will contain a read-only snapshot directory which provides access to each of the volume's snapshots (defaults to true).</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="storageToNetworkProximity" /></td>
    <td><code>string</code></td>
    <td>Provides storage to network proximity information for the volume. Known values are: "Default", "T1", "T2", and "AcrossT2". (Default, T1, T2, AcrossT2)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="t2Network" /></td>
    <td><code>string</code></td>
    <td>T2 network information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="throughputMibps" /></td>
    <td><code>number</code></td>
    <td>Maximum throughput in MiB/s that can be achieved by this volume and this will be accepted as input only for manual qosType volume.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unixPermissions" /></td>
    <td><code>string</code></td>
    <td>UNIX permissions for NFS volume accepted in octal 4 digit format. First digit selects the set user ID(4), set group ID (2) and sticky (1) attributes. Second digit selects permission for the owner of the file: read (4), write (2) and execute (1). Third selects permissions for other users in the same group. the fourth for other users not in the group. 0755 - gives read/write/execute permissions to owner and read/execute to group and other users.</td>
</tr>
<tr>
    <td><CopyableCode code="usageThreshold" /></td>
    <td><code>integer</code></td>
    <td>Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. For regular volumes, valid values are in the range 50GiB to 100TiB. For large volumes, valid values are in the range 100TiB to 500TiB, and on an exceptional basis, from to 2400GiB to 2400TiB. For extra large volumes, valid values are in the range 2400GiB to 7200TiB. Values expressed in bytes as multiples of 1 GiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeGroupName" /></td>
    <td><code>string</code></td>
    <td>Volume Group Name.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeSpecName" /></td>
    <td><code>string</code></td>
    <td>Volume spec name is the application specific designation or identifier for the particular volume in a volume group for e.g. data, log.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeType" /></td>
    <td><code>string</code></td>
    <td>What type of volume is this. For destination volumes in Cross Region Replication, set type to DataProtection. For creating clone volume, set type to ShortTermClone.</td>
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
    <td><a href="#list_get_group_id_list_for_ldap_user"><CopyableCode code="list_get_group_id_list_for_ldap_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the list of group Ids for a specific LDAP User.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the details of the specified volume.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all volumes within the capacity pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the specified volume within the capacity pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the specified volume.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the specified volume within the capacity pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDelete"><code>forceDelete</code></a></td>
    <td>Delete the specified volume.</td>
</tr>
<tr>
    <td><a href="#list_replications"><CopyableCode code="list_replications" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all replications for a specified volume.</td>
</tr>
<tr>
    <td><a href="#list_quota_report"><CopyableCode code="list_quota_report" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get quota report for volume (with filter support).</td>
</tr>
<tr>
    <td><a href="#populate_availability_zone"><CopyableCode code="populate_availability_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation will populate availability zone information for a volume.</td>
</tr>
<tr>
    <td><a href="#revert"><CopyableCode code="revert" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revert a volume to the snapshot specified in the body.</td>
</tr>
<tr>
    <td><a href="#reset_cifs_password"><CopyableCode code="reset_cifs_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reset cifs password from volume.</td>
</tr>
<tr>
    <td><a href="#split_clone_from_parent"><CopyableCode code="split_clone_from_parent" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Split operation to convert clone volume to an independent volume.</td>
</tr>
<tr>
    <td><a href="#break_file_locks"><CopyableCode code="break_file_locks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Break all the file locks on a volume.</td>
</tr>
<tr>
    <td><a href="#break_replication"><CopyableCode code="break_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Break the replication connection on the destination volume.</td>
</tr>
<tr>
    <td><a href="#reestablish_replication"><CopyableCode code="reestablish_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Re-establish a previously deleted replication between 2 volumes that have a common ad-hoc or policy-based snapshots.</td>
</tr>
<tr>
    <td><a href="#replication_status"><CopyableCode code="replication_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of the replication.</td>
</tr>
<tr>
    <td><a href="#resync_replication"><CopyableCode code="resync_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from destination to source.</td>
</tr>
<tr>
    <td><a href="#delete_replication"><CopyableCode code="delete_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the replication connection on the destination volume, and send release to the source replication.</td>
</tr>
<tr>
    <td><a href="#authorize_replication"><CopyableCode code="authorize_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Authorize the replication connection on the source volume.</td>
</tr>
<tr>
    <td><a href="#re_initialize_replication"><CopyableCode code="re_initialize_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Re-Initializes the replication connection on the destination volume.</td>
</tr>
<tr>
    <td><a href="#peer_external_cluster"><CopyableCode code="peer_external_cluster" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-peerIpAddresses"><code>peerIpAddresses</code></a></td>
    <td></td>
    <td>Starts peering the external cluster for this migration volume.</td>
</tr>
<tr>
    <td><a href="#authorize_external_replication"><CopyableCode code="authorize_external_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts SVM peering and returns a command to be run on the external ONTAP to accept it. Once the SVM have been peered a SnapMirror will be created.</td>
</tr>
<tr>
    <td><a href="#finalize_external_replication"><CopyableCode code="finalize_external_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Finalizes the migration of an external volume by releasing the replication and breaking the external cluster peering if no other migration is active.</td>
</tr>
<tr>
    <td><a href="#perform_replication_transfer"><CopyableCode code="perform_replication_transfer" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Performs an adhoc replication transfer on a volume with volumeType Migration.</td>
</tr>
<tr>
    <td><a href="#pool_change"><CopyableCode code="pool_change" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-newPoolResourceId"><code>newPoolResourceId</code></a></td>
    <td></td>
    <td>Moves volume to another pool.</td>
</tr>
<tr>
    <td><a href="#relocate"><CopyableCode code="relocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Relocates volume to a new stamp.</td>
</tr>
<tr>
    <td><a href="#finalize_relocation"><CopyableCode code="finalize_relocation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Finalizes the relocation of the volume and cleans up the old volume.</td>
</tr>
<tr>
    <td><a href="#revert_relocation"><CopyableCode code="revert_relocation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reverts the volume relocation process, cleans up the new volume and starts using the former-existing volume.</td>
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
    <td>The name of the NetApp account. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capacity pool. Required.</td>
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
<tr id="parameter-volume_name">
    <td><CopyableCode code="volume_name" /></td>
    <td><code>string</code></td>
    <td>The name of the volume. Required.</td>
</tr>
<tr id="parameter-forceDelete">
    <td><CopyableCode code="forceDelete" /></td>
    <td><code>boolean</code></td>
    <td>An option to force delete the volume. Will cleanup resources connected to the particular volume. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_get_group_id_list_for_ldap_user"
    values={[
        { label: 'list_get_group_id_list_for_ldap_user', value: 'list_get_group_id_list_for_ldap_user' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_get_group_id_list_for_ldap_user">

Returns the list of group Ids for a specific LDAP User.

```sql
SELECT
groupIdsForLdapUser
FROM azure_isv.netapp.volumes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the details of the specified volume.

```sql
SELECT
id,
name,
acceptGrowCapacityPoolForShortTermCloneSplit,
actualThroughputMibps,
avsDataStore,
backupId,
baremetalTenantId,
breakthroughMode,
capacityPoolResourceId,
cloneProgress,
coolAccess,
coolAccessRetrievalPolicy,
coolAccessTieringPolicy,
coolnessPeriod,
creationToken,
dataProtection,
dataStoreResourceId,
defaultGroupQuotaInKiBs,
defaultUserQuotaInKiBs,
deleteBaseSnapshot,
effectiveNetworkFeatures,
enableSubvolumes,
encrypted,
encryptionKeySource,
etag,
exportPolicy,
fileAccessLogs,
fileSystemId,
inheritedSizeInBytes,
isDefaultQuotaEnabled,
isLargeVolume,
isRestoring,
kerberosEnabled,
keyVaultPrivateEndpointResourceId,
language,
largeVolumeType,
ldapEnabled,
ldapServerType,
location,
maximumNumberOfFiles,
mountTargets,
networkFeatures,
networkSiblingSetId,
originatingResourceId,
placementRules,
protocolTypes,
provisionedAvailabilityZone,
provisioningState,
proximityPlacementGroup,
securityStyle,
serviceLevel,
smbAccessBasedEnumeration,
smbContinuouslyAvailable,
smbEncryption,
smbNonBrowsable,
snapshotDirectoryVisible,
snapshotId,
storageToNetworkProximity,
subnetId,
systemData,
t2Network,
tags,
throughputMibps,
type,
unixPermissions,
usageThreshold,
volumeGroupName,
volumeSpecName,
volumeType,
zones
FROM azure_isv.netapp.volumes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all volumes within the capacity pool.

```sql
SELECT
id,
name,
acceptGrowCapacityPoolForShortTermCloneSplit,
actualThroughputMibps,
avsDataStore,
backupId,
baremetalTenantId,
breakthroughMode,
capacityPoolResourceId,
cloneProgress,
coolAccess,
coolAccessRetrievalPolicy,
coolAccessTieringPolicy,
coolnessPeriod,
creationToken,
dataProtection,
dataStoreResourceId,
defaultGroupQuotaInKiBs,
defaultUserQuotaInKiBs,
deleteBaseSnapshot,
effectiveNetworkFeatures,
enableSubvolumes,
encrypted,
encryptionKeySource,
etag,
exportPolicy,
fileAccessLogs,
fileSystemId,
inheritedSizeInBytes,
isDefaultQuotaEnabled,
isLargeVolume,
isRestoring,
kerberosEnabled,
keyVaultPrivateEndpointResourceId,
language,
largeVolumeType,
ldapEnabled,
ldapServerType,
location,
maximumNumberOfFiles,
mountTargets,
networkFeatures,
networkSiblingSetId,
originatingResourceId,
placementRules,
protocolTypes,
provisionedAvailabilityZone,
provisioningState,
proximityPlacementGroup,
securityStyle,
serviceLevel,
smbAccessBasedEnumeration,
smbContinuouslyAvailable,
smbEncryption,
smbNonBrowsable,
snapshotDirectoryVisible,
snapshotId,
storageToNetworkProximity,
subnetId,
systemData,
t2Network,
tags,
throughputMibps,
type,
unixPermissions,
usageThreshold,
volumeGroupName,
volumeSpecName,
volumeType,
zones
FROM azure_isv.netapp.volumes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create or update the specified volume within the capacity pool.

```sql
INSERT INTO azure_isv.netapp.volumes (
tags,
location,
properties,
zones,
resource_group_name,
account_name,
pool_name,
volume_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ zones }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ pool_name }}',
'{{ volume_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: volumes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the volumes resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the volumes resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the volumes resource.
    - name: volume_name
      value: "{{ volume_name }}"
      description: Required parameter for the volumes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the volumes resource.
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
        Volume properties. Required.
      value:
        fileSystemId: "{{ fileSystemId }}"
        creationToken: "{{ creationToken }}"
        serviceLevel: "{{ serviceLevel }}"
        usageThreshold: {{ usageThreshold }}
        exportPolicy:
          rules:
            - ruleIndex: {{ ruleIndex }}
              unixReadOnly: {{ unixReadOnly }}
              unixReadWrite: {{ unixReadWrite }}
              kerberos5ReadOnly: {{ kerberos5ReadOnly }}
              kerberos5ReadWrite: {{ kerberos5ReadWrite }}
              kerberos5iReadOnly: {{ kerberos5iReadOnly }}
              kerberos5iReadWrite: {{ kerberos5iReadWrite }}
              kerberos5pReadOnly: {{ kerberos5pReadOnly }}
              kerberos5pReadWrite: {{ kerberos5pReadWrite }}
              cifs: {{ cifs }}
              nfsv3: {{ nfsv3 }}
              nfsv41: {{ nfsv41 }}
              allowedClients: "{{ allowedClients }}"
              hasRootAccess: {{ hasRootAccess }}
              chownMode: "{{ chownMode }}"
        protocolTypes:
          - "{{ protocolTypes }}"
        provisioningState: "{{ provisioningState }}"
        snapshotId: "{{ snapshotId }}"
        deleteBaseSnapshot: {{ deleteBaseSnapshot }}
        backupId: "{{ backupId }}"
        baremetalTenantId: "{{ baremetalTenantId }}"
        subnetId: "{{ subnetId }}"
        networkFeatures: "{{ networkFeatures }}"
        effectiveNetworkFeatures: "{{ effectiveNetworkFeatures }}"
        networkSiblingSetId: "{{ networkSiblingSetId }}"
        storageToNetworkProximity: "{{ storageToNetworkProximity }}"
        mountTargets:
          - mountTargetId: "{{ mountTargetId }}"
            fileSystemId: "{{ fileSystemId }}"
            ipAddress: "{{ ipAddress }}"
            smbServerFqdn: "{{ smbServerFqdn }}"
        volumeType: "{{ volumeType }}"
        dataProtection:
          backup:
            backupPolicyId: "{{ backupPolicyId }}"
            policyEnforced: {{ policyEnforced }}
            backupVaultId: "{{ backupVaultId }}"
          replication:
            replicationId: "{{ replicationId }}"
            endpointType: "{{ endpointType }}"
            replicationSchedule: "{{ replicationSchedule }}"
            remoteVolumeResourceId: "{{ remoteVolumeResourceId }}"
            remotePath:
              externalHostName: "{{ externalHostName }}"
              serverName: "{{ serverName }}"
              volumeName: "{{ volumeName }}"
            remoteVolumeRegion: "{{ remoteVolumeRegion }}"
            destinationReplications:
              - resourceId: "{{ resourceId }}"
                replicationType: "{{ replicationType }}"
                region: "{{ region }}"
                zone: "{{ zone }}"
            externalReplicationSetupStatus: "{{ externalReplicationSetupStatus }}"
            externalReplicationSetupInfo: "{{ externalReplicationSetupInfo }}"
            mirrorState: "{{ mirrorState }}"
            relationshipStatus: "{{ relationshipStatus }}"
          snapshot:
            snapshotPolicyId: "{{ snapshotPolicyId }}"
          volumeRelocation:
            relocationRequested: {{ relocationRequested }}
            readyToBeFinalized: {{ readyToBeFinalized }}
          ransomwareProtection:
            desiredRansomwareProtectionState: "{{ desiredRansomwareProtectionState }}"
            actualRansomwareProtectionState: "{{ actualRansomwareProtectionState }}"
        acceptGrowCapacityPoolForShortTermCloneSplit: "{{ acceptGrowCapacityPoolForShortTermCloneSplit }}"
        isRestoring: {{ isRestoring }}
        snapshotDirectoryVisible: {{ snapshotDirectoryVisible }}
        kerberosEnabled: {{ kerberosEnabled }}
        securityStyle: "{{ securityStyle }}"
        smbEncryption: {{ smbEncryption }}
        smbAccessBasedEnumeration: "{{ smbAccessBasedEnumeration }}"
        smbNonBrowsable: "{{ smbNonBrowsable }}"
        smbContinuouslyAvailable: {{ smbContinuouslyAvailable }}
        throughputMibps: {{ throughputMibps }}
        actualThroughputMibps: {{ actualThroughputMibps }}
        encryptionKeySource: "{{ encryptionKeySource }}"
        keyVaultPrivateEndpointResourceId: "{{ keyVaultPrivateEndpointResourceId }}"
        ldapEnabled: {{ ldapEnabled }}
        ldapServerType: "{{ ldapServerType }}"
        coolAccess: {{ coolAccess }}
        coolnessPeriod: {{ coolnessPeriod }}
        coolAccessRetrievalPolicy: "{{ coolAccessRetrievalPolicy }}"
        coolAccessTieringPolicy: "{{ coolAccessTieringPolicy }}"
        unixPermissions: "{{ unixPermissions }}"
        cloneProgress: {{ cloneProgress }}
        fileAccessLogs: "{{ fileAccessLogs }}"
        avsDataStore: "{{ avsDataStore }}"
        dataStoreResourceId:
          - "{{ dataStoreResourceId }}"
        isDefaultQuotaEnabled: {{ isDefaultQuotaEnabled }}
        defaultUserQuotaInKiBs: {{ defaultUserQuotaInKiBs }}
        defaultGroupQuotaInKiBs: {{ defaultGroupQuotaInKiBs }}
        maximumNumberOfFiles: {{ maximumNumberOfFiles }}
        volumeGroupName: "{{ volumeGroupName }}"
        capacityPoolResourceId: "{{ capacityPoolResourceId }}"
        proximityPlacementGroup: "{{ proximityPlacementGroup }}"
        t2Network: "{{ t2Network }}"
        volumeSpecName: "{{ volumeSpecName }}"
        encrypted: {{ encrypted }}
        placementRules:
          - key: "{{ key }}"
            value: "{{ value }}"
        enableSubvolumes: "{{ enableSubvolumes }}"
        provisionedAvailabilityZone: "{{ provisionedAvailabilityZone }}"
        isLargeVolume: {{ isLargeVolume }}
        largeVolumeType: "{{ largeVolumeType }}"
        originatingResourceId: "{{ originatingResourceId }}"
        inheritedSizeInBytes: {{ inheritedSizeInBytes }}
        language: "{{ language }}"
        breakthroughMode: "{{ breakthroughMode }}"
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

Patch the specified volume.

```sql
UPDATE azure_isv.netapp.volumes
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Create or update the specified volume within the capacity pool.

```sql
REPLACE azure_isv.netapp.volumes
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
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

Delete the specified volume.

```sql
DELETE FROM azure_isv.netapp.volumes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDelete = '{{ forceDelete }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_replications"
    values={[
        { label: 'list_replications', value: 'list_replications' },
        { label: 'list_quota_report', value: 'list_quota_report' },
        { label: 'populate_availability_zone', value: 'populate_availability_zone' },
        { label: 'revert', value: 'revert' },
        { label: 'reset_cifs_password', value: 'reset_cifs_password' },
        { label: 'split_clone_from_parent', value: 'split_clone_from_parent' },
        { label: 'break_file_locks', value: 'break_file_locks' },
        { label: 'break_replication', value: 'break_replication' },
        { label: 'reestablish_replication', value: 'reestablish_replication' },
        { label: 'replication_status', value: 'replication_status' },
        { label: 'resync_replication', value: 'resync_replication' },
        { label: 'delete_replication', value: 'delete_replication' },
        { label: 'authorize_replication', value: 'authorize_replication' },
        { label: 're_initialize_replication', value: 're_initialize_replication' },
        { label: 'peer_external_cluster', value: 'peer_external_cluster' },
        { label: 'authorize_external_replication', value: 'authorize_external_replication' },
        { label: 'finalize_external_replication', value: 'finalize_external_replication' },
        { label: 'perform_replication_transfer', value: 'perform_replication_transfer' },
        { label: 'pool_change', value: 'pool_change' },
        { label: 'relocate', value: 'relocate' },
        { label: 'finalize_relocation', value: 'finalize_relocation' },
        { label: 'revert_relocation', value: 'revert_relocation' }
    ]}
>
<TabItem value="list_replications">

List all replications for a specified volume.

```sql
EXEC azure_isv.netapp.volumes.list_replications 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"exclude": "{{ exclude }}"
}'
;
```
</TabItem>
<TabItem value="list_quota_report">

Get quota report for volume (with filter support).

```sql
EXEC azure_isv.netapp.volumes.list_quota_report 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"quotaType": "{{ quotaType }}", 
"quotaTarget": "{{ quotaTarget }}", 
"usageThresholdPercentage": {{ usageThresholdPercentage }}
}'
;
```
</TabItem>
<TabItem value="populate_availability_zone">

This operation will populate availability zone information for a volume.

```sql
EXEC azure_isv.netapp.volumes.populate_availability_zone 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="revert">

Revert a volume to the snapshot specified in the body.

```sql
EXEC azure_isv.netapp.volumes.revert 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"snapshotId": "{{ snapshotId }}"
}'
;
```
</TabItem>
<TabItem value="reset_cifs_password">

Reset cifs password from volume.

```sql
EXEC azure_isv.netapp.volumes.reset_cifs_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="split_clone_from_parent">

Split operation to convert clone volume to an independent volume.

```sql
EXEC azure_isv.netapp.volumes.split_clone_from_parent 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="break_file_locks">

Break all the file locks on a volume.

```sql
EXEC azure_isv.netapp.volumes.break_file_locks 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"clientIp": "{{ clientIp }}", 
"confirmRunningDisruptiveOperation": {{ confirmRunningDisruptiveOperation }}
}'
;
```
</TabItem>
<TabItem value="break_replication">

Break the replication connection on the destination volume.

```sql
EXEC azure_isv.netapp.volumes.break_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"forceBreakReplication": {{ forceBreakReplication }}
}'
;
```
</TabItem>
<TabItem value="reestablish_replication">

Re-establish a previously deleted replication between 2 volumes that have a common ad-hoc or policy-based snapshots.

```sql
EXEC azure_isv.netapp.volumes.reestablish_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sourceVolumeId": "{{ sourceVolumeId }}"
}'
;
```
</TabItem>
<TabItem value="replication_status">

Get the status of the replication.

```sql
EXEC azure_isv.netapp.volumes.replication_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resync_replication">

Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from destination to source.

```sql
EXEC azure_isv.netapp.volumes.resync_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_replication">

Delete the replication connection on the destination volume, and send release to the source replication.

```sql
EXEC azure_isv.netapp.volumes.delete_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="authorize_replication">

Authorize the replication connection on the source volume.

```sql
EXEC azure_isv.netapp.volumes.authorize_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"remoteVolumeResourceId": "{{ remoteVolumeResourceId }}"
}'
;
```
</TabItem>
<TabItem value="re_initialize_replication">

Re-Initializes the replication connection on the destination volume.

```sql
EXEC azure_isv.netapp.volumes.re_initialize_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="peer_external_cluster">

Starts peering the external cluster for this migration volume.

```sql
EXEC azure_isv.netapp.volumes.peer_external_cluster 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"peerIpAddresses": "{{ peerIpAddresses }}"
}'
;
```
</TabItem>
<TabItem value="authorize_external_replication">

Starts SVM peering and returns a command to be run on the external ONTAP to accept it. Once the SVM have been peered a SnapMirror will be created.

```sql
EXEC azure_isv.netapp.volumes.authorize_external_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="finalize_external_replication">

Finalizes the migration of an external volume by releasing the replication and breaking the external cluster peering if no other migration is active.

```sql
EXEC azure_isv.netapp.volumes.finalize_external_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="perform_replication_transfer">

Performs an adhoc replication transfer on a volume with volumeType Migration.

```sql
EXEC azure_isv.netapp.volumes.perform_replication_transfer 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="pool_change">

Moves volume to another pool.

```sql
EXEC azure_isv.netapp.volumes.pool_change 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"newPoolResourceId": "{{ newPoolResourceId }}"
}'
;
```
</TabItem>
<TabItem value="relocate">

Relocates volume to a new stamp.

```sql
EXEC azure_isv.netapp.volumes.relocate 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"creationToken": "{{ creationToken }}"
}'
;
```
</TabItem>
<TabItem value="finalize_relocation">

Finalizes the relocation of the volume and cleans up the old volume.

```sql
EXEC azure_isv.netapp.volumes.finalize_relocation 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="revert_relocation">

Reverts the volume relocation process, cleans up the new volume and starts using the former-existing volume.

```sql
EXEC azure_isv.netapp.volumes.revert_relocation 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
