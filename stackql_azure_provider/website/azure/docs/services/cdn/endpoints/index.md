--- 
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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

Creates, updates, deletes, gets or lists an <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_profile', value: 'list_by_profile' }
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
    <td><CopyableCode code="contentTypesToCompress" /></td>
    <td><code>array</code></td>
    <td>List of content types on which compression applies. The value should be a valid MIME type.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomains" /></td>
    <td><code>array</code></td>
    <td>The custom domains under the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOriginGroup" /></td>
    <td><code>object</code></td>
    <td>Reference to another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryPolicy" /></td>
    <td><code>object</code></td>
    <td>A policy that specifies the delivery rules to be used for an endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="geoFilters" /></td>
    <td><code>array</code></td>
    <td>List of rules defining the user's geo access within a CDN endpoint. Each geo filter defines an access rule to a specified path or content, e.g. block APAC for path /pictures/.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the endpoint structured as &#123;endpointName&#125;.&#123;DNSZone&#125;, e.g. contoso.azureedge.net.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompressionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether content compression is enabled on CDN. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on CDN when requested content is smaller than 1 byte or larger than 1 MB.</td>
</tr>
<tr>
    <td><CopyableCode code="isHttpAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether HTTP traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="isHttpsAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether HTTPS traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizationType" /></td>
    <td><code>string</code></td>
    <td>Specifies what scenario the customer wants this CDN endpoint to optimize for, e.g. Download, Media services. With this information, CDN can apply scenario driven optimization. Known values are: "GeneralWebDelivery", "GeneralMediaStreaming", "VideoOnDemandMediaStreaming", "LargeFileDownload", and "DynamicSiteAcceleration". (GeneralWebDelivery, GeneralMediaStreaming, VideoOnDemandMediaStreaming, LargeFileDownload, DynamicSiteAcceleration)</td>
</tr>
<tr>
    <td><CopyableCode code="originGroups" /></td>
    <td><code>array</code></td>
    <td>The origin groups comprising of origins that are used for load balancing the traffic based on availability.</td>
</tr>
<tr>
    <td><CopyableCode code="originHostHeader" /></td>
    <td><code>string</code></td>
    <td>The host header value sent to the origin with each request. This property at Endpoint is only allowed when endpoint uses single origin and can be overridden by the same property specified at origin.If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default.</td>
</tr>
<tr>
    <td><CopyableCode code="originPath" /></td>
    <td><code>string</code></td>
    <td>A directory path on the origin that CDN can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The source of the content being delivered via CDN. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="probePath" /></td>
    <td><code>string</code></td>
    <td>Path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the origin path. This property is only relevant when using a single origin.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the endpoint. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="queryStringCachingBehavior" /></td>
    <td><code>string</code></td>
    <td>Defines how CDN caches requests that include query strings. You can ignore any query strings when caching, bypass caching to prevent requests that contain query strings from being cached, or cache every request with a unique URL. Known values are: "IgnoreQueryString", "BypassCaching", "UseQueryString", and "NotSet". (IgnoreQueryString, BypassCaching, UseQueryString, NotSet)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the endpoint. Known values are: "Creating", "Deleting", "Running", "Starting", "Stopped", and "Stopping". (Creating, Deleting, Running, Starting, Stopped, Stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<tr>
    <td><CopyableCode code="urlSigningKeys" /></td>
    <td><code>array</code></td>
    <td>List of keys used to validate the signed URL hashes.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallPolicyLink" /></td>
    <td><code>object</code></td>
    <td>Defines the Web Application Firewall policy for the endpoint (if applicable).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_profile">

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
    <td><CopyableCode code="contentTypesToCompress" /></td>
    <td><code>array</code></td>
    <td>List of content types on which compression applies. The value should be a valid MIME type.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomains" /></td>
    <td><code>array</code></td>
    <td>The custom domains under the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOriginGroup" /></td>
    <td><code>object</code></td>
    <td>Reference to another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryPolicy" /></td>
    <td><code>object</code></td>
    <td>A policy that specifies the delivery rules to be used for an endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="geoFilters" /></td>
    <td><code>array</code></td>
    <td>List of rules defining the user's geo access within a CDN endpoint. Each geo filter defines an access rule to a specified path or content, e.g. block APAC for path /pictures/.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the endpoint structured as &#123;endpointName&#125;.&#123;DNSZone&#125;, e.g. contoso.azureedge.net.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompressionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether content compression is enabled on CDN. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on CDN when requested content is smaller than 1 byte or larger than 1 MB.</td>
</tr>
<tr>
    <td><CopyableCode code="isHttpAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether HTTP traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="isHttpsAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether HTTPS traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizationType" /></td>
    <td><code>string</code></td>
    <td>Specifies what scenario the customer wants this CDN endpoint to optimize for, e.g. Download, Media services. With this information, CDN can apply scenario driven optimization. Known values are: "GeneralWebDelivery", "GeneralMediaStreaming", "VideoOnDemandMediaStreaming", "LargeFileDownload", and "DynamicSiteAcceleration". (GeneralWebDelivery, GeneralMediaStreaming, VideoOnDemandMediaStreaming, LargeFileDownload, DynamicSiteAcceleration)</td>
</tr>
<tr>
    <td><CopyableCode code="originGroups" /></td>
    <td><code>array</code></td>
    <td>The origin groups comprising of origins that are used for load balancing the traffic based on availability.</td>
</tr>
<tr>
    <td><CopyableCode code="originHostHeader" /></td>
    <td><code>string</code></td>
    <td>The host header value sent to the origin with each request. This property at Endpoint is only allowed when endpoint uses single origin and can be overridden by the same property specified at origin.If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default.</td>
</tr>
<tr>
    <td><CopyableCode code="originPath" /></td>
    <td><code>string</code></td>
    <td>A directory path on the origin that CDN can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The source of the content being delivered via CDN. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="probePath" /></td>
    <td><code>string</code></td>
    <td>Path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the origin path. This property is only relevant when using a single origin.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the endpoint. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="queryStringCachingBehavior" /></td>
    <td><code>string</code></td>
    <td>Defines how CDN caches requests that include query strings. You can ignore any query strings when caching, bypass caching to prevent requests that contain query strings from being cached, or cache every request with a unique URL. Known values are: "IgnoreQueryString", "BypassCaching", "UseQueryString", and "NotSet". (IgnoreQueryString, BypassCaching, UseQueryString, NotSet)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the endpoint. Known values are: "Creating", "Deleting", "Running", "Starting", "Stopped", and "Stopping". (Creating, Deleting, Running, Starting, Stopped, Stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<tr>
    <td><CopyableCode code="urlSigningKeys" /></td>
    <td><code>array</code></td>
    <td>List of keys used to validate the signed URL hashes.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallPolicyLink" /></td>
    <td><code>object</code></td>
    <td>Defines the Web Application Firewall policy for the endpoint (if applicable).</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.</td>
</tr>
<tr>
    <td><a href="#list_by_profile"><CopyableCode code="list_by_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists existing CDN endpoints.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update custom domains, use the Update Custom Domain operation.</td>
</tr>
<tr>
    <td><a href="#purge_content"><CopyableCode code="purge_content" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes a content from CDN.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.</td>
</tr>
<tr>
    <td><a href="#list_resource_usage"><CopyableCode code="list_resource_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the quota and usage of geo filters and custom domains under the given endpoint.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts an existing CDN endpoint that is on a stopped state.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops an existing running CDN endpoint.</td>
</tr>
<tr>
    <td><a href="#load_content"><CopyableCode code="load_content" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-contentPaths"><code>contentPaths</code></a></td>
    <td></td>
    <td>Pre-loads a content to CDN. Available for Verizon Profiles.</td>
</tr>
<tr>
    <td><a href="#validate_custom_domain"><CopyableCode code="validate_custom_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-hostName"><code>hostName</code></a></td>
    <td></td>
    <td>Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS.</td>
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
        { label: 'list_by_profile', value: 'list_by_profile' }
    ]}
>
<TabItem value="get">

Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

```sql
SELECT
id,
name,
contentTypesToCompress,
customDomains,
defaultOriginGroup,
deliveryPolicy,
geoFilters,
hostName,
isCompressionEnabled,
isHttpAllowed,
isHttpsAllowed,
location,
optimizationType,
originGroups,
originHostHeader,
originPath,
origins,
probePath,
provisioningState,
queryStringCachingBehavior,
resourceState,
systemData,
tags,
type,
urlSigningKeys,
webApplicationFirewallPolicyLink
FROM azure.cdn.endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_profile">

Lists existing CDN endpoints.

```sql
SELECT
id,
name,
contentTypesToCompress,
customDomains,
defaultOriginGroup,
deliveryPolicy,
geoFilters,
hostName,
isCompressionEnabled,
isHttpAllowed,
isHttpsAllowed,
location,
optimizationType,
originGroups,
originHostHeader,
originPath,
origins,
probePath,
provisioningState,
queryStringCachingBehavior,
resourceState,
systemData,
tags,
type,
urlSigningKeys,
webApplicationFirewallPolicyLink
FROM azure.cdn.endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
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

Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

```sql
INSERT INTO azure.cdn.endpoints (
tags,
location,
properties,
resource_group_name,
profile_name,
endpoint_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ endpoint_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: endpoints
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the endpoints resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the endpoints resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the endpoints resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the endpoints resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The JSON object that contains the properties required to create an endpoint.
      value:
        originPath: "{{ originPath }}"
        contentTypesToCompress:
          - "{{ contentTypesToCompress }}"
        originHostHeader: "{{ originHostHeader }}"
        isCompressionEnabled: {{ isCompressionEnabled }}
        isHttpAllowed: {{ isHttpAllowed }}
        isHttpsAllowed: {{ isHttpsAllowed }}
        queryStringCachingBehavior: "{{ queryStringCachingBehavior }}"
        optimizationType: "{{ optimizationType }}"
        probePath: "{{ probePath }}"
        geoFilters:
          - relativePath: "{{ relativePath }}"
            action: "{{ action }}"
            countryCodes: "{{ countryCodes }}"
        defaultOriginGroup:
          id: "{{ id }}"
        urlSigningKeys:
          - keyId: "{{ keyId }}"
            keySourceParameters:
              typeName: "{{ typeName }}"
              subscriptionId: "{{ subscriptionId }}"
              resourceGroupName: "{{ resourceGroupName }}"
              vaultName: "{{ vaultName }}"
              secretName: "{{ secretName }}"
              secretVersion: "{{ secretVersion }}"
        deliveryPolicy:
          description: "{{ description }}"
          rules:
            - name: "{{ name }}"
              order: {{ order }}
              conditions: "{{ conditions }}"
              actions: "{{ actions }}"
        webApplicationFirewallPolicyLink:
          id: "{{ id }}"
        hostName: "{{ hostName }}"
        origins:
          - name: "{{ name }}"
            properties:
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
              privateEndpointStatus: "{{ privateEndpointStatus }}"
        originGroups:
          - name: "{{ name }}"
            properties:
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
        customDomains:
          - name: "{{ name }}"
            properties:
              hostName: "{{ hostName }}"
              validationData: "{{ validationData }}"
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

Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update custom domains, use the Update Custom Domain operation.

```sql
UPDATE azure.cdn.endpoints
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="purge_content"
    values={[
        { label: 'purge_content', value: 'purge_content' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="purge_content">

Removes a content from CDN.

```sql
DELETE FROM azure.cdn.endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

```sql
DELETE FROM azure.cdn.endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_resource_usage"
    values={[
        { label: 'list_resource_usage', value: 'list_resource_usage' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'load_content', value: 'load_content' },
        { label: 'validate_custom_domain', value: 'validate_custom_domain' }
    ]}
>
<TabItem value="list_resource_usage">

Checks the quota and usage of geo filters and custom domains under the given endpoint.

```sql
EXEC azure.cdn.endpoints.list_resource_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts an existing CDN endpoint that is on a stopped state.

```sql
EXEC azure.cdn.endpoints.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops an existing running CDN endpoint.

```sql
EXEC azure.cdn.endpoints.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="load_content">

Pre-loads a content to CDN. Available for Verizon Profiles.

```sql
EXEC azure.cdn.endpoints.load_content 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"contentPaths": "{{ contentPaths }}"
}'
;
```
</TabItem>
<TabItem value="validate_custom_domain">

Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS.

```sql
EXEC azure.cdn.endpoints.validate_custom_domain 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"hostName": "{{ hostName }}"
}'
;
```
</TabItem>
</Tabs>
