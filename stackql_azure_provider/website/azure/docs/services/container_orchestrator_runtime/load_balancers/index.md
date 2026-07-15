--- 
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - container_orchestrator_runtime
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

Creates, updates, deletes, gets or lists a <code>load_balancers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_orchestrator_runtime.load_balancers" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addresses" /></td>
    <td><code>array</code></td>
    <td>IP Range. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="advertiseMode" /></td>
    <td><code>string</code></td>
    <td>Advertise Mode. Required. Known values are: "ARP", "BGP", and "Both". (ARP, BGP, Both)</td>
</tr>
<tr>
    <td><CopyableCode code="bgpPeers" /></td>
    <td><code>array</code></td>
    <td>The list of BGP peers it should advertise to. Null or empty means to advertise to all peers.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provision state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceSelector" /></td>
    <td><code>object</code></td>
    <td>A dynamic label mapping to select related services. For instance, if you want to create a load balancer only for services with label "a=b", then please specify &#123;"a": "b"&#125; in the field.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addresses" /></td>
    <td><code>array</code></td>
    <td>IP Range. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="advertiseMode" /></td>
    <td><code>string</code></td>
    <td>Advertise Mode. Required. Known values are: "ARP", "BGP", and "Both". (ARP, BGP, Both)</td>
</tr>
<tr>
    <td><CopyableCode code="bgpPeers" /></td>
    <td><code>array</code></td>
    <td>The list of BGP peers it should advertise to. Null or empty means to advertise to all peers.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provision state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceSelector" /></td>
    <td><code>object</code></td>
    <td>A dynamic label mapping to select related services. For instance, if you want to create a load balancer only for services with label "a=b", then please specify &#123;"a": "b"&#125; in the field.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a></td>
    <td></td>
    <td>Get a LoadBalancer.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>List LoadBalancer resources by parent.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a></td>
    <td></td>
    <td>Create a LoadBalancer.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a></td>
    <td></td>
    <td>Create a LoadBalancer.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a></td>
    <td></td>
    <td>Delete a LoadBalancer.</td>
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
<tr id="parameter-load_balancer_name">
    <td><CopyableCode code="load_balancer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the LoadBalancer. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
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

Get a LoadBalancer.

```sql
SELECT
id,
name,
addresses,
advertiseMode,
bgpPeers,
provisioningState,
serviceSelector,
systemData,
type
FROM azure.container_orchestrator_runtime.load_balancers
WHERE resource_uri = '{{ resource_uri }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List LoadBalancer resources by parent.

```sql
SELECT
id,
name,
addresses,
advertiseMode,
bgpPeers,
provisioningState,
serviceSelector,
systemData,
type
FROM azure.container_orchestrator_runtime.load_balancers
WHERE resource_uri = '{{ resource_uri }}' -- required
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

Create a LoadBalancer.

```sql
INSERT INTO azure.container_orchestrator_runtime.load_balancers (
properties,
resource_uri,
load_balancer_name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ load_balancer_name }}'
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
- name: load_balancers
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the load_balancers resource.
    - name: load_balancer_name
      value: "{{ load_balancer_name }}"
      description: Required parameter for the load_balancers resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        addresses:
          - "{{ addresses }}"
        serviceSelector: "{{ serviceSelector }}"
        advertiseMode: "{{ advertiseMode }}"
        bgpPeers:
          - "{{ bgpPeers }}"
        provisioningState: "{{ provisioningState }}"
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

Create a LoadBalancer.

```sql
REPLACE azure.container_orchestrator_runtime.load_balancers
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
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

Delete a LoadBalancer.

```sql
DELETE FROM azure.container_orchestrator_runtime.load_balancers
WHERE resource_uri = '{{ resource_uri }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
;
```
</TabItem>
</Tabs>
