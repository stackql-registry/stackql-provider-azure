--- 
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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

Creates, updates, deletes, gets or lists a <code>routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="routes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.routes" /></td></tr>
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
    <td><CopyableCode code="cacheConfiguration" /></td>
    <td><code>object</code></td>
    <td>The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomains" /></td>
    <td><code>array</code></td>
    <td>Domains referenced by this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="endpointName" /></td>
    <td><code>string</code></td>
    <td>The name of the endpoint which holds the route.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardingProtocol" /></td>
    <td><code>string</code></td>
    <td>Protocol this rule will use when forwarding traffic to backends. Known values are: "HttpOnly", "HttpsOnly", and "MatchRequest". (HttpOnly, HttpsOnly, MatchRequest)</td>
</tr>
<tr>
    <td><CopyableCode code="httpsRedirect" /></td>
    <td><code>string</code></td>
    <td>Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="linkToDefaultDomain" /></td>
    <td><code>string</code></td>
    <td>whether this route will be linked to the default endpoint domain. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="originGroup" /></td>
    <td><code>object</code></td>
    <td>Reference to another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="originPath" /></td>
    <td><code>string</code></td>
    <td>A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.</td>
</tr>
<tr>
    <td><CopyableCode code="patternsToMatch" /></td>
    <td><code>array</code></td>
    <td>The route patterns of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleSets" /></td>
    <td><code>array</code></td>
    <td>rule sets referenced by this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedProtocols" /></td>
    <td><code>array</code></td>
    <td>List of supported protocols for this route.</td>
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
    <td><CopyableCode code="cacheConfiguration" /></td>
    <td><code>object</code></td>
    <td>The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomains" /></td>
    <td><code>array</code></td>
    <td>Domains referenced by this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="endpointName" /></td>
    <td><code>string</code></td>
    <td>The name of the endpoint which holds the route.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardingProtocol" /></td>
    <td><code>string</code></td>
    <td>Protocol this rule will use when forwarding traffic to backends. Known values are: "HttpOnly", "HttpsOnly", and "MatchRequest". (HttpOnly, HttpsOnly, MatchRequest)</td>
</tr>
<tr>
    <td><CopyableCode code="httpsRedirect" /></td>
    <td><code>string</code></td>
    <td>Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="linkToDefaultDomain" /></td>
    <td><code>string</code></td>
    <td>whether this route will be linked to the default endpoint domain. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="originGroup" /></td>
    <td><code>object</code></td>
    <td>Reference to another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="originPath" /></td>
    <td><code>string</code></td>
    <td>A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.</td>
</tr>
<tr>
    <td><CopyableCode code="patternsToMatch" /></td>
    <td><code>array</code></td>
    <td>The route patterns of the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleSets" /></td>
    <td><code>array</code></td>
    <td>rule sets referenced by this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedProtocols" /></td>
    <td><code>array</code></td>
    <td>List of supported protocols for this route.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_endpoint"><CopyableCode code="list_by_endpoint" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the existing origins within a profile.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.</td>
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
<tr id="parameter-route_name">
    <td><CopyableCode code="route_name" /></td>
    <td><code>string</code></td>
    <td>Name of the routing rule. Required.</td>
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

Gets an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.

```sql
SELECT
id,
name,
cacheConfiguration,
customDomains,
deploymentStatus,
enabledState,
endpointName,
forwardingProtocol,
httpsRedirect,
linkToDefaultDomain,
originGroup,
originPath,
patternsToMatch,
provisioningState,
ruleSets,
supportedProtocols,
systemData,
type
FROM azure.cdn.routes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND route_name = '{{ route_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_endpoint">

Lists all of the existing origins within a profile.

```sql
SELECT
id,
name,
cacheConfiguration,
customDomains,
deploymentStatus,
enabledState,
endpointName,
forwardingProtocol,
httpsRedirect,
linkToDefaultDomain,
originGroup,
originPath,
patternsToMatch,
provisioningState,
ruleSets,
supportedProtocols,
systemData,
type
FROM azure.cdn.routes
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

Creates a new route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.

```sql
INSERT INTO azure.cdn.routes (
properties,
resource_group_name,
profile_name,
endpoint_name,
route_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ endpoint_name }}',
'{{ route_name }}',
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
- name: routes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the routes resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the routes resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the routes resource.
    - name: route_name
      value: "{{ route_name }}"
      description: Required parameter for the routes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the routes resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the Routes to create.
      value:
        endpointName: "{{ endpointName }}"
        customDomains:
          - id: "{{ id }}"
            isActive: {{ isActive }}
        originGroup:
          id: "{{ id }}"
        originPath: "{{ originPath }}"
        ruleSets:
          - id: "{{ id }}"
        supportedProtocols:
          - "{{ supportedProtocols }}"
        patternsToMatch:
          - "{{ patternsToMatch }}"
        cacheConfiguration:
          queryStringCachingBehavior: "{{ queryStringCachingBehavior }}"
          queryParameters: "{{ queryParameters }}"
          compressionSettings:
            contentTypesToCompress:
              - "{{ contentTypesToCompress }}"
            isCompressionEnabled: {{ isCompressionEnabled }}
        forwardingProtocol: "{{ forwardingProtocol }}"
        linkToDefaultDomain: "{{ linkToDefaultDomain }}"
        httpsRedirect: "{{ httpsRedirect }}"
        enabledState: "{{ enabledState }}"
        provisioningState: "{{ provisioningState }}"
        deploymentStatus: "{{ deploymentStatus }}"
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

Updates an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.

```sql
UPDATE azure.cdn.routes
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND route_name = '{{ route_name }}' --required
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

Deletes an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.

```sql
DELETE FROM azure.cdn.routes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND route_name = '{{ route_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
