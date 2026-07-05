--- 
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
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

Creates, updates, deletes, gets or lists a <code>gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appplatform.gateways" /></td></tr>
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
    <td><CopyableCode code="apiMetadataProperties" /></td>
    <td><code>object</code></td>
    <td>API metadata property for Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="apms" /></td>
    <td><code>array</code></td>
    <td>Collection of ApmReferences in service level.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAuth" /></td>
    <td><code>object</code></td>
    <td>Client-Certification Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="corsProperties" /></td>
    <td><code>object</code></td>
    <td>Cross-Origin Resource Sharing property.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>object</code></td>
    <td>Environment variables of Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsOnly" /></td>
    <td><code>boolean</code></td>
    <td>Indicate if only https is allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>Collection of instances belong to Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of the Spring Cloud Gateway Operator.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Spring Cloud Gateway. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="public" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Spring Cloud Gateway exposes endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRequests" /></td>
    <td><code>object</code></td>
    <td>The requested resource quantity for required CPU and Memory.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Spring Cloud Gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoProperties" /></td>
    <td><code>object</code></td>
    <td>Single sign-on related configuration.</td>
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
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>URL of the Spring Cloud Gateway, exposed when 'public' is true.</td>
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
    <td><CopyableCode code="apiMetadataProperties" /></td>
    <td><code>object</code></td>
    <td>API metadata property for Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="apms" /></td>
    <td><code>array</code></td>
    <td>Collection of ApmReferences in service level.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAuth" /></td>
    <td><code>object</code></td>
    <td>Client-Certification Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="corsProperties" /></td>
    <td><code>object</code></td>
    <td>Cross-Origin Resource Sharing property.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>object</code></td>
    <td>Environment variables of Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsOnly" /></td>
    <td><code>boolean</code></td>
    <td>Indicate if only https is allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>Collection of instances belong to Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of the Spring Cloud Gateway Operator.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Spring Cloud Gateway. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="public" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Spring Cloud Gateway exposes endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRequests" /></td>
    <td><code>object</code></td>
    <td>The requested resource quantity for required CPU and Memory.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Spring Cloud Gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ssoProperties" /></td>
    <td><code>object</code></td>
    <td>Single sign-on related configuration.</td>
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
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>URL of the Spring Cloud Gateway, exposed when 'public' is true.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Spring Cloud Gateway and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in a Service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create the default Spring Cloud Gateway or update the existing Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create the default Spring Cloud Gateway or update the existing Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable the default Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><a href="#list_env_secrets"><CopyableCode code="list_env_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List sensitive environment variables of Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restart the Spring Cloud Gateway.</td>
</tr>
<tr>
    <td><a href="#validate_domain"><CopyableCode code="validate_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Check the domains are valid as well as not in use.</td>
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

Get the Spring Cloud Gateway and its properties.

```sql
SELECT
id,
name,
apiMetadataProperties,
apms,
clientAuth,
corsProperties,
environmentVariables,
httpsOnly,
instances,
operatorProperties,
provisioningState,
public,
resourceRequests,
sku,
ssoProperties,
systemData,
type,
url
FROM azure.appplatform.gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Handles requests to list all resources in a Service.

```sql
SELECT
id,
name,
apiMetadataProperties,
apms,
clientAuth,
corsProperties,
environmentVariables,
httpsOnly,
instances,
operatorProperties,
provisioningState,
public,
resourceRequests,
sku,
ssoProperties,
systemData,
type,
url
FROM azure.appplatform.gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
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

Create the default Spring Cloud Gateway or update the existing Spring Cloud Gateway.

```sql
INSERT INTO azure.appplatform.gateways (
properties,
sku,
resource_group_name,
service_name,
gateway_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ gateway_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
sku,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the gateways resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the gateways resource.
    - name: gateway_name
      value: "{{ gateway_name }}"
      description: Required parameter for the gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the gateways resource.
    - name: properties
      description: |
        Spring Cloud Gateway properties payload.
      value:
        provisioningState: "{{ provisioningState }}"
        public: {{ public }}
        url: "{{ url }}"
        httpsOnly: {{ httpsOnly }}
        ssoProperties:
          scope:
            - "{{ scope }}"
          clientId: "{{ clientId }}"
          clientSecret: "{{ clientSecret }}"
          issuerUri: "{{ issuerUri }}"
        apiMetadataProperties:
          title: "{{ title }}"
          description: "{{ description }}"
          documentation: "{{ documentation }}"
          version: "{{ version }}"
          serverUrl: "{{ serverUrl }}"
        corsProperties:
          allowedOrigins:
            - "{{ allowedOrigins }}"
          allowedOriginPatterns:
            - "{{ allowedOriginPatterns }}"
          allowedMethods:
            - "{{ allowedMethods }}"
          allowedHeaders:
            - "{{ allowedHeaders }}"
          maxAge: {{ maxAge }}
          allowCredentials: {{ allowCredentials }}
          exposedHeaders:
            - "{{ exposedHeaders }}"
        clientAuth:
          certificates:
            - "{{ certificates }}"
          certificateVerification: "{{ certificateVerification }}"
        apms:
          - resourceId: "{{ resourceId }}"
        environmentVariables:
          properties: "{{ properties }}"
          secrets: "{{ secrets }}"
        resourceRequests:
          cpu: "{{ cpu }}"
          memory: "{{ memory }}"
        instances:
          - name: "{{ name }}"
            status: "{{ status }}"
        operatorProperties:
          resourceRequests:
            cpu: "{{ cpu }}"
            memory: "{{ memory }}"
            instanceCount: {{ instanceCount }}
          instances:
            - name: "{{ name }}"
              status: "{{ status }}"
    - name: sku
      description: |
        Sku of the Spring Cloud Gateway resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
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

Create the default Spring Cloud Gateway or update the existing Spring Cloud Gateway.

```sql
REPLACE azure.appplatform.gateways
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
sku,
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

Disable the default Spring Cloud Gateway.

```sql
DELETE FROM azure.appplatform.gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_env_secrets"
    values={[
        { label: 'list_env_secrets', value: 'list_env_secrets' },
        { label: 'restart', value: 'restart' },
        { label: 'validate_domain', value: 'validate_domain' }
    ]}
>
<TabItem value="list_env_secrets">

List sensitive environment variables of Spring Cloud Gateway.

```sql
EXEC azure.appplatform.gateways.list_env_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restart the Spring Cloud Gateway.

```sql
EXEC azure.appplatform.gateways.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_domain">

Check the domains are valid as well as not in use.

```sql
EXEC azure.appplatform.gateways.validate_domain 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}"
}'
;
```
</TabItem>
</Tabs>
