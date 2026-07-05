--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - databox
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databox.jobs" /></td></tr>
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
    <td>Id of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="allDevicesLost" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate if all devices associated with the job are lost.</td>
</tr>
<tr>
    <td><CopyableCode code="cancellationReason" /></td>
    <td><code>string</code></td>
    <td>Reason for cancellation.</td>
</tr>
<tr>
    <td><CopyableCode code="delayedStage" /></td>
    <td><code>string</code></td>
    <td>Name of the stage where delay might be present. Known values are: "DeviceOrdered", "DevicePrepared", "Dispatched", "Delivered", "PickedUp", "AtAzureDC", "DataCopy", "Completed", "CompletedWithErrors", "Cancelled", "Failed_IssueReportedAtCustomer", "Failed_IssueDetectedAtAzureDC", "Aborted", "CompletedWithWarnings", "ReadyToDispatchFromAzureDC", "ReadyToReceiveAtAzureDC", "Created", "ShippedToAzureDC", "AwaitingShipmentDetails", "PreparingToShipFromAzureDC", and "ShippedToCustomer".</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryInfo" /></td>
    <td><code>object</code></td>
    <td>Delivery Info of Job.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryType" /></td>
    <td><code>string</code></td>
    <td>Delivery type of Job. Known values are: "NonScheduled" and "Scheduled".</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Details of a job run. This field will only be sent for expand details filter.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Top level error for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Msi identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the job is cancellable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellableWithoutFee" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate cancellation of scheduled job.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeletable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the job is deletable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrepareToShipEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is Prepare To Ship Enabled on this job.</td>
</tr>
<tr>
    <td><CopyableCode code="isShippingAddressEditable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the shipping address is editable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="reverseShippingDetailsUpdate" /></td>
    <td><code>string</code></td>
    <td>The Editable status for Reverse Shipping Address and Contact Info. Known values are: "Enabled", "Disabled", and "NotSupported".</td>
</tr>
<tr>
    <td><CopyableCode code="reverseTransportPreferenceUpdate" /></td>
    <td><code>string</code></td>
    <td>The Editable status for Reverse Transport preferences. Known values are: "Enabled", "Disabled", and "NotSupported".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the job was started in UTC ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Name of the stage which is in progress. Known values are: "DeviceOrdered", "DevicePrepared", "Dispatched", "Delivered", "PickedUp", "AtAzureDC", "DataCopy", "Completed", "CompletedWithErrors", "Cancelled", "Failed_IssueReportedAtCustomer", "Failed_IssueDetectedAtAzureDC", "Aborted", "CompletedWithWarnings", "ReadyToDispatchFromAzureDC", "ReadyToReceiveAtAzureDC", "Created", "ShippedToAzureDC", "AwaitingShipmentDetails", "PreparingToShipFromAzureDC", and "ShippedToCustomer".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).</td>
</tr>
<tr>
    <td><CopyableCode code="transferType" /></td>
    <td><code>string</code></td>
    <td>Type of the data transfer. Required. Known values are: "ImportToAzure" and "ExportFromAzure".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the object.</td>
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
    <td>Id of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="allDevicesLost" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate if all devices associated with the job are lost.</td>
</tr>
<tr>
    <td><CopyableCode code="cancellationReason" /></td>
    <td><code>string</code></td>
    <td>Reason for cancellation.</td>
</tr>
<tr>
    <td><CopyableCode code="delayedStage" /></td>
    <td><code>string</code></td>
    <td>Name of the stage where delay might be present. Known values are: "DeviceOrdered", "DevicePrepared", "Dispatched", "Delivered", "PickedUp", "AtAzureDC", "DataCopy", "Completed", "CompletedWithErrors", "Cancelled", "Failed_IssueReportedAtCustomer", "Failed_IssueDetectedAtAzureDC", "Aborted", "CompletedWithWarnings", "ReadyToDispatchFromAzureDC", "ReadyToReceiveAtAzureDC", "Created", "ShippedToAzureDC", "AwaitingShipmentDetails", "PreparingToShipFromAzureDC", and "ShippedToCustomer".</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryInfo" /></td>
    <td><code>object</code></td>
    <td>Delivery Info of Job.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryType" /></td>
    <td><code>string</code></td>
    <td>Delivery type of Job. Known values are: "NonScheduled" and "Scheduled".</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Details of a job run. This field will only be sent for expand details filter.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Top level error for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Msi identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the job is cancellable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellableWithoutFee" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate cancellation of scheduled job.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeletable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the job is deletable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrepareToShipEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is Prepare To Ship Enabled on this job.</td>
</tr>
<tr>
    <td><CopyableCode code="isShippingAddressEditable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the shipping address is editable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="reverseShippingDetailsUpdate" /></td>
    <td><code>string</code></td>
    <td>The Editable status for Reverse Shipping Address and Contact Info. Known values are: "Enabled", "Disabled", and "NotSupported".</td>
</tr>
<tr>
    <td><CopyableCode code="reverseTransportPreferenceUpdate" /></td>
    <td><code>string</code></td>
    <td>The Editable status for Reverse Transport preferences. Known values are: "Enabled", "Disabled", and "NotSupported".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the job was started in UTC ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Name of the stage which is in progress. Known values are: "DeviceOrdered", "DevicePrepared", "Dispatched", "Delivered", "PickedUp", "AtAzureDC", "DataCopy", "Completed", "CompletedWithErrors", "Cancelled", "Failed_IssueReportedAtCustomer", "Failed_IssueDetectedAtAzureDC", "Aborted", "CompletedWithWarnings", "ReadyToDispatchFromAzureDC", "ReadyToReceiveAtAzureDC", "Created", "ShippedToAzureDC", "AwaitingShipmentDetails", "PreparingToShipFromAzureDC", and "ShippedToCustomer".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).</td>
</tr>
<tr>
    <td><CopyableCode code="transferType" /></td>
    <td><code>string</code></td>
    <td>Type of the data transfer. Required. Known values are: "ImportToAzure" and "ExportFromAzure".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the object.</td>
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
    <td>Id of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="allDevicesLost" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate if all devices associated with the job are lost.</td>
</tr>
<tr>
    <td><CopyableCode code="cancellationReason" /></td>
    <td><code>string</code></td>
    <td>Reason for cancellation.</td>
</tr>
<tr>
    <td><CopyableCode code="delayedStage" /></td>
    <td><code>string</code></td>
    <td>Name of the stage where delay might be present. Known values are: "DeviceOrdered", "DevicePrepared", "Dispatched", "Delivered", "PickedUp", "AtAzureDC", "DataCopy", "Completed", "CompletedWithErrors", "Cancelled", "Failed_IssueReportedAtCustomer", "Failed_IssueDetectedAtAzureDC", "Aborted", "CompletedWithWarnings", "ReadyToDispatchFromAzureDC", "ReadyToReceiveAtAzureDC", "Created", "ShippedToAzureDC", "AwaitingShipmentDetails", "PreparingToShipFromAzureDC", and "ShippedToCustomer".</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryInfo" /></td>
    <td><code>object</code></td>
    <td>Delivery Info of Job.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryType" /></td>
    <td><code>string</code></td>
    <td>Delivery type of Job. Known values are: "NonScheduled" and "Scheduled".</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Details of a job run. This field will only be sent for expand details filter.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Top level error for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Msi identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the job is cancellable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellableWithoutFee" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate cancellation of scheduled job.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeletable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the job is deletable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrepareToShipEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is Prepare To Ship Enabled on this job.</td>
</tr>
<tr>
    <td><CopyableCode code="isShippingAddressEditable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the shipping address is editable or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="reverseShippingDetailsUpdate" /></td>
    <td><code>string</code></td>
    <td>The Editable status for Reverse Shipping Address and Contact Info. Known values are: "Enabled", "Disabled", and "NotSupported".</td>
</tr>
<tr>
    <td><CopyableCode code="reverseTransportPreferenceUpdate" /></td>
    <td><code>string</code></td>
    <td>The Editable status for Reverse Transport preferences. Known values are: "Enabled", "Disabled", and "NotSupported".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the job was started in UTC ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Name of the stage which is in progress. Known values are: "DeviceOrdered", "DevicePrepared", "Dispatched", "Delivered", "PickedUp", "AtAzureDC", "DataCopy", "Completed", "CompletedWithErrors", "Cancelled", "Failed_IssueReportedAtCustomer", "Failed_IssueDetectedAtAzureDC", "Aborted", "CompletedWithWarnings", "ReadyToDispatchFromAzureDC", "ReadyToReceiveAtAzureDC", "Created", "ShippedToAzureDC", "AwaitingShipmentDetails", "PreparingToShipFromAzureDC", and "ShippedToCustomer".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).</td>
</tr>
<tr>
    <td><CopyableCode code="transferType" /></td>
    <td><code>string</code></td>
    <td>Type of the data transfer. Required. Known values are: "ImportToAzure" and "ExportFromAzure".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the object.</td>
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
    <td>Gets information about the specified job.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists all the jobs available under the given resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists all the jobs available under the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates the properties of an existing job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a job.</td>
</tr>
<tr>
    <td><a href="#list_credentials"><CopyableCode code="list_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This method gets the unencrypted secrets related to the job.</td>
</tr>
<tr>
    <td><a href="#mark_devices_shipped"><CopyableCode code="mark_devices_shipped" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-deliverToDcPackageDetails"><code>deliverToDcPackageDetails</code></a></td>
    <td></td>
    <td>Request to mark devices for a given job as shipped.</td>
</tr>
<tr>
    <td><a href="#book_shipment_pick_up"><CopyableCode code="book_shipment_pick_up" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-shipmentLocation"><code>shipmentLocation</code></a></td>
    <td></td>
    <td>Book shipment pick up.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-reason"><code>reason</code></a></td>
    <td></td>
    <td>CancelJob.</td>
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
    <td>The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The Resource Group Name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>$expand is supported on details parameter for job, which provides details on the job stages. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>$skipToken is supported on Get list of jobs, which provides the next page in the list of jobs. Default value is None.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value. Default value is None.</td>
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

Gets information about the specified job.

```sql
SELECT
id,
name,
allDevicesLost,
cancellationReason,
delayedStage,
deliveryInfo,
deliveryType,
details,
error,
identity,
isCancellable,
isCancellableWithoutFee,
isDeletable,
isPrepareToShipEnabled,
isShippingAddressEditable,
location,
reverseShippingDetailsUpdate,
reverseTransportPreferenceUpdate,
sku,
startTime,
status,
systemData,
tags,
transferType,
type
FROM azure.databox.jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the jobs available under the given resource group.

```sql
SELECT
id,
name,
allDevicesLost,
cancellationReason,
delayedStage,
deliveryInfo,
deliveryType,
details,
error,
identity,
isCancellable,
isCancellableWithoutFee,
isDeletable,
isPrepareToShipEnabled,
isShippingAddressEditable,
location,
reverseShippingDetailsUpdate,
reverseTransportPreferenceUpdate,
sku,
startTime,
status,
systemData,
tags,
transferType,
type
FROM azure.databox.jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list">

Lists all the jobs available under the subscription.

```sql
SELECT
id,
name,
allDevicesLost,
cancellationReason,
delayedStage,
deliveryInfo,
deliveryType,
details,
error,
identity,
isCancellable,
isCancellableWithoutFee,
isDeletable,
isPrepareToShipEnabled,
isShippingAddressEditable,
location,
reverseShippingDetailsUpdate,
reverseTransportPreferenceUpdate,
sku,
startTime,
status,
systemData,
tags,
transferType,
type
FROM azure.databox.jobs
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
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

Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.

```sql
INSERT INTO azure.databox.jobs (
location,
tags,
sku,
identity,
properties,
resource_group_name,
job_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ sku }}' /* required */,
'{{ identity }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ job_name }}',
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
- name: jobs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the jobs resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the jobs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the jobs resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).
    - name: sku
      description: |
        The sku type. Required.
      value:
        name: "{{ name }}"
        displayName: "{{ displayName }}"
        family: "{{ family }}"
        model: "{{ model }}"
    - name: identity
      description: |
        Msi identity of the resource.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        transferType: "{{ transferType }}"
        details:
          jobStages:
            - stageName: "{{ stageName }}"
              displayName: "{{ displayName }}"
              stageStatus: "{{ stageStatus }}"
              stageTime: "{{ stageTime }}"
              jobStageDetails: "{{ jobStageDetails }}"
              delayInformation: "{{ delayInformation }}"
          contactDetails:
            contactName: "{{ contactName }}"
            phone: "{{ phone }}"
            phoneExtension: "{{ phoneExtension }}"
            mobile: "{{ mobile }}"
            emailList:
              - "{{ emailList }}"
            notificationPreference:
              - stageName: "{{ stageName }}"
                sendNotification: {{ sendNotification }}
          shippingAddress:
            streetAddress1: "{{ streetAddress1 }}"
            streetAddress2: "{{ streetAddress2 }}"
            streetAddress3: "{{ streetAddress3 }}"
            city: "{{ city }}"
            stateOrProvince: "{{ stateOrProvince }}"
            country: "{{ country }}"
            postalCode: "{{ postalCode }}"
            zipExtendedCode: "{{ zipExtendedCode }}"
            companyName: "{{ companyName }}"
            addressType: "{{ addressType }}"
            skipAddressValidation: {{ skipAddressValidation }}
            taxIdentificationNumber: "{{ taxIdentificationNumber }}"
          deliveryPackage:
            trackingUrl: "{{ trackingUrl }}"
            carrierName: "{{ carrierName }}"
            trackingId: "{{ trackingId }}"
          returnPackage:
            trackingUrl: "{{ trackingUrl }}"
            carrierName: "{{ carrierName }}"
            trackingId: "{{ trackingId }}"
          dataImportDetails:
            - accountDetails:
                dataAccountType: "{{ dataAccountType }}"
                sharePassword: "{{ sharePassword }}"
              logCollectionLevel: "{{ logCollectionLevel }}"
          dataExportDetails:
            - transferConfiguration:
                transferConfigurationType: "{{ transferConfigurationType }}"
                transferFilterDetails:
                  include: "{{ include }}"
                transferAllDetails:
                  include: "{{ include }}"
              logCollectionLevel: "{{ logCollectionLevel }}"
              accountDetails:
                dataAccountType: "{{ dataAccountType }}"
                sharePassword: "{{ sharePassword }}"
          jobDetailsType: "{{ jobDetailsType }}"
          preferences:
            preferredDataCenterRegion:
              - "{{ preferredDataCenterRegion }}"
            transportPreferences:
              preferredShipmentType: "{{ preferredShipmentType }}"
              isUpdated: {{ isUpdated }}
            reverseTransportPreferences:
              preferredShipmentType: "{{ preferredShipmentType }}"
              isUpdated: {{ isUpdated }}
            encryptionPreferences:
              doubleEncryption: "{{ doubleEncryption }}"
              hardwareEncryption: "{{ hardwareEncryption }}"
            storageAccountAccessTierPreferences:
              - "{{ storageAccountAccessTierPreferences }}"
          reverseShippingDetails:
            contactDetails:
              contactName: "{{ contactName }}"
              phone: "{{ phone }}"
              phoneExtension: "{{ phoneExtension }}"
              mobile: "{{ mobile }}"
            shippingAddress:
              streetAddress1: "{{ streetAddress1 }}"
              streetAddress2: "{{ streetAddress2 }}"
              streetAddress3: "{{ streetAddress3 }}"
              city: "{{ city }}"
              stateOrProvince: "{{ stateOrProvince }}"
              country: "{{ country }}"
              postalCode: "{{ postalCode }}"
              zipExtendedCode: "{{ zipExtendedCode }}"
              companyName: "{{ companyName }}"
              addressType: "{{ addressType }}"
              skipAddressValidation: {{ skipAddressValidation }}
              taxIdentificationNumber: "{{ taxIdentificationNumber }}"
            isUpdated: {{ isUpdated }}
          copyLogDetails:
            - copyLogDetailsType: "{{ copyLogDetailsType }}"
          reverseShipmentLabelSasKey: "{{ reverseShipmentLabelSasKey }}"
          chainOfCustodySasKey: "{{ chainOfCustodySasKey }}"
          deviceErasureDetails:
            deviceErasureStatus: "{{ deviceErasureStatus }}"
            erasureOrDestructionCertificateSasKey: "{{ erasureOrDestructionCertificateSasKey }}"
          keyEncryptionKey:
            kekType: "{{ kekType }}"
            identityProperties:
              type: "{{ type }}"
              userAssigned:
                resourceId: "{{ resourceId }}"
            kekUrl: "{{ kekUrl }}"
            kekVaultResourceID: "{{ kekVaultResourceID }}"
          expectedDataSizeInTeraBytes: {{ expectedDataSizeInTeraBytes }}
          actions:
            - "{{ actions }}"
          lastMitigationActionOnJob:
            actionDateTimeInUtc: "{{ actionDateTimeInUtc }}"
            isPerformedByCustomer: {{ isPerformedByCustomer }}
            customerResolution: "{{ customerResolution }}"
          datacenterAddress:
            datacenterAddressType: "{{ datacenterAddressType }}"
            supportedCarriersForReturnShipment:
              - "{{ supportedCarriersForReturnShipment }}"
            dataCenterAzureLocation: "{{ dataCenterAzureLocation }}"
          dataCenterCode: "{{ dataCenterCode }}"
        deliveryType: "{{ deliveryType }}"
        deliveryInfo:
          scheduledDateTime: "{{ scheduledDateTime }}"
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

Updates the properties of an existing job.

```sql
UPDATE azure.databox.jobs
SET 
tags = '{{ tags }}',
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

Deletes a job.

```sql
DELETE FROM azure.databox.jobs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_credentials"
    values={[
        { label: 'list_credentials', value: 'list_credentials' },
        { label: 'mark_devices_shipped', value: 'mark_devices_shipped' },
        { label: 'book_shipment_pick_up', value: 'book_shipment_pick_up' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="list_credentials">

This method gets the unencrypted secrets related to the job.

```sql
EXEC azure.databox.jobs.list_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="mark_devices_shipped">

Request to mark devices for a given job as shipped.

```sql
EXEC azure.databox.jobs.mark_devices_shipped 
@job_name='{{ job_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"deliverToDcPackageDetails": "{{ deliverToDcPackageDetails }}"
}'
;
```
</TabItem>
<TabItem value="book_shipment_pick_up">

Book shipment pick up.

```sql
EXEC azure.databox.jobs.book_shipment_pick_up 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startTime": "{{ startTime }}", 
"endTime": "{{ endTime }}", 
"shipmentLocation": "{{ shipmentLocation }}"
}'
;
```
</TabItem>
<TabItem value="cancel">

CancelJob.

```sql
EXEC azure.databox.jobs.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"reason": "{{ reason }}"
}'
;
```
</TabItem>
</Tabs>
