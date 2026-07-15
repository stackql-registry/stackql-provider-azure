--- 
title: auto_upgrade_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_upgrade_profiles
  - container_service_fleet
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

Creates, updates, deletes, gets or lists an <code>auto_upgrade_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="auto_upgrade_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service_fleet.auto_upgrade_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_fleet', value: 'list_by_fleet' }
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
    <td><CopyableCode code="autoUpgradeProfileStatus" /></td>
    <td><code>object</code></td>
    <td>The status of the auto upgrade profile.</td>
</tr>
<tr>
    <td><CopyableCode code="channel" /></td>
    <td><code>string</code></td>
    <td>Configures how auto-upgrade will be run. Required. Known values are: "Stable", "Rapid", "NodeImage", and "TargetKubernetesVersion". (Stable, Rapid, NodeImage, TargetKubernetesVersion)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>If set to False: the auto upgrade has effect - target managed clusters will be upgraded on schedule. If set to True: the auto upgrade has no effect - no upgrade will be run on the target managed clusters. This is a boolean and not an enum because enabled/disabled are all available states of the auto upgrade profile. By default, this is set to False.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermSupport" /></td>
    <td><code>boolean</code></td>
    <td>If upgrade channel is not TargetKubernetesVersion, this field must be False. If set to True: Fleet auto upgrade will continue generate update runs for patches of minor versions earlier than N-2 (where N is the latest supported minor version) if those minor versions support Long-Term Support (LTS). By default, this is set to False. For more information on AKS LTS, please see `https://learn.microsoft.com/en-us/azure/aks/long-term-support `_.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageSelection" /></td>
    <td><code>object</code></td>
    <td>The node image upgrade to be applied to the target clusters in auto upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the AutoUpgradeProfile resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>This is the target Kubernetes version for auto-upgrade. The format must be `&#123;major version&#125;.&#123;minor version&#125;`. For example, "1.30". By default, this is empty. If upgrade channel is set to TargetKubernetesVersion, this field must not be empty. If upgrade channel is Rapid, Stable or NodeImage, this field must be empty.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateStrategyId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the UpdateStrategy resource to reference. If not specified, the auto upgrade will run on all clusters which are members of the fleet.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_fleet">

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
    <td><CopyableCode code="autoUpgradeProfileStatus" /></td>
    <td><code>object</code></td>
    <td>The status of the auto upgrade profile.</td>
</tr>
<tr>
    <td><CopyableCode code="channel" /></td>
    <td><code>string</code></td>
    <td>Configures how auto-upgrade will be run. Required. Known values are: "Stable", "Rapid", "NodeImage", and "TargetKubernetesVersion". (Stable, Rapid, NodeImage, TargetKubernetesVersion)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>If set to False: the auto upgrade has effect - target managed clusters will be upgraded on schedule. If set to True: the auto upgrade has no effect - no upgrade will be run on the target managed clusters. This is a boolean and not an enum because enabled/disabled are all available states of the auto upgrade profile. By default, this is set to False.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermSupport" /></td>
    <td><code>boolean</code></td>
    <td>If upgrade channel is not TargetKubernetesVersion, this field must be False. If set to True: Fleet auto upgrade will continue generate update runs for patches of minor versions earlier than N-2 (where N is the latest supported minor version) if those minor versions support Long-Term Support (LTS). By default, this is set to False. For more information on AKS LTS, please see `https://learn.microsoft.com/en-us/azure/aks/long-term-support `_.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageSelection" /></td>
    <td><code>object</code></td>
    <td>The node image upgrade to be applied to the target clusters in auto upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the AutoUpgradeProfile resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>This is the target Kubernetes version for auto-upgrade. The format must be `&#123;major version&#125;.&#123;minor version&#125;`. For example, "1.30". By default, this is empty. If upgrade channel is set to TargetKubernetesVersion, this field must not be empty. If upgrade channel is Rapid, Stable or NodeImage, this field must be empty.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateStrategyId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the UpdateStrategy resource to reference. If not specified, the auto upgrade will run on all clusters which are members of the fleet.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-auto_upgrade_profile_name"><code>auto_upgrade_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AutoUpgradeProfile.</td>
</tr>
<tr>
    <td><a href="#list_by_fleet"><CopyableCode code="list_by_fleet" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List AutoUpgradeProfile resources by Fleet.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-auto_upgrade_profile_name"><code>auto_upgrade_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a AutoUpgradeProfile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-auto_upgrade_profile_name"><code>auto_upgrade_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a AutoUpgradeProfile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-auto_upgrade_profile_name"><code>auto_upgrade_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a AutoUpgradeProfile.</td>
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
<tr id="parameter-auto_upgrade_profile_name">
    <td><CopyableCode code="auto_upgrade_profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the AutoUpgradeProfile resource. Required.</td>
</tr>
<tr id="parameter-fleet_name">
    <td><CopyableCode code="fleet_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Fleet resource. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The page-continuation token to use with a paged version of this API. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_fleet', value: 'list_by_fleet' }
    ]}
>
<TabItem value="get">

Get a AutoUpgradeProfile.

```sql
SELECT
id,
name,
autoUpgradeProfileStatus,
channel,
disabled,
eTag,
longTermSupport,
nodeImageSelection,
provisioningState,
systemData,
targetKubernetesVersion,
type,
updateStrategyId
FROM azure.container_service_fleet.auto_upgrade_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fleet_name = '{{ fleet_name }}' -- required
AND auto_upgrade_profile_name = '{{ auto_upgrade_profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_fleet">

List AutoUpgradeProfile resources by Fleet.

```sql
SELECT
id,
name,
autoUpgradeProfileStatus,
channel,
disabled,
eTag,
longTermSupport,
nodeImageSelection,
provisioningState,
systemData,
targetKubernetesVersion,
type,
updateStrategyId
FROM azure.container_service_fleet.auto_upgrade_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fleet_name = '{{ fleet_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Create a AutoUpgradeProfile.

```sql
INSERT INTO azure.container_service_fleet.auto_upgrade_profiles (
properties,
resource_group_name,
fleet_name,
auto_upgrade_profile_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ fleet_name }}',
'{{ auto_upgrade_profile_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: auto_upgrade_profiles
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the auto_upgrade_profiles resource.
    - name: fleet_name
      value: "{{ fleet_name }}"
      description: Required parameter for the auto_upgrade_profiles resource.
    - name: auto_upgrade_profile_name
      value: "{{ auto_upgrade_profile_name }}"
      description: Required parameter for the auto_upgrade_profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the auto_upgrade_profiles resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        updateStrategyId: "{{ updateStrategyId }}"
        channel: "{{ channel }}"
        nodeImageSelection:
          type: "{{ type }}"
        disabled: {{ disabled }}
        autoUpgradeProfileStatus:
          lastTriggeredAt: "{{ lastTriggeredAt }}"
          lastTriggerStatus: "{{ lastTriggerStatus }}"
          lastTriggerError:
            code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                target: "{{ target }}"
                details: "{{ details }}"
                additionalInfo: "{{ additionalInfo }}"
            additionalInfo:
              - type: "{{ type }}"
                info: "{{ info }}"
          lastTriggerUpgradeVersions:
            - "{{ lastTriggerUpgradeVersions }}"
        targetKubernetesVersion: "{{ targetKubernetesVersion }}"
        longTermSupport: {{ longTermSupport }}
`}</CodeBlock>

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

Create a AutoUpgradeProfile.

```sql
REPLACE azure.container_service_fleet.auto_upgrade_profiles
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND auto_upgrade_profile_name = '{{ auto_upgrade_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
properties,
systemData,
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

Delete a AutoUpgradeProfile.

```sql
DELETE FROM azure.container_service_fleet.auto_upgrade_profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND auto_upgrade_profile_name = '{{ auto_upgrade_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
