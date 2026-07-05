--- 
title: integration_service_environment_managed_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_managed_apis
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

Creates, updates, deletes, gets or lists an <code>integration_service_environment_managed_apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_service_environment_managed_apis" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.integration_service_environment_managed_apis" /></td></tr>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="apiDefinitionUrl" /></td>
    <td><code>string</code></td>
    <td>The API definition.</td>
</tr>
<tr>
    <td><CopyableCode code="apiDefinitions" /></td>
    <td><code>object</code></td>
    <td>The api definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="backendService" /></td>
    <td><code>object</code></td>
    <td>The backend service.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>The capabilities.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category. Known values are: "NotSpecified", "Enterprise", "Standard", and "Premium".</td>
</tr>
<tr>
    <td><CopyableCode code="connectionParameters" /></td>
    <td><code>object</code></td>
    <td>The connection parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentParameters" /></td>
    <td><code>object</code></td>
    <td>The integration service environment managed api deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="generalInformation" /></td>
    <td><code>object</code></td>
    <td>The api general information.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironment" /></td>
    <td><code>object</code></td>
    <td>The integration service environment reference.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>object</code></td>
    <td>The policies for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeUrls" /></td>
    <td><code>array</code></td>
    <td>The runtime urls.</td>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="apiDefinitionUrl" /></td>
    <td><code>string</code></td>
    <td>The API definition.</td>
</tr>
<tr>
    <td><CopyableCode code="apiDefinitions" /></td>
    <td><code>object</code></td>
    <td>The api definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="backendService" /></td>
    <td><code>object</code></td>
    <td>The backend service.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>The capabilities.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category. Known values are: "NotSpecified", "Enterprise", "Standard", and "Premium".</td>
</tr>
<tr>
    <td><CopyableCode code="connectionParameters" /></td>
    <td><code>object</code></td>
    <td>The connection parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentParameters" /></td>
    <td><code>object</code></td>
    <td>The integration service environment managed api deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="generalInformation" /></td>
    <td><code>object</code></td>
    <td>The api general information.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironment" /></td>
    <td><code>object</code></td>
    <td>The integration service environment reference.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>object</code></td>
    <td>The policies for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeUrls" /></td>
    <td><code>array</code></td>
    <td>The runtime urls.</td>
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
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-api_name"><code>api_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the integration service environment managed Api.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the integration service environment managed Apis.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-api_name"><code>api_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the integration service environment managed Api.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-integration_service_environment_name"><code>integration_service_environment_name</code></a>, <a href="#parameter-api_name"><code>api_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Puts the integration service environment managed Api.</td>
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
<tr id="parameter-api_name">
    <td><CopyableCode code="api_name" /></td>
    <td><code>string</code></td>
    <td>The api name. Required.</td>
</tr>
<tr id="parameter-integration_service_environment_name">
    <td><CopyableCode code="integration_service_environment_name" /></td>
    <td><code>string</code></td>
    <td>The integration service environment name. Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
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

Gets the integration service environment managed Api.

```sql
SELECT
id,
name,
apiDefinitionUrl,
apiDefinitions,
backendService,
capabilities,
category,
connectionParameters,
deploymentParameters,
generalInformation,
integrationServiceEnvironment,
location,
metadata,
policies,
provisioningState,
runtimeUrls,
tags,
type
FROM azure.logic.integration_service_environment_managed_apis
WHERE resource_group = '{{ resource_group }}' -- required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' -- required
AND api_name = '{{ api_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the integration service environment managed Apis.

```sql
SELECT
id,
name,
apiDefinitionUrl,
apiDefinitions,
backendService,
capabilities,
category,
connectionParameters,
deploymentParameters,
generalInformation,
integrationServiceEnvironment,
location,
metadata,
policies,
provisioningState,
runtimeUrls,
tags,
type
FROM azure.logic.integration_service_environment_managed_apis
WHERE resource_group = '{{ resource_group }}' -- required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
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

Deletes the integration service environment managed Api.

```sql
DELETE FROM azure.logic.integration_service_environment_managed_apis
WHERE resource_group = '{{ resource_group }}' --required
AND integration_service_environment_name = '{{ integration_service_environment_name }}' --required
AND api_name = '{{ api_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' }
    ]}
>
<TabItem value="put">

Puts the integration service environment managed Api.

```sql
EXEC azure.logic.integration_service_environment_managed_apis.put 
@resource_group='{{ resource_group }}' --required, 
@integration_service_environment_name='{{ integration_service_environment_name }}' --required, 
@api_name='{{ api_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
