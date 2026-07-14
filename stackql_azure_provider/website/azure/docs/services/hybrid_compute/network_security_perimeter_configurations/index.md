--- 
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - hybrid_compute
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_security_perimeter_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_private_link_scope"
    values={[
        { label: 'get_by_private_link_scope', value: 'get_by_private_link_scope' },
        { label: 'list_by_private_link_scope', value: 'list_by_private_link_scope' }
    ]}
>
<TabItem value="get_by_private_link_scope">

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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>The Network Security Perimeter associated with this configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>Network Security Perimeter profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>Provisioning issues.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this NetworkSecurityPerimeter: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Provisioning ,Succeeded, Canceled and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>The Resource Association.</td>
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
<TabItem value="list_by_private_link_scope">

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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>The Network Security Perimeter associated with this configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>Network Security Perimeter profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>Provisioning issues.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this NetworkSecurityPerimeter: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Provisioning ,Succeeded, Canceled and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>The Resource Association.</td>
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
    <td><a href="#get_by_private_link_scope"><CopyableCode code="get_by_private_link_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-perimeter_name"><code>perimeter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the network security perimeter configuration for a private link scope.</td>
</tr>
<tr>
    <td><a href="#list_by_private_link_scope"><CopyableCode code="list_by_private_link_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the network security perimeter configurations for a private link scope.</td>
</tr>
<tr>
    <td><a href="#reconcile_for_private_link_scope"><CopyableCode code="reconcile_for_private_link_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scope_name"><code>scope_name</code></a>, <a href="#parameter-perimeter_name"><code>perimeter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Forces the network security perimeter configuration to refresh for a private link scope.</td>
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
<tr id="parameter-perimeter_name">
    <td><CopyableCode code="perimeter_name" /></td>
    <td><code>string</code></td>
    <td>The name, in the format &#123;perimeterGuid&#125;.&#123;associationName&#125;, of the Network Security Perimeter resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-scope_name">
    <td><CopyableCode code="scope_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure Arc PrivateLinkScope resource. Required.</td>
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
    defaultValue="get_by_private_link_scope"
    values={[
        { label: 'get_by_private_link_scope', value: 'get_by_private_link_scope' },
        { label: 'list_by_private_link_scope', value: 'list_by_private_link_scope' }
    ]}
>
<TabItem value="get_by_private_link_scope">

Gets the network security perimeter configuration for a private link scope.

```sql
SELECT
id,
name,
networkSecurityPerimeter,
profile,
provisioningIssues,
provisioningState,
resourceAssociation,
systemData,
type
FROM azure.hybrid_compute.network_security_perimeter_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scope_name = '{{ scope_name }}' -- required
AND perimeter_name = '{{ perimeter_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_private_link_scope">

Lists the network security perimeter configurations for a private link scope.

```sql
SELECT
id,
name,
networkSecurityPerimeter,
profile,
provisioningIssues,
provisioningState,
resourceAssociation,
systemData,
type
FROM azure.hybrid_compute.network_security_perimeter_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scope_name = '{{ scope_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reconcile_for_private_link_scope"
    values={[
        { label: 'reconcile_for_private_link_scope', value: 'reconcile_for_private_link_scope' }
    ]}
>
<TabItem value="reconcile_for_private_link_scope">

Forces the network security perimeter configuration to refresh for a private link scope.

```sql
EXEC azure.hybrid_compute.network_security_perimeter_configurations.reconcile_for_private_link_scope 
@resource_group_name='{{ resource_group_name }}' --required, 
@scope_name='{{ scope_name }}' --required, 
@perimeter_name='{{ perimeter_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
