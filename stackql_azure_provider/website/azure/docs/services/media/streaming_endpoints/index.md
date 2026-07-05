--- 
title: streaming_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_endpoints
  - media
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

Creates, updates, deletes, gets or lists a <code>streaming_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="streaming_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media.streaming_endpoints" /></td></tr>
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
    <td><CopyableCode code="accessControl" /></td>
    <td><code>object</code></td>
    <td>The access control definition of the streaming endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySetName" /></td>
    <td><code>string</code></td>
    <td>This feature is deprecated, do not set a value for this property.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The CDN enabled flag.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnProfile" /></td>
    <td><code>string</code></td>
    <td>The CDN profile name.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnProvider" /></td>
    <td><code>string</code></td>
    <td>The CDN provider name.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The exact time the streaming endpoint was created.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSiteAccessPolicies" /></td>
    <td><code>object</code></td>
    <td>The streaming endpoint access policies.</td>
</tr>
<tr>
    <td><CopyableCode code="customHostNames" /></td>
    <td><code>array</code></td>
    <td>The custom host names of the streaming endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The streaming endpoint description.</td>
</tr>
<tr>
    <td><CopyableCode code="freeTrialEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The free trial expiration time.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The streaming endpoint host name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The exact time the streaming endpoint was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCacheAge" /></td>
    <td><code>integer</code></td>
    <td>Max cache age.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the streaming endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>The resource state of the streaming endpoint. Known values are: "Stopped", "Starting", "Running", "Stopping", "Deleting", and "Scaling".</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnits" /></td>
    <td><code>integer</code></td>
    <td>The number of scale units. Use the Scale operation to adjust this value.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The streaming endpoint sku.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><CopyableCode code="accessControl" /></td>
    <td><code>object</code></td>
    <td>The access control definition of the streaming endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySetName" /></td>
    <td><code>string</code></td>
    <td>This feature is deprecated, do not set a value for this property.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The CDN enabled flag.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnProfile" /></td>
    <td><code>string</code></td>
    <td>The CDN profile name.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnProvider" /></td>
    <td><code>string</code></td>
    <td>The CDN provider name.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The exact time the streaming endpoint was created.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSiteAccessPolicies" /></td>
    <td><code>object</code></td>
    <td>The streaming endpoint access policies.</td>
</tr>
<tr>
    <td><CopyableCode code="customHostNames" /></td>
    <td><code>array</code></td>
    <td>The custom host names of the streaming endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The streaming endpoint description.</td>
</tr>
<tr>
    <td><CopyableCode code="freeTrialEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The free trial expiration time.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The streaming endpoint host name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The exact time the streaming endpoint was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCacheAge" /></td>
    <td><code>integer</code></td>
    <td>Max cache age.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the streaming endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>The resource state of the streaming endpoint. Known values are: "Stopped", "Starting", "Running", "Stopping", "Deleting", and "Scaling".</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnits" /></td>
    <td><code>integer</code></td>
    <td>The number of scale units. Use the Scale operation to adjust this value.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The streaming endpoint sku.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get StreamingEndpoint. Gets a streaming endpoint.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List StreamingEndpoints. Lists the streaming endpoints in the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-autoStart"><code>autoStart</code></a></td>
    <td>Create StreamingEndpoint. Creates a streaming endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Update StreamingEndpoint. Updates a existing streaming endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete StreamingEndpoint. Deletes a streaming endpoint.</td>
</tr>
<tr>
    <td><a href="#skus"><CopyableCode code="skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List StreamingEndpoint skus. List streaming endpoint supported skus.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start StreamingEndpoint. Starts an existing streaming endpoint.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop StreamingEndpoint. Stops an existing streaming endpoint.</td>
</tr>
<tr>
    <td><a href="#scale"><CopyableCode code="scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Scale StreamingEndpoint. Scales an existing streaming endpoint.</td>
</tr>
<tr>
    <td><a href="#async_operation"><CopyableCode code="async_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get operation status. Get a streaming endpoint operation status.</td>
</tr>
<tr>
    <td><a href="#operation_location"><CopyableCode code="operation_location" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_endpoint_name"><code>streaming_endpoint_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get operation status. Get a streaming endpoint operation status.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The Media Services account name. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The ID of an ongoing async operation. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group within the Azure subscription. Required.</td>
</tr>
<tr id="parameter-streaming_endpoint_name">
    <td><CopyableCode code="streaming_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the streaming endpoint, maximum length is 24. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-autoStart">
    <td><CopyableCode code="autoStart" /></td>
    <td><code>boolean</code></td>
    <td>The flag indicates if the resource should be automatically started on creation. Default value is None.</td>
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

Get StreamingEndpoint. Gets a streaming endpoint.

```sql
SELECT
id,
name,
accessControl,
availabilitySetName,
cdnEnabled,
cdnProfile,
cdnProvider,
created,
crossSiteAccessPolicies,
customHostNames,
description,
freeTrialEndTime,
hostName,
lastModified,
location,
maxCacheAge,
provisioningState,
resourceState,
scaleUnits,
sku,
systemData,
tags,
type
FROM azure.media.streaming_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND streaming_endpoint_name = '{{ streaming_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List StreamingEndpoints. Lists the streaming endpoints in the account.

```sql
SELECT
id,
name,
accessControl,
availabilitySetName,
cdnEnabled,
cdnProfile,
cdnProvider,
created,
crossSiteAccessPolicies,
customHostNames,
description,
freeTrialEndTime,
hostName,
lastModified,
location,
maxCacheAge,
provisioningState,
resourceState,
scaleUnits,
sku,
systemData,
tags,
type
FROM azure.media.streaming_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
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

Create StreamingEndpoint. Creates a streaming endpoint.

```sql
INSERT INTO azure.media.streaming_endpoints (
tags,
location,
sku,
properties,
resource_group_name,
account_name,
streaming_endpoint_name,
subscription_id,
autoStart
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ sku }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ streaming_endpoint_name }}',
'{{ subscription_id }}',
'{{ autoStart }}'
RETURNING
id,
name,
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
- name: streaming_endpoints
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the streaming_endpoints resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the streaming_endpoints resource.
    - name: streaming_endpoint_name
      value: "{{ streaming_endpoint_name }}"
      description: Required parameter for the streaming_endpoints resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the streaming_endpoints resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: sku
      description: |
        The streaming endpoint sku.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
    - name: properties
      value:
        description: "{{ description }}"
        scaleUnits: {{ scaleUnits }}
        availabilitySetName: "{{ availabilitySetName }}"
        accessControl:
          akamai:
            akamaiSignatureHeaderAuthenticationKeyList:
              - identifier: "{{ identifier }}"
                base64Key: "{{ base64Key }}"
                expiration: "{{ expiration }}"
          ip:
            allow:
              - name: "{{ name }}"
                address: "{{ address }}"
                subnetPrefixLength: {{ subnetPrefixLength }}
        maxCacheAge: {{ maxCacheAge }}
        customHostNames:
          - "{{ customHostNames }}"
        cdnEnabled: {{ cdnEnabled }}
        cdnProvider: "{{ cdnProvider }}"
        cdnProfile: "{{ cdnProfile }}"
        crossSiteAccessPolicies:
          clientAccessPolicy: "{{ clientAccessPolicy }}"
          crossDomainPolicy: "{{ crossDomainPolicy }}"
    - name: autoStart
      value: {{ autoStart }}
      description: The flag indicates if the resource should be automatically started on creation. Default value is None.
      description: The flag indicates if the resource should be automatically started on creation. Default value is None.
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

Update StreamingEndpoint. Updates a existing streaming endpoint.

```sql
UPDATE azure.media.streaming_endpoints
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND streaming_endpoint_name = '{{ streaming_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete StreamingEndpoint. Deletes a streaming endpoint.

```sql
DELETE FROM azure.media.streaming_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND streaming_endpoint_name = '{{ streaming_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="skus"
    values={[
        { label: 'skus', value: 'skus' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'scale', value: 'scale' },
        { label: 'async_operation', value: 'async_operation' },
        { label: 'operation_location', value: 'operation_location' }
    ]}
>
<TabItem value="skus">

List StreamingEndpoint skus. List streaming endpoint supported skus.

```sql
EXEC azure.media.streaming_endpoints.skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@streaming_endpoint_name='{{ streaming_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start StreamingEndpoint. Starts an existing streaming endpoint.

```sql
EXEC azure.media.streaming_endpoints.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@streaming_endpoint_name='{{ streaming_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop StreamingEndpoint. Stops an existing streaming endpoint.

```sql
EXEC azure.media.streaming_endpoints.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@streaming_endpoint_name='{{ streaming_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="scale">

Scale StreamingEndpoint. Scales an existing streaming endpoint.

```sql
EXEC azure.media.streaming_endpoints.scale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@streaming_endpoint_name='{{ streaming_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"scaleUnit": {{ scaleUnit }}
}'
;
```
</TabItem>
<TabItem value="async_operation">

Get operation status. Get a streaming endpoint operation status.

```sql
EXEC azure.media.streaming_endpoints.async_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="operation_location">

Get operation status. Get a streaming endpoint operation status.

```sql
EXEC azure.media.streaming_endpoints.operation_location 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@streaming_endpoint_name='{{ streaming_endpoint_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
