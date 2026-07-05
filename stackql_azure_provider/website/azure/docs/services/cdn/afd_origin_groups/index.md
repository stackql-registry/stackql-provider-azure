--- 
title: afd_origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origin_groups
  - cdn
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

Creates, updates, deletes, gets or lists an <code>afd_origin_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="afd_origin_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_origin_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_profile', value: 'list_by_profile' }
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
    <td><CopyableCode code="authentication" /></td>
    <td><code>object</code></td>
    <td>Authentication settings for origin in origin group.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="healthProbeSettings" /></td>
    <td><code>object</code></td>
    <td>Health probe settings to the origin that is used to determine the health of the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingSettings" /></td>
    <td><code>object</code></td>
    <td>Load balancing settings for a backend pool.</td>
</tr>
<tr>
    <td><CopyableCode code="profileName" /></td>
    <td><code>string</code></td>
    <td>The name of the profile which holds the origin group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionAffinityState" /></td>
    <td><code>string</code></td>
    <td>Whether to allow session affinity on this host. Valid options are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRestorationTimeToHealedOrNewEndpointsInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_profile">

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
    <td><CopyableCode code="authentication" /></td>
    <td><code>object</code></td>
    <td>Authentication settings for origin in origin group.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="healthProbeSettings" /></td>
    <td><code>object</code></td>
    <td>Health probe settings to the origin that is used to determine the health of the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingSettings" /></td>
    <td><code>object</code></td>
    <td>Load balancing settings for a backend pool.</td>
</tr>
<tr>
    <td><CopyableCode code="profileName" /></td>
    <td><code>string</code></td>
    <td>The name of the profile which holds the origin group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionAffinityState" /></td>
    <td><code>string</code></td>
    <td>Whether to allow session affinity on this host. Valid options are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRestorationTimeToHealedOrNewEndpointsInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing origin group within a profile.</td>
</tr>
<tr>
    <td><a href="#list_by_profile"><CopyableCode code="list_by_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the existing origin groups within a profile.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new origin group within the specified profile.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing origin group within a profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing origin group within a profile.</td>
</tr>
<tr>
    <td><a href="#list_resource_usage"><CopyableCode code="list_resource_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the quota and actual usage of endpoints under the given Azure Front Door profile.</td>
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
<tr id="parameter-origin_group_name">
    <td><CopyableCode code="origin_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the origin group which is unique within the endpoint. Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group. Required.</td>
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
        { label: 'list_by_profile', value: 'list_by_profile' }
    ]}
>
<TabItem value="get">

Gets an existing origin group within a profile.

```sql
SELECT
id,
name,
authentication,
deploymentStatus,
healthProbeSettings,
loadBalancingSettings,
profileName,
provisioningState,
sessionAffinityState,
systemData,
trafficRestorationTimeToHealedOrNewEndpointsInMinutes,
type
FROM azure.cdn.afd_origin_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND origin_group_name = '{{ origin_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_profile">

Lists all of the existing origin groups within a profile.

```sql
SELECT
id,
name,
authentication,
deploymentStatus,
healthProbeSettings,
loadBalancingSettings,
profileName,
provisioningState,
sessionAffinityState,
systemData,
trafficRestorationTimeToHealedOrNewEndpointsInMinutes,
type
FROM azure.cdn.afd_origin_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
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

Creates a new origin group within the specified profile.

```sql
INSERT INTO azure.cdn.afd_origin_groups (
properties,
resource_group_name,
profile_name,
origin_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ origin_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: afd_origin_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the afd_origin_groups resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the afd_origin_groups resource.
    - name: origin_group_name
      value: "{{ origin_group_name }}"
      description: Required parameter for the afd_origin_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the afd_origin_groups resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the origin group.
      value:
        profileName: "{{ profileName }}"
        loadBalancingSettings:
          sampleSize: {{ sampleSize }}
          successfulSamplesRequired: {{ successfulSamplesRequired }}
          additionalLatencyInMilliseconds: {{ additionalLatencyInMilliseconds }}
        healthProbeSettings:
          probePath: "{{ probePath }}"
          probeRequestType: "{{ probeRequestType }}"
          probeProtocol: "{{ probeProtocol }}"
          probeIntervalInSeconds: {{ probeIntervalInSeconds }}
        trafficRestorationTimeToHealedOrNewEndpointsInMinutes: {{ trafficRestorationTimeToHealedOrNewEndpointsInMinutes }}
        sessionAffinityState: "{{ sessionAffinityState }}"
        authentication:
          type: "{{ type }}"
          userAssignedIdentity:
            id: "{{ id }}"
          scope: "{{ scope }}"
        provisioningState: "{{ provisioningState }}"
        deploymentStatus: "{{ deploymentStatus }}"
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

Updates an existing origin group within a profile.

```sql
UPDATE azure.cdn.afd_origin_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND origin_group_name = '{{ origin_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Deletes an existing origin group within a profile.

```sql
DELETE FROM azure.cdn.afd_origin_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND origin_group_name = '{{ origin_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_resource_usage"
    values={[
        { label: 'list_resource_usage', value: 'list_resource_usage' }
    ]}
>
<TabItem value="list_resource_usage">

Checks the quota and actual usage of endpoints under the given Azure Front Door profile.

```sql
EXEC azure.cdn.afd_origin_groups.list_resource_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@origin_group_name='{{ origin_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
