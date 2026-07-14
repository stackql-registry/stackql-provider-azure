--- 
title: broker_authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_authorization
  - iot_operations
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

Creates, updates, deletes, gets or lists a <code>broker_authorization</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="broker_authorization" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_operations.broker_authorization" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
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
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>object</code></td>
    <td>The list of authorization policies supported by the Authorization Resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
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
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>object</code></td>
    <td>The list of authorization policies supported by the Authorization Resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a BrokerAuthorizationResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List BrokerAuthorizationResource resources by BrokerResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a BrokerAuthorizationResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a BrokerAuthorizationResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a BrokerAuthorizationResource.</td>
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
<tr id="parameter-authorization_name">
    <td><CopyableCode code="authorization_name" /></td>
    <td><code>string</code></td>
    <td>Name of Instance broker authorization resource. Required.</td>
</tr>
<tr id="parameter-broker_name">
    <td><CopyableCode code="broker_name" /></td>
    <td><code>string</code></td>
    <td>Name of broker. Required.</td>
</tr>
<tr id="parameter-instance_name">
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of instance. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
    ]}
>
<TabItem value="get">

Get a BrokerAuthorizationResource.

```sql
SELECT
id,
name,
authorizationPolicies,
extendedLocation,
healthState,
provisioningState,
systemData,
type
FROM azure.iot_operations.broker_authorization
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
AND broker_name = '{{ broker_name }}' -- required
AND authorization_name = '{{ authorization_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List BrokerAuthorizationResource resources by BrokerResource.

```sql
SELECT
id,
name,
authorizationPolicies,
extendedLocation,
healthState,
provisioningState,
systemData,
type
FROM azure.iot_operations.broker_authorization
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
AND broker_name = '{{ broker_name }}' -- required
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

Create a BrokerAuthorizationResource.

```sql
INSERT INTO azure.iot_operations.broker_authorization (
properties,
extendedLocation,
resource_group_name,
instance_name,
broker_name,
authorization_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ instance_name }}',
'{{ broker_name }}',
'{{ authorization_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: broker_authorization
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the broker_authorization resource.
    - name: instance_name
      value: "{{ instance_name }}"
      description: Required parameter for the broker_authorization resource.
    - name: broker_name
      value: "{{ broker_name }}"
      description: Required parameter for the broker_authorization resource.
    - name: authorization_name
      value: "{{ authorization_name }}"
      description: Required parameter for the broker_authorization resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the broker_authorization resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        authorizationPolicies:
          cache: "{{ cache }}"
          rules:
            - brokerResources: "{{ brokerResources }}"
              principals:
                attributes: "{{ attributes }}"
                clientIds:
                  - "{{ clientIds }}"
                usernames:
                  - "{{ usernames }}"
              stateStoreResources: "{{ stateStoreResources }}"
        provisioningState: "{{ provisioningState }}"
        healthState: "{{ healthState }}"
    - name: extendedLocation
      description: |
        Edge location of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Create a BrokerAuthorizationResource.

```sql
REPLACE azure.iot_operations.broker_authorization
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND broker_name = '{{ broker_name }}' --required
AND authorization_name = '{{ authorization_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
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

Delete a BrokerAuthorizationResource.

```sql
DELETE FROM azure.iot_operations.broker_authorization
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND broker_name = '{{ broker_name }}' --required
AND authorization_name = '{{ authorization_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
