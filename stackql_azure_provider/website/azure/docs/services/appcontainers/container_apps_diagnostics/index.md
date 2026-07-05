--- 
title: container_apps_diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_diagnostics
  - appcontainers
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

Creates, updates, deletes, gets or lists a <code>container_apps_diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps_diagnostics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.container_apps_diagnostics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_revision"
    values={[
        { label: 'get_revision', value: 'get_revision' },
        { label: 'get_detector', value: 'get_detector' },
        { label: 'list_revisions', value: 'list_revisions' }
    ]}
>
<TabItem value="get_revision">

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
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>Boolean describing if the Revision is Active.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp describing when the revision was created by controller.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of the revision.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>Current health State of the revision. Known values are: "Healthy", "Unhealthy", and "None". (Healthy, Unhealthy, None)</td>
</tr>
<tr>
    <td><CopyableCode code="lastActiveTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp describing when the revision was last active. Only meaningful when revision is inactive.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningError" /></td>
    <td><code>string</code></td>
    <td>Optional Field - Platform Error Message.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning State of the revision. Known values are: "Provisioning", "Provisioned", "Failed", "Deprovisioning", and "Deprovisioned". (Provisioning, Provisioned, Failed, Deprovisioning, Deprovisioned)</td>
</tr>
<tr>
    <td><CopyableCode code="replicas" /></td>
    <td><code>integer</code></td>
    <td>Number of pods currently running for this revision.</td>
</tr>
<tr>
    <td><CopyableCode code="runningState" /></td>
    <td><code>string</code></td>
    <td>Current running state of the revision. Known values are: "Running", "Processing", "Stopped", "Degraded", "Failed", and "Unknown". (Running, Processing, Stopped, Degraded, Failed, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container App Revision Template with all possible settings and the defaults if user did not provide them. The defaults are populated as they were at the creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficWeight" /></td>
    <td><code>integer</code></td>
    <td>Traffic weight assigned to this revision.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_detector">

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
    <td><CopyableCode code="dataProviderMetadata" /></td>
    <td><code>object</code></td>
    <td>List of data providers' metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>array</code></td>
    <td>Set of data collections associated with the response.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of the diagnostics response.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of the diagnostics response.</td>
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
<TabItem value="list_revisions">

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
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>Boolean describing if the Revision is Active.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp describing when the revision was created by controller.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of the revision.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>Current health State of the revision. Known values are: "Healthy", "Unhealthy", and "None". (Healthy, Unhealthy, None)</td>
</tr>
<tr>
    <td><CopyableCode code="lastActiveTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp describing when the revision was last active. Only meaningful when revision is inactive.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningError" /></td>
    <td><code>string</code></td>
    <td>Optional Field - Platform Error Message.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning State of the revision. Known values are: "Provisioning", "Provisioned", "Failed", "Deprovisioning", and "Deprovisioned". (Provisioning, Provisioned, Failed, Deprovisioning, Deprovisioned)</td>
</tr>
<tr>
    <td><CopyableCode code="replicas" /></td>
    <td><code>integer</code></td>
    <td>Number of pods currently running for this revision.</td>
</tr>
<tr>
    <td><CopyableCode code="runningState" /></td>
    <td><code>string</code></td>
    <td>Current running state of the revision. Known values are: "Running", "Processing", "Stopped", "Degraded", "Failed", and "Unknown". (Running, Processing, Stopped, Degraded, Failed, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container App Revision Template with all possible settings and the defaults if user did not provide them. The defaults are populated as they were at the creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficWeight" /></td>
    <td><code>integer</code></td>
    <td>Traffic weight assigned to this revision.</td>
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
    <td><a href="#get_revision"><CopyableCode code="get_revision" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-revision_name"><code>revision_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a revision of a Container App. Get a revision of a Container App.</td>
</tr>
<tr>
    <td><a href="#get_detector"><CopyableCode code="get_detector" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a diagnostics result of a Container App. Get a diagnostics result of a Container App.</td>
</tr>
<tr>
    <td><a href="#list_revisions"><CopyableCode code="list_revisions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get the Revisions for a given Container App. A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#list_detectors"><CopyableCode code="list_detectors" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the list of diagnostics for a given Container App. Get the list of diagnostics for a given Container App.</td>
</tr>
<tr>
    <td><a href="#get_root"><CopyableCode code="get_root" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a Container App. Get the properties of a Container App.</td>
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
<tr id="parameter-container_app_name">
    <td><CopyableCode code="container_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App. Required.</td>
</tr>
<tr id="parameter-detector_name">
    <td><CopyableCode code="detector_name" /></td>
    <td><code>string</code></td>
    <td>Name of the detector. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-revision_name">
    <td><CopyableCode code="revision_name" /></td>
    <td><code>string</code></td>
    <td>Name of the detector. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_revision"
    values={[
        { label: 'get_revision', value: 'get_revision' },
        { label: 'get_detector', value: 'get_detector' },
        { label: 'list_revisions', value: 'list_revisions' }
    ]}
>
<TabItem value="get_revision">

Get a revision of a Container App. Get a revision of a Container App.

```sql
SELECT
id,
name,
active,
createdTime,
fqdn,
healthState,
lastActiveTime,
provisioningError,
provisioningState,
replicas,
runningState,
systemData,
template,
trafficWeight,
type
FROM azure.appcontainers.container_apps_diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND revision_name = '{{ revision_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_detector">

Get a diagnostics result of a Container App. Get a diagnostics result of a Container App.

```sql
SELECT
id,
name,
dataProviderMetadata,
dataset,
metadata,
status,
systemData,
type
FROM azure.appcontainers.container_apps_diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_revisions">

Get the Revisions for a given Container App. A synchronous resource action.

```sql
SELECT
id,
name,
active,
createdTime,
fqdn,
healthState,
lastActiveTime,
provisioningError,
provisioningState,
replicas,
runningState,
systemData,
template,
trafficWeight,
type
FROM azure.appcontainers.container_apps_diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_detectors"
    values={[
        { label: 'list_detectors', value: 'list_detectors' },
        { label: 'get_root', value: 'get_root' }
    ]}
>
<TabItem value="list_detectors">

Get the list of diagnostics for a given Container App. Get the list of diagnostics for a given Container App.

```sql
EXEC azure.appcontainers.container_apps_diagnostics.list_detectors 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_root">

Get the properties of a Container App. Get the properties of a Container App.

```sql
EXEC azure.appcontainers.container_apps_diagnostics.get_root 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
