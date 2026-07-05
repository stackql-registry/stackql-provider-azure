--- 
title: data_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_controllers
  - azurearcdata
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

Creates, updates, deletes, gets or lists a <code>data_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_controllers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azurearcdata.data_controllers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_data_controller"
    values={[
        { label: 'get_data_controller', value: 'get_data_controller' },
        { label: 'list_in_group', value: 'list_in_group' },
        { label: 'list_in_subscription', value: 'list_in_subscription' }
    ]}
>
<TabItem value="get_data_controller">

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
    <td><CopyableCode code="basicLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Deprecated. Azure Arc Data Services data controller no longer expose any endpoint. All traffic are exposed through Kubernetes native API.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the connected cluster the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the extension the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructure" /></td>
    <td><code>string</code></td>
    <td>The infrastructure the data controller is running on. Known values are: "azure", "gcp", "aws", "alibaba", "onpremises", and "other".</td>
</tr>
<tr>
    <td><CopyableCode code="k8sRaw" /></td>
    <td><code>object</code></td>
    <td>The raw kubernetes information.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last uploaded date from Kubernetes cluster. Defaults to current date time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceConfig" /></td>
    <td><code>object</code></td>
    <td>Log analytics workspace id and primary key.</td>
</tr>
<tr>
    <td><CopyableCode code="logsDashboardCredential" /></td>
    <td><code>object</code></td>
    <td>Login credential for logs dashboard on the Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsDashboardCredential" /></td>
    <td><code>object</code></td>
    <td>Login credential for metrics dashboard on the Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremiseProperty" /></td>
    <td><code>object</code></td>
    <td>Properties from the Kubernetes data controller.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc Data Controller resource.</td>
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
    <td><CopyableCode code="uploadServicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Deprecated. Service principal is deprecated in favor of Arc Kubernetes service extension managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadWatermark" /></td>
    <td><code>object</code></td>
    <td>Properties on upload watermark. Mostly timestamp for each upload data type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_in_group">

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
    <td><CopyableCode code="basicLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Deprecated. Azure Arc Data Services data controller no longer expose any endpoint. All traffic are exposed through Kubernetes native API.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the connected cluster the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the extension the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructure" /></td>
    <td><code>string</code></td>
    <td>The infrastructure the data controller is running on. Known values are: "azure", "gcp", "aws", "alibaba", "onpremises", and "other".</td>
</tr>
<tr>
    <td><CopyableCode code="k8sRaw" /></td>
    <td><code>object</code></td>
    <td>The raw kubernetes information.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last uploaded date from Kubernetes cluster. Defaults to current date time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceConfig" /></td>
    <td><code>object</code></td>
    <td>Log analytics workspace id and primary key.</td>
</tr>
<tr>
    <td><CopyableCode code="logsDashboardCredential" /></td>
    <td><code>object</code></td>
    <td>Login credential for logs dashboard on the Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsDashboardCredential" /></td>
    <td><code>object</code></td>
    <td>Login credential for metrics dashboard on the Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremiseProperty" /></td>
    <td><code>object</code></td>
    <td>Properties from the Kubernetes data controller.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc Data Controller resource.</td>
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
    <td><CopyableCode code="uploadServicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Deprecated. Service principal is deprecated in favor of Arc Kubernetes service extension managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadWatermark" /></td>
    <td><code>object</code></td>
    <td>Properties on upload watermark. Mostly timestamp for each upload data type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_in_subscription">

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
    <td><CopyableCode code="basicLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Deprecated. Azure Arc Data Services data controller no longer expose any endpoint. All traffic are exposed through Kubernetes native API.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the connected cluster the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>If a CustomLocation is provided, this contains the ARM id of the extension the custom location belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructure" /></td>
    <td><code>string</code></td>
    <td>The infrastructure the data controller is running on. Known values are: "azure", "gcp", "aws", "alibaba", "onpremises", and "other".</td>
</tr>
<tr>
    <td><CopyableCode code="k8sRaw" /></td>
    <td><code>object</code></td>
    <td>The raw kubernetes information.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last uploaded date from Kubernetes cluster. Defaults to current date time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsWorkspaceConfig" /></td>
    <td><code>object</code></td>
    <td>Log analytics workspace id and primary key.</td>
</tr>
<tr>
    <td><CopyableCode code="logsDashboardCredential" /></td>
    <td><code>object</code></td>
    <td>Login credential for logs dashboard on the Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsDashboardCredential" /></td>
    <td><code>object</code></td>
    <td>Login credential for metrics dashboard on the Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremiseProperty" /></td>
    <td><code>object</code></td>
    <td>Properties from the Kubernetes data controller.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Arc Data Controller resource.</td>
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
    <td><CopyableCode code="uploadServicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Deprecated. Service principal is deprecated in favor of Arc Kubernetes service extension managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadWatermark" /></td>
    <td><code>object</code></td>
    <td>Properties on upload watermark. Mostly timestamp for each upload data type.</td>
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
    <td><a href="#get_data_controller"><CopyableCode code="get_data_controller" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a dataController resource.</td>
</tr>
<tr>
    <td><a href="#list_in_group"><CopyableCode code="list_in_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List dataController resources in the resource group. List dataController resources in the resource group.</td>
</tr>
<tr>
    <td><a href="#list_in_subscription"><CopyableCode code="list_in_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List dataController resources in the subscription. List dataController resources in the subscription.</td>
</tr>
<tr>
    <td><a href="#delete_data_controller"><CopyableCode code="delete_data_controller" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a dataController resource.</td>
</tr>
<tr>
    <td><a href="#put_data_controller"><CopyableCode code="put_data_controller" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or replaces a dataController resource.</td>
</tr>
<tr>
    <td><a href="#patch_data_controller"><CopyableCode code="patch_data_controller" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a dataController resource.</td>
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
<tr id="parameter-data_controller_name">
    <td><CopyableCode code="data_controller_name" /></td>
    <td><code>string</code></td>
    <td>The name of the data controller. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure resource group. Required.</td>
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
    defaultValue="get_data_controller"
    values={[
        { label: 'get_data_controller', value: 'get_data_controller' },
        { label: 'list_in_group', value: 'list_in_group' },
        { label: 'list_in_subscription', value: 'list_in_subscription' }
    ]}
>
<TabItem value="get_data_controller">

Retrieves a dataController resource.

```sql
SELECT
id,
name,
basicLoginInformation,
clusterId,
extendedLocation,
extensionId,
infrastructure,
k8sRaw,
lastUploadedDate,
location,
logAnalyticsWorkspaceConfig,
logsDashboardCredential,
metricsDashboardCredential,
onPremiseProperty,
provisioningState,
systemData,
tags,
type,
uploadServicePrincipal,
uploadWatermark
FROM azure.azurearcdata.data_controllers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_controller_name = '{{ data_controller_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_in_group">

List dataController resources in the resource group. List dataController resources in the resource group.

```sql
SELECT
id,
name,
basicLoginInformation,
clusterId,
extendedLocation,
extensionId,
infrastructure,
k8sRaw,
lastUploadedDate,
location,
logAnalyticsWorkspaceConfig,
logsDashboardCredential,
metricsDashboardCredential,
onPremiseProperty,
provisioningState,
systemData,
tags,
type,
uploadServicePrincipal,
uploadWatermark
FROM azure.azurearcdata.data_controllers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_in_subscription">

List dataController resources in the subscription. List dataController resources in the subscription.

```sql
SELECT
id,
name,
basicLoginInformation,
clusterId,
extendedLocation,
extensionId,
infrastructure,
k8sRaw,
lastUploadedDate,
location,
logAnalyticsWorkspaceConfig,
logsDashboardCredential,
metricsDashboardCredential,
onPremiseProperty,
provisioningState,
systemData,
tags,
type,
uploadServicePrincipal,
uploadWatermark
FROM azure.azurearcdata.data_controllers
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_data_controller"
    values={[
        { label: 'delete_data_controller', value: 'delete_data_controller' }
    ]}
>
<TabItem value="delete_data_controller">

Deletes a dataController resource.

```sql
DELETE FROM azure.azurearcdata.data_controllers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND data_controller_name = '{{ data_controller_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put_data_controller"
    values={[
        { label: 'put_data_controller', value: 'put_data_controller' },
        { label: 'patch_data_controller', value: 'patch_data_controller' }
    ]}
>
<TabItem value="put_data_controller">

Creates or replaces a dataController resource.

```sql
EXEC azure.azurearcdata.data_controllers.put_data_controller 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_controller_name='{{ data_controller_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"location": "{{ location }}", 
"extendedLocation": "{{ extendedLocation }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="patch_data_controller">

Updates a dataController resource.

```sql
EXEC azure.azurearcdata.data_controllers.patch_data_controller 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_controller_name='{{ data_controller_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
