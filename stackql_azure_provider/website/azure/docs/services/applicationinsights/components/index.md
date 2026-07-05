--- 
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
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

Creates, updates, deletes, gets or lists a <code>components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="components" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.components" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_purge_status"
    values={[
        { label: 'get_purge_status', value: 'get_purge_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_purge_status">

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
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the operation represented by the requested Id. Required. Known values are: "pending" and "completed". (pending, completed)</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="AppId" /></td>
    <td><code>string</code></td>
    <td>Application Insights Unique ID for your Application.</td>
</tr>
<tr>
    <td><CopyableCode code="ApplicationId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of your application. This field mirrors the 'Name' field and cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="Application_Type" /></td>
    <td><code>string</code></td>
    <td>Type of application being monitored. Required. Known values are: "web" and "other". (web, other)</td>
</tr>
<tr>
    <td><CopyableCode code="ConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights component connection string.</td>
</tr>
<tr>
    <td><CopyableCode code="CreationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation Date for the Application Insights component, in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="DisableIpMasking" /></td>
    <td><code>boolean</code></td>
    <td>Disable IP masking.</td>
</tr>
<tr>
    <td><CopyableCode code="DisableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Disable Non-AAD based Auth.</td>
</tr>
<tr>
    <td><CopyableCode code="Flow_Type" /></td>
    <td><code>string</code></td>
    <td>Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API. "Bluefield" (Bluefield)</td>
</tr>
<tr>
    <td><CopyableCode code="ForceCustomerStorageForProfiler" /></td>
    <td><code>boolean</code></td>
    <td>Force users to create their own storage account for profiler and debugger.</td>
</tr>
<tr>
    <td><CopyableCode code="HockeyAppId" /></td>
    <td><code>string</code></td>
    <td>The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.</td>
</tr>
<tr>
    <td><CopyableCode code="HockeyAppToken" /></td>
    <td><code>string</code></td>
    <td>Token used to authenticate communications with between Application Insights and HockeyApp.</td>
</tr>
<tr>
    <td><CopyableCode code="ImmediatePurgeDataOn30Days" /></td>
    <td><code>boolean</code></td>
    <td>Purge data immediately after 30 days.</td>
</tr>
<tr>
    <td><CopyableCode code="IngestionMode" /></td>
    <td><code>string</code></td>
    <td>Indicates the flow of the ingestion. Known values are: "ApplicationInsights", "ApplicationInsightsWithDiagnosticSettings", and "LogAnalytics". (ApplicationInsights, ApplicationInsightsWithDiagnosticSettings, LogAnalytics)</td>
</tr>
<tr>
    <td><CopyableCode code="InstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>Application Insights Instrumentation key. A read-only value that applications can use to identify the destination for all telemetry sent to Azure Application Insights. This value will be supplied upon construction of each new Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="LaMigrationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date which the component got migrated to LA, in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>Application name.</td>
</tr>
<tr>
    <td><CopyableCode code="PrivateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of linked private link scope resources.</td>
</tr>
<tr>
    <td><CopyableCode code="Request_Source" /></td>
    <td><code>string</code></td>
    <td>Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'. "rest" (rest)</td>
</tr>
<tr>
    <td><CopyableCode code="RetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period in days.</td>
</tr>
<tr>
    <td><CopyableCode code="SamplingPercentage" /></td>
    <td><code>number</code></td>
    <td>Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="TenantId" /></td>
    <td><code>string</code></td>
    <td>Azure Tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="WorkspaceResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this component: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForIngestion" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Application Insights ingestion. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForQuery" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Application Insights query. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="AppId" /></td>
    <td><code>string</code></td>
    <td>Application Insights Unique ID for your Application.</td>
</tr>
<tr>
    <td><CopyableCode code="ApplicationId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of your application. This field mirrors the 'Name' field and cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="Application_Type" /></td>
    <td><code>string</code></td>
    <td>Type of application being monitored. Required. Known values are: "web" and "other". (web, other)</td>
</tr>
<tr>
    <td><CopyableCode code="ConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights component connection string.</td>
</tr>
<tr>
    <td><CopyableCode code="CreationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation Date for the Application Insights component, in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="DisableIpMasking" /></td>
    <td><code>boolean</code></td>
    <td>Disable IP masking.</td>
</tr>
<tr>
    <td><CopyableCode code="DisableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Disable Non-AAD based Auth.</td>
</tr>
<tr>
    <td><CopyableCode code="Flow_Type" /></td>
    <td><code>string</code></td>
    <td>Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API. "Bluefield" (Bluefield)</td>
</tr>
<tr>
    <td><CopyableCode code="ForceCustomerStorageForProfiler" /></td>
    <td><code>boolean</code></td>
    <td>Force users to create their own storage account for profiler and debugger.</td>
</tr>
<tr>
    <td><CopyableCode code="HockeyAppId" /></td>
    <td><code>string</code></td>
    <td>The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.</td>
</tr>
<tr>
    <td><CopyableCode code="HockeyAppToken" /></td>
    <td><code>string</code></td>
    <td>Token used to authenticate communications with between Application Insights and HockeyApp.</td>
</tr>
<tr>
    <td><CopyableCode code="ImmediatePurgeDataOn30Days" /></td>
    <td><code>boolean</code></td>
    <td>Purge data immediately after 30 days.</td>
</tr>
<tr>
    <td><CopyableCode code="IngestionMode" /></td>
    <td><code>string</code></td>
    <td>Indicates the flow of the ingestion. Known values are: "ApplicationInsights", "ApplicationInsightsWithDiagnosticSettings", and "LogAnalytics". (ApplicationInsights, ApplicationInsightsWithDiagnosticSettings, LogAnalytics)</td>
</tr>
<tr>
    <td><CopyableCode code="InstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>Application Insights Instrumentation key. A read-only value that applications can use to identify the destination for all telemetry sent to Azure Application Insights. This value will be supplied upon construction of each new Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="LaMigrationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date which the component got migrated to LA, in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>Application name.</td>
</tr>
<tr>
    <td><CopyableCode code="PrivateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of linked private link scope resources.</td>
</tr>
<tr>
    <td><CopyableCode code="Request_Source" /></td>
    <td><code>string</code></td>
    <td>Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'. "rest" (rest)</td>
</tr>
<tr>
    <td><CopyableCode code="RetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period in days.</td>
</tr>
<tr>
    <td><CopyableCode code="SamplingPercentage" /></td>
    <td><code>number</code></td>
    <td>Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="TenantId" /></td>
    <td><code>string</code></td>
    <td>Azure Tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="WorkspaceResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this component: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForIngestion" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Application Insights ingestion. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForQuery" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Application Insights query. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="AppId" /></td>
    <td><code>string</code></td>
    <td>Application Insights Unique ID for your Application.</td>
</tr>
<tr>
    <td><CopyableCode code="ApplicationId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of your application. This field mirrors the 'Name' field and cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="Application_Type" /></td>
    <td><code>string</code></td>
    <td>Type of application being monitored. Required. Known values are: "web" and "other". (web, other)</td>
</tr>
<tr>
    <td><CopyableCode code="ConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights component connection string.</td>
</tr>
<tr>
    <td><CopyableCode code="CreationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation Date for the Application Insights component, in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="DisableIpMasking" /></td>
    <td><code>boolean</code></td>
    <td>Disable IP masking.</td>
</tr>
<tr>
    <td><CopyableCode code="DisableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Disable Non-AAD based Auth.</td>
</tr>
<tr>
    <td><CopyableCode code="Flow_Type" /></td>
    <td><code>string</code></td>
    <td>Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API. "Bluefield" (Bluefield)</td>
</tr>
<tr>
    <td><CopyableCode code="ForceCustomerStorageForProfiler" /></td>
    <td><code>boolean</code></td>
    <td>Force users to create their own storage account for profiler and debugger.</td>
</tr>
<tr>
    <td><CopyableCode code="HockeyAppId" /></td>
    <td><code>string</code></td>
    <td>The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.</td>
</tr>
<tr>
    <td><CopyableCode code="HockeyAppToken" /></td>
    <td><code>string</code></td>
    <td>Token used to authenticate communications with between Application Insights and HockeyApp.</td>
</tr>
<tr>
    <td><CopyableCode code="ImmediatePurgeDataOn30Days" /></td>
    <td><code>boolean</code></td>
    <td>Purge data immediately after 30 days.</td>
</tr>
<tr>
    <td><CopyableCode code="IngestionMode" /></td>
    <td><code>string</code></td>
    <td>Indicates the flow of the ingestion. Known values are: "ApplicationInsights", "ApplicationInsightsWithDiagnosticSettings", and "LogAnalytics". (ApplicationInsights, ApplicationInsightsWithDiagnosticSettings, LogAnalytics)</td>
</tr>
<tr>
    <td><CopyableCode code="InstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>Application Insights Instrumentation key. A read-only value that applications can use to identify the destination for all telemetry sent to Azure Application Insights. This value will be supplied upon construction of each new Application Insights component.</td>
</tr>
<tr>
    <td><CopyableCode code="LaMigrationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date which the component got migrated to LA, in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>Application name.</td>
</tr>
<tr>
    <td><CopyableCode code="PrivateLinkScopedResources" /></td>
    <td><code>array</code></td>
    <td>List of linked private link scope resources.</td>
</tr>
<tr>
    <td><CopyableCode code="Request_Source" /></td>
    <td><code>string</code></td>
    <td>Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'. "rest" (rest)</td>
</tr>
<tr>
    <td><CopyableCode code="RetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period in days.</td>
</tr>
<tr>
    <td><CopyableCode code="SamplingPercentage" /></td>
    <td><code>number</code></td>
    <td>Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="TenantId" /></td>
    <td><code>string</code></td>
    <td>Azure Tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="WorkspaceResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this component: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForIngestion" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Application Insights ingestion. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccessForQuery" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing Application Insights query. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
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
    <td><a href="#get_purge_status"><CopyableCode code="get_purge_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-purge_id"><code>purge_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get status for an ongoing purge operation.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Application Insights components within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all Application Insights components within a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing component's tags. To update other fields use the CreateOrUpdate method.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.</td>
</tr>
<tr>
    <td><a href="#purge"><CopyableCode code="purge" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Purges data in an Application Insights component by a set of user-defined filters. In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected. Note: this operation is intended for Classic resources, for workspace-based Application Insights resource please run purge operation (directly on the workspace)(`https://docs.microsoft.com/en-us/rest/api/loganalytics/workspace-purge/purge `_) , scoped to specific resource id.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Application Insights component.</td>
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
<tr id="parameter-purge_id">
    <td><CopyableCode code="purge_id" /></td>
    <td><code>string</code></td>
    <td>In a purge status request, this is the Id of the operation the status of which is returned. Required.</td>
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
    defaultValue="get_purge_status"
    values={[
        { label: 'get_purge_status', value: 'get_purge_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_purge_status">

Get status for an ongoing purge operation.

```sql
SELECT
status
FROM azure.applicationinsights.components
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND purge_id = '{{ purge_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Returns an Application Insights component.

```sql
SELECT
id,
name,
AppId,
ApplicationId,
Application_Type,
ConnectionString,
CreationDate,
DisableIpMasking,
DisableLocalAuth,
Flow_Type,
ForceCustomerStorageForProfiler,
HockeyAppId,
HockeyAppToken,
ImmediatePurgeDataOn30Days,
IngestionMode,
InstrumentationKey,
LaMigrationDate,
Name,
PrivateLinkScopedResources,
Request_Source,
RetentionInDays,
SamplingPercentage,
TenantId,
WorkspaceResourceId,
etag,
kind,
location,
provisioningState,
publicNetworkAccessForIngestion,
publicNetworkAccessForQuery,
tags,
type
FROM azure.applicationinsights.components
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of Application Insights components within a resource group.

```sql
SELECT
id,
name,
AppId,
ApplicationId,
Application_Type,
ConnectionString,
CreationDate,
DisableIpMasking,
DisableLocalAuth,
Flow_Type,
ForceCustomerStorageForProfiler,
HockeyAppId,
HockeyAppToken,
ImmediatePurgeDataOn30Days,
IngestionMode,
InstrumentationKey,
LaMigrationDate,
Name,
PrivateLinkScopedResources,
Request_Source,
RetentionInDays,
SamplingPercentage,
TenantId,
WorkspaceResourceId,
etag,
kind,
location,
provisioningState,
publicNetworkAccessForIngestion,
publicNetworkAccessForQuery,
tags,
type
FROM azure.applicationinsights.components
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of all Application Insights components within a subscription.

```sql
SELECT
id,
name,
AppId,
ApplicationId,
Application_Type,
ConnectionString,
CreationDate,
DisableIpMasking,
DisableLocalAuth,
Flow_Type,
ForceCustomerStorageForProfiler,
HockeyAppId,
HockeyAppToken,
ImmediatePurgeDataOn30Days,
IngestionMode,
InstrumentationKey,
LaMigrationDate,
Name,
PrivateLinkScopedResources,
Request_Source,
RetentionInDays,
SamplingPercentage,
TenantId,
WorkspaceResourceId,
etag,
kind,
location,
provisioningState,
publicNetworkAccessForIngestion,
publicNetworkAccessForQuery,
tags,
type
FROM azure.applicationinsights.components
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

Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

```sql
INSERT INTO azure.applicationinsights.components (
location,
tags,
kind,
etag,
properties,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ kind }}' /* required */,
'{{ etag }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: components
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the components resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the components resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the components resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. Required.
    - name: etag
      value: "{{ etag }}"
      description: |
        Resource etag.
    - name: properties
      description: |
        Properties that define an Application Insights component resource.
      value:
        ApplicationId: "{{ ApplicationId }}"
        AppId: "{{ AppId }}"
        Name: "{{ Name }}"
        Application_Type: "{{ Application_Type }}"
        Flow_Type: "{{ Flow_Type }}"
        Request_Source: "{{ Request_Source }}"
        InstrumentationKey: "{{ InstrumentationKey }}"
        CreationDate: "{{ CreationDate }}"
        TenantId: "{{ TenantId }}"
        HockeyAppId: "{{ HockeyAppId }}"
        HockeyAppToken: "{{ HockeyAppToken }}"
        provisioningState: "{{ provisioningState }}"
        SamplingPercentage: {{ SamplingPercentage }}
        ConnectionString: "{{ ConnectionString }}"
        RetentionInDays: {{ RetentionInDays }}
        DisableIpMasking: {{ DisableIpMasking }}
        ImmediatePurgeDataOn30Days: {{ ImmediatePurgeDataOn30Days }}
        WorkspaceResourceId: "{{ WorkspaceResourceId }}"
        LaMigrationDate: "{{ LaMigrationDate }}"
        PrivateLinkScopedResources:
          - ResourceId: "{{ ResourceId }}"
            ScopeId: "{{ ScopeId }}"
        publicNetworkAccessForIngestion: "{{ publicNetworkAccessForIngestion }}"
        publicNetworkAccessForQuery: "{{ publicNetworkAccessForQuery }}"
        IngestionMode: "{{ IngestionMode }}"
        DisableLocalAuth: {{ DisableLocalAuth }}
        ForceCustomerStorageForProfiler: {{ ForceCustomerStorageForProfiler }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates an existing component's tags. To update other fields use the CreateOrUpdate method.

```sql
UPDATE azure.applicationinsights.components
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
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

Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

```sql
REPLACE azure.applicationinsights.components
SET 
location = '{{ location }}',
tags = '{{ tags }}',
kind = '{{ kind }}',
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="purge"
    values={[
        { label: 'purge', value: 'purge' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="purge">

Purges data in an Application Insights component by a set of user-defined filters. In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected. Note: this operation is intended for Classic resources, for workspace-based Application Insights resource please run purge operation (directly on the workspace)(`https://docs.microsoft.com/en-us/rest/api/loganalytics/workspace-purge/purge `_) , scoped to specific resource id.

```sql
DELETE FROM azure.applicationinsights.components
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes an Application Insights component.

```sql
DELETE FROM azure.applicationinsights.components
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
