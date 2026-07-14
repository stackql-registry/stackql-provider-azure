--- 
title: vm_instance_guest_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_instance_guest_agents
  - connected_vmware
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

Creates, updates, deletes, gets or lists a <code>vm_instance_guest_agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vm_instance_guest_agents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.connected_vmware.vm_instance_guest_agents" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials" /></td>
    <td><code>object</code></td>
    <td>Username / Password Credentials to provision guest agent.</td>
</tr>
<tr>
    <td><CopyableCode code="customResourceName" /></td>
    <td><code>string</code></td>
    <td>Gets the name of the corresponding resource in Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="httpProxyConfig" /></td>
    <td><code>object</code></td>
    <td>HTTP Proxy configuration for the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopeResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the private link scope this machine is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningAction" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the guest agent provisioning action. Known values are: "install", "uninstall", and "repair".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the guest agent status.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
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
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for this resource.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Gets GuestAgent. Implements GuestAgent GET method.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements GuestAgent PUT method. Create Or Update GuestAgent.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Deletes an GuestAgent. Implements GuestAgent DELETE method.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements GET GuestAgent in a vm. Returns the list of GuestAgent of the given vm.</td>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets GuestAgent. Implements GuestAgent GET method.

```sql
SELECT
id,
name,
credentials,
customResourceName,
httpProxyConfig,
privateLinkScopeResourceId,
provisioningAction,
provisioningState,
status,
statuses,
systemData,
type,
uuid
FROM azure.connected_vmware.vm_instance_guest_agents
WHERE resource_uri = '{{ resource_uri }}' -- required
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

Implements GuestAgent PUT method. Create Or Update GuestAgent.

```sql
INSERT INTO azure.connected_vmware.vm_instance_guest_agents (
properties,
resource_uri
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}'
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
- name: vm_instance_guest_agents
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the vm_instance_guest_agents resource.
    - name: properties
      value:
        credentials:
          username: "{{ username }}"
          password: "{{ password }}"
        privateLinkScopeResourceId: "{{ privateLinkScopeResourceId }}"
        httpProxyConfig:
          httpsProxy: "{{ httpsProxy }}"
        provisioningAction: "{{ provisioningAction }}"
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

Deletes an GuestAgent. Implements GuestAgent DELETE method.

```sql
DELETE FROM azure.connected_vmware.vm_instance_guest_agents
WHERE resource_uri = '{{ resource_uri }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

Implements GET GuestAgent in a vm. Returns the list of GuestAgent of the given vm.

```sql
EXEC azure.connected_vmware.vm_instance_guest_agents.list_raw 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
</Tabs>
