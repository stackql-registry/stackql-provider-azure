--- 
title: agent_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_applications
  - cognitive_services
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

Creates, updates, deletes, gets or lists an <code>agent_applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agent_applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.agent_applications" /></td></tr>
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
    <td><CopyableCode code="agentIdentityBlueprint" /></td>
    <td><code>object</code></td>
    <td>The EntraId Agentic Blueprint of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="agents" /></td>
    <td><code>array</code></td>
    <td>The list of agent definitions comprising this application, returned as references to the objects under the parent project; use this to obtain a flat list of all agent-version pairs represented by this application.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicy" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the authorization policy associated with this agentic application instance.</td>
</tr>
<tr>
    <td><CopyableCode code="baseUrl" /></td>
    <td><code>string</code></td>
    <td>The application's dedicated invocation endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultInstanceIdentity" /></td>
    <td><code>object</code></td>
    <td>The (default) agent instance identity of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enabledstate of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the application. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRoutingPolicy" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the traffic routing policy for the application's deployments.</td>
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
    <td><CopyableCode code="agentIdentityBlueprint" /></td>
    <td><code>object</code></td>
    <td>The EntraId Agentic Blueprint of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="agents" /></td>
    <td><code>array</code></td>
    <td>The list of agent definitions comprising this application, returned as references to the objects under the parent project; use this to obtain a flat list of all agent-version pairs represented by this application.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicy" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the authorization policy associated with this agentic application instance.</td>
</tr>
<tr>
    <td><CopyableCode code="baseUrl" /></td>
    <td><code>string</code></td>
    <td>The application's dedicated invocation endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultInstanceIdentity" /></td>
    <td><code>object</code></td>
    <td>The (default) agent instance identity of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Enabledstate of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the application. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRoutingPolicy" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the traffic routing policy for the application's deployments.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Agent Application by name. Gets an Agent Application by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-count"><code>count</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-searchText"><code>searchText</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-orderByAsc"><code>orderByAsc</code></a></td>
    <td>Lists Agent Applications in the project. Lists Agent Applications in the project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an Agent Application (asynchronous). Creates or updates an Agent Application (asynchronous).</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an Agent Application (asynchronous). Creates or updates an Agent Application (asynchronous).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Agent Application. Delete Agent Application.</td>
</tr>
<tr>
    <td><a href="#list_agents"><CopyableCode code="list_agents" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists agents for an Agent Application. Lists agents for an Agent Application.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enables an Agent Application. Enables an Agent Application.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables an Agent Application. Disables an Agent Application.</td>
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
    <td>The name of Cognitive Services account. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name for the Agent Application. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of Cognitive Services account's project. Required.</td>
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
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of agent applications to skip. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Continuation token for pagination. Default value is None.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of agent applications to be retrieved in a page of results. Default value is 30.</td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td>Field to order by. Default value is None.</td>
</tr>
<tr id="parameter-orderByAsc">
    <td><CopyableCode code="orderByAsc" /></td>
    <td><code>boolean</code></td>
    <td>Whether to order in ascending order. Default value is False.</td>
</tr>
<tr id="parameter-searchText">
    <td><CopyableCode code="searchText" /></td>
    <td><code>string</code></td>
    <td>Search text for filtering agent applications. Default value is None.</td>
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

Gets an Agent Application by name. Gets an Agent Application by name.

```sql
SELECT
id,
name,
agentIdentityBlueprint,
agents,
authorizationPolicy,
baseUrl,
defaultInstanceIdentity,
description,
displayName,
isEnabled,
provisioningState,
systemData,
tags,
trafficRoutingPolicy,
type
FROM azure.cognitive_services.agent_applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Agent Applications in the project. Lists Agent Applications in the project.

```sql
SELECT
id,
name,
agentIdentityBlueprint,
agents,
authorizationPolicy,
baseUrl,
defaultInstanceIdentity,
description,
displayName,
isEnabled,
provisioningState,
systemData,
tags,
trafficRoutingPolicy,
type
FROM azure.cognitive_services.agent_applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND count = '{{ count }}'
AND $skip = '{{ $skip }}'
AND $skipToken = '{{ $skipToken }}'
AND searchText = '{{ searchText }}'
AND orderBy = '{{ orderBy }}'
AND orderByAsc = '{{ orderByAsc }}'
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

Creates or updates an Agent Application (asynchronous). Creates or updates an Agent Application (asynchronous).

```sql
INSERT INTO azure.cognitive_services.agent_applications (
properties,
resource_group_name,
account_name,
project_name,
name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ project_name }}',
'{{ name }}',
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
- name: agent_applications
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the agent_applications resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the agent_applications resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the agent_applications resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the agent_applications resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the agent_applications resource.
    - name: properties
      description: |
        [Required] Additional attributes of the entity. Required.
      value:
        description: "{{ description }}"
        tags: "{{ tags }}"
        displayName: "{{ displayName }}"
        baseUrl: "{{ baseUrl }}"
        agents:
          - agentId: "{{ agentId }}"
            agentName: "{{ agentName }}"
        agentIdentityBlueprint:
          kind: "{{ kind }}"
          type: "{{ type }}"
          clientId: "{{ clientId }}"
          principalId: "{{ principalId }}"
          tenantId: "{{ tenantId }}"
          subject: "{{ subject }}"
          provisioningState: "{{ provisioningState }}"
        defaultInstanceIdentity:
          kind: "{{ kind }}"
          type: "{{ type }}"
          clientId: "{{ clientId }}"
          principalId: "{{ principalId }}"
          tenantId: "{{ tenantId }}"
          subject: "{{ subject }}"
          provisioningState: "{{ provisioningState }}"
        authorizationPolicy:
          type: "{{ type }}"
        trafficRoutingPolicy:
          protocol: "{{ protocol }}"
          rules:
            - ruleId: "{{ ruleId }}"
              description: "{{ description }}"
              deploymentId: "{{ deploymentId }}"
              trafficPercentage: {{ trafficPercentage }}
        provisioningState: "{{ provisioningState }}"
        isEnabled: {{ isEnabled }}
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

Creates or updates an Agent Application (asynchronous). Creates or updates an Agent Application (asynchronous).

```sql
REPLACE azure.cognitive_services.agent_applications
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND project_name = '{{ project_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Delete Agent Application. Delete Agent Application.

```sql
DELETE FROM azure.cognitive_services.agent_applications
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND project_name = '{{ project_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_agents"
    values={[
        { label: 'list_agents', value: 'list_agents' },
        { label: 'enable', value: 'enable' },
        { label: 'disable', value: 'disable' }
    ]}
>
<TabItem value="list_agents">

Lists agents for an Agent Application. Lists agents for an Agent Application.

```sql
EXEC azure.cognitive_services.agent_applications.list_agents 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable">

Enables an Agent Application. Enables an Agent Application.

```sql
EXEC azure.cognitive_services.agent_applications.enable 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="disable">

Disables an Agent Application. Disables an Agent Application.

```sql
EXEC azure.cognitive_services.agent_applications.disable 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
