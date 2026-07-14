--- 
title: arc_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - arc_settings
  - azure_stack_hci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>arc_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="arc_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.arc_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cluster', value: 'list_by_cluster' }
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
    <td><CopyableCode code="aggregateState" /></td>
    <td><code>string</code></td>
    <td>Aggregate state of Arc agent across the nodes in this HCI cluster. Known values are: "NotSpecified", "Error", "Succeeded", "Canceled", "Failed", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Canceled, Failed, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="arcApplicationClientId" /></td>
    <td><code>string</code></td>
    <td>App id of arc AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="arcApplicationObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of arc AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="arcApplicationTenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant id of arc AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="arcInstanceResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group that hosts the Arc agents, ie. Hybrid Compute Machine resources.</td>
</tr>
<tr>
    <td><CopyableCode code="arcServicePrincipalObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of arc AAD service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityProperties" /></td>
    <td><code>object</code></td>
    <td>contains connectivity related configuration for ARC resources.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultExtensions" /></td>
    <td><code>array</code></td>
    <td>Properties for each of the default extensions category.</td>
</tr>
<tr>
    <td><CopyableCode code="perNodeDetails" /></td>
    <td><code>array</code></td>
    <td>State of Arc agent in each of the nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the ArcSetting proxy resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_cluster">

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
    <td><CopyableCode code="aggregateState" /></td>
    <td><code>string</code></td>
    <td>Aggregate state of Arc agent across the nodes in this HCI cluster. Known values are: "NotSpecified", "Error", "Succeeded", "Canceled", "Failed", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Canceled, Failed, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="arcApplicationClientId" /></td>
    <td><code>string</code></td>
    <td>App id of arc AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="arcApplicationObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of arc AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="arcApplicationTenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant id of arc AAD identity.</td>
</tr>
<tr>
    <td><CopyableCode code="arcInstanceResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group that hosts the Arc agents, ie. Hybrid Compute Machine resources.</td>
</tr>
<tr>
    <td><CopyableCode code="arcServicePrincipalObjectId" /></td>
    <td><code>string</code></td>
    <td>Object id of arc AAD service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityProperties" /></td>
    <td><code>object</code></td>
    <td>contains connectivity related configuration for ARC resources.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultExtensions" /></td>
    <td><code>array</code></td>
    <td>Properties for each of the default extensions category.</td>
</tr>
<tr>
    <td><CopyableCode code="perNodeDetails" /></td>
    <td><code>array</code></td>
    <td>State of Arc agent in each of the nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the ArcSetting proxy resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get ArcSetting resource details of HCI Cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_cluster"><CopyableCode code="list_by_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get ArcSetting resources of HCI Cluster.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create ArcSetting for HCI cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update ArcSettings for HCI cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete ArcSetting resource details of HCI Cluster.</td>
</tr>
<tr>
    <td><a href="#generate_password"><CopyableCode code="generate_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate password for arc settings.</td>
</tr>
<tr>
    <td><a href="#create_identity"><CopyableCode code="create_identity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Aad identity for arc settings.</td>
</tr>
<tr>
    <td><a href="#reconcile"><CopyableCode code="reconcile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reconcile Arc Settings with information related to all nodes.</td>
</tr>
<tr>
    <td><a href="#consent_and_install_default_extensions"><CopyableCode code="consent_and_install_default_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add consent time for default extensions and initiate extensions installation.</td>
</tr>
<tr>
    <td><a href="#initialize_disable_process"><CopyableCode code="initialize_disable_process" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-arc_setting_name"><code>arc_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initializes ARC Disable process on the cluster.</td>
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
<tr id="parameter-arc_setting_name">
    <td><CopyableCode code="arc_setting_name" /></td>
    <td><code>string</code></td>
    <td>The name of the proxy resource holding details of HCI ArcSetting information. Required.</td>
</tr>
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
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
        { label: 'list_by_cluster', value: 'list_by_cluster' }
    ]}
>
<TabItem value="get">

Get ArcSetting resource details of HCI Cluster.

```sql
SELECT
id,
name,
aggregateState,
arcApplicationClientId,
arcApplicationObjectId,
arcApplicationTenantId,
arcInstanceResourceGroup,
arcServicePrincipalObjectId,
connectivityProperties,
defaultExtensions,
perNodeDetails,
provisioningState,
systemData,
type
FROM azure_stack.azure_stack_hci.arc_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND arc_setting_name = '{{ arc_setting_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cluster">

Get ArcSetting resources of HCI Cluster.

```sql
SELECT
id,
name,
aggregateState,
arcApplicationClientId,
arcApplicationObjectId,
arcApplicationTenantId,
arcInstanceResourceGroup,
arcServicePrincipalObjectId,
connectivityProperties,
defaultExtensions,
perNodeDetails,
provisioningState,
systemData,
type
FROM azure_stack.azure_stack_hci.arc_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
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

Create ArcSetting for HCI cluster.

```sql
INSERT INTO azure_stack.azure_stack_hci.arc_settings (
properties,
resource_group_name,
cluster_name,
arc_setting_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ arc_setting_name }}',
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
- name: arc_settings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the arc_settings resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the arc_settings resource.
    - name: arc_setting_name
      value: "{{ arc_setting_name }}"
      description: Required parameter for the arc_settings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the arc_settings resource.
    - name: properties
      description: |
        ArcSetting properties.
      value:
        provisioningState: "{{ provisioningState }}"
        arcInstanceResourceGroup: "{{ arcInstanceResourceGroup }}"
        arcApplicationClientId: "{{ arcApplicationClientId }}"
        arcApplicationTenantId: "{{ arcApplicationTenantId }}"
        arcServicePrincipalObjectId: "{{ arcServicePrincipalObjectId }}"
        arcApplicationObjectId: "{{ arcApplicationObjectId }}"
        aggregateState: "{{ aggregateState }}"
        perNodeDetails:
          - name: "{{ name }}"
            arcInstance: "{{ arcInstance }}"
            arcNodeServicePrincipalObjectId: "{{ arcNodeServicePrincipalObjectId }}"
            state: "{{ state }}"
        connectivityProperties:
          enabled: {{ enabled }}
          serviceConfigurations:
            - serviceName: "{{ serviceName }}"
              port: {{ port }}
        defaultExtensions:
          - category: "{{ category }}"
            consentTime: "{{ consentTime }}"
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

Update ArcSettings for HCI cluster.

```sql
UPDATE azure_stack.azure_stack_hci.arc_settings
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND arc_setting_name = '{{ arc_setting_name }}' --required
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

Delete ArcSetting resource details of HCI Cluster.

```sql
DELETE FROM azure_stack.azure_stack_hci.arc_settings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND arc_setting_name = '{{ arc_setting_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_password"
    values={[
        { label: 'generate_password', value: 'generate_password' },
        { label: 'create_identity', value: 'create_identity' },
        { label: 'reconcile', value: 'reconcile' },
        { label: 'consent_and_install_default_extensions', value: 'consent_and_install_default_extensions' },
        { label: 'initialize_disable_process', value: 'initialize_disable_process' }
    ]}
>
<TabItem value="generate_password">

Generate password for arc settings.

```sql
EXEC azure_stack.azure_stack_hci.arc_settings.generate_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@arc_setting_name='{{ arc_setting_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_identity">

Create Aad identity for arc settings.

```sql
EXEC azure_stack.azure_stack_hci.arc_settings.create_identity 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@arc_setting_name='{{ arc_setting_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reconcile">

Reconcile Arc Settings with information related to all nodes.

```sql
EXEC azure_stack.azure_stack_hci.arc_settings.reconcile 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@arc_setting_name='{{ arc_setting_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="consent_and_install_default_extensions">

Add consent time for default extensions and initiate extensions installation.

```sql
EXEC azure_stack.azure_stack_hci.arc_settings.consent_and_install_default_extensions 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@arc_setting_name='{{ arc_setting_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="initialize_disable_process">

Initializes ARC Disable process on the cluster.

```sql
EXEC azure_stack.azure_stack_hci.arc_settings.initialize_disable_process 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@arc_setting_name='{{ arc_setting_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
