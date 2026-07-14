--- 
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>data_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_sources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.data_sources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the data source.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the DataSource. Required. Known values are: "WindowsEvent", "WindowsPerformanceCounter", "IISLogs", "LinuxSyslog", "LinuxSyslogCollection", "LinuxPerformanceObject", "LinuxPerformanceCollection", "CustomLog", "CustomLogCollection", "AzureAuditLog", "AzureActivityLog", "GenericDataSource", "ChangeTrackingCustomPath", "ChangeTrackingPath", "ChangeTrackingServices", "ChangeTrackingDataTypeConfiguration", "ChangeTrackingDefaultRegistry", "ChangeTrackingRegistry", "ChangeTrackingLinuxPath", "LinuxChangeTrackingPath", "ChangeTrackingContentLocation", "WindowsTelemetry", "Office365", "SecurityWindowsBaselineConfiguration", "SecurityCenterSecurityWindowsBaselineConfiguration", "SecurityEventCollectionConfiguration", "SecurityInsightsSecurityEventCollectionConfiguration", "ImportComputerGroup", "NetworkMonitoring", "Itsm", "DnsAnalytics", "ApplicationInsights", and "SqlDataClassification". (WindowsEvent, WindowsPerformanceCounter, IISLogs, LinuxSyslog, LinuxSyslogCollection, LinuxPerformanceObject, LinuxPerformanceCollection, CustomLog, CustomLogCollection, AzureAuditLog, AzureActivityLog, GenericDataSource, ChangeTrackingCustomPath, ChangeTrackingPath, ChangeTrackingServices, ChangeTrackingDataTypeConfiguration, ChangeTrackingDefaultRegistry, ChangeTrackingRegistry, ChangeTrackingLinuxPath, LinuxChangeTrackingPath, ChangeTrackingContentLocation, WindowsTelemetry, Office365, SecurityWindowsBaselineConfiguration, SecurityCenterSecurityWindowsBaselineConfiguration, SecurityEventCollectionConfiguration, SecurityInsightsSecurityEventCollectionConfiguration, ImportComputerGroup, NetworkMonitoring, Itsm, DnsAnalytics, ApplicationInsights, SqlDataClassification)</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The data source properties in raw json format, each kind of data source have it's own schema. Required.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the data source.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the DataSource. Required. Known values are: "WindowsEvent", "WindowsPerformanceCounter", "IISLogs", "LinuxSyslog", "LinuxSyslogCollection", "LinuxPerformanceObject", "LinuxPerformanceCollection", "CustomLog", "CustomLogCollection", "AzureAuditLog", "AzureActivityLog", "GenericDataSource", "ChangeTrackingCustomPath", "ChangeTrackingPath", "ChangeTrackingServices", "ChangeTrackingDataTypeConfiguration", "ChangeTrackingDefaultRegistry", "ChangeTrackingRegistry", "ChangeTrackingLinuxPath", "LinuxChangeTrackingPath", "ChangeTrackingContentLocation", "WindowsTelemetry", "Office365", "SecurityWindowsBaselineConfiguration", "SecurityCenterSecurityWindowsBaselineConfiguration", "SecurityEventCollectionConfiguration", "SecurityInsightsSecurityEventCollectionConfiguration", "ImportComputerGroup", "NetworkMonitoring", "Itsm", "DnsAnalytics", "ApplicationInsights", and "SqlDataClassification". (WindowsEvent, WindowsPerformanceCounter, IISLogs, LinuxSyslog, LinuxSyslogCollection, LinuxPerformanceObject, LinuxPerformanceCollection, CustomLog, CustomLogCollection, AzureAuditLog, AzureActivityLog, GenericDataSource, ChangeTrackingCustomPath, ChangeTrackingPath, ChangeTrackingServices, ChangeTrackingDataTypeConfiguration, ChangeTrackingDefaultRegistry, ChangeTrackingRegistry, ChangeTrackingLinuxPath, LinuxChangeTrackingPath, ChangeTrackingContentLocation, WindowsTelemetry, Office365, SecurityWindowsBaselineConfiguration, SecurityCenterSecurityWindowsBaselineConfiguration, SecurityEventCollectionConfiguration, SecurityInsightsSecurityEventCollectionConfiguration, ImportComputerGroup, NetworkMonitoring, Itsm, DnsAnalytics, ApplicationInsights, SqlDataClassification)</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The data source properties in raw json format, each kind of data source have it's own schema. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_source_name"><code>data_source_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a datasource instance.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Gets the first page of data source instances in a workspace with the link to the next page.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_source_name"><code>data_source_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create or update a data source.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_source_name"><code>data_source_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create or update a data source.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_source_name"><code>data_source_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a data source instance.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Required.</td>
</tr>
<tr id="parameter-data_source_name">
    <td><CopyableCode code="data_source_name" /></td>
    <td><code>string</code></td>
    <td>Name of the datasource. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Starting point of the collection of data source instances. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Gets a datasource instance.

```sql
SELECT
id,
name,
etag,
kind,
properties,
systemData,
tags,
type
FROM azure.log_analytics.data_sources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND data_source_name = '{{ data_source_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

Gets the first page of data source instances in a workspace with the link to the next page.

```sql
SELECT
id,
name,
etag,
kind,
properties,
systemData,
tags,
type
FROM azure.log_analytics.data_sources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
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

Create or update a data source.

```sql
INSERT INTO azure.log_analytics.data_sources (
properties,
etag,
kind,
tags,
resource_group_name,
workspace_name,
data_source_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ etag }}',
'{{ kind }}' /* required */,
'{{ tags }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ data_source_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: data_sources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_sources resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the data_sources resource.
    - name: data_source_name
      value: "{{ data_source_name }}"
      description: Required parameter for the data_sources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_sources resource.
    - name: properties
      value: "{{ properties }}"
      description: |
        The data source properties in raw json format, each kind of data source have it's own schema. Required.
    - name: etag
      value: "{{ etag }}"
      description: |
        The ETag of the data source.
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the DataSource. Required. Known values are: "WindowsEvent", "WindowsPerformanceCounter", "IISLogs", "LinuxSyslog", "LinuxSyslogCollection", "LinuxPerformanceObject", "LinuxPerformanceCollection", "CustomLog", "CustomLogCollection", "AzureAuditLog", "AzureActivityLog", "GenericDataSource", "ChangeTrackingCustomPath", "ChangeTrackingPath", "ChangeTrackingServices", "ChangeTrackingDataTypeConfiguration", "ChangeTrackingDefaultRegistry", "ChangeTrackingRegistry", "ChangeTrackingLinuxPath", "LinuxChangeTrackingPath", "ChangeTrackingContentLocation", "WindowsTelemetry", "Office365", "SecurityWindowsBaselineConfiguration", "SecurityCenterSecurityWindowsBaselineConfiguration", "SecurityEventCollectionConfiguration", "SecurityInsightsSecurityEventCollectionConfiguration", "ImportComputerGroup", "NetworkMonitoring", "Itsm", "DnsAnalytics", "ApplicationInsights", and "SqlDataClassification".
      valid_values: ['WindowsEvent', 'WindowsPerformanceCounter', 'IISLogs', 'LinuxSyslog', 'LinuxSyslogCollection', 'LinuxPerformanceObject', 'LinuxPerformanceCollection', 'CustomLog', 'CustomLogCollection', 'AzureAuditLog', 'AzureActivityLog', 'GenericDataSource', 'ChangeTrackingCustomPath', 'ChangeTrackingPath', 'ChangeTrackingServices', 'ChangeTrackingDataTypeConfiguration', 'ChangeTrackingDefaultRegistry', 'ChangeTrackingRegistry', 'ChangeTrackingLinuxPath', 'LinuxChangeTrackingPath', 'ChangeTrackingContentLocation', 'WindowsTelemetry', 'Office365', 'SecurityWindowsBaselineConfiguration', 'SecurityCenterSecurityWindowsBaselineConfiguration', 'SecurityEventCollectionConfiguration', 'SecurityInsightsSecurityEventCollectionConfiguration', 'ImportComputerGroup', 'NetworkMonitoring', 'Itsm', 'DnsAnalytics', 'ApplicationInsights', 'SqlDataClassification']
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
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

Create or update a data source.

```sql
REPLACE azure.log_analytics.data_sources
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
kind = '{{ kind }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND data_source_name = '{{ data_source_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
etag,
kind,
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

Deletes a data source instance.

```sql
DELETE FROM azure.log_analytics.data_sources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND data_source_name = '{{ data_source_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
