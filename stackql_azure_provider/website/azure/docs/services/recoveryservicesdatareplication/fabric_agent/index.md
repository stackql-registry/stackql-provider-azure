--- 
title: fabric_agent
hide_title: false
hide_table_of_contents: false
keywords:
  - fabric_agent
  - recoveryservicesdatareplication
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

Creates, updates, deletes, gets or lists a <code>fabric_agent</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fabric_agent" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesdatareplication.fabric_agent" /></td></tr>
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
    <td><CopyableCode code="authenticationIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity model. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric agent correlation Id.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Fabric agent model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="isResponsive" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether the fabric agent is responsive.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartbeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the time when last heartbeat was sent by the fabric agent.</td>
</tr>
<tr>
    <td><CopyableCode code="machineId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the machine Id where fabric agent is running. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the machine name where fabric agent is running. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the fabric agent. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAccessIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity model. Required.</td>
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
    <td><CopyableCode code="versionNumber" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric agent version.</td>
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
    <td><CopyableCode code="authenticationIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity model. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric agent correlation Id.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Fabric agent model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="isResponsive" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether the fabric agent is responsive.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartbeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the time when last heartbeat was sent by the fabric agent.</td>
</tr>
<tr>
    <td><CopyableCode code="machineId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the machine Id where fabric agent is running. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the machine name where fabric agent is running. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the fabric agent. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAccessIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity model. Required.</td>
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
    <td><CopyableCode code="versionNumber" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric agent version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-fabric_agent_name"><code>fabric_agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the fabric agent.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of fabric agents in the given fabric.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-fabric_agent_name"><code>fabric_agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates the fabric agent.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-fabric_agent_name"><code>fabric_agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes fabric agent.</td>
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
<tr id="parameter-fabric_agent_name">
    <td><CopyableCode code="fabric_agent_name" /></td>
    <td><code>string</code></td>
    <td>The fabric agent name. Required.</td>
</tr>
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>The fabric name. Required.</td>
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

Gets the details of the fabric agent.

```sql
SELECT
id,
name,
authenticationIdentity,
correlationId,
customProperties,
healthErrors,
isResponsive,
lastHeartbeat,
machineId,
machineName,
provisioningState,
resourceAccessIdentity,
systemData,
type,
versionNumber
FROM azure.recoveryservicesdatareplication.fabric_agent
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND fabric_agent_name = '{{ fabric_agent_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of fabric agents in the given fabric.

```sql
SELECT
id,
name,
authenticationIdentity,
correlationId,
customProperties,
healthErrors,
isResponsive,
lastHeartbeat,
machineId,
machineName,
provisioningState,
resourceAccessIdentity,
systemData,
type,
versionNumber
FROM azure.recoveryservicesdatareplication.fabric_agent
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
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

Creates the fabric agent.

```sql
INSERT INTO azure.recoveryservicesdatareplication.fabric_agent (
properties,
resource_group_name,
fabric_name,
fabric_agent_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ fabric_name }}',
'{{ fabric_agent_name }}',
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
- name: fabric_agent
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the fabric_agent resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the fabric_agent resource.
    - name: fabric_agent_name
      value: "{{ fabric_agent_name }}"
      description: Required parameter for the fabric_agent resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the fabric_agent resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        correlationId: "{{ correlationId }}"
        machineId: "{{ machineId }}"
        machineName: "{{ machineName }}"
        authenticationIdentity:
          tenantId: "{{ tenantId }}"
          applicationId: "{{ applicationId }}"
          objectId: "{{ objectId }}"
          audience: "{{ audience }}"
          aadAuthority: "{{ aadAuthority }}"
        resourceAccessIdentity:
          tenantId: "{{ tenantId }}"
          applicationId: "{{ applicationId }}"
          objectId: "{{ objectId }}"
          audience: "{{ audience }}"
          aadAuthority: "{{ aadAuthority }}"
        isResponsive: {{ isResponsive }}
        lastHeartbeat: "{{ lastHeartbeat }}"
        versionNumber: "{{ versionNumber }}"
        provisioningState: "{{ provisioningState }}"
        healthErrors:
          - affectedResourceType: "{{ affectedResourceType }}"
            affectedResourceCorrelationIds: "{{ affectedResourceCorrelationIds }}"
            childErrors: "{{ childErrors }}"
            code: "{{ code }}"
            healthCategory: "{{ healthCategory }}"
            category: "{{ category }}"
            severity: "{{ severity }}"
            source: "{{ source }}"
            creationTime: "{{ creationTime }}"
            isCustomerResolvable: {{ isCustomerResolvable }}
            summary: "{{ summary }}"
            message: "{{ message }}"
            causes: "{{ causes }}"
            recommendation: "{{ recommendation }}"
        customProperties:
          instanceType: "{{ instanceType }}"
`}</CodeBlock>

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

Deletes fabric agent.

```sql
DELETE FROM azure.recoveryservicesdatareplication.fabric_agent
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND fabric_agent_name = '{{ fabric_agent_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
