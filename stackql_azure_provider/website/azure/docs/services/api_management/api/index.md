--- 
title: api
hide_title: false
hide_table_of_contents: false
keywords:
  - api
  - api_management
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

Creates, updates, deletes, gets or lists an <code>api</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="api" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service', value: 'list_by_service' }
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
    <td><CopyableCode code="apiRevision" /></td>
    <td><code>string</code></td>
    <td>Describes the revision of the API. If no value is provided, default revision 1 is created.</td>
</tr>
<tr>
    <td><CopyableCode code="apiRevisionDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the API Revision.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersion" /></td>
    <td><code>string</code></td>
    <td>Indicates the version identifier of the API if the API is versioned.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the API Version.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionSet" /></td>
    <td><code>object</code></td>
    <td>Version set details.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionSetId" /></td>
    <td><code>string</code></td>
    <td>A resource identifier for the related ApiVersionSet.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationSettings" /></td>
    <td><code>object</code></td>
    <td>Collection of authentication settings included into this API.</td>
</tr>
<tr>
    <td><CopyableCode code="contact" /></td>
    <td><code>object</code></td>
    <td>Contact information for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the API. May include HTML formatting tags.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>API name. Must be 1 to 300 characters long.</td>
</tr>
<tr>
    <td><CopyableCode code="isCurrent" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if API revision is current api revision.</td>
</tr>
<tr>
    <td><CopyableCode code="isOnline" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if API revision is accessible via the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="license" /></td>
    <td><code>object</code></td>
    <td>License information for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocols" /></td>
    <td><code>array</code></td>
    <td>Describes on which protocols the operations in this API can be invoked.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceUrl" /></td>
    <td><code>string</code></td>
    <td>Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceApiId" /></td>
    <td><code>string</code></td>
    <td>API identifier of the source API.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionKeyParameterNames" /></td>
    <td><code>object</code></td>
    <td>Protocols over which API is made available.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionRequired" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether an API or Product subscription is required for accessing the API.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="termsOfServiceUrl" /></td>
    <td><code>string</code></td>
    <td>A URL to the Terms of Service for the API. MUST be in the format of a URL.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_service">

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
    <td><CopyableCode code="apiRevision" /></td>
    <td><code>string</code></td>
    <td>Describes the revision of the API. If no value is provided, default revision 1 is created.</td>
</tr>
<tr>
    <td><CopyableCode code="apiRevisionDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the API Revision.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersion" /></td>
    <td><code>string</code></td>
    <td>Indicates the version identifier of the API if the API is versioned.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the API Version.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionSet" /></td>
    <td><code>object</code></td>
    <td>Version set details.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionSetId" /></td>
    <td><code>string</code></td>
    <td>A resource identifier for the related ApiVersionSet.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationSettings" /></td>
    <td><code>object</code></td>
    <td>Collection of authentication settings included into this API.</td>
</tr>
<tr>
    <td><CopyableCode code="contact" /></td>
    <td><code>object</code></td>
    <td>Contact information for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the API. May include HTML formatting tags.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>API name. Must be 1 to 300 characters long.</td>
</tr>
<tr>
    <td><CopyableCode code="isCurrent" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if API revision is current api revision.</td>
</tr>
<tr>
    <td><CopyableCode code="isOnline" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if API revision is accessible via the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="license" /></td>
    <td><code>object</code></td>
    <td>License information for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocols" /></td>
    <td><code>array</code></td>
    <td>Describes on which protocols the operations in this API can be invoked.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceUrl" /></td>
    <td><code>string</code></td>
    <td>Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceApiId" /></td>
    <td><code>string</code></td>
    <td>API identifier of the source API.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionKeyParameterNames" /></td>
    <td><code>object</code></td>
    <td>Protocols over which API is made available.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionRequired" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether an API or Product subscription is required for accessing the API.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="termsOfServiceUrl" /></td>
    <td><code>string</code></td>
    <td>A URL to the Terms of Service for the API. MUST be in the format of a URL.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the API specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_service"><CopyableCode code="list_by_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-expandApiVersionSet"><code>expandApiVersionSet</code></a></td>
    <td>Lists all APIs of the API Management service instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates new or updates existing specified API of the API Management service instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specified API of the API Management service instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates new or updates existing specified API of the API Management service instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteRevisions"><code>deleteRevisions</code></a></td>
    <td>Deletes the specified API of the API Management service instance.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the entity state (Etag) version of the API specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_tags"><CopyableCode code="list_by_tags" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-includeNotTaggedApis"><code>includeNotTaggedApis</code></a></td>
    <td>Lists a collection of apis associated with tags.</td>
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
<tr id="parameter-api_id">
    <td><CopyableCode code="api_id" /></td>
    <td><code>string</code></td>
    <td>API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>| Field | Usage | Supported operators | Supported functions ||-------------|-------------|-------------|-------------|| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || apiRevision | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || path | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || description | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || serviceUrl | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || isCurrent | filter | eq | |. Default value is None.</td>
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
<tr id="parameter-deleteRevisions">
    <td><CopyableCode code="deleteRevisions" /></td>
    <td><code>boolean</code></td>
    <td>Delete all revisions of the Api. Default value is None.</td>
</tr>
<tr id="parameter-expandApiVersionSet">
    <td><CopyableCode code="expandApiVersionSet" /></td>
    <td><code>boolean</code></td>
    <td>Include full ApiVersionSet resource in response. Default value is None.</td>
</tr>
<tr id="parameter-includeNotTaggedApis">
    <td><CopyableCode code="includeNotTaggedApis" /></td>
    <td><code>boolean</code></td>
    <td>Include not tagged APIs. Default value is None.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td>Include tags in the response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service', value: 'list_by_service' }
    ]}
>
<TabItem value="get">

Gets the details of the API specified by its identifier.

```sql
SELECT
id,
name,
apiRevision,
apiRevisionDescription,
apiVersion,
apiVersionDescription,
apiVersionSet,
apiVersionSetId,
authenticationSettings,
contact,
description,
displayName,
isCurrent,
isOnline,
license,
path,
protocols,
provisioningState,
serviceUrl,
sourceApiId,
subscriptionKeyParameterNames,
subscriptionRequired,
systemData,
termsOfServiceUrl,
type
FROM azure.api_management.api
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND api_id = '{{ api_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_service">

Lists all APIs of the API Management service instance.

```sql
SELECT
id,
name,
apiRevision,
apiRevisionDescription,
apiVersion,
apiVersionDescription,
apiVersionSet,
apiVersionSetId,
authenticationSettings,
contact,
description,
displayName,
isCurrent,
isOnline,
license,
path,
protocols,
provisioningState,
serviceUrl,
sourceApiId,
subscriptionKeyParameterNames,
subscriptionRequired,
systemData,
termsOfServiceUrl,
type
FROM azure.api_management.api
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND tags = '{{ tags }}'
AND expandApiVersionSet = '{{ expandApiVersionSet }}'
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

Creates new or updates existing specified API of the API Management service instance.

```sql
INSERT INTO azure.api_management.api (
properties,
resource_group_name,
service_name,
api_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ api_id }}',
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
- name: api
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the api resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the api resource.
    - name: api_id
      value: "{{ api_id }}"
      description: Required parameter for the api resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the api resource.
    - name: properties
      description: |
        API entity create of update properties.
      value:
        description: "{{ description }}"
        authenticationSettings:
          oAuth2:
            authorizationServerId: "{{ authorizationServerId }}"
            scope: "{{ scope }}"
          openid:
            openidProviderId: "{{ openidProviderId }}"
            bearerTokenSendingMethods:
              - "{{ bearerTokenSendingMethods }}"
          oAuth2AuthenticationSettings:
            - authorizationServerId: "{{ authorizationServerId }}"
              scope: "{{ scope }}"
          openidAuthenticationSettings:
            - openidProviderId: "{{ openidProviderId }}"
              bearerTokenSendingMethods: "{{ bearerTokenSendingMethods }}"
        subscriptionKeyParameterNames:
          header: "{{ header }}"
          query: "{{ query }}"
        type: "{{ type }}"
        apiRevision: "{{ apiRevision }}"
        apiVersion: "{{ apiVersion }}"
        isCurrent: {{ isCurrent }}
        isOnline: {{ isOnline }}
        apiRevisionDescription: "{{ apiRevisionDescription }}"
        apiVersionDescription: "{{ apiVersionDescription }}"
        apiVersionSetId: "{{ apiVersionSetId }}"
        subscriptionRequired: {{ subscriptionRequired }}
        termsOfServiceUrl: "{{ termsOfServiceUrl }}"
        contact:
          name: "{{ name }}"
          url: "{{ url }}"
          email: "{{ email }}"
        license:
          name: "{{ name }}"
          url: "{{ url }}"
        sourceApiId: "{{ sourceApiId }}"
        displayName: "{{ displayName }}"
        serviceUrl: "{{ serviceUrl }}"
        path: "{{ path }}"
        protocols:
          - "{{ protocols }}"
        apiVersionSet:
          id: "{{ id }}"
          name: "{{ name }}"
          description: "{{ description }}"
          versioningScheme: "{{ versioningScheme }}"
          versionQueryName: "{{ versionQueryName }}"
          versionHeaderName: "{{ versionHeaderName }}"
        provisioningState: "{{ provisioningState }}"
        value: "{{ value }}"
        format: "{{ format }}"
        wsdlSelector:
          wsdlServiceName: "{{ wsdlServiceName }}"
          wsdlEndpointName: "{{ wsdlEndpointName }}"
        apiType: "{{ apiType }}"
        translateRequiredQueryParameters: "{{ translateRequiredQueryParameters }}"
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

Updates the specified API of the API Management service instance.

```sql
UPDATE azure.api_management.api
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND api_id = '{{ api_id }}' --required
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

Creates new or updates existing specified API of the API Management service instance.

```sql
REPLACE azure.api_management.api
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND api_id = '{{ api_id }}' --required
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

Deletes the specified API of the API Management service instance.

```sql
DELETE FROM azure.api_management.api
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND api_id = '{{ api_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteRevisions = '{{ deleteRevisions }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_entity_tag"
    values={[
        { label: 'get_entity_tag', value: 'get_entity_tag' },
        { label: 'list_by_tags', value: 'list_by_tags' }
    ]}
>
<TabItem value="get_entity_tag">

Gets the entity state (Etag) version of the API specified by its identifier.

```sql
EXEC azure.api_management.api.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@api_id='{{ api_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_by_tags">

Lists a collection of apis associated with tags.

```sql
EXEC azure.api_management.api.list_by_tags 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}', 
@$top='{{ $top }}', 
@$skip='{{ $skip }}', 
@includeNotTaggedApis={{ includeNotTaggedApis }}
;
```
</TabItem>
</Tabs>
