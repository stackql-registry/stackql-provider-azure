--- 
title: security_policies_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies_interface
  - service_networking
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

Creates, updates, deletes, gets or lists a <code>security_policies_interface</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="security_policies_interface" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.security_policies_interface" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_traffic_controller', value: 'list_by_traffic_controller' }
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
    <td><CopyableCode code="ipAccessRulesPolicy" /></td>
    <td><code>object</code></td>
    <td>Ip Access Policy of the Traffic Controller Security Policy. Single Security Policy can have only one policy type set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>Type of the Traffic Controller Security Policy. Known values are: "waf" and "ipAccessRules". (waf, ipAccessRules)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of Traffic Controller SecurityPolicy Resource. Known values are: "Provisioning", "Updating", "Deleting", "Accepted", "Succeeded", "Failed", and "Canceled". (Provisioning, Updating, Deleting, Accepted, Succeeded, Failed, Canceled)</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="wafPolicy" /></td>
    <td><code>object</code></td>
    <td>Web Application Firewall Policy of the Traffic Controller Security Policy. Single Security Policy can have only one policy type set.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_traffic_controller">

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
    <td><CopyableCode code="ipAccessRulesPolicy" /></td>
    <td><code>object</code></td>
    <td>Ip Access Policy of the Traffic Controller Security Policy. Single Security Policy can have only one policy type set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>Type of the Traffic Controller Security Policy. Known values are: "waf" and "ipAccessRules". (waf, ipAccessRules)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of Traffic Controller SecurityPolicy Resource. Known values are: "Provisioning", "Updating", "Deleting", "Accepted", "Succeeded", "Failed", and "Canceled". (Provisioning, Updating, Deleting, Accepted, Succeeded, Failed, Canceled)</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="wafPolicy" /></td>
    <td><code>object</code></td>
    <td>Web Application Firewall Policy of the Traffic Controller Security Policy. Single Security Policy can have only one policy type set.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-traffic_controller_name"><code>traffic_controller_name</code></a>, <a href="#parameter-security_policy_name"><code>security_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a SecurityPolicy.</td>
</tr>
<tr>
    <td><a href="#list_by_traffic_controller"><CopyableCode code="list_by_traffic_controller" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-traffic_controller_name"><code>traffic_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List SecurityPolicy resources by TrafficController.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-traffic_controller_name"><code>traffic_controller_name</code></a>, <a href="#parameter-security_policy_name"><code>security_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a SecurityPolicy.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-traffic_controller_name"><code>traffic_controller_name</code></a>, <a href="#parameter-security_policy_name"><code>security_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a SecurityPolicy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-traffic_controller_name"><code>traffic_controller_name</code></a>, <a href="#parameter-security_policy_name"><code>security_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a SecurityPolicy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-traffic_controller_name"><code>traffic_controller_name</code></a>, <a href="#parameter-security_policy_name"><code>security_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a SecurityPolicy.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-security_policy_name">
    <td><CopyableCode code="security_policy_name" /></td>
    <td><code>string</code></td>
    <td>SecurityPolicy. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-traffic_controller_name">
    <td><CopyableCode code="traffic_controller_name" /></td>
    <td><code>string</code></td>
    <td>traffic controller name for path. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_traffic_controller', value: 'list_by_traffic_controller' }
    ]}
>
<TabItem value="get">

Get a SecurityPolicy.

```sql
SELECT
id,
name,
ipAccessRulesPolicy,
location,
policyType,
provisioningState,
systemData,
tags,
type,
wafPolicy
FROM azure.service_networking.security_policies_interface
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND traffic_controller_name = '{{ traffic_controller_name }}' -- required
AND security_policy_name = '{{ security_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_traffic_controller">

List SecurityPolicy resources by TrafficController.

```sql
SELECT
id,
name,
ipAccessRulesPolicy,
location,
policyType,
provisioningState,
systemData,
tags,
type,
wafPolicy
FROM azure.service_networking.security_policies_interface
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND traffic_controller_name = '{{ traffic_controller_name }}' -- required
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

Create a SecurityPolicy.

```sql
INSERT INTO azure.service_networking.security_policies_interface (
tags,
location,
properties,
resource_group_name,
traffic_controller_name,
security_policy_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ traffic_controller_name }}',
'{{ security_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: security_policies_interface
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the security_policies_interface resource.
    - name: traffic_controller_name
      value: "{{ traffic_controller_name }}"
      description: Required parameter for the security_policies_interface resource.
    - name: security_policy_name
      value: "{{ security_policy_name }}"
      description: Required parameter for the security_policies_interface resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the security_policies_interface resource.
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
        The resource-specific properties for this resource.
      value:
        policyType: "{{ policyType }}"
        wafPolicy:
          id: "{{ id }}"
        ipAccessRulesPolicy:
          rules:
            - name: "{{ name }}"
              priority: {{ priority }}
              sourceAddressPrefixes: "{{ sourceAddressPrefixes }}"
              action: "{{ action }}"
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

Update a SecurityPolicy.

```sql
UPDATE azure.service_networking.security_policies_interface
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND traffic_controller_name = '{{ traffic_controller_name }}' --required
AND security_policy_name = '{{ security_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create a SecurityPolicy.

```sql
REPLACE azure.service_networking.security_policies_interface
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND traffic_controller_name = '{{ traffic_controller_name }}' --required
AND security_policy_name = '{{ security_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete a SecurityPolicy.

```sql
DELETE FROM azure.service_networking.security_policies_interface
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND traffic_controller_name = '{{ traffic_controller_name }}' --required
AND security_policy_name = '{{ security_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
