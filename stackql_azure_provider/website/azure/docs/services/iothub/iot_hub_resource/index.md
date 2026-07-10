--- 
title: iot_hub_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_hub_resource
  - iothub
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

Creates, updates, deletes, gets or lists an <code>iot_hub_resource</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iot_hub_resource" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iothub.iot_hub_resource" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_event_hub_consumer_group"
    values={[
        { label: 'get_event_hub_consumer_group', value: 'get_event_hub_consumer_group' },
        { label: 'list_event_hub_consumer_groups', value: 'list_event_hub_consumer_groups' },
        { label: 'get_job', value: 'get_job' },
        { label: 'get_keys_for_key_name', value: 'get_keys_for_key_name' },
        { label: 'get', value: 'get' },
        { label: 'get_endpoint_health', value: 'get_endpoint_health' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_event_hub_consumer_group">

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
    <td>The etag.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The tags.</td>
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
<TabItem value="list_event_hub_consumer_groups">

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
    <td>The etag.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The tags.</td>
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
<TabItem value="get_job">

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
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the job stopped processing.</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>If status == failed, this string containing the reason for the failure.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>The job identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="parentJobId" /></td>
    <td><code>string</code></td>
    <td>The job identifier of the parent job, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the job. Known values are: "unknown", "enqueued", "running", "completed", "failed", and "cancelled". (unknown, enqueued, running, completed, failed, cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The status message for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the job. Known values are: "unknown", "export", "import", "backup", "readDeviceProperties", "writeDeviceProperties", "updateDeviceConfiguration", "rebootDevice", "factoryResetDevice", and "firmwareUpdate". (unknown, export, import, backup, readDeviceProperties, writeDeviceProperties, updateDeviceConfiguration, rebootDevice, factoryResetDevice, firmwareUpdate)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_keys_for_key_name">

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
    <td><CopyableCode code="keyName" /></td>
    <td><code>string</code></td>
    <td>The name of the shared access policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryKey" /></td>
    <td><code>string</code></td>
    <td>The primary key.</td>
</tr>
<tr>
    <td><CopyableCode code="rights" /></td>
    <td><code>string</code></td>
    <td>The permissions assigned to the shared access policy. Required. Known values are: "RegistryRead", "RegistryWrite", "ServiceConnect", "DeviceConnect", "RegistryRead, RegistryWrite", "RegistryRead, ServiceConnect", "RegistryRead, DeviceConnect", "RegistryWrite, ServiceConnect", "RegistryWrite, DeviceConnect", "ServiceConnect, DeviceConnect", "RegistryRead, RegistryWrite, ServiceConnect", "RegistryRead, RegistryWrite, DeviceConnect", "RegistryRead, ServiceConnect, DeviceConnect", "RegistryWrite, ServiceConnect, DeviceConnect", and "RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect". (RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect, RegistryRead, RegistryWrite, RegistryRead, ServiceConnect, RegistryRead, DeviceConnect, RegistryWrite, ServiceConnect, RegistryWrite, DeviceConnect, ServiceConnect, DeviceConnect, RegistryRead, RegistryWrite, ServiceConnect, RegistryRead, RegistryWrite, DeviceConnect, RegistryRead, ServiceConnect, DeviceConnect, RegistryWrite, ServiceConnect, DeviceConnect, RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryKey" /></td>
    <td><code>string</code></td>
    <td>The secondary key.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>List of allowed FQDNs(Fully Qualified Domain Name) for egress from Iot Hub.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>array</code></td>
    <td>The shared access policies you can use to secure a connection to the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudToDevice" /></td>
    <td><code>object</code></td>
    <td>The IoT hub cloud-to-device messaging properties.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>IoT hub comments.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceHostName" /></td>
    <td><code>string</code></td>
    <td>The name of the device host. Supports secure connections over TLS 1.3.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRegistry" /></td>
    <td><code>object</code></td>
    <td>Represents properties related to the Azure Device Registry (ADR).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceStreams" /></td>
    <td><code>object</code></td>
    <td>The device streams properties of iothub.</td>
</tr>
<tr>
    <td><CopyableCode code="disableDeviceSAS" /></td>
    <td><code>boolean</code></td>
    <td>If true, all device(including Edge devices but excluding modules) scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>If true, SAS tokens with Iot hub scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="disableModuleSAS" /></td>
    <td><code>boolean</code></td>
    <td>If true, all module scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDataResidency" /></td>
    <td><code>boolean</code></td>
    <td>This property when set to true, will enable data residency, thus, disabling disaster recovery.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFileUploadNotifications" /></td>
    <td><code>boolean</code></td>
    <td>If True, file upload notifications are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubEndpoints" /></td>
    <td><code>object</code></td>
    <td>The Event Hub-compatible endpoint properties. The only possible keys to this dictionary is events. This key has to be present in the dictionary while making create or update calls for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>string</code></td>
    <td>The capabilities and features enabled for the IoT hub. Known values are: "None" and "DeviceManagement". (None, DeviceManagement)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The name of the host.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identities for the IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubDetails" /></td>
    <td><code>object</code></td>
    <td>Set of additional read-only properties for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="ipFilterRules" /></td>
    <td><code>array</code></td>
    <td>The IP filter rules.</td>
</tr>
<tr>
    <td><CopyableCode code="ipVersion" /></td>
    <td><code>string</code></td>
    <td>This property specifies the IP Version the hub is currently utilizing. Known values are: "ipv4", "ipv6", and "ipv4ipv6". (ipv4, ipv6, ipv4ipv6)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>Primary and secondary location for iot hub.</td>
</tr>
<tr>
    <td><CopyableCode code="messagingEndpoints" /></td>
    <td><code>object</code></td>
    <td>The messaging endpoint properties for the file upload notification queue.</td>
</tr>
<tr>
    <td><CopyableCode code="minTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Specifies the minimum TLS version to support for this hub. Can be set to "1.2" to have clients that use a TLS version below 1.2 to be rejected.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleSets" /></td>
    <td><code>object</code></td>
    <td>Network Rule Set Properties of IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on this IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>If true, egress from IotHub will be restricted to only the allowed FQDNs that are configured via allowedFqdnList.</td>
</tr>
<tr>
    <td><CopyableCode code="rootCertificate" /></td>
    <td><code>object</code></td>
    <td>This property store root certificate related information.</td>
</tr>
<tr>
    <td><CopyableCode code="routing" /></td>
    <td><code>object</code></td>
    <td>The routing related properties of the IoT hub. See: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging `_.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceHostName" /></td>
    <td><code>string</code></td>
    <td>The name of the service host. Supports secure connections over TLS 1.3.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>IotHub SKU info. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The hub state.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoints" /></td>
    <td><code>object</code></td>
    <td>The list of Azure Storage endpoints where you can upload files. Currently you can configure only one Azure Storage account and that MUST have its key as $default. Specifying more than one storage account causes an error to be thrown. Not specifying a value for this property when the enableFileUploadNotifications property is set to True, causes an error to be thrown.</td>
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
<TabItem value="get_endpoint_health">

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
    <td><CopyableCode code="endpointId" /></td>
    <td><code>string</code></td>
    <td>Id of the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Health statuses have following meanings. The 'healthy' status shows that the endpoint is accepting messages as expected. The 'unhealthy' status shows that the endpoint is not accepting messages as expected and IoT Hub is retrying to send data to this endpoint. The status of an unhealthy endpoint will be updated to healthy when IoT Hub has established an eventually consistent state of health. The 'dead' status shows that the endpoint is not accepting messages, after IoT Hub retried sending messages for the retrial period. See IoT Hub metrics to identify errors and monitor issues with endpoints. The 'unknown' status shows that the IoT Hub has not established a connection with the endpoint. No messages have been delivered to or rejected from this endpoint. Known values are: "unknown", "healthy", "degraded", "unhealthy", and "dead". (unknown, healthy, degraded, unhealthy, dead)</td>
</tr>
<tr>
    <td><CopyableCode code="lastKnownError" /></td>
    <td><code>string</code></td>
    <td>Last error obtained when a message failed to be delivered to iot hub.</td>
</tr>
<tr>
    <td><CopyableCode code="lastKnownErrorTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the last known error occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSendAttemptTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time iot hub tried to send a message to the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulSendAttemptTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time iot hub successfully sent a message to the endpoint.</td>
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
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>List of allowed FQDNs(Fully Qualified Domain Name) for egress from Iot Hub.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>array</code></td>
    <td>The shared access policies you can use to secure a connection to the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudToDevice" /></td>
    <td><code>object</code></td>
    <td>The IoT hub cloud-to-device messaging properties.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>IoT hub comments.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceHostName" /></td>
    <td><code>string</code></td>
    <td>The name of the device host. Supports secure connections over TLS 1.3.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRegistry" /></td>
    <td><code>object</code></td>
    <td>Represents properties related to the Azure Device Registry (ADR).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceStreams" /></td>
    <td><code>object</code></td>
    <td>The device streams properties of iothub.</td>
</tr>
<tr>
    <td><CopyableCode code="disableDeviceSAS" /></td>
    <td><code>boolean</code></td>
    <td>If true, all device(including Edge devices but excluding modules) scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>If true, SAS tokens with Iot hub scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="disableModuleSAS" /></td>
    <td><code>boolean</code></td>
    <td>If true, all module scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDataResidency" /></td>
    <td><code>boolean</code></td>
    <td>This property when set to true, will enable data residency, thus, disabling disaster recovery.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFileUploadNotifications" /></td>
    <td><code>boolean</code></td>
    <td>If True, file upload notifications are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubEndpoints" /></td>
    <td><code>object</code></td>
    <td>The Event Hub-compatible endpoint properties. The only possible keys to this dictionary is events. This key has to be present in the dictionary while making create or update calls for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>string</code></td>
    <td>The capabilities and features enabled for the IoT hub. Known values are: "None" and "DeviceManagement". (None, DeviceManagement)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The name of the host.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identities for the IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubDetails" /></td>
    <td><code>object</code></td>
    <td>Set of additional read-only properties for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="ipFilterRules" /></td>
    <td><code>array</code></td>
    <td>The IP filter rules.</td>
</tr>
<tr>
    <td><CopyableCode code="ipVersion" /></td>
    <td><code>string</code></td>
    <td>This property specifies the IP Version the hub is currently utilizing. Known values are: "ipv4", "ipv6", and "ipv4ipv6". (ipv4, ipv6, ipv4ipv6)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>Primary and secondary location for iot hub.</td>
</tr>
<tr>
    <td><CopyableCode code="messagingEndpoints" /></td>
    <td><code>object</code></td>
    <td>The messaging endpoint properties for the file upload notification queue.</td>
</tr>
<tr>
    <td><CopyableCode code="minTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Specifies the minimum TLS version to support for this hub. Can be set to "1.2" to have clients that use a TLS version below 1.2 to be rejected.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleSets" /></td>
    <td><code>object</code></td>
    <td>Network Rule Set Properties of IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on this IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>If true, egress from IotHub will be restricted to only the allowed FQDNs that are configured via allowedFqdnList.</td>
</tr>
<tr>
    <td><CopyableCode code="rootCertificate" /></td>
    <td><code>object</code></td>
    <td>This property store root certificate related information.</td>
</tr>
<tr>
    <td><CopyableCode code="routing" /></td>
    <td><code>object</code></td>
    <td>The routing related properties of the IoT hub. See: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging `_.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceHostName" /></td>
    <td><code>string</code></td>
    <td>The name of the service host. Supports secure connections over TLS 1.3.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>IotHub SKU info. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The hub state.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoints" /></td>
    <td><code>object</code></td>
    <td>The list of Azure Storage endpoints where you can upload files. Currently you can configure only one Azure Storage account and that MUST have its key as $default. Specifying more than one storage account causes an error to be thrown. Not specifying a value for this property when the enableFileUploadNotifications property is set to True, causes an error to be thrown.</td>
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
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>The detailed reason message.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>The value which indicates whether the provided name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for unavailability. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
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
    <td><CopyableCode code="allowedFqdnList" /></td>
    <td><code>array</code></td>
    <td>List of allowed FQDNs(Fully Qualified Domain Name) for egress from Iot Hub.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>array</code></td>
    <td>The shared access policies you can use to secure a connection to the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudToDevice" /></td>
    <td><code>object</code></td>
    <td>The IoT hub cloud-to-device messaging properties.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>IoT hub comments.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceHostName" /></td>
    <td><code>string</code></td>
    <td>The name of the device host. Supports secure connections over TLS 1.3.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRegistry" /></td>
    <td><code>object</code></td>
    <td>Represents properties related to the Azure Device Registry (ADR).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceStreams" /></td>
    <td><code>object</code></td>
    <td>The device streams properties of iothub.</td>
</tr>
<tr>
    <td><CopyableCode code="disableDeviceSAS" /></td>
    <td><code>boolean</code></td>
    <td>If true, all device(including Edge devices but excluding modules) scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>If true, SAS tokens with Iot hub scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="disableModuleSAS" /></td>
    <td><code>boolean</code></td>
    <td>If true, all module scoped SAS keys cannot be used for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDataResidency" /></td>
    <td><code>boolean</code></td>
    <td>This property when set to true, will enable data residency, thus, disabling disaster recovery.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFileUploadNotifications" /></td>
    <td><code>boolean</code></td>
    <td>If True, file upload notifications are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="eventHubEndpoints" /></td>
    <td><code>object</code></td>
    <td>The Event Hub-compatible endpoint properties. The only possible keys to this dictionary is events. This key has to be present in the dictionary while making create or update calls for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>string</code></td>
    <td>The capabilities and features enabled for the IoT hub. Known values are: "None" and "DeviceManagement". (None, DeviceManagement)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The name of the host.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identities for the IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubDetails" /></td>
    <td><code>object</code></td>
    <td>Set of additional read-only properties for the IoT hub.</td>
</tr>
<tr>
    <td><CopyableCode code="ipFilterRules" /></td>
    <td><code>array</code></td>
    <td>The IP filter rules.</td>
</tr>
<tr>
    <td><CopyableCode code="ipVersion" /></td>
    <td><code>string</code></td>
    <td>This property specifies the IP Version the hub is currently utilizing. Known values are: "ipv4", "ipv6", and "ipv4ipv6". (ipv4, ipv6, ipv4ipv6)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>Primary and secondary location for iot hub.</td>
</tr>
<tr>
    <td><CopyableCode code="messagingEndpoints" /></td>
    <td><code>object</code></td>
    <td>The messaging endpoint properties for the file upload notification queue.</td>
</tr>
<tr>
    <td><CopyableCode code="minTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Specifies the minimum TLS version to support for this hub. Can be set to "1.2" to have clients that use a TLS version below 1.2 to be rejected.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRuleSets" /></td>
    <td><code>object</code></td>
    <td>Network Rule Set Properties of IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on this IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>If true, egress from IotHub will be restricted to only the allowed FQDNs that are configured via allowedFqdnList.</td>
</tr>
<tr>
    <td><CopyableCode code="rootCertificate" /></td>
    <td><code>object</code></td>
    <td>This property store root certificate related information.</td>
</tr>
<tr>
    <td><CopyableCode code="routing" /></td>
    <td><code>object</code></td>
    <td>The routing related properties of the IoT hub. See: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging `_.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceHostName" /></td>
    <td><code>string</code></td>
    <td>The name of the service host. Supports secure connections over TLS 1.3.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>IotHub SKU info. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The hub state.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoints" /></td>
    <td><code>object</code></td>
    <td>The list of Azure Storage endpoints where you can upload files. Currently you can configure only one Azure Storage account and that MUST have its key as $default. Specifying more than one storage account causes an error to be thrown. Not specifying a value for this property when the enableFileUploadNotifications property is set to True, causes an error to be thrown.</td>
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
    <td><a href="#get_event_hub_consumer_group"><CopyableCode code="get_event_hub_consumer_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-event_hub_endpoint_name"><code>event_hub_endpoint_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub. Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.</td>
</tr>
<tr>
    <td><a href="#list_event_hub_consumer_groups"><CopyableCode code="list_event_hub_consumer_groups" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-event_hub_endpoint_name"><code>event_hub_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub. Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.</td>
</tr>
<tr>
    <td><a href="#get_job"><CopyableCode code="get_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the details of a job from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_. Get the details of a job from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_.</td>
</tr>
<tr>
    <td><a href="#get_keys_for_key_name"><CopyableCode code="get_keys_for_key_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a shared access policy by name from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_. Get a shared access policy by name from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the non-security related metadata of an IoT hub. Get the non-security related metadata of an IoT hub.</td>
</tr>
<tr>
    <td><a href="#get_endpoint_health"><CopyableCode code="get_endpoint_health" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iot_hub_name"><code>iot_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the health for routing endpoints. Get the health for routing endpoints.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all the IoT hubs in a resource group. Get all the IoT hubs in a resource group.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check if an IoT hub name is available. Check if an IoT hub name is available.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all the IoT hubs in a subscription. Get all the IoT hubs in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update the metadata of an IoT hub. Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing IoT Hubs tags. Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update the metadata of an IoT hub. Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an IoT hub. Delete an IoT hub.</td>
</tr>
<tr>
    <td><a href="#list_jobs"><CopyableCode code="list_jobs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of all the jobs in an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_. Get a list of all the jobs in an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the security metadata for an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_. Get the security metadata for an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_.</td>
</tr>
<tr>
    <td><a href="#get_valid_skus"><CopyableCode code="get_valid_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the list of valid SKUs for an IoT hub. Get the list of valid SKUs for an IoT hub.</td>
</tr>
<tr>
    <td><a href="#get_quota_metrics"><CopyableCode code="get_quota_metrics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the quota metrics for an IoT hub. Get the quota metrics for an IoT hub.</td>
</tr>
<tr>
    <td><a href="#get_stats"><CopyableCode code="get_stats" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the statistics from an IoT hub. Get the statistics from an IoT hub.</td>
</tr>
<tr>
    <td><a href="#create_event_hub_consumer_group"><CopyableCode code="create_event_hub_consumer_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-event_hub_endpoint_name"><code>event_hub_endpoint_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Add a consumer group to an Event Hub-compatible endpoint in an IoT hub. Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.</td>
</tr>
<tr>
    <td><a href="#delete_event_hub_consumer_group"><CopyableCode code="delete_event_hub_consumer_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-event_hub_endpoint_name"><code>event_hub_endpoint_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub. Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.</td>
</tr>
<tr>
    <td><a href="#test_all_routes"><CopyableCode code="test_all_routes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-iot_hub_name"><code>iot_hub_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Test all routes. Test all routes configured in this Iot Hub.</td>
</tr>
<tr>
    <td><a href="#test_route"><CopyableCode code="test_route" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-iot_hub_name"><code>iot_hub_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-route"><code>route</code></a></td>
    <td></td>
    <td>Test the new route. Test the new route for this Iot Hub.</td>
</tr>
<tr>
    <td><a href="#export_devices"><CopyableCode code="export_devices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-exportBlobContainerUri"><code>exportBlobContainerUri</code></a>, <a href="#parameter-excludeKeys"><code>excludeKeys</code></a></td>
    <td></td>
    <td>Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_. Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_.</td>
</tr>
<tr>
    <td><a href="#import_devices"><CopyableCode code="import_devices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-inputBlobContainerUri"><code>inputBlobContainerUri</code></a>, <a href="#parameter-outputBlobContainerUri"><code>outputBlobContainerUri</code></a></td>
    <td></td>
    <td>Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_. Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_.</td>
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
<tr id="parameter-event_hub_endpoint_name">
    <td><CopyableCode code="event_hub_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the EventHubEndpoint. Required.</td>
</tr>
<tr id="parameter-iot_hub_name">
    <td><CopyableCode code="iot_hub_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job identifier. Required.</td>
</tr>
<tr id="parameter-key_name">
    <td><CopyableCode code="key_name" /></td>
    <td><code>string</code></td>
    <td>The name of the shared access policy. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the consumer group to retrieve. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the IoT hub. Required.</td>
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
    defaultValue="get_event_hub_consumer_group"
    values={[
        { label: 'get_event_hub_consumer_group', value: 'get_event_hub_consumer_group' },
        { label: 'list_event_hub_consumer_groups', value: 'list_event_hub_consumer_groups' },
        { label: 'get_job', value: 'get_job' },
        { label: 'get_keys_for_key_name', value: 'get_keys_for_key_name' },
        { label: 'get', value: 'get' },
        { label: 'get_endpoint_health', value: 'get_endpoint_health' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_event_hub_consumer_group">

Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub. Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.

```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND event_hub_endpoint_name = '{{ event_hub_endpoint_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_event_hub_consumer_groups">

Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub. Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.

```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND event_hub_endpoint_name = '{{ event_hub_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_job">

Get the details of a job from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_. Get the details of a job from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_.

```sql
SELECT
endTimeUtc,
failureReason,
jobId,
parentJobId,
startTimeUtc,
status,
statusMessage,
type
FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND job_id = '{{ job_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_keys_for_key_name">

Get a shared access policy by name from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_. Get a shared access policy by name from an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_.

```sql
SELECT
keyName,
primaryKey,
rights,
secondaryKey
FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND key_name = '{{ key_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the non-security related metadata of an IoT hub. Get the non-security related metadata of an IoT hub.

```sql
SELECT
id,
name,
allowedFqdnList,
authorizationPolicies,
cloudToDevice,
comments,
deviceHostName,
deviceRegistry,
deviceStreams,
disableDeviceSAS,
disableLocalAuth,
disableModuleSAS,
enableDataResidency,
enableFileUploadNotifications,
encryption,
etag,
eventHubEndpoints,
features,
hostName,
identity,
iotHubDetails,
ipFilterRules,
ipVersion,
location,
locations,
messagingEndpoints,
minTlsVersion,
networkRuleSets,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
restrictOutboundNetworkAccess,
rootCertificate,
routing,
serviceHostName,
sku,
state,
storageEndpoints,
systemData,
tags,
type
FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_endpoint_health">

Get the health for routing endpoints. Get the health for routing endpoints.

```sql
SELECT
endpointId,
healthStatus,
lastKnownError,
lastKnownErrorTime,
lastSendAttemptTime,
lastSuccessfulSendAttemptTime
FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND iot_hub_name = '{{ iot_hub_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all the IoT hubs in a resource group. Get all the IoT hubs in a resource group.

```sql
SELECT
id,
name,
allowedFqdnList,
authorizationPolicies,
cloudToDevice,
comments,
deviceHostName,
deviceRegistry,
deviceStreams,
disableDeviceSAS,
disableLocalAuth,
disableModuleSAS,
enableDataResidency,
enableFileUploadNotifications,
encryption,
etag,
eventHubEndpoints,
features,
hostName,
identity,
iotHubDetails,
ipFilterRules,
ipVersion,
location,
locations,
messagingEndpoints,
minTlsVersion,
networkRuleSets,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
restrictOutboundNetworkAccess,
rootCertificate,
routing,
serviceHostName,
sku,
state,
storageEndpoints,
systemData,
tags,
type
FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Check if an IoT hub name is available. Check if an IoT hub name is available.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.iothub.iot_hub_resource
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get all the IoT hubs in a subscription. Get all the IoT hubs in a subscription.

```sql
SELECT
id,
name,
allowedFqdnList,
authorizationPolicies,
cloudToDevice,
comments,
deviceHostName,
deviceRegistry,
deviceStreams,
disableDeviceSAS,
disableLocalAuth,
disableModuleSAS,
enableDataResidency,
enableFileUploadNotifications,
encryption,
etag,
eventHubEndpoints,
features,
hostName,
identity,
iotHubDetails,
ipFilterRules,
ipVersion,
location,
locations,
messagingEndpoints,
minTlsVersion,
networkRuleSets,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
restrictOutboundNetworkAccess,
rootCertificate,
routing,
serviceHostName,
sku,
state,
storageEndpoints,
systemData,
tags,
type
FROM azure.iothub.iot_hub_resource
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

Create or update the metadata of an IoT hub. Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub.

```sql
INSERT INTO azure.iothub.iot_hub_resource (
tags,
location,
properties,
etag,
sku,
identity,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ etag }}',
'{{ sku }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: iot_hub_resource
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the iot_hub_resource resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the iot_hub_resource resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the iot_hub_resource resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        IotHub properties.
      value:
        authorizationPolicies:
          - keyName: "{{ keyName }}"
            primaryKey: "{{ primaryKey }}"
            secondaryKey: "{{ secondaryKey }}"
            rights: "{{ rights }}"
        disableLocalAuth: {{ disableLocalAuth }}
        disableDeviceSAS: {{ disableDeviceSAS }}
        disableModuleSAS: {{ disableModuleSAS }}
        restrictOutboundNetworkAccess: {{ restrictOutboundNetworkAccess }}
        allowedFqdnList:
          - "{{ allowedFqdnList }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        ipFilterRules:
          - filterName: "{{ filterName }}"
            action: "{{ action }}"
            ipMask: "{{ ipMask }}"
        networkRuleSets:
          defaultAction: "{{ defaultAction }}"
          applyToBuiltInEventHubEndpoint: {{ applyToBuiltInEventHubEndpoint }}
          ipRules:
            - filterName: "{{ filterName }}"
              action: "{{ action }}"
              ipMask: "{{ ipMask }}"
        minTlsVersion: "{{ minTlsVersion }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
        provisioningState: "{{ provisioningState }}"
        state: "{{ state }}"
        hostName: "{{ hostName }}"
        deviceHostName: "{{ deviceHostName }}"
        serviceHostName: "{{ serviceHostName }}"
        eventHubEndpoints: "{{ eventHubEndpoints }}"
        routing:
          endpoints:
            serviceBusQueues:
              - id: "{{ id }}"
                connectionString: "{{ connectionString }}"
                endpointUri: "{{ endpointUri }}"
                entityPath: "{{ entityPath }}"
                authenticationType: "{{ authenticationType }}"
                identity:
                  userAssignedIdentity: "{{ userAssignedIdentity }}"
                name: "{{ name }}"
                subscriptionId: "{{ subscriptionId }}"
                resourceGroup: "{{ resourceGroup }}"
            serviceBusTopics:
              - id: "{{ id }}"
                connectionString: "{{ connectionString }}"
                endpointUri: "{{ endpointUri }}"
                entityPath: "{{ entityPath }}"
                authenticationType: "{{ authenticationType }}"
                identity:
                  userAssignedIdentity: "{{ userAssignedIdentity }}"
                name: "{{ name }}"
                subscriptionId: "{{ subscriptionId }}"
                resourceGroup: "{{ resourceGroup }}"
            eventHubs:
              - id: "{{ id }}"
                connectionString: "{{ connectionString }}"
                endpointUri: "{{ endpointUri }}"
                entityPath: "{{ entityPath }}"
                authenticationType: "{{ authenticationType }}"
                identity:
                  userAssignedIdentity: "{{ userAssignedIdentity }}"
                name: "{{ name }}"
                subscriptionId: "{{ subscriptionId }}"
                resourceGroup: "{{ resourceGroup }}"
            storageContainers:
              - id: "{{ id }}"
                connectionString: "{{ connectionString }}"
                endpointUri: "{{ endpointUri }}"
                authenticationType: "{{ authenticationType }}"
                identity:
                  userAssignedIdentity: "{{ userAssignedIdentity }}"
                name: "{{ name }}"
                subscriptionId: "{{ subscriptionId }}"
                resourceGroup: "{{ resourceGroup }}"
                containerName: "{{ containerName }}"
                fileNameFormat: "{{ fileNameFormat }}"
                batchFrequencyInSeconds: {{ batchFrequencyInSeconds }}
                maxChunkSizeInBytes: {{ maxChunkSizeInBytes }}
                encoding: "{{ encoding }}"
            cosmosDBSqlContainers:
              - name: "{{ name }}"
                id: "{{ id }}"
                subscriptionId: "{{ subscriptionId }}"
                resourceGroup: "{{ resourceGroup }}"
                endpointUri: "{{ endpointUri }}"
                authenticationType: "{{ authenticationType }}"
                identity:
                  userAssignedIdentity: "{{ userAssignedIdentity }}"
                primaryKey: "{{ primaryKey }}"
                secondaryKey: "{{ secondaryKey }}"
                databaseName: "{{ databaseName }}"
                containerName: "{{ containerName }}"
                partitionKeyName: "{{ partitionKeyName }}"
                partitionKeyTemplate: "{{ partitionKeyTemplate }}"
          routes:
            - name: "{{ name }}"
              source: "{{ source }}"
              condition: "{{ condition }}"
              endpointNames: "{{ endpointNames }}"
              isEnabled: {{ isEnabled }}
          fallbackRoute:
            name: "{{ name }}"
            source: "{{ source }}"
            condition: "{{ condition }}"
            endpointNames:
              - "{{ endpointNames }}"
            isEnabled: {{ isEnabled }}
          enrichments:
            - key: "{{ key }}"
              value: "{{ value }}"
              endpointNames: "{{ endpointNames }}"
        storageEndpoints: "{{ storageEndpoints }}"
        messagingEndpoints: "{{ messagingEndpoints }}"
        enableFileUploadNotifications: {{ enableFileUploadNotifications }}
        cloudToDevice:
          maxDeliveryCount: {{ maxDeliveryCount }}
          defaultTtlAsIso8601: "{{ defaultTtlAsIso8601 }}"
          feedback:
            lockDurationAsIso8601: "{{ lockDurationAsIso8601 }}"
            ttlAsIso8601: "{{ ttlAsIso8601 }}"
            maxDeliveryCount: {{ maxDeliveryCount }}
        comments: "{{ comments }}"
        deviceStreams:
          streamingEndpoints:
            - "{{ streamingEndpoints }}"
        features: "{{ features }}"
        encryption:
          keySource: "{{ keySource }}"
          keyVaultProperties:
            - keyIdentifier: "{{ keyIdentifier }}"
              identity:
                userAssignedIdentity: "{{ userAssignedIdentity }}"
        locations:
          - location: "{{ location }}"
            role: "{{ role }}"
        enableDataResidency: {{ enableDataResidency }}
        rootCertificate:
          enableRootCertificateV2: {{ enableRootCertificateV2 }}
          lastUpdatedTimeUtc: "{{ lastUpdatedTimeUtc }}"
        ipVersion: "{{ ipVersion }}"
        deviceRegistry:
          namespaceResourceId: "{{ namespaceResourceId }}"
          identityResourceId: "{{ identityResourceId }}"
        iotHubDetails:
          gatewayVersion: "{{ gatewayVersion }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
    - name: sku
      description: |
        IotHub SKU info. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        The managed identities for the IotHub.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update an existing IoT Hubs tags. Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method.

```sql
UPDATE azure.iothub.iot_hub_resource
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update the metadata of an IoT hub. Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub.

```sql
REPLACE azure.iothub.iot_hub_resource
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
etag = '{{ etag }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
etag,
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

Delete an IoT hub. Delete an IoT hub.

```sql
DELETE FROM azure.iothub.iot_hub_resource
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_jobs"
    values={[
        { label: 'list_jobs', value: 'list_jobs' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get_valid_skus', value: 'get_valid_skus' },
        { label: 'get_quota_metrics', value: 'get_quota_metrics' },
        { label: 'get_stats', value: 'get_stats' },
        { label: 'create_event_hub_consumer_group', value: 'create_event_hub_consumer_group' },
        { label: 'delete_event_hub_consumer_group', value: 'delete_event_hub_consumer_group' },
        { label: 'test_all_routes', value: 'test_all_routes' },
        { label: 'test_route', value: 'test_route' },
        { label: 'export_devices', value: 'export_devices' },
        { label: 'import_devices', value: 'import_devices' }
    ]}
>
<TabItem value="list_jobs">

Get a list of all the jobs in an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_. Get a list of all the jobs in an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry `_.

```sql
EXEC azure.iothub.iot_hub_resource.list_jobs 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_keys">

Get the security metadata for an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_. Get the security metadata for an IoT hub. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security `_.

```sql
EXEC azure.iothub.iot_hub_resource.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_valid_skus">

Get the list of valid SKUs for an IoT hub. Get the list of valid SKUs for an IoT hub.

```sql
EXEC azure.iothub.iot_hub_resource.get_valid_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_quota_metrics">

Get the quota metrics for an IoT hub. Get the quota metrics for an IoT hub.

```sql
EXEC azure.iothub.iot_hub_resource.get_quota_metrics 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_stats">

Get the statistics from an IoT hub. Get the statistics from an IoT hub.

```sql
EXEC azure.iothub.iot_hub_resource.get_stats 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_event_hub_consumer_group">

Add a consumer group to an Event Hub-compatible endpoint in an IoT hub. Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.

```sql
EXEC azure.iothub.iot_hub_resource.create_event_hub_consumer_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@event_hub_endpoint_name='{{ event_hub_endpoint_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_event_hub_consumer_group">

Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub. Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.

```sql
EXEC azure.iothub.iot_hub_resource.delete_event_hub_consumer_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@event_hub_endpoint_name='{{ event_hub_endpoint_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="test_all_routes">

Test all routes. Test all routes configured in this Iot Hub.

```sql
EXEC azure.iothub.iot_hub_resource.test_all_routes 
@iot_hub_name='{{ iot_hub_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"routingSource": "{{ routingSource }}", 
"message": "{{ message }}", 
"twin": "{{ twin }}"
}'
;
```
</TabItem>
<TabItem value="test_route">

Test the new route. Test the new route for this Iot Hub.

```sql
EXEC azure.iothub.iot_hub_resource.test_route 
@iot_hub_name='{{ iot_hub_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"message": "{{ message }}", 
"route": "{{ route }}", 
"twin": "{{ twin }}"
}'
;
```
</TabItem>
<TabItem value="export_devices">

Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_. Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_.

```sql
EXEC azure.iothub.iot_hub_resource.export_devices 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"exportBlobContainerUri": "{{ exportBlobContainerUri }}", 
"excludeKeys": {{ excludeKeys }}, 
"exportBlobName": "{{ exportBlobName }}", 
"authenticationType": "{{ authenticationType }}", 
"identity": "{{ identity }}", 
"includeConfigurations": {{ includeConfigurations }}, 
"configurationsBlobName": "{{ configurationsBlobName }}"
}'
;
```
</TabItem>
<TabItem value="import_devices">

Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_. Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: `https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities `_.

```sql
EXEC azure.iothub.iot_hub_resource.import_devices 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"inputBlobContainerUri": "{{ inputBlobContainerUri }}", 
"outputBlobContainerUri": "{{ outputBlobContainerUri }}", 
"inputBlobName": "{{ inputBlobName }}", 
"outputBlobName": "{{ outputBlobName }}", 
"authenticationType": "{{ authenticationType }}", 
"identity": "{{ identity }}", 
"includeConfigurations": {{ includeConfigurations }}, 
"configurationsBlobName": "{{ configurationsBlobName }}"
}'
;
```
</TabItem>
</Tabs>
