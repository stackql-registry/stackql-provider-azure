--- 
title: springbootservers
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootservers
  - springappdiscovery
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>springbootservers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="springbootservers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.springappdiscovery.springbootservers" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdnAndIpAddressList" /></td>
    <td><code>array</code></td>
    <td>The alternative FQDN or IP addresses to discover for this server.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmId" /></td>
    <td><code>string</code></td>
    <td>The machine Id from ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Target server port for remote login.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="server" /></td>
    <td><code>string</code></td>
    <td>Server is the target server name or ip address to discover of SpringBootServer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="springBootApps" /></td>
    <td><code>integer</code></td>
    <td>The total number of spring boot apps been discovered.</td>
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
    <td><CopyableCode code="totalApps" /></td>
    <td><code>integer</code></td>
    <td>The total number of apps been discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdnAndIpAddressList" /></td>
    <td><code>array</code></td>
    <td>The alternative FQDN or IP addresses to discover for this server.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmId" /></td>
    <td><code>string</code></td>
    <td>The machine Id from ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Target server port for remote login.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="server" /></td>
    <td><code>string</code></td>
    <td>Server is the target server name or ip address to discover of SpringBootServer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="springBootApps" /></td>
    <td><code>integer</code></td>
    <td>The total number of spring boot apps been discovered.</td>
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
    <td><CopyableCode code="totalApps" /></td>
    <td><code>integer</code></td>
    <td>The total number of apps been discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdnAndIpAddressList" /></td>
    <td><code>array</code></td>
    <td>The alternative FQDN or IP addresses to discover for this server.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmId" /></td>
    <td><code>string</code></td>
    <td>The machine Id from ARM.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Target server port for remote login.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="server" /></td>
    <td><code>string</code></td>
    <td>Server is the target server name or ip address to discover of SpringBootServer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="springBootApps" /></td>
    <td><code>integer</code></td>
    <td>The total number of spring boot apps been discovered.</td>
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
    <td><CopyableCode code="totalApps" /></td>
    <td><code>integer</code></td>
    <td>The total number of apps been discovered.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-springbootservers_name"><code>springbootservers_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List springbootservers resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List springbootservers resource by resourceGroup.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List springbootservers resource by subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-springbootservers_name"><code>springbootservers_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create springbootservers resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-springbootservers_name"><code>springbootservers_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update springbootservers resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-springbootservers_name"><code>springbootservers_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create springbootservers resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-springbootservers_name"><code>springbootservers_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete springbootservers resource.</td>
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
<tr id="parameter-site_name">
    <td><CopyableCode code="site_name" /></td>
    <td><code>string</code></td>
    <td>The springbootsites name. Required.</td>
</tr>
<tr id="parameter-springbootservers_name">
    <td><CopyableCode code="springbootservers_name" /></td>
    <td><code>string</code></td>
    <td>The springbootservers name. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

List springbootservers resource.

```sql
SELECT
id,
name,
errors,
fqdnAndIpAddressList,
machineArmId,
port,
provisioningState,
server,
springBootApps,
systemData,
tags,
totalApps,
type
FROM azure_extras.springappdiscovery.springbootservers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND springbootservers_name = '{{ springbootservers_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List springbootservers resource by resourceGroup.

```sql
SELECT
id,
name,
errors,
fqdnAndIpAddressList,
machineArmId,
port,
provisioningState,
server,
springBootApps,
systemData,
tags,
totalApps,
type
FROM azure_extras.springappdiscovery.springbootservers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List springbootservers resource by subscription.

```sql
SELECT
id,
name,
errors,
fqdnAndIpAddressList,
machineArmId,
port,
provisioningState,
server,
springBootApps,
systemData,
tags,
totalApps,
type
FROM azure_extras.springappdiscovery.springbootservers
WHERE site_name = '{{ site_name }}' -- required
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

Create springbootservers resource.

```sql
INSERT INTO azure_extras.springappdiscovery.springbootservers (
tags,
properties,
resource_group_name,
site_name,
springbootservers_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ site_name }}',
'{{ springbootservers_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: springbootservers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the springbootservers resource.
    - name: site_name
      value: "{{ site_name }}"
      description: Required parameter for the springbootservers resource.
    - name: springbootservers_name
      value: "{{ springbootservers_name }}"
      description: Required parameter for the springbootservers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the springbootservers resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        The springbootservers resource definition.
      value:
        port: {{ port }}
        server: "{{ server }}"
        fqdnAndIpAddressList:
          - "{{ fqdnAndIpAddressList }}"
        machineArmId: "{{ machineArmId }}"
        totalApps: {{ totalApps }}
        springBootApps: {{ springBootApps }}
        errors:
          - id: {{ id }}
            code: "{{ code }}"
            summaryMessage: "{{ summaryMessage }}"
            runAsAccountId: "{{ runAsAccountId }}"
            message: "{{ message }}"
            possibleCauses: "{{ possibleCauses }}"
            recommendedAction: "{{ recommendedAction }}"
            severity: "{{ severity }}"
            updatedTimeStamp: "{{ updatedTimeStamp }}"
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

Update springbootservers resource.

```sql
UPDATE azure_extras.springappdiscovery.springbootservers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND site_name = '{{ site_name }}' --required
AND springbootservers_name = '{{ springbootservers_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create springbootservers resource.

```sql
REPLACE azure_extras.springappdiscovery.springbootservers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND site_name = '{{ site_name }}' --required
AND springbootservers_name = '{{ springbootservers_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete springbootservers resource.

```sql
DELETE FROM azure_extras.springappdiscovery.springbootservers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND site_name = '{{ site_name }}' --required
AND springbootservers_name = '{{ springbootservers_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
