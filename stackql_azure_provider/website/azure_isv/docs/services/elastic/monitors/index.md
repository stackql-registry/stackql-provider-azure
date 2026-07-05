--- 
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - elastic
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.monitors" /></td></tr>
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
    <td><CopyableCode code="elasticProperties" /></td>
    <td><code>object</code></td>
    <td>Elastic cloud properties.</td>
</tr>
<tr>
    <td><CopyableCode code="generateApiKey" /></td>
    <td><code>boolean</code></td>
    <td>Flag to determine if User API Key has to be generated and shared.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingType" /></td>
    <td><code>string</code></td>
    <td>Hosting type of the monitor resource - either Hosted deployments OR Serverless Projects. Known values are: "Hosted" and "Serverless".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity properties of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the Elastic resource - observability, security, search etc.</td>
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
    <td>The location of the monitor resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying if the resource monitoring is enabled or disabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="planDetails" /></td>
    <td><code>object</code></td>
    <td>Plan details of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="projectDetails" /></td>
    <td><code>object</code></td>
    <td>Project details of the monitor resource IF it belongs to Serverless offer kind.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the monitor resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="saaSAzureSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Subscription where Marketplace SaaS is located.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCampaignId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier associated with the campaign.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCampaignName" /></td>
    <td><code>string</code></td>
    <td>Name of the marketing campaign.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure Subscription containing the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User information.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of elastic of the monitor resource.</td>
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
    <td><CopyableCode code="elasticProperties" /></td>
    <td><code>object</code></td>
    <td>Elastic cloud properties.</td>
</tr>
<tr>
    <td><CopyableCode code="generateApiKey" /></td>
    <td><code>boolean</code></td>
    <td>Flag to determine if User API Key has to be generated and shared.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingType" /></td>
    <td><code>string</code></td>
    <td>Hosting type of the monitor resource - either Hosted deployments OR Serverless Projects. Known values are: "Hosted" and "Serverless".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity properties of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the Elastic resource - observability, security, search etc.</td>
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
    <td>The location of the monitor resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying if the resource monitoring is enabled or disabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="planDetails" /></td>
    <td><code>object</code></td>
    <td>Plan details of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="projectDetails" /></td>
    <td><code>object</code></td>
    <td>Project details of the monitor resource IF it belongs to Serverless offer kind.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the monitor resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="saaSAzureSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Subscription where Marketplace SaaS is located.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCampaignId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier associated with the campaign.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCampaignName" /></td>
    <td><code>string</code></td>
    <td>Name of the marketing campaign.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure Subscription containing the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User information.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of elastic of the monitor resource.</td>
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
    <td><CopyableCode code="elasticProperties" /></td>
    <td><code>object</code></td>
    <td>Elastic cloud properties.</td>
</tr>
<tr>
    <td><CopyableCode code="generateApiKey" /></td>
    <td><code>boolean</code></td>
    <td>Flag to determine if User API Key has to be generated and shared.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingType" /></td>
    <td><code>string</code></td>
    <td>Hosting type of the monitor resource - either Hosted deployments OR Serverless Projects. Known values are: "Hosted" and "Serverless".</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity properties of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the Elastic resource - observability, security, search etc.</td>
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
    <td>The location of the monitor resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>Flag specifying if the resource monitoring is enabled or disabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="planDetails" /></td>
    <td><code>object</code></td>
    <td>Plan details of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="projectDetails" /></td>
    <td><code>object</code></td>
    <td>Project details of the monitor resource IF it belongs to Serverless offer kind.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the monitor resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="saaSAzureSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Azure Subscription where Marketplace SaaS is located.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCampaignId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier associated with the campaign.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCampaignName" /></td>
    <td><code>string</code></td>
    <td>Name of the marketing campaign.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionState" /></td>
    <td><code>string</code></td>
    <td>State of the Azure Subscription containing the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userInfo" /></td>
    <td><code>object</code></td>
    <td>User information.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of elastic of the monitor resource.</td>
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
    <td>Get detailed properties of a specific Elastic monitor resource, helping you manage observability and performance. Get detailed properties of a specific Elastic monitor resource, helping you manage observability and performance.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Elastic monitor resources within a specified resource group of the subscription, helping you audit and manage your monitoring setup. List all Elastic monitor resources within a specified resource group of the subscription, helping you audit and manage your monitoring setup.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Elastic monitor resources within a specified subscription, helping you audit and manage your monitoring setup. List all Elastic monitor resources within a specified subscription, helping you audit and manage your monitoring setup.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a new Elastic monitor resource in your Azure subscription, enabling observability and monitoring of your Azure resources through Elastic. Create a new Elastic monitor resource in your Azure subscription, enabling observability and monitoring of your Azure resources through Elastic.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing Elastic monitor resource in your Azure subscription, ensuring optimal observability and performance. Update an existing Elastic monitor resource in your Azure subscription, ensuring optimal observability and performance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an existing Elastic monitor resource from your Azure subscription, removing its observability and monitoring capabilities. Delete an existing Elastic monitor resource from your Azure subscription, removing its observability and monitoring capabilities.</td>
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

Get detailed properties of a specific Elastic monitor resource, helping you manage observability and performance. Get detailed properties of a specific Elastic monitor resource, helping you manage observability and performance.

```sql
SELECT
id,
name,
elasticProperties,
generateApiKey,
hostingType,
identity,
kind,
liftrResourceCategory,
liftrResourcePreference,
location,
monitoringStatus,
planDetails,
projectDetails,
provisioningState,
saaSAzureSubscriptionStatus,
sku,
sourceCampaignId,
sourceCampaignName,
subscriptionState,
systemData,
tags,
type,
userInfo,
version
FROM azure_isv.elastic.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all Elastic monitor resources within a specified resource group of the subscription, helping you audit and manage your monitoring setup. List all Elastic monitor resources within a specified resource group of the subscription, helping you audit and manage your monitoring setup.

```sql
SELECT
id,
name,
elasticProperties,
generateApiKey,
hostingType,
identity,
kind,
liftrResourceCategory,
liftrResourcePreference,
location,
monitoringStatus,
planDetails,
projectDetails,
provisioningState,
saaSAzureSubscriptionStatus,
sku,
sourceCampaignId,
sourceCampaignName,
subscriptionState,
systemData,
tags,
type,
userInfo,
version
FROM azure_isv.elastic.monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Elastic monitor resources within a specified subscription, helping you audit and manage your monitoring setup. List all Elastic monitor resources within a specified subscription, helping you audit and manage your monitoring setup.

```sql
SELECT
id,
name,
elasticProperties,
generateApiKey,
hostingType,
identity,
kind,
liftrResourceCategory,
liftrResourcePreference,
location,
monitoringStatus,
planDetails,
projectDetails,
provisioningState,
saaSAzureSubscriptionStatus,
sku,
sourceCampaignId,
sourceCampaignName,
subscriptionState,
systemData,
tags,
type,
userInfo,
version
FROM azure_isv.elastic.monitors
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

Create a new Elastic monitor resource in your Azure subscription, enabling observability and monitoring of your Azure resources through Elastic. Create a new Elastic monitor resource in your Azure subscription, enabling observability and monitoring of your Azure resources through Elastic.

```sql
INSERT INTO azure_isv.elastic.monitors (
kind,
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
'{{ kind }}',
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
kind,
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
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the Elastic resource - observability, security, search etc.
    - name: sku
      description: |
        SKU of the monitor resource.
      value:
        name: "{{ name }}"
    - name: properties
      description: |
        Properties of the monitor resource.
      value:
        provisioningState: "{{ provisioningState }}"
        monitoringStatus: "{{ monitoringStatus }}"
        elasticProperties:
          elasticCloudUser:
            emailAddress: "{{ emailAddress }}"
            id: "{{ id }}"
            elasticCloudSsoDefaultUrl: "{{ elasticCloudSsoDefaultUrl }}"
          elasticCloudDeployment:
            name: "{{ name }}"
            deploymentId: "{{ deploymentId }}"
            azureSubscriptionId: "{{ azureSubscriptionId }}"
            elasticsearchRegion: "{{ elasticsearchRegion }}"
            elasticsearchServiceUrl: "{{ elasticsearchServiceUrl }}"
            kibanaServiceUrl: "{{ kibanaServiceUrl }}"
            kibanaSsoUrl: "{{ kibanaSsoUrl }}"
        userInfo:
          firstName: "{{ firstName }}"
          lastName: "{{ lastName }}"
          companyName: "{{ companyName }}"
          emailAddress: "{{ emailAddress }}"
          companyInfo:
            domain: "{{ domain }}"
            business: "{{ business }}"
            employeesNumber: "{{ employeesNumber }}"
            state: "{{ state }}"
            country: "{{ country }}"
        planDetails:
          offerID: "{{ offerID }}"
          publisherID: "{{ publisherID }}"
          termID: "{{ termID }}"
          planID: "{{ planID }}"
          planName: "{{ planName }}"
        version: "{{ version }}"
        subscriptionState: "{{ subscriptionState }}"
        saaSAzureSubscriptionStatus: "{{ saaSAzureSubscriptionStatus }}"
        sourceCampaignName: "{{ sourceCampaignName }}"
        sourceCampaignId: "{{ sourceCampaignId }}"
        liftrResourceCategory: "{{ liftrResourceCategory }}"
        liftrResourcePreference: {{ liftrResourcePreference }}
        generateApiKey: {{ generateApiKey }}
        hostingType: "{{ hostingType }}"
        projectDetails:
          projectType: "{{ projectType }}"
          configurationType: "{{ configurationType }}"
    - name: identity
      description: |
        Identity properties of the monitor resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags of the monitor resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location of the monitor resource. Required.
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

Update an existing Elastic monitor resource in your Azure subscription, ensuring optimal observability and performance. Update an existing Elastic monitor resource in your Azure subscription, ensuring optimal observability and performance.

```sql
UPDATE azure_isv.elastic.monitors
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
kind,
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

Delete an existing Elastic monitor resource from your Azure subscription, removing its observability and monitoring capabilities. Delete an existing Elastic monitor resource from your Azure subscription, removing its observability and monitoring capabilities.

```sql
DELETE FROM azure_isv.elastic.monitors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
