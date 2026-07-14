--- 
title: namespace_discovered_assets
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace_discovered_assets
  - device_registry
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

Creates, updates, deletes, gets or lists a <code>namespace_discovered_assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespace_discovered_assets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.namespace_discovered_assets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
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
    <td><CopyableCode code="assetTypeRefs" /></td>
    <td><code>array</code></td>
    <td>URIs or type definition IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>A set of key-value pairs that contain custom attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="datasets" /></td>
    <td><code>array</code></td>
    <td>Array of datasets that are part of the asset. Each dataset spec describes the data points that make up the set.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDatasetsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all datasets. Each dataset can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDatasetsDestinations" /></td>
    <td><code>array</code></td>
    <td>Default destinations for a dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultEventsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all events. Each event can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultEventsDestinations" /></td>
    <td><code>array</code></td>
    <td>Default destinations for an event.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultManagementGroupsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all management groups. Each management group can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStreamsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all streams. Each stream can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStreamsDestinations" /></td>
    <td><code>array</code></td>
    <td>Default destinations for a stream.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Human-readable description of the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRef" /></td>
    <td><code>object</code></td>
    <td>Reference to the device that provides data for this asset. Must provide device name & endpoint on the device to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryId" /></td>
    <td><code>string</code></td>
    <td>Identifier used to detect changes in the asset. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Human-readable display name.</td>
</tr>
<tr>
    <td><CopyableCode code="documentationUri" /></td>
    <td><code>string</code></td>
    <td>Asset documentation reference.</td>
</tr>
<tr>
    <td><CopyableCode code="eventGroups" /></td>
    <td><code>array</code></td>
    <td>Array of event groups that are part of the asset. Each event group can have per-event group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="externalAssetId" /></td>
    <td><code>string</code></td>
    <td>Asset ID provided by the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareRevision" /></td>
    <td><code>string</code></td>
    <td>Asset hardware revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroups" /></td>
    <td><code>array</code></td>
    <td>Array of management groups that are part of the asset. Each management group can have a per-group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>Asset manufacturer.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturerUri" /></td>
    <td><code>string</code></td>
    <td>Asset manufacturer URI.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>Asset model.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Asset product code.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Asset serial number.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareRevision" /></td>
    <td><code>string</code></td>
    <td>Asset software revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="streams" /></td>
    <td><code>array</code></td>
    <td>Array of streams that are part of the asset. Each stream can have a per-stream configuration.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>An integer that is incremented each time the resource is modified. Required.</td>
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
    <td><CopyableCode code="assetTypeRefs" /></td>
    <td><code>array</code></td>
    <td>URIs or type definition IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>A set of key-value pairs that contain custom attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="datasets" /></td>
    <td><code>array</code></td>
    <td>Array of datasets that are part of the asset. Each dataset spec describes the data points that make up the set.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDatasetsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all datasets. Each dataset can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDatasetsDestinations" /></td>
    <td><code>array</code></td>
    <td>Default destinations for a dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultEventsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all events. Each event can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultEventsDestinations" /></td>
    <td><code>array</code></td>
    <td>Default destinations for an event.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultManagementGroupsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all management groups. Each management group can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStreamsConfiguration" /></td>
    <td><code>string</code></td>
    <td>Stringified JSON that contains connector-specific default configuration for all streams. Each stream can have its own configuration that overrides the default settings here.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStreamsDestinations" /></td>
    <td><code>array</code></td>
    <td>Default destinations for a stream.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Human-readable description of the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRef" /></td>
    <td><code>object</code></td>
    <td>Reference to the device that provides data for this asset. Must provide device name & endpoint on the device to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryId" /></td>
    <td><code>string</code></td>
    <td>Identifier used to detect changes in the asset. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Human-readable display name.</td>
</tr>
<tr>
    <td><CopyableCode code="documentationUri" /></td>
    <td><code>string</code></td>
    <td>Asset documentation reference.</td>
</tr>
<tr>
    <td><CopyableCode code="eventGroups" /></td>
    <td><code>array</code></td>
    <td>Array of event groups that are part of the asset. Each event group can have per-event group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="externalAssetId" /></td>
    <td><code>string</code></td>
    <td>Asset ID provided by the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareRevision" /></td>
    <td><code>string</code></td>
    <td>Asset hardware revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroups" /></td>
    <td><code>array</code></td>
    <td>Array of management groups that are part of the asset. Each management group can have a per-group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>Asset manufacturer.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturerUri" /></td>
    <td><code>string</code></td>
    <td>Asset manufacturer URI.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>Asset model.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Asset product code.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Asset serial number.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareRevision" /></td>
    <td><code>string</code></td>
    <td>Asset software revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="streams" /></td>
    <td><code>array</code></td>
    <td>Array of streams that are part of the asset. Each stream can have a per-stream configuration.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>An integer that is incremented each time the resource is modified. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-discovered_asset_name"><code>discovered_asset_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a NamespaceDiscoveredAsset.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List NamespaceDiscoveredAsset resources by Namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-discovered_asset_name"><code>discovered_asset_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a NamespaceDiscoveredAsset.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-discovered_asset_name"><code>discovered_asset_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a NamespaceDiscoveredAsset.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-discovered_asset_name"><code>discovered_asset_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a NamespaceDiscoveredAsset.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-discovered_asset_name"><code>discovered_asset_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a NamespaceDiscoveredAsset.</td>
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
<tr id="parameter-discovered_asset_name">
    <td><CopyableCode code="discovered_asset_name" /></td>
    <td><code>string</code></td>
    <td>The name of the discovered asset. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the namespace. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
    ]}
>
<TabItem value="get">

Get a NamespaceDiscoveredAsset.

```sql
SELECT
id,
name,
assetTypeRefs,
attributes,
datasets,
defaultDatasetsConfiguration,
defaultDatasetsDestinations,
defaultEventsConfiguration,
defaultEventsDestinations,
defaultManagementGroupsConfiguration,
defaultStreamsConfiguration,
defaultStreamsDestinations,
description,
deviceRef,
discoveryId,
displayName,
documentationUri,
eventGroups,
extendedLocation,
externalAssetId,
hardwareRevision,
location,
managementGroups,
manufacturer,
manufacturerUri,
model,
productCode,
provisioningState,
serialNumber,
softwareRevision,
streams,
systemData,
tags,
type,
version
FROM azure.device_registry.namespace_discovered_assets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND discovered_asset_name = '{{ discovered_asset_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List NamespaceDiscoveredAsset resources by Namespace.

```sql
SELECT
id,
name,
assetTypeRefs,
attributes,
datasets,
defaultDatasetsConfiguration,
defaultDatasetsDestinations,
defaultEventsConfiguration,
defaultEventsDestinations,
defaultManagementGroupsConfiguration,
defaultStreamsConfiguration,
defaultStreamsDestinations,
description,
deviceRef,
discoveryId,
displayName,
documentationUri,
eventGroups,
extendedLocation,
externalAssetId,
hardwareRevision,
location,
managementGroups,
manufacturer,
manufacturerUri,
model,
productCode,
provisioningState,
serialNumber,
softwareRevision,
streams,
systemData,
tags,
type,
version
FROM azure.device_registry.namespace_discovered_assets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_replace">

Create a NamespaceDiscoveredAsset.

```sql
INSERT INTO azure.device_registry.namespace_discovered_assets (
tags,
location,
properties,
extendedLocation,
resource_group_name,
namespace_name,
discovered_asset_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}' /* required */,
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ discovered_asset_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
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
- name: namespace_discovered_assets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the namespace_discovered_assets resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the namespace_discovered_assets resource.
    - name: discovered_asset_name
      value: "{{ discovered_asset_name }}"
      description: Required parameter for the namespace_discovered_assets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the namespace_discovered_assets resource.
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
        The resource-specific properties for this resource.
      value:
        deviceRef:
          deviceName: "{{ deviceName }}"
          endpointName: "{{ endpointName }}"
        displayName: "{{ displayName }}"
        assetTypeRefs:
          - "{{ assetTypeRefs }}"
        description: "{{ description }}"
        discoveryId: "{{ discoveryId }}"
        externalAssetId: "{{ externalAssetId }}"
        version: {{ version }}
        manufacturer: "{{ manufacturer }}"
        manufacturerUri: "{{ manufacturerUri }}"
        model: "{{ model }}"
        productCode: "{{ productCode }}"
        hardwareRevision: "{{ hardwareRevision }}"
        softwareRevision: "{{ softwareRevision }}"
        documentationUri: "{{ documentationUri }}"
        serialNumber: "{{ serialNumber }}"
        attributes: "{{ attributes }}"
        defaultDatasetsConfiguration: "{{ defaultDatasetsConfiguration }}"
        defaultEventsConfiguration: "{{ defaultEventsConfiguration }}"
        defaultStreamsConfiguration: "{{ defaultStreamsConfiguration }}"
        defaultManagementGroupsConfiguration: "{{ defaultManagementGroupsConfiguration }}"
        defaultDatasetsDestinations:
          - target: "{{ target }}"
        defaultEventsDestinations:
          - target: "{{ target }}"
        defaultStreamsDestinations:
          - target: "{{ target }}"
        datasets:
          - name: "{{ name }}"
            dataSource: "{{ dataSource }}"
            typeRef: "{{ typeRef }}"
            datasetConfiguration: "{{ datasetConfiguration }}"
            destinations: "{{ destinations }}"
            dataPoints: "{{ dataPoints }}"
            lastUpdatedOn: "{{ lastUpdatedOn }}"
        eventGroups:
          - name: "{{ name }}"
            dataSource: "{{ dataSource }}"
            eventGroupConfiguration: "{{ eventGroupConfiguration }}"
            defaultDestinations: "{{ defaultDestinations }}"
            typeRef: "{{ typeRef }}"
            events: "{{ events }}"
        streams:
          - name: "{{ name }}"
            streamConfiguration: "{{ streamConfiguration }}"
            typeRef: "{{ typeRef }}"
            destinations: "{{ destinations }}"
            lastUpdatedOn: "{{ lastUpdatedOn }}"
        managementGroups:
          - name: "{{ name }}"
            managementGroupConfiguration: "{{ managementGroupConfiguration }}"
            typeRef: "{{ typeRef }}"
            dataSource: "{{ dataSource }}"
            defaultTopic: "{{ defaultTopic }}"
            defaultTimeoutInSeconds: {{ defaultTimeoutInSeconds }}
            actions: "{{ actions }}"
            lastUpdatedOn: "{{ lastUpdatedOn }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extended location. Required.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
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

Update a NamespaceDiscoveredAsset.

```sql
UPDATE azure.device_registry.namespace_discovered_assets
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND discovered_asset_name = '{{ discovered_asset_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' }
    ]}
>
<TabItem value="create_or_replace">

Create a NamespaceDiscoveredAsset.

```sql
REPLACE azure.device_registry.namespace_discovered_assets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND discovered_asset_name = '{{ discovered_asset_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
RETURNING
id,
name,
extendedLocation,
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

Delete a NamespaceDiscoveredAsset.

```sql
DELETE FROM azure.device_registry.namespace_discovered_assets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND discovered_asset_name = '{{ discovered_asset_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
