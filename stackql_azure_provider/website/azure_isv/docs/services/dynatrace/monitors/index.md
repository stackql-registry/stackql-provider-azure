--- 
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - dynatrace
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
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
    <td><CopyableCode code="dynatraceEnvironmentProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of the Dynatrace environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Liftr Resource category. Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Marketplace subscription status. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the monitor. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Billing plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System metadata for this resource.</td>
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
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User info.</td>
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
    <td><CopyableCode code="dynatraceEnvironmentProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of the Dynatrace environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Liftr Resource category. Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Marketplace subscription status. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the monitor. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Billing plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System metadata for this resource.</td>
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
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User info.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription_id">

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
    <td><CopyableCode code="dynatraceEnvironmentProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of the Dynatrace environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourceCategory" /></td>
    <td><code>string</code></td>
    <td>Liftr Resource category. Known values are: "Unknown" and "MonitorLogs".</td>
</tr>
<tr>
    <td><CopyableCode code="liftrResourcePreference" /></td>
    <td><code>integer</code></td>
    <td>The priority of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Marketplace subscription status. Known values are: "Active" and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the monitor. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="planData" /></td>
    <td><code>object</code></td>
    <td>Billing plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System metadata for this resource.</td>
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
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User info.</td>
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
    <td>Get a MonitorResource. Get a MonitorResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List MonitorResource resources by resource group. List MonitorResource resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription_id"><CopyableCode code="list_by_subscription_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all MonitorResource by subscriptionId. List all MonitorResource by subscriptionId.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a MonitorResource. Create a MonitorResource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a MonitorResource. Update a MonitorResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a MonitorResource. Create a MonitorResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a MonitorResource. Delete a MonitorResource.</td>
</tr>
<tr>
    <td><a href="#list_monitored_resources"><CopyableCode code="list_monitored_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the resources currently being monitored by the Dynatrace monitor resource. List the resources currently being monitored by the Dynatrace monitor resource.</td>
</tr>
<tr>
    <td><a href="#list_hosts"><CopyableCode code="list_hosts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the VM/VMSS resources currently being monitored by the Dynatrace resource. List the VM/VMSS resources currently being monitored by the Dynatrace resource.</td>
</tr>
<tr>
    <td><a href="#list_app_services"><CopyableCode code="list_app_services" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets list of App Services with Dynatrace PaaS OneAgent enabled. Gets list of App Services with Dynatrace PaaS OneAgent enabled.</td>
</tr>
<tr>
    <td><a href="#list_linkable_environments"><CopyableCode code="list_linkable_environments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-tenantId"><code>tenantId</code></a>, <a href="#parameter-userPrincipal"><code>userPrincipal</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td></td>
    <td>Gets all the Dynatrace environments that a user can link a azure resource to. Gets all the Dynatrace environments that a user can link a azure resource to.</td>
</tr>
<tr>
    <td><a href="#get_vm_host_payload"><CopyableCode code="get_vm_host_payload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the payload that needs to be passed in the request body for installing Dynatrace agent on a VM. Returns the payload that needs to be passed in the request body for installing Dynatrace agent on a VM.</td>
</tr>
<tr>
    <td><a href="#get_marketplace_saa_s_resource_details"><CopyableCode code="get_marketplace_saa_s_resource_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-tenantId"><code>tenantId</code></a></td>
    <td></td>
    <td>Get Marketplace SaaS resource details of a tenant under a specific subscription.</td>
</tr>
<tr>
    <td><a href="#get_metric_status"><CopyableCode code="get_metric_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get metric status.</td>
</tr>
<tr>
    <td><a href="#get_sso_details"><CopyableCode code="get_sso_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-userPrincipal"><code>userPrincipal</code></a></td>
    <td></td>
    <td>Gets the SSO configuration details from the partner. Gets the SSO configuration details from the partner.</td>
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
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
    ]}
>
<TabItem value="get">

Get a MonitorResource. Get a MonitorResource.

```sql
SELECT
id,
name,
dynatraceEnvironmentProperties,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionStatus,
monitoringStatus,
planData,
provisioningState,
systemData,
tags,
type,
userInfo
FROM azure_isv.dynatrace.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List MonitorResource resources by resource group. List MonitorResource resources by resource group.

```sql
SELECT
id,
name,
dynatraceEnvironmentProperties,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionStatus,
monitoringStatus,
planData,
provisioningState,
systemData,
tags,
type,
userInfo
FROM azure_isv.dynatrace.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription_id">

List all MonitorResource by subscriptionId. List all MonitorResource by subscriptionId.

```sql
SELECT
id,
name,
dynatraceEnvironmentProperties,
identity,
liftrResourceCategory,
liftrResourcePreference,
location,
marketplaceSubscriptionStatus,
monitoringStatus,
planData,
provisioningState,
systemData,
tags,
type,
userInfo
FROM azure_isv.dynatrace.monitors
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

Create a MonitorResource. Create a MonitorResource.

```sql
INSERT INTO azure_isv.dynatrace.monitors (
tags,
location,
identity,
properties,
resource_group_name,
monitor_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
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
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        monitoringStatus: "{{ monitoringStatus }}"
        marketplaceSubscriptionStatus: "{{ marketplaceSubscriptionStatus }}"
        dynatraceEnvironmentProperties:
          userId: "{{ userId }}"
          accountInfo:
            accountId: "{{ accountId }}"
            regionId: "{{ regionId }}"
          environmentInfo:
            environmentId: "{{ environmentId }}"
            ingestionKey: "{{ ingestionKey }}"
            logsIngestionEndpoint: "{{ logsIngestionEndpoint }}"
            landingURL: "{{ landingURL }}"
          singleSignOnProperties:
            singleSignOnState: "{{ singleSignOnState }}"
            enterpriseAppId: "{{ enterpriseAppId }}"
            singleSignOnUrl: "{{ singleSignOnUrl }}"
            aadDomains:
              - "{{ aadDomains }}"
            provisioningState: "{{ provisioningState }}"
        userInfo:
          firstName: "{{ firstName }}"
          lastName: "{{ lastName }}"
          emailAddress: "{{ emailAddress }}"
          phoneNumber: "{{ phoneNumber }}"
          country: "{{ country }}"
        planData:
          usageType: "{{ usageType }}"
          billingCycle: "{{ billingCycle }}"
          planDetails: "{{ planDetails }}"
          effectiveDate: "{{ effectiveDate }}"
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

Update a MonitorResource. Update a MonitorResource.

```sql
UPDATE azure_isv.dynatrace.monitors
SET 
tags = '{{ tags }}'
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

Create a MonitorResource. Create a MonitorResource.

```sql
REPLACE azure_isv.dynatrace.monitors
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
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

Delete a MonitorResource. Delete a MonitorResource.

```sql
DELETE FROM azure_isv.dynatrace.monitors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_monitored_resources"
    values={[
        { label: 'list_monitored_resources', value: 'list_monitored_resources' },
        { label: 'list_hosts', value: 'list_hosts' },
        { label: 'list_app_services', value: 'list_app_services' },
        { label: 'list_linkable_environments', value: 'list_linkable_environments' },
        { label: 'get_vm_host_payload', value: 'get_vm_host_payload' },
        { label: 'get_marketplace_saa_s_resource_details', value: 'get_marketplace_saa_s_resource_details' },
        { label: 'get_metric_status', value: 'get_metric_status' },
        { label: 'get_sso_details', value: 'get_sso_details' }
    ]}
>
<TabItem value="list_monitored_resources">

List the resources currently being monitored by the Dynatrace monitor resource. List the resources currently being monitored by the Dynatrace monitor resource.

```sql
EXEC azure_isv.dynatrace.monitors.list_monitored_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_hosts">

List the VM/VMSS resources currently being monitored by the Dynatrace resource. List the VM/VMSS resources currently being monitored by the Dynatrace resource.

```sql
EXEC azure_isv.dynatrace.monitors.list_hosts 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_app_services">

Gets list of App Services with Dynatrace PaaS OneAgent enabled. Gets list of App Services with Dynatrace PaaS OneAgent enabled.

```sql
EXEC azure_isv.dynatrace.monitors.list_app_services 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_linkable_environments">

Gets all the Dynatrace environments that a user can link a azure resource to. Gets all the Dynatrace environments that a user can link a azure resource to.

```sql
EXEC azure_isv.dynatrace.monitors.list_linkable_environments 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tenantId": "{{ tenantId }}", 
"userPrincipal": "{{ userPrincipal }}", 
"region": "{{ region }}"
}'
;
```
</TabItem>
<TabItem value="get_vm_host_payload">

Returns the payload that needs to be passed in the request body for installing Dynatrace agent on a VM. Returns the payload that needs to be passed in the request body for installing Dynatrace agent on a VM.

```sql
EXEC azure_isv.dynatrace.monitors.get_vm_host_payload 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_marketplace_saa_s_resource_details">

Get Marketplace SaaS resource details of a tenant under a specific subscription.

```sql
EXEC azure_isv.dynatrace.monitors.get_marketplace_saa_s_resource_details 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tenantId": "{{ tenantId }}"
}'
;
```
</TabItem>
<TabItem value="get_metric_status">

Get metric status.

```sql
EXEC azure_isv.dynatrace.monitors.get_metric_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_sso_details">

Gets the SSO configuration details from the partner. Gets the SSO configuration details from the partner.

```sql
EXEC azure_isv.dynatrace.monitors.get_sso_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"userPrincipal": "{{ userPrincipal }}"
}'
;
```
</TabItem>
</Tabs>
