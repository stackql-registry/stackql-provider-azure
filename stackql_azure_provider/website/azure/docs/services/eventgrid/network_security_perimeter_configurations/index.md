--- 
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - eventgrid
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid.network_security_perimeter_configurations" /></td></tr>
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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>Network security perimeter info.</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>Nsp profile configuration, access rules and diagnostic settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>Provisioning issues to reflect status when attempting to retrieve nsp profile configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to reflect configuration state and indicate status of nsp profile configuration retrieval. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "Deleted", and "Accepted". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, Deleted, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>Nsp association name and access mode of association.</td>
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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>Network security perimeter info.</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>Nsp profile configuration, access rules and diagnostic settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>Provisioning issues to reflect status when attempting to retrieve nsp profile configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to reflect configuration state and indicate status of nsp profile configuration retrieval. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "Deleted", and "Accepted". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, Deleted, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>Nsp association name and access mode of association.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-perimeter_guid"><code>perimeter_guid</code></a>, <a href="#parameter-association_name"><code>association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a specific network security perimeter configuration. Get a specific network security perimeter configuration with a topic or domain.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all network security perimeter configurations for resource. Get all network security perimeter configurations associated with a topic or domain.</td>
</tr>
<tr>
    <td><a href="#reconcile"><CopyableCode code="reconcile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-perimeter_guid"><code>perimeter_guid</code></a>, <a href="#parameter-association_name"><code>association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reconcile a specific network security perimeter configuration for a given network security perimeter association. Reconcile a specific network security perimeter configuration for a given network security perimeter association with a topic or domain.</td>
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
<tr id="parameter-association_name">
    <td><CopyableCode code="association_name" /></td>
    <td><code>string</code></td>
    <td>Association name to association network security perimeter resource to profile. Required.</td>
</tr>
<tr id="parameter-perimeter_guid">
    <td><CopyableCode code="perimeter_guid" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for perimeter. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group within the user's subscription. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. This can be either \\'topics\\', or \\'domains\\'. Known values are: "topics" and "domains". Required.</td>
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

Get a specific network security perimeter configuration. Get a specific network security perimeter configuration with a topic or domain.

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
FROM azure.eventgrid.network_security_perimeter_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND perimeter_guid = '{{ perimeter_guid }}' -- required
AND association_name = '{{ association_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all network security perimeter configurations for resource. Get all network security perimeter configurations associated with a topic or domain.

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
FROM azure.eventgrid.network_security_perimeter_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reconcile"
    values={[
        { label: 'reconcile', value: 'reconcile' }
    ]}
>
<TabItem value="reconcile">

Reconcile a specific network security perimeter configuration for a given network security perimeter association. Reconcile a specific network security perimeter configuration for a given network security perimeter association with a topic or domain.

```sql
EXEC azure.eventgrid.network_security_perimeter_configurations.reconcile 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_type='{{ resource_type }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@perimeter_guid='{{ perimeter_guid }}' --required, 
@association_name='{{ association_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
