--- 
title: fhir_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_destinations
  - health_data_services
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>fhir_destinations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fhir_destinations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_data_services.fhir_destinations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_iot_connector"
    values={[
        { label: 'list_by_iot_connector', value: 'list_by_iot_connector' }
    ]}
>
<TabItem value="list_by_iot_connector">

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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>An etag associated with the resource, used for optimistic concurrency when editing it.</td>
</tr>
<tr>
    <td><CopyableCode code="fhirMapping" /></td>
    <td><code>object</code></td>
    <td>FHIR Mappings. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fhirServiceResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of the FHIR service to connect to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Deleting", "Succeeded", "Creating", "Accepted", "Verifying", "Updating", "Failed", "Canceled", "Deprovisioned", "Moving", "Suspended", "Warned", and "SystemMaintenance". (Deleting, Succeeded, Creating, Accepted, Verifying, Updating, Failed, Canceled, Deprovisioned, Moving, Suspended, Warned, SystemMaintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceIdentityResolutionType" /></td>
    <td><code>string</code></td>
    <td>Determines how resource identity is resolved on the destination. Required. Known values are: "Create" and "Lookup". (Create, Lookup)</td>
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
    <td><a href="#list_by_iot_connector"><CopyableCode code="list_by_iot_connector" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-iot_connector_name"><code>iot_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all FHIR destinations for the given IoT Connector.</td>
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
<tr id="parameter-iot_connector_name">
    <td><CopyableCode code="iot_connector_name" /></td>
    <td><code>string</code></td>
    <td>The name of IoT Connector resource. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of workspace resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_iot_connector"
    values={[
        { label: 'list_by_iot_connector', value: 'list_by_iot_connector' }
    ]}
>
<TabItem value="list_by_iot_connector">

Lists all FHIR destinations for the given IoT Connector.

```sql
SELECT
id,
name,
etag,
fhirMapping,
fhirServiceResourceId,
location,
provisioningState,
resourceIdentityResolutionType,
systemData,
type
FROM azure_extras.health_data_services.fhir_destinations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND iot_connector_name = '{{ iot_connector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
