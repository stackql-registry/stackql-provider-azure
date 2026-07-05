--- 
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
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

Creates, updates, deletes, gets or lists a <code>workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workflows" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.workflows" /></td></tr>
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
    <td><CopyableCode code="accessControl" /></td>
    <td><code>object</code></td>
    <td>The access control configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="accessEndpoint" /></td>
    <td><code>string</code></td>
    <td>Gets the access endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the created time.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>The definition.</td>
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
    <td><CopyableCode code="integrationAccount" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironment" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets the version.</td>
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
    <td><CopyableCode code="accessControl" /></td>
    <td><code>object</code></td>
    <td>The access control configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="accessEndpoint" /></td>
    <td><code>string</code></td>
    <td>Gets the access endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the created time.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>The definition.</td>
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
    <td><CopyableCode code="integrationAccount" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironment" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets the version.</td>
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
    <td><CopyableCode code="accessControl" /></td>
    <td><code>object</code></td>
    <td>The access control configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="accessEndpoint" /></td>
    <td><code>string</code></td>
    <td>Gets the access endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the created time.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>The definition.</td>
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
    <td><CopyableCode code="integrationAccount" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationServiceEnvironment" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", "Completed", "Renewing", "Pending", "Waiting", and "InProgress".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Gets the version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a workflow.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a list of workflows by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a list of workflows by subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a workflow.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a workflow.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a workflow.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a workflow.</td>
</tr>
<tr>
    <td><a href="#list_callback_url"><CopyableCode code="list_callback_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the workflow callback Url.</td>
</tr>
<tr>
    <td><a href="#list_swagger"><CopyableCode code="list_swagger" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an OpenAPI definition for the workflow.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables a workflow.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enables a workflow.</td>
</tr>
<tr>
    <td><a href="#generate_upgraded_definition"><CopyableCode code="generate_upgraded_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates the upgraded definition for a workflow.</td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Moves an existing workflow.</td>
</tr>
<tr>
    <td><a href="#regenerate_access_key"><CopyableCode code="regenerate_access_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerates the callback URL access key for request triggers.</td>
</tr>
<tr>
    <td><a href="#validate_by_resource_group"><CopyableCode code="validate_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates the workflow.</td>
</tr>
<tr>
    <td><a href="#validate_by_location"><CopyableCode code="validate_by_location" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates the workflow definition.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The workflow location. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>The workflow name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId. Default value is None.</td>
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

Gets a workflow.

```sql
SELECT
id,
name,
accessControl,
accessEndpoint,
changedTime,
createdTime,
definition,
endpointsConfiguration,
identity,
integrationAccount,
integrationServiceEnvironment,
location,
parameters,
provisioningState,
sku,
state,
tags,
type,
version
FROM azure.logic.workflows
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of workflows by resource group.

```sql
SELECT
id,
name,
accessControl,
accessEndpoint,
changedTime,
createdTime,
definition,
endpointsConfiguration,
identity,
integrationAccount,
integrationServiceEnvironment,
location,
parameters,
provisioningState,
sku,
state,
tags,
type,
version
FROM azure.logic.workflows
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of workflows by subscription.

```sql
SELECT
id,
name,
accessControl,
accessEndpoint,
changedTime,
createdTime,
definition,
endpointsConfiguration,
identity,
integrationAccount,
integrationServiceEnvironment,
location,
parameters,
provisioningState,
sku,
state,
tags,
type,
version
FROM azure.logic.workflows
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
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

Creates or updates a workflow.

```sql
INSERT INTO azure.logic.workflows (
location,
tags,
identity,
properties,
resource_group_name,
workflow_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workflow_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workflows
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workflows resource.
    - name: workflow_name
      value: "{{ workflow_name }}"
      description: Required parameter for the workflows resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workflows resource.
    - name: location
      value: "{{ location }}"
      description: |
        The resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: identity
      description: |
        Managed service identity properties.
      value:
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        state: "{{ state }}"
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
        accessControl:
          triggers:
            allowedCallerIpAddresses:
              - addressRange: "{{ addressRange }}"
            openAuthenticationPolicies:
              policies: "{{ policies }}"
          contents:
            allowedCallerIpAddresses:
              - addressRange: "{{ addressRange }}"
            openAuthenticationPolicies:
              policies: "{{ policies }}"
          actions:
            allowedCallerIpAddresses:
              - addressRange: "{{ addressRange }}"
            openAuthenticationPolicies:
              policies: "{{ policies }}"
          workflowManagement:
            allowedCallerIpAddresses:
              - addressRange: "{{ addressRange }}"
            openAuthenticationPolicies:
              policies: "{{ policies }}"
        integrationAccount:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
        integrationServiceEnvironment:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
        definition: "{{ definition }}"
        parameters: "{{ parameters }}"
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

Updates a workflow.

```sql
UPDATE azure.logic.workflows
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
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

Creates or updates a workflow.

```sql
REPLACE azure.logic.workflows
SET 
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
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

Deletes a workflow.

```sql
DELETE FROM azure.logic.workflows
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_callback_url"
    values={[
        { label: 'list_callback_url', value: 'list_callback_url' },
        { label: 'list_swagger', value: 'list_swagger' },
        { label: 'disable', value: 'disable' },
        { label: 'enable', value: 'enable' },
        { label: 'generate_upgraded_definition', value: 'generate_upgraded_definition' },
        { label: 'move', value: 'move' },
        { label: 'regenerate_access_key', value: 'regenerate_access_key' },
        { label: 'validate_by_resource_group', value: 'validate_by_resource_group' },
        { label: 'validate_by_location', value: 'validate_by_location' }
    ]}
>
<TabItem value="list_callback_url">

Get the workflow callback Url.

```sql
EXEC azure.logic.workflows.list_callback_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"notAfter": "{{ notAfter }}", 
"keyType": "{{ keyType }}"
}'
;
```
</TabItem>
<TabItem value="list_swagger">

Gets an OpenAPI definition for the workflow.

```sql
EXEC azure.logic.workflows.list_swagger 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="disable">

Disables a workflow.

```sql
EXEC azure.logic.workflows.disable 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable">

Enables a workflow.

```sql
EXEC azure.logic.workflows.enable 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_upgraded_definition">

Generates the upgraded definition for a workflow.

```sql
EXEC azure.logic.workflows.generate_upgraded_definition 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetSchemaVersion": "{{ targetSchemaVersion }}"
}'
;
```
</TabItem>
<TabItem value="move">

Moves an existing workflow.

```sql
EXEC azure.logic.workflows.move 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}"
}'
;
```
</TabItem>
<TabItem value="regenerate_access_key">

Regenerates the callback URL access key for request triggers.

```sql
EXEC azure.logic.workflows.regenerate_access_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyType": "{{ keyType }}"
}'
;
```
</TabItem>
<TabItem value="validate_by_resource_group">

Validates the workflow.

```sql
EXEC azure.logic.workflows.validate_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="validate_by_location">

Validates the workflow definition.

```sql
EXEC azure.logic.workflows.validate_by_location 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
