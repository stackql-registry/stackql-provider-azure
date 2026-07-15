--- 
title: iot_connector_fhir_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_connector_fhir_destination
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

Creates, updates, deletes, gets or lists an <code>iot_connector_fhir_destination</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iot_connector_fhir_destination" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_data_services.iot_connector_fhir_destination" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-iot_connector_name"><code>iot_connector_name</code></a>, <a href="#parameter-fhir_destination_name"><code>fhir_destination_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the specified Iot Connector FHIR destination.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-iot_connector_name"><code>iot_connector_name</code></a>, <a href="#parameter-fhir_destination_name"><code>fhir_destination_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an IoT Connector FHIR destination resource with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-iot_connector_name"><code>iot_connector_name</code></a>, <a href="#parameter-fhir_destination_name"><code>fhir_destination_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an IoT Connector FHIR destination resource with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-iot_connector_name"><code>iot_connector_name</code></a>, <a href="#parameter-fhir_destination_name"><code>fhir_destination_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an IoT Connector FHIR destination.</td>
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
<tr id="parameter-fhir_destination_name">
    <td><CopyableCode code="fhir_destination_name" /></td>
    <td><code>string</code></td>
    <td>The name of IoT Connector FHIR destination resource. Required.</td>
</tr>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the properties of the specified Iot Connector FHIR destination.

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
FROM azure_extras.health_data_services.iot_connector_fhir_destination
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND iot_connector_name = '{{ iot_connector_name }}' -- required
AND fhir_destination_name = '{{ fhir_destination_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates an IoT Connector FHIR destination resource with the specified parameters.

```sql
INSERT INTO azure_extras.health_data_services.iot_connector_fhir_destination (
properties,
etag,
location,
resource_group_name,
workspace_name,
iot_connector_name,
fhir_destination_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ etag }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ iot_connector_name }}',
'{{ fhir_destination_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: iot_connector_fhir_destination
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the iot_connector_fhir_destination resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the iot_connector_fhir_destination resource.
    - name: iot_connector_name
      value: "{{ iot_connector_name }}"
      description: Required parameter for the iot_connector_fhir_destination resource.
    - name: fhir_destination_name
      value: "{{ fhir_destination_name }}"
      description: Required parameter for the iot_connector_fhir_destination resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the iot_connector_fhir_destination resource.
    - name: properties
      description: |
        IoT FHIR Destination settings. Required.
      value:
        provisioningState: "{{ provisioningState }}"
        resourceIdentityResolutionType: "{{ resourceIdentityResolutionType }}"
        fhirServiceResourceId: "{{ fhirServiceResourceId }}"
        fhirMapping:
          content: "{{ content }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        An etag associated with the resource, used for optimistic concurrency when editing it.
    - name: location
      value: "{{ location }}"
      description: |
        The resource location.
`}</CodeBlock>

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

Creates or updates an IoT Connector FHIR destination resource with the specified parameters.

```sql
REPLACE azure_extras.health_data_services.iot_connector_fhir_destination
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND iot_connector_name = '{{ iot_connector_name }}' --required
AND fhir_destination_name = '{{ fhir_destination_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
location,
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

Deletes an IoT Connector FHIR destination.

```sql
DELETE FROM azure_extras.health_data_services.iot_connector_fhir_destination
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND iot_connector_name = '{{ iot_connector_name }}' --required
AND fhir_destination_name = '{{ fhir_destination_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
