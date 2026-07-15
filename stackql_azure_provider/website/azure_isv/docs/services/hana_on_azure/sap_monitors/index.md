--- 
title: sap_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_monitors
  - hana_on_azure
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

Creates, updates, deletes, gets or lists a <code>sap_monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sap_monitors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.hana_on_azure.sap_monitors" /></td></tr>
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
    <td><CopyableCode code="enableCustomerAnalytics" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether to send analytics to Microsoft.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Log Analytics Workspace that is used for monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The workspace ID of the log analytics workspace to be used for monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceSharedKey" /></td>
    <td><code>string</code></td>
    <td>The shared key of the log analytics workspace that is used for monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group the SAP Monitor resources get deployed into.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorSubnet" /></td>
    <td><code>string</code></td>
    <td>The subnet which the SAP monitor will be deployed in.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the HanaInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Accepted, Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="sapMonitorCollectorVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the payload running in the Collector VM.</td>
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
    <td><CopyableCode code="enableCustomerAnalytics" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether to send analytics to Microsoft.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceArmId" /></td>
    <td><code>string</code></td>
    <td>The ARM ID of the Log Analytics Workspace that is used for monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The workspace ID of the log analytics workspace to be used for monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceSharedKey" /></td>
    <td><code>string</code></td>
    <td>The shared key of the log analytics workspace that is used for monitoring.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group the SAP Monitor resources get deployed into.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorSubnet" /></td>
    <td><code>string</code></td>
    <td>The subnet which the SAP monitor will be deployed in.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the HanaInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Accepted, Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="sapMonitorCollectorVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the payload running in the Collector VM.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets properties of a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of SAP monitors in the specified subscription. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patches the Tags field of a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sap_monitor_name">
    <td><CopyableCode code="sap_monitor_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SAP monitor resource. Required.</td>
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

Gets properties of a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
SELECT
id,
name,
enableCustomerAnalytics,
location,
logAnalyticsWorkspaceArmId,
logAnalyticsWorkspaceId,
logAnalyticsWorkspaceSharedKey,
managedResourceGroupName,
monitorSubnet,
provisioningState,
sapMonitorCollectorVersion,
systemData,
tags,
type
FROM azure_isv.hana_on_azure.sap_monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_monitor_name = '{{ sap_monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of SAP monitors in the specified subscription. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
SELECT
id,
name,
enableCustomerAnalytics,
location,
logAnalyticsWorkspaceArmId,
logAnalyticsWorkspaceId,
logAnalyticsWorkspaceSharedKey,
managedResourceGroupName,
monitorSubnet,
provisioningState,
sapMonitorCollectorVersion,
systemData,
tags,
type
FROM azure_isv.hana_on_azure.sap_monitors
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

Creates a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
INSERT INTO azure_isv.hana_on_azure.sap_monitors (
tags,
location,
properties,
resource_group_name,
sap_monitor_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sap_monitor_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: sap_monitors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sap_monitors resource.
    - name: sap_monitor_name
      value: "{{ sap_monitor_name }}"
      description: Required parameter for the sap_monitors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sap_monitors resource.
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
        SAP monitor properties.
      value:
        provisioningState: "{{ provisioningState }}"
        managedResourceGroupName: "{{ managedResourceGroupName }}"
        logAnalyticsWorkspaceArmId: "{{ logAnalyticsWorkspaceArmId }}"
        enableCustomerAnalytics: {{ enableCustomerAnalytics }}
        logAnalyticsWorkspaceId: "{{ logAnalyticsWorkspaceId }}"
        logAnalyticsWorkspaceSharedKey: "{{ logAnalyticsWorkspaceSharedKey }}"
        sapMonitorCollectorVersion: "{{ sapMonitorCollectorVersion }}"
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

Patches the Tags field of a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
UPDATE azure_isv.hana_on_azure.sap_monitors
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sap_monitor_name = '{{ sap_monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Deletes a SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
DELETE FROM azure_isv.hana_on_azure.sap_monitors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sap_monitor_name = '{{ sap_monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
