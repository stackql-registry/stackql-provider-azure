--- 
title: integration_service_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environments
  - logic
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

Creates, updates, deletes, gets or lists an <code>integration_service_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_service_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.integration_service_environments" /></td></tr>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionConfiguration" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointsConfiguration" /></td>
    <td><code>object</code></td>
    <td>The endpoints configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity properties.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Gets the tracking id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The integration service environment state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionConfiguration" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointsConfiguration" /></td>
    <td><code>object</code></td>
    <td>The endpoints configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity properties.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Gets the tracking id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The integration service environment state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionConfiguration" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointsConfiguration" /></td>
    <td><code>object</code></td>
    <td>The endpoints configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity properties.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Gets the tracking id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The integration service environment state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
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
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an integration service environment.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets a list of integration service environments by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets a list of integration service environments by subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an integration service environment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an integration service environment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an integration service environment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an integration service environment.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts an integration service environment.</td>
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
<tr id="parameter-integration_service_environment_name">
    <td><CopyableCode code="integration_service_environment_name" /></td>
    <td><code>string</code></td>
    <td>The integration service environment name. Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>The resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of items to be included in the result. Default value is None.</td>
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

Gets an integration service environment.

```sql
SELECT
id,
name,
encryptionConfiguration,
endpointsConfiguration,
identity,
integrationServiceEnvironmentId,
location,
networkConfiguration,
provisioningState,
sku,
state,
tags,
type
FROM azure.logic.integration_service_environments
WHERE resource_group = '{{ resource_group }}' -- required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of integration service environments by resource group.

```sql
SELECT
id,
name,
encryptionConfiguration,
endpointsConfiguration,
identity,
integrationServiceEnvironmentId,
location,
networkConfiguration,
provisioningState,
sku,
state,
tags,
type
FROM azure.logic.integration_service_environments
WHERE resource_group = '{{ resource_group }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of integration service environments by subscription.

```sql
SELECT
id,
name,
encryptionConfiguration,
endpointsConfiguration,
identity,
integrationServiceEnvironmentId,
location,
networkConfiguration,
provisioningState,
sku,
state,
tags,
type
FROM azure.logic.integration_service_environments
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates an integration service environment.

```sql
INSERT INTO azure.logic.integration_service_environments (
location,
tags,
properties,
sku,
identity,
resource_group,
integration_service_environment_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group }}',
'{{ integration_service_environment_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: integration_service_environments
  props:
    - name: resource_group
      value: "{{ resource_group }}"
      description: Required parameter for the integration_service_environments resource.
    - name: integration_service_environment_name
      value: "{{ integration_service_environment_name }}"
      description: Required parameter for the integration_service_environments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the integration_service_environments resource.
    - name: location
      value: "{{ location }}"
      description: |
        The resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: properties
      description: |
        The integration service environment properties.
      value:
        provisioningState: "{{ provisioningState }}"
        state: "{{ state }}"
        integrationServiceEnvironmentId: "{{ integrationServiceEnvironmentId }}"
        endpointsConfiguration:
          workflow:
            outgoingIpAddresses:
              - address: "{{ address }}"
            accessEndpointIpAddresses:
              - address: "{{ address }}"
          connector:
            outgoingIpAddresses:
              - address: "{{ address }}"
            accessEndpointIpAddresses:
              - address: "{{ address }}"
        networkConfiguration:
          virtualNetworkAddressSpace: "{{ virtualNetworkAddressSpace }}"
          accessEndpoint:
            type: "{{ type }}"
          subnets:
            - id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
        encryptionConfiguration:
          encryptionKeyReference:
            keyVault:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
            keyName: "{{ keyName }}"
            keyVersion: "{{ keyVersion }}"
    - name: sku
      description: |
        The sku.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Managed service identity properties.
      value:
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates an integration service environment.

```sql
UPDATE azure.logic.integration_service_environments
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group = '{{ resource_group }}' --required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Creates or updates an integration service environment.

```sql
REPLACE azure.logic.integration_service_environments
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group = '{{ resource_group }}' --required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Deletes an integration service environment.

```sql
DELETE FROM azure.logic.integration_service_environments
WHERE resource_group = '{{ resource_group }}' --required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restart"
    values={[
        { label: 'restart', value: 'restart' }
    ]}
>
<TabItem value="restart">

Restarts an integration service environment.

```sql
EXEC azure.logic.integration_service_environments.restart 
@resource_group='{{ resource_group }}' --required, 
@integration_service_environment_name='{{ integration_service_environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
