--- 
title: connected_environments_dapr_components
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_dapr_components
  - appcontainers
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

Creates, updates, deletes, gets or lists a <code>connected_environments_dapr_components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connected_environments_dapr_components" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.connected_environments_dapr_components" /></td></tr>
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
    <td><CopyableCode code="componentType" /></td>
    <td><code>string</code></td>
    <td>Component type.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="ignoreErrors" /></td>
    <td><code>boolean</code></td>
    <td>Boolean describing if the component errors are ignores.</td>
</tr>
<tr>
    <td><CopyableCode code="initTimeout" /></td>
    <td><code>string</code></td>
    <td>Initialization timeout.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>Component metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Connected Environment Dapr Component. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>Names of container apps that can use this Dapr component.</td>
</tr>
<tr>
    <td><CopyableCode code="secretStoreComponent" /></td>
    <td><code>string</code></td>
    <td>Name of a Dapr component to retrieve component secrets from.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>array</code></td>
    <td>Collection of secrets used by a Dapr component.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Component version.</td>
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
    <td><CopyableCode code="componentType" /></td>
    <td><code>string</code></td>
    <td>Component type.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="ignoreErrors" /></td>
    <td><code>boolean</code></td>
    <td>Boolean describing if the component errors are ignores.</td>
</tr>
<tr>
    <td><CopyableCode code="initTimeout" /></td>
    <td><code>string</code></td>
    <td>Initialization timeout.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>Component metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Connected Environment Dapr Component. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>Names of container apps that can use this Dapr component.</td>
</tr>
<tr>
    <td><CopyableCode code="secretStoreComponent" /></td>
    <td><code>string</code></td>
    <td>Name of a Dapr component to retrieve component secrets from.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>array</code></td>
    <td>Collection of secrets used by a Dapr component.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Component version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-component_name"><code>component_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a dapr component. Get a dapr component.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Dapr Components for a connected environment. Get the Dapr Components for a connected environment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-component_name"><code>component_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Dapr Component. Creates or updates a Dapr Component in a connected environment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-component_name"><code>component_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Dapr Component. Creates or updates a Dapr Component in a connected environment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-component_name"><code>component_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Dapr Component. Delete a Dapr Component from a connected environment.</td>
</tr>
<tr>
    <td><a href="#list_secrets"><CopyableCode code="list_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-component_name"><code>component_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List secrets for a dapr component. List secrets for a dapr component.</td>
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
<tr id="parameter-component_name">
    <td><CopyableCode code="component_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Dapr Component. Required.</td>
</tr>
<tr id="parameter-connected_environment_name">
    <td><CopyableCode code="connected_environment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the connected environment. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a dapr component. Get a dapr component.

```sql
SELECT
id,
name,
componentType,
deploymentErrors,
ignoreErrors,
initTimeout,
metadata,
provisioningState,
scopes,
secretStoreComponent,
secrets,
systemData,
type,
version
FROM azure.appcontainers.connected_environments_dapr_components
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND connected_environment_name = '{{ connected_environment_name }}' -- required
AND component_name = '{{ component_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the Dapr Components for a connected environment. Get the Dapr Components for a connected environment.

```sql
SELECT
id,
name,
componentType,
deploymentErrors,
ignoreErrors,
initTimeout,
metadata,
provisioningState,
scopes,
secretStoreComponent,
secrets,
systemData,
type,
version
FROM azure.appcontainers.connected_environments_dapr_components
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND connected_environment_name = '{{ connected_environment_name }}' -- required
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

Creates or updates a Dapr Component. Creates or updates a Dapr Component in a connected environment.

```sql
INSERT INTO azure.appcontainers.connected_environments_dapr_components (
properties,
resource_group_name,
connected_environment_name,
component_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ connected_environment_name }}',
'{{ component_name }}',
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
- name: connected_environments_dapr_components
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connected_environments_dapr_components resource.
    - name: connected_environment_name
      value: "{{ connected_environment_name }}"
      description: Required parameter for the connected_environments_dapr_components resource.
    - name: component_name
      value: "{{ component_name }}"
      description: Required parameter for the connected_environments_dapr_components resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connected_environments_dapr_components resource.
    - name: properties
      description: |
        Dapr Component resource specific properties.
      value:
        componentType: "{{ componentType }}"
        version: "{{ version }}"
        ignoreErrors: {{ ignoreErrors }}
        initTimeout: "{{ initTimeout }}"
        secrets:
          - name: "{{ name }}"
            value: "{{ value }}"
            identity: "{{ identity }}"
            keyVaultUrl: "{{ keyVaultUrl }}"
        secretStoreComponent: "{{ secretStoreComponent }}"
        metadata:
          - name: "{{ name }}"
            value: "{{ value }}"
            secretRef: "{{ secretRef }}"
        scopes:
          - "{{ scopes }}"
        provisioningState: "{{ provisioningState }}"
        deploymentErrors: "{{ deploymentErrors }}"
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

Creates or updates a Dapr Component. Creates or updates a Dapr Component in a connected environment.

```sql
REPLACE azure.appcontainers.connected_environments_dapr_components
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND connected_environment_name = '{{ connected_environment_name }}' --required
AND component_name = '{{ component_name }}' --required
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

Delete a Dapr Component. Delete a Dapr Component from a connected environment.

```sql
DELETE FROM azure.appcontainers.connected_environments_dapr_components
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND connected_environment_name = '{{ connected_environment_name }}' --required
AND component_name = '{{ component_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_secrets"
    values={[
        { label: 'list_secrets', value: 'list_secrets' }
    ]}
>
<TabItem value="list_secrets">

List secrets for a dapr component. List secrets for a dapr component.

```sql
EXEC azure.appcontainers.connected_environments_dapr_components.list_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@connected_environment_name='{{ connected_environment_name }}' --required, 
@component_name='{{ component_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
