--- 
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - workloads
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

Creates, updates, deletes, gets or lists a <code>monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="monitors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.workloads.monitors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="appLocation" /></td>
    <td><code>string</code></td>
    <td>The SAP monitor resources will be deployed in the SAP monitoring region. The subnet region should be same as the SAP monitoring region.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the SAP monitor errors.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>[currently not in use] Managed service identity(user assigned identities).</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Log Analytics Workspace that is used for SAP monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorSubnet" /></td>
    <td><code>string</code></td>
    <td>The subnet which the SAP monitor will be deployed in.</td>
</tr>
<tr>
    <td><CopyableCode code="msiArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the MSI used for SAP monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the SAP monitor. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating".</td>
</tr>
<tr>
    <td><CopyableCode code="routingPreference" /></td>
    <td><code>string</code></td>
    <td>Sets the routing preference of the SAP monitor. By default only RFC1918 traffic is routed to the customer VNET. Known values are: "Default" and "RouteAll".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Storage account used for SAP monitoring.</td>
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
    <td><CopyableCode code="zoneRedundancyPreference" /></td>
    <td><code>string</code></td>
    <td>Sets the preference for zone redundancy on resources created for the SAP monitor. By default resources will be created which do not support zone redundancy.</td>
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
    <td><CopyableCode code="appLocation" /></td>
    <td><code>string</code></td>
    <td>The SAP monitor resources will be deployed in the SAP monitoring region. The subnet region should be same as the SAP monitoring region.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the SAP monitor errors.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>[currently not in use] Managed service identity(user assigned identities).</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Log Analytics Workspace that is used for SAP monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorSubnet" /></td>
    <td><code>string</code></td>
    <td>The subnet which the SAP monitor will be deployed in.</td>
</tr>
<tr>
    <td><CopyableCode code="msiArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the MSI used for SAP monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the SAP monitor. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating".</td>
</tr>
<tr>
    <td><CopyableCode code="routingPreference" /></td>
    <td><code>string</code></td>
    <td>Sets the routing preference of the SAP monitor. By default only RFC1918 traffic is routed to the customer VNET. Known values are: "Default" and "RouteAll".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Storage account used for SAP monitoring.</td>
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
    <td><CopyableCode code="zoneRedundancyPreference" /></td>
    <td><code>string</code></td>
    <td>Sets the preference for zone redundancy on resources created for the SAP monitor. By default resources will be created which do not support zone redundancy.</td>
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
    <td><CopyableCode code="appLocation" /></td>
    <td><code>string</code></td>
    <td>The SAP monitor resources will be deployed in the SAP monitoring region. The subnet region should be same as the SAP monitoring region.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the SAP monitor errors.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>[currently not in use] Managed service identity(user assigned identities).</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Log Analytics Workspace that is used for SAP monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorSubnet" /></td>
    <td><code>string</code></td>
    <td>The subnet which the SAP monitor will be deployed in.</td>
</tr>
<tr>
    <td><CopyableCode code="msiArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the MSI used for SAP monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the SAP monitor. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating".</td>
</tr>
<tr>
    <td><CopyableCode code="routingPreference" /></td>
    <td><code>string</code></td>
    <td>Sets the routing preference of the SAP monitor. By default only RFC1918 traffic is routed to the customer VNET. Known values are: "Default" and "RouteAll".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Storage account used for SAP monitoring.</td>
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
    <td><CopyableCode code="zoneRedundancyPreference" /></td>
    <td><code>string</code></td>
    <td>Sets the preference for zone redundancy on resources created for the SAP monitor. By default resources will be created which do not support zone redundancy.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets properties of a SAP monitor. Gets properties of a SAP monitor for the specified subscription, resource group, and resource name.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of SAP monitors. Gets a list of SAP monitors in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of SAP monitors in the specified subscription. Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a SAP monitor. Creates a SAP monitor for the specified subscription, resource group, and resource name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patches the Tags field of a SAP monitor. Patches the Tags field of a SAP monitor for the specified subscription, resource group, and SAP monitor name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a SAP monitor. Deletes a SAP monitor with the specified subscription, resource group, and SAP monitor name.</td>
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
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SAP monitor resource. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets properties of a SAP monitor. Gets properties of a SAP monitor for the specified subscription, resource group, and resource name.

```sql
SELECT
id,
name,
appLocation,
errors,
identity,
location,
logAnalyticsWorkspaceArmId,
managedResourceGroupConfiguration,
monitorSubnet,
msiArmId,
provisioningState,
routingPreference,
storageAccountArmId,
systemData,
tags,
type,
zoneRedundancyPreference
FROM azure_isv.workloads.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of SAP monitors. Gets a list of SAP monitors in the specified resource group.

```sql
SELECT
id,
name,
appLocation,
errors,
identity,
location,
logAnalyticsWorkspaceArmId,
managedResourceGroupConfiguration,
monitorSubnet,
msiArmId,
provisioningState,
routingPreference,
storageAccountArmId,
systemData,
tags,
type,
zoneRedundancyPreference
FROM azure_isv.workloads.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of SAP monitors in the specified subscription. Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor.

```sql
SELECT
id,
name,
appLocation,
errors,
identity,
location,
logAnalyticsWorkspaceArmId,
managedResourceGroupConfiguration,
monitorSubnet,
msiArmId,
provisioningState,
routingPreference,
storageAccountArmId,
systemData,
tags,
type,
zoneRedundancyPreference
FROM azure_isv.workloads.monitors
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

Creates a SAP monitor. Creates a SAP monitor for the specified subscription, resource group, and resource name.

```sql
INSERT INTO azure_isv.workloads.monitors (
tags,
location,
identity,
properties,
resource_group_name,
monitor_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
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
- name: monitors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the monitors resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the monitors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the monitors resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: identity
      description: |
        [currently not in use] Managed service identity(user assigned identities).
      value:
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        appLocation: "{{ appLocation }}"
        routingPreference: "{{ routingPreference }}"
        zoneRedundancyPreference: "{{ zoneRedundancyPreference }}"
        managedResourceGroupConfiguration:
          name: "{{ name }}"
        logAnalyticsWorkspaceArmId: "{{ logAnalyticsWorkspaceArmId }}"
        monitorSubnet: "{{ monitorSubnet }}"
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

Patches the Tags field of a SAP monitor. Patches the Tags field of a SAP monitor for the specified subscription, resource group, and SAP monitor name.

```sql
UPDATE azure_isv.workloads.monitors
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
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

Deletes a SAP monitor. Deletes a SAP monitor with the specified subscription, resource group, and SAP monitor name.

```sql
DELETE FROM azure_isv.workloads.monitors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
