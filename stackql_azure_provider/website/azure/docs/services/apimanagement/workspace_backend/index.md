--- 
title: workspace_backend
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_backend
  - apimanagement
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

Creates, updates, deletes, gets or lists a <code>workspace_backend</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_backend" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.apimanagement.workspace_backend" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="azureRegion" /></td>
    <td><code>string</code></td>
    <td>Azure region in which the backend is deployed. Can be optionally specified to use features such as carbon-optimized load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitBreaker" /></td>
    <td><code>object</code></td>
    <td>Backend Circuit Breaker Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials" /></td>
    <td><code>object</code></td>
    <td>Backend Credentials Contract Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Backend Description.</td>
</tr>
<tr>
    <td><CopyableCode code="pool" /></td>
    <td><code>object</code></td>
    <td>Backend Pool Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Backend Properties contract.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Backend communication protocol. Required when backend type is 'Single'. Known values are: "http" and "soap". (http, soap)</td>
</tr>
<tr>
    <td><CopyableCode code="proxy" /></td>
    <td><code>object</code></td>
    <td>Backend gateway Contract Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Management Uri of the Resource in External System. This URL can be the Arm Resource Id of Logic Apps, Function Apps or API Apps.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Backend Title.</td>
</tr>
<tr>
    <td><CopyableCode code="tls" /></td>
    <td><code>object</code></td>
    <td>Backend TLS Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Runtime Url of the Backend. Required when backend type is 'Single'.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="azureRegion" /></td>
    <td><code>string</code></td>
    <td>Azure region in which the backend is deployed. Can be optionally specified to use features such as carbon-optimized load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitBreaker" /></td>
    <td><code>object</code></td>
    <td>Backend Circuit Breaker Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials" /></td>
    <td><code>object</code></td>
    <td>Backend Credentials Contract Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Backend Description.</td>
</tr>
<tr>
    <td><CopyableCode code="pool" /></td>
    <td><code>object</code></td>
    <td>Backend Pool Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Backend Properties contract.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Backend communication protocol. Required when backend type is 'Single'. Known values are: "http" and "soap". (http, soap)</td>
</tr>
<tr>
    <td><CopyableCode code="proxy" /></td>
    <td><code>object</code></td>
    <td>Backend gateway Contract Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Management Uri of the Resource in External System. This URL can be the Arm Resource Id of Logic Apps, Function Apps or API Apps.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Backend Title.</td>
</tr>
<tr>
    <td><CopyableCode code="tls" /></td>
    <td><code>object</code></td>
    <td>Backend TLS Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Runtime Url of the Backend. Required when backend type is 'Single'.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-backend_id"><code>backend_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the backend specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Lists a collection of backends in the specified workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-backend_id"><code>backend_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a backend.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-backend_id"><code>backend_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing backend.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-backend_id"><code>backend_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a backend.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-backend_id"><code>backend_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified backend.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-backend_id"><code>backend_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the entity state (Etag) version of the backend specified by its identifier.</td>
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
<tr id="parameter-backend_id">
    <td><CopyableCode code="backend_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the Backend entity. Must be unique in the current API Management service instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>string</code></td>
    <td>Workspace identifier. Must be unique in the current API Management service instance. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>| Field | Usage | Supported operators | Supported functions ||-------------|-------------|-------------|-------------|| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || title | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || url | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of records to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of records to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Gets the details of the backend specified by its identifier.

```sql
SELECT
id,
name,
azureRegion,
circuitBreaker,
credentials,
description,
pool,
properties,
protocol,
proxy,
resourceId,
systemData,
title,
tls,
type,
url
FROM azure.apimanagement.workspace_backend
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
AND backend_id = '{{ backend_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

Lists a collection of backends in the specified workspace.

```sql
SELECT
id,
name,
azureRegion,
circuitBreaker,
credentials,
description,
pool,
properties,
protocol,
proxy,
resourceId,
systemData,
title,
tls,
type,
url
FROM azure.apimanagement.workspace_backend
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
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

Creates or Updates a backend.

```sql
INSERT INTO azure.apimanagement.workspace_backend (
properties,
resource_group_name,
service_name,
workspace_id,
backend_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ workspace_id }}',
'{{ backend_id }}',
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
- name: workspace_backend
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspace_backend resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the workspace_backend resource.
    - name: workspace_id
      value: "{{ workspace_id }}"
      description: Required parameter for the workspace_backend resource.
    - name: backend_id
      value: "{{ backend_id }}"
      description: Required parameter for the workspace_backend resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspace_backend resource.
    - name: properties
      description: |
        Backend entity contract properties.
      value:
        title: "{{ title }}"
        description: "{{ description }}"
        resourceId: "{{ resourceId }}"
        properties:
          serviceFabricCluster:
            clientCertificateId: "{{ clientCertificateId }}"
            clientCertificatethumbprint: "{{ clientCertificatethumbprint }}"
            maxPartitionResolutionRetries: {{ maxPartitionResolutionRetries }}
            managementEndpoints:
              - "{{ managementEndpoints }}"
            serverCertificateThumbprints:
              - "{{ serverCertificateThumbprints }}"
            serverX509Names:
              - name: "{{ name }}"
                issuerCertificateThumbprint: "{{ issuerCertificateThumbprint }}"
        credentials:
          certificateIds:
            - "{{ certificateIds }}"
          certificate:
            - "{{ certificate }}"
          query: "{{ query }}"
          header: "{{ header }}"
          authorization:
            scheme: "{{ scheme }}"
            parameter: "{{ parameter }}"
        proxy:
          url: "{{ url }}"
          username: "{{ username }}"
          password: "{{ password }}"
        tls:
          validateCertificateChain: {{ validateCertificateChain }}
          validateCertificateName: {{ validateCertificateName }}
          serverCertificateThumbprints:
            - "{{ serverCertificateThumbprints }}"
          serverX509Names:
            - name: "{{ name }}"
              issuerCertificateThumbprint: "{{ issuerCertificateThumbprint }}"
        circuitBreaker:
          rules:
            - name: "{{ name }}"
              failureCondition:
                count: {{ count }}
                percentage: {{ percentage }}
                interval: "{{ interval }}"
                statusCodeRanges:
                  - min: {{ min }}
                    max: {{ max }}
                errorReasons:
                  - "{{ errorReasons }}"
              tripDuration: "{{ tripDuration }}"
              acceptRetryAfter: {{ acceptRetryAfter }}
              failureResponse:
                statusCode: {{ statusCode }}
        azureRegion: "{{ azureRegion }}"
        pool:
          services:
            - id: "{{ id }}"
              weight: {{ weight }}
              priority: {{ priority }}
              preferredCarbonEmission: "{{ preferredCarbonEmission }}"
          failureResponse:
            statusCode: {{ statusCode }}
          sessionAffinity:
            sessionId:
              source: "{{ source }}"
              name: "{{ name }}"
        type: "{{ type }}"
        url: "{{ url }}"
        protocol: "{{ protocol }}"
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

Updates an existing backend.

```sql
UPDATE azure.apimanagement.workspace_backend
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND backend_id = '{{ backend_id }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or Updates a backend.

```sql
REPLACE azure.apimanagement.workspace_backend
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND backend_id = '{{ backend_id }}' --required
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

Deletes the specified backend.

```sql
DELETE FROM azure.apimanagement.workspace_backend
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND backend_id = '{{ backend_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_entity_tag"
    values={[
        { label: 'get_entity_tag', value: 'get_entity_tag' }
    ]}
>
<TabItem value="get_entity_tag">

Gets the entity state (Etag) version of the backend specified by its identifier.

```sql
EXEC azure.apimanagement.workspace_backend.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@workspace_id='{{ workspace_id }}' --required, 
@backend_id='{{ backend_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
