--- 
title: gateway_route_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_route_configs
  - app_platform
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

Creates, updates, deletes, gets or lists a <code>gateway_route_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gateway_route_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_platform.gateway_route_configs" /></td></tr>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="appResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the Azure Spring Apps app, required unless route defines `uri`.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>To modify the request before sending it to the target endpoint, or the received response in app level.</td>
</tr>
<tr>
    <td><CopyableCode code="openApi" /></td>
    <td><code>object</code></td>
    <td>OpenAPI properties of Spring Cloud Gateway route config.</td>
</tr>
<tr>
    <td><CopyableCode code="predicates" /></td>
    <td><code>array</code></td>
    <td>A number of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Protocol of routed Azure Spring Apps applications. Known values are: "HTTP" and "HTTPS".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Spring Cloud Gateway route config. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>Array of API routes, each route contains properties such as `title`\ , `uri`\ , `ssoEnabled`\ , `predicates`\ , `filters`.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enable Single Sign-On in app level.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><CopyableCode code="appResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the Azure Spring Apps app, required unless route defines `uri`.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>To modify the request before sending it to the target endpoint, or the received response in app level.</td>
</tr>
<tr>
    <td><CopyableCode code="openApi" /></td>
    <td><code>object</code></td>
    <td>OpenAPI properties of Spring Cloud Gateway route config.</td>
</tr>
<tr>
    <td><CopyableCode code="predicates" /></td>
    <td><code>array</code></td>
    <td>A number of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Protocol of routed Azure Spring Apps applications. Known values are: "HTTP" and "HTTPS".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Spring Cloud Gateway route config. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>Array of API routes, each route contains properties such as `title`\ , `uri`\ , `ssoEnabled`\ , `predicates`\ , `filters`.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enable Single Sign-On in app level.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-route_config_name"><code>route_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Spring Cloud Gateway route configs.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handle requests to list all Spring Cloud Gateway route configs.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-route_config_name"><code>route_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create the default Spring Cloud Gateway route configs or update the existing Spring Cloud Gateway route configs.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-route_config_name"><code>route_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create the default Spring Cloud Gateway route configs or update the existing Spring Cloud Gateway route configs.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-route_config_name"><code>route_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the Spring Cloud Gateway route config.</td>
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
<tr id="parameter-gateway_name">
    <td><CopyableCode code="gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of Spring Cloud Gateway. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-route_config_name">
    <td><CopyableCode code="route_config_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Spring Cloud Gateway route config. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the Spring Cloud Gateway route configs.

```sql
SELECT
id,
name,
appResourceId,
filters,
openApi,
predicates,
protocol,
provisioningState,
routes,
ssoEnabled,
systemData,
type
FROM azure_extras.app_platform.gateway_route_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND route_config_name = '{{ route_config_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Handle requests to list all Spring Cloud Gateway route configs.

```sql
SELECT
id,
name,
appResourceId,
filters,
openApi,
predicates,
protocol,
provisioningState,
routes,
ssoEnabled,
systemData,
type
FROM azure_extras.app_platform.gateway_route_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
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

Create the default Spring Cloud Gateway route configs or update the existing Spring Cloud Gateway route configs.

```sql
INSERT INTO azure_extras.app_platform.gateway_route_configs (
properties,
resource_group_name,
service_name,
gateway_name,
route_config_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ gateway_name }}',
'{{ route_config_name }}',
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
- name: gateway_route_configs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the gateway_route_configs resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the gateway_route_configs resource.
    - name: gateway_name
      value: "{{ gateway_name }}"
      description: Required parameter for the gateway_route_configs resource.
    - name: route_config_name
      value: "{{ route_config_name }}"
      description: Required parameter for the gateway_route_configs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the gateway_route_configs resource.
    - name: properties
      description: |
        API route config of the Spring Cloud Gateway.
      value:
        provisioningState: "{{ provisioningState }}"
        appResourceId: "{{ appResourceId }}"
        openApi:
          uri: "{{ uri }}"
        protocol: "{{ protocol }}"
        routes:
          - title: "{{ title }}"
            description: "{{ description }}"
            uri: "{{ uri }}"
            ssoEnabled: {{ ssoEnabled }}
            tokenRelay: {{ tokenRelay }}
            predicates: "{{ predicates }}"
            filters: "{{ filters }}"
            order: {{ order }}
            tags: "{{ tags }}"
        ssoEnabled: {{ ssoEnabled }}
        predicates:
          - "{{ predicates }}"
        filters:
          - "{{ filters }}"
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

Create the default Spring Cloud Gateway route configs or update the existing Spring Cloud Gateway route configs.

```sql
REPLACE azure_extras.app_platform.gateway_route_configs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND route_config_name = '{{ route_config_name }}' --required
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

Delete the Spring Cloud Gateway route config.

```sql
DELETE FROM azure_extras.app_platform.gateway_route_configs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND route_config_name = '{{ route_config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
