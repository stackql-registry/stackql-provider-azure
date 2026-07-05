--- 
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
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

Creates, updates, deletes, gets or lists a <code>volume_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="volume_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volume_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_net_app_account', value: 'list_by_net_app_account' }
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
    <td><CopyableCode code="groupMetaData" /></td>
    <td><code>object</code></td>
    <td>Volume group details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>List of volumes from group.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_net_app_account">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="groupMetaData" /></td>
    <td><code>object</code></td>
    <td>Volume group details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get details of the specified volume group.</td>
</tr>
<tr>
    <td><a href="#list_by_net_app_account"><CopyableCode code="list_by_net_app_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all volume groups for given account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a volume group along with specified volumes.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the specified volume group only if there are no volumes under volume group.</td>
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
<tr id="parameter-volume_group_name">
    <td><CopyableCode code="volume_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the volumeGroup. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_net_app_account', value: 'list_by_net_app_account' }
    ]}
>
<TabItem value="get">

Get details of the specified volume group.

```sql
SELECT
id,
name,
groupMetaData,
location,
provisioningState,
systemData,
type,
volumes
FROM azure_isv.netapp.volume_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND volume_group_name = '{{ volume_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_net_app_account">

List all volume groups for given account.

```sql
SELECT
id,
name,
groupMetaData,
location,
provisioningState,
type
FROM azure_isv.netapp.volume_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a volume group along with specified volumes.

```sql
INSERT INTO azure_isv.netapp.volume_groups (
properties,
location,
resource_group_name,
account_name,
volume_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ volume_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: volume_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the volume_groups resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the volume_groups resource.
    - name: volume_group_name
      value: "{{ volume_group_name }}"
      description: Required parameter for the volume_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the volume_groups resource.
    - name: properties
      description: |
        Volume group properties.
      value:
        provisioningState: "{{ provisioningState }}"
        groupMetaData:
          groupDescription: "{{ groupDescription }}"
          applicationType: "{{ applicationType }}"
          applicationIdentifier: "{{ applicationIdentifier }}"
          globalPlacementRules:
            - key: "{{ key }}"
              value: "{{ value }}"
          volumesCount: {{ volumesCount }}
        volumes:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            tags: "{{ tags }}"
            zones: "{{ zones }}"
            properties:
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
                  remotePath: "{{ remotePath }}"
                  remoteVolumeRegion: "{{ remoteVolumeRegion }}"
                  destinationReplications: "{{ destinationReplications }}"
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
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
`}</CodeBlock>

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

Delete the specified volume group only if there are no volumes under volume group.

```sql
DELETE FROM azure_isv.netapp.volume_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND volume_group_name = '{{ volume_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
