--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_detector"
    values={[
        { label: 'get_detector', value: 'get_detector' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_detector">

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
    <td><CopyableCode code="dataProviderMetadata" /></td>
    <td><code>object</code></td>
    <td>List of data providers' metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>array</code></td>
    <td>Set of data collections associated with the response.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of the diagnostics response.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of the diagnostics response.</td>
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
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>Container Apps Job configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of environment.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the container apps job.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound IP Addresses of a container apps job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Container Apps Job. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container Apps job definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name to pin for container apps job execution.</td>
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
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>Container Apps Job configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of environment.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the container apps job.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound IP Addresses of a container apps job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Container Apps Job. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container Apps job definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name to pin for container apps job execution.</td>
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
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>Container Apps Job configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of environment.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the container apps job.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound IP Addresses of a container apps job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Container Apps Job. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>Container Apps job definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name to pin for container apps job execution.</td>
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
    <td><a href="#get_detector"><CopyableCode code="get_detector" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the diagnostics data for a given Container App Job. Get the diagnostics data for a Container App Job.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a Container Apps Job. Get the properties of a Container Apps Job.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Container Apps Jobs in a given resource group. Get the Container Apps Jobs in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Container Apps Jobs in a given subscription. Get the Container Apps Jobs in a given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or Update a Container Apps Job. Create or Update a Container Apps Job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update properties of a Container Apps Job. Patches a Container Apps Job using JSON Merge Patch.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or Update a Container Apps Job. Create or Update a Container Apps Job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Container Apps Job. Delete a Container Apps Job.</td>
</tr>
<tr>
    <td><a href="#list_secrets"><CopyableCode code="list_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List secrets for a container apps job. List secrets for a container apps job.</td>
</tr>
<tr>
    <td><a href="#list_detectors"><CopyableCode code="list_detectors" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the list of diagnostics for a given Container App Job. Get the list of diagnostics for a Container App Job.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start a Container Apps Job. Start a Container Apps Job.</td>
</tr>
<tr>
    <td><a href="#stop_multiple_executions"><CopyableCode code="stop_multiple_executions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Terminates execution of a running container apps job. Terminates execution of a running container apps job.</td>
</tr>
<tr>
    <td><a href="#stop_execution"><CopyableCode code="stop_execution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_execution_name"><code>job_execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Terminates execution of a running container apps job. Terminates execution of a running container apps job.</td>
</tr>
<tr>
    <td><a href="#proxy_get"><CopyableCode code="proxy_get" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-api_name"><code>api_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a Container App Job. Get the properties for a given Container App Job.</td>
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
    <td>Proxy API Name for Container App Job. Required.</td>
</tr>
<tr id="parameter-detector_name">
    <td><CopyableCode code="detector_name" /></td>
    <td><code>string</code></td>
    <td>Proxy API Name for Container App Job. Required.</td>
</tr>
<tr id="parameter-job_execution_name">
    <td><CopyableCode code="job_execution_name" /></td>
    <td><code>string</code></td>
    <td>Job execution name. Required.</td>
</tr>
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>Job Name. Required.</td>
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
    defaultValue="get_detector"
    values={[
        { label: 'get_detector', value: 'get_detector' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_detector">

Get the diagnostics data for a given Container App Job. Get the diagnostics data for a Container App Job.

```sql
SELECT
id,
name,
dataProviderMetadata,
dataset,
metadata,
status,
systemData,
type
FROM azure.appcontainers.jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the properties of a Container Apps Job. Get the properties of a Container Apps Job.

```sql
SELECT
id,
name,
configuration,
environmentId,
eventStreamEndpoint,
identity,
location,
outboundIpAddresses,
provisioningState,
systemData,
tags,
template,
type,
workloadProfileName
FROM azure.appcontainers.jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get the Container Apps Jobs in a given resource group. Get the Container Apps Jobs in a given resource group.

```sql
SELECT
id,
name,
configuration,
environmentId,
eventStreamEndpoint,
identity,
location,
outboundIpAddresses,
provisioningState,
systemData,
tags,
template,
type,
workloadProfileName
FROM azure.appcontainers.jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get the Container Apps Jobs in a given subscription. Get the Container Apps Jobs in a given subscription.

```sql
SELECT
id,
name,
configuration,
environmentId,
eventStreamEndpoint,
identity,
location,
outboundIpAddresses,
provisioningState,
systemData,
tags,
template,
type,
workloadProfileName
FROM azure.appcontainers.jobs
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or Update a Container Apps Job. Create or Update a Container Apps Job.

```sql
INSERT INTO azure.appcontainers.jobs (
tags,
location,
properties,
identity,
resource_group_name,
job_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ job_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: jobs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the jobs resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the jobs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the jobs resource.
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
        Container Apps Job resource specific properties.
      value:
        provisioningState: "{{ provisioningState }}"
        environmentId: "{{ environmentId }}"
        workloadProfileName: "{{ workloadProfileName }}"
        configuration:
          secrets:
            - name: "{{ name }}"
              value: "{{ value }}"
              identity: "{{ identity }}"
              keyVaultUrl: "{{ keyVaultUrl }}"
          triggerType: "{{ triggerType }}"
          replicaTimeout: {{ replicaTimeout }}
          replicaRetryLimit: {{ replicaRetryLimit }}
          manualTriggerConfig:
            replicaCompletionCount: {{ replicaCompletionCount }}
            parallelism: {{ parallelism }}
          scheduleTriggerConfig:
            replicaCompletionCount: {{ replicaCompletionCount }}
            cronExpression: "{{ cronExpression }}"
            parallelism: {{ parallelism }}
          eventTriggerConfig:
            replicaCompletionCount: {{ replicaCompletionCount }}
            parallelism: {{ parallelism }}
            scale:
              pollingInterval: {{ pollingInterval }}
              minExecutions: {{ minExecutions }}
              maxExecutions: {{ maxExecutions }}
              rules:
                - name: "{{ name }}"
                  type: "{{ type }}"
                  metadata: "{{ metadata }}"
                  auth: "{{ auth }}"
                  identity: "{{ identity }}"
          registries:
            - server: "{{ server }}"
              username: "{{ username }}"
              passwordSecretRef: "{{ passwordSecretRef }}"
              identity: "{{ identity }}"
          identitySettings:
            - identity: "{{ identity }}"
              lifecycle: "{{ lifecycle }}"
        template:
          initContainers:
            - image: "{{ image }}"
              name: "{{ name }}"
              command: "{{ command }}"
              args: "{{ args }}"
              env: "{{ env }}"
              resources:
                cpu: {{ cpu }}
                memory: "{{ memory }}"
                ephemeralStorage: "{{ ephemeralStorage }}"
              volumeMounts: "{{ volumeMounts }}"
          containers:
            - image: "{{ image }}"
              name: "{{ name }}"
              command: "{{ command }}"
              args: "{{ args }}"
              env: "{{ env }}"
              resources:
                cpu: {{ cpu }}
                memory: "{{ memory }}"
                ephemeralStorage: "{{ ephemeralStorage }}"
              volumeMounts: "{{ volumeMounts }}"
              probes: "{{ probes }}"
          volumes:
            - name: "{{ name }}"
              storageType: "{{ storageType }}"
              storageName: "{{ storageName }}"
              secrets: "{{ secrets }}"
              mountOptions: "{{ mountOptions }}"
        outboundIpAddresses:
          - "{{ outboundIpAddresses }}"
        eventStreamEndpoint: "{{ eventStreamEndpoint }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
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

Update properties of a Container Apps Job. Patches a Container Apps Job using JSON Merge Patch.

```sql
UPDATE azure.appcontainers.jobs
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Create or Update a Container Apps Job. Create or Update a Container Apps Job.

```sql
REPLACE azure.appcontainers.jobs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Delete a Container Apps Job. Delete a Container Apps Job.

```sql
DELETE FROM azure.appcontainers.jobs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_secrets"
    values={[
        { label: 'list_secrets', value: 'list_secrets' },
        { label: 'list_detectors', value: 'list_detectors' },
        { label: 'start', value: 'start' },
        { label: 'stop_multiple_executions', value: 'stop_multiple_executions' },
        { label: 'stop_execution', value: 'stop_execution' },
        { label: 'proxy_get', value: 'proxy_get' }
    ]}
>
<TabItem value="list_secrets">

List secrets for a container apps job. List secrets for a container apps job.

```sql
EXEC azure.appcontainers.jobs.list_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_detectors">

Get the list of diagnostics for a given Container App Job. Get the list of diagnostics for a Container App Job.

```sql
EXEC azure.appcontainers.jobs.list_detectors 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start a Container Apps Job. Start a Container Apps Job.

```sql
EXEC azure.appcontainers.jobs.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"containers": "{{ containers }}", 
"initContainers": "{{ initContainers }}"
}'
;
```
</TabItem>
<TabItem value="stop_multiple_executions">

Terminates execution of a running container apps job. Terminates execution of a running container apps job.

```sql
EXEC azure.appcontainers.jobs.stop_multiple_executions 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_execution">

Terminates execution of a running container apps job. Terminates execution of a running container apps job.

```sql
EXEC azure.appcontainers.jobs.stop_execution 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@job_execution_name='{{ job_execution_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="proxy_get">

Get the properties of a Container App Job. Get the properties for a given Container App Job.

```sql
EXEC azure.appcontainers.jobs.proxy_get 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@api_name='{{ api_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
