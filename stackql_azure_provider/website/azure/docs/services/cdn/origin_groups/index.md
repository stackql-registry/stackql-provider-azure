--- 
title: origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_groups
  - cdn
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

Creates, updates, deletes, gets or lists an <code>origin_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="origin_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.origin_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_endpoint', value: 'list_by_endpoint' }
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
    <td><CopyableCode code="healthProbeSettings" /></td>
    <td><code>object</code></td>
    <td>Health probe settings to the origin that is used to determine the health of the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The source of the content being delivered via CDN within given origin group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the origin group. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the origin group. Known values are: "Creating", "Active", and "Deleting". (Creating, Active, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="responseBasedOriginErrorDetectionSettings" /></td>
    <td><code>object</code></td>
    <td>The JSON object that contains the properties to determine origin health using real requests/responses. This property is currently not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRestorationTimeToHealedOrNewEndpointsInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_endpoint">

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
    <td><CopyableCode code="healthProbeSettings" /></td>
    <td><code>object</code></td>
    <td>Health probe settings to the origin that is used to determine the health of the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The source of the content being delivered via CDN within given origin group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the origin group. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the origin group. Known values are: "Creating", "Active", and "Deleting". (Creating, Active, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="responseBasedOriginErrorDetectionSettings" /></td>
    <td><code>object</code></td>
    <td>The JSON object that contains the properties to determine origin health using real requests/responses. This property is currently not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRestorationTimeToHealedOrNewEndpointsInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing origin group within an endpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_endpoint"><CopyableCode code="list_by_endpoint" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the existing origin groups within an endpoint.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new origin group within the specified endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing origin group within an endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing origin group within an endpoint.</td>
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
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of the endpoint under the profile which is unique globally. Required.</td>
</tr>
<tr id="parameter-origin_group_name">
    <td><CopyableCode code="origin_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the origin group which is unique within the endpoint. Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group. Required.</td>
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
        { label: 'list_by_endpoint', value: 'list_by_endpoint' }
    ]}
>
<TabItem value="get">

Gets an existing origin group within an endpoint.

```sql
SELECT
id,
name,
healthProbeSettings,
origins,
provisioningState,
resourceState,
responseBasedOriginErrorDetectionSettings,
systemData,
trafficRestorationTimeToHealedOrNewEndpointsInMinutes,
type
FROM azure.cdn.origin_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND origin_group_name = '{{ origin_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_endpoint">

Lists all of the existing origin groups within an endpoint.

```sql
SELECT
id,
name,
healthProbeSettings,
origins,
provisioningState,
resourceState,
responseBasedOriginErrorDetectionSettings,
systemData,
trafficRestorationTimeToHealedOrNewEndpointsInMinutes,
type
FROM azure.cdn.origin_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
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

Creates a new origin group within the specified endpoint.

```sql
INSERT INTO azure.cdn.origin_groups (
properties,
resource_group_name,
profile_name,
endpoint_name,
origin_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ endpoint_name }}',
'{{ origin_group_name }}',
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
- name: origin_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the origin_groups resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the origin_groups resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the origin_groups resource.
    - name: origin_group_name
      value: "{{ origin_group_name }}"
      description: Required parameter for the origin_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the origin_groups resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the origin group.
      value:
        healthProbeSettings:
          probePath: "{{ probePath }}"
          probeRequestType: "{{ probeRequestType }}"
          probeProtocol: "{{ probeProtocol }}"
          probeIntervalInSeconds: {{ probeIntervalInSeconds }}
        origins:
          - id: "{{ id }}"
        trafficRestorationTimeToHealedOrNewEndpointsInMinutes: {{ trafficRestorationTimeToHealedOrNewEndpointsInMinutes }}
        responseBasedOriginErrorDetectionSettings:
          responseBasedDetectedErrorTypes: "{{ responseBasedDetectedErrorTypes }}"
          responseBasedFailoverThresholdPercentage: {{ responseBasedFailoverThresholdPercentage }}
          httpErrorRanges:
            - begin: {{ begin }}
              end: {{ end }}
        resourceState: "{{ resourceState }}"
        provisioningState: "{{ provisioningState }}"
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

Updates an existing origin group within an endpoint.

```sql
UPDATE azure.cdn.origin_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND origin_group_name = '{{ origin_group_name }}' --required
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

Deletes an existing origin group within an endpoint.

```sql
DELETE FROM azure.cdn.origin_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND origin_group_name = '{{ origin_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
