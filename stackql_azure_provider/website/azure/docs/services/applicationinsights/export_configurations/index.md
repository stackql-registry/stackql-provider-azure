--- 
title: export_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - export_configurations
  - applicationinsights
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

Creates, updates, deletes, gets or lists an <code>export_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="export_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.export_configurations" /></td></tr>
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
    <td><CopyableCode code="ApplicationName" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="ContainerName" /></td>
    <td><code>string</code></td>
    <td>The name of the destination storage container.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationAccountId" /></td>
    <td><code>string</code></td>
    <td>The name of destination account.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationStorageLocationId" /></td>
    <td><code>string</code></td>
    <td>The destination account location ID.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationStorageSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The destination storage account subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationType" /></td>
    <td><code>string</code></td>
    <td>The destination type.</td>
</tr>
<tr>
    <td><CopyableCode code="ExportId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the export configuration inside an Application Insights component. It is auto generated when the Continuous Export configuration is created.</td>
</tr>
<tr>
    <td><CopyableCode code="ExportStatus" /></td>
    <td><code>string</code></td>
    <td>This indicates current Continuous Export configuration status. The possible values are 'Preparing', 'Success', 'Failure'.</td>
</tr>
<tr>
    <td><CopyableCode code="InstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>The instrumentation key of the Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="IsUserEnabled" /></td>
    <td><code>string</code></td>
    <td>This will be 'true' if the Continuous Export configuration is enabled, otherwise it will be 'false'.</td>
</tr>
<tr>
    <td><CopyableCode code="LastGapTime" /></td>
    <td><code>string</code></td>
    <td>The last time the Continuous Export configuration started failing.</td>
</tr>
<tr>
    <td><CopyableCode code="LastSuccessTime" /></td>
    <td><code>string</code></td>
    <td>The last time data was successfully delivered to the destination storage container for this Continuous Export configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="LastUserUpdate" /></td>
    <td><code>string</code></td>
    <td>Last time the Continuous Export configuration was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="NotificationQueueEnabled" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="PermanentErrorReason" /></td>
    <td><code>string</code></td>
    <td>This is the reason the Continuous Export configuration started failing. It can be 'AzureStorageNotFound' or 'AzureStorageAccessDenied'.</td>
</tr>
<tr>
    <td><CopyableCode code="RecordTypes" /></td>
    <td><code>string</code></td>
    <td>This comma separated list of document types that will be exported. The possible values include 'Requests', 'Event', 'Exceptions', 'Metrics', 'PageViews', 'PageViewPerformance', 'Rdd', 'PerformanceCounters', 'Availability', 'Messages'.</td>
</tr>
<tr>
    <td><CopyableCode code="ResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="StorageName" /></td>
    <td><code>string</code></td>
    <td>The name of the destination storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="SubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscription of the Application Insights component.</td>
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
    <td><CopyableCode code="ApplicationName" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="ContainerName" /></td>
    <td><code>string</code></td>
    <td>The name of the destination storage container.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationAccountId" /></td>
    <td><code>string</code></td>
    <td>The name of destination account.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationStorageLocationId" /></td>
    <td><code>string</code></td>
    <td>The destination account location ID.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationStorageSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The destination storage account subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="DestinationType" /></td>
    <td><code>string</code></td>
    <td>The destination type.</td>
</tr>
<tr>
    <td><CopyableCode code="ExportId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the export configuration inside an Application Insights component. It is auto generated when the Continuous Export configuration is created.</td>
</tr>
<tr>
    <td><CopyableCode code="ExportStatus" /></td>
    <td><code>string</code></td>
    <td>This indicates current Continuous Export configuration status. The possible values are 'Preparing', 'Success', 'Failure'.</td>
</tr>
<tr>
    <td><CopyableCode code="InstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>The instrumentation key of the Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="IsUserEnabled" /></td>
    <td><code>string</code></td>
    <td>This will be 'true' if the Continuous Export configuration is enabled, otherwise it will be 'false'.</td>
</tr>
<tr>
    <td><CopyableCode code="LastGapTime" /></td>
    <td><code>string</code></td>
    <td>The last time the Continuous Export configuration started failing.</td>
</tr>
<tr>
    <td><CopyableCode code="LastSuccessTime" /></td>
    <td><code>string</code></td>
    <td>The last time data was successfully delivered to the destination storage container for this Continuous Export configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="LastUserUpdate" /></td>
    <td><code>string</code></td>
    <td>Last time the Continuous Export configuration was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="NotificationQueueEnabled" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="PermanentErrorReason" /></td>
    <td><code>string</code></td>
    <td>This is the reason the Continuous Export configuration started failing. It can be 'AzureStorageNotFound' or 'AzureStorageAccessDenied'.</td>
</tr>
<tr>
    <td><CopyableCode code="RecordTypes" /></td>
    <td><code>string</code></td>
    <td>This comma separated list of document types that will be exported. The possible values include 'Requests', 'Event', 'Exceptions', 'Metrics', 'PageViews', 'PageViewPerformance', 'Rdd', 'PerformanceCounters', 'Availability', 'Messages'.</td>
</tr>
<tr>
    <td><CopyableCode code="ResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="StorageName" /></td>
    <td><code>string</code></td>
    <td>The name of the destination storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="SubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscription of the Application Insights component.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-export_id"><code>export_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Continuous Export configuration for this export id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Continuous Export configuration of an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Continuous Export configuration of an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-export_id"><code>export_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the Continuous Export configuration for this export id.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-export_id"><code>export_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Continuous Export configuration of an Application Insights component.</td>
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
<tr id="parameter-export_id">
    <td><CopyableCode code="export_id" /></td>
    <td><code>string</code></td>
    <td>The Continuous Export configuration ID. This is unique within a Application Insights component. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component resource. Required.</td>
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

Get the Continuous Export configuration for this export id.

```sql
SELECT
ApplicationName,
ContainerName,
DestinationAccountId,
DestinationStorageLocationId,
DestinationStorageSubscriptionId,
DestinationType,
ExportId,
ExportStatus,
InstrumentationKey,
IsUserEnabled,
LastGapTime,
LastSuccessTime,
LastUserUpdate,
NotificationQueueEnabled,
PermanentErrorReason,
RecordTypes,
ResourceGroup,
StorageName,
SubscriptionId
FROM azure.applicationinsights.export_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND export_id = '{{ export_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of Continuous Export configuration of an Application Insights component.

```sql
SELECT
ApplicationName,
ContainerName,
DestinationAccountId,
DestinationStorageLocationId,
DestinationStorageSubscriptionId,
DestinationType,
ExportId,
ExportStatus,
InstrumentationKey,
IsUserEnabled,
LastGapTime,
LastSuccessTime,
LastUserUpdate,
NotificationQueueEnabled,
PermanentErrorReason,
RecordTypes,
ResourceGroup,
StorageName,
SubscriptionId
FROM azure.applicationinsights.export_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Create a Continuous Export configuration of an Application Insights component.

```sql
INSERT INTO azure.applicationinsights.export_configurations (
RecordTypes,
DestinationType,
DestinationAddress,
IsEnabled,
NotificationQueueEnabled,
NotificationQueueUri,
DestinationStorageSubscriptionId,
DestinationStorageLocationId,
DestinationAccountId,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ RecordTypes }}',
'{{ DestinationType }}',
'{{ DestinationAddress }}',
'{{ IsEnabled }}',
'{{ NotificationQueueEnabled }}',
'{{ NotificationQueueUri }}',
'{{ DestinationStorageSubscriptionId }}',
'{{ DestinationStorageLocationId }}',
'{{ DestinationAccountId }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
ApplicationName,
ContainerName,
DestinationAccountId,
DestinationStorageLocationId,
DestinationStorageSubscriptionId,
DestinationType,
ExportId,
ExportStatus,
InstrumentationKey,
IsUserEnabled,
LastGapTime,
LastSuccessTime,
LastUserUpdate,
NotificationQueueEnabled,
PermanentErrorReason,
RecordTypes,
ResourceGroup,
StorageName,
SubscriptionId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: export_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the export_configurations resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the export_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the export_configurations resource.
    - name: RecordTypes
      value: "{{ RecordTypes }}"
      description: |
        The document types to be exported, as comma separated values. Allowed values include 'Requests', 'Event', 'Exceptions', 'Metrics', 'PageViews', 'PageViewPerformance', 'Rdd', 'PerformanceCounters', 'Availability', 'Messages'.
    - name: DestinationType
      value: "{{ DestinationType }}"
      description: |
        The Continuous Export destination type. This has to be 'Blob'.
    - name: DestinationAddress
      value: "{{ DestinationAddress }}"
      description: |
        The SAS URL for the destination storage container. It must grant write permission.
    - name: IsEnabled
      value: "{{ IsEnabled }}"
      description: |
        Set to 'true' to create a Continuous Export configuration as enabled, otherwise set it to 'false'.
    - name: NotificationQueueEnabled
      value: "{{ NotificationQueueEnabled }}"
      description: |
        Deprecated.
    - name: NotificationQueueUri
      value: "{{ NotificationQueueUri }}"
      description: |
        Deprecated.
    - name: DestinationStorageSubscriptionId
      value: "{{ DestinationStorageSubscriptionId }}"
      description: |
        The subscription ID of the destination storage container.
    - name: DestinationStorageLocationId
      value: "{{ DestinationStorageLocationId }}"
      description: |
        The location ID of the destination storage container.
    - name: DestinationAccountId
      value: "{{ DestinationAccountId }}"
      description: |
        The name of destination storage account.
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

Update the Continuous Export configuration for this export id.

```sql
UPDATE azure.applicationinsights.export_configurations
SET 
RecordTypes = '{{ RecordTypes }}',
DestinationType = '{{ DestinationType }}',
DestinationAddress = '{{ DestinationAddress }}',
IsEnabled = '{{ IsEnabled }}',
NotificationQueueEnabled = '{{ NotificationQueueEnabled }}',
NotificationQueueUri = '{{ NotificationQueueUri }}',
DestinationStorageSubscriptionId = '{{ DestinationStorageSubscriptionId }}',
DestinationStorageLocationId = '{{ DestinationStorageLocationId }}',
DestinationAccountId = '{{ DestinationAccountId }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND export_id = '{{ export_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
ApplicationName,
ContainerName,
DestinationAccountId,
DestinationStorageLocationId,
DestinationStorageSubscriptionId,
DestinationType,
ExportId,
ExportStatus,
InstrumentationKey,
IsUserEnabled,
LastGapTime,
LastSuccessTime,
LastUserUpdate,
NotificationQueueEnabled,
PermanentErrorReason,
RecordTypes,
ResourceGroup,
StorageName,
SubscriptionId;
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

Delete a Continuous Export configuration of an Application Insights component.

```sql
DELETE FROM azure.applicationinsights.export_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND export_id = '{{ export_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
