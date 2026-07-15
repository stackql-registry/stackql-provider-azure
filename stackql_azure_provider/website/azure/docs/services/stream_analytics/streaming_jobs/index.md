--- 
title: streaming_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_jobs
  - stream_analytics
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

Creates, updates, deletes, gets or lists a <code>streaming_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="streaming_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.streaming_jobs" /></td></tr>
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster" /></td>
    <td><code>object</code></td>
    <td>The cluster which streaming jobs will run on.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibilityLevel" /></td>
    <td><code>string</code></td>
    <td>Controls certain runtime behaviors of the streaming job. Known values are: "1.0" and "1.2".</td>
</tr>
<tr>
    <td><CopyableCode code="contentStoragePolicy" /></td>
    <td><code>string</code></td>
    <td>Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this requires the user to also specify jobStorageAccount property. . Known values are: "SystemAccount" and "JobStorageAccount".</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is an ISO-8601 formatted UTC timestamp indicating when the streaming job was created.</td>
</tr>
<tr>
    <td><CopyableCode code="dataLocale" /></td>
    <td><code>string</code></td>
    <td>The data locale of the stream analytics job. Value should be the name of a supported .NET Culture from the set https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx. Defaults to 'en-US' if none specified.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The current entity tag for the streaming job. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsLateArrivalMaxDelayInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum tolerable delay in seconds where events arriving late could be included. Supported range is -1 to 1814399 (20.23:59:59 days) and -1 is used to specify wait indefinitely. If the property is absent, it is interpreted to have a value of -1.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsOutOfOrderMaxDelayInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsOutOfOrderPolicy" /></td>
    <td><code>string</code></td>
    <td>Indicates the policy to apply to events that arrive out of order in the input event stream. Known values are: "Adjust" and "Drop".</td>
</tr>
<tr>
    <td><CopyableCode code="externals" /></td>
    <td><code>object</code></td>
    <td>The storage account where the custom code artifacts are located.</td>
</tr>
<tr>
    <td><CopyableCode code="functions" /></td>
    <td><code>array</code></td>
    <td>A list of one or more functions for the streaming job. The name property for each function is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual transformation.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Describes the managed identity assigned to this job that can be used to authenticate with inputs and outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>array</code></td>
    <td>A list of one or more inputs to the streaming job. The name property for each input is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual input.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>A GUID uniquely identifying the streaming job. This GUID is generated upon creation of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobState" /></td>
    <td><code>string</code></td>
    <td>Describes the state of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobStorageAccount" /></td>
    <td><code>object</code></td>
    <td>The properties that are associated with an Azure Storage account with MSI.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Describes the type of the job. Valid modes are `Cloud` and 'Edge'. Known values are: "Cloud" and "Edge".</td>
</tr>
<tr>
    <td><CopyableCode code="lastOutputEventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is either an ISO-8601 formatted timestamp indicating the last output event time of the streaming job or null indicating that output has not yet been produced. In case of multiple outputs or multiple streams, this shows the latest value in that set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="outputErrorPolicy" /></td>
    <td><code>string</code></td>
    <td>Indicates the policy to apply to events that arrive at the output and cannot be written to the external storage due to being malformed (missing column values, column values of wrong type or size). Known values are: "Stop" and "Drop".</td>
</tr>
<tr>
    <td><CopyableCode code="outputStartMode" /></td>
    <td><code>string</code></td>
    <td>This property should only be utilized when it is desired that the job be started immediately upon creation. Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the starting point of the output event stream should start whenever the job is started, start at a custom user time stamp specified via the outputStartTime property, or start from the last event output time. Known values are: "JobStartTime", "CustomTime", and "LastOutputEventTime".</td>
</tr>
<tr>
    <td><CopyableCode code="outputStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is either an ISO-8601 formatted time stamp that indicates the starting point of the output event stream, or null to indicate that the output event stream will start whenever the streaming job is started. This property must have a value if outputStartMode is set to CustomTime.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>array</code></td>
    <td>A list of one or more outputs for the streaming job. The name property for each output is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual output.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Describes the provisioning status of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Describes the SKU of the streaming job. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="transformation" /></td>
    <td><code>object</code></td>
    <td>Indicates the query and the number of streaming units to use for the streaming job. The name property of the transformation is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual transformation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster" /></td>
    <td><code>object</code></td>
    <td>The cluster which streaming jobs will run on.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibilityLevel" /></td>
    <td><code>string</code></td>
    <td>Controls certain runtime behaviors of the streaming job. Known values are: "1.0" and "1.2".</td>
</tr>
<tr>
    <td><CopyableCode code="contentStoragePolicy" /></td>
    <td><code>string</code></td>
    <td>Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this requires the user to also specify jobStorageAccount property. . Known values are: "SystemAccount" and "JobStorageAccount".</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is an ISO-8601 formatted UTC timestamp indicating when the streaming job was created.</td>
</tr>
<tr>
    <td><CopyableCode code="dataLocale" /></td>
    <td><code>string</code></td>
    <td>The data locale of the stream analytics job. Value should be the name of a supported .NET Culture from the set https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx. Defaults to 'en-US' if none specified.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The current entity tag for the streaming job. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsLateArrivalMaxDelayInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum tolerable delay in seconds where events arriving late could be included. Supported range is -1 to 1814399 (20.23:59:59 days) and -1 is used to specify wait indefinitely. If the property is absent, it is interpreted to have a value of -1.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsOutOfOrderMaxDelayInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsOutOfOrderPolicy" /></td>
    <td><code>string</code></td>
    <td>Indicates the policy to apply to events that arrive out of order in the input event stream. Known values are: "Adjust" and "Drop".</td>
</tr>
<tr>
    <td><CopyableCode code="externals" /></td>
    <td><code>object</code></td>
    <td>The storage account where the custom code artifacts are located.</td>
</tr>
<tr>
    <td><CopyableCode code="functions" /></td>
    <td><code>array</code></td>
    <td>A list of one or more functions for the streaming job. The name property for each function is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual transformation.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Describes the managed identity assigned to this job that can be used to authenticate with inputs and outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>array</code></td>
    <td>A list of one or more inputs to the streaming job. The name property for each input is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual input.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>A GUID uniquely identifying the streaming job. This GUID is generated upon creation of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobState" /></td>
    <td><code>string</code></td>
    <td>Describes the state of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobStorageAccount" /></td>
    <td><code>object</code></td>
    <td>The properties that are associated with an Azure Storage account with MSI.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Describes the type of the job. Valid modes are `Cloud` and 'Edge'. Known values are: "Cloud" and "Edge".</td>
</tr>
<tr>
    <td><CopyableCode code="lastOutputEventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is either an ISO-8601 formatted timestamp indicating the last output event time of the streaming job or null indicating that output has not yet been produced. In case of multiple outputs or multiple streams, this shows the latest value in that set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="outputErrorPolicy" /></td>
    <td><code>string</code></td>
    <td>Indicates the policy to apply to events that arrive at the output and cannot be written to the external storage due to being malformed (missing column values, column values of wrong type or size). Known values are: "Stop" and "Drop".</td>
</tr>
<tr>
    <td><CopyableCode code="outputStartMode" /></td>
    <td><code>string</code></td>
    <td>This property should only be utilized when it is desired that the job be started immediately upon creation. Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the starting point of the output event stream should start whenever the job is started, start at a custom user time stamp specified via the outputStartTime property, or start from the last event output time. Known values are: "JobStartTime", "CustomTime", and "LastOutputEventTime".</td>
</tr>
<tr>
    <td><CopyableCode code="outputStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is either an ISO-8601 formatted time stamp that indicates the starting point of the output event stream, or null to indicate that the output event stream will start whenever the streaming job is started. This property must have a value if outputStartMode is set to CustomTime.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>array</code></td>
    <td>A list of one or more outputs for the streaming job. The name property for each output is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual output.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Describes the provisioning status of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Describes the SKU of the streaming job. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="transformation" /></td>
    <td><code>object</code></td>
    <td>Indicates the query and the number of streaming units to use for the streaming job. The name property of the transformation is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual transformation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster" /></td>
    <td><code>object</code></td>
    <td>The cluster which streaming jobs will run on.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibilityLevel" /></td>
    <td><code>string</code></td>
    <td>Controls certain runtime behaviors of the streaming job. Known values are: "1.0" and "1.2".</td>
</tr>
<tr>
    <td><CopyableCode code="contentStoragePolicy" /></td>
    <td><code>string</code></td>
    <td>Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this requires the user to also specify jobStorageAccount property. . Known values are: "SystemAccount" and "JobStorageAccount".</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is an ISO-8601 formatted UTC timestamp indicating when the streaming job was created.</td>
</tr>
<tr>
    <td><CopyableCode code="dataLocale" /></td>
    <td><code>string</code></td>
    <td>The data locale of the stream analytics job. Value should be the name of a supported .NET Culture from the set https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx. Defaults to 'en-US' if none specified.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The current entity tag for the streaming job. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsLateArrivalMaxDelayInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum tolerable delay in seconds where events arriving late could be included. Supported range is -1 to 1814399 (20.23:59:59 days) and -1 is used to specify wait indefinitely. If the property is absent, it is interpreted to have a value of -1.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsOutOfOrderMaxDelayInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order.</td>
</tr>
<tr>
    <td><CopyableCode code="eventsOutOfOrderPolicy" /></td>
    <td><code>string</code></td>
    <td>Indicates the policy to apply to events that arrive out of order in the input event stream. Known values are: "Adjust" and "Drop".</td>
</tr>
<tr>
    <td><CopyableCode code="externals" /></td>
    <td><code>object</code></td>
    <td>The storage account where the custom code artifacts are located.</td>
</tr>
<tr>
    <td><CopyableCode code="functions" /></td>
    <td><code>array</code></td>
    <td>A list of one or more functions for the streaming job. The name property for each function is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual transformation.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Describes the managed identity assigned to this job that can be used to authenticate with inputs and outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>array</code></td>
    <td>A list of one or more inputs to the streaming job. The name property for each input is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual input.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>A GUID uniquely identifying the streaming job. This GUID is generated upon creation of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobState" /></td>
    <td><code>string</code></td>
    <td>Describes the state of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobStorageAccount" /></td>
    <td><code>object</code></td>
    <td>The properties that are associated with an Azure Storage account with MSI.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Describes the type of the job. Valid modes are `Cloud` and 'Edge'. Known values are: "Cloud" and "Edge".</td>
</tr>
<tr>
    <td><CopyableCode code="lastOutputEventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is either an ISO-8601 formatted timestamp indicating the last output event time of the streaming job or null indicating that output has not yet been produced. In case of multiple outputs or multiple streams, this shows the latest value in that set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="outputErrorPolicy" /></td>
    <td><code>string</code></td>
    <td>Indicates the policy to apply to events that arrive at the output and cannot be written to the external storage due to being malformed (missing column values, column values of wrong type or size). Known values are: "Stop" and "Drop".</td>
</tr>
<tr>
    <td><CopyableCode code="outputStartMode" /></td>
    <td><code>string</code></td>
    <td>This property should only be utilized when it is desired that the job be started immediately upon creation. Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the starting point of the output event stream should start whenever the job is started, start at a custom user time stamp specified via the outputStartTime property, or start from the last event output time. Known values are: "JobStartTime", "CustomTime", and "LastOutputEventTime".</td>
</tr>
<tr>
    <td><CopyableCode code="outputStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Value is either an ISO-8601 formatted time stamp that indicates the starting point of the output event stream, or null to indicate that the output event stream will start whenever the streaming job is started. This property must have a value if outputStartMode is set to CustomTime.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>array</code></td>
    <td>A list of one or more outputs for the streaming job. The name property for each output is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual output.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Describes the provisioning status of the streaming job.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Describes the SKU of the streaming job. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="transformation" /></td>
    <td><code>object</code></td>
    <td>Indicates the query and the number of streaming units to use for the streaming job. The name property of the transformation is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual transformation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets details about the specified streaming job.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the streaming jobs in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the streaming jobs in the given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates a streaming job or replaces an already existing streaming job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates an existing streaming job. This can be used to partially update (ie. update one or two properties) a streaming job without affecting the rest the job definition.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates a streaming job or replaces an already existing streaming job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a streaming job.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a streaming job. Once a job is started it will start processing input events and produce output.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops a running streaming job. This will cause a running streaming job to stop processing input events and producing output.</td>
</tr>
<tr>
    <td><a href="#scale"><CopyableCode code="scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Scales a streaming job when the job is running.</td>
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
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The name of the streaming job. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The $expand OData query parameter. This is a comma-separated list of additional streaming job properties to include in the response, beyond the default set returned when this parameter is absent. The default set is all streaming job properties other than 'inputs', 'transformation', 'outputs', and 'functions'. Default value is None.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The ETag of the streaming job. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>Set to '*' to allow a new streaming job to be created, but to prevent updating an existing record set. Other values will result in a 412 Pre-condition Failed response. Default value is None.</td>
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

Gets details about the specified streaming job.

```sql
SELECT
id,
name,
cluster,
compatibilityLevel,
contentStoragePolicy,
createdDate,
dataLocale,
etag,
eventsLateArrivalMaxDelayInSeconds,
eventsOutOfOrderMaxDelayInSeconds,
eventsOutOfOrderPolicy,
externals,
functions,
identity,
inputs,
jobId,
jobState,
jobStorageAccount,
jobType,
lastOutputEventTime,
location,
outputErrorPolicy,
outputStartMode,
outputStartTime,
outputs,
provisioningState,
sku,
tags,
transformation,
type
FROM azure.stream_analytics.streaming_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all of the streaming jobs in the specified resource group.

```sql
SELECT
id,
name,
cluster,
compatibilityLevel,
contentStoragePolicy,
createdDate,
dataLocale,
etag,
eventsLateArrivalMaxDelayInSeconds,
eventsOutOfOrderMaxDelayInSeconds,
eventsOutOfOrderPolicy,
externals,
functions,
identity,
inputs,
jobId,
jobState,
jobStorageAccount,
jobType,
lastOutputEventTime,
location,
outputErrorPolicy,
outputStartMode,
outputStartTime,
outputs,
provisioningState,
sku,
tags,
transformation,
type
FROM azure.stream_analytics.streaming_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Lists all of the streaming jobs in the given subscription.

```sql
SELECT
id,
name,
cluster,
compatibilityLevel,
contentStoragePolicy,
createdDate,
dataLocale,
etag,
eventsLateArrivalMaxDelayInSeconds,
eventsOutOfOrderMaxDelayInSeconds,
eventsOutOfOrderPolicy,
externals,
functions,
identity,
inputs,
jobId,
jobState,
jobStorageAccount,
jobType,
lastOutputEventTime,
location,
outputErrorPolicy,
outputStartMode,
outputStartTime,
outputs,
provisioningState,
sku,
tags,
transformation,
type
FROM azure.stream_analytics.streaming_jobs
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_replace">

Creates a streaming job or replaces an already existing streaming job.

```sql
INSERT INTO azure.stream_analytics.streaming_jobs (
tags,
location,
sku,
identity,
properties,
resource_group_name,
job_name,
subscription_id,
If-Match,
If-None-Match
)
SELECT 
'{{ tags }}',
'{{ location }}',
'{{ sku }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ job_name }}',
'{{ subscription_id }}',
'{{ If-Match }}',
'{{ If-None-Match }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: streaming_jobs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the streaming_jobs resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the streaming_jobs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the streaming_jobs resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: sku
      description: |
        Describes the SKU of the streaming job. Required on PUT (CreateOrReplace) requests.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Describes the managed identity assigned to this job that can be used to authenticate with inputs and outputs.
      value:
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        sku:
          name: "{{ name }}"
          capacity: {{ capacity }}
        jobType: "{{ jobType }}"
        outputStartMode: "{{ outputStartMode }}"
        outputStartTime: "{{ outputStartTime }}"
        eventsOutOfOrderPolicy: "{{ eventsOutOfOrderPolicy }}"
        outputErrorPolicy: "{{ outputErrorPolicy }}"
        eventsOutOfOrderMaxDelayInSeconds: {{ eventsOutOfOrderMaxDelayInSeconds }}
        eventsLateArrivalMaxDelayInSeconds: {{ eventsLateArrivalMaxDelayInSeconds }}
        dataLocale: "{{ dataLocale }}"
        compatibilityLevel: "{{ compatibilityLevel }}"
        inputs:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              type: "{{ type }}"
              serialization:
                type: "{{ type }}"
              diagnostics:
                conditions:
                  - since: "{{ since }}"
                    code: "{{ code }}"
                    message: "{{ message }}"
              etag: "{{ etag }}"
              compression:
                type: "{{ type }}"
              partitionKey: "{{ partitionKey }}"
              watermarkSettings:
                watermarkMode: "{{ watermarkMode }}"
        transformation:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          properties:
            streamingUnits: {{ streamingUnits }}
            validStreamingUnits:
              - {{ validStreamingUnits }}
            query: "{{ query }}"
            etag: "{{ etag }}"
        outputs:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              datasource:
                type: "{{ type }}"
              timeWindow: "{{ timeWindow }}"
              sizeWindow: {{ sizeWindow }}
              serialization:
                type: "{{ type }}"
              diagnostics:
                conditions:
                  - since: "{{ since }}"
                    code: "{{ code }}"
                    message: "{{ message }}"
              etag: "{{ etag }}"
              lastOutputEventTimestamps:
                - lastOutputEventTime: "{{ lastOutputEventTime }}"
                  lastUpdateTime: "{{ lastUpdateTime }}"
              watermarkSettings:
                watermarkMode: "{{ watermarkMode }}"
                maxWatermarkDifferenceAcrossPartitions: "{{ maxWatermarkDifferenceAcrossPartitions }}"
        functions:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              type: "{{ type }}"
              etag: "{{ etag }}"
              properties:
                inputs:
                  - dataType: "{{ dataType }}"
                    isConfigurationParameter: {{ isConfigurationParameter }}
                output:
                  dataType: "{{ dataType }}"
                binding:
                  type: "{{ type }}"
        jobStorageAccount:
          accountName: "{{ accountName }}"
          accountKey: "{{ accountKey }}"
          authenticationMode: "{{ authenticationMode }}"
        contentStoragePolicy: "{{ contentStoragePolicy }}"
        externals:
          storageAccount:
            accountName: "{{ accountName }}"
            accountKey: "{{ accountKey }}"
            authenticationMode: "{{ authenticationMode }}"
          container: "{{ container }}"
          path: "{{ path }}"
          refreshConfiguration:
            pathPattern: "{{ pathPattern }}"
            dateFormat: "{{ dateFormat }}"
            timeFormat: "{{ timeFormat }}"
            refreshInterval: "{{ refreshInterval }}"
            refreshType: "{{ refreshType }}"
        cluster:
          id: "{{ id }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: The ETag of the streaming job. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
      description: The ETag of the streaming job. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
    - name: If-None-Match
      value: "{{ If-None-Match }}"
      description: Set to '*' to allow a new streaming job to be created, but to prevent updating an existing record set. Other values will result in a 412 Pre-condition Failed response. Default value is None.
      description: Set to '*' to allow a new streaming job to be created, but to prevent updating an existing record set. Other values will result in a 412 Pre-condition Failed response. Default value is None.
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

Updates an existing streaming job. This can be used to partially update (ie. update one or two properties) a streaming job without affecting the rest the job definition.

```sql
UPDATE azure.stream_analytics.streaming_jobs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' }
    ]}
>
<TabItem value="create_or_replace">

Creates a streaming job or replaces an already existing streaming job.

```sql
REPLACE azure.stream_analytics.streaming_jobs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
AND If-None-Match = '{{ If-None-Match}}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Deletes a streaming job.

```sql
DELETE FROM azure.stream_analytics.streaming_jobs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'scale', value: 'scale' }
    ]}
>
<TabItem value="start">

Starts a streaming job. Once a job is started it will start processing input events and produce output.

```sql
EXEC azure.stream_analytics.streaming_jobs.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"outputStartMode": "{{ outputStartMode }}", 
"outputStartTime": "{{ outputStartTime }}"
}'
;
```
</TabItem>
<TabItem value="stop">

Stops a running streaming job. This will cause a running streaming job to stop processing input events and producing output.

```sql
EXEC azure.stream_analytics.streaming_jobs.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="scale">

Scales a streaming job when the job is running.

```sql
EXEC azure.stream_analytics.streaming_jobs.scale 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"streamingUnits": {{ streamingUnits }}
}'
;
```
</TabItem>
</Tabs>
