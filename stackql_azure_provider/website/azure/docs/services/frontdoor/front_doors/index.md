--- 
title: front_doors
hide_title: false
hide_table_of_contents: false
keywords:
  - front_doors
  - frontdoor
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

Creates, updates, deletes, gets or lists a <code>front_doors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="front_doors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.frontdoor.front_doors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPools" /></td>
    <td><code>array</code></td>
    <td>Backend pools available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPoolsSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for all backendPools.</td>
</tr>
<tr>
    <td><CopyableCode code="cname" /></td>
    <td><code>string</code></td>
    <td>The host that each frontendEndpoint must CNAME to.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>A friendly name for the frontDoor.</td>
</tr>
<tr>
    <td><CopyableCode code="frontdoorId" /></td>
    <td><code>string</code></td>
    <td>The Id of the frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendEndpoints" /></td>
    <td><code>array</code></td>
    <td>Frontend endpoints available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="healthProbeSettings" /></td>
    <td><code>array</code></td>
    <td>Health probe settings associated with this Front Door instance.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingSettings" /></td>
    <td><code>array</code></td>
    <td>Load balancing settings associated with this Front Door instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Front Door.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the Front Door or Front Door SubResource. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", "Deleting", "Migrating", and "Migrated". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting, Migrating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="routingRules" /></td>
    <td><code>array</code></td>
    <td>Routing rules associated with this Front Door.</td>
</tr>
<tr>
    <td><CopyableCode code="rulesEngines" /></td>
    <td><code>array</code></td>
    <td>Rules Engine Configurations available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPools" /></td>
    <td><code>array</code></td>
    <td>Backend pools available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPoolsSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for all backendPools.</td>
</tr>
<tr>
    <td><CopyableCode code="cname" /></td>
    <td><code>string</code></td>
    <td>The host that each frontendEndpoint must CNAME to.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>A friendly name for the frontDoor.</td>
</tr>
<tr>
    <td><CopyableCode code="frontdoorId" /></td>
    <td><code>string</code></td>
    <td>The Id of the frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendEndpoints" /></td>
    <td><code>array</code></td>
    <td>Frontend endpoints available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="healthProbeSettings" /></td>
    <td><code>array</code></td>
    <td>Health probe settings associated with this Front Door instance.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingSettings" /></td>
    <td><code>array</code></td>
    <td>Load balancing settings associated with this Front Door instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Front Door.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the Front Door or Front Door SubResource. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", "Deleting", "Migrating", and "Migrated". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting, Migrating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="routingRules" /></td>
    <td><code>array</code></td>
    <td>Routing rules associated with this Front Door.</td>
</tr>
<tr>
    <td><CopyableCode code="rulesEngines" /></td>
    <td><code>array</code></td>
    <td>Rules Engine Configurations available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPools" /></td>
    <td><code>array</code></td>
    <td>Backend pools available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPoolsSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for all backendPools.</td>
</tr>
<tr>
    <td><CopyableCode code="cname" /></td>
    <td><code>string</code></td>
    <td>The host that each frontendEndpoint must CNAME to.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>A friendly name for the frontDoor.</td>
</tr>
<tr>
    <td><CopyableCode code="frontdoorId" /></td>
    <td><code>string</code></td>
    <td>The Id of the frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendEndpoints" /></td>
    <td><code>array</code></td>
    <td>Frontend endpoints available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="healthProbeSettings" /></td>
    <td><code>array</code></td>
    <td>Health probe settings associated with this Front Door instance.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingSettings" /></td>
    <td><code>array</code></td>
    <td>Load balancing settings associated with this Front Door instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Front Door.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the Front Door or Front Door SubResource. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", "Deleting", "Migrating", and "Migrated". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting, Migrating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="routingRules" /></td>
    <td><code>array</code></td>
    <td>Routing rules associated with this Front Door.</td>
</tr>
<tr>
    <td><CopyableCode code="rulesEngines" /></td>
    <td><code>array</code></td>
    <td>Rules Engine Configurations available to routing rules.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Front Door with the specified Front Door name under the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the Front Doors within a resource group under a subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the Front Doors within an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Front Door with a Front Door name under the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Front Door with a Front Door name under the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Front Door with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#validate_custom_domain"><CopyableCode code="validate_custom_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-hostName"><code>hostName</code></a></td>
    <td></td>
    <td>Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS.</td>
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
<tr id="parameter-front_door_name">
    <td><CopyableCode code="front_door_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Front Door which is globally unique. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a Front Door with the specified Front Door name under the specified subscription and resource group.

```sql
SELECT
id,
name,
backendPools,
backendPoolsSettings,
cname,
enabledState,
extendedProperties,
friendlyName,
frontdoorId,
frontendEndpoints,
healthProbeSettings,
loadBalancingSettings,
location,
provisioningState,
resourceState,
routingRules,
rulesEngines,
tags,
type
FROM azure.frontdoor.front_doors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND front_door_name = '{{ front_door_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all of the Front Doors within a resource group under a subscription.

```sql
SELECT
id,
name,
backendPools,
backendPoolsSettings,
cname,
enabledState,
extendedProperties,
friendlyName,
frontdoorId,
frontendEndpoints,
healthProbeSettings,
loadBalancingSettings,
location,
provisioningState,
resourceState,
routingRules,
rulesEngines,
tags,
type
FROM azure.frontdoor.front_doors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all of the Front Doors within an Azure subscription.

```sql
SELECT
id,
name,
backendPools,
backendPoolsSettings,
cname,
enabledState,
extendedProperties,
friendlyName,
frontdoorId,
frontendEndpoints,
healthProbeSettings,
loadBalancingSettings,
location,
provisioningState,
resourceState,
routingRules,
rulesEngines,
tags,
type
FROM azure.frontdoor.front_doors
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

Creates a new Front Door with a Front Door name under the specified subscription and resource group.

```sql
INSERT INTO azure.frontdoor.front_doors (
location,
tags,
properties,
resource_group_name,
front_door_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ front_door_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: front_doors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the front_doors resource.
    - name: front_door_name
      value: "{{ front_door_name }}"
      description: Required parameter for the front_doors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the front_doors resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the Front Door Load Balancer.
      value:
        friendlyName: "{{ friendlyName }}"
        routingRules:
          - id: "{{ id }}"
            properties:
              frontendEndpoints:
                - id: "{{ id }}"
              acceptedProtocols:
                - "{{ acceptedProtocols }}"
              patternsToMatch:
                - "{{ patternsToMatch }}"
              enabledState: "{{ enabledState }}"
              routeConfiguration:
                @odata:
                  type: "{{ type }}"
              rulesEngine:
                id: "{{ id }}"
              webApplicationFirewallPolicyLink:
                id: "{{ id }}"
              resourceState: "{{ resourceState }}"
            name: "{{ name }}"
            type: "{{ type }}"
        loadBalancingSettings:
          - id: "{{ id }}"
            properties:
              sampleSize: {{ sampleSize }}
              successfulSamplesRequired: {{ successfulSamplesRequired }}
              additionalLatencyMilliseconds: {{ additionalLatencyMilliseconds }}
              resourceState: "{{ resourceState }}"
            name: "{{ name }}"
            type: "{{ type }}"
        healthProbeSettings:
          - id: "{{ id }}"
            properties:
              path: "{{ path }}"
              protocol: "{{ protocol }}"
              intervalInSeconds: {{ intervalInSeconds }}
              healthProbeMethod: "{{ healthProbeMethod }}"
              enabledState: "{{ enabledState }}"
              resourceState: "{{ resourceState }}"
            name: "{{ name }}"
            type: "{{ type }}"
        backendPools:
          - id: "{{ id }}"
            properties:
              backends:
                - address: "{{ address }}"
                  privateLinkAlias: "{{ privateLinkAlias }}"
                  privateLinkResourceId: "{{ privateLinkResourceId }}"
                  privateLinkLocation: "{{ privateLinkLocation }}"
                  privateEndpointStatus: "{{ privateEndpointStatus }}"
                  privateLinkApprovalMessage: "{{ privateLinkApprovalMessage }}"
                  httpPort: {{ httpPort }}
                  httpsPort: {{ httpsPort }}
                  enabledState: "{{ enabledState }}"
                  priority: {{ priority }}
                  weight: {{ weight }}
                  backendHostHeader: "{{ backendHostHeader }}"
              loadBalancingSettings:
                id: "{{ id }}"
              healthProbeSettings:
                id: "{{ id }}"
              resourceState: "{{ resourceState }}"
            name: "{{ name }}"
            type: "{{ type }}"
        frontendEndpoints:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              hostName: "{{ hostName }}"
              sessionAffinityEnabledState: "{{ sessionAffinityEnabledState }}"
              sessionAffinityTtlSeconds: {{ sessionAffinityTtlSeconds }}
              webApplicationFirewallPolicyLink:
                id: "{{ id }}"
              resourceState: "{{ resourceState }}"
              customHttpsProvisioningState: "{{ customHttpsProvisioningState }}"
              customHttpsProvisioningSubstate: "{{ customHttpsProvisioningSubstate }}"
              customHttpsConfiguration:
                certificateSource: "{{ certificateSource }}"
                protocolType: "{{ protocolType }}"
                minimumTlsVersion: "{{ minimumTlsVersion }}"
                keyVaultCertificateSourceParameters:
                  vault: "{{ vault }}"
                  secretName: "{{ secretName }}"
                  secretVersion: "{{ secretVersion }}"
                frontDoorCertificateSourceParameters:
                  certificateType: "{{ certificateType }}"
        backendPoolsSettings:
          enforceCertificateNameCheck: "{{ enforceCertificateNameCheck }}"
          sendRecvTimeoutSeconds: {{ sendRecvTimeoutSeconds }}
        enabledState: "{{ enabledState }}"
        resourceState: "{{ resourceState }}"
        provisioningState: "{{ provisioningState }}"
        cname: "{{ cname }}"
        frontdoorId: "{{ frontdoorId }}"
        rulesEngines:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              rules:
                - name: "{{ name }}"
                  priority: {{ priority }}
                  action:
                    requestHeaderActions: "{{ requestHeaderActions }}"
                    responseHeaderActions: "{{ responseHeaderActions }}"
                    routeConfigurationOverride: "{{ routeConfigurationOverride }}"
                  matchConditions: "{{ matchConditions }}"
                  matchProcessingBehavior: "{{ matchProcessingBehavior }}"
              resourceState: "{{ resourceState }}"
        extendedProperties: "{{ extendedProperties }}"
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

Creates a new Front Door with a Front Door name under the specified subscription and resource group.

```sql
REPLACE azure.frontdoor.front_doors
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND front_door_name = '{{ front_door_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Deletes an existing Front Door with the specified parameters.

```sql
DELETE FROM azure.frontdoor.front_doors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND front_door_name = '{{ front_door_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_custom_domain"
    values={[
        { label: 'validate_custom_domain', value: 'validate_custom_domain' }
    ]}
>
<TabItem value="validate_custom_domain">

Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS.

```sql
EXEC azure.frontdoor.front_doors.validate_custom_domain 
@resource_group_name='{{ resource_group_name }}' --required, 
@front_door_name='{{ front_door_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"hostName": "{{ hostName }}"
}'
;
```
</TabItem>
</Tabs>
