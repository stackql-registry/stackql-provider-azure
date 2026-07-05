--- 
title: partner_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_namespaces
  - eventgrid
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

Creates, updates, deletes, gets or lists a <code>partner_namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="partner_namespaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid.partner_namespaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the partner namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the partner namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this partner namespace. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegistrationFullyQualifiedId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.EventGrid/partnerRegistrations/&#123;partnerRegistrationName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicRoutingMode" /></td>
    <td><code>string</code></td>
    <td>This determines if events published to this partner namespace should use the source attribute in the event payload or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic. Known values are: "SourceEventAttribute" and "ChannelNameHeader". (SourceEventAttribute, ChannelNameHeader)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the partner namespace. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the partner namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the partner namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this partner namespace. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegistrationFullyQualifiedId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.EventGrid/partnerRegistrations/&#123;partnerRegistrationName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicRoutingMode" /></td>
    <td><code>string</code></td>
    <td>This determines if events published to this partner namespace should use the source attribute in the event payload or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic. Known values are: "SourceEventAttribute" and "ChannelNameHeader". (SourceEventAttribute, ChannelNameHeader)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the partner namespace. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only Microsoft Entra ID token will be used to authenticate if user is allowed to publish to the partner namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Endpoint for the partner namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this partner namespace. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegistrationFullyQualifiedId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.EventGrid/partnerRegistrations/&#123;partnerRegistrationName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicRoutingMode" /></td>
    <td><code>string</code></td>
    <td>This determines if events published to this partner namespace should use the source attribute in the event payload or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic. Known values are: "SourceEventAttribute" and "ChannelNameHeader". (SourceEventAttribute, ChannelNameHeader)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the partner namespace. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a partner namespace. Get properties of a partner namespace.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List partner namespaces under a resource group. List all the partner namespaces under a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List partner namespaces under an Azure subscription. List all the partner namespaces under an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a partner namespace. Asynchronously creates a new partner namespace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a partner namespace. Asynchronously updates a partner namespace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a partner namespace. Asynchronously creates a new partner namespace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a partner namespace. Delete existing partner namespace.</td>
</tr>
<tr>
    <td><a href="#list_shared_access_keys"><CopyableCode code="list_shared_access_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List keys for a partner namespace. List the two keys used to publish to a partner namespace.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyName"><code>keyName</code></a></td>
    <td></td>
    <td>Regenerate key for a partner namespace. Regenerate a shared access key for a partner namespace.</td>
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
<tr id="parameter-partner_namespace_name">
    <td><CopyableCode code="partner_namespace_name" /></td>
    <td><code>string</code></td>
    <td>Name of the partner namespace. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a partner namespace. Get properties of a partner namespace.

```sql
SELECT
id,
name,
disableLocalAuth,
endpoint,
inboundIpRules,
location,
minimumTlsVersionAllowed,
partnerRegistrationFullyQualifiedId,
partnerTopicRoutingMode,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
systemData,
tags,
type
FROM azure.eventgrid.partner_namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND partner_namespace_name = '{{ partner_namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List partner namespaces under a resource group. List all the partner namespaces under a resource group.

```sql
SELECT
id,
name,
disableLocalAuth,
endpoint,
inboundIpRules,
location,
minimumTlsVersionAllowed,
partnerRegistrationFullyQualifiedId,
partnerTopicRoutingMode,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
systemData,
tags,
type
FROM azure.eventgrid.partner_namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

List partner namespaces under an Azure subscription. List all the partner namespaces under an Azure subscription.

```sql
SELECT
id,
name,
disableLocalAuth,
endpoint,
inboundIpRules,
location,
minimumTlsVersionAllowed,
partnerRegistrationFullyQualifiedId,
partnerTopicRoutingMode,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
systemData,
tags,
type
FROM azure.eventgrid.partner_namespaces
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
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

Create a partner namespace. Asynchronously creates a new partner namespace with the specified parameters.

```sql
INSERT INTO azure.eventgrid.partner_namespaces (
tags,
location,
properties,
resource_group_name,
partner_namespace_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ partner_namespace_name }}',
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
- name: partner_namespaces
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the partner_namespaces resource.
    - name: partner_namespace_name
      value: "{{ partner_namespace_name }}"
      description: Required parameter for the partner_namespaces resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the partner_namespaces resource.
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
        Properties of the Partner Namespace.
      value:
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              groupIds:
                - "{{ groupIds }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        provisioningState: "{{ provisioningState }}"
        partnerRegistrationFullyQualifiedId: "{{ partnerRegistrationFullyQualifiedId }}"
        minimumTlsVersionAllowed: "{{ minimumTlsVersionAllowed }}"
        endpoint: "{{ endpoint }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        inboundIpRules:
          - ipMask: "{{ ipMask }}"
            action: "{{ action }}"
        disableLocalAuth: {{ disableLocalAuth }}
        partnerTopicRoutingMode: "{{ partnerTopicRoutingMode }}"
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

Update a partner namespace. Asynchronously updates a partner namespace with the specified parameters.

```sql
UPDATE azure.eventgrid.partner_namespaces
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND partner_namespace_name = '{{ partner_namespace_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a partner namespace. Asynchronously creates a new partner namespace with the specified parameters.

```sql
REPLACE azure.eventgrid.partner_namespaces
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND partner_namespace_name = '{{ partner_namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a partner namespace. Delete existing partner namespace.

```sql
DELETE FROM azure.eventgrid.partner_namespaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND partner_namespace_name = '{{ partner_namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_shared_access_keys"
    values={[
        { label: 'list_shared_access_keys', value: 'list_shared_access_keys' },
        { label: 'regenerate_key', value: 'regenerate_key' }
    ]}
>
<TabItem value="list_shared_access_keys">

List keys for a partner namespace. List the two keys used to publish to a partner namespace.

```sql
EXEC azure.eventgrid.partner_namespaces.list_shared_access_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@partner_namespace_name='{{ partner_namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerate key for a partner namespace. Regenerate a shared access key for a partner namespace.

```sql
EXEC azure.eventgrid.partner_namespaces.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@partner_namespace_name='{{ partner_namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}"
}'
;
```
</TabItem>
</Tabs>
