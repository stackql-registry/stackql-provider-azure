--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - appplatform
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appplatform.services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified dns name of the service instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The GEO location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceResource" /></td>
    <td><code>object</code></td>
    <td>Purchasing 3rd party product of the Service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network profile of the Service.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Power state of the Service. Known values are: "Running" and "Stopped".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Service. Known values are: "Creating", "Updating", "Starting", "Stopping", "Deleting", "Deleted", "Succeeded", "Failed", "Moving", "Moved", and "MoveFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceId" /></td>
    <td><code>string</code></td>
    <td>ServiceInstanceEntity Id which uniquely identifies a created resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags of the service which is a list of key value pairs that describe the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>Version of the Service.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetAddons" /></td>
    <td><code>object</code></td>
    <td>Additional Service settings in vnet injection instance.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>:vartype zone_redundant: bool</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified dns name of the service instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The GEO location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceResource" /></td>
    <td><code>object</code></td>
    <td>Purchasing 3rd party product of the Service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network profile of the Service.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Power state of the Service. Known values are: "Running" and "Stopped".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Service. Known values are: "Creating", "Updating", "Starting", "Stopping", "Deleting", "Deleted", "Succeeded", "Failed", "Moving", "Moved", and "MoveFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceId" /></td>
    <td><code>string</code></td>
    <td>ServiceInstanceEntity Id which uniquely identifies a created resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags of the service which is a list of key value pairs that describe the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>Version of the Service.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetAddons" /></td>
    <td><code>object</code></td>
    <td>Additional Service settings in vnet injection instance.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>:vartype zone_redundant: bool</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified dns name of the service instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The GEO location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceResource" /></td>
    <td><code>object</code></td>
    <td>Purchasing 3rd party product of the Service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network profile of the Service.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Power state of the Service. Known values are: "Running" and "Stopped".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Service. Known values are: "Creating", "Updating", "Starting", "Stopping", "Deleting", "Deleted", "Succeeded", "Failed", "Moving", "Moved", and "MoveFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceId" /></td>
    <td><code>string</code></td>
    <td>ServiceInstanceEntity Id which uniquely identifies a created resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Service resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags of the service which is a list of key value pairs that describe the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>Version of the Service.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetAddons" /></td>
    <td><code>object</code></td>
    <td>Additional Service settings in vnet injection instance.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>:vartype zone_redundant: bool</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Service and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Service or update an exiting Service.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to update an exiting Service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Service or update an exiting Service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to delete a Service.</td>
</tr>
<tr>
    <td><a href="#list_test_keys"><CopyableCode code="list_test_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List test keys for a Service.</td>
</tr>
<tr>
    <td><a href="#list_supported_apm_types"><CopyableCode code="list_supported_apm_types" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List supported APM types for a Service.</td>
</tr>
<tr>
    <td><a href="#list_globally_enabled_apms"><CopyableCode code="list_globally_enabled_apms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List globally enabled APMs for a Service.</td>
</tr>
<tr>
    <td><a href="#list_supported_server_versions"><CopyableCode code="list_supported_server_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the available server versions supported by Microsoft.AppPlatform provider.</td>
</tr>
<tr>
    <td><a href="#regenerate_test_key"><CopyableCode code="regenerate_test_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyType"><code>keyType</code></a></td>
    <td></td>
    <td>Regenerate a test key for a Service.</td>
</tr>
<tr>
    <td><a href="#disable_test_endpoint"><CopyableCode code="disable_test_endpoint" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable test endpoint functionality for a Service.</td>
</tr>
<tr>
    <td><a href="#enable_test_endpoint"><CopyableCode code="enable_test_endpoint" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enable test endpoint functionality for a Service.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop a Service.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start a Service.</td>
</tr>
<tr>
    <td><a href="#flush_vnet_dns_setting"><CopyableCode code="flush_vnet_dns_setting" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Flush Virtual Network DNS settings for a VNET injected Service.</td>
</tr>
<tr>
    <td><a href="#enable_apm_globally"><CopyableCode code="enable_apm_globally" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceId"><code>resourceId</code></a></td>
    <td></td>
    <td>Enable an APM globally.</td>
</tr>
<tr>
    <td><a href="#disable_apm_globally"><CopyableCode code="disable_apm_globally" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceId"><code>resourceId</code></a></td>
    <td></td>
    <td>Disable an APM globally.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Checks that the resource name is valid and is not already in use.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the region. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Service resource. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a Service and its properties.

```sql
SELECT
id,
name,
fqdn,
location,
marketplaceResource,
networkProfile,
powerState,
provisioningState,
serviceId,
sku,
systemData,
tags,
type,
version,
vnetAddons,
zoneRedundant
FROM azure.appplatform.services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Handles requests to list all resources in a resource group.

```sql
SELECT
id,
name,
fqdn,
location,
marketplaceResource,
networkProfile,
powerState,
provisioningState,
serviceId,
sku,
systemData,
tags,
type,
version,
vnetAddons,
zoneRedundant
FROM azure.appplatform.services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Handles requests to list all resources in a subscription.

```sql
SELECT
id,
name,
fqdn,
location,
marketplaceResource,
networkProfile,
powerState,
provisioningState,
serviceId,
sku,
systemData,
tags,
type,
version,
vnetAddons,
zoneRedundant
FROM azure.appplatform.services
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

Create a new Service or update an exiting Service.

```sql
INSERT INTO azure.appplatform.services (
location,
tags,
properties,
sku,
resource_group_name,
service_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ subscription_id }}'
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
- name: services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the services resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the services resource.
    - name: location
      value: "{{ location }}"
      description: |
        The GEO location of the resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tags of the service which is a list of key value pairs that describe the resource.
    - name: properties
      description: |
        Properties of the Service resource.
      value:
        provisioningState: "{{ provisioningState }}"
        networkProfile:
          serviceRuntimeSubnetId: "{{ serviceRuntimeSubnetId }}"
          appSubnetId: "{{ appSubnetId }}"
          serviceCidr: "{{ serviceCidr }}"
          serviceRuntimeNetworkResourceGroup: "{{ serviceRuntimeNetworkResourceGroup }}"
          appNetworkResourceGroup: "{{ appNetworkResourceGroup }}"
          outboundIPs:
            publicIPs:
              - "{{ publicIPs }}"
          requiredTraffics:
            - protocol: "{{ protocol }}"
              port: {{ port }}
              ips: "{{ ips }}"
              fqdns: "{{ fqdns }}"
              direction: "{{ direction }}"
          ingressConfig:
            readTimeoutInSeconds: {{ readTimeoutInSeconds }}
          outboundType: "{{ outboundType }}"
        vnetAddons:
          logStreamPublicEndpoint: {{ logStreamPublicEndpoint }}
          dataPlanePublicEndpoint: {{ dataPlanePublicEndpoint }}
        version: {{ version }}
        serviceId: "{{ serviceId }}"
        powerState: "{{ powerState }}"
        zoneRedundant: {{ zoneRedundant }}
        fqdn: "{{ fqdn }}"
        marketplaceResource:
          plan: "{{ plan }}"
          publisher: "{{ publisher }}"
          product: "{{ product }}"
    - name: sku
      description: |
        Sku of the Service resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
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

Operation to update an exiting Service.

```sql
UPDATE azure.appplatform.services
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a new Service or update an exiting Service.

```sql
REPLACE azure.appplatform.services
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Operation to delete a Service.

```sql
DELETE FROM azure.appplatform.services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_test_keys"
    values={[
        { label: 'list_test_keys', value: 'list_test_keys' },
        { label: 'list_supported_apm_types', value: 'list_supported_apm_types' },
        { label: 'list_globally_enabled_apms', value: 'list_globally_enabled_apms' },
        { label: 'list_supported_server_versions', value: 'list_supported_server_versions' },
        { label: 'regenerate_test_key', value: 'regenerate_test_key' },
        { label: 'disable_test_endpoint', value: 'disable_test_endpoint' },
        { label: 'enable_test_endpoint', value: 'enable_test_endpoint' },
        { label: 'stop', value: 'stop' },
        { label: 'start', value: 'start' },
        { label: 'flush_vnet_dns_setting', value: 'flush_vnet_dns_setting' },
        { label: 'enable_apm_globally', value: 'enable_apm_globally' },
        { label: 'disable_apm_globally', value: 'disable_apm_globally' },
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="list_test_keys">

List test keys for a Service.

```sql
EXEC azure.appplatform.services.list_test_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_supported_apm_types">

List supported APM types for a Service.

```sql
EXEC azure.appplatform.services.list_supported_apm_types 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_globally_enabled_apms">

List globally enabled APMs for a Service.

```sql
EXEC azure.appplatform.services.list_globally_enabled_apms 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_supported_server_versions">

Lists all of the available server versions supported by Microsoft.AppPlatform provider.

```sql
EXEC azure.appplatform.services.list_supported_server_versions 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_test_key">

Regenerate a test key for a Service.

```sql
EXEC azure.appplatform.services.regenerate_test_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyType": "{{ keyType }}"
}'
;
```
</TabItem>
<TabItem value="disable_test_endpoint">

Disable test endpoint functionality for a Service.

```sql
EXEC azure.appplatform.services.disable_test_endpoint 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_test_endpoint">

Enable test endpoint functionality for a Service.

```sql
EXEC azure.appplatform.services.enable_test_endpoint 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop a Service.

```sql
EXEC azure.appplatform.services.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start a Service.

```sql
EXEC azure.appplatform.services.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="flush_vnet_dns_setting">

Flush Virtual Network DNS settings for a VNET injected Service.

```sql
EXEC azure.appplatform.services.flush_vnet_dns_setting 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_apm_globally">

Enable an APM globally.

```sql
EXEC azure.appplatform.services.enable_apm_globally 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceId": "{{ resourceId }}"
}'
;
```
</TabItem>
<TabItem value="disable_apm_globally">

Disable an APM globally.

```sql
EXEC azure.appplatform.services.disable_apm_globally 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceId": "{{ resourceId }}"
}'
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks that the resource name is valid and is not already in use.

```sql
EXEC azure.appplatform.services.check_name_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"type": "{{ type }}", 
"name": "{{ name }}"
}'
;
```
</TabItem>
</Tabs>
