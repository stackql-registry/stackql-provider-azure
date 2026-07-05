--- 
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - datadog
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

Creates, updates, deletes, gets or lists a <code>monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="monitors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.monitors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>ARM id of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="datadogOrganizationProperties" /></td>
    <td><code>object</code></td>
    <td>Specify the Datadog organization name. In the case of linking to existing organizations, Id, ApiKey, and Applicationkey is required as well.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.datadog.models.IdentityProperties</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state. Known values are: "Provisioning", "Active", "Suspended", and "Unsubscribed".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying if the resource monitoring is enabled or disabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.datadog.models.ResourceSku</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of .</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>Includes name, email and optionally, phone number. User Information can't be null.</td>
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
    <td>ARM id of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="datadogOrganizationProperties" /></td>
    <td><code>object</code></td>
    <td>Specify the Datadog organization name. In the case of linking to existing organizations, Id, ApiKey, and Applicationkey is required as well.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.datadog.models.IdentityProperties</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state. Known values are: "Provisioning", "Active", "Suspended", and "Unsubscribed".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying if the resource monitoring is enabled or disabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.datadog.models.ResourceSku</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of .</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>Includes name, email and optionally, phone number. User Information can't be null.</td>
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
    <td>ARM id of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="datadogOrganizationProperties" /></td>
    <td><code>object</code></td>
    <td>Specify the Datadog organization name. In the case of linking to existing organizations, Id, ApiKey, and Applicationkey is required as well.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>:vartype identity: ~azure.mgmt.datadog.models.IdentityProperties</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state. Known values are: "Provisioning", "Active", "Suspended", and "Unsubscribed".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying if the resource monitoring is enabled or disabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>:vartype sku: ~azure.mgmt.datadog.models.ResourceSku</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of .</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>Includes name, email and optionally, phone number. User Information can't be null.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a specific monitor resource. Get the properties of a specific monitor resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all monitors under the specified resource group. List all monitors under the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all monitors under the specified subscription. List all monitors under the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a monitor resource. Create a monitor resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a monitor resource. Update a monitor resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a monitor resource. Delete a monitor resource.</td>
</tr>
<tr>
    <td><a href="#list_api_keys"><CopyableCode code="list_api_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the api keys for a given monitor resource. List the api keys for a given monitor resource.</td>
</tr>
<tr>
    <td><a href="#list_hosts"><CopyableCode code="list_hosts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the hosts for a given monitor resource. List the hosts for a given monitor resource.</td>
</tr>
<tr>
    <td><a href="#list_linked_resources"><CopyableCode code="list_linked_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Azure resources associated to the same Datadog organization as the target resource. List all Azure resources associated to the same Datadog organization as the target resource.</td>
</tr>
<tr>
    <td><a href="#list_monitored_resources"><CopyableCode code="list_monitored_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the resources currently being monitored by the Datadog monitor resource. List the resources currently being monitored by the Datadog monitor resource.</td>
</tr>
<tr>
    <td><a href="#get_default_key"><CopyableCode code="get_default_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the default api key. Get the default api key.</td>
</tr>
<tr>
    <td><a href="#set_default_key"><CopyableCode code="set_default_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-key"><code>key</code></a></td>
    <td></td>
    <td>Set the default api key. Set the default api key.</td>
</tr>
<tr>
    <td><a href="#refresh_set_password_link"><CopyableCode code="refresh_set_password_link" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refresh the set password link and return a latest one. Refresh the set password link and return a latest one.</td>
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
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Monitor resource name. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the properties of a specific monitor resource. Get the properties of a specific monitor resource.

```sql
SELECT
id,
name,
datadogOrganizationProperties,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionStatus,
monitoringStatus,
provisioningState,
sku,
systemData,
tags,
type,
userInfo
FROM azure_isv.datadog.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all monitors under the specified resource group. List all monitors under the specified resource group.

```sql
SELECT
id,
name,
datadogOrganizationProperties,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionStatus,
monitoringStatus,
provisioningState,
sku,
systemData,
tags,
type,
userInfo
FROM azure_isv.datadog.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all monitors under the specified subscription. List all monitors under the specified subscription.

```sql
SELECT
id,
name,
datadogOrganizationProperties,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionStatus,
monitoringStatus,
provisioningState,
sku,
systemData,
tags,
type,
userInfo
FROM azure_isv.datadog.monitors
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a monitor resource. Create a monitor resource.

```sql
INSERT INTO azure_isv.datadog.monitors (
sku,
properties,
identity,
tags,
location,
resource_group_name,
monitor_name,
subscription_id
)
SELECT 
'{{ sku }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}' /* required */,
'{{ resource_group_name }}',
'{{ monitor_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: monitors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the monitors resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the monitors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the monitors resource.
    - name: sku
      description: |
        :vartype sku: ~azure.mgmt.datadog.models.ResourceSku
      value:
        name: "{{ name }}"
    - name: properties
      description: |
        Properties specific to the monitor resource.
      value:
        provisioningState: "{{ provisioningState }}"
        monitoringStatus: "{{ monitoringStatus }}"
        marketplaceSubscriptionStatus: "{{ marketplaceSubscriptionStatus }}"
        datadogOrganizationProperties:
          name: "{{ name }}"
          id: "{{ id }}"
          linkingAuthCode: "{{ linkingAuthCode }}"
          linkingClientId: "{{ linkingClientId }}"
          redirectUri: "{{ redirectUri }}"
          apiKey: "{{ apiKey }}"
          applicationKey: "{{ applicationKey }}"
          enterpriseAppId: "{{ enterpriseAppId }}"
          cspm: {{ cspm }}
        userInfo:
          name: "{{ name }}"
          emailAddress: "{{ emailAddress }}"
          phoneNumber: "{{ phoneNumber }}"
        liftrResourceCategory: "{{ liftrResourceCategory }}"
        liftrResourcePreference: {{ liftrResourcePreference }}
    - name: identity
      description: |
        :vartype identity: ~azure.mgmt.datadog.models.IdentityProperties
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Dictionary of .
    - name: location
      value: "{{ location }}"
      description: |
        Required.
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

Update a monitor resource. Update a monitor resource.

```sql
UPDATE azure_isv.datadog.monitors
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Delete a monitor resource. Delete a monitor resource.

```sql
DELETE FROM azure_isv.datadog.monitors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_api_keys"
    values={[
        { label: 'list_api_keys', value: 'list_api_keys' },
        { label: 'list_hosts', value: 'list_hosts' },
        { label: 'list_linked_resources', value: 'list_linked_resources' },
        { label: 'list_monitored_resources', value: 'list_monitored_resources' },
        { label: 'get_default_key', value: 'get_default_key' },
        { label: 'set_default_key', value: 'set_default_key' },
        { label: 'refresh_set_password_link', value: 'refresh_set_password_link' }
    ]}
>
<TabItem value="list_api_keys">

List the api keys for a given monitor resource. List the api keys for a given monitor resource.

```sql
EXEC azure_isv.datadog.monitors.list_api_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_hosts">

List the hosts for a given monitor resource. List the hosts for a given monitor resource.

```sql
EXEC azure_isv.datadog.monitors.list_hosts 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_linked_resources">

List all Azure resources associated to the same Datadog organization as the target resource. List all Azure resources associated to the same Datadog organization as the target resource.

```sql
EXEC azure_isv.datadog.monitors.list_linked_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_monitored_resources">

List the resources currently being monitored by the Datadog monitor resource. List the resources currently being monitored by the Datadog monitor resource.

```sql
EXEC azure_isv.datadog.monitors.list_monitored_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_default_key">

Get the default api key. Get the default api key.

```sql
EXEC azure_isv.datadog.monitors.get_default_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_default_key">

Set the default api key. Set the default api key.

```sql
EXEC azure_isv.datadog.monitors.set_default_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"createdBy": "{{ createdBy }}", 
"name": "{{ name }}", 
"key": "{{ key }}", 
"created": "{{ created }}"
}'
;
```
</TabItem>
<TabItem value="refresh_set_password_link">

Refresh the set password link and return a latest one. Refresh the set password link and return a latest one.

```sql
EXEC azure_isv.datadog.monitors.refresh_set_password_link 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
