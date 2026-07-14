--- 
title: caches
hide_title: false
hide_table_of_contents: false
keywords:
  - caches
  - netapp
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

Creates, updates, deletes, gets or lists a <code>caches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="caches" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.caches" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="actualThroughputMibps" /></td>
    <td><code>number</code></td>
    <td>Actual throughput in MiB/s for auto qosType volumes calculated based on size and serviceLevel.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheState" /></td>
    <td><code>string</code></td>
    <td>Azure NetApp Files Cache lifecycle management. Known values are: "ClusterPeeringOfferSent", "VserverPeeringOfferSent", "Creating", "Succeeded", and "Failed". (ClusterPeeringOfferSent, VserverPeeringOfferSent, Creating, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="cacheSubnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated cache subnet that will be used to allocate data IPs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cifsChangeNotifications" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether a CIFS change notification is enabled for the cache. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>string</code></td>
    <td>Specifies if the cache is encryption or not. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionKeySource" /></td>
    <td><code>string</code></td>
    <td>Source of key used to encrypt data in the cache. Applicable if NetApp account has encryption.keySource = 'Microsoft.KeyVault'. Possible values (case-insensitive) are: 'Microsoft.NetApp, Microsoft.KeyVault'. Required. Known values are: "Microsoft.NetApp" and "Microsoft.KeyVault". (Microsoft.NetApp, Microsoft.KeyVault)</td>
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
    <td>Flag indicating whether file access logs are enabled for the Cache, based on active diagnostic settings present on the Cache. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>The file path of the Cache. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="globalFileLocking" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether the global file lock is enabled for the cache. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="kerberos" /></td>
    <td><code>string</code></td>
    <td>Describe if a cache is Kerberos enabled. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
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
    <td><CopyableCode code="ldap" /></td>
    <td><code>string</code></td>
    <td>Specifies whether LDAP is enabled or not for flexcache volume. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="ldapServerType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of LDAP server for flexcache volume. Known values are: "ActiveDirectory" and "OpenLDAP". (ActiveDirectory, OpenLDAP)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfFiles" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of files allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="mountTargets" /></td>
    <td><code>array</code></td>
    <td>List of mount targets that can be used to mount this cache.</td>
</tr>
<tr>
    <td><CopyableCode code="originClusterInformation" /></td>
    <td><code>object</code></td>
    <td>Origin cluster information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringSubnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated subnet that will be used for ANF Intercluster Interface IP addresses. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolTypes" /></td>
    <td><code>array</code></td>
    <td>Set of supported protocol types, which include NFSv3, NFSv4 and SMB protocol.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Creating", "Updating", "Deleting", "Failed", "Succeeded", and "Canceled". (Creating, Updating, Deleting, Failed, Succeeded, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Maximum storage quota allowed for a file system in bytes. Valid values are in the range 50GiB to 1PiB. Values expressed in bytes as multiples of 1GiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="smbSettings" /></td>
    <td><code>object</code></td>
    <td>SMB information for the cache.</td>
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
    <td><CopyableCode code="throughputMibps" /></td>
    <td><code>number</code></td>
    <td>Maximum throughput in MiB/s that can be achieved by this cache volume and this will be accepted as input only for manual qosType cache.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="writeBack" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether writeback is enabled for the cache. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
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
    <td><CopyableCode code="actualThroughputMibps" /></td>
    <td><code>number</code></td>
    <td>Actual throughput in MiB/s for auto qosType volumes calculated based on size and serviceLevel.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheState" /></td>
    <td><code>string</code></td>
    <td>Azure NetApp Files Cache lifecycle management. Known values are: "ClusterPeeringOfferSent", "VserverPeeringOfferSent", "Creating", "Succeeded", and "Failed". (ClusterPeeringOfferSent, VserverPeeringOfferSent, Creating, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="cacheSubnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated cache subnet that will be used to allocate data IPs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cifsChangeNotifications" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether a CIFS change notification is enabled for the cache. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>string</code></td>
    <td>Specifies if the cache is encryption or not. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionKeySource" /></td>
    <td><code>string</code></td>
    <td>Source of key used to encrypt data in the cache. Applicable if NetApp account has encryption.keySource = 'Microsoft.KeyVault'. Possible values (case-insensitive) are: 'Microsoft.NetApp, Microsoft.KeyVault'. Required. Known values are: "Microsoft.NetApp" and "Microsoft.KeyVault". (Microsoft.NetApp, Microsoft.KeyVault)</td>
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
    <td>Flag indicating whether file access logs are enabled for the Cache, based on active diagnostic settings present on the Cache. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>The file path of the Cache. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="globalFileLocking" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether the global file lock is enabled for the cache. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="kerberos" /></td>
    <td><code>string</code></td>
    <td>Describe if a cache is Kerberos enabled. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
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
    <td><CopyableCode code="ldap" /></td>
    <td><code>string</code></td>
    <td>Specifies whether LDAP is enabled or not for flexcache volume. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="ldapServerType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of LDAP server for flexcache volume. Known values are: "ActiveDirectory" and "OpenLDAP". (ActiveDirectory, OpenLDAP)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfFiles" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of files allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="mountTargets" /></td>
    <td><code>array</code></td>
    <td>List of mount targets that can be used to mount this cache.</td>
</tr>
<tr>
    <td><CopyableCode code="originClusterInformation" /></td>
    <td><code>object</code></td>
    <td>Origin cluster information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringSubnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated subnet that will be used for ANF Intercluster Interface IP addresses. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolTypes" /></td>
    <td><code>array</code></td>
    <td>Set of supported protocol types, which include NFSv3, NFSv4 and SMB protocol.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Creating", "Updating", "Deleting", "Failed", "Succeeded", and "Canceled". (Creating, Updating, Deleting, Failed, Succeeded, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Maximum storage quota allowed for a file system in bytes. Valid values are in the range 50GiB to 1PiB. Values expressed in bytes as multiples of 1GiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="smbSettings" /></td>
    <td><code>object</code></td>
    <td>SMB information for the cache.</td>
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
    <td><CopyableCode code="throughputMibps" /></td>
    <td><code>number</code></td>
    <td>Maximum throughput in MiB/s that can be achieved by this cache volume and this will be accepted as input only for manual qosType cache.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="writeBack" /></td>
    <td><code>string</code></td>
    <td>Flag indicating whether writeback is enabled for the cache. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the details of the specified Cache.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Caches within the Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the specified Cache within the Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the specified Cache.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the specified Cache within the Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the specified cache.</td>
</tr>
<tr>
    <td><a href="#list_peering_passphrases"><CopyableCode code="list_peering_passphrases" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation will list the cluster peering command, cluster peering passphrase and the vserver peering command.</td>
</tr>
<tr>
    <td><a href="#pool_change"><CopyableCode code="pool_change" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-newPoolResourceId"><code>newPoolResourceId</code></a></td>
    <td></td>
    <td>Moves Cache to another Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#reset_smb_password"><CopyableCode code="reset_smb_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets the SMB password for the cache.</td>
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
<tr id="parameter-cache_name">
    <td><CopyableCode code="cache_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cache resource. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the details of the specified Cache.

```sql
SELECT
id,
name,
actualThroughputMibps,
cacheState,
cacheSubnetResourceId,
cifsChangeNotifications,
encryption,
encryptionKeySource,
etag,
exportPolicy,
fileAccessLogs,
filePath,
globalFileLocking,
kerberos,
keyVaultPrivateEndpointResourceId,
language,
ldap,
ldapServerType,
location,
maximumNumberOfFiles,
mountTargets,
originClusterInformation,
peeringSubnetResourceId,
protocolTypes,
provisioningState,
size,
smbSettings,
systemData,
tags,
throughputMibps,
type,
writeBack,
zones
FROM azure.netapp.caches
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND cache_name = '{{ cache_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Caches within the Capacity Pool.

```sql
SELECT
id,
name,
actualThroughputMibps,
cacheState,
cacheSubnetResourceId,
cifsChangeNotifications,
encryption,
encryptionKeySource,
etag,
exportPolicy,
fileAccessLogs,
filePath,
globalFileLocking,
kerberos,
keyVaultPrivateEndpointResourceId,
language,
ldap,
ldapServerType,
location,
maximumNumberOfFiles,
mountTargets,
originClusterInformation,
peeringSubnetResourceId,
protocolTypes,
provisioningState,
size,
smbSettings,
systemData,
tags,
throughputMibps,
type,
writeBack,
zones
FROM azure.netapp.caches
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

Create or update the specified Cache within the Capacity Pool.

```sql
INSERT INTO azure.netapp.caches (
tags,
location,
properties,
zones,
resource_group_name,
account_name,
pool_name,
cache_name,
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
'{{ cache_name }}',
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
- name: caches
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the caches resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the caches resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the caches resource.
    - name: cache_name
      value: "{{ cache_name }}"
      description: Required parameter for the caches resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the caches resource.
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
        Cache properties. Required.
      value:
        filePath: "{{ filePath }}"
        size: {{ size }}
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
        cacheState: "{{ cacheState }}"
        cacheSubnetResourceId: "{{ cacheSubnetResourceId }}"
        peeringSubnetResourceId: "{{ peeringSubnetResourceId }}"
        mountTargets:
          - mountTargetId: "{{ mountTargetId }}"
            ipAddress: "{{ ipAddress }}"
            smbServerFqdn: "{{ smbServerFqdn }}"
        kerberos: "{{ kerberos }}"
        smbSettings:
          smbEncryption: "{{ smbEncryption }}"
          smbAccessBasedEnumeration: "{{ smbAccessBasedEnumeration }}"
          smbNonBrowsable: "{{ smbNonBrowsable }}"
        throughputMibps: {{ throughputMibps }}
        actualThroughputMibps: {{ actualThroughputMibps }}
        encryptionKeySource: "{{ encryptionKeySource }}"
        keyVaultPrivateEndpointResourceId: "{{ keyVaultPrivateEndpointResourceId }}"
        maximumNumberOfFiles: {{ maximumNumberOfFiles }}
        encryption: "{{ encryption }}"
        language: "{{ language }}"
        ldap: "{{ ldap }}"
        ldapServerType: "{{ ldapServerType }}"
        originClusterInformation:
          peerClusterName: "{{ peerClusterName }}"
          peerAddresses:
            - "{{ peerAddresses }}"
          peerVserverName: "{{ peerVserverName }}"
          peerVolumeName: "{{ peerVolumeName }}"
        cifsChangeNotifications: "{{ cifsChangeNotifications }}"
        globalFileLocking: "{{ globalFileLocking }}"
        writeBack: "{{ writeBack }}"
        fileAccessLogs: "{{ fileAccessLogs }}"
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

Patch the specified Cache.

```sql
UPDATE azure.netapp.caches
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND cache_name = '{{ cache_name }}' --required
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

Create or update the specified Cache within the Capacity Pool.

```sql
REPLACE azure.netapp.caches
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND cache_name = '{{ cache_name }}' --required
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

Delete the specified cache.

```sql
DELETE FROM azure.netapp.caches
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_peering_passphrases"
    values={[
        { label: 'list_peering_passphrases', value: 'list_peering_passphrases' },
        { label: 'pool_change', value: 'pool_change' },
        { label: 'reset_smb_password', value: 'reset_smb_password' }
    ]}
>
<TabItem value="list_peering_passphrases">

This operation will list the cluster peering command, cluster peering passphrase and the vserver peering command.

```sql
EXEC azure.netapp.caches.list_peering_passphrases 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="pool_change">

Moves Cache to another Capacity Pool.

```sql
EXEC azure.netapp.caches.pool_change 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"newPoolResourceId": "{{ newPoolResourceId }}"
}'
;
```
</TabItem>
<TabItem value="reset_smb_password">

Resets the SMB password for the cache.

```sql
EXEC azure.netapp.caches.reset_smb_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
