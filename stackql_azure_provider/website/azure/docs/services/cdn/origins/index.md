--- 
title: origins
hide_title: false
hide_table_of_contents: false
keywords:
  - origins
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

Creates, updates, deletes, gets or lists an <code>origins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="origins" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.origins" /></td></tr>
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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Origin is enabled for load balancing or not.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="httpPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTP port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTPS port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="originHostHeader" /></td>
    <td><code>string</code></td>
    <td>The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStatus" /></td>
    <td><code>string</code></td>
    <td>The approval status for the connection to the Private Link. Known values are: "Pending", "Approved", "Rejected", "Disconnected", and "Timeout". (Pending, Approved, Rejected, Disconnected, Timeout)</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkAlias" /></td>
    <td><code>string</code></td>
    <td>The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkApprovalMessage" /></td>
    <td><code>string</code></td>
    <td>A custom message to be included in the approval request to connect to the Private Link.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the origin. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the origin. Known values are: "Creating", "Active", and "Deleting". (Creating, Active, Deleting)</td>
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
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>Weight of the origin in given origin group for load balancing. Must be between 1 and 1000.</td>
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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Origin is enabled for load balancing or not.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="httpPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTP port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTPS port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="originHostHeader" /></td>
    <td><code>string</code></td>
    <td>The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStatus" /></td>
    <td><code>string</code></td>
    <td>The approval status for the connection to the Private Link. Known values are: "Pending", "Approved", "Rejected", "Disconnected", and "Timeout". (Pending, Approved, Rejected, Disconnected, Timeout)</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkAlias" /></td>
    <td><code>string</code></td>
    <td>The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkApprovalMessage" /></td>
    <td><code>string</code></td>
    <td>A custom message to be included in the approval request to connect to the Private Link.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the origin. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the origin. Known values are: "Creating", "Active", and "Deleting". (Creating, Active, Deleting)</td>
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
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>Weight of the origin in given origin group for load balancing. Must be between 1 and 1000.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing origin within an endpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_endpoint"><CopyableCode code="list_by_endpoint" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the existing origins within an endpoint.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new origin within the specified endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing origin within an endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing origin within an endpoint.</td>
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
<tr id="parameter-origin_name">
    <td><CopyableCode code="origin_name" /></td>
    <td><code>string</code></td>
    <td>Name of the origin which is unique within the endpoint. Required.</td>
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

Gets an existing origin within an endpoint.

```sql
SELECT
id,
name,
enabled,
hostName,
httpPort,
httpsPort,
originHostHeader,
priority,
privateEndpointStatus,
privateLinkAlias,
privateLinkApprovalMessage,
privateLinkLocation,
privateLinkResourceId,
provisioningState,
resourceState,
systemData,
type,
weight
FROM azure.cdn.origins
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND origin_name = '{{ origin_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_endpoint">

Lists all of the existing origins within an endpoint.

```sql
SELECT
id,
name,
enabled,
hostName,
httpPort,
httpsPort,
originHostHeader,
priority,
privateEndpointStatus,
privateLinkAlias,
privateLinkApprovalMessage,
privateLinkLocation,
privateLinkResourceId,
provisioningState,
resourceState,
systemData,
type,
weight
FROM azure.cdn.origins
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

Creates a new origin within the specified endpoint.

```sql
INSERT INTO azure.cdn.origins (
properties,
resource_group_name,
profile_name,
endpoint_name,
origin_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ endpoint_name }}',
'{{ origin_name }}',
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
- name: origins
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the origins resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the origins resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the origins resource.
    - name: origin_name
      value: "{{ origin_name }}"
      description: Required parameter for the origins resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the origins resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the origin.
      value:
        hostName: "{{ hostName }}"
        httpPort: {{ httpPort }}
        httpsPort: {{ httpsPort }}
        originHostHeader: "{{ originHostHeader }}"
        priority: {{ priority }}
        weight: {{ weight }}
        enabled: {{ enabled }}
        privateLinkAlias: "{{ privateLinkAlias }}"
        privateLinkResourceId: "{{ privateLinkResourceId }}"
        privateLinkLocation: "{{ privateLinkLocation }}"
        privateLinkApprovalMessage: "{{ privateLinkApprovalMessage }}"
        resourceState: "{{ resourceState }}"
        provisioningState: "{{ provisioningState }}"
        privateEndpointStatus: "{{ privateEndpointStatus }}"
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

Updates an existing origin within an endpoint.

```sql
UPDATE azure.cdn.origins
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND origin_name = '{{ origin_name }}' --required
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

Deletes an existing origin within an endpoint.

```sql
DELETE FROM azure.cdn.origins
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND origin_name = '{{ origin_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
