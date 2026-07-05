--- 
title: site_network_services
hide_title: false
hide_table_of_contents: false
keywords:
  - site_network_services
  - hybridnetwork
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

Creates, updates, deletes, gets or lists a <code>site_network_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="site_network_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridnetwork.site_network_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="desiredStateConfigurationGroupValueReferences" /></td>
    <td><code>object</code></td>
    <td>The goal state of the site network service resource. This has references to the configuration group value objects that describe the desired state of the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity of the Site network service, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateConfigurationGroupValueReferences" /></td>
    <td><code>object</code></td>
    <td>The last state of the site network service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateNetworkServiceDesignVersionName" /></td>
    <td><code>string</code></td>
    <td>The network service design version for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignGroupName" /></td>
    <td><code>string</code></td>
    <td>The network service design group name for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionName" /></td>
    <td><code>string</code></td>
    <td>The network service design version for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionOfferingLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the network service design offering.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionResourceReference" /></td>
    <td><code>object</code></td>
    <td>The network service design version resource reference.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the site network service resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
</tr>
<tr>
    <td><CopyableCode code="publisherName" /></td>
    <td><code>string</code></td>
    <td>The publisher name for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherScope" /></td>
    <td><code>string</code></td>
    <td>The scope of the publisher. Known values are: "Unknown" and "Private".</td>
</tr>
<tr>
    <td><CopyableCode code="siteReference" /></td>
    <td><code>object</code></td>
    <td>The site details.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the site network service.</td>
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
    <td><CopyableCode code="desiredStateConfigurationGroupValueReferences" /></td>
    <td><code>object</code></td>
    <td>The goal state of the site network service resource. This has references to the configuration group value objects that describe the desired state of the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity of the Site network service, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateConfigurationGroupValueReferences" /></td>
    <td><code>object</code></td>
    <td>The last state of the site network service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateNetworkServiceDesignVersionName" /></td>
    <td><code>string</code></td>
    <td>The network service design version for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignGroupName" /></td>
    <td><code>string</code></td>
    <td>The network service design group name for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionName" /></td>
    <td><code>string</code></td>
    <td>The network service design version for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionOfferingLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the network service design offering.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionResourceReference" /></td>
    <td><code>object</code></td>
    <td>The network service design version resource reference.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the site network service resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
</tr>
<tr>
    <td><CopyableCode code="publisherName" /></td>
    <td><code>string</code></td>
    <td>The publisher name for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherScope" /></td>
    <td><code>string</code></td>
    <td>The scope of the publisher. Known values are: "Unknown" and "Private".</td>
</tr>
<tr>
    <td><CopyableCode code="siteReference" /></td>
    <td><code>object</code></td>
    <td>The site details.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the site network service.</td>
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
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="desiredStateConfigurationGroupValueReferences" /></td>
    <td><code>object</code></td>
    <td>The goal state of the site network service resource. This has references to the configuration group value objects that describe the desired state of the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity of the Site network service, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateConfigurationGroupValueReferences" /></td>
    <td><code>object</code></td>
    <td>The last state of the site network service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateNetworkServiceDesignVersionName" /></td>
    <td><code>string</code></td>
    <td>The network service design version for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignGroupName" /></td>
    <td><code>string</code></td>
    <td>The network service design group name for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionName" /></td>
    <td><code>string</code></td>
    <td>The network service design version for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionOfferingLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the network service design offering.</td>
</tr>
<tr>
    <td><CopyableCode code="networkServiceDesignVersionResourceReference" /></td>
    <td><code>object</code></td>
    <td>The network service design version resource reference.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the site network service resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
</tr>
<tr>
    <td><CopyableCode code="publisherName" /></td>
    <td><code>string</code></td>
    <td>The publisher name for the site network service.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherScope" /></td>
    <td><code>string</code></td>
    <td>The scope of the publisher. Known values are: "Unknown" and "Private".</td>
</tr>
<tr>
    <td><CopyableCode code="siteReference" /></td>
    <td><code>object</code></td>
    <td>The site details.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the site network service.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_network_service_name"><code>site_network_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified site network service.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all site network services.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all sites in the network service in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_network_service_name"><code>site_network_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a network site.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_network_service_name"><code>site_network_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a site update tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_network_service_name"><code>site_network_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a network site.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_network_service_name"><code>site_network_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified site network service.</td>
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
<tr id="parameter-site_network_service_name">
    <td><CopyableCode code="site_network_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the site network service. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets information about the specified site network service.

```sql
SELECT
id,
name,
desiredStateConfigurationGroupValueReferences,
identity,
lastStateConfigurationGroupValueReferences,
lastStateNetworkServiceDesignVersionName,
location,
managedResourceGroupConfiguration,
networkServiceDesignGroupName,
networkServiceDesignVersionName,
networkServiceDesignVersionOfferingLocation,
networkServiceDesignVersionResourceReference,
provisioningState,
publisherName,
publisherScope,
siteReference,
sku,
systemData,
tags,
type
FROM azure.hybridnetwork.site_network_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_network_service_name = '{{ site_network_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all site network services.

```sql
SELECT
id,
name,
desiredStateConfigurationGroupValueReferences,
identity,
lastStateConfigurationGroupValueReferences,
lastStateNetworkServiceDesignVersionName,
location,
managedResourceGroupConfiguration,
networkServiceDesignGroupName,
networkServiceDesignVersionName,
networkServiceDesignVersionOfferingLocation,
networkServiceDesignVersionResourceReference,
provisioningState,
publisherName,
publisherScope,
siteReference,
sku,
systemData,
tags,
type
FROM azure.hybridnetwork.site_network_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all sites in the network service in a subscription.

```sql
SELECT
id,
name,
desiredStateConfigurationGroupValueReferences,
identity,
lastStateConfigurationGroupValueReferences,
lastStateNetworkServiceDesignVersionName,
location,
managedResourceGroupConfiguration,
networkServiceDesignGroupName,
networkServiceDesignVersionName,
networkServiceDesignVersionOfferingLocation,
networkServiceDesignVersionResourceReference,
provisioningState,
publisherName,
publisherScope,
siteReference,
sku,
systemData,
tags,
type
FROM azure.hybridnetwork.site_network_services
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a network site.

```sql
INSERT INTO azure.hybridnetwork.site_network_services (
tags,
location,
properties,
identity,
sku,
resource_group_name,
site_network_service_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ site_network_service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: site_network_services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the site_network_services resource.
    - name: site_network_service_name
      value: "{{ site_network_service_name }}"
      description: Required parameter for the site_network_services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the site_network_services resource.
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
        Site network service properties.
      value:
        provisioningState: "{{ provisioningState }}"
        managedResourceGroupConfiguration:
          name: "{{ name }}"
          location: "{{ location }}"
        siteReference:
          id: "{{ id }}"
        publisherName: "{{ publisherName }}"
        publisherScope: "{{ publisherScope }}"
        networkServiceDesignGroupName: "{{ networkServiceDesignGroupName }}"
        networkServiceDesignVersionName: "{{ networkServiceDesignVersionName }}"
        networkServiceDesignVersionOfferingLocation: "{{ networkServiceDesignVersionOfferingLocation }}"
        networkServiceDesignVersionResourceReference:
          idType: "{{ idType }}"
        desiredStateConfigurationGroupValueReferences: "{{ desiredStateConfigurationGroupValueReferences }}"
        lastStateNetworkServiceDesignVersionName: "{{ lastStateNetworkServiceDesignVersionName }}"
        lastStateConfigurationGroupValueReferences: "{{ lastStateConfigurationGroupValueReferences }}"
    - name: identity
      description: |
        The managed identity of the Site network service, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: sku
      description: |
        Sku of the site network service.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates a site update tags.

```sql
UPDATE azure.hybridnetwork.site_network_services
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND site_network_service_name = '{{ site_network_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type;
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

Creates or updates a network site.

```sql
REPLACE azure.hybridnetwork.site_network_services
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND site_network_service_name = '{{ site_network_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Deletes the specified site network service.

```sql
DELETE FROM azure.hybridnetwork.site_network_services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND site_network_service_name = '{{ site_network_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
