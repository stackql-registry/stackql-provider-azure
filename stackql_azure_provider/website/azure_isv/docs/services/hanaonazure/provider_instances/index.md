--- 
title: provider_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_instances
  - hanaonazure
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>provider_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.hanaonazure.provider_instances" /></td></tr>
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
    <td><CopyableCode code="metadata" /></td>
    <td><code>string</code></td>
    <td>A JSON string containing metadata of the provider instance.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>string</code></td>
    <td>A JSON string containing the properties of the provider instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the provider instance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Accepted, Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>string</code></td>
    <td>A JSON string containing metadata of the provider instance.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>string</code></td>
    <td>A JSON string containing the properties of the provider instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the provider instance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Accepted, Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-provider_instance_name"><code>provider_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets properties of a provider instance. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of provider instances in the specified SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-provider_instance_name"><code>provider_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a provider instance. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_monitor_name"><code>sap_monitor_name</code></a>, <a href="#parameter-provider_instance_name"><code>provider_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a provider instance. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.</td>
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
<tr id="parameter-provider_instance_name">
    <td><CopyableCode code="provider_instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of the provider instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sap_monitor_name">
    <td><CopyableCode code="sap_monitor_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SAP monitor resource. Required.</td>
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

Gets properties of a provider instance. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
SELECT
id,
name,
metadata,
properties,
provisioningState,
systemData,
type
FROM azure_isv.hanaonazure.provider_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_monitor_name = '{{ sap_monitor_name }}' -- required
AND provider_instance_name = '{{ provider_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of provider instances in the specified SAP monitor. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
SELECT
id,
name,
metadata,
properties,
provisioningState,
systemData,
type
FROM azure_isv.hanaonazure.provider_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_monitor_name = '{{ sap_monitor_name }}' -- required
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

Creates a provider instance. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
INSERT INTO azure_isv.hanaonazure.provider_instances (
properties,
resource_group_name,
sap_monitor_name,
provider_instance_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sap_monitor_name }}',
'{{ provider_instance_name }}',
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
- name: provider_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the provider_instances resource.
    - name: sap_monitor_name
      value: "{{ sap_monitor_name }}"
      description: Required parameter for the provider_instances resource.
    - name: provider_instance_name
      value: "{{ provider_instance_name }}"
      description: Required parameter for the provider_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the provider_instances resource.
    - name: properties
      description: |
        Provider Instance properties.
      value:
        type: "{{ type }}"
        properties: "{{ properties }}"
        metadata: "{{ metadata }}"
        provisioningState: "{{ provisioningState }}"
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

Deletes a provider instance. The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

```sql
DELETE FROM azure_isv.hanaonazure.provider_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sap_monitor_name = '{{ sap_monitor_name }}' --required
AND provider_instance_name = '{{ provider_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
