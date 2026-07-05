--- 
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
  - storagemover
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

Creates, updates, deletes, gets or lists an <code>agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagemover.agents" /></td></tr>
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
    <td><CopyableCode code="agentStatus" /></td>
    <td><code>string</code></td>
    <td>The Agent status. Known values are: "Registering", "Offline", "Online", "Executing", "RequiresAttention", and "Unregistering". (Registering, Offline, Online, Executing, RequiresAttention, Unregistering)</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>The Agent version.</td>
</tr>
<tr>
    <td><CopyableCode code="arcResourceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Hybrid Compute resource for the Agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="arcVmUuid" /></td>
    <td><code>string</code></td>
    <td>The VM UUID of the Hybrid Compute resource for the Agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>:vartype error_details: ~azure.mgmt.storagemover.models.AgentPropertiesErrorDetails</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusUpdate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last updated time of the Agent status.</td>
</tr>
<tr>
    <td><CopyableCode code="localIPAddress" /></td>
    <td><code>string</code></td>
    <td>Local IP address reported by the Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryInMB" /></td>
    <td><code>integer</code></td>
    <td>Available memory reported by the Agent, in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Available compute cores reported by the Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The agent's local time zone represented in Windows format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uploadLimitSchedule" /></td>
    <td><code>object</code></td>
    <td>The WAN-link upload limit schedule that applies to any Job Run the agent executes. Data plane operations (migrating files) are affected. Control plane operations ensure seamless migration functionality and are not limited by this schedule. The schedule is interpreted with the agent's local time.</td>
</tr>
<tr>
    <td><CopyableCode code="uptimeInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Uptime of the Agent in seconds.</td>
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
    <td><CopyableCode code="agentStatus" /></td>
    <td><code>string</code></td>
    <td>The Agent status. Known values are: "Registering", "Offline", "Online", "Executing", "RequiresAttention", and "Unregistering". (Registering, Offline, Online, Executing, RequiresAttention, Unregistering)</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>The Agent version.</td>
</tr>
<tr>
    <td><CopyableCode code="arcResourceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Hybrid Compute resource for the Agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="arcVmUuid" /></td>
    <td><code>string</code></td>
    <td>The VM UUID of the Hybrid Compute resource for the Agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>:vartype error_details: ~azure.mgmt.storagemover.models.AgentPropertiesErrorDetails</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusUpdate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last updated time of the Agent status.</td>
</tr>
<tr>
    <td><CopyableCode code="localIPAddress" /></td>
    <td><code>string</code></td>
    <td>Local IP address reported by the Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryInMB" /></td>
    <td><code>integer</code></td>
    <td>Available memory reported by the Agent, in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Available compute cores reported by the Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The agent's local time zone represented in Windows format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uploadLimitSchedule" /></td>
    <td><code>object</code></td>
    <td>The WAN-link upload limit schedule that applies to any Job Run the agent executes. Data plane operations (migrating files) are affected. Control plane operations ensure seamless migration functionality and are not limited by this schedule. The schedule is interpreted with the agent's local time.</td>
</tr>
<tr>
    <td><CopyableCode code="uptimeInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Uptime of the Agent in seconds.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Agent resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Agents in a Storage Mover.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an Agent resource, which references a hybrid compute machine that can run jobs.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Agent resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an Agent resource, which references a hybrid compute machine that can run jobs.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Agent resource.</td>
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
<tr id="parameter-agent_name">
    <td><CopyableCode code="agent_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Agent resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_mover_name">
    <td><CopyableCode code="storage_mover_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Storage Mover resource. Required.</td>
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

Gets an Agent resource.

```sql
SELECT
id,
name,
agentStatus,
agentVersion,
arcResourceId,
arcVmUuid,
description,
errorDetails,
lastStatusUpdate,
localIPAddress,
memoryInMB,
numberOfCores,
provisioningState,
systemData,
timeZone,
type,
uploadLimitSchedule,
uptimeInSeconds
FROM azure.storagemover.agents
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
AND agent_name = '{{ agent_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Agents in a Storage Mover.

```sql
SELECT
id,
name,
agentStatus,
agentVersion,
arcResourceId,
arcVmUuid,
description,
errorDetails,
lastStatusUpdate,
localIPAddress,
memoryInMB,
numberOfCores,
provisioningState,
systemData,
timeZone,
type,
uploadLimitSchedule,
uptimeInSeconds
FROM azure.storagemover.agents
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
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

Creates or updates an Agent resource, which references a hybrid compute machine that can run jobs.

```sql
INSERT INTO azure.storagemover.agents (
properties,
resource_group_name,
storage_mover_name,
agent_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ storage_mover_name }}',
'{{ agent_name }}',
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
- name: agents
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the agents resource.
    - name: storage_mover_name
      value: "{{ storage_mover_name }}"
      description: Required parameter for the agents resource.
    - name: agent_name
      value: "{{ agent_name }}"
      description: Required parameter for the agents resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the agents resource.
    - name: properties
      description: |
        Required.
      value:
        description: "{{ description }}"
        agentVersion: "{{ agentVersion }}"
        arcResourceId: "{{ arcResourceId }}"
        arcVmUuid: "{{ arcVmUuid }}"
        agentStatus: "{{ agentStatus }}"
        lastStatusUpdate: "{{ lastStatusUpdate }}"
        localIPAddress: "{{ localIPAddress }}"
        memoryInMB: {{ memoryInMB }}
        numberOfCores: {{ numberOfCores }}
        uptimeInSeconds: {{ uptimeInSeconds }}
        timeZone: "{{ timeZone }}"
        uploadLimitSchedule:
          weeklyRecurrences:
            - startTime:
                hour: {{ hour }}
                minute: "{{ minute }}"
              endTime:
                hour: {{ hour }}
                minute: "{{ minute }}"
              days: "{{ days }}"
              limitInMbps: {{ limitInMbps }}
        errorDetails:
          code: "{{ code }}"
          message: "{{ message }}"
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

Creates or updates an Agent resource.

```sql
UPDATE azure.storagemover.agents
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND agent_name = '{{ agent_name }}' --required
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

Creates or updates an Agent resource, which references a hybrid compute machine that can run jobs.

```sql
REPLACE azure.storagemover.agents
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND agent_name = '{{ agent_name }}' --required
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

Deletes an Agent resource.

```sql
DELETE FROM azure.storagemover.agents
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND agent_name = '{{ agent_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
